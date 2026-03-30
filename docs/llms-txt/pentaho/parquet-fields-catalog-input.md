# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-input/general-catalog-input/fields-tab-catalog-input/parquet-fields-catalog-input.md

# Parquet fields

When Parquet data is read, the table defines the fields to read as input from the Parquet file.

![Parquet fields](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-293c0d0d7c45ad2feb7d6f01ba881c75e14a8b77%2FPDI_CatalogInput_Fields_Parquet.png?alt=media)

Enter the information for the Catalog Input step fields, as shown in the following table.

| Column                  | Description                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path**                | The name of the field as it appears in the Parquet data file, and the Parquet data type. An associated PDI field type is provided in parentheses.                                                                |
| **Name**                | The name of the input field.                                                                                                                                                                                     |
| **Type**                | The type of the input field as detected by PDI.                                                                                                                                                                  |
| **Format**              | Specify the [Date formats](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/common-formats/date-formats) when the **Type** specified is **Date**. |
| **Get Fields** (button) | Click to retrieve a list of fields derived from the source file in Data Catalog.                                                                                                                                 |

Provide a path to a Parquet data file and click **Get Fields**. When the fields are retrieved, the Parquet type is converted to an applicable PDI type, as shown in the [PDI types](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-input/general-catalog-input/fields-tab-catalog-input/parquet-fields-catalog-input/pdi-types) table. You can change the type by using the **Type** drop-down menu or by entering the type manually.
