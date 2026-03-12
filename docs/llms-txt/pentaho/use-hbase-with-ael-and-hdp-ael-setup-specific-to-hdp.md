# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hortonworks/use-hbase-with-ael-and-hdp-ael-setup-specific-to-hdp.md

# Use HBase with AEL and HDP

To use HBase with AEL and HDP, you must add the HBase JAR files to PDI.

Perform the following steps to add the HBase JAR files:

1. Copy the following files for your version of HDP from the `/usr/hdp/current/hbase/lib/` directory of your cluster.
   * `hbase-client-*&lt;x.x.x&gt;*.jar`
   * `hbase-common-*&lt;x.x.x&gt;*.jar`
   * `hbase-hadoop-compat-*&lt;x.x.x&gt;*.jar`
   * `hbase-mapreduce-*&lt;x.x.x&gt;*.jar`
   * `hbase-protocol-*&lt;x.x.x&gt;*.jar`
   * `hbase-protocol-shaded-*&lt;x.x.x&gt;*.jar`
   * `hbase-server-*&lt;x.x.x&gt;*.jar`
   * `hbase-shaded-miscellaneous-*&lt;x.x.x&gt;*.jar`
   * `hbase-shaded-netty-*&lt;x.x.x&gt;*.jar`
   * `hbase-shaded-protobuf-*&lt;x.x.x&gt;*.jar`
2. Follow the instructions for setting up vendor-specified JARs in the **Pentaho Data Integration** document to install the files.
