# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/using-oozie-shared/set-up-oozie-on-the-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/using-oozie-shared/set-up-oozie-on-the-server.md

# Set up Oozie on the server

Perform the following steps to add a PDI proxy user on the server:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `config.properties` file.

   **Note:** This filepath and the `config.properties` file are created when you create a named connection. See the **Pentaho Data Integration** document for details about named connections.
2. Add the proxy user name to the **pentaho.oozie.proxy.user** parameter.
3. Save and close the file.

Refer to the **Pentaho Data Integration** document for more nameed connection information.
