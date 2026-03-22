# Source: https://cypress.visual-image-diff.dev/migrate-from-v1-to-v2.md

# Migrate from v1 to v2

In a mission to provide a robust and easy-to-use visual regression tool for front-end development, **Cypress Image Diff** version 2 introduces [**Cypress Image Diff HTML Report**](https://github.com/kien-ht/cypress-image-diff-html-report) as a separate npm package with extensive features and provides a new compareSnapshot arguments type.

## [New HTML Report](https://github.com/kien-ht/cypress-image-diff-html-report)

<figure><img src="https://2460381240-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZyBQte7cOp75X6TWkWrZ%2Fuploads%2Fb5k1ULDJIuP0KifbVpmF%2FScreenshot%202023-11-24%20at%2000.56.13.png?alt=media&#x26;token=062cf9ed-a44d-43a2-9b04-0e60125f87da" alt=""><figcaption></figcaption></figure>

We've separated out the core plugin and the HTML report (under the name of **Cypress Image Diff HTML Report**) with the aim of providing a beautiful interactive HTML report with a JSON file with all the details about your test suites, together with extensive features:

* Update baseline screenshots
* Toggle between different screenshot inspector modes: carousel, slider, and mirror
* Select your preferred colour scheme

Although **Cypress Image Diff HTML Report** is a standalone npm package, the [integration](https://cypress.visual-image-diff.dev/getting-started/cypress-integration) with the core Cypress Image Diff is seamless, and they are expected to work together out of the box without any further configuration.

*Note: The old report still continues to function in **Cypress Image Diff** version 2, but it is planned to be deprecated once the **Cypress Image Diff HTML Report** reaches its stable state.*

***

## New compareSnapshot arguments type

* compareSnapshot now could accept new arguments:  cypressScreenshotOptions and exactName
* New global config option: CYPRESS\_SCREENSHOT\_OPTIONS

<pre class="language-javascript"><code class="lang-javascript">// cypress-image-diff v1.32.0 and older
cy.compareSnapshot('header')
cy.compareSnapshot('header', 0.2)
cy.compareSnapshot('header', 0.2, { limit: 6, delay: 1000 })

// cypress-image-diff v2.0.0 and newer
cy.compareSnapshot('header')
cy.compareSnapshot({
  name: 'header',
  testThreshold: 0.2
})
cy.compareSnapshot({
  name: 'header',
  testThreshold: 0.2,
  recurseOptions: { limit: 6, delay: 1000 }
})
cy.compareSnapshot({
  name: 'header',
  testThreshold: 0.2,
  recurseOptions: { limit: 6, delay: 1000 },
  // new custom cypress screenshot options
<strong>  cypressScreenshotOptions: {
</strong>    clip: { x: 0, y: 0, width: 100, height: 100 }
  }
  // new exactName option
  exactName: true
})
</code></pre>

***

## Rename import path

<pre class="language-javascript"><code class="lang-javascript"><strong>🚫 import getCompareSnapshotsPlugin from 'cypress-image-diff-js/dist/plugin';
</strong>✅ import getCompareSnapshotsPlugin from 'cypress-image-diff-js/plugin';

<strong>🚫 import compareSnapshotCommand from 'cypress-image-diff-js/dist/command';
</strong>✅ import compareSnapshotCommand from 'cypress-image-diff-js/command';
</code></pre>

***

## Rename default screenshots and report folder

```
🚫 cypress-visual-screenshots
✅ cypress-image-diff-screenshots

🚫 cypress-visual-report
✅ cypress-image-diff-html-report
```

***

## New config options

* make screenshots and report folder configurable

```javascript
// cypress-image-diff.config.js
const config = {
  REPORT_DIR: 'html-report',
  SCREENSHOTS_DIR: 'visual-screenshots'
};

module.exports = config;
```

*Note: REPORT\_DIR and SCREENSHOTS\_DIR only work for **Cypress Image Diff Html Report,** and this is intentional. Please consider using **Cypress Image Diff Html Report** for better support.*

***
