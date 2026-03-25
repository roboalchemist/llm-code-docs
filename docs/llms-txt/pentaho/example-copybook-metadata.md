# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook/example-copybook-metadata.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook/example-copybook-metadata.md

# Example

In this example, we are using the `accounts.cbl` sample copybook definition file available in the `design-tools/data-integration/samples/transformations/copybook/redefines_example/accounts.cbl` directory.

![Sample copybook definition file](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6c44df8a83503caaae5204d71537b48bd610ddcf%2FPDI_ReadMetadataFromCopybook_Example.png?alt=media)

The **Standard columns (6 to 72)** option was selected to match the file format. The **Extract parent groups** option was selected to include the group information. The following image shows how the data displays in the PDI stream after running the transformation using the sample file.

![Step output to PDI stream](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-eda0987cf8773742d827f7ba06c16f67bccd7976%2FPDI_TransStep_Read_metadata_from_Copybook_Output_results.png?alt=media)

The **field\_kettle\_type** column displays the data types that are generated to the PDI stream.
