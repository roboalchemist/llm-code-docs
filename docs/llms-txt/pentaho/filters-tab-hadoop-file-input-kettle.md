# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/filters-tab-hadoop-file-input-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/filters-tab-hadoop-file-input-kettle.md

# Filters tab

![Filters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-56536bc13b3bd364fb269e852e6c1dbac4e120ee%2FPDITransStep_HadoopFileInput_FilterTab.png?alt=media)

In the **Filters** tab, you can specify the lines you want to skip in the text file.

| Option              | Description                                                                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Filter string**   | The string for which to search.                                                                                                                                                                         |
| **Filter position** | The position where the filter string must be placed in the line. Zero (0) is the first position in the line. If you specify a value below zero, the filter string is searched for in the entire string. |
| **Stop on filter**  | Enter `Y` here if you want to stop processing the current text file when the filter string is encountered.                                                                                              |
| **Positive match**  | Turns filters into positive mode when turned on. Only lines that match this filter will be passed. Negative filters take precedence and are immediately discarded.                                      |
