# nexdose-website

Static website for [Nexdose](https://www.nexdose.app/), a private injection tracker for iPhone. Hosted on GitHub Pages. Plain HTML and CSS, with no build step.

- `index.html` is the home page. Each other page lives in its own folder (`plus/`, `how-to/`, `support/`, `privacy-policy/`, `about/`, `injection-safety/`).
- `assets/style.css` is shared by every page, and `assets/logo.svg` is the logo.
- `sitemap.xml` and `robots.txt` are for search engines.

## Editing

Pages are generated from the templates in `tools/`. Edit the matching `tools/*.py` file, then run `sh tools/build.sh` and commit both the template and the generated HTML.
