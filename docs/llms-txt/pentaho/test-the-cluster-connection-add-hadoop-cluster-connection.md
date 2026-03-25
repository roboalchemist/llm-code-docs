# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection.md

# Test a cluster connection

Perform the following steps to test a cluster connection:

1. In the PDI client, select the **View** tab and navigate to the **Hadoop clusters** folder.
2. If needed, expand the **Hadoop clusters** folder then right-click the cluster you want to test and select **Test cluster**.

   The **Test results** dialog box appears.

   ![Test results dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ab4fb9a1b20079d330f988dc3914f7342e96a23a%2FPDI_Test_results_new.png?alt=media)

   For each tested connection, the dialog box displays one of the following icons to indicate the results:

   * ![Green checkmark symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-70b381e9695752080f7ce45b1c9147afb198803e%2FGreen_checkmark_symbol.png?alt=media) A green checkmark indicates the connection to the cluster service was successful.
   * ![Yellow caution symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-836ed7595a799183751ee91d6292df85afdd3c9f%2FYellow_caution_symbol.png?alt=media) A yellow caution symbol indicates the cluster service information was not supplied, so the test for that component was skipped.
   * ![Red circle-backslash symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-06da8125a1d391cc723c1f07f85a53ef9b7bef11%2FRed_circle_backslash_symbol.png?alt=media) A red circle-backslash indicates the connection failed. Check the connection information and then test the connection again. If you suspect a different issue, see the troubleshooting section in the **Install Pentaho Data Integration and Analytics** document or consult the cluster administrator.**Note:** You can click the drop-down arrow in the **Hadoop file system** test for more details.
3. Click **Finish**.

If no errors occur during the connection, PDI is successfully connected.

If you have errors, see troubleshooting section of the **Administer Pentaho Data Integration and Analytics** document to resolve the issues then test your connection again. When no error messages are returned, the connection is properly configured.
