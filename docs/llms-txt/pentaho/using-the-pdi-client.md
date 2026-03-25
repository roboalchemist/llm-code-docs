# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster/using-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster/using-the-pdi-client.md

# Using the PDI client

Perform the following steps to configure the PDI client host machine to run jobs or transformations from the command line interface (CLI).

1. Create a connection to the Hadoop cluster where you want to run your job or transformation.
2. Create and test the job or transformation in the PDI client to verify it works as expected.
3. Navigate to the `design-tools/data-integration/plugins/pentaho-big-data-plugin` directory and open the `plugin.properties` file with any text editor.
4. Set the value of the *hadoop.configurations.path* property to the location of the `metastore` directory, such as `hadoop.configurations.path=/home/<user>/.pentaho`.

   The `metastore` directory is created when you set up a named connection to the Hadoop cluster. The default metastore location for the PDI client is `home/<user>/.pentaho/metastore`.
5. 5. Save and close the `plugin.properties` file.
