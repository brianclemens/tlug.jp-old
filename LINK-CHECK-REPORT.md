# Link Check Report

**Date**: February 5, 2026  
**Hugo Version**: 0.151.2  

## Summary

Automated link checking and fixing has been performed on the migrated TLUG Hugo site.

### Results

| Metric | Before Fixes | After Fixes | Improvement |
|--------|-------------|-------------|-------------|
| **Total Internal Links** | 2,010 | 1,167 | -843 (cleaned up) |
| **Broken Links** | 1,026 (51.0%) | 198 (17.0%) | **-828 fixed** |
| **Pages with Broken Links** | 337 | 68 | **-269 fixed** |

### Fixes Applied

The `fix-links.py` script automatically corrected:

1. **Malformed Person Links** (152 fixes)
   - Pattern: `[LastName](FirstName)(/user/name/)` 
   - Fixed to: `[FirstName LastName](/user/name/)`

2. **Category Links** (269 fixes)
   - Pattern: `[Text](/category/...)`
   - Fixed to: `*Text*` (converted to italic text)
   - Note: MediaWiki categories don't translate directly to Hugo

3. **Image Link Syntax** (29 fixes)
   - Pattern: `[Image:file](/image/path/)`
   - Fixed to: `![file](/images/path)`

4. **Simple Name Links** (200+ fixes)
   - Standalone names like `[Edward](/)` converted to plain text
   - Common contributor names handled

5. **MediaWiki Templates** (100+ fixes)
   - Pattern: `{{Template:Name}}`
   - Converted to: `*Name*`

## Remaining Broken Links: 198

### By Pattern

1. **User Profile Links** (109 links)
   - Pattern: `/user/username/`
   - Cause: Some users referenced don't have profile pages
   - Fix: Create stub pages or link to actual user pages

2. **Meeting Links** (27 links)
   - Pattern: `/meetings/YYYY/MM/`
   - Cause: References to meetings that don't exist
   - Fix: Verify meeting data and create missing pages

3. **Image Links** (9 links)
   - Pattern: `/image/filename/`
   - Cause: Images not migrated or wrong path
   - Fix: Update to `/images/filename` or add missing images

4. **Category Links** (9 links)
   - Remaining category references that need manual review

5. **Special Pages** (5 links)
   - MediaWiki special pages like `/special/recentchanges/`
   - These don't exist in Hugo and should be removed

6. **Other Internal Links** (39 links)
   - Various other broken references

### Top Pages with Remaining Issues

1. **pages/tlug-timeline/index.html** - 63 broken links
   - Historical references to members and events
   - Many references to `/tlug/memberguide#history/`

2. **pages/tlugwiki-wiki-topics/index.html** - 15 broken links
   - User profile references
   - Special page references

3. **pages/linux-quiz-questions/index.html** - 8 broken links
   - User profile references

## Recommendations

### High Priority

1. **Review TLUG Timeline** (`content/pages/tlug-timeline.md`)
   - Most broken links are here
   - Update historical references
   - Fix member guide links

2. **User Profiles**
   - Review which user pages exist in `content/users/`
   - Create stub pages for frequently referenced users
   - Or convert references to plain text

3. **Meeting References**
   - Verify meeting data completeness
   - Add missing meeting pages or fix references

### Medium Priority

1. **Image Paths**
   - Audit images in `static/images/`
   - Fix remaining image references
   - Ensure all referenced images exist

2. **Remove MediaWiki Artifacts**
   - Remove references to special pages
   - Clean up remaining template syntax
   - Update category references

### Low Priority

1. **Manual Review**
   - Review top 20 pages with broken links
   - Manually fix context-specific issues
   - Improve link text where needed

## Tools Used

- `check-links.py` - Automated link checker
- `fix-links.py` - Automated link fixer
- Hugo build system

## Next Steps

1. ✅ Run automated fixes (completed)
2. ⏳ Rebuild site and verify improvements
3. ⏳ Manual review of high-priority pages
4. ⏳ Create missing user profile stubs
5. ⏳ Final link check before production

## Notes

- External links are not checked by these tools
- Some "broken" links may be intentionally pointing to non-existent content
- Hugo's built-in link checking can be enabled with `--buildDrafts --buildFuture`
- Consider adding `ref` and `relref` shortcodes for more reliable internal linking

## Conclusion

**80% of broken links have been automatically fixed** (828 out of 1,026). The remaining 198 broken links are primarily:
- User profile references (55%)
- Meeting references (14%)  
- Other internal references (31%)

These can be addressed through:
1. Creating stub user pages
2. Verifying meeting data
3. Manual review of high-value content pages

The site is functional with the current link status, but addressing the remaining issues will improve the user experience.
