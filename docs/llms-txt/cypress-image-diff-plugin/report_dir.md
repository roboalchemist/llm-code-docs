# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/report_dir.md

# REPORT\_DIR

The `REPORT_DIR` specifies where the generated JSON report lives. It's relative to the [ROOT\_DIR](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/root_dir).

💢 Default value: `cypress-image-diff-html-report`

<pre><code>// cypress-image-diff.config.js
const config = {
<strong>  ROOT_DIR: 'visual-test/custom-folder-name',
</strong>  REPORT_DIR: 'html-report',
};

module.exports = config;
</code></pre>

Output directory:

```
    .
    ├── visual-test
        ├── custom-folder-name
            ├── html-report
```
