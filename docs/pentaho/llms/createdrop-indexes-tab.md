# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/createdrop-indexes-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/createdrop-indexes-tab.md

# Create/drop indexes tab

![MongoDB Output Create or drop indexes tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-250815400218c9dc43c3c0ca3a0d108468c8de4f%2FPDI_TransStep_MongoDB_Output_Create-Drop_Indexes_Tab.png?alt=media)

Use the **Create/drop indexes** tab to create and drop [indexes](http://www.mongodb.org/display/DOCS/Indexes) on one or more fields. Unless unique indexes are being used, MongoDB allows duplicate records to be inserted. Indexing is performed after all rows have been processed by the step.

Enter the following information in the transformation step fields:

| Field            | Description                                                                                                                                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Index fields** | Specify a single index (using one field) or a compound index (using multiple fields). Compound indexes are specified by a comma-separated list of paths. Use dot notation to specify the path to a field to use in the index. An optional direction indicator can be specified: `1` for ascending or `-1` for descending. |
| **Index opp**    | Specify whether to create or drop an index.                                                                                                                                                                                                                                                                               |
| **Unique**       | Specify whether to index only fields with unique values.                                                                                                                                                                                                                                                                  |
| **Sparse**       | Specify whether to index only documents that have the indexed field.                                                                                                                                                                                                                                                      |
| **Show indexes** | Click **Show indexes** to display a list of existing indexes.                                                                                                                                                                                                                                                             |
