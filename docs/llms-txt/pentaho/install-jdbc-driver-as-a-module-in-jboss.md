# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/install-jdbc-driver-as-a-module-in-jboss.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss.md

# Install JDBC driver as a module in JBoss

In JBoss, JDBC driver information is stored in a module, which is an XML file that you create. You must download the JDBC driver software component to the correct directory, then create `module.xml` files for each database. The [JDBC drivers reference](https://docs.pentaho.com/install/9.3-install/jdbc-drivers-reference) has a list of supported drivers.
