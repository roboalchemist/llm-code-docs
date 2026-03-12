# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-input/using-the-avro-input-step-on-the-pentaho-engine/options-reuse/lookup-fields-tab-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-input/options-reuse/lookup-fields-tab-reuse.md

# Lookup Fields tab

![Avro Input Lookup Fields Tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-171d2e2e7f53fe47600bc4e8c70718fdc5e096a7%2FPDI_TransStep_Avro_Input_Lookup_Fields_Tab.png?alt=media)

You can use the **Lookup Fields** tab to create variables and map them to a specific field to use as lookups into an Avro structure at decoding time. The table in this tab defines the following field properties:

| Field Property    | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| **Name**          | The name of the incoming field                                 |
| **Variable**      | The variable you want to use as the value of an incoming field |
| **Default value** | The value to use when the incoming field value is null         |

Click **Get fields** to populate the **Name** column with names of the incoming fields.
