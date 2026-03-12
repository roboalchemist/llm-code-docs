# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-windows/step-4-start-the-pentaho-server.md

# Step 5: Start the Pentaho Server

Perform the following steps to start the Pentaho Server.

1. If you installed your own web application server, run the startup script for the server by launching the applicable batch file for your server type.
   * Tomcat: Launch the `startup.bat` file, located in the Tomcat `bin` directory.
   * JBoss: Launch the `standalone.bat` file, located in the JBoss `bin` directory.
2. From a workstation, open a web browser and enter this URL: `http://localhost:8080/pentaho` to access the Pentaho User Console (PUC).

   **Note:** If your server has a different hostname or port, replace `localhost` and `8080` with your specific values.
