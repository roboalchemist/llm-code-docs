# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/add-a-cluster-connection-by-import-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/add-a-cluster-connection-by-import-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/add-a-cluster-connection-by-import-add-hadoop-cluster-connection.md

# Import a cluster connection

You can add a cluster by importing the `site.xml` files from an existing cluster. Perform the following steps to import a cluster connection.

1. In the PDI client, create a new transformation or job or open an existing transformation or job.
2. Click the **View** tab and then right-click the **Hadoop Clusters** folder.
3. Click **Import cluster**.

   The **Hadoop Clusters** dialog box appears.

   ![Hadoop Clusters dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2FBdIlGSlPAGV87W7pfN1O%2FNewCluster.png?alt=media\&token=92aaf1ff-4a20-403f-8db4-90a595735246)
4. Enter a user-defined name for the cluster connection in the **Cluster name** field.

   Valid cluster names may include uppercase and lowercase letters, and numbers. In addition, the only special character allowed is the dash (`-`). To ensure a valid cluster name, do not use any other symbols, punctuation characters, or blank spaces.

   After you create the connection, you can locate this named connection in the **View** tab on the PDI client.

   **Note:** If the **Cluster name** is already in use, you will be notified that proceeding will overwrite an existing cluster, which cannot be undone. In this case:

   * Click **Cancel** then enter a unique name to create the cluster.
   * Click **Yes, Overwrite** to overwrite the existing cluster.
5. Use the **Driver** and **Version** options to select the distribution of Hadoop on the cluster and its version number. The [Support Portal](https://support.pentaho.com/hc/en-us) provides supported drivers that you can download and install.
6. Click **Browse to add file(s)** and browse to the directory containing the `site.xml` files that were provided to you by the cluster administrator.

   The required files include:

   * `hive-site.xml`
   * `mapred-site.xml`
   * `yarn-site.xml`
   * `core-site.xml`
   * `hbase-site.xml`
   * `hdfs-site.xml`
   * `oozie-site.xml` (if you are using Oozie in the configuration)
7. Click **Open**.

   The **Site XML files** section displays the files you selected.
8. If you are connecting to a secure cluster, then enter the credentials in the **Username** and **Password** fields in the **HDFS** section.
9. Click **Next** and then specify the security option for the cluster.
   * If the Hadoop cluster is non-secure, select **None** and then click **Next** to [test the connection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection).
   * If your Hadoop cluster is secure, you need to add security to the cluster connection. See [Add security to cluster connections](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection) for instructions.
