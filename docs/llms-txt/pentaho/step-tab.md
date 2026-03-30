# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/options-mongodb-execute/step-tab.md

# Step tab

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b2c5432f93bdbdf056c7af43ad8323bc1cb6f21e%2FStep%20tab%20MongoDB.png?alt=media)

You use this tab to specify step behavior.

| Option             | Description                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Result field name  | Enter a value to add a **String** field to the step's output stream containing output information for each command executed. If more than one command is specified for execution, there will be a row output with resulting information for each command.                                                                                                          |
| Command field name | Enter a value to add a **String** field to the step's output stream containing command information for each retrieved row. This field identifies the structure of each row’s results when there are multiple commands executed in the script and the subsequent step parses the information. Leave the field name empty to omit this field in the output stream, . |
| Stop on error      | Select this option to write to the log and stop the transformation when an error occurs. If if you do not select this option, errors are reported to the step's error-handling stream.                                                                                                                                                                             |
