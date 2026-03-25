# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/retry_options.md

# RETRY\_OPTIONS

💢 Default value: `{}`

```
// cypress-image-diff.config.js
const config = {
  RETRY_OPTIONS: {
    log: true,
    limit: 50, // max number of iterations
    timeout: 30000, // time limit in ms
    delay: 300, // delay before next iteration, ms
  },
};

module.exports = config;
```

You can find all available options here: [retry options](https://www.npmjs.com/package/cypress-recurse#options)
