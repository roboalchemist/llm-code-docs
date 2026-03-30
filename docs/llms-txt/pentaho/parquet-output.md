# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-output.md

# Parquet Output

The Parquet Output step allows you to map PDI fields to fields within data files and choose where you want to process those files, such as on HDFS. For big data users, the [Parquet Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-input) and Parquet Output steps enable you to gather data from various sources and move that data into the Hadoop ecosystem in the Parquet format.

Before using the Parquet Output step, you will need to configure a named connection for your distribution, even if your **Location** is set to *Local*. For information on named connections, see [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article).
