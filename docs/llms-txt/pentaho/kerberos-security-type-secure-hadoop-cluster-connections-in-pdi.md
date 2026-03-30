# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection/kerberos-security-type-secure-hadoop-cluster-connections-in-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection/kerberos-security-type-secure-hadoop-cluster-connections-in-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/secure-cluster-connections-add-hadoop-cluster-connection/kerberos-security-type-secure-hadoop-cluster-connections-in-pdi.md

# Specify Kerberos security

Perform the following steps to specify the credentials for the Kerberos security.

**Note:** You can define different principal users for each of the named connections only if all the clusters for these connections are in the same Kerberos realm. See [MIT Kerberos Documentation](https://web.mit.edu/kerberos/krb5-devel/doc/admin/realm_config.html) for more information about Kerberos realms.

1. Select **Kerberos** as the security type.
2. Click **Next**.
3. Choose one of the following security methods and specify the Kerberos credentials you obtained from the cluster administrator:
   * **Password**: Specify the **Authentication username** and **Password** options. Additionally, if you are connected to the Pentaho Repository and are using secure impersonation, specify the **Impersonation username** and **Password**. See **Try Pentaho Data Integration and Analytics** if the environment requires advanced settings, the server is on Windows, or when you are using a Cloudera Impala database for secure impersonation.

     ![Edit Cluster dialog box - Password option](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-aecfc8918e94f6efafa29eaefdf0ee0c9483ea84%2FPDI_Edit_Cluster_Password.png?alt=media)
   * **Keytab**: Specify the **Authentication username** and **Authentication Keytab** options. Click **Browse** to navigate to your keytab file. Additionally, if you are connected to the Pentaho Repository and are using secure impersonation, specify the **Impersonation username** and **Impersonation Keytab**. See **Try Pentaho Data Integration and Analytics** if the environment requires advanced settings, the server is on Windows, or when you are using a Cloudera Impala database for secure impersonation.

     ![Edit Cluster dialog box - Keytab option](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-37b82e9148a9e8b9400f13871be360180a4e7118%2FPDI_Edit_Cluster_Keytab.png?alt=media)
4. Click **Next** to test the connection. See [Test a cluster connection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/adding-a-cluster-connection-connect-to-a-hadoop-cluster-with-the-pdi-client/test-the-cluster-connection-add-hadoop-cluster-connection) for more information.

   The **Test results** dialog box appears.

   ![Test results dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ab4fb9a1b20079d330f988dc3914f7342e96a23a%2FPDI_Test_results_new.png?alt=media)

   For each tested connection, the dialog box displays one of the following icons to indicate the results:

   * ![Green checkmark symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-70b381e9695752080f7ce45b1c9147afb198803e%2FGreen_checkmark_symbol.png?alt=media) A green checkmark indicates the connection to the cluster service was successful.
   * ![Yellow caution symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-836ed7595a799183751ee91d6292df85afdd3c9f%2FYellow_caution_symbol.png?alt=media) A yellow caution symbol indicates the cluster service information was not supplied, so the test for that component was skipped.
   * ![Red circle-backslash symbol](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-06da8125a1d391cc723c1f07f85a53ef9b7bef11%2FRed_circle_backslash_symbol.png?alt=media) A red circle-backslash indicates the connection failed. Check the connection information and then test the connection again. If you suspect a different issue, see the troubleshooting section in the **Install Pentaho Data Integration and Analytics** document or consult the cluster administrator.**Note:** You can click the drop-down arrow in the **Hadoop file system** test for more details.
5. Click **Finish**.

If no errors occur during the connection, PDI is successfully connected.

If you have errors, see the troubleshooting section in the **Administer Pentaho Data Integration and Analytics** document to resolve the issues or consult the cluster administrator, then run the test again. When no error messages are returned, the connection is properly configured.
