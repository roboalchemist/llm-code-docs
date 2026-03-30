# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/splunk-input/options-splunk-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/options-s3-file-output/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-output/options-parquet-output/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-output/options-microsoft-excel-output/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-bulk-insert-deprecated/options-elasticsearch-bulk-insert/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/splunk-input/options-splunk-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-input/options-salesforce-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/options-s3-file-output/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/query-metadata-from-a-database-article/options-query-from-database/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-output/options-parquet-output/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/json-input/options-json-input/fields-tab.md

# Fields tab

![Fields tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-1b88a675035e0522c97209734720b0f0fd4fc423%2FPDI_JSON_Inputs_Fields_9.4.png?alt=media)

The **Fields** tab displays field definitions to extract values from the JSON structure. The table in this tab contain the following columns:

| Column        | Description                                                                                                                                                                                                                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**      | Name of field that maps to the corresponding field in the JSON input stream.                                                                                                                                                                                                                               |
| **Path**      | Complete path of the field name in the JSON input stream. All records can be retrieved by adding the asterisk `*` in the path. For example, `$.mydata.*`                                                                                                                                                   |
| **Type**      | Data type of the input field.                                                                                                                                                                                                                                                                              |
| **Format**    | An optional mask for converting the format of the original field. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on common valid date and numeric formats you can use in this step. |
| **Length**    | Length of the field.                                                                                                                                                                                                                                                                                       |
| **Precision** | Number of floating point digits for number-type fields.                                                                                                                                                                                                                                                    |
| **Currency**  | Currency symbol (`$` or `€`, for example).                                                                                                                                                                                                                                                                 |
| **Decimal**   | A decimal point can be a `.` (`5,000.00` for example) or `,` (`5.000,00` for example).                                                                                                                                                                                                                     |
| **Group**     | A grouping can be a `,` (`10,000.00` for example) or `.` (`5.000,00` for example).                                                                                                                                                                                                                         |
| **Trim type** | The trim method to apply to a string.                                                                                                                                                                                                                                                                      |
| **Repeat**    | The corresponding value from the last row repeated if a row is empty.                                                                                                                                                                                                                                      |

Click **Select Fields** to have the step populate the table with fields derived from the source file. All fields identified by this step will be added to the table.

See [Understanding PDI data types and field metadata](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata) to maximize the efficiency of your transformation and job results.
