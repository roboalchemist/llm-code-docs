# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-yarn-mode.md

# Configure the AEL daemon for YARN mode

Typically, the AEL daemon is run in YARN mode for production purposes. In YARN mode, the driver application launches and delegates work to the YARN cluster. The `pdi-spark-executor` application must be installed on each of the YARN nodes.

The `daemon.sh` script is only supported in UNIX-based environments.

**Note:** Because of limitations for Cloudera Distribution Spark (CDS) Powered by Apache Spark in Cloudera Distribution Hadoop (CDH) 6.x, AEL does not support Hive or Impala in YARN mode. If you would like specific information, see the [Cloudera documentation](https://docs.cloudera.com).

To configure the AEL daemon for a YARN production environment, complete the following steps.

1. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file.
2. Set the following properties for your environment:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Property</td><td>Value</td></tr><tr><td><strong>websocketURL</strong></td><td><p>The fully-qualified domain name of the node where the AEL daemon is installed. The following command is an example of how to obtain the fully qualified name: ```<br>[devuser@hito31-n2 ~]$ hostname -f<br>hito31-n2.cs1cloud.internal</p><pre><code>
An example of a fully qualified name is `websocketURL=ws://localhost:${ael.unencrypted.port}`.

\</td>\</tr>\<tr>\<td>

**sparkHome**

\</td>\<td>

The path to the Spark client folder on your cluster

\</td>\</tr>\<tr>\<td>

**sparkApp**

\</td>\<td>

The `data-integration` directory

\</td>\</tr>\<tr>\<td>

**hadoopConfDir**

\</td>\<td>

The directory containing the `*site.xml` files. This property value tells Spark which Hadoop/YARN cluster to use. You can download the directory containing the `*site.xml` files using the cluster management tool, or you can set the **hadoopConfDir** property to the location in the cluster.

\</td>\</tr>\<tr>\<td>

**hadoopUser**

\</td>\<td>

The user ID the Spark application will use. This user must have permissions to access the file in the Hadoop file system.

\</td>\</tr>\<tr>\<td>

**hbaseConfDir**

\</td>\<td>

The directory containing the `hbase-site.xml` file. This property value tells Spark how HBase is configured for your cluster. You can download the directory containing the `*site.xml` files using the cluster management tool, or you can set the **hadoopConfDir** property to the location in the cluster.

\</td>\</tr>\<tr>\<td>

**sparkMaster**

\</td>\<td>

`yarn`

\</td>\</tr>\<tr>\<td>

**SparkDeployMode**

\</td>\<td>

`client`**Note:** YARN-cluster deployment mode in YARN is not supported by AEL

\</td>\</tr>\<tr>\<td>

**assemblyZip**

\</td>\<td>

`hdfs:*$HDFS\_SPARK\_EXECUTOR\_LOCATION*`

\</td>\</tr>\</tbody>
\</table>3.  Save and close the file.

4. Copy the `pdi-spark-executor.zip` file to your HDFS cluster, as shown in the following example:

   ```
   $ hdfs dfs put pdi-spark-executor.zip /opt/pentaho/pdi-spark-executor.zip
   ```

5. Perform the following steps to start the AEL daemon.

   You can start the AEL daemon by running the `daemon.sh` script. By default, this startup script is installed in the `data-integration/adaptive-execution` folder, which is referred to as the variable *PDI\_AEL\_DAEMON\_HOME*.

   1. Navigate to the `data-integration/adaptive-execution` directory.

   2. Run the `daemon.sh` script.

      The `daemon.sh` script supports the following commands:

      | Command            | Action                                                                                                         |
      | ------------------ | -------------------------------------------------------------------------------------------------------------- |
      | `daemon.sh`        | Starts the daemon as a foreground process.                                                                     |
      | `daemon.sh start`  | Starts the daemon as a background process. Logs are written to the `*PDI\_AEL\_DAEMON\_HOME*/daemon.log` file. |
      | `daemon.sh stop`   | Stops the daemon.                                                                                              |
      | `daemon.sh status` | Reports the status of the daemon.                                                                              |

</code></pre></td></tr></tbody></table>
