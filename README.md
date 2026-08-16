# projectportfolio

Static portfolio website for GitHub Pages.

## Adding a Media Publication

1. Add a record to `R` in `scripts/build_media.py`. Keep attribution explicit: `BY_ME`, `PERSONAL_MENTION`, `SPEAKING`, `PROJECT_IN_MEDIA`, `PRODUCT_REFERENCE`, `COMPANY_REFERENCE`, or `MEDIA_ARCHIVE`.
2. Verify the canonical external URL, source title and date. Use `verified` only for confirmed sources; otherwise use `needs_recheck` and `published=False`.
3. Use an owned project image from `projects-media/`, an official product image with clear rights, or a neutral local cover. Never fabricate a publication screenshot.
4. Run `python scripts/build_media.py` from the repository root. This rebuilds `data/media.json`, `/media/` and all `/media/<slug>/` detail pages.
5. Serve the repository over HTTP and test the index, filters, detail pages, source CTA, mobile layout, metadata and existing routes before publishing.

`data/media.json` is the generated structured registry. Do not hand-edit it without updating the generator source as well.
