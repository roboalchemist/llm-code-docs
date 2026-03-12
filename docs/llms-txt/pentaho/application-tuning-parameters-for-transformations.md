# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations.md

# Application tuning parameters for Spark

Application tuning parameters use the `spark.` prefix and are passed directly to the Spark cluster for configuration. Pentaho offers full support of Spark properties. See the [Spark properties documentation](https://spark.apache.org/docs/2.3.0/configuration.html#available-properties) for a full list.

Available application tuning parameters for Spark may depend on your deployment or cluster management. All the Spark parameters in PDI support the use of variables. The following table lists the Spark parameters available in PDI. See the [Spark properties documentation](https://spark.apache.org/docs/2.3.0/configuration.html#available-properties) for full descriptions, default values, and recommendations.

| Spark                             | Parameter Value | Description                                                                                                                            |
| --------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **spark.executor.instances**      | Integer         | The number of executors for the Spark application.                                                                                     |
| **spark.executor.memoryOverhead** | Integer         | The amount of off-heap memory to be allocated per executor.                                                                            |
| **spark.executor.memory**         | Integer         | The amount of memory to use per executor process.                                                                                      |
| **spark.driver.memoryOverhead**   | Integer         | The amount of off-heap memory to be allocated per driver in cluster mode.                                                              |
| **spark.driver.memory**           | Integer         | The amount of memory to use for the driver process.                                                                                    |
| **spark.executor.cores**          | Integer         | The number of cores to use on each executor.                                                                                           |
| **spark.driver.cores**            | Integer         | The number of cores to use for the driver process in cluster mode.                                                                     |
| **spark.default.parallelism**     | Integer         | The default number of partitions in RDDs returned by transformations, such as join, reduceByKey, and parallelize when not set by user. |

If an identical property is set in a user's transformation, it overrides the setting on the cluster or Pentaho Server.

**Note:** Tuning parameters at the step-level do not use the `spark.` prefix and are executed on the Spark cluster as applications without affecting the cluster configuration. See [Setting PDI step Spark tuning options](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/opening-spark-tuning-options-cp/setting-spark-tuning-options) for details.
