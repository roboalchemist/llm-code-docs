# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/output-tab-elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/output-tab-elasticsearch-rest-bulk-insert.md

# Output tab

![Elasticsearch REST Bulk Insert step, Output tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8ab5ded1552c5146940de20e024ddc56dc35866%2FPDI_ElasticsearchRESTbulkInsert_OutputTab.png?alt=media)

Use the **Output** tab configure the output of the step and error handling.

Select from the following **Index Settings** options for the field identifier and index handling.

| Field                   | Description                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID Field**            | (Optional) Enter a value that identifies the document indexed in Elasticsearch. If you do not enter a value, Elastic generates an ID automatically.                                                                                   |
| **Overwrite if exists** | When selected and the **ID Field** is specified, updates a document index if the ID exists in the target Elastic index. If the destination ID does not exist in the index, then the new document index is added to the Elastic index. |

Select from the following \*\*Step Settings\*\* options to specify how row data and errors are processed.

| Field               | Description                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stop on error**   | Stop processing if there is an error, such as a problem with adding the document or the bulk push to the index or if the JSON is not well-formed. If this option is not selected, and an error occurs, the row is not processed, but the transformation keeps running so that other rows are processed.                                                       |
| **Output rows**     | Select to pass through the input row data as well as a new output document index ID if the **ID Output Field** value is specified. If you select **Stop on Error**, the rows that were successful up until the time the error occurs are sent to the next step or the output. Otherwise, rows successfully processed are sent to the next step or the output. |
| **ID Output Field** | (Optional) Enter the name of the ID field to output newly indexed document IDs. If this is left blank, the value in the **ID Field** is used.                                                                                                                                                                                                                 |

Select from the following **Batch Settings** options to set the number of rows and timeout value.

| Field       | Description                                                                                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Size**    | Specify the number of items in a batch. Specify a size greater than one to perform a bulk insert. A size of one does not perform a bulk insert.                                      |
| **Timeout** | Specify a value and unit of measure to configure the maximum allowable period for the bulk request to process on the Elastic server before the batch times out, and processing ends. |
