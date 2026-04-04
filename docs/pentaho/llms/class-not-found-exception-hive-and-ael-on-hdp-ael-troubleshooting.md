# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/errors-when-using-hive-and-ael-on-a-hortonworks-cluster-ael-troubleshooting/class-not-found-exception-hive-and-ael-on-hdp-ael-troubleshooting.md

# Class not found exception

The "ClassNotFoundException" may occur in the AEL daemon log when using Hive and AEL on Hortonworks. This exception occurs when the HiveWarehouseSession class is not recognized by the daemon.

```
[2019-12-02 18:56:38.038] [INFO ] org.pentaho.di.engine.api.remote.ExecutionException:
[2019-12-02 18:56:38.038] [INFO ] java.lang.ClassNotFoundException: com.hortonworks.hwc.HiveWarehouseSession
[2019-12-02 18:56:38.038] [INFO ] com.hortonworks.hwc.HiveWarehouseSession

```

To resolve this issue, create a symbolic link in the `/extra` directory to the Hive Warehouse Connector Assembly and restart the daemon, as shown in the following example:

```
cd data-integration/adaptive-execution/extra
ln -s /usr/hdp/current/hive_warehouse_connector/hive-warehouse-connector-assembly-1.0.0.3.1.0.0-78.jar

```
