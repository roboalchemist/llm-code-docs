# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/configuring-the-ael-daemon-for-hive-warehouse-connector-on-your-hortonworks-cluster/configure-the-ael-daemon-for-hive-warehouse-connector-ael-setup-specific-to-hive.md

# Configure the AEL daemon for the Hive Warehouse Connector

You need to set up the AEL daemon for the Hive Warehouse Connector (HWC).

**Note:** AEL allows you to configure either the Hive Warehouse Connector (HWC) or the JDBC driver option for cluster management. The JDBC driver option is the default configuration.

Perform the following steps.

1. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file with any text editor.
2. Set the values for your environment as shown in the following table.

| Parameter                                          | Value                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableHiveConnection`                             | Enables AEL access to Hive tables. Set this value to `true`.                                                                                                                                                                                                                          |
| `hiveMetastoreUris`                                | Identifies the location of Hive metastore. Set this value to `thrift://*&lt;fully qualified hostname&gt;*:9083`.                                                                                                                                                                      |
| `spark.sql.hive.hiveserver2.jdbc.url`              | Identifies the location of the interactive service. Use the value found at `Ambari Services > Hive > Summary > HIVESERVER2 INTERACTIVE JDBC URL`.                                                                                                                                     |
| `spark.datasource.hive.warehouse.metastoreUri`     | Identifies the location of the Hive metastore. Use the value found at `Ambari Services > Hive > CONFIGS > ADVANCED > General > hive.metastore.uris`.                                                                                                                                  |
| `spark.datasource.hive.warehouse.load.staging.dir` | Determines the HDFS temporary directory used for batch writing to Hive. Set this value to `/tmp`.**Note:** Ensure that your HWC users have permissions for this directory.                                                                                                            |
| `spark.hadoop.hive.llap.daemon.service.hosts`      | Specifies the name of the LLAP queue. Use the value found at `Ambari Services > Hive > CONFIGS > ADVANCED > Advanced hive-interactive-site > hive.llap.daemon.service.hosts`.                                                                                                         |
| `spark.hadoop.hive.zookeeper.quorum`               | Provides the Hive endpoint to access the Hive tables. Use the value found at `Ambari Services > Hive > CONFIGS > ADVANCED > Advanced hive-site > hive.zookeeper.quorum`.                                                                                                              |
| `spark.driver.extraClassPath`                      | Specifies the path to the directory containing the `hive-site.xml` file on the driver node. It causes the `hive-site.xml` file to be loaded as a resource in the driver. This resource defines the Hive endpoints and security setting required by AEL to access the Hive subsystem.  |
| `spark.executor.extraClassPath`                    | Specifies the path to the directory containing the `hive-site.xml` on the executor nodes. It causes the `hive-site.xml` file to be loaded as a resource on each executor. This resource defines the Hive endpoints and security setting required by AEL to access the Hive subsystem. |

The following lines of code show sample values for these parameters:

````
```
# AEL Spark Hive Property Settings
enableHiveConnection=true
spark.driver.extraClassPath=/usr/hdp/current/spark2-client/conf/
spark.executor.extraClassPath=/usr/hdp/current/spark2-client/conf/
spark.sql.hive.hiveserver2.jdbc.url=jdbc:hive2://hito31-n3.cs1cloud.internal:2181,hito31-n2.cs1cloud.internal:2181,hito31-n1.cs1cloud.internal:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2-interactive
spark.datasource.hive.warehouse.metastoreUri=thrift://hito31-n2.cs1cloud.internal:9083
spark.datasource.hive.warehouse.load.staging.dir=/user/devuser/tmp
spark.hadoop.hive.llap.daemon.service.hosts=@llap0
spark.hadoop.hive.zookeeper.quoruma=hito31-n3.cs1cloud.internal:2181,hito31-n2.cs1cloud.internal:2181,hito31-n1.cs1cloud.internal:2181
```
````

3\. Save and close the file.

4. Create a symbolic link to the HWC JAR file in the `/data-integration/adaptive-execution/extra` directory. For example, if you are in the `extra` directory, the following command creates this link:

   ```
   ln -s /usr/hdp/current/hivewarehouseconnector/hive-warehouse-connector-assembly-1.0.0.3.1.0.0-78.jar/<user_name>/data-integration/adaptive-execution/extra/
   ```
5. Save and close the file.
6. Restart the AEL daemon.
7. [Stop, then start the Pentaho Server](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration).

You can use PDI with a **Hive Warehouse Connector** database connnection.
