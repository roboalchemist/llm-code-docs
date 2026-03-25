# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-input.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-input.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-input.md

# Parquet Input

The Parquet Input step decodes Parquet data formats and extracts fields using the schema defined in the Parquet source files. The Parquet Input and the [Parquet Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-output) transformation steps gather data from various sources and move that data into the Hadoop ecosystem in the Parquet format.

Before using the Parquet Input step, you must configure a named connection for your distribution, even if your **Location** is set to `Local`. For information named connections, see [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article).
