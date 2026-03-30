# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-input/select-an-engine-parquet-input/using-parquet-input-on-pentaho-engine/general-parquet-input-kettle/fields-pentaho-engine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-input/general-parquet-input-kettle/fields-pentaho-engine.md

# Fields

The **Fields** section contains the following items:

![Parquet input step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-36f4ac7f91b4de654f1e709d4a0d2cebf04a9815%2FPDI_ParquetInput_Fields_PentahoEngine.png?alt=media)

* The **Pass through fields from the previous step** option reads the fields from the input file without redefining any of the fields.
* The table defines the data about the columns to read from the Parquet file.

The table in the **Fields** section defines the fields to read as input from the Parquet file, the associated PDI field name, and the data type of the field.

Enter the information for the **Parquet input** step fields, as shown in the following table:

| Field      | Description                                                                                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path**   | Specify the name of the field as it will appear in the Parquet data file or files, and the Parquet data type.                                                                                       |
| **Name**   | Specify the name of the input field.                                                                                                                                                                |
| **Type**   | Specify the type of the input field.                                                                                                                                                                |
| **Format** | Specify the [date format](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/common-formats) when the **Type** specified is **Date**. |

Provide a path to a Parquet data file and click **Get Fields**. When the fields are retrieved, the Parquet type is converted to an appropriate PDI type, as shown in the table below. You can preview the data in the Parquet file by clicking **Preview**. You can change the Type by using the **Type** drop-down or by entering the type manually.
