# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article.md

# Connecting to a Hadoop cluster with the PDI client

To connect to a Hadoop cluster, you must access a driver, create a named connection, then configure and test the connection. A named connection is information, including the IP address and port number, used to connect to the Hadoop cluster which is then stored by the name you assign to the connection for later use. You can create named connections to any supported vendor cluster and vendor version.

After you have a named connection set up, you can edit or duplicate that connection. For example, if you want to use a configuration with different security credentials, you can duplicate a connection, then edit the security settings on the copy. Named connections are useful when you move the jobs and transformations from a development server to a production server because you only need to update the connection information for the cluster name in the Hadoop Clusters dialog box. The jobs and transformations use the new connection information from the named connection.
