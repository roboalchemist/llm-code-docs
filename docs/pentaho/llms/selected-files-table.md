# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/files-tab/selected-files-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/file-tab/selected-files-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/files-tab/selected-files-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/file-tab/selected-files-table.md

# Selected files table

The Selected files table shows files or directories to use as source locations for input. This table is populated by clicking **Add** after you specify a **File or directory**. The JSON input step tries to connect to the specified file or directory when you click **Add** to include it into the table.

The table contains the following columns:

| Column                 | Description                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| **File/Directory**     | The source location indicated by clicking **Add** after specifying it in **File or directory**. |
| **Wildcard (RegExp)**  | Wildcards as specified in **Regular expression**.                                               |
| **Exclude wildcard**   | Excluded wildcards as specified in **Exclude regular expression**.                              |
| **Required**           | Required source location for input.                                                             |
| **Include subfolders** | Whether subfolders are included within the source location.                                     |

Click **Delete** to remove a source from the table. Click **Edit** to remove a source from the table and return it back to the **File or directory** option.

Use **Show filename(s)** to display the file names of the sources successfully connected to the JSON Input step.
