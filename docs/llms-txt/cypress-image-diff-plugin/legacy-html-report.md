# Source: https://cypress.visual-image-diff.dev/getting-started/reporting/legacy-html-report.md

# Legacy HTML Report

Legacy HTML Report from version 1 continues to function in version 2, but is planned to be deprecated soon. Please consider using the [**Cypress Image Diff HTML Report**](https://app.gitbook.com/o/boZ108LU5mrfWT6zkLtJ/s/ZyBQte7cOp75X6TWkWrZ/~/changes/17/getting-started/reporting/cypress-image-diff-html-report)**.**

For some reasons, you still want to use the legacy HTML report, add the following `after` hook:

```js
// cypress/support/index.js for Cypress versions below 10
// cypress/support/{scheme}.js for Cypress versions 10 and above, where {scheme} defaults to e2e
after(() => {
  cy.task('generateReport')
})
```

The report will look something like:

<figure><img src="https://2460381240-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZyBQte7cOp75X6TWkWrZ%2Fuploads%2FkEzNfAD4HSJk8VlJGgI3%2Freport-example.png?alt=media&#x26;token=9782ea76-c210-4014-aa81-29ac262ef3c0" alt=""><figcaption></figcaption></figure>

*Note: Baseline, comparison and diff images will only be added to the report for failing tests.*

Legacy HTML report will be created following folder:

```
    .
    ├── cypress-image-diff-html-report
```

*Note: Report folder name for legacy HTML report can't be customized via REPORT\_DIR, it's hardcoded as `cypress-image-diff-html-report`.*
