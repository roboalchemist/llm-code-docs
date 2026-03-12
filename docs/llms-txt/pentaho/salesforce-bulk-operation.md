# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation.md

# Salesforce bulk operation

You can use the Salesforce bulk operation step to perform bulk mutative operations (insert, update, upsert, and delete) on Salesforce objects using the Salesforce Bulk API 2.0. This is accomplished by reading data from a stream, buffering a CSV file of mutations, and then executing the bulk job on the buffered file. Upon completion, you can optionally retrieve the successful results, unprocessed records, and failed results on different output streams of the step. You must have a Salesforce Client ID and Client Secret to use this step.
