# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/cloudera.md

# Cloudera

If your Cloudera Spark client does not contain the Hadoop libraries, you must add the Hadoop libraries to the classpath using the *SPARK\_DIST\_CLASSPATH* environment variable, as shown in the following example command:

```
export *SPARK\_DIST\_CLASSPATH*=$(hadoop classpath)
```

**Note:** Because of limitations for CDS Powered by Apache Spark in CDH 6.x, AEL does not support Hive or Impala in YARN mode. If you would like specific information, see the [Cloudera documentation](https://docs.cloudera.com).
