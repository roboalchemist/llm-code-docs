# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser/general/target-fields-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser/general/target-fields-table.md

# Target fields table

![Target fields table in Row denormaliser](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-35f77795ff50e8ade8681bbddb535ee1beeb28fa%2FPDITransStep_RowDenormaliser_TargetFieldsTable.png?alt=media)

Use the **Target fields** table to select the fields to denormalize by specifying the String value for the **Key field**. Options are provided to convert data types. Strings are most common as key-value pairs so you must often convert to Integer, Number or Date. If you get key-value pair collisions (key is not unique for the group specified), specify the aggregation method to use. You can click **Get lookup fields** to retrieve fields from the PDI data stream.
