# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/write-metadata/options-write-metadata-step/input-tab-write-metadata-step.md

# Input tab

Use the **Input** tab to describe where a data resource ID (Data Catalog’s identification key) originates as input from within your transformation.

If your transformation only needs a specific data resource, type the ID into the **Resource ID** field. The Write Metadata step then adds new tags only to that specific data resource.

![Input tab](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-1013582a6f0e134c00b7e4c6ac098b467dc570b7%2Fpdi_write_catalog_metadata_step_input_tab_populated.png?alt=media)

If the transformation is designed to work with multiple resource IDs, they can be supplied as input from a previous step in the transformation, for example, with the Read metadata step. Specify one of the following options.

| Resource ID option                           | Description                                                                                                                         |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Accept resource ids from previous step**   | Select this option if the exact resource IDs are the incoming data from a previous step in the transformation.                      |
| **Pass through fields from previous step**   | Select this option if the resource IDs are located in a specific field that is incoming from a previous step in the transformation. |
| **Field in the input to use as resource id** | If you select **Pass through fields from previous step**, enter the name of the field that contains the resource IDs.               |
