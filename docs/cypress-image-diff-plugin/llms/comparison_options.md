# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/comparison_options.md

# COMPARISON\_OPTIONS

Custom options passed to pixelmatch, default to `{ threshold: 0.1 }`. Please note that the `COMPARISON_OPTIONS.threshold` is different from the `FAILURE_THRESHOLD`

* `COMPARISON_OPTIONS.threshold`: is the failure threshold for every pixel comparison
* `FAILURE_THRESHOLD`: is the failure threshold for the whole comparison

💢 Default value: `{ threshold: 0.1 }`

```
// cypress-image-diff.config.js
const config = {
  COMPARISON_OPTIONS: { threshold: 0.2 },
};

module.exports = config;
```

You can verify all available and updated options here: [pixelmatch options](https://github.com/mapbox/pixelmatch#api)
