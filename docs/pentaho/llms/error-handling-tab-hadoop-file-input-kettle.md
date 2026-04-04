# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/error-handling-tab-hadoop-file-input-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/error-handling-tab-hadoop-file-input-kettle.md

# Error Handling tab

![Error Handling tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e5cbcbd8c966a16b70ce00a9f9178d390c2f5337%2FPDITransStep_HadoopFileInput_ErrorHandlingTab.png?alt=media)

In the **Error Handling** tab, you can specify how the step reacts when errors occur, such as malformed records, bad enclosure strings, wrong number of fields, and premature line ends.

| Option                                   | Description                                                                                                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ignore errors?**                       | Select if you want to ignore errors during parsing.                                                                                                                                                                                        |
| **Skip error lines?**                    | Select if you want to skip those lines that contain errors. You can generate an extra file that contains the line numbers where the errors occur. Lines with errors are not skipped. The fields that have parsing errors are empty (null). |
| **Error count field name**               | Add a field to the output stream rows. This field contains the number of errors on the line.                                                                                                                                               |
| **Error fields field name**              | Add a field to the output stream rows. This field contains the field names on which an error occurred.                                                                                                                                     |
| **Error fields text field name**         | Add a field to the output stream rows. This field contains the descriptions of the parsing errors that have occurred.                                                                                                                      |
| **Warnings file directory**              | When warnings are generated, they are placed in this directory. The name of that file is `<warning dir>/filename.<date_time>.<warning extension>`.                                                                                         |
| **Error files directory**                | When errors occur, they are placed in this directory. The name of the file is `<errorfile_dir>/filename.<date_time>.<errorfile_extension>`.                                                                                                |
| **Failing line numbers files directory** | When a parsing error occurs on a line, the line number is placed in this directory. The name of that file is `<errorline dir>/filename.<date_time>.<errorline extension>`.                                                                 |
