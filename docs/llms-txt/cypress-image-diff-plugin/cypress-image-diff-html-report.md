# Source: https://cypress.visual-image-diff.dev/getting-started/reporting/cypress-image-diff-html-report.md

# Cypress Image Diff HTML Report

From **Cypress Image Diff** version 2, **Cypress Image Diff HTML Report** is the recommended HTML report over the [Legacy HTML report](https://app.gitbook.com/o/boZ108LU5mrfWT6zkLtJ/s/ZyBQte7cOp75X6TWkWrZ/~/changes/17/getting-started/reporting/legacy-html-report). **Cypress Image Diff HTML Report** generates a beautiful HTML report out of a [JSON file](https://cypress.visual-image-diff.dev/getting-started/reporting/json-report), and offers extensive features:

* Update baseline screenshots
* Toggle between different screenshot inspector modes: carousel, slider, and mirror
* Select your preferred colour scheme

Once you've done the [integration part](https://cypress.visual-image-diff.dev/getting-started/cypress-integration), these quick command lines will be helpful:

* `cypress-image-diff-html-report start`: to serve the HTML report out of a generated JSON file in an interactive mode, where you can update the baseline screenshots.
* `cypress-image-diff-html-report generate`: to generate and write to disc the HTML report in case you just want to view the static report.

Or you could integrate the report programmatically:

```javascript
import { start } from 'cypress-image-diff-html-report'

;(async () => {
  await start({
    configFile: 'custom.config.js',
    serverPort: 3000
    // ...
  })
})()
```

[See here](https://github.com/kien-ht/cypress-image-diff-html-report) for more details about how to use Cypress Image Diff HTML Report.

<figure><img src="https://2460381240-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZyBQte7cOp75X6TWkWrZ%2Fuploads%2Fb5k1ULDJIuP0KifbVpmF%2FScreenshot%202023-11-24%20at%2000.56.13.png?alt=media&#x26;token=062cf9ed-a44d-43a2-9b04-0e60125f87da" alt=""><figcaption></figcaption></figure>

If you run the `generate` command, this following folder structure will be expected:

```
    .
    ├── cypress-image-diff-html-report
        ├── cypress-image-diff-html-report.html
        ├── report_[datetime].json
```
