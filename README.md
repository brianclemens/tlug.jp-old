# tlug.jp: Tokyo Linux Users Group Website

This is the Hugo-based version of <https://tlug.jp>, the Tokyo Linux Users Group website. It's a fully static site generated using [Hugo] and deployed via GitHub Pages.

The current developers/maintainers are:
- Curt Sampson ([`@0cjs`]) <cjs@cynic.net>
- Jim Tittsler ([`@jimt`]) <jimt@onjapan.net>
- [`@sssjjjnnn`]

## Quick Start

### Prerequisites

- [Hugo](https://gohugo.io/installation/) (Extended version recommended)
- Git

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/brianclemens/tlug.jp-old.git
   cd tlug.jp-old
   git checkout hugo
   ```

2. Run the local development server:
   ```bash
   hugo server -D
   ```

3. Open your browser to `http://localhost:1313`

The site will automatically rebuild and refresh as you make changes.

### Building the Site

To build the production site:

```bash
hugo --minify
```

The generated site will be in the `public/` directory.

## Site Organization

### Directory Structure

- `content/` - All site content in Markdown format
  - `meetings/` - Historical meeting data organized by year
  - `help/` - Linux help guides and tips
  - `about/` - Organization information
  - `users/` - User profile pages
  - `pages/` - Other miscellaneous content
- `layouts/` - Hugo templates and layouts
  - `meetings/` - Custom templates for meeting pages
  - `shortcodes/` - Reusable content snippets
  - `partials/` - Template partials
- `static/` - Static assets (images, CSS, downloads)
- `themes/PaperMod/` - Hugo PaperMod theme
- `hugo.toml` - Site configuration

### Content Types

The site has several content types with different templates:

1. **Meetings** - Monthly technical meetings and nomikai events
2. **Help** - Guides, tutorials, and tips
3. **About** - Organizational information
4. **Users** - Member profile pages

## Creating Content

### Adding a New Meeting

Use the meeting archetype:

```bash
hugo new meetings/2025/03.md
```

This creates a new meeting page with the proper front matter template. Edit the file to add meeting details.

### Adding a Help Guide

```bash
hugo new help/my-new-guide.md
```

### Front Matter

All content files use YAML front matter. Example for a meeting:

```yaml
---
title: "Technical Meeting - March 2025"
date: 2025-03-08
type: meeting
meeting_type: technical
location: "Shibuya"
venue: "Amazon Office"
categories: [meetings, technical]
years: ["2025"]
meeting-types: ["technical"]
---
```

## Multilingual Support

The site supports both English and Japanese content:

- Create English content: `content/about/_index.en.md`
- Create Japanese content: `content/about/_index.ja.md`

Hugo will automatically handle language switching.

## Deployment

### Automatic Deployment (GitHub Actions)

The site automatically deploys to GitHub Pages when you push to the `hugo` or `main` branch:

1. GitHub Actions builds the site using Hugo
2. The built site is pushed to the `gh-pages` branch
3. GitHub Pages serves the content from `gh-pages`

### Manual Deployment

If you need to deploy manually:

```bash
# Build the site
hugo --minify

# The public/ directory now contains the built site
# Deploy this to your hosting provider
```

## GitHub Pages Configuration

The site is deployed to GitHub Pages via GitHub Actions:
- Workflow: `.github/workflows/hugo.yaml`
- Build command: `hugo --minify --verbose`
- Publish directory: `public`
- Deploy branch: `gh-pages`
- Custom domain: `www.tlug.jp` (configured via CNAME)

## Migration from Hakyll

This site was migrated from a Hakyll-based system. The `convert-wiki.py` script was used to convert ~560 MediaWiki format pages to Hugo-compatible Markdown.

Key improvements in the Hugo version:
- **Faster builds**: Seconds instead of 30+ minutes
- **Simpler toolchain**: No Haskell Stack, GHC, or custom parsers
- **Lower barrier to entry**: Standard Markdown and simple configuration
- **Better themes**: Modern, responsive design with PaperMod

## Contributing

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b my-new-feature`
3. Make your changes
4. Test locally: `hugo server -D`
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin my-new-feature`
7. Submit a pull request

### Content Guidelines

- Use clear, descriptive titles
- Include proper front matter
- Test your changes locally before submitting
- Follow the existing content structure

### Code Style

- Use 2 spaces for indentation in templates
- Keep line length under 100 characters when possible
- Comment complex template logic

## Documentation

Additional documentation is available in the `doc/` directory:

- `doc/ORGANIZATION.md` - Site organization and history
- `doc/hosting.md` - Hosting configuration
- `doc/proposals.md` - Historical proposals and design decisions

## Discussion Forums

* [TLUG Matrix room](https://matrix.to/#/#tlug.jp:matrix.org) - Web or desktop/mobile app
* [TLUG mailing list](https://lists.tlug.jp/) - [Archives](https://lists.tlug.jp/ML/index.html)

## License

Content is licensed under CC-BY-4.0. See [LICENSE.md](LICENSE.md) for details.

---

[Hugo]: https://gohugo.io/
[`@0cjs`]: https://github.com/0cjs
[`@jimt`]: https://github.com/jimt
[`@sssjjjnnn`]: https://github.com/sssjjjnnn
