# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/metadata-injection-support-copybook-input-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/metadata-injection-support-copybook-input-step.md

# Metadata injection support

All fields of this step support metadata injection. You can use this step with [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection) to pass metadata to your transformation at runtime.

Use the [Read metadata from Copybook](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook) step to read copybook definition files and obtain the required mapping information to inject fields. In addition to the **Name**, **Path**, **Dest Type**, and **Conversion**, a decimal precision must be provided.
