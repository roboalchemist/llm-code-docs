# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/result-rows-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/result-rows-tab.md

# Result rows tab

![Result rows tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-581c616a82b76cb8487a792f00363d56039ff1e0%2FTransExecutorStep_ResultRowsTab.png?alt=media)

In this tab, you can specify the destination of the result rows from the transformation execution as well as the layout of the expected result rows.

This step will verify that the data type of the result row fields are identical to what is specified. If there is a difference, an error message will display.

**Note:** When you want to send the results from the child transformation back to the parent transformation as the output from the Transformation Executor step, you must enter information in the layout table in the **Result rows** tab.

| Option                          | Description                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Target step for result rows** | Use the drop-down menu to select a step in the current transformation as the target step.      |
| **Field name**                  | Specify the name of the field.                                                                 |
| **Data type**                   | Use the drop-down menu to specify the data type of the field, such as number, date, or string. |
| **Length**                      | If applicable, specify the length of the data type specified.                                  |
| **Precision**                   | If applicable, specify the precision to use.                                                   |
