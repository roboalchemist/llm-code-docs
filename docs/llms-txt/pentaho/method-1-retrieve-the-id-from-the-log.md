# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/steps-cannot-run-in-parallel/get-the-step-id/method-1-retrieve-the-id-from-the-log.md

# Method 1: Retrieve the ID from the log

You can retrieve a step ID though the PDI client with the following steps:

1. In the PDI client, create a new transformation and add the step to the transformation. For example, if you needed to know the ID for the Select values step, you would add that step to the new transformation.
2. Set the log level to debug.
3. Execute the transformation using the Spark engine.

   The step ID will display in the **Logging** tab of the **Execution Results** pane. For example, the log will display:

   ```
   Selected the SelectValues step to run in parallel as a GenericSparkOperation,
   ```

   where *SelectValues* is the step ID.
