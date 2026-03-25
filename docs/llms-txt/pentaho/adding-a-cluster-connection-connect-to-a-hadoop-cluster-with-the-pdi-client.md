# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Adding a cluster connection

You can add named connections manually or by importing them. If you are using high availability (HA) clusters, you must manually add the connection information in the New cluster dialog box to create your connection.

If you are connected to the Pentaho Repository when you add a new cluster connection, you and other users can reuse the connection. Cluster connections are registered by all transformations and jobs in the repository and are loaded during execution unless the connections cannot be found.

If you are not connected to the Pentaho Repository when you create the connection, then only you can reuse the connection, as it is registered exclusively by the local file system for transformations and jobs.

**Note:** Security is set up on a per-user basis. Security information is not stored in the repository.

* To add a new cluster connection using import, see [Import a cluster connection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/add-a-cluster-connection-by-import-add-hadoop-cluster-connection)
* To add a new cluster connection manually, see [Manually add a cluster connection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/add-a-cluster-connection-manually-add-hadoop-cluster-connection)
