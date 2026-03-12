# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list.md

# Hadoop connection and access information list

After your [Hadoop cluster has been configured](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster), users need some information and permissions to connect to the cluster and access its services.

### Pentaho

You'll need read access to the following Pentaho directories:

* Pentaho Server, Spoon, PRD, and PME directories for cluster drivers
* Pentaho log directories

### Hadoop cluster

You'll need to know this information about your Hadoop Cluster. You can get these things from your Hadoop administrator or the Hadoop Cluster Management tool.

* Installed version
* Hostname and IP address for each cluster node, including Yarn servers
* If your cluster is enabled for High Availability, you will also need the name of the nameservice, (DNS lookup table)

### Optional Services

If you are going to use the following services, you'll need this information.

#### HDFS

Your Hadoop administrator should be able to provide this information:

* Hostname/IP address, Namenode Port and Namenode Web Console Port
* Paths to directories that will be used
* Owners for the various data sets in HDFS
* If S3 is used, you'll need the access key and secret key

You will also need permission to access to the directories you need.

#### Hive2 and Impala

Check with your Hadoop administrator or the Hadoop Cluster Management Console for:

* Username (and password) the service will run under
* Hostname, IP address, and port
* JDBC URL (you must use the thrift interface)

#### HBase

See your Hadoop administrator or the Hadoop Cluster Management Console to get information on:

* Zookeeper connection hostname
* Zookeeper connection port

#### Oozie

Check your Hadoop administrator or the Hadoop Cluster Management Console to get the:

* URL to Oozie web interface
* Jobtracker Hostname/IP and port number (or Resource Manager Hostname/IP and port number)
* Namenode Hostname/IP and port number

#### Pentaho MapReduce (PMR)

See your Hadoop administrator or the Hadoop Cluster Management Console to get information on:

* Job History Server IP and Port
* Jobtracker Hostname/IP and port number (or Resource Manager Hostname/IP and Port number)
* Hostname/IP Address, Namenode Port and Namenode Web Console Port

#### Sqoop

Get this information from your IT administrator:

* JDBC Connection details for target or source databases
* JDBC Drivers
* Jobtracker Hostname/IP and Port number (or Resource Manager Hostname/IP and Port number)
* Hostname/IP Address, Namenode Port and Namenode Web Console Port

Get this information from the PDI Developer or Database Administrator:

* Username used to access HDFS

#### Spark

Get this information from the Hadoop Administrator:

* Master URL
* Spark Client Location
* Jobtracker Hostname/IP and Port number (or Resource Manager Hostname/IP and Port number)
* Hostname/IP Address, Namenode Port and Namenode Web Console Port
* Job History Server IP and Port

#### Zookeeper

Get this information the Hadoop Cluster Management Console or the Hadoop Administrator:

* Hostname or IP Address
* Port
