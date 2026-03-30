# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/before-you-begin/pentaho-spark-application.md

# Pentaho Spark application

The Pentaho Spark application is built upon PDI's Pentaho execution engine, which allows you to develop Spark applications with familiar Pentaho tools. Some third-party plugins, such as those plugins available in the Pentaho Marketplace, may not be included by default within the Pentaho Spark application. To address this issue, we include functionality in the Spark Application builder tool so you can customize the Pentaho Spark application by adding or removing components to fit your needs.

After running the Spark application builder tool, copy and unzip the resulting `pdi-spark-driver.zip` file to an edge node in your Hadoop cluster. The unpacked contents consist of the `data-integration` folder and the `pdi-spark-executor.zip` file, which includes only the required libraries needed by the Spark nodes themselves to execute a transformation when the AEL daemon is configured to run in YARN mode. Since the `pdi-spark-executor.zip` file needs to be accessible by all nodes in the cluster, it must be copied into HDFS. Spark distributes this ZIP file to other nodes and then automatically extracts it.

Perform the following steps to run the Spark application build tool and manage the resulting files:

1. Ensure that you have configured your PDI client with all the plugins that you will use.
2. Navigate to the `design-tools/data-integration` folder and locate the `spark-app-builder.bat` (Windows) or the `spark-app-builder.sh` (Linux).
3. Execute the Spark application builder tool script.

   A console window will display and the `pdi-spark-driver.zip` file will be created in the `data-integration` folder (unless otherwise specified by the `-outputLocation` parameter described below).

   The following parameters can be used when running the script to build the `pdi-spark-driver.zip`.

   | Parameter                   | Action                                                                                         |
   | --------------------------- | ---------------------------------------------------------------------------------------------- |
   | `–h` or `--help`            | Displays the help.                                                                             |
   | `–e` or `--exclude-plugins` | Specifies plugins from the `data-integration/plugins` folder not to exclude from the assembly. |
   | `–o` or `--outputLocation`  | Specifies the output location.                                                                 |

   The `pdi-spark-driver.zip` file contains a `data-integration` folder and `pdi-spark-executor.zip` file.
4. Copy the `data-integration` folder to the edge node where you want to run the AEL daemon.
5. Copy the `pdi-spark-executor.zip` file to the HDFS node where you will run Spark.

   This folder will be referred to as *HDFS\_SPARK\_EXECUTOR\_LOCATION*.

**Note:** For the cluster nodes to use the functionality provided by PDI plugins when executing a transformation, they must be installed into the PDI client prior to generating the Pentaho Spark application. If you install other plugins later, you must regenerate the Pentaho Spark application.
