# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/edit-hadoop-cluster-connections.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/edit-hadoop-cluster-connections.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/managing-hadoop-cluster-connections-connect-to-a-hadoop-cluster-with-the-pdi-client/edit-hadoop-cluster-connections.md

# Edit Hadoop cluster connections

How updates occur depend on whether you are connected to the repository.

* **If you are connected to a repository**

  Hadoop cluster connection changes are registered by all transformations and jobs in the repository. The Hadoop cluster connection information is loaded during execution unless it cannot be found.
* **If you are not connected to a repository**

  Hadoop cluster connection changes are registered by the local (file system) transformations and jobs. Note that changes to the Hadoop cluster connection are not updated in any transformations or jobs for the purpose of fallback unless they are saved again.

Perform the following steps to edit a Hadoop cluster connection:

1. Click the **Hadoop Clusters** folder in the **View** tab.
2. Right-click the existing connection, then select **Edit**. Optionally, you can double-click the existing connection.

   The Edit cluster dialog box appears.
3. Make the changes, then click **Next**.

   If the cluster is enabled for high availability (HA), then a port number is not needed, and you should clear the port number.
4. For the security type, select **None** and click **Next** or see [Add security to cluster connections](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection) to add or edit security.

   The Test results dialog box displays.
5. Click **Close** to save the changes.
