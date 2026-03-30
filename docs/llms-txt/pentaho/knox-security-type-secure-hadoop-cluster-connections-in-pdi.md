# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection/knox-security-type-secure-hadoop-cluster-connections-in-pdi.md

# Specify Knox security

Perform the following steps to specify the credentials for your Knox security, which is only available for the Hortonworks driver.

1. Select **Knox** as your security type.
2. Click **Next** to specify the Knox credentials you obtained from your cluster administrator.

   ![Gateway options for Hadoop cluster secured with Knox](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-fffb621da9f70b87e287ebdd65daf3416da5cd42%2FssPDI_HadoopCluster_KnoxSecurity.png?alt=media)
3. Specify the **Gateway URL** for the Knox server.
4. Specify the **Gateway Username** and **Gateway Password** for the Knox server.
5. Click **Next** to test your connection. See [Configure and test connection](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection) for more information.

After you specify your security credentials, PDI tests the connection to your Hadoop cluster. If no errors occur during the connection, PDI is successfully connected to your Hadoop cluster.

If you have problems, see the troubleshooting section in the **Administer Pentaho Data Integration and Analytics** document to resolve the errors, then test your connection again.
