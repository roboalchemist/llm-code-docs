# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-output/using-the-avro-output-step-on-the-pentaho-engine/options-avro-output-reuse/fields-tab-avro-output-pentaho-engine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-output/options-avro-output-reuse/fields-tab-avro-output-pentaho-engine.md

# Fields tab

![Avro Output Fields tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-cfc60398332eedfa27948f4fa6e297287cdd5415%2FPDI_AvroOutput_FieldsTab_PentahoEngine.png?alt=media)

**Note:** The table in the **Fields** tab defines the following fields that make up the Avro schema created by this step:

| Field             | Description                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Avro path**     | The name of the field as it will appear in the Avro data and schema files.                             |
| **Name**          | The name of the PDI field.                                                                             |
| **Avro type**     | Defines the Avro data type of the field.                                                               |
| **Precision**     | Applies only to the Decimal Avro type, the total number of digits in the number. The default is 10.    |
| **Scale**         | Applies only to the Decimal Avro type, the number of digits after the decimal point. The default is 0. |
| **Default value** | The default value of the field if it is null or empty.                                                 |
| **Null**          | Specify if the field can contain null values.                                                          |

**Note:** To avoid a transformation failure, make sure the **Default value** field contains values for all fields where **Null** is set to No.

**Note:** As shown in the table below, you can click **Get Fields** to populate the fields from the incoming PDI stream or these fields can be defined manually. During the retrieval of fields, a PDI type is converted to an appropriate Avro type. If desired, you can change the converted field type to another Avro type.

| PDI Type        | Avro Type |
| --------------- | --------- |
| **InetAddress** | String    |
| **String**      | String    |
| **TimeStamp**   | TimeStamp |
| **Binary**      | Bytes     |
| **BigNumber**   | Decimal   |
| **Boolean**     | Boolean   |
| **Date**        | Date      |
| **Integer**     | Long      |
| **Number**      | Double    |
