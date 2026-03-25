# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally.md

# Set the Spark parameters globally

Within the `application.properties` file, you may add any number of Spark properties to make global changes to the application tuning parameters for your Spark cluster that runs PDI. To view the full list of Spark parameters, see [Spark properties documentation](https://spark.apache.org/docs/2.3.0/configuration.html#available-properties). .

Spark tuning may be affected by the following factors:

* When a Hadoop or a Spark cluster is a shared enterprise asset.
* When cluster resources are shared among many Spark applications that are processed in parallel.

Perform the following steps to set up the `application.properties` file:

1. Log on to the cluster and stop the AEL daemon as described in Step 6 of [Configure the AEL daemon for YARN mode](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-yarn-mode).
2. Navigate to the `design-tools/data-integration/adaptive-execution/config` folder and open the `application.properties` file with any text editor.
3. Enter the Spark configuration parameter and value for each setting that you want to make in the cluster. For example, `spark.yarn.executor.memoryOverhead=1024`

   **Note:** See [Determining Spark resource requirements](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally/determining-spark-resource-requirements) for an example of calculating resources.
4. Save and close the file.
5. Restart the AEL daemon as described in Step 6 of [Configure the AEL daemon for YARN mode](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-yarn-mode).

The Spark parameters configured in the properties file are now globally applied to the Spark cluster. The performance results of your executed transformations are available on the YARN ResourceManager and Spark History Server. You can refine the tuning of the cluster at the transformation level as described in [Set the Spark parameters locally in PDI](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-locally-in-pdi).
