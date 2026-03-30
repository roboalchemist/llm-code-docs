# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/query-hcp/options-query-hcp/query-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/query-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/query-hcp/options-query-hcp/query-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/query-tab.md

# Query tab

![MongoDB Input Query tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-91849ac23657ac0ea14b07fe04be32ff20056d18%2FPDI_MongoDB_Input_Query_tab.png?alt=media)

Use the **Query** tab to refine read requests. This tab operates in two different query modes:

* **Query expression** mode (default)
* **Aggregation pipeline specification** mode.

The **Query is aggregation pipeline** option toggles between these two modes. The **Query expression** uses MongoDB’s JSON-like query language with [query operators](https://docs.mongodb.com/manual/reference/operator/query/) to perform query operations. The **Aggregation pipeline specification** field uses MongoDB’s [aggregation framework](http://docs.mongodb.org/manual/applications/aggregation/) to transform and combine documents in a collection. An aggregation pipeline connects several [pipeline expressions](https://docs.mongodb.com/manual/core/aggregation-pipeline/#pipeline-expressions) together, with the output of the previous expression becoming the input for the next.

Enter the following information in the **Query** fields:

| Fields/Option                                 | Definition                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Query expression (JSON)**                   | Enter a query expression in this field to limit the output.                                                                                                                                                                                                                                                                                       |
| **Aggregation pipeline specification (JSON)** | Select the **Query is aggregation pipeline** option to display the **Aggregation pipeline specification (JSON)** field. Then enter a pipeline expression to perform aggregations or selections. The method name, including the collection name of the database you selected in the **Input Options** tab, appears after the label for this field. |
| **Query is aggregation pipeline**             | Select this option to use the aggregation pipeline framework.                                                                                                                                                                                                                                                                                     |
| **Allow disk use**                            | Select this option to turn on the **allowDiskUse** property so that you can process aggregation pipeline data when it exceeds the standard 100MB RAM allocation.                                                                                                                                                                                  |
| **Execute for each row**                      | Select this option to perform the query on each row of data.                                                                                                                                                                                                                                                                                      |
| **Fields expression (JSON)**                  | Enter an argument to control the projection (fields to return) from a query. If empty, all fields are returned. This field is only available for query expressions.                                                                                                                                                                               |
