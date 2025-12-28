# Source: https://docs.readthedocs.com/platform/latest/reference/sitemaps.html

# Sitemap support[](#sitemap-support "Link to this heading")

[Sitemaps](https://www.sitemaps.org/) allow you to inform search engines about URLs that are available for crawling. This makes your content more [[discoverable]](../glossary.html#term-discoverability), and improves your [[Search Engine Optimization (SEO)]](../guides/technical-docs-seo-guide.html).

## How it works[](#how-it-works "Link to this heading")

The [`sitemap.xml`] file is read by search engines to index your documentation. It contains information such as:

-   When a URL was last updated.

-   How often that URL changes.

-   How important this URL is in relation to other URLs on the site.

-   What translations are available for a page.

Read the Docs automatically generates a [`sitemap.xml`] for your project. The sitemap includes [[public and not hidden versions]](../versions.html#version-states) of your documentation and when they were last updated, sorted by version number.

This allows search engines to prioritize results based on the version number, sorted by [semantic versioning](https://semver.org/).