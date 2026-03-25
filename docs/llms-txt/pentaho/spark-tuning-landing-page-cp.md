# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp.md

# Spark Tuning

You can use these PDI step tuning options to customize the transformations that run on the Spark engine.Spark tuning is the customization of PDI transformation and step parameters to improve the performance of running your PDI transformations on Spark. These parameters affect memory, cores, and instances used by the Spark engine. These Spark parameters include:

* **Application tuning parameters** which are transformation parameters for working with PDI transformations on Spark.
* **Spark tuning options** which are parameters for a specific PDI step.

Use the Spark tuning options to customize Spark parameters within a PDI step to further refine how your transformation runs. For example, if your KTR contains many complex computations, you can adjust the Spark tuning options for a PDI step to increase performance and decrease run times when executing your transformation.

**Note:** Spark tuning options for a step override the application tuning parameters for the transformation. You can set application tuning parameters in AEL in the `data-integration/adaptive-execution/config/application.properties` file or in PDI in the Transformation Properties window. For more information, see [Configuring application tuning parameters for Spark](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark).

This article provides a reference for the step-level Spark tuning options available in PDI. The Spark tuning categories, options, and applicable steps are listed below. For more information about the Spark tuning workflow, see [About Spark tuning in PDI](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp).

Spark tuning options for PDI steps include the following categories:

* [**Dataset**](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/dataset-tuning-options-spark)

  Set these options for data persistence, repartitioning, and coalesce. Tune these options to help you save downstream computation, such as reducing the amount of possible recalculations after [wide Spark transformations](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/executing-on-the-spark-engine-about-spark-tuning). Options include partitioning data, persisting data, and caching data.
* [**Join**](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/join-tuning-options-spark)

  Set this broadcast join option to push datasets out to the executors which can reduce shuffling during join operations.
* [**JDBC**](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/jdbc-tuning-options-spark)

  Set these options to specify the number of JDBC connections, including partitioning attributes.
* [**Dataframe Writer**](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/dataframe-writer-tuning-options-spark)

  Set these options for partitioning management, including bucketing file writes.
