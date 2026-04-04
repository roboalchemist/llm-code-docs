# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/metadata-injection-support-sdr-shared-dimension.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/metadata-injection-support-sdr-shared-dimension.md

# Metadata injection support

All fields of this step support metadata injection. You can use this step with [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection) to pass metadata to your transformation at runtime.

When using metadata injection with the Shared Dimension step, the system will load the currently defined annotations in the shared dimension step, whether or not the shared dimension name is a match. The new set of annotations are saved to the transformation and in the metastore. If a shared dimension with the same name already exists in the metastore, it will be overwritten with the new shared dimension.
