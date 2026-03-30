# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/row-grouping-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/job-executor/options-job-executor/row-grouping-tab.md

# Row grouping tab

![Row grouping tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-da4f35fd39d1a3f8f5d803baa1292eae84b88a00%2FJobExecutor_step_RowGrouping_tab.png?alt=media)

Specify how to group the result rows by one of the following methods:

* Specific number of rows.
* Specific field.
* Specified duration of time.

You can use the result rows in a transformation or job entry, or you can get the records themselves by using the ﻿Get rows from result step in a transformation.

To access the **Field to group rows on** or **Duration time when collecting rows** options, delete the default value in the **Number of rows to send to transformation** option.

| Option                                       | Description                                                                                                                                                                                                                   |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Number of rows to send to transformation** | Specify a number. After every n number of rows, the job will be executed and these n rows will be passed to the transformation.                                                                                               |
| **Field to group rows on**                   | Specify a field for grouping rows. Rows will be collected in a group as long as the field value stays the same. If the value changes, the job will be executed and the accumulated rows will be passed to the transformation. |
| **Duration time when collecting rows**       | Specify a time in milliseconds. This value is the amount of time the step will spend collecting rows prior to the execution of the job.                                                                                       |
