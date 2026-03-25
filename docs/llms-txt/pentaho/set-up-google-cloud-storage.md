# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/set-up-google-cloud-storage.md

# Google Cloud Storage

This configuration task is intended for Pentaho administrators and Hadoop cluster administrators who want to set up access to Google Cloud Storage (GCS) for PDI transformations running on Spark.

This task assumes that you have obtained the settings for your site's Google Cloud Storage (GCS) configuration from your Hadoop cluster administrator.

Perform the following steps to set up Hadoop cluster access to GCS:

1. Log on to the cluster and stop the AEL daemon by running the shutdown script, `daemon.sh stop`, from the command line interface.
2. Download the GCS Hadoop Connector JAR file and save it in a location where you can access it. You can use the following UNIX command to download the GCS Hadoop Connector Jar:

   `wget https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop2-latest.jar`
3. Use the following command to add the GCS Hadoop Connector JAR file to the `SPARK_DIST_CLASSPATH` where */full/path/to* is the location where you stored the JAR file:

   `export SPARK_DIST_CLASSPATH=$(hadoop classpath):*/full/path/to*/gcs-connector-hadoop2-latest.jar`
4. Configure your clusters with the GCS connector with Hadoop/Spark using the instructions located in the Google Cloud Platform interoperability GitHub repository: <https://github.com/GoogleCloudPlatform/bigdata-interop/blob/master/gcs/INSTALL.md>
5. Configure AEL to use the GCS Hadoop Connector. Possible ways of configuring AEL include on of the following.
   * Adding the GCS properties to the `/etc/hadoop/conf/core-site.xml` file.
   * Adding JSON keyfile parameters for GCS to the AEL daemon `application.properties` file. Follow the instructions in Step 6.

     **Note:** The JSON keyfile for GCS must be present on all the nodes in the cluster.
6. (Optional) If you choose to add a JSON keyfile to the `application.properties` file, follow these steps.
   1. Navigate to the `data-integration/adaptive-execution/config/` directory and open the `application.properties` file with any text editor.
   2. Add the following lines of code:
      * `spark.hadoop.google.cloud.auth.service.account.enable=true`
      * `spark.hadoop.google.cloud.auth.service.account.json.keyfile=/path/to/keyfile.json`
   3. Save the file and close it.
7. Restart the AEL daemon by running the startup script, `daemon.sh`, from the command line interface.
