# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster.md

# Advanced settings for connecting to an Amazon EMR cluster

The following advanced settings are also available while you are configuring the Pentaho Server to connect to a working Amazon EMR cluster.

**Note:** EMR clusters (version 7.x and later) built with JDK 17 exclude the `commons-lang-2.6.jar` library from their standard Hadoop library directories (`$HADOOP_HOME/lib`). To use the EMR driver for EMR 7.x, obtain the `commons-lang-2.6.jar` file from a trusted source, such as the official Maven repository ([Maven Repository: commons-lang » commons-lang » 2.6](https://mvnrepository.com/artifact/commons-lang/commons-lang/2.6)). Then manually copy the downloaded JAR file to the `$HADOOP_HOME/lib` or `$HADOOP_MAPRED_HOME/lib` directory on each node within the EMR cluster to ensure that all worker nodes have access to the library.
