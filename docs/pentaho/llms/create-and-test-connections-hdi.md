# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/connect-other-pentaho-components-to-hdi-hdi/create-and-test-connections-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/connect-other-pentaho-components-to-hdi-hdi/create-and-test-connections-hdi.md

# Create and test connections for other Pentaho components

For each Pentaho component, create the test as described in the following list.

* **Pentaho Server for DI**

  Create a transformation in the PDI client and run it remotely.
* **Pentaho Server for BA**

  Create a connection to HDI in the Data Source Wizard.
* **PME**

  Create a connection to HDI in PME.
* **PRD**

  Create a connection to HDI in PRD.

After you have properly connected to HDI and its services, provide the connection information to your users who need access to the platform and its services.

Users need the following information and permissions to connect:

* Distribution and version of CDP
* HDFS, JobTracker, ZooKeeper, and Hive2/Impala hostnames, IP addresses, and port numbers
* Oozie URL (if used)
* Permissions to access the directories that they need on HDFS, including their home directory and any other required directories.

Additionally, users might need more information depending on the transformation steps, job entries, and services they use. See [Hadoop connection and access information list](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list).
