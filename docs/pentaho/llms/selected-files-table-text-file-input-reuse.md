# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/select-an-engine-text-file-input/using-text-file-input-on-pentaho-engine-cp/options-text-file-input-reuse/file-tab-text-file-input-pentaho-engine/selected-files-table-text-file-input-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/options-text-file-input-reuse/file-tab-text-file-input-pentaho-engine/selected-files-table-text-file-input-reuse.md

# Selected files table

The Selected files table shows files or directories to use as source locations for input. This table is populated by clicking **Add** after you specify a **File or directory**. The input step tries to connect to the specified file or directory when you click **Add** to include it in the table.

The table contains the following columns:

| Column                 | Description                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| **File/Directory**     | The source location indicated by clicking **Add** after specifying it in **File or directory**. |
| **Wildcard (RegExp)**  | Specify a regular expression to match filenames within a specified directory.                   |
| **Exclude wildcard**   | Specify a regular expression to exclude filenames within a specified directory.                 |
| **Required**           | Required source location for input.                                                             |
| **Include subfolders** | Whether subfolders are included within the source location.                                     |

Click **Delete** to remove a source from the table. Click **Edit** to remove a source from the table and return it back to the **File or directory** option.
