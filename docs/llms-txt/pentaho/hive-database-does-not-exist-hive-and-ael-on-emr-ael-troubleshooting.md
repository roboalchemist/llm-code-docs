# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/errors-when-using-hive-and-ael-on-an-amazon-emr-cluster-ael-troubleshooting/hive-database-does-not-exist-hive-and-ael-on-emr-ael-troubleshooting.md

# Hive database does not exist

If the following exception occurs in the AEL daemon log when using Hive and AEL on Amazon EMR, you must set extra properties for the AEL daemon.

```
2019/12/04 16:42:01 - Table input.0 - ERROR (version 9.0.0.0-332, build 9.0.0.0-332 from
      2019-11-25 11.19.55 by buildguy) : org.pentaho.di.engine.api.remote.ExecutionException: hivedb
      does not exist. Check your Hive in application.properties.
```

To resolve this issue, set the **enableHiveConnection** property in the `application.properties` file to `true` and verify that the **extraClassPath** property is set as shown in the following example:

```
# AEL Spark Hive Property Settings
enableHiveConnection=true
spark.driver.extraClassPath=/etc/spark/conf.dist/
spark.executor.extraClassPath=/etc/spark/conf.dist/

```

Restart the AEL daemon after you have saved the above changes.
