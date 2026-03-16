# Source: https://cypress.visual-image-diff.dev/getting-started/reporting/json-report.md

# JSON report

If you want to generate your custom report, generate a report json file by passing `JSON_REPORT` in the [custom config file](https://cypress.visual-image-diff.dev/getting-started/custom-config-file), and build your own HTML file from this json.&#x20;

Example JSON could be found at the bottom of this page.

### Folder structure

When a JSON report is generated, it will be created in the following default folder:

```
    .
    ├── cypress-image-diff-report
        ├── report_[datetime].json
```

Report folders can be customized via the [REPORT\_DIR](https://cypress.visual-image-diff.dev/getting-started/custom-config-file/report_dir) config option.

Example JSON:

```
{
  "total": 6,
  "totalPassed": 3,
  "totalFailed": 3,
  "totalSuites": 3,
  "suites": [
    {
      "name": "image-diff.cy.js",
      "path": "cypress/specs/image-diff.cy.js",
      "tests": [
        {
          "status": "fail",
          "name": "image-diff.cy-wholePage",
          "percentage": 0.0900966398590363,
          "failureThreshold": 0,
          "specPath": "cypress/specs/image-diff.cy.js",
          "specFilename": "image-diff.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/image-diff.cy-wholePage.png",
          "diffPath": "cypress-visual-screenshots/diff/image-diff.cy-wholePage.png",
          "comparisonPath": "cypress-visual-screenshots/comparison/image-diff.cy-wholePage.png"
        },
        {
          "status": "pass",
          "name": "image-diff.cy-wholePageThreshold",
          "percentage": 0.0900966398590363,
          "failureThreshold": 0.2,
          "specPath": "cypress/specs/image-diff.cy.js",
          "specFilename": "image-diff.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/image-diff.cy-wholePageThreshold.png",
          "diffPath": "",
          "comparisonPath": "cypress-visual-screenshots/comparison/image-diff.cy-wholePageThreshold.png"
        },
        {
          "status": "pass",
          "name": "image-diff.cy-element",
          "percentage": 0,
          "failureThreshold": 0,
          "specPath": "cypress/specs/image-diff.cy.js",
          "specFilename": "image-diff.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/image-diff.cy-element.png",
          "diffPath": "",
          "comparisonPath": "cypress-visual-screenshots/comparison/image-diff.cy-element.png"
        },
        {
          "status": "fail",
          "name": "image-diff.cy-hideElement",
          "percentage": 0.0900966398590363,
          "failureThreshold": 0,
          "specPath": "cypress/specs/image-diff.cy.js",
          "specFilename": "image-diff.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/image-diff.cy-hideElement.png",
          "diffPath": "cypress-visual-screenshots/diff/image-diff.cy-hideElement.png",
          "comparisonPath": "cypress-visual-screenshots/comparison/image-diff.cy-hideElement.png"
        }
      ]
    },
    {
      "name": "retry.cy.js",
      "path": "cypress/specs/retry.cy.js",
      "tests": [
        {
          "status": "pass",
          "name": "retry.cy-retry",
          "percentage": 0,
          "failureThreshold": 0,
          "specPath": "cypress/specs/retry.cy.js",
          "specFilename": "retry.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/retry.cy-retry.png",
          "diffPath": "",
          "comparisonPath": "cypress-visual-screenshots/comparison/retry.cy-retry.png"
        }
      ]
    },
    {
      "name": "folder-structure.cy.js",
      "path": "cypress/specs/folder-structure-test/folder-structure.cy.js",
      "tests": [
        {
          "status": "fail",
          "name": "folder-structure.cy-wholePage",
          "percentage": 0.0900966398590363,
          "failureThreshold": 0,
          "specPath": "cypress/specs/folder-structure-test/folder-structure.cy.js",
          "specFilename": "folder-structure.cy.js",
          "baselinePath": "cypress-visual-screenshots/baseline/folder-structure.cy-wholePage.png",
          "diffPath": "cypress-visual-screenshots/diff/folder-structure.cy-wholePage.png",
          "comparisonPath": "cypress-visual-screenshots/comparison/folder-structure.cy-wholePage.png"
        }
      ]
    }
  ],
  "startedAt": "2023-08-25T09:53:41.477Z",
  "endedAt": "2023-08-25T09:54:00.875Z",
  "duration": 15318,
  "browserName": "chrome",
  "browserVersion": "116.0.5845.110",
  "cypressVersion": "10.8.0"
}
```
