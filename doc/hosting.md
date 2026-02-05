Hosting for this Website
========================

> For information on how to release a new version of the website, see the
> ["Deployment"][deployment] section of the `README` file at the
> top level of this repo.

Current Status
--------------

The site is now deployed via GitHub Pages at <https://www.tlug.jp>.

The Hugo-based site is built automatically via GitHub Actions when changes
are pushed to the `hugo` or `main` branch, and deployed to the `gh-pages`
branch which GitHub Pages serves.


Contacting Site Administrators
------------------------------

Send a message to the [TLUG mailing list] or try the [TLUG Matrix room].


Release Branch
--------------

The compiled website is committed to the `gh-pages` branch. This is handled
automatically by GitHub Actions.

The procedure for building and deploying is:
1. Make changes to content in the `hugo` or `main` branch
2. Commit and push changes
3. GitHub Actions automatically:
   - Checks out the code with submodules
   - Builds the site with Hugo
   - Deploys to `gh-pages` branch
4. GitHub Pages serves the content


GitHub Pages Configuration
--------------------------

The site is hosted on GitHub Pages with a custom domain:

- **Repository**: `brianclemens/tlug.jp-old` (or upstream `tlug/tlug.jp`)
- **Source Branch**: `gh-pages`
- **Custom Domain**: `www.tlug.jp`
- **CNAME**: Automatically created by GitHub Actions workflow

### GitHub Actions Workflow

The `.github/workflows/hugo.yaml` file configures:
- **Trigger**: Push to `hugo` or `main` branch
- **Build**: Hugo latest extended version
- **Command**: `hugo --minify --verbose`
- **Deploy**: Uses `peaceiris/actions-gh-pages@v3`
- **Permissions**: `contents: write` for gh-pages deployment

### Setting up GitHub Pages

To enable GitHub Pages for this repository:

1. Go to repository Settings
2. Navigate to Pages section (left sidebar)
3. Under "Build and deployment":
   - Source: Deploy from a branch
   - Branch: `gh-pages` / `/ (root)`
4. Under "Custom domain":
   - Enter: `www.tlug.jp`
   - Enable "Enforce HTTPS"

### DNS Configuration

For the custom domain to work, DNS records must be configured:

**For `www.tlug.jp`:**
```
CNAME www -> brianclemens.github.io (or tlug.github.io for upstream)
```

**For apex domain `tlug.jp` (optional redirect):**
```
A @ -> 185.199.108.153
A @ -> 185.199.109.153
A @ -> 185.199.110.153
A @ -> 185.199.111.153
```

These are GitHub Pages IP addresses. Configure apex domain to redirect to www
is recommended for better performance and SEO.


Build Process
-------------

### Local Build

```bash
# Install Hugo extended
# See https://gohugo.io/installation/

# Clone repository
git clone https://github.com/brianclemens/tlug.jp-old.git
cd tlug.jp-old
git checkout hugo

# Initialize submodules (theme)
git submodule update --init --recursive

# Build site
hugo --minify

# Output in public/ directory
```

### Development Server

```bash
hugo server -D
# Visit http://localhost:1313
```

### CI/CD Pipeline

GitHub Actions handles all builds automatically:

1. **Trigger**: Any push to `hugo` or `main` branch
2. **Environment**: Ubuntu latest
3. **Hugo Version**: Latest extended (auto-updated)
4. **Build Time**: ~1-2 seconds for full site (1000+ pages)
5. **Deploy**: Automatic push to `gh-pages`


Deployment Workflow
-------------------

### For Content Updates

1. Edit content files in `content/` directory
2. Commit changes: `git commit -am "Update content"`
3. Push to hugo branch: `git push origin hugo`
4. GitHub Actions automatically builds and deploys
5. Site live in ~1-2 minutes

### For Site Configuration

1. Edit `hugo.toml` or layout files
2. Test locally: `hugo server -D`
3. Commit and push changes
4. GitHub Actions rebuilds and deploys

### For Theme Updates

```bash
# Update theme submodule
cd themes/PaperMod
git pull origin master
cd ../..
git add themes/PaperMod
git commit -m "Update PaperMod theme"
git push origin hugo
```


Rollback Procedure
------------------

If a deployment has issues:

### Option 1: Revert Commit
```bash
git revert <commit-hash>
git push origin hugo
# GitHub Actions will deploy the reverted version
```

### Option 2: Reset gh-pages
```bash
git checkout gh-pages
git reset --hard <previous-commit>
git push --force origin gh-pages
# WARNING: Only do this if you understand the implications
```

### Option 3: Redeploy Previous Version
```bash
git checkout <previous-good-commit>
git push origin hugo
# This creates a new deployment
```


Monitoring and Maintenance
--------------------------

### Check Build Status

- View GitHub Actions: https://github.com/brianclemens/tlug.jp-old/actions
- Check for failed builds or warnings
- Review build logs for errors

### Site Health

- Monitor site uptime: https://www.tlug.jp
- Check GitHub Pages status: https://www.githubstatus.com
- Review broken links: Run `python3 check-links.py` locally

### Performance

- Build times should be under 5 seconds
- Page load times should be under 2 seconds
- Use browser dev tools to check performance


Troubleshooting
---------------

### Build Fails

1. Check GitHub Actions logs for errors
2. Test build locally: `hugo --minify --verbose`
3. Verify hugo.toml syntax
4. Check for broken submodule references

### Site Not Updating

1. Verify push was successful: `git log origin/hugo`
2. Check GitHub Actions completed successfully
3. Clear browser cache
4. Wait 1-2 minutes for GitHub Pages to refresh

### Custom Domain Issues

1. Verify CNAME file exists in gh-pages branch
2. Check DNS propagation: `dig www.tlug.jp`
3. Verify GitHub Pages settings show custom domain
4. Check SSL certificate is active


Historical Notes
----------------

### Previous Hosting

The site was previously:
1. Hosted on `akari.tlug.jp` (2006-2024) with MediaWiki
2. Migrated to Netlify briefly during Hugo transition
3. Now deployed via GitHub Pages (2025+)

### Migration Path

1. Hakyll-based site (master branch) - Legacy
2. Hugo migration (hugo branch) - Current
3. GitHub Pages deployment - Current hosting


Resources
---------

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Hugo Documentation](https://gohugo.io/documentation/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod)



<!-------------------------------------------------------------------->
[TLUG Matrix room]: https://matrix.to/#/#tlug.jp:matrix.org
[TLUG mailing list]: https://lists.tlug.jp/
[deployment]: ../README.md#deployment
