# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/root_dir.md

# ROOT\_DIR

The ROOT\_DIR value should be relative to the root of the directory.

💢 Default value: `''`

```
// cypress-image-diff.config.js
const config = {
  ROOT_DIR: 'visual-test/custom-folder-name',
};

module.exports = config;
```

Output directory:

```
    .
    ├── visual-test
        ├── custom-folder-name
            ├── cypress-visual-screenshots
                ├── baseline
                ├── comparison
                ├── diff
            ├── cypress-visual-report
```
