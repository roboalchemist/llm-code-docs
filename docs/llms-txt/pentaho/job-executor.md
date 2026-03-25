# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/job-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/job-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor.md

# Job Executor

The Job Executor step allows you to execute a Pentaho Data Integration (PDI) job. It is similar to the [Transformation Executor](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor) step, but works with jobs. By default, the specified job will be executed once for each input row. You can use the input row to set parameters and variables. The executor step then passes this row to the job in the form of a result row.

You can also pass a group of records based on the value in a field, such that when the value changes, the specified job is executed. In these cases, the first row in the group of rows is used to set parameters or variables in the job.

You can also launch multiple copies of this step to assist in parallel job processing.

**Note:** This step does not abort when the calling job errors out. To control the flow or to abort the job incase of errors, please specify the fields and a target step in the **Execution results** tab to log the number of errors.
