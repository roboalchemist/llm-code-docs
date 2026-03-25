# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/screenshots_dir.md

# SCREENSHOTS\_DIR

The `SCREENSHOTS_DIR` specifies where all the screenshots are saved. It's relative to the [ROOT\_DIR](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/root_dir).

💢 Default value: `cypress-image-diff-screenshots`

```
// cypress-image-diff.config.js
const config = {
  ROOT_DIR: 'visual-test',
  SCREENSHOTS_DIR: 'screenshots'
};

module.exports = config;
```

Output directory:

```
    .
    ├── visual-test
        ├── screenshots
            ├── baseline
            ├── comparison
            ├── diff
```
