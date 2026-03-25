# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/about-spark-tuning-in-pdi-cp/tuning-the-spark-application-parameters-about-spark-tuning/opening-spark-application-tuning-about-spark-tuning.md

# Opening Spark application tuning

You can specify values for fine tuning the following types of Spark application parameters within either the `data-integration/adaptive-execution/config/application.properties` file or the **Parameters** tab of the PDI Transformation properties dialog box:

* Executor and driver resource sizing
* YARN utilization impacts
* Default partitioning
* Memory splits

You can also control these types of Spark application parameters through PDI environments variables.

As an example of application tuning, the number of default executors may be too low for your PDI transformation to efficiently utilize YARN capacity. You would improve capacity by increasing the number of executors based on data storage memory and cluster resources.

See [Configuring application tuning parameters for Spark](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark) for more information on setting Spark application parameters in PDI. See the Spark [Application Properties](http://spark.apache.org/docs/latest/configuration.html#available-properties) documentation for a full list of Spark application parameters.
