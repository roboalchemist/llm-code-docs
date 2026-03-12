# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/execution-results-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/execution-results-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/execution-results-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/execution-results-tab.md

# Execution results tab

![Execution results tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-dc5ad1865a0161231175851a9081510d4ed24d7f%2FJob_Executor_step_ExecutionResults_tab.png?alt=media)

You can define the result fields for the job and to which step in the transformation to send them. If you do not need a certain result, leave a blank input field.

| Option                                    | Description                                                                                                           | Default Value           |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **Target step for the execution results** | Use the drop-down menu to select a step in the transformation as the target step to receive the results from the job. | N/A                     |
| **Execution time (ms)**                   | Specify the field name for the job execution time.                                                                    | ExecutionTime           |
| **Execution result**                      | Specify the field name for the job execution result.                                                                  | ExecutionResult         |
| **Number of errors**                      | Specify the field name for the number of errors during the execution of the job.                                      | ExecutionNrErrors       |
| **Number of rows read**                   | Specify the field name for the total number of rows read during the execution of the job.                             | ExecutionLinesRead      |
| **Number of rows written**                | Specify the field name for the total number of rows written during the execution of the job.                          | ExecutionLinesWritten   |
| **Number of rows input**                  | Specify the field name for the total number of input rows during the execution of the job.                            | ExecutionLinesInput     |
| **Number of rows output**                 | Specify the field name for the total number of output rows during the execution of the job.                           | ExecutionLinesOutput    |
| **Number of rows rejected**               | Specify the field name for the total number of rows rejected during the execution of the job.                         | ExecutionLinesRejected  |
| **Number of rows updated**                | Specify the field name for the total number of rows updated during the execution of the job.                          | ExecutionLinesUpdated   |
| **Number of rows deleted**                | Specify the field name for the total number of rows deleted during the execution of the job.                          | ExecutionLinesDeleted   |
| **Number of files retrieved**             | Specify the field name for the total number of files retrieved during the execution of the job.                       | ExecutionFilesRetrieved |
| **Exit status**                           | Specify the field name for the exit status of the execution of the job.                                               | ExecutionExitStatus     |
| **Execution logging text**                | Specify the field name for the logging text from the execution of the job.                                            | ExecutionLogText        |
| **Log channel ID**                        | Specify the field name for the log channel ID used during the execution of the job.                                   | ExecutionLogChannelID   |
