# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/document-tab-elasticsearch-rest-bulk-insert/creating-a-document-to-index-with-stream-field-data-elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/document-tab-elasticsearch-rest-bulk-insert/creating-a-document-to-index-with-stream-field-data-elasticsearch-rest-bulk-insert.md

# Creating a document to index with stream field data

![Elasticsearch REST Bulk Insert step, Document tab - Create index option](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-4bbae0fec862112cbf42f63e93e840a0b58f9212%2FPDI_ElasticsearchRESTbulkInsert_DocumentTab.png?alt=media)

Use the **Create a document to index with stream field data** option if you want to turn each row of stream data into a unique JSON document to be indexed in the bulk request. You must define the fields to use from the input stream with a target name. Click **Get Fields** to automatically find all incoming stream data.

| Field           | Description                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| **Name**        | Enter the name of the source field that the step receives on the input stream.                            |
| **Target name** | Enter the name of the destination field in the generated JSON document to use for the input stream field. |
