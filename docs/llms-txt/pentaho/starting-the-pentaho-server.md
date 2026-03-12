# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/starting-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/configure-and-start-the-pentaho-server-after-manual-installation/starting-the-pentaho-server.md

# Starting the Pentaho Server

After you have configured the Pentaho Server for your platform, perform the following steps to start the Pentaho Server:

1. Define the **DI\_HOME** environment variable.

   The default path for Windows and Linux is shown below:

   * Windows: `PENTAHO_INSTALLATION_FOLDER\pentaho-server\pentaho-solutions\system\kettle`
   * Linux: `PENTAHO_INSTALLATION_FOLDER/pentaho-server/pentaho-solutions/system/kettle`
2. Run the startup script for your web application server by launching the following applicable startup file for your platform:
   * Windows: Launch the `startup.bat` file, located in the Tomcat `bin` folder.
   * Linux: Launch the `startup.sh` file, located in the Tomcat `bin` directory.
3. From a workstation, open a web browser and enter this URL: `http://localhost:8080/pentaho` to access the Pentaho User Console (PUC).

   The User Console Log On window appears.

   **Note:** If your server has a different hostname or port, replace `localhost` and `8080` with your specific values.
