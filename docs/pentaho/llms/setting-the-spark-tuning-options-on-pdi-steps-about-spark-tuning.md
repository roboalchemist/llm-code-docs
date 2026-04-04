# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/setting-the-spark-tuning-options-on-pdi-steps-about-spark-tuning.md

# Setting the Spark tuning options on PDI steps

At the PDI step level, you have the following capabilities to fine tune your execution on the Spark engine:

* **Data persistence**

  The **cache** and **persist.storageLevel** options help you save downstream computations after wide Spark transformations to reduce the amount of possible recalculations. See Spark[RDD Persistence](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence) documentation for a list of possible Spark storage values.
* **Repartition and coalesce**

  The **repartition.numPartitions**, **repartition.columns**, and **coalesce** options help you increase or decrease the number of partitions. Repartition splits and shuffles data into new partitions. Coalesce collapses down the number of partitions without shuffling.
* **Broadcast join**

  The **join.broadcast.stepName** option helps you push datasets out to executors to reduce shuffling during join operations. You should only broadcast out relatively small amounts of data. The maximum broadcast size is set by the **spark.sql.autoBroadcastJoinThreshold** parameter.
