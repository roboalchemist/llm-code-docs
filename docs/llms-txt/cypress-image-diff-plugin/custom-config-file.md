# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file.md

# Custom config file

If you'd like to take advantages of additional features, you will need to set up the custom config file.

Create a file called `cypress-image-diff.config.js`. This should live along side `cypress.config.js`, in the root of the directory.

If your project is written in ESM module, then you would need to use .cjs instead of .js extension.

```
// cypress-image-diff.config.js
// cypress-image-diff.config.cjs
const config = {
  ROOT_DIR: 'custom-folder-name',
};

module.exports = config;
```

> **Note**: In order to make this custom config values effective, remember to return `getCompareSnapshotsPlugin` instance inside function `setupNodeEvents`:

```
export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
     return getCompareSnapshotsPlugin(on, config);
    },
  },
})
```

Currently supported values in the custom config file:

* [**ROOT\_DIR**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/root_dir)
* [**FAILURE\_THRESHOLD**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/failure_threshold)
* [**RETRY\_OPTIONS**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/retry_options)
* [**FAIL\_ON\_MISSING\_BASELINE**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/fail_on_missing_baseline)
* [**COMPARISON\_OPTIONS**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/comparison_options)
* [**JSON\_REPORT**](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/json_report)
* [**CYPRESS\_SCREENSHOT\_OPTIONS**](https://app.gitbook.com/o/boZ108LU5mrfWT6zkLtJ/s/ZyBQte7cOp75X6TWkWrZ/~/changes/17/getting-started/custom-config-file/cypress_)
* [**REPORT\_DIR**](https://app.gitbook.com/o/boZ108LU5mrfWT6zkLtJ/s/ZyBQte7cOp75X6TWkWrZ/~/changes/17/getting-started/custom-config-file/report_dir)
* [**SCREENSHOTS\_DIR**](https://app.gitbook.com/o/boZ108LU5mrfWT6zkLtJ/s/ZyBQte7cOp75X6TWkWrZ/~/changes/17/getting-started/custom-config-file/screenshots_dir)
