# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/select-an-engine-text-file-input/using-text-file-input-on-pentaho-engine-cp/options-text-file-input-reuse/filters-tab-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/options-text-file-input-reuse/filters-tab-kettle.md

# Filters tab

![Filters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-04bf9e3b70874e3bd61d20bd2c8421553b8050b2%2FPDI_TextFileInput_Dialog_Filters.png?alt=media)

The **Filters** tab contains a table with the columns where you can specify the lines you want to skip in the text file.

| Column              | Description                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Filter string**   | The string that you want to search for.                                                                                                                                                                     |
| **Filter position** | The position where the filter string must be placed in the line. Zero (0) is the first position in the line. If you specify a value below zero (0), the filter string is searched for in the entire string. |
| **Stop on filter**  | Enter `Y` if you want to stop processing the current text file when the filter string is encountered. Enter `N` to continue processing after encountering the string.                                       |
| **Positive match**  | Enter `Y` if you want to process lines that match the filter string. Enter `N` to ignore matching lines.                                                                                                    |
