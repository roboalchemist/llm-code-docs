# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/hadoop-libraries-are-missing/set-spark-home-variable.md

# Set Spark home variable

If you are using the Spark client from the Cloudera or Hortonworks Hadoop distributions, you may also receive the following log error:

```
Exception in thread "main" java.lang.NoSuchFieldError: TOKEN_KIND

```

If you received this log error, you must also complete the following steps for your Hadoop distribution:

1. Download the Spark client for your Hadoop cluster distribution (Cloudera or Hortonworks).
2. Navigate to the `adaptive-execution/config` directory and open the `application.properties` file.
3. Set the **sparkHome** location to where Spark 2 is located on your machine.

Example for Cloudera:

```
**sparkhome** = /opt/cloudera/parcels/SPARK2/lib/spark2

```

Example for Hortonworks:

```
**sparkhome** =/opt/horton/SPARK2/lib/spark2
```
