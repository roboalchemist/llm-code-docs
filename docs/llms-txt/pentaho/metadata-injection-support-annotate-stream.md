# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/metadata-injection-support-annotate-stream.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/metadata-injection-support-annotate-stream.md

# Metadata injection support

All fields of this step support metadata injection. You can use this step with [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection) to pass metadata to your transformation at runtime.

When using metadata injection with the Annotate Stream step, you can reuse shared annotation groups which already exist, but you cannot create a new shared annotation group. If you inject a shared annotation group by providing a value for **SHARED\_ANNOTATION\_GROUP**, then it is assumed that you are re-using an existing shared annotation group. As a result, any annotations defined in the ETL Metadata Injection step are ignored.
