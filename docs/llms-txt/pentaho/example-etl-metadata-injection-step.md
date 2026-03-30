# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step.md

# Example

In this example, you have a template transformation to load transaction data values from a supplier’s spreadsheet, filter specific values to examine, and output them to a text file. The template transformation is injected with metadata values stored in Microsoft spreadsheets.

The example is in the `pentaho/design-tools/data-integration/samples/transformations/metadata-injection-example` folder of your PDI distribution. The folder contains the following structure:

![Metadata injection example folder strucutre](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b4a8dbca30dcfea1bd59e60d227d1df7cacbf280%2FMDI%20example%20-%20sample%20folder%20structure.png?alt=media)

Microsoft spreadsheets containing input data are stored in the `metadata-injection-example/data/in` folder. Metadata values are stored in spreadsheets within the `metadata-injection-example/metadata` folder. The template and the transformation for injecting the metadata are in the `metadata-injection-example/transformations` folder.

**Note:** This example assumes a basic understanding of [working with transformations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp) and steps.
