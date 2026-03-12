# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab/variable-to-fields-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab/variable-to-fields-processing.md

# Variable to fields processing

Select the **Variable to fields** option if your script is intended to produce its output in the form of individual variables, each of which contains a built-in type, such numerics, strings, and Booleans. This option will map the Python variables and their data types to PDI fields and their data types when running the transformation.

![Output tab in Python Executor](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-55cc4e8f3d2af2bffd579ee345c75005f91d9f34%2FPDI_TransStep_PythonExec_Output_VariablesToFields.png?alt=media)

These are the fields in the **Mapping** table. Select the **Get fields** button to populate the table with fields from the output step(s) in your transformation.

**Note:** The **Get fields** button will execute your Python script using random input values to determine the output variables. If your script is long running, or has fixed data requirements, consider manually entering the output variable mapping.

| Option               | Description                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Variable**         | The name of the Python variable that will be mapped to a PDI field.                                                                                                                                                                                                                                                                         |
| **Python data type** | The value of the data type of the variable. For detailed information on data types, see [Mapping data types from Python to PDI](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/options-python-executor/output-tab/mapping-data-types-from-python-to-pdi). |
| **PDI field**        | The value of the PDI field to which you want to map the Python variable.                                                                                                                                                                                                                                                                    |
| **PDI data type**    | The value of the data type assigned to the PDI field, such as a date, a number, or a timestamp.                                                                                                                                                                                                                                             |
