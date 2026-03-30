# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/access-the-apache-hadoop-driver-work-with-data-connecting-to-hadoop-cluster-with-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/access-the-apache-hadoop-driver-work-with-data-connecting-to-hadoop-cluster-with-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/access-the-apache-hadoop-driver-work-with-data-connecting-to-hadoop-cluster-with-pdi-client.md

# Using the pre-installed Apache Hadoop driver

You can access and use the installed Apache Hadoop driver for HDFS copy file operations as well as for executing input and output transformations and jobs. The driver works with both secure and unsecured clusters. Because the driver pre-installed, you do not have to install a KAR file.

The supported big data steps in Pentaho include:

* [Avro Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-input)
* [Avro Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-output)
* [ORC Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/orc-input)
* [ORC Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/orc-output)
* [Parquet Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-input)
* [Parquet Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-output)

Both operating system file browsers and the Pentaho virtual file system browsers are supported, as well as basic HDFS and VFS operations. For more information, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser).

**Note:** Only Hadoop clusters that conform with standard Hadoop connection rules work with the Apache Hadoop Driver. For example, while EMR clusters may work, MapR does not work with this driver because the connection rules for MapR are not standard. The Apache Hadoop Driver is not intended to support higher level Hadoop operations such as Hive, HBase, Sqoop, and Oozie. If you require these operations, install the KAR file for the applicable vendor.
