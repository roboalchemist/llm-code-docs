# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step/input-data-etl-metadata-injection-step-example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step/input-data-etl-metadata-injection-step-example.md

# Input data

Data files are frequently uploaded from multiple sources. This example models a situation where two suppliers have uploaded spreadsheets into the `metadata-injection-example/data/in` folder.

When using metadata injection, you usually want to focus on a subset of data values common to all your input files. Metadata for the following values are used in this example:

* Transaction date
* Transaction invoice number
* Net value of the transaction
* Currency used in the transaction

The metadata for these values and the output target text file are created and maintained in the `metadata-injection-example/metadata` folder.
