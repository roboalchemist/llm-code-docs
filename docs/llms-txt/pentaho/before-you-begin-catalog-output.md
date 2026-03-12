# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-output/before-you-begin-catalog-output.md

# Before you begin

Before using the Catalog Output step, be aware of the following conditions:

* You must have an established **Catalog** connection to Data Catalog. For details, see [Access to Pentaho Data Catalog](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-lumada-data-catalog).
* S3 must be configured as the **Default S3 Connection** in VFS Connections to access S3 storage. For details, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser).
* You must have an established PDI connection to the cluster(s) you plan on using. For example, a Hadoop driver must be configured as a named connection for your distribution for accessing HDFS. For information on named connections, see [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article).
