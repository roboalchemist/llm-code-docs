# Source: https://cypress.visual-image-diff.dev/getting-started/cypress-integration/cypress-less-than-v10.md

# Cypress < v10

### Cypress plugin

Import and initialise the Cypress image diff plugin:

```js
// cypress/plugin/index.js
module.exports = (on, config) => {
  const getCompareSnapshotsPlugin = require('cypress-image-diff-js/plugin')
  return getCompareSnapshotsPlugin(on, config)
};
```

### Cypress support

Import and add Cypress image command:

```js
// cypress/support/index.js
require('./commands');

// cypress/support/commands.js
compareSnapshotCommand();
```
