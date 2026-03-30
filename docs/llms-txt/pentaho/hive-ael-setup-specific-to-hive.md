# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive.md

# Hive

To achieve the best performance using Hive, ensure that you have optimized your AEL environment as described in [About Spark tuning in PDI](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp). After tuning Spark, you can make additional improvements to Hive performance with the following tuning techniques:

* Setup Hive partitioning on the tables for more efficient queries and use bucketing for manageable dataset parts. For more information, see [hive-partitioning-vs-bucketing](https://data-flair.training/blogs/hive-partitioning-vs-bucketing/).
* Use the `hive.auto.convert.join` parameter to reduce query times.
* Use the `mapred.compress.map.output` parameter to save cluster space.
* Enable parallel execution to improve cluster utilization.
* For better pipeline and cache usage, enable vectorization to batch process rows and perform operations on column vectors.
* Configure the Live Long and Processed (LLAP) queue capacity to maximize the YARN resources for LLAP without wasting cluster space.

For more information about these methods, see [hive-best-practices](https://www.qubole.com/blog/hive-best-practices/). Refer to your vendor-specific documentation for implementation.

Lastly, you might consider the differences between the Amazon's Elastic Map Reduce (EMR) and other Hive environments, specifically how formats are handled differently. EMR uses the Parquet storage format, instead of ORC with compression, to provide better performance. EMR, however, does not support LLAP. For more information on other exceptions, see [emr-hive-differences](https://docs.amazonaws.cn/en_us/emr/latest/ReleaseGuide/emr-hive-differences.html).

The following sections show you how to use Spark on AEL with Hive. Pentaho supports Hive access from Spark for Amazon's Elastic MapReduce 5.24 and Hortonworks Data Platform 3.x.
