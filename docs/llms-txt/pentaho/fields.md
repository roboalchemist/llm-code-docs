# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-upsert/options-salesforce-upsert/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-update/options-salesforce-update/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/salesforce-insert/options-salesforce-insert/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-csv-input-cp/options-s3-csv-input/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/csv-file-input/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-upsert/options-salesforce-upsert/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-update/options-salesforce-update/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-insert/options-salesforce-insert/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-csv-input-cp/options-s3-csv-input/fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/csv-file-input/fields.md

# Fields

You can specify what fields to read from your CSV file through the **Fields** table. Click **Get fields** to have the step populate the table with fields derived from the source file based on the current specified settings (such as **Delimiter** or **Enclosure**). All fields identified by this step are added to the table.

The table contains the following columns:

| Column        | Description                                                                                                                                                                                                                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**      | Name of the field.                                                                                                                                                                                                                                                                                         |
| **Type**      | Type of field (either String, Date, or Number).                                                                                                                                                                                                                                                            |
| **Format**    | An optional mask for converting the format of the original field. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on common valid date and numeric formats you can use in this step. |
| **Length**    | <p>The length of the field depends on the following field types:</p><ul><li>Number: Total number of significant figures in a number.</li><li>String: Total length of string.</li><li>Date: Length of printed output of the string (for example, <code>four</code> is a length for a year).</li></ul>       |
| **Precision** | Number of floating point digits for number-type fields.                                                                                                                                                                                                                                                    |
| **Currency**  | Symbol used to represent currencies (`$5,000.00` or `€5.000,00` for example).                                                                                                                                                                                                                              |
| **Decimal**   | A decimal point can be a "`.`" or "`,`" (`5,000.00` or `5.000,00` for example).                                                                                                                                                                                                                            |
| **Group**     | A grouping can be a "`,`" or "`.`" (`5,000.00` or`5.000,00` for example).                                                                                                                                                                                                                                  |
| **Trim Type** | The trimming method to apply to a string.                                                                                                                                                                                                                                                                  |

Click \*\*Preview\*\* to view the data coming from the source file.

See [Understanding PDI data types and field metadata](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata) to maximize the efficiency of your transformation and job results.
