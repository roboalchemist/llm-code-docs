# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-output/select-an-engine-orc-output-step/using-orc-output-step-on-pentaho-engine/options-orc-output-reuse/fields-tab-orc-output-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/orc-output/options-orc-output-reuse/fields-tab-orc-output-kettle.md

# Fields tab

![ORC Output step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-abc64ce2a33e90dae85b13d26ca6cac792bafc36%2FPDI_OrcOutput_Fields_PentahoEngine.png?alt=media)

In the **Fields** tab, you can define fields that make up the **ORC type** description created by this step. The table below describes each of the options for configuring the **ORC type** description.

| Field             | Description                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| **ORC path**      | Specify the name of the field as it will appear in the ORC data file or files.                                        |
| **Name**          | Specify the name of the PDI field.                                                                                    |
| **ORC type**      | Defines the data type of the field.                                                                                   |
| **Precision**     | Specify the total number of digits in the number (only applies to the Decimal ORC type). The default value is 20.     |
| **Scale**         | Specify the number of digits after the decimal point (only applies to the Decimal ORC type). The default value is 10. |
| **Default value** | Specify the default value of the field if it is null or empty.                                                        |
| **Null**          | Specifies if the field can contain null values.                                                                       |

To avoid a transformation failure, make sure the **Default value** field contains values for all fields where **Null** is set to `No`.

You can define the fields manually, or you can provide a path to the PDI data stream and click **Get Fields** to populate all the fields. During the retrieval of the fields, a PDI type is converted to an applicable ORC type, as shown in the table below. You can also change the selected ORC type by using the **Type** drop-down or by entering the type manually.
