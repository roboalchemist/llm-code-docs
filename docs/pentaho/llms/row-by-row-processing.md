# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/input-tab/row-by-row-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/input-tab/row-by-row-processing.md

# Row by row processing

Select the **Row by row** option to process your data row by row. Each input row will have its fields mapped to the variables as defined in the **Mapping** table, below. Your Python script will be executed once for each incoming row.

**CAUTION:**

When using the PDI Engine, you can include multiple input steps of the same schema. Each input step must have the same field structure, such that fields and types must appear in the same order in each incoming step. If you include multiple input steps of different schema, an error will occur.

![Input tab in Python Executor](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6d391cab727ddd0ff32e8bcb6cfaef48fe4dc436%2FPDI_TransStep_PythonExec_Input_RowByRow.png?alt=media)

The **Mapping** table contains the following field properties.

| Field Property       | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Variable**         | String assigned as a Python variable.                                                                                                                                                                                                                                                                                                                                                                                      |
| **Python data type** | The Python data type assigned to the variable, such as a string (‘str’), an integer (‘int’), or a floating point (‘float’). For detailed information on data types, see [Mapping data types from PDI to Python](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/input-tab/mapping-data-types-from-pdi-to-python). |
| **PDI field**        | The PDI field to which you want to map the Python variable.                                                                                                                                                                                                                                                                                                                                                                |
| **PDI data type**    | The data type assigned to the PDI field, such as a date, a number, or a timestamp.                                                                                                                                                                                                                                                                                                                                         |

Select the **Get fields** button to populate the table with fields from the input step(s) in your transformation. If necessary, you can modify your selections.
