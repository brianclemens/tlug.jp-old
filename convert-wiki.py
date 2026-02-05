#!/usr/bin/env python3
"""
MediaWiki to Hugo Markdown Converter for TLUG

This script converts MediaWiki format files from the wiki/ directory
to Hugo-compatible Markdown in the content/ directory.
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import yaml

# Configuration
WIKI_DIR = Path("wiki")
CONTENT_DIR = Path("content")
MEETINGS_DIR = CONTENT_DIR / "meetings"
HELP_DIR = CONTENT_DIR / "help"
ABOUT_DIR = CONTENT_DIR / "about"
USERS_DIR = CONTENT_DIR / "users"
OTHER_DIR = CONTENT_DIR / "pages"

# Create output directories
for dir in [MEETINGS_DIR, HELP_DIR, ABOUT_DIR, USERS_DIR, OTHER_DIR]:
    dir.mkdir(parents=True, exist_ok=True)


def extract_categories(content):
    """Extract MediaWiki categories from content."""
    categories = []
    # Pattern: {{Category:MeetingsName}}
    category_patterns = [r"\{\{Category:([^}]+)\}\}", r"\[\[Category:([^\]]+)\]\]"]
    for pattern in category_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        categories.extend([cat.strip() for cat in matches])
    return list(set(categories))


def extract_redirect(content):
    """Extract redirect target if this is a redirect page."""
    match = re.match(
        r"^\s*#REDIRECT\s*\[\[([^\]]+)\]\]", content, re.IGNORECASE | re.MULTILINE
    )
    if match:
        target = match.group(1).strip()
        # Clean up the target
        target = target.replace("_", "-").lower()
        return target
    return None


def is_meeting_page(filename):
    """Determine if a file is a meeting page."""
    meeting_patterns = [
        r"^Meetings?:(\d{4}):(\d{2})$",
        r"^Meetings?:.*(\d{4}).*(\d{2})",
    ]
    for pattern in meeting_patterns:
        if re.match(pattern, filename):
            return True
    return False


def extract_meeting_info(filename, content):
    """Extract meeting metadata from filename and content."""
    # Try to extract year and month
    match = re.search(r"(\d{4})[:\-_/](\d{1,2})", filename)
    if not match:
        return None

    year = match.group(1)
    month = match.group(2).zfill(2)

    # Try to determine meeting type
    meeting_type = "technical"
    if "nomikai" in filename.lower() or "nomikai" in content.lower()[:500]:
        meeting_type = "nomikai"

    # Try to extract location
    location = ""
    location_match = re.search(r"\*\*Location:\*\*\s*([^\n]+)", content)
    if not location_match:
        location_match = re.search(r"Location[:\s]+([^\n]+)", content)
    if location_match:
        location = location_match.group(1).strip()

    return {
        "year": year,
        "month": month,
        "meeting_type": meeting_type,
        "location": location,
        "date": f"{year}-{month}-01",  # Default to first of month
    }


def convert_mediawiki_to_markdown(content):
    """Convert MediaWiki syntax to Markdown using pandoc."""
    try:
        # Use pandoc for conversion
        result = subprocess.run(
            ["pandoc", "-f", "mediawiki", "-t", "markdown"],
            input=content,
            capture_output=True,
            text=True,
            check=True,
        )
        markdown = result.stdout

        # Post-process the markdown
        # Fix wiki links [[Page]] -> [Page](/page/)
        markdown = re.sub(
            r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
            lambda m: f"[{m.group(2) or m.group(1)}](/{m.group(1).replace(':', '/').replace('_', '-').lower()}/)",
            markdown,
        )

        # Remove category tags
        markdown = re.sub(r"\{\{Category:[^}]+\}\}", "", markdown, flags=re.IGNORECASE)

        # Convert MediaWiki templates to something more readable
        # {{Template:Name|param}} -> [Template: Name]
        markdown = re.sub(r"\{\{([^}|]+)(?:\|[^}]+)?\}\}", r"*[\1]*", markdown)

        return markdown.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error converting with pandoc: {e}")
        print(f"stderr: {e.stderr}")
        return content
    except FileNotFoundError:
        print("Warning: pandoc not found, using basic conversion")
        return basic_mediawiki_conversion(content)


def basic_mediawiki_conversion(content):
    """Basic MediaWiki to Markdown conversion without pandoc."""
    # Remove redirects
    content = re.sub(r"#REDIRECT\s*\[\[[^\]]+\]\]", "", content, flags=re.IGNORECASE)

    # Convert headings
    content = re.sub(
        r"^======\s*(.+?)\s*======", r"###### \1", content, flags=re.MULTILINE
    )
    content = re.sub(
        r"^=====\s*(.+?)\s*=====", r"##### \1", content, flags=re.MULTILINE
    )
    content = re.sub(r"^====\s*(.+?)\s*====", r"#### \1", content, flags=re.MULTILINE)
    content = re.sub(r"^===\s*(.+?)\s*===", r"### \1", content, flags=re.MULTILINE)
    content = re.sub(r"^==\s*(.+?)\s*==", r"## \1", content, flags=re.MULTILINE)

    # Convert bold and italic
    content = re.sub(r"'''(.+?)'''", r"**\1**", content)
    content = re.sub(r"''(.+?)''", r"*\1*", content)

    # Convert lists
    content = re.sub(r"^\*\s+", "- ", content, flags=re.MULTILINE)
    content = re.sub(r"^#+\s+", "1. ", content, flags=re.MULTILINE)

    # Convert links
    content = re.sub(
        r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
        lambda m: f"[{m.group(2) or m.group(1)}](/{m.group(1).replace(':', '/').replace('_', '-').lower()}/)",
        content,
    )

    # External links
    content = re.sub(r"\[([^\s\]]+)\s+([^\]]+)\]", r"[\2](\1)", content)

    return content.strip()


def create_front_matter(filename, content, metadata):
    """Create Hugo front matter for the content."""
    title = filename.replace("_", " ").replace(":", " - ")

    front_matter = {
        "title": title,
        "date": metadata.get("date", datetime.now().strftime("%Y-%m-%d")),
        "draft": False,
    }

    # Add categories
    categories = extract_categories(content)
    if categories:
        front_matter["categories"] = categories

    # Handle redirects
    redirect_target = extract_redirect(content)
    if redirect_target:
        front_matter["aliases"] = [f"/{redirect_target}/"]
        front_matter["redirect"] = redirect_target

    # Add meeting-specific metadata
    if metadata.get("is_meeting"):
        front_matter["type"] = "meeting"
        front_matter["meeting_type"] = metadata.get("meeting_type", "technical")
        if metadata.get("location"):
            front_matter["location"] = metadata["location"]
        front_matter["years"] = [metadata["year"]]
        front_matter["meeting-types"] = [metadata["meeting_type"]]

    return front_matter


def determine_output_path(filename, metadata):
    """Determine the output path for a converted file."""
    # Meetings
    if metadata.get("is_meeting") and metadata.get("year") and metadata.get("month"):
        year = metadata["year"]
        month = metadata["month"]
        year_dir = MEETINGS_DIR / year
        year_dir.mkdir(exist_ok=True)
        return year_dir / f"{month}.md"

    # Help pages
    if filename.startswith("Linux_Help"):
        slug = (
            filename.replace("Linux_Help:", "")
            .replace(":", "-")
            .replace("_", "-")
            .lower()
        )
        return HELP_DIR / f"{slug}.md"

    # User pages
    if filename.startswith("User:"):
        slug = filename.replace("User:", "").replace("_", "-").lower()
        return USERS_DIR / f"{slug}.md"

    # TLUG org pages
    if filename.startswith("TLUG:"):
        slug = filename.replace("TLUG:", "").replace("_", "-").lower()
        return ABOUT_DIR / f"{slug}.md"

    # Everything else
    slug = filename.replace(":", "-").replace("_", "-").lower()
    return OTHER_DIR / f"{slug}.md"


def convert_file(wiki_file):
    """Convert a single wiki file to Hugo markdown."""
    filename = wiki_file.stem

    # Read the wiki content
    try:
        content = wiki_file.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"Error reading {wiki_file}: {e}")
        return False

    # Skip empty files
    if not content.strip():
        print(f"Skipping empty file: {filename}")
        return False

    # Check if it's a meeting page
    metadata = {"is_meeting": False}
    if is_meeting_page(filename):
        meeting_info = extract_meeting_info(filename, content)
        if meeting_info:
            metadata.update(meeting_info)
            metadata["is_meeting"] = True

    # Convert content
    markdown = convert_mediawiki_to_markdown(content)

    # Create front matter
    front_matter = create_front_matter(filename, content, metadata)

    # Determine output path
    output_path = determine_output_path(filename, metadata)

    # Write the output file
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(front_matter, f, default_flow_style=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(markdown)
        print(f"Converted: {filename} -> {output_path}")
        return True
    except Exception as e:
        print(f"Error writing {output_path}: {e}")
        return False


def main():
    """Main conversion function."""
    print("TLUG MediaWiki to Hugo Converter")
    print("=" * 50)

    # Check if pandoc is available
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        print("✓ Pandoc found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ Pandoc not found - using basic conversion")

    # Get all wiki files
    wiki_files = list(WIKI_DIR.glob("*"))
    wiki_files = [f for f in wiki_files if f.is_file() and not f.name.startswith(".")]

    print(f"\nFound {len(wiki_files)} wiki files to convert")
    print("-" * 50)

    # Convert each file
    success_count = 0
    for wiki_file in sorted(wiki_files):
        if convert_file(wiki_file):
            success_count += 1

    print("-" * 50)
    print(f"\nConversion complete!")
    print(f"Successfully converted: {success_count}/{len(wiki_files)} files")
    print(f"\nOutput directories:")
    print(f"  Meetings: {MEETINGS_DIR}")
    print(f"  Help: {HELP_DIR}")
    print(f"  About: {ABOUT_DIR}")
    print(f"  Users: {USERS_DIR}")
    print(f"  Other: {OTHER_DIR}")


if __name__ == "__main__":
    main()
