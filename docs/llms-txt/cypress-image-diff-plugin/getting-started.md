# Source: https://cypress.visual-image-diff.dev/getting-started.md

# Getting started

Visual regression test with cypress

This tool was created to make visual regression as simple as possible, by exposing basic functions that allow you to view the difference between images. The wrapper uses [pixelmatch](https://github.com/mapbox/pixelmatch) which is simple and powerful and relies on [cypress](https://github.com/cypress-io) to take screenshots.

### Table of contents

* [Cypress integration](https://cypress.visual-image-diff.dev/getting-started/cypress-integration)
* [Custom config file](https://cypress.visual-image-diff.dev/getting-started/custom-config-file)
* [Reporting](https://cypress.visual-image-diff.dev/getting-started/reporting)
* [Client options](https://cypress.visual-image-diff.dev/getting-started/client-options)
* [Running tests](https://cypress.visual-image-diff.dev/getting-started/running-tests)
* [Contributing](https://cypress.visual-image-diff.dev/getting-started/contributing)
* [Publishing](https://cypress.visual-image-diff.dev/getting-started/publishing)

### Plugin features

* [Screenshot of whole page](#take-screenshot-and-compare-the-whole-page)
* [Screenshot with increased pixel threshold tolerance](#take-screenshot-with-increased-pixel-threshold-for-an-individual-test)
* [Retry for an individual test](#retry-for-an-individual-test)
* [Screenshot of an element](#take-screenshot-and-compare-an-element)
* [Hide an element before taking a screenshot](#hiding-an-element-before-taking-a-screenshot)

### Other

* [Guidelines for better testing results](#guidelines-for-better-visual-testing-results)
* [Update baseline images](#updating-baseline-images)
* [Folder structure](#folder-structure)
* [Force resolution size](#force-resolution-size)
* [Preserve cypress original screenshots](#preserving-the-original-screenshot)

### Getting started

Once you have setup cypress and followed [Cypress integration](https://cypress.visual-image-diff.dev/getting-started/cypress-integration) you can start writing tests

#### Writing a test

Create a spec file under cypress integration folder i.e `cypress/integration/specs/some-test-spec.js`

Then use the cypress image diff command to take screenshots of pages or elements:

#### Take screenshot and compare the whole page

```js
describe('Visuals', () => {
  it('should compare screenshot of the entire page', () => {
    cy.visit('www.google.com')
    cy.compareSnapshot('home-page')
  })
})
```

#### Take screenshot with increased pixel threshold for an individual test

You can also make the comparison assertion more flexible by applying a higher threshold (default is 0):

```js
describe('Visuals', () => {
  it('should compare screenshot of the entire page', () => {
    cy.visit('www.google.com')
    cy.compareSnapshot({
      name: 'home-page-with-threshold',
      testThreshold: 0.2
    })
  })
})
```

#### Retry for an individual test

You can also retry the snapshot comparison by passing in an optional third parameter. It accepts the same options as [cypress-recurse](https://github.com/bahmutov/cypress-recurse#options).

```js
describe('Visuals', () => {
  it('should compare screenshot of the entire page', () => {
    cy.visit('www.google.com')
    cy.compareSnapshot({
      name: 'home-page-with-threshold',
      testThreshold: 0, 
      retryOptions: {
        limit: 5, // max number of retries
        delay: 500 // delay before next iteration, ms
      }
    })
  })
})
```

#### Take screenshot and compare an element

```js
describe('Visuals', () => {
  it('should compare screenshot from a given element', () => {
    cy.visit('www.google.com')
    cy.get('#report-header').compareSnapshot('search-bar-element')
  })
})
```

#### Hiding an element before taking a screenshot

```js
describe('Visuals', () => {
  it('should compare screenshot from a given element', () => {
    cy.visit('www.google.com')
    cy.get('#report-header').hideElement() // hideElement(false) to unhide
    cy.compareSnapshot('search-bar-element')
  })
})
```

#### Updating baseline images

If there are wanted changes to the application in test and if we need to update baseline images, you can follow the steps in [Client options](https://cypress.visual-image-diff.dev/getting-started/client-options) documentation to update the baselines.

Alternatively, you can delete the baseline image that you wish to be updated and rerun the tests, this will create a new baseline image with the updated image.

#### Folder structure

This folder structure will be created by default at the root of your project where your `package.json` lives:

```
    .
    ├── cypress-image-diff-screenshots
        ├── baseline
        ├── comparison
        ├── diff
    ├── cypress-image-diff-html-report
```

In some cases, you may want to modify the folder structure relative to the directory. To accomplish this you will need to set a value on the ROOT\_DIR key value on the `cypress-image-diff.config.js` [custom config file](https://cypress.visual-image-diff.dev/getting-started/custom-config-file). `ROOT_DIR` is a path relative to the current working directory.

#### Force resolution size

In order to force the screenshot resolution when running a test you will need to set the following cypress config values in `cypress.json`:

```js
{
  "viewportWidth": 1000, // Default value: 1280
  "viewportHeight": 660 // Default value: 720
}
```

#### Preserving the original screenshot

All screenshots will be renamed and moved from the default screenshot location to a new screenshot folder structure. To preserve the screenshot in the original location, set the following values in `cypress.json`:

```json
{
  "env": {
    "preserveOriginalScreenshot": true
  }
}
```

### Guidelines for better visual testing results

> **Note**: This plugin internally uses `cypress.screenshot` command and due to its limitation on taking full page screenshots (<https://github.com/cypress-io/cypress/issues/2681>), you might encounter some weird results if you have `html`, `body` set to `100%`, or `scroll-behavior: smooth`, this workaround of reseting these CSS properties before invoking the command might help:

```
cy.get("html, body").invoke(
  "attr",
  "style",
  "height: auto; scroll-behavior: auto;"
);
```

Full page screenshots are generally not recommended over individual DOM elements, as stated in the [Cypress docs](https://docs.cypress.io/guides/tooling/visual-testing#Visual-diff-elements), so use them sparingly.

> **Note**: Be aware that despite forcing a screenshot resolution to a particular height and width for a test, if this test is run on different infrastructure (i.e a 13" Mac vs PC attached to a 30" monitor), the results will be different. So it's extremely important that you standardize where the tests will run, both locally and CI.
>
> One way to handle this, is by running it with docker container or against BrowserStack or alike.
>
> This project tests use a docker container to run the tests so it could be used as an example.
