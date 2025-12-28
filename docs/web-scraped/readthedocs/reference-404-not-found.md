# Source: https://docs.readthedocs.com/platform/latest/reference/404-not-found.html

# [`404`]` `[`Not`]` `[`Found`] pages[](#not-found-pages "Link to this heading")

If you want your project to use a custom or branded [`404`]` `[`Not`]` `[`Found`] page, you can put a [`404.html`] or [`404/index.html`] at the top level of your project's HTML output.

## How it works[](#how-it-works "Link to this heading")

When our servers return a [`404`]` `[`Not`]` `[`Found`] error, we check if there is a [`404.html`] or [`404/index.html`] in the root of your project's output.

The following locations are checked, in order:

-   [`/404.html`] or [`404/index.html`] in the *current* documentation version.

-   [`/404.html`] or [`404/index.html`] in the *default* documentation version.