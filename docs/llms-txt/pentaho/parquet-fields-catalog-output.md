# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-output/before-you-begin-catalog-output/general-catalog-output/fields-tab-catalog-output/parquet-fields-catalog-output.md

# Parquet fields

![Parquet fields](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-3d5d238d12725ce2700f4d98f4f752d20b3956dd%2FPDI_CatalogOutput_Fields_Parquet.png?alt=media)

The table below describes options for configuring the properties of the fields being written for Parquet data.

| Column                  | Description                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parquet Path**        | Specify the name of the column in the Parquet file.                                                                               |
| **Name**                | Specify the name of the PDI field.                                                                                                |
| **Parquet Type**        | Specify the data type used to store the data in the Parquet file.                                                                 |
| **Precision**           | Specify the total number of significant digits in the number (only applies to the Decimal Parquet type). The default value is 20. |
| **Scale**               | Specify the number of digits after the decimal point (only applies to the Decimal Parquet type). The default value is 10.         |
| **Default value**       | Specify the default value of the field if it is null or empty.                                                                    |
| **Null**                | Specify if the field can contain null values.                                                                                     |
| **Get Fields** (button) | Click to retrieve a list of fields from the input stream.                                                                         |

**Note:** To avoid a transformation failure, make sure the **Default value** field contains values for all fields where **Null** is set to **No**.

You can define the fields manually, or you can click **Get Fields** to automatically populate the fields. When the fields are retrieved, a PDI type is converted into an appropriate Parquet type, as shown in the table below. You can also change the selected Parquet type by using the **Type** drop-down menu or by entering the type manually.

| PDI Type    | Parquet Type    |
| ----------- | --------------- |
| InetAddress | UTF8            |
| String      | UTF8            |
| TimeStamp   | TimestampMillis |
| Binary      | Binary          |
| BigNumber   | Decimal         |
| Boolean     | Boolean         |
| Date        | Date            |
| Integer     | Int64           |
| Number      | Double          |
