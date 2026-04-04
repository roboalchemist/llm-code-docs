# Source: https://docs.pentaho.com/install/9.3-install/components-reference/pentaho-java-11-and-hadoop-cluster-compatibility-components-reference-cp/cloudera-6.3-secured-cluster-comp-ref-java-11-compat.md

# Cloudera 6.3 secured cluster

When connecting to a Cloudera 6.3 secured cluster running in Java 8 from Pentaho running Java 11 while using the Pentaho Cloudera 7.1 driver, the following component compatibilities apply:

* **Compatible components**

  HDFS, Avro, Parquet, ORC, Oozie, Pig, Pentaho MapReduce
* **Non-compatible components**

  HBase, Hive, HadoopExecutor, Sqoop

When connecting to a Cloudera 6.3 secured cluster running in Java 8 from Pentaho running Java 11 while using the Pentaho Cloudera 6.1 driver, the following component compatibilities apply:

* **Compatible components**

  HDFS, Avro, Parquet, ORC, HBase, Hive, HadoopExecutor, Oozie, Pentaho MapReduce
* **Non-compatible components**

  Sqoop, Pig
