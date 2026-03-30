# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-access-input/options-microsoft-access-input/fields-tab-microsoft-access-input.md

# Fields tab

Use the **Fields** tab to define properties for the fields being exported.

![Microsoft Access input step Fields tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-87ee8c4d041a8ed535374c082466cc552a7b252f%2FPDI%20Microsoft%20Access%20input%20step%20Fields%20tab.png?alt=media)

| Option         | Description                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**       | The name of the output field.                                                                                                                                 |
| **Column**     | The name of the column in the Access table.                                                                                                                   |
| **Type**       | The target data type to convert.                                                                                                                              |
| **Format**     | The format or conversion mask to use in the data type conversion.                                                                                             |
| **Length**     | The length of the output data type.                                                                                                                           |
| **Precision**  | The precision of the output data type.                                                                                                                        |
| **Currency**   | The currency symbol to use during data type conversion.                                                                                                       |
| **Decimal**    | The numeric decimal symbol to use during data type conversion.                                                                                                |
| **Group**      | The numeric grouping symbol to use during data type conversion.                                                                                               |
| **Trim type**  | The type of trimming to use during data type conversion.                                                                                                      |
| **Repeat**     | Select **Y**to repeat the column value of the previous row if the column value is empty (null)                                                                |
| **Get fields** | Click **Get Fields** to have the step populate the table with fields derived from the source file. All fields identified by this step are added to the table. |
