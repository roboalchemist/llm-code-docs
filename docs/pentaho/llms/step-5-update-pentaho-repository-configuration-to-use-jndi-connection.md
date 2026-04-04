# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-5-update-pentaho-repository-configuration-to-use-jndi-connection.md

# Step 5: Update Pentaho Repository configuration to use JNDI connection

Update the `repository.xml` file to use the Jackrabbit JNDI connection.

1. Navigate to the `repository.xml` file in the`/server/pentaho-server/pentaho-solutions/jackrabbit/` directory and open it with any text editor.
2. Modify the **url** parameter for the `FileSystem` element. Replace `<param name="url" value="java:comp/env/jdbc/jackrabbit"/>` with `<param name="url" value="java:jboss/datasources/Jackrabbit"/>`.
3. Save and close the file.
