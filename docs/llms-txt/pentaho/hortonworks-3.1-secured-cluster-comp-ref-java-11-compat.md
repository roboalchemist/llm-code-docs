# Source: https://docs.pentaho.com/install/9.3-install/components-reference/pentaho-java-11-and-hadoop-cluster-compatibility-components-reference-cp/hortonworks-3.1-secured-cluster-comp-ref-java-11-compat.md

# Hortonworks 3.1 secured cluster

When connecting to a Hortonworks 3.1 secured cluster running in Java 8 from Pentaho running Java 11 while using the Pentaho Hortonworks 3.0 driver, the following component compatibilities apply:

* **Compatible components**

  HDFS, Avro, Parquet, ORC, HBase, Hive, HadoopExecutor\*
* **Non-compatible components**

  Sqoop, Oozie, Pig

\* Compatible as long as the source JAR is compiled with Java 8.

**Note:** The Pentaho MapReduce component was not tested.
