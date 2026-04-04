# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/row-grouping-tab-transformation-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/row-grouping-tab-transformation-executor.md

# Row grouping tab

![Row grouping tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9f27fbb55c7ce919568f1a82c45d1db642cbc46c%2FTransExecutorStep_RowGroupingTab.png?alt=media)

Specify how to group the input rows by one of the following methods:

* Specific number of rows.
* Specific field.
* Specified duration of time.

You can use the input rows in a transformation or job entry, or you can get the records themselves by using the ﻿Get rows from result step in a transformation.

To access the **Field to group rows on** or **Duration time when collecting rows** options, delete the default value in the **Number of rows to send to transformation** option.

| Option                                       | Group                                                                                                                                                                                                                                    |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Number of rows to send to transformation** | Specify a number. After every N number of rows, the job will be executed and these N rows will be passed to the transformation.                                                                                                          |
| **Field to group rows on**                   | Specify a field for grouping rows. Rows will be collected in a group as long as the field value stays the same. If the value changes, the transformation will be executed and the accumulated rows will be passed to the transformation. |
| **Duration time when collecting rows**       | Specify a time in milliseconds. This value is the amount of time the step will spend collecting rows prior to the execution of the transformation.                                                                                       |
