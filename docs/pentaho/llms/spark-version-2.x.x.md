# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/spark-submit/install-and-configure-spark-client-for-pdi-use-spark-submit-entry/spark-version-2.x.x.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/spark-submit/install-and-configure-spark-client-for-pdi-use-spark-submit-entry/spark-version-2.x.x.md

# Spark version 2.x.x

Complete the following steps to install and configure the Spark client:

1. On the client, download the Spark distribution of the same or higher version as the one used on the cluster.
2. Set the **HADOOP\_CONF\_DIR** environment variable to a folder containing cluster configuration files as shown in the following sample for an already-configured driver:
   * `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*`
3. Navigate to `<SPARK_HOME>/conf` and create the `spark-defaults.conf` file using the instructions outlined in <https://spark.apache.org/docs/latest/configuration.html>.
4. Create a ZIP archive containing all the JAR files in the `SPARK_HOME/jars` directory.
5. Copy the ZIP file from the local file system to a world-readable location on the cluster.
6. Edit the `spark-defaults.conf` file to set the **spark.yarn.archive** property to the world-readable location of your ZIP file on the cluster as shown in the following examples:
   * `spark.yarn.archive hdfs://*NameNode hostname*:8020/user/spark/lib/*your ZIP file*`
7. Add the following line of code to the `spark-defaults.conf` file:
   * `spark.hadoop.yarn.timeline-service.enabled false`
8. If you are connecting to an HDP cluster, add the following lines in the `spark-defaults.conf` file:
   * `spark.driver.extraJavaOptions -Dhdp.version=2.3.0.0-2557`
   * `spark.yarn.am.extraJavaOptions -Dhdp.version=2.3.0.0-2557`**Note:** The `-Dhdp` version should be the same as Hadoop version used on the cluster.
9. If you are connecting to an HDP cluster, also create a text file named `java-opts` in the `<SPARK_HOME>/conf` folder and add your HDP version to it as shown in the following example:
   * `-Dhdp.version=2.3.0.0-2557`**Note:** Run the `hdp-select status Hadoop client` command to determine your version of HDP.
10. If you are connecting to a supported version of the HDP or CDH cluster, open the `core-site.xml` file, then comment out the **net.topology.script.file** property as shown in the following code block:

    ```xml
    <!--
    <property>
    <name>net.topology.script.file.name</name>
    <value>/etc/hadoop/conf/topology_script.py</value>
    </property>
    --> 
    ```

The Spark client is now ready for use with Spark Submit in PDI.
