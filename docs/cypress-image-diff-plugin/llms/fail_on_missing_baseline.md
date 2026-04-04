# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/fail_on_missing_baseline.md

# FAIL\_ON\_MISSING\_BASELINE

Boolean to determine whether to fail a test if its baseline doesn't exist, default to false.

💢 Default value: `false`

```
// cypress-image-diff.config.js
const config = {
  FAIL_ON_MISSING_BASELINE: true,
};

module.exports = config;
```

This is beneficial if you constantly get engineers pushing new along with their baselines. Failing the test in CI or locally.
