# Source: https://cypress.visual-image-diff.dev/getting-started/cypress-integration/typescript.md

# Typescript

### Cypress plugin

Import and initialise the Cypress image diff plugin:

```js
// cypress.config.ts
import { defineConfig } from 'cypress';
import getCompareSnapshotsPlugin from 'cypress-image-diff-js/plugin';

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      return getCompareSnapshotsPlugin(on, config);
    },
  },
});
```

### Cypress support

Import compareSnapshotCommand command:

```js
// cypress/support/{scheme}.ts, where {scheme} defaults to e2e
import compareSnapshotCommand from 'cypress-image-diff-js/command';
// for Cypress v12.17.3 and older
import compareSnapshotCommand from 'cypress-image-diff-js';
compareSnapshotCommand();
```

### Troubleshooting

1. `>(0, command_1.default) is not a function`

<figure><img src="https://2460381240-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZyBQte7cOp75X6TWkWrZ%2Fuploads%2FARxNspzFxzZkMLNEItH5%2Fimage.png?alt=media&#x26;token=18676942-09cc-4c1e-b07a-9320293c80b2" alt=""><figcaption></figcaption></figure>

Extend your `tsconfig.json` `compilerOptions` with:

```jsonc
"esModuleInterop": true,
```

in this case your tsconfig.json should look like this:

```

{
    "compilerOptions": {
      "target": "es5",
      "lib": ["es5", "dom"],
      "types": ["cypress", "node"],
      "esModuleInterop": true,
    },
    "include": ["**/*.ts"]
  }

```

Note: You have to restart the Cypress application to reload the changes
