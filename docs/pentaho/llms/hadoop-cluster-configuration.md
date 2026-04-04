# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/options-pentaho-mapreduce-job/cluster-tab/hadoop-cluster-configuration.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/options-pentaho-mapreduce-job/cluster-tab/hadoop-cluster-configuration.md

# Hadoop cluster configuration

When you click the **Edit** or **New** buttons next to the**Hadoop Cluster** field, the Hadoop cluster dialog box appears. Use this dialog box to specify configuration details such as host names and ports for HDFS, Job Tracker, and other big data cluster components. These configuration options are reused in the related transformation steps and job entries that support big data features.

| Option                                   | Definition                                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Cluster Name**                         | Enter the name that you assign the cluster configuration.                                                                                                                |
| **Hostname** (in **HDFS** section)       | Enter the hostname for the HDFS node in your Hadoop cluster.                                                                                                             |
| **Port** (in **HDFS** section)           | Enter the port for the HDFS node in your Hadoop cluster.                                                                                                                 |
| **Username** (in **HDFS** section)       | Enter the username for the HDFS node.                                                                                                                                    |
| **Password** (in **HDFS** section)       | Enter the password for the HDFS node.                                                                                                                                    |
| **Hostname** (in **JobTracker** section) | Enter the hostname for the JobTracker node in your Hadoop cluster. If you have a separate job tracker node, type in the hostname here. Otherwise, use the HDFS hostname. |
| **Port** (in **JobTracker** section)     | Enter the port for the JobTracker in your Hadoop cluster. Job tracker port number cannot be the same as the HDFS port number.                                            |
| **Hostname** (in **ZooKeeper** section)  | Enter the hostname for the Zookeeper node in your Hadoop cluster.                                                                                                        |
| **Port** (in **Zookeeper** section)      | Enter the port for the Zookeeper node in your Hadoop cluster.                                                                                                            |
| **URL** (in **Oozie** section)           | Enter a URL of a valid Oozie location.                                                                                                                                   |

After you have finished setting these configuration options, perform the following steps:

1. Click **Test** to try your configurations on the Hadoop cluster. If you are unable to connect, see [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article) for further details on Hadoop cluster connections.
2. Click **OK** to return to the **Cluster** tab.
