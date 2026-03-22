# Source: https://cypress.visual-image-diff.dev/getting-started/cypress-integration/javascript.md

# Javascript

### Cypress plugin

Import and initialise the Cypress image diff plugin:

```js
// cypress.config.js
const { defineConfig } = require("cypress");
const getCompareSnapshotsPlugin = require('cypress-image-diff-js/plugin');


module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      return getCompareSnapshotsPlugin(on, config);
    },
  },
});
```

### Cypress support

Import and add Cypress image command:

```js
// cypress/support/{scheme}.js, where {scheme} defaults to e2e
const compareSnapshotCommand = require('cypress-image-diff-js/command');
// for Cypress v12.17.3 and older
const compareSnapshotCommand = require('cypress-image-diff-js');
compareSnapshotCommand();
```
