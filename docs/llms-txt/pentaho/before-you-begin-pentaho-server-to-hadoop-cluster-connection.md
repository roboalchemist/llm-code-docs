# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/before-you-begin-pentaho-server-to-hadoop-cluster-connection.md

# Before you begin

Before you connect to the Pentaho Server, set the connection path to the metastore, which is where these types of connections are stored.

1. Navigate to the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-big-data-plugin` directory and open the `plugin.properties` file with any text editor.
2. Locate the **hadoop.configurations.path** property and set the value to the `metastore` directory. For example, `/home/devuser/.pentaho/metastore`.
3. Save and close the `plugin.properties` file.
4. [Restart the server](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration)
