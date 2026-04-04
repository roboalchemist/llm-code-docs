# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-input/select-an-engine-orc-input-step/using-orc-input-step-on-the-spark-engine/options-orc-input-spark-engine/fields-orc-input-spark-engine.md

# Fields

The **Fields** section contains the following items:

* A **Pass through fields from the previous step** option that allows you to read the fields from the input file without redefining any of the fields.
* A table defining data about the columns to read from the ORC file.

![ORC Input step](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-33094a12e8a225718433a53bf561317b118bfab7%2FPDI_OrcInput_Fields_SparkEngine.png?alt=media)

The table in the **Fields** section defines the fields to read as input from the ORC file, the associated PDI field name, and the data type of the field. Enter the information for the ORC Input step fields as shown in the following table:

| Field                   | Description                                                                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ORC path (ORC type)** | Specify the name of the field as it will appear in the ORC data file or files, and the ORC data type.                                                                                              |
| **Name**                | Specify the name of the input field.                                                                                                                                                               |
| **Type**                | Specify the data type of the input field.                                                                                                                                                          |
| **Format**              | Specify the [date format](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/common-formats) when the **Type** specified is **Date**. |

You can define the fields manually, or you can provide a path to an ORC data file and click **Get Fields** to populate all the fields. When the fields are retrieved, the ORC type is converted into an appropriate PDI type. You can preview the data in the ORC file by clicking **Preview**. You can change the PDI type by using the **Type** drop-down or by entering the type manually.
