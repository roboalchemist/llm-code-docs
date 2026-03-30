# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer-in-silent-mode-cp/using-silent-mode-to-upgrade-pentaho-products/use-silent-mode-to-upgrade-manual-installation-pentaho-upgrade-installer-silent-mode.md

# Use silent mode to upgrade manual installation

To upgrade a manual installation without using a graphical interface, use silent mode to install upgrade files into an empty folder, copy those upgrade files into your existing installation, and then update any customizations that you made to your installation.

Perform the following steps to upgrade a manual installation in silent mode:

1. Exit out of any Pentaho products that you are currently running.

   If you are upgrading your Pentaho Server, stop the server. For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Install upgrade files into an empty folder by completing the following sub steps:
   1. Open a command line interface.
   2. Run one of the following commands to install upgrade files to an empty folder named `pentaho-upgrade-files`:

      * **Linux**

        `/pentaho-update-<version>.bin -i silent -DEULA=true -DUSER_INSTALL_DIR=/<filepath>/pentaho-upgrade-files/ -DHASH_ZIP_FILE=/<filepath>/installer-hash-files-<version>.zip -DFRESH_INSTALL=true`
      * **Windows**

        `/pentaho-update-<version>.exe -i silent -DEULA=true -DUSER_INSTALL_DIR=/<filepath>/pentaho-upgrade-files/ -DHASH_ZIP_FILE=/<filepath>/installer-hash-files-<version>.zip -DFRESH_INSTALL=true`

      Upgrade files are installed into an empty folder named `pentaho-upgrade-files` at the `filepath` that you specified.
3. Copy the upgrade files that you installed in the previous step to your existing manual installation by completing the following sub steps:
   1. Navigate to the `<root installation folder>/Pentaho__Installation` folder in your manual installation and delete the following files and folders:
      * `pentaho.war`
      * `pentaho-style.war`
      * All files and folders inside the `pentaho-server/pentaho-solutions` folder
   2. Copy the upgrade files from the `pentaho-upgrade-files/server/pentaho-server/pentaho-solutions` folder and paste them into the empty `pentaho-server/pentaho-solutions` folder of your manual installation.
   3. Navigate to the `pentaho-upgrade-files/server/pentaho-server/tomcat/webapps/pentaho` folder and compress the folder contents into a ZIP file with the file name `pentaho.war`:
   4. Copy the `pentaho.war` file that you created in the previous step and paste the file into the `<root installation folder>/Pentaho__Installation` folder of your manual installation.
   5. Navigate to the `pentaho-upgrade-files/server/pentaho-server/tomcat/webapps/pentaho-style` folder contents and compress the folder into a ZIP file with the file name `pentaho-style.war`.
   6. Copy the `pentaho-style.war` file that you created in the previous step and paste the file into the `<root installation folder>/Pentaho__Installation` of your manual installation.
4. Start the Pentaho Server.

   For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).

   **Note:** If you plan to test that the Pentaho Server is running, clear the cache in your browser that you use to access the Pentaho Server.

After you upgrade your Pentaho products, complete these [Post-upgrade tasks](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp) to verify that your Pentaho configuration is ready to use.
