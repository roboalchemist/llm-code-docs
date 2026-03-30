# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/defining-jndi-connections-for-pdi-clients.md

# Defining JNDI connections for PDI clients

If you are publishing to the Pentaho Server from a PDI client, Pentaho supplies a method for you to configure your PDI client to have the same JNDI connection information as the Pentaho Server. By using this method, your application server will not be continuously running during the development and testing of transformations.

* To configure a JNDI connection for your PDI client, edit the `jdbc.properties` file to mirror the JNDI connection information of your application server data sources. The `jdbc.properties` file is located here: `/pentaho/design-tools/data-integration/simple-jndi`.
