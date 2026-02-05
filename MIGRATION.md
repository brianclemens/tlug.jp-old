# Hugo Migration Guide

This document describes the migration from Hakyll to Hugo for the TLUG website.

## Summary

The TLUG website has been successfully migrated from Hakyll (Haskell-based) to Hugo (Go-based) static site generator.

### Migration Results

- **Content Converted**: 563/567 wiki files (99.3% success rate)
- **Total Pages**: 1,152 pages generated
- **Build Time**: ~350ms (previously 30+ minutes cold build)
- **Size**: 23MB generated site

## What Changed

### Technology Stack

**Before (Hakyll):**
- Haskell Stack + GHC compiler
- Custom MediaWiki parser in Haskell
- Pandoc for some conversions
- Complex build caching requirements
- 30+ minute CI builds (cold)

**After (Hugo):**
- Single Hugo binary
- Standard Markdown
- Built-in template system
- No external dependencies
- Sub-second builds

### Content Organization

Content has been reorganized into a cleaner structure:

```
content/
├── meetings/       # Organized by year (1994-2025)
│   ├── 1994/
│   ├── 1995/
│   └── ...
├── help/          # Linux guides and tips
├── about/         # TLUG organization info
├── users/         # Member profiles
└── pages/         # Other content
```

### URL Structure

URLs have been modernized (no redirects as per project requirements):

**Old URLs:**
- `/wiki/Meetings:2025:02`
- `/wiki/Linux_Help:QND-Guides:SSH_Keypair_Authentication`
- `/wiki/TLUG:Organization`

**New URLs:**
- `/meetings/2025/02/`
- `/help/qnd-guides-ssh-keypair-authentication/`
- `/about/organization/`

### Build Process

**Old Process:**
```bash
# Required Stack, GHC, Hakyll, and custom MediaWiki parser
./Test  # Could take 30+ minutes on first build
```

**New Process:**
```bash
# Just Hugo
hugo    # Takes ~350ms
```

## Conversion Process

The migration used a Python script (`convert-wiki.py`) that:

1. **Extracted metadata** from MediaWiki files
   - Categories → Hugo taxonomies
   - Redirects → Hugo aliases
   - Meeting info → Structured front matter

2. **Converted syntax**
   - MediaWiki markup → Markdown
   - Wiki links → Hugo links
   - MediaWiki templates → Hugo shortcodes (where applicable)

3. **Organized content**
   - Meeting pages → `content/meetings/YEAR/MONTH.md`
   - Help pages → `content/help/`
   - User pages → `content/users/`
   - Other pages → Appropriate sections

## Known Limitations

1. **MediaWiki Template Syntax**: Some complex MediaWiki template syntax (like `{{Meetings:Locations:Shibuya:Axsh}}`) was not fully converted and appears as-is in the content. These can be manually updated or converted to Hugo shortcodes.

2. **URL Changes**: Old URLs no longer work. As per project requirements, no automatic redirects were implemented.

3. **Manual Cleanup Needed**: Some pages may need manual review for:
   - Broken internal links
   - Unconverted template syntax
   - Formatting issues
   - Metadata accuracy

## Features Gained

### Hugo Built-in Features

1. **Fast Builds**: Hugo is known for its speed
2. **Live Reload**: Automatic browser refresh during development
3. **Image Processing**: Built-in image optimization
4. **Taxonomies**: Native support for categories, tags, etc.
5. **Multilingual**: First-class i18n support
6. **Search**: JSON index generation for client-side search
7. **RSS Feeds**: Automatic feed generation
8. **Sitemap**: Automatic sitemap generation

### Theme Benefits (PaperMod)

1. **Modern Design**: Clean, responsive layout
2. **Dark Mode**: Built-in dark mode support
3. **Mobile Friendly**: Optimized for mobile devices
4. **SEO Optimized**: Meta tags and structured data
5. **Fast Loading**: Minimized CSS/JS
6. **Accessibility**: WCAG compliant

## Content Migration Details

### Meetings (239 files)

Meetings are the core content type, organized by year and month:
- Format: `/meetings/YYYY/MM.md`
- Front matter includes: date, type, location, venue
- Taxonomies: year, meeting-type

### Help Content (19 files)

Linux guides and tips:
- QND Guides (Quick and Dirty guides)
- Tips of the Day
- How-to articles

### About Pages (4 files)

Organizational information:
- Member Guide
- Organization structure
- History and timeline

### User Pages (41 files)

Member profile pages with contributions and information.

### Other Pages (260 files)

Miscellaneous content including:
- Templates and archive pages
- Project pages
- Historical content

## Testing Checklist

Before deploying to production, verify:

- [ ] Home page loads correctly
- [ ] Meeting pages display properly
- [ ] Navigation works
- [ ] Internal links function
- [ ] Images display
- [ ] Search works (if enabled)
- [ ] RSS feeds generate
- [ ] Mobile responsive
- [ ] Dark mode toggles
- [ ] Multiple browsers (Chrome, Firefox, Safari)

## Deployment Notes

### GitHub Actions

The `.github/workflows/hugo.yaml` file configures:
- Build on push to `hugo` or `main` branch
- Hugo extended version
- Automatic deployment to `gh-pages`

### GitHub Pages

The site deploys via GitHub Actions to GitHub Pages:
- Workflow: `.github/workflows/hugo.yaml`
- Hugo version: latest extended
- Build command: `hugo --minify --verbose`
- Deploy branch: `gh-pages`
- Custom domain: `www.tlug.jp`

## Rollback Plan

If issues arise, rollback is simple:

1. The `master` branch still contains the Hakyll version
2. Simply merge `master` to `gh-pages` to revert
3. Update deployment configuration if needed

## Performance Comparison

| Metric | Hakyll | Hugo | Improvement |
|--------|--------|------|-------------|
| Build Time (cold) | 30+ min | 350ms | 5100x faster |
| Build Time (warm) | 5-10s | 350ms | 14-28x faster |
| Dependencies | Stack, GHC, Hakyll | Hugo binary | Much simpler |
| Developer Setup | 20+ min | 1 min | 20x faster |
| CI Build Time | 30-60 min | <1 min | 30-60x faster |

## Next Steps

### Immediate

1. **Review converted content** - Check for formatting issues
2. **Update broken links** - Fix any broken internal references
3. **Test thoroughly** - Verify all functionality works
4. **Deploy to staging** - Test via GitHub Pages deployment

### Short Term

1. **Content cleanup** - Manual review of high-priority pages
2. **Custom shortcodes** - Convert remaining MediaWiki templates
3. **Documentation** - Update any outdated documentation
4. **SEO** - Verify meta tags and structured data

### Long Term

1. **Search implementation** - Add client-side search (Lunr.js/Pagefind)
2. **Progressive enhancement** - Add optional JavaScript features
3. **Performance optimization** - Image optimization, lazy loading
4. **Archive old content** - Move historical content to archive section

## Support

For questions or issues:
- TLUG Mailing List: <https://lists.tlug.jp/>
- Matrix Room: <https://matrix.to/#/#tlug.jp:matrix.org>
- GitHub Issues: <https://github.com/brianclemens/tlug.jp-old/issues>

## Credits

Migration performed by: OpenCode + Brian Clemens
Date: February 2026
Hugo Version: 0.151.2
Theme: PaperMod
