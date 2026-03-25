# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/results-rows-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/results-rows-tab.md

# Results rows tab

![Result rows tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-170f778968b6ca5093ade7566f40debfef2339d4%2FJobExecutor_step_ResultRows_tab.png?alt=media)

In this tab, you can specify the destination of the result rows from the job execution as well as the layout of the expected result rows.

**Note:** This step will verify that the data type of the result row fields are identical to what is specified. If there is a difference, an error message will display.

| Option                          | Description                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Target step for result rows** | Use the drop-down menu to select a step in the transformation as the target step.              |
| **Field name**                  | Specify the name of the field.                                                                 |
| **Data type**                   | Use the drop-down menu to specify the data type of the field, such as number, date, or string. |
| **Length**                      | If applicable, specify the length of the field.                                                |
| **Precision**                   | If applicable, specify the precision to use.                                                   |
