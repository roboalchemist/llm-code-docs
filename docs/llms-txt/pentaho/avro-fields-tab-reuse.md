# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-input/using-the-avro-input-step-on-the-pentaho-engine/options-reuse/avro-fields-tab-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-input/options-reuse/avro-fields-tab-reuse.md

# Avro Fields tab

![Avro Input Avro Fields Tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e0afda2c4be9bcc051d55ea155ccdb0b9f258115%2FPDI_TransStep_Avro_Input_AvroFields_Tab.png?alt=media)

The table in the **Avro Fields** tab defines the following properties for the input fields from the Avro source:

| Field Property                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Avro path** (**Avro type**) | The location of the Avro source (and its format type).                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Indexed values**            | <p>The index key to use in an Avro path collection. You can use this field for map or array expansion, which expands array or map values to return multiple rows of data.</p><ul><li>To return map elements, specify an index key.</li><li>To return array elements, specify the array index number, or use the asterisk wildcard (\*) to return all elements of an array.</li></ul><p>When this field is left blank, data is not returned for the field.</p> |
| **Name**                      | The name of the input field.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Type**                      | The type of the input field, such as String or Date.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Format**                    | The format of the input field.                                                                                                                                                                                                                                                                                                                                                                                                                                |

The \*\*Avro Fields\*\* tab also contains the following options for specifying how certain fields behave in this step:

| Option                                            | Description                                                                                                                                                                                                                              |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pass through fields from previous step**        | <p>Specify how fields pass through this step:</p><ul><li>Select to pass the fields from the previous step along with the fields in the current step to the next step.</li><li>Clear to not pass these fields to the next step.</li></ul> |
| **Allow null values for missing paths or fields** | <p>Specify how missing fields should be replaced:</p><ul><li>Select to replace missing fields in the incoming data with null values.</li><li>Clear to not replace missing fields with null values.</li></ul>                             |

After you have provided a path to an Avro data file or Avro schema, click \*\*Get Fields\*\* to populate the fields.

These fields represent the Avro schema. When the schema field is retrieved, the Avro type is converted to an appropriate PDI type. A user can change the PDI type. Below is the Avro-to-PDI data type conversion table.

| Avro Type | PDI Type  |
| --------- | --------- |
| String    | String    |
| TimeStamp | TimeStamp |
| Bytes     | Binary    |
| Decimal   | BigNumber |
| Boolean   | Boolean   |
| Date      | Date      |
| Long      | Integer   |
| Double    | Number    |
| int       | Integer   |
| float     | Number    |

**Note:** The default format mask for the date type is yyyy-MM-dd. The default format mask for the timestamp type is yyyy-MM-dd HH:mm:ss.SSS. If the data stored is any other format, and was stored as a string data type, it will not be possible to retrieve the column data. In that case, null will be returned for that column.
