# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/spark-tuning-example-use-case-about-spark-tuning.md

# Example: Improving performance using Spark step tuning options

As an example, you may have a PDI transformation you are trying to execute on the Spark engine that takes many hours to run. While researching this slow performance, you notice only a small amount of YARN memory is used for this execution. Further research indicates you have not enough executors for too many partitions based on the default HDFS block size.

You could try the following workflow to possibly improve performance:

1. Determine how many executors are feasible to use more available YARN memory.
2. Adjust application tuning parameters in the **Parameters** tab of the PDI **Transformation properties** dialog box to increase the number of executors to the feasible amount.

   You are now using a higher amount of YARN memory and performance is better, but you feel you need further performance improvement. You could start tuning at the PDI step level. Because of the large amount of default partitions, you could coalesce down to a smaller number of partitions.
3. Determine how far you can coalesce down to a target number of partitions per your memory and cluster resources.
4. Set **coalesce** to **true** and **repartition.numPartitions** to your target number of partitions.

   You also notice you are joining data within your PDI transformation.
5. Set **joinBroadcast.stepName** to the name of the PDI step introducing the data into your join step.

   Performance has improved, but you feel it could be even better. You could persist the data after the wide Spark transformations but before output to save downstream computations
6. Set **persist.storageLevel** to **OFF\_HEAP**. The **IN\_MEMORY** setting allocates memory away from the executors and could lead to an overflow. See [RDD Persistence](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence) for possible storage options.

This workflow could work in improving performance for a given PDI transformation with too few executors for too many partitions, yet every PDI transformation and your cluster resources are different. Before trying to apply application and step tuning, you should know how to effectively adjust Spark parameters, your specific PDI transformation, and cluster resources . Generally, 3 to 5 YARN cores per executor is a good point for sizing your resources. You can assess the number of partitions after you size the executors.

For more information about how to improve the performance of your transformations, see [Optimizing Spark tuning](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning).
