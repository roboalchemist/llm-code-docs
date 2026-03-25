# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/use-error-handling-copybook-input-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/use-error-handling-copybook-input-step.md

# Use Error Handling

The JSON object is placed in the error description field within the error row. **Error handling** must be enabled on the step to capture the error columns and descriptions. On the canvas, right-click the Copybook Input step and select **Error Handling** to open the Step error handling settings window and configure the error output column names. See the [Use the Transformation menu](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/use-the-transformation-menu) for details.

The following table details the JSON object format for the output error stream.

| Key        | Type    | Example                                  | Description                                                   |
| ---------- | ------- | ---------------------------------------- | ------------------------------------------------------------- |
| record     | Integer | 0                                        | The record number originating from the Copybook Input step.   |
| converter  | String  | BigNumberColumnConverter                 | The converter class that originated the error.                |
| exception  | String  | RecordException                          | The exception class of the error.                             |
| message    | String  | Invalid sign in field: OPEN-YEAR         | The error message text, if it exists.                         |
| fieldName  | String  | OPEN-YEAR                                | The name of field that has the error.                         |
| position   | Integer | 22                                       | The position of the field.                                    |
| length     | Integer | 3                                        | The length of the field.                                      |
| value      | String  | 404040                                   | The value read as a hexadecimal string.                       |
| recordHash | String  | 240c992c3aaebccf6dc0e99a4ed1a447e4811bed | The record checksum originating from the Copybook Input step. |
