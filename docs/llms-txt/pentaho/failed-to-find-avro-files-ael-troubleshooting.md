# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/failed-to-find-avro-files-ael-troubleshooting.md

# Failed to find AVRO files

If you are using the Spark engine with an EMR cluster, you may receive the following error message when trying to access AVRO files:

```
Failed to find data source: org.apache.spark.sql.avro.AvroFileFormat. Please find packages
        at http://spark.apache.org/third-party-projects.html
```

The libraries needed for accessing AVRO files on an EMR cluster are not included in Spark default class path. You must add them to the AEL daemon `extra/` directory.

To resolve the issue, copy the vendor-supplied data source JAR libraries on the `/usr/lib/spark/external/lib/` directory, such as "`file spark-avro_2.11_2.4.2.jar`" for example, to the AEL `extra/` directory on the daemon, as shown in the following example:

```
cp /usr/lib/spark/external/lib/spark-avro_2.22_2.4.2.jar
        $AEL_DAEMON_DIRECTORY/data-integration/adaptive-execution/extra/
```
