# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-streaming-optimization.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-streaming-optimization.md

# Apply streaming optimization

This optimization technique limits the batch size used for processing.

The records of the streaming Pentaho Data Service are partitioned into windows (batches) for processing. How the records are batched depends on the window mode you choose. A window can be time-based or row-based. A time-based window is created within a specified interval of time. A row-based window is created per a specified number of rows collected for processing.
