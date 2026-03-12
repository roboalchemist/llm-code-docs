# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster.md

# Configuring AEL with Spark in a secure cluster

The AEL daemon works in an unsecured cluster by default. You can secure communication channels between the PDI client and the AEL daemon server and also between the AEL daemon server and the Spark driver using SSL (Secure Sockets Layer), Kerberos, or both. If your AEL daemon server and your cluster machines are in a secure environment like a data center, you may only want to configure a secure connection between the PDI client and the AEL daemon server.

**Note:** Because of limitations for CDS Powered by Apache Spark in CDH 6.x, AEL does not support Hive or Impala in YARN mode. If you would like specific information, see the [Cloudera documentation](https://docs.cloudera.com).
