# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-input/using-the-avro-input-step-on-the-pentaho-engine/options-reuse/source-tab-kettle-engine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-input/options-reuse/source-tab-kettle-engine.md

# Source tab

![Avro Input step Source tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-26e101d5505b7096adf7ff1f8c92b21a3468b142%2FPDI_AvroInput_SourceTab_PentahoEngine.png?alt=media)

Use the **Source** tab to specify the location of the source data and its related schema. The schema that defines the Avro data is either embedded or in a different location.

Use **Format** to select from one of the following formats:

* **Avro file**

  The source material is in a single location. The schema is embedded with the data.
* **JSON datum**

  The source material is in different locations. The data is contained in a JSON format, and the schema is separate from the data.
* **Binary datum**

  The source material is in different locations. The data is contained in a binary format, and the schema is separate from the data.
* **Avro file (use alternate schema)**

  The source material is in different locations. The schema is separate from the data.

The options presented in the **Source** tab depend on whether the schema is embedded with or separate from the data.
