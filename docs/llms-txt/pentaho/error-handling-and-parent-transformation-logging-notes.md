# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/error-handling-and-parent-transformation-logging-notes.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/error-handling-and-parent-transformation-logging-notes.md

# Error handling and parent transformation logging notes

Keep the following notes in mind when building transformations with the Transformation Executor step:

* This step does not abort when the calling transformation errors out. To control the flow or to abort the transformation in case of errors, please specify the fields and a target step in the **Execution results** tab to log the number of errors.
* During the actual implementation, the log of the parent transformation contains only the last processed batch of data. This method lessens the strain on the back-end logging. You can obtain a detailed log of the child transformation by viewing the execution results. Be sure to define a target step within the **Execution results** tab and view the field name of the execution logging text, by default, ExecutionLogText.
