# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster.md

# Set up Pentaho to connect to a Hadoop cluster

For IT administrators, who need to configure Pentaho to connect to a Hadoop cluster for teams working with Big Data, you can set up Pentaho to connect to Amazon Elastic MapReduce (EMR), Azure HDInsight (HDI), Cloudera Distribution for Hadoop (CDH) and Cloudera Data Platform (CDP), Google Dataproc, and Hortonworks Data Platform (HDP). Pentaho also supports related services such as HDFS, HBase, Hive, Oozie, Sqoop, Yarn/MapReduce, ZooKeeper, and Spark. You can connect to clusters and services from these Pentaho components:

* PDI client (Spoon), along with Kitchen and Pan command line tools
* Pentaho Server
* Analyzer (PAZ)
* Pentaho Interactive Reports (PIR)
* Pentaho Report Designer (PRD)
* Pentaho Metadata Editor (PME)

You can configure the Pentaho Server to connect to a Hadoop cluster through a compatibility layer called a driver. Pentaho regularly develops and releases new drivers, so you can stay up-to-date with the latest technological developments. To view which drivers are supported for this version of Pentaho, see the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference).

When drivers for new Hadoop versions are released, you can download them from the [Hitachi Vantara Lumada and Pentaho Support Portal](https://support.pentaho.com/hc/en-us) and then add them to Pentaho to connect to the new Hadoop distributions. For more information about downloading and adding a new driver, see [Adding a new driver](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/adding-a-new-driver-to-pentaho).

**Note:** Pentaho ships with a generic Apache Hadoop driver. For specific vendor drivers, visit the [Hitachi Vantara Lumada and Pentaho Support Portal](https://support.pentaho.com/hc/en-us) to download the drivers.

Before you can add a named connection to a cluster, you must install a driver for the vendor and version of the Hadoop cluster that you are connecting to.
