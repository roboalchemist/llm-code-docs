# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration/starting-and-stopping-the-pentaho-server-on-linux/pentaho-installation-wizard.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration/starting-and-stopping-the-pentaho-server-on-windows/pentaho-installation-wizard.md

# Pentaho Installation Wizard

If you ran the Pentaho Installation Wizard on Windows, then the Pentaho Server is deployed in an Apache Tomcat application server. You can manage both the Pentaho and Tomcat servers by clicking **Start** > **All Programs** > **Pentaho Enterprise Edition** > **Server Management** and selecting one of these menu items:

* **Start Pentaho Server**
* **Stop Pentaho Server**

The installation wizard also registered the Pentaho Server, as well as the Pentaho Repository, as services. These services are set to run automatically, enabling them to start and stop when the computer running them boots up or shuts down. You can use the Windows Services applet found in the Control Panel to start and stop the Pentaho Server and the Pentaho Repository.

1. Click **Start** > **Control Panel** > **Administrative Tools** > **Services**.
2. In the Services window, right-click on one of these services in the list and take the appropriate action:
   * **Pentaho Server**
   * **Data Integration**
   * **Pentaho Repository**
