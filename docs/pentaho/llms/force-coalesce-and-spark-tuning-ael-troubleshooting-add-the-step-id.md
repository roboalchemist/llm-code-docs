# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/steps-cannot-run-in-parallel/add-the-step-id-to-the-configuration-file/force-coalesce-and-spark-tuning-ael-troubleshooting-add-the-step-id.md

# Force coalesce and Spark tuning

Any steps to the `org.pentaho.pdi.engine.spark.cfg` force coalesce configuration file do a coalesce. If the `stepTuningOverrideForceCoalesceList` `application.properties` setting is set to `true`, then step tuning takes precedence over force coalesce.
