# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/failure_threshold.md

# FAILURE\_THRESHOLD

Create a file called `cypress-image-diff.config.js`. This should live along side `cypress.config.js`, in the root of the directory.

💢 Default value: `0`

```
// cypress-image-diff.config.js
const config = {
  FAILURE_THRESHOLD: 0.1,
};

module.exports = config;
```

This pass all tests as long as the difference between the baseline and comparison is not greater than 10%
