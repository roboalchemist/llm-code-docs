# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/options-s3-file-output/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/options-regex-evaluation/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-writer/options-microsoft-excel-writer/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-output/options-microsoft-excel-output/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/options-s3-file-output/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/options-regex-evaluation/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-writer/options-microsoft-excel-writer/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/content-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/content-tab.md

# Content tab

![Content tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-de79f9c18a4475d242e81dbf1c5df98afa0959b6%2FPDI_JSON_Input_Content.png?alt=media)

The **Content** tab contains the following options for configuring which data to retrieve:

| Option                                | Description                                                                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ignore empty file**                 | Select to skip empty files. When cleared, empty files will cause the process to fail and stop.                                                                                                         |
| **Do not raise an error if no files** | Select to continue when no files are available to process.                                                                                                                                             |
| **Ignore missing path**               | Select to continue processing files when an error occurs that (1) no fields match the JSON path or (2) that all the values are null. When cleared, no further rows are processed when an error occurs. |
| **Default path leaf to null**         | Select to return a null value for missing paths.                                                                                                                                                       |
| **Limit**                             | Specify a limit on the number of records generated from the step. Results are not limited when set to `zero`.                                                                                          |
| **Include filename in output**        | Select to add a string field with the filename in the result.                                                                                                                                          |
| **Rownum in output**                  | Select to add an integer field with the row number in the result.                                                                                                                                      |
| **Add filenames to result**           | Select to add processed files to the result file list.                                                                                                                                                 |
