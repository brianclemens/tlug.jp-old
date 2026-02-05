#!/usr/bin/env python3
"""
Check for broken internal links in the Hugo generated site.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse, unquote
from collections import defaultdict

# Configuration
PUBLIC_DIR = Path("public")
BASE_URL = "https://www.tlug.jp"


def find_html_files():
    """Find all HTML files in the public directory."""
    return list(PUBLIC_DIR.rglob("*.html"))


def extract_links(html_file):
    """Extract all internal links from an HTML file."""
    try:
        content = html_file.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        return []

    links = []

    # Find href attributes
    href_pattern = r'href=["\']([^"\']+)["\']'
    for match in re.finditer(href_pattern, content):
        link = match.group(1)

        # Skip external links, anchors, and special protocols
        if link.startswith(
            ("http://", "https://", "mailto:", "tel:", "#", "javascript:")
        ):
            continue

        # Skip data URIs
        if link.startswith("data:"):
            continue

        links.append(link)

    return links


def normalize_path(link, source_file):
    """Normalize a link path to an absolute path."""
    # Remove query strings and fragments
    link = link.split("?")[0].split("#")[0]

    # Decode URL encoding
    link = unquote(link)

    if link.startswith("/"):
        # Absolute path
        path = PUBLIC_DIR / link.lstrip("/")
    else:
        # Relative path
        source_dir = source_file.parent
        path = (source_dir / link).resolve()

    return path


def check_path_exists(path):
    """Check if a path exists, trying various options."""
    # Direct file
    if path.exists():
        return True

    # Try as directory with index.html
    if path.is_dir():
        index_path = path / "index.html"
        if index_path.exists():
            return True

    # Try adding index.html
    if not str(path).endswith(".html"):
        index_path = path / "index.html"
        if index_path.exists():
            return True

    # Try adding .html extension
    if not str(path).endswith(".html"):
        html_path = Path(str(path) + ".html")
        if html_path.exists():
            return True

    # Try removing trailing slash and adding /index.html
    if str(path).endswith("/"):
        no_slash = Path(str(path).rstrip("/"))
        if no_slash.exists():
            return True
        index_path = no_slash / "index.html"
        if index_path.exists():
            return True

    return False


def main():
    """Main function to check all links."""
    print("TLUG Hugo Site Link Checker")
    print("=" * 60)

    if not PUBLIC_DIR.exists():
        print(f"Error: {PUBLIC_DIR} directory not found. Run 'hugo' first.")
        return

    html_files = find_html_files()
    print(f"Found {len(html_files)} HTML files to check\n")

    broken_links = defaultdict(list)
    total_links = 0
    broken_count = 0

    for html_file in html_files:
        rel_path = html_file.relative_to(PUBLIC_DIR)
        links = extract_links(html_file)

        for link in links:
            total_links += 1
            target_path = normalize_path(link, html_file)

            if not check_path_exists(target_path):
                broken_links[str(rel_path)].append(link)
                broken_count += 1

    print(f"Total internal links checked: {total_links}")
    print(f"Broken links found: {broken_count}")
    print("=" * 60)

    if broken_links:
        print("\nBroken Links by Page:")
        print("-" * 60)

        # Sort by number of broken links (most first)
        sorted_pages = sorted(
            broken_links.items(), key=lambda x: len(x[1]), reverse=True
        )

        # Show top 20 pages with most broken links
        for page, links in sorted_pages[:20]:
            print(f"\n{page} ({len(links)} broken links):")
            for link in links[:5]:  # Show first 5 broken links per page
                print(f"  - {link}")
            if len(links) > 5:
                print(f"  ... and {len(links) - 5} more")

        if len(sorted_pages) > 20:
            print(f"\n... and {len(sorted_pages) - 20} more pages with broken links")

        # Summary of most common broken link patterns
        print("\n" + "=" * 60)
        print("Most Common Broken Link Patterns:")
        print("-" * 60)

        all_broken = []
        for links in broken_links.values():
            all_broken.extend(links)

        # Count patterns
        pattern_count = defaultdict(int)
        for link in all_broken:
            # Extract pattern (first part of path)
            parts = link.strip("/").split("/")
            if parts:
                pattern = "/" + parts[0]
                pattern_count[pattern] += 1

        # Show top 10 patterns
        top_patterns = sorted(pattern_count.items(), key=lambda x: x[1], reverse=True)[
            :10
        ]
        for pattern, count in top_patterns:
            print(f"  {pattern}/* : {count} broken links")
    else:
        print("\n✓ No broken internal links found!")

    print("\n" + "=" * 60)
    print("\nNote: This checker only validates internal links.")
    print("External links are not checked.")
    print("\nTo fix broken links:")
    print("1. Review the conversion in content/ directory")
    print("2. Update MediaWiki link syntax")
    print("3. Check front matter aliases for redirects")


if __name__ == "__main__":
    main()
