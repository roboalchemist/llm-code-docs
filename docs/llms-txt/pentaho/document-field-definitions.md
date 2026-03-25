# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/mongo-document-fields-tab/example/document-field-definitions.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/mongo-document-fields-tab/example/document-field-definitions.md

# Document field definitions

| Name    | Mongo document path | Use field name | NULL values | JSON | Match field for update | Modifier operation | Modifier policy |
| ------- | ------------------- | -------------- | ----------- | ---- | ---------------------- | ------------------ | --------------- |
| first   | top1                | Y              |             | N    | N                      | N/A                | lnsert\&Update  |
| last    | array\[O]           | Y              |             | N    | N                      | N/A                | lnsert\&Update  |
| address | array\[O]           | Y              |             | N    | N                      | N/A                | lnsert\&Update  |
| age     | array\[O]           | Y              |             | N    | N                      | N/A                | lnsert\&Update  |
