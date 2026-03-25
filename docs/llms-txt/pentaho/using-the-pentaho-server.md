# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster/using-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster/using-the-pentaho-server.md

# Using the Pentaho Server

To run Pan or Kitchen on your Hadoop cluster, the Pentaho Server must have access to the metastore where the Hadoop connections are stored.

Perform the following steps to configure the Pentaho Server to run jobs or transformations from the command line interface (CLI).

1. If the server is on a different host than the PDI client, copy the `metastore` directory and its contents from the PDI client to a location accessible to the server.

   The `metastore` directory is created when you set up a named connection to the Hadoop cluster. The default metastore location for the PDI client is `home/<user>/.pentaho/metastore`.
2. Navigate to the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-big-data-plugin` directory and open the `plugin.properties` file with any text editor.
3. Set the value of the *hadoop.configurations.path* property to the `metastore` directory.
4. Save and close the `plugin.properties` file.
