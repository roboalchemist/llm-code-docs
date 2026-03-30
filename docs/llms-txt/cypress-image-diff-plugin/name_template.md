# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/name_template.md

# NAME\_TEMPLATE

The snapshot naming pattern using replaceable labels. All possible labels are:&#x20;

* specName: The spec file name
* givenName: The name value in `cy.compareSnapshot`
* browserName: Short browser name currently running the tests
* width: Width in pixels for the application under tests' viewport
* height: Height in pixels for the application under tests' viewport

Any label in square brackets is replaced with its actual value during runtime.

💢 Default value:  `undefined`

```
// cypress-image-diff.config.js
const config = {
  NAME_TEMPLATE: '[browserName]/[specName]-[givenName]'
};

module.exports = config;

// home-page.cy.js
cy.compareSnapshot('top-banner')
```

Computed name that is passed to `cy.screenshot`:&#x20;

<pre><code>// presumably the browserName is chrome
<strong>chrome/home-page.cy-top-banner
</strong></code></pre>

Output directory:

```
.
├── baseline
    ├── chrome
        ├── home-page.cy-top-banner.png
├── comparison
    ├── chrome
        ├── home-page.cy-top-banner.png
├── diff
    ├── chrome
        ├── home-page.cy-top-banner.png
```
