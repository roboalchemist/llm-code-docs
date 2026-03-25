# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/steps-cannot-run-in-parallel/add-the-step-id-to-the-configuration-file.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/steps-cannot-run-in-parallel/add-the-step-id-to-the-configuration-file.md

# Add the step ID to the configuration file

The configuration file, `org.pentaho.pdi.engine.spark.cfg`, contains the **forceCoalesceSteps** property. The property is a pipe-delimited listing of all the IDs for the steps that should run with a coalesced dataset. Pentaho supplies a default set to which you can add IDs for steps that generate errors.

Perform the following steps to add another step ID to the configuration file:

1. Navigate to the `data-integration/system/karaf/etc` folder on the edge node running the AEL daemon and open the `org.pentaho.pdi.engine.spark.cfg` file.
2. Append your step ID to the **forceCoalesceSteps** property value list, using a pipe character separator between the step IDs.
3. Save and close the file.
