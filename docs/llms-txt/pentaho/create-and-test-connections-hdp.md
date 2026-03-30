# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/connect-other-pentaho-components-to-the-hortonworks-cluster/create-and-test-connections-hdp.md

# Create and test connections

For each Pentaho component, create the test as described in the following list.

* **Pentaho Server for DI**

  Create a transformation in the PDI client and run it remotely.
* **Pentaho Server for BA**

  Create a connection to the cluster in the Data Source Wizard.
* **PME**

  Create a connection to the cluster in PME.
* **PRD**

  Create a connection to the cluster in PRD.

After you have connected to the cluster and its services properly, provide connection information to users who need access to the cluster and its services. Those users can only obtain access from machines that are properly configured to connect to the cluster.

Here is what users need to connect:

* Hadoop Distribution and version of the cluster
* HDFS, JobTracker, ZooKeeper, and Hive2/Impala Hostnames, IP addresses and port numbers
* Oozie URL (if used)

Users also require the permissions to access the directories they need on HDFS, such as their home directory and any other required directories.

Users might also require more information for specific job entries, transformation steps, and services. [Here's a more detailed list of information that your users might need from you](https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list).
