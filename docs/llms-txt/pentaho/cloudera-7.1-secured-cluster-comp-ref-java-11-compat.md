# Source: https://docs.pentaho.com/install/9.3-install/components-reference/pentaho-java-11-and-hadoop-cluster-compatibility-components-reference-cp/cloudera-7.1-secured-cluster-comp-ref-java-11-compat.md

# Cloudera 7.1 secured cluster

When connecting to a Cloudera 7.1 secured cluster running in Java 8 from Pentaho running Java 11 while using the Pentaho Cloudera 7.1 driver, the following component compatibilities apply:

* **Compatible components**

  HDFS, Avro, Parquet, ORC, HBase, Hive, HadoopExecutor\*, Oozie, Pig, Pentaho MapReduce
* **Non-compatible components**

  Sqoop

\* Compatible as long as the source JAR is compiled with Java 8.
