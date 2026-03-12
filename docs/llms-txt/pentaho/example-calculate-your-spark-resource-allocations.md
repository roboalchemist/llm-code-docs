# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally/determining-spark-resource-requirements/example-calculate-your-spark-resource-allocations.md

# Example: Calculate your Spark application settings

Use the following steps to calculate the Spark application settings for the cluster. Adjust the example to fit your environment and requirements.

In the following example, your cluster size is:

* 11 nodes (1 master node and 10 worker nodes)
* 66 cores (6 cores per node)
* 110 GB RAM (10 GB per node)

In the following example, your job requirements for the allowable percentage of consumable cluster resources by a KTR include:

* Run with 50 percent YARN utilization
* 19 executors (1 driver and 18 worker nodes)

1. Calculate the initial application tuning settings for the parameters.

| Action                                                                       | Calculation                                                                                                    | Example                                                                                         |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Determine the core resources for the Spark application.                      | Multiply the number of cluster cores by the YARN utilization percentage.                                       | 66 x 0.5 = 33Provides 3 driver and 30 worker node cores.                                        |
| Determine the memory resources available for the Spark application.          | Multiply the cluster RAM size by the YARN utilization percentage.                                              | 110 x 0.5 = 55Provides 5 GB RAM for available drivers and 50 GB RAM available for worker nodes. |
| Discount 1 core per worker node to determine the executor core instances.    | Subtract the number of available worker node cores from the reserved core allocations.                         | 30 - 10 = 20Provides 20 executor core instances.                                                |
| Discount 1 GB RAM per worker node to determine available worker node memory. | Subtract the memory resources available for the worker node cores from the reserved core allocations.          | 50 - 10 = 40Provides 40 GB RAM.                                                                 |
| Allow a 10 percent memory overhead per executor.                             | Multiply the available GB RAM by percentage available for use.                                                 | (1.0 - 0.1) x 40 = 36Provides 36 GB RAM.                                                        |
| Determine the Spark executor cores value.                                    | Divide the number of executor core instances by the reserved core allocations.                                 | 20 / 10 = 2 cores per nodeProvides 1 core per executor.                                         |
| Determine the Spark executor memory value.                                   | Divide the usable memory by the reserved core allocations, then divide that amount by the number of executors. | (36 / 9) / 2 = 2 GBProvides 2 GB RAM per executor.                                              |

\*\*Note:\*\* The \*\*spark.yarn.driver.memoryOverhead\*\* and \*\*spark.driver.cores\*\* values are derived from the resources of the node that AEL is installed on, under the assumption that only the driver executor is running there. The \*\*spark.default.parallelism\*\* value is derived from the amount of parallelism per core that is required \\(an arbitrary setting\\). In the example above, a value of 36 is derived from a parallelism per core setting of 2, multiplied by the \*\*spark.executor.instances\*\*, 18.

2. Apply the Spark application settings that you calculated, as described in [Set the Spark parameters globally](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally).

   For example:

   | Parameter                              | Value  |
   | -------------------------------------- | ------ |
   | **spark.executor.instances**           | `18`   |
   | **spark.yarn.executor.memoryOverhead** | `1024` |
   | **spark.executor.memory**              | `2G`   |
   | **spark.yarn.driver.memoryOverhead**   | `1024` |
   | **spark.driver.memory**                | `3G`   |
   | **spark.executor.cores**               | `1`    |
   | **spark.driver.cores**                 | `2`    |
   | **spark.default.parallelism**          | `36`   |

The initial application tuning parameters for Spark are set on the cluster. To complete the Spark tuning process, see [Optimizing Spark tuning](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning).
