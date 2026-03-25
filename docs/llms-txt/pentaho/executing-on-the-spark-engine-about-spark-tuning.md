# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/executing-on-the-spark-engine-about-spark-tuning.md

# Executing on the Spark engine

The Spark engine groups data into partitions. Data is processed in each partition. The Spark engine creates executors, which process partitions of the data. In some cases, you can improve performance by either adding executors or increasing their memory size. The amount and size of executors is limited to your cluster resources.

Not all the memory set aside in the **Spark memory model** is available for data processing. The memory allotted in the Spark memory model is broken down into the following segments:

| Memory type     | Amount                                                | Note                                                                                            |
| --------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Reserved memory | 300 MB hard coded for Spark.                          | Cannot be adjusted and is not available to any executor.                                        |
| User memory     | 25% of the memory leftover after the reserved memory. | Non-dataset storage used for the executors.                                                     |
| Spark memory    | 75% of the memory leftover after the reserved memory. | Roughly half of this memory is used for data storage, and the other half is used for execution. |

The amount of memory available for partitions comes from the data storage part of Spark memory model. The rest of the Spark memory model is available for the executor. ETL tasks usually require more data storage, while AI and machine learning tasks need more execution memory.

The Spark engine changes the state of data in the memory model through the following types of Spark transformations:

* **Narrow Spark transformation**

  A Spark task that only requires data from a single partition. The data can be input, transformed, and output all within the same partition.
* **Wide Spark transformation**

  A Spark task that requires data from multiple partitions. In a wide transformation, the data must be shuffled between partitions. The partition used to input the data is not the same as the partition used to transform and output the data.

A PDI transformation may have one or more narrow or wide transformations in Spark.

Narrow Spark transformations are more efficient than wide Spark transformations. Wide Spark transformations can lead to repartitioning, which can lead to slow data transfer speeds, transfer failures, and re-calculations. Examples of wide transformations are join, sort, and grouping operations. You can improve execution by coalescing the partitions (reducing the number of partitions) to consolidate splits without shuffling data.
