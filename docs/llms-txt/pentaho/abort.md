# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/abort.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/abort.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/abort.md

# Abort

The Abort step can be used to stop a transformation based on the input data. This step is especially useful for error handling. For example, you can use this step so that a transformation will stop processing at a specified number of rows after Abort detects an error.

![PDI Abort step dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-fe709b97a6036ee89fcb875e5895b79f55583bd0%2FPDI_TransStep_Abort_Dialog.png?alt=media)

### General

Enter the following information in the transformation step field:

* **Step name**: Specify the unique name of the Abort step on the canvas. You can customize the name or leave it as the default.

### Options

The Abort step has the following options:

| Option                               | Description                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Abort the running transformation** | Select to stop the transformation when the **Abort threshold** is reached.                                                                                                                                                                                                                                                                             |
| **Abort and log as an error**        | Select to log an error report when the Abort step stops the transformation. This option is useful when a parent step (such as the Kafka Consumer step) executes a sub-transformation containing the Abort step, where the Abort step will cause the parent step to stop.                                                                               |
| **Stop input processing**            | Select to stop the input steps to the transformation when the **Abort threshold** is reached, while allowing any records already retrieved or initiated to be processed.                                                                                                                                                                               |
| **Abort threshold**                  | Specify the number of rows at which to abort the transformation after an error is detected. For example, if the threshold is set to `0`, the Abort step stops the transformation after the first row is processed. If the threshold is set to `5`, the Abort step stops the transformation after the sixth row is processed. The default value is `0`. |

### Logging

The Abort step has the following logging options:

| Option              | Description                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Abort message**   | Specify the log message to use when the transformation has been aborted. If this field is left blank, a default message is used. |
| **Always log rows** | Select to always log the rows processed by the Abort step, so that you can see the rows that caused the transformation to abort. |
