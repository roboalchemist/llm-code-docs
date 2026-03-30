# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection.md

# ETL metadata injection

The ETL Metadata Injection step inserts data from multiple sources into another transformation at runtime. This insertion reduces the need to call repetitive tasks each time a different input source is used.

In PDI, you can create a transformation to use as a template for your repetitive tasks. This transformation is known as the template transformation. The template transformation is a child transformation that is reused by the ETL Metadata Injection step with the metadata created from various input sources. You will create another transformation to prepare what common values you want to use as metadata and inject these selected values through the ETL Metadata Injection step into your template transformation, as shown in the following diagram:

![ETL Metadata Injection Process](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b8ea6d63f472773af4524509fa2c6d90e150a7bf%2FPDI_TransStep_ETL_Metadata_Injection_Process.png?alt=media)

For example, you might have a simple transformation to load transaction data values from a supplier, filter specific values, and output them to a file. If you have more than one supplier, you would need to run this simple transformation for each supplier. Yet, with metadata injection, you can expand this simple repetitive transformation by inserting metadata from another transformation that contains the ETL Metadata Injection step. The ETL Metadata Injection step coordinates the data values from the various inputs through the metadata you define. This process reduces the need for you to adjust and run the repetitive transformation for each specific input. See the [Example](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step) section for more details on the example.

The following basic procedure is recommended for using this step to inject metadata:

1. Optimize your data for injection, such as preparing folder structures and inputs.
2. Develop transformations for the following task:
   * The repetitive process (the template transformation)
   * Metadata injection through the ETL Metadata Injection step
   * Handling of multiple inputs (as needed)

The metadata is injected into the template transformation through any step that supports metadata injection. See [Steps supporting metadata injection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/steps-supporting-metadata-injection) for which steps support metadata injection.
