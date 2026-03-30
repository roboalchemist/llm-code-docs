# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection.md

# Add security to cluster connections

If you have a secure Hadoop cluster, the security options depend on the driver. All drivers have the **Kerberos** option. If you are using a Hortonworks driver, you can also select **Knox** as the security type. If you are connected to a Pentaho Repository, you can specify additional Kerberos options for secure impersonation. See the **Administer Pentaho Data Integration and Analytics** document for further information on secure impersonation.

If you are not sure what security type is set up for the Hadoop cluster, contact the cluster administrator.

**Note:** For Kerberos, you need the authentication user name and either a password or a keytab file. For Knox, you need the Gateway URL, user name, and password.
