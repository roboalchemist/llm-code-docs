# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-manual-installation/update-files-in-manual-installation.md

# Update files in manual installation

Update files while upgrading a manual installation by first deleting specified files and then copying upgrade files to specified locations.

Complete the following steps to update files in a manual installation.

1. Navigate to the `<root installation folder>/Pentaho__Installation` folder in your manual installation and delete the following files and folders:
   * `pentaho.war`
   * `pentaho-style.war`
   * All files and folders inside the `pentaho-server/pentaho-solutions` folder
2. Navigate to the upgrade files in the `pentaho-upgrade-files/server/pentaho-server/pentaho-solutions` folder.

   You set up the upgrade files in the previous procedure, [Install upgrade files into empty folder](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-manual-installation/install-upgrade-files-into-empty-folder).
3. Copy the upgrade files from the `pentaho-upgrade-files/server/pentaho-server/pentaho-solutions` folder and paste them into the empty `pentaho-server/pentaho-solutions` folder of your manual installation.
4. Navigate to the `pentaho-upgrade-files/server/pentaho-server/tomcat/webapps/pentaho` folder and compress the folder contents into a ZIP file with the file name `pentaho.war`.
5. Copy the `pentaho.war` file that you created in the previous step into the `<root installation folder>/Pentaho__Installation` folder.
6. Navigate to the `pentaho-upgrade-files/server/pentaho-server/tomcat/webapps/pentaho-style` folder and compress the folder contents into a ZIP file with the file name `pentaho-style.war`.
7. Copy the `pentaho-style.war` file that you created in the previous step into the `<root installation folder>/Pentaho__Installation` folder.

Consider whether to perform post-upgrade tasks listed in the topic, [Post-upgrade tasks](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp).

If you use a Quartz database, consider whether you must upgrade the database by reviewing [Mandatory Quartz upgrade for versions 10.2.0.1 and later](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/mandatory-quartz-upgrade-for-versions-10.2.0.1-and-later).
