# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/unable-to-read-or-write-files-to-hdfs-on-amazon-emr-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/unable-to-read-or-write-files-to-hdfs-on-amazon-emr-cluster.md

# Unable to read or write files to HDFS on the Amazon EMR cluster

When running a transformation on an EMR cluster, the transformation appears to run successfully, but an empty file is written to the cluster. When PDI is not installed on the Amazon EC2 instance where you are running your transformation, you are unable to read or write files to the HDFS cluster. Any files written to the cluster are empty.

To resolve this issue, perform the following steps to edit the `hdfs-site.xml` file on the PDI client

:

1. Navigate to the `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/<user-defined connection name>` directory.
2. Open the `hdfs-site.xml` file with any text editor.
3. Add the following code:

   ```
   <property>
        <name>dfs.client.use.datanode.hostname</name>
        <value>true</value>
   </property>

   ```
4. Save and close the file.
