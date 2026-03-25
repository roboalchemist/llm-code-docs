# Source: https://cypress.visual-image-diff.dev/getting-started/custom-config-file/json_report.md

# JSON\_REPORT

Below are the options available to generate the JSON report

* **FILENAME**: custom name for the json report file, default to `report_[datetime].json` in which `[datetime]` will be replaced with a timestamp. (ie. `report_29-08-2023_233219.json`)
* **OVERWRITE**: set to false if you don't want to overwrite existing report files, default to true. If a duplicate filename is found, the report will be saved with a counter digit added to the filename. (ie.`custom_report_name_1.json`)

💢 Default value: `{ FILENAME: 'report_[datetime].json', OVERWRITE: true }`

```
// cypress-image-diff.config.js
const config = {
  JSON_REPORT: { 
    FILENAME: 'cypress_visual_report',
    OVERWRITE: false,
  }, 
};

module.exports = config;
```
