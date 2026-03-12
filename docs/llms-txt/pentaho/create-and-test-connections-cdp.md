# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/connect-other-pentaho-components-to-the-cdp-cluster/create-and-test-connections-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/connect-other-pentaho-components-to-the-cdp-cluster/create-and-test-connections-cdp.md

# Create and test connections for other Pentaho components

For each Pentaho component, create the test as described in the following list.

* **Pentaho Server for DI**

  Create a transformation in the PDI client and run it remotely.
* **Pentaho Server for BA**

  Create a connection to CDP in the Data Source Wizard.
* **PME**

  Create a connection to CDP in PME.
* **PRD**

  Create a connection to CDP in PRD.

After you have properly connected to CDP and its services, provide connection information to your users who need access to the platform and its services.

Users need the following information and permissions to connect:

* Distribution and version of CDP
* HDFS, JobTracker, ZooKeeper, and Hive2/Impala Hostnames, IP addresses and port numbers
* Oozie URL (if used)
* Permissions to access the directories they need on HDFS, including their home directory and any other required directories.

Additionality, users might need more information depending on the transformation steps, job entries, and services they use. [Here's a more detailed list of information that your users might need from you](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list).
