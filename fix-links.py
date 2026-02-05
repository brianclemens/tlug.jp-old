#!/usr/bin/env python3
"""
Fix common broken link patterns in converted content.
"""

import re
from pathlib import Path

CONTENT_DIR = Path("content")


def fix_malformed_person_links(content):
    """
    Fix links like [Middleton](Edward)(/user/edward/)
    to proper format [Edward Middleton](/user/edward/)
    """
    # Pattern: [Text1](Text2)(/path/)
    pattern = r"\[([^\]]+)\]\(([^\)]+)\)\((/[^\)]+/)\)"

    def replacer(match):
        text1 = match.group(1)
        text2 = match.group(2)
        path = match.group(3)
        # Combine text2 and text1 (usually FirstName LastName)
        combined = f"{text2} {text1}"
        return f"[{combined}]({path})"

    return re.sub(pattern, replacer, content)


def fix_category_links(content):
    """
    Fix category links that are broken.
    Category links should point to taxonomies or be removed.
    """
    # Pattern: [Text](/category/...)
    # These were MediaWiki category links that don't translate well
    # We'll convert them to regular text or proper category pages

    # For now, convert to regular text in parentheses
    pattern = r"\[([^\]]+)\]\(/category/[^\)]+/\)"
    return re.sub(pattern, r"*\1*", content)


def fix_image_links(content):
    """
    Fix image links with wrong syntax.
    Pattern: [Image:filename](/image/filename/)
    Should be: ![Alt text](/images/filename)
    """
    # Pattern: [Image:filename.ext](/image/path/)
    pattern = r"\[Image:([^\]]+)\]\(/image/([^\)]+)/\)"

    def replacer(match):
        filename = match.group(1)
        path = match.group(2)
        # Convert to proper image syntax
        return f"![{filename}](/images/{path})"

    return re.sub(pattern, replacer, content)


def fix_simple_name_links(content):
    """
    Fix standalone name links like [Edward](/) or just names in links.
    These are often from MediaWiki [[Name]] syntax.
    """
    # Names that appear as broken links - convert to plain text
    common_names = [
        "Edward",
        "Jim",
        "Craig",
        "Steve",
        "Josh",
        "Alberto",
        "Andreas",
        "Simon",
        "Nori",
        "Rainer",
        "Matthew",
        "Emerson",
        "Stephen",
        "Henri",
        "Keith",
        "Alain",
        "Jonathan",
        "Godwin",
        "Scott",
        "Lewske",
        "Masafumi",
        "Sach",
        "Christian",
        "Felipe",
        "Travis",
        "Bruno",
        "Mattia",
        "Daniel",
        "Alexei",
        "Curt",
    ]

    for name in common_names:
        # Pattern: [Name](/) or [Name](/whatever/) where whatever is just the name
        content = re.sub(rf"\[{name}\]\(/{name.lower()}/?\)", name, content)
        content = re.sub(rf"\[{name}\]\(/\)", name, content)
        # Also fix cases where it's just the name as a broken link
        content = re.sub(rf"\[{name}\]\([^){{]*\)", name, content)

    return content


def fix_mediawiki_templates(content):
    """
    Remove or convert remaining MediaWiki template syntax.
    """
    # {{Template:Something}} -> *Template: Something*
    content = re.sub(r"\{\{([^}|]+)(?:\|[^}]+)?\}\}", r"*\1*", content)

    return content


def fix_tlug_internal_links(content):
    """
    Fix common TLUG internal page references.
    """
    replacements = {
        r"\[TLUG Timeline\]\(/tlug-timeline/\)": "[TLUG Timeline](/pages/tlug-timeline/)",
        r"\[Main Page\]\(/main-page/\)": "[Main Page](/pages/main-page/)",
        r"\[TLUG:Organization\]\(/tlug/organization/\)": "[Organization](/about/organization/)",
        r"\[TLUG:MemberGuide\]\(/tlug/memberguide/\)": "[Member Guide](/about/memberguide/)",
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    return content


def process_file(filepath):
    """Process a single file and apply all fixes."""
    try:
        content = filepath.read_text(encoding="utf-8")
        original = content

        # Apply all fixes
        content = fix_malformed_person_links(content)
        content = fix_category_links(content)
        content = fix_image_links(content)
        content = fix_simple_name_links(content)
        content = fix_mediawiki_templates(content)
        content = fix_tlug_internal_links(content)

        # Write back if changed
        if content != original:
            filepath.write_text(content, encoding="utf-8")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Main function to process all content files."""
    print("TLUG Link Fixer")
    print("=" * 60)

    if not CONTENT_DIR.exists():
        print(f"Error: {CONTENT_DIR} directory not found.")
        return

    # Find all markdown files
    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files to process\n")

    modified_count = 0
    for md_file in md_files:
        if process_file(md_file):
            modified_count += 1
            print(f"Fixed: {md_file.relative_to(CONTENT_DIR)}")

    print("\n" + "=" * 60)
    print(f"Modified {modified_count} files")
    print("\nNote: This fixes common patterns. Some broken links may remain.")
    print("Run 'python3 check-links.py' again to see remaining issues.")


if __name__ == "__main__":
    main()
