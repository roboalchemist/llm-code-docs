# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/duplicate-a-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/duplicate-a-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/duplicate-a-hadoop-cluster-connection.md

# Duplicate a Hadoop cluster connection

You can duplicate a cluster connection. This task is useful if you want to test a change to a named connection without affecting the existing setup or if you want to add different security permissions.

To duplicate a cluster connection, perform the following steps:

1. Click the **Hadoop clusters** folder in the **View** tab.
2. Right-click an existing connection and select **Duplicate cluster**.

   The Hadoop clusters (Edit cluster) dialog box appears.
3. Enter a different name in the **Cluster Name** field.

   The system automatically adds `copy-of-` to the beginning of the cluster name.
4. Click **Browse to add files(s)**. Use the file browser to select the `site.xml` files you want to import.

   **Note:** Duplicating a cluster connection copies the existing `site.xml` files to a new metastore directory. If you select `site.xml` files in this step, these files replace the copied `site.xml`.
5. Click **Next**.
6. For the security type, select **None** and click **Next** or see [Add security to cluster connections](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection) to add or edit security.
7. Click **Edit cluster** to open the **Edit cluster** dialog box
8. Make the applicable changes to the cluster configuration values, then click **Next**.

   The **Congratulations** dialog box appears.
9. Click **Close**.
