# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/before-you-begin/spark-client-cp/spark-client-already-on-a-cluster.md

# Use a Spark client already installed on a cluster

To use a Spark client that already resides on a cluster, specify the cluster path in the **sparkHome=** parameter in the `application.properties` file. For example:

**sparkHome=/cluster\_path/spark-2.4.5-bin-hadoop2.7/**

where `cluster_path` is your specific path.

The Spark client is started as part of the AEL execution and does not require any manual startup. The following examples show common cluster configurations.

| Cluster Configuration | Example Entry                                                                 |
| --------------------- | ----------------------------------------------------------------------------- |
| CDH 6.1               | **sparkHome=/opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/lib/spark/** |
| CDH 6.2               | **sparkHome=/opt/cloudera/parcels/CDH-6.2.0-1.cdh6.2.0.p0.967373/lib/spark/** |
| EMR 5.24              | **sparkHome=/usr/lib/spark/**                                                 |
| GDP 1.4.2.1           | **sparkHome=/usr/lib/spark/**                                                 |
| HDP 3.1               | **sparkHome=/usr/hdp/current/spark2-client**                                  |
