# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-local-mode.md

# Configure the AEL daemon for local mode

You can configure the AEL daemon to run in Spark local mode for development or demonstration purposes. In local mode, you can build and test a Spark application on your desktop with sample data, then reconfigure the application to run on your clusters.

**Note:** Configuring the AEL daemon to run in Spark local mode is not supported, but can be useful for development and debugging.

To configure the AEL daemon for a local mode, complete the following steps:

1. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file.
2. Set the following properties for your environment:
   1. Set the **sparkHome** property to the Spark 2 filepath on your local machine.
   2. Set the **sparkApp** property to the `data-integration` directory.
   3. Set the **hadoopConfDir** property to the directory containing the `*site.xml` files.
3. Save and close the file.
4. Navigate to the `data-integration/adaptive-execution` folder and run the `daemon.sh` command from the command line interface.
