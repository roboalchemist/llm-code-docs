# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/errors-when-using-hive-and-ael-on-a-hortonworks-cluster-ael-troubleshooting/hive-database-does-not-exist-hive-and-ael-on-hdp-ael-troubleshooting.md

# Hive database does not exist

The "Hivedb does not exist" exception may occur in the AEL daemon log when using Hive and AEL on Hortonworks. To clear this exception, you must set extra properties for the AEL daemon.

```
2019/12/04 16:42:01 - Table input.0 - ERROR (version 9.0.0.0-332, build 9.0.0.0-332 from
      2019-11-25 11.19.55 by buildguy) : org.pentaho.di.engine.api.remote.ExecutionException: hivedb
      does not exist. Check your Hive in application.properties.
```

To resolve this issue, set the required properties as shown in the following example:

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

You can find the value for the key in the `application.properties` file list for Ambari.
