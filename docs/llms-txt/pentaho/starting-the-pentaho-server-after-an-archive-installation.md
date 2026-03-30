# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/starting-the-pentaho-server-after-an-archive-installation.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/starting-the-pentaho-server-after-an-archive-installation.md

# Starting the Pentaho Server after an archive installation

The Pentaho Server is located on the Pentaho-provided Tomcat web application server. The way you start the Pentaho Server depends on your operating system.

Perform the following steps to start the Pentaho Server.

1. Navigate to the `<*your pentaho directory*>/server/pentaho-server` folder.
2. Run the startup script by launching the appropriate file for your operating system type:

   | Operating system | File                |
   | ---------------- | ------------------- |
   | Windows          | `start-pentaho.bat` |
   | Linux            | `start-pentaho.sh`  |

   The Tomcat web application server and the Pentaho Server start.
3. From a workstation, open a web browser and enter `http://localhost:8080/pentaho` in the address bar.

   **Note:** If your server has a different hostname or port, replace `localhost` or `8080` with your specific values.

   The Pentaho User Console login page appears.
4. Enter your user name and password then click **Login**.

   The Pentaho User Console (PUC) appears.

   **Note:** Upon logging in the first time after installation, you must enter a license server code or the individual license codes for Pentaho before proceeding.

See the **Administer Pentaho Data Integration and Analytics** document for instructions on setting up your licenses and optional Operations Mart logging.

If you are having problems starting the Pentaho Server, visit our [Troubleshooting Guide](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues) for help.
