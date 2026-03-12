# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/before-you-begin-pentaho-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/before-you-begin-pentaho-upgrade.md

# Before you begin

Before you can run the Pentaho Upgrade Installer, you must perform the following tasks:

* Verify that your system components are current. Your system components, such as web browsers or repository databases, must be up to date. To verify the system requirements, see [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference).
* When upgrading your environment, stop the server before performing backups and installation. For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
* Review your customizations.
  * For an archive installation, reviewing customization files helps you know which items to specify for inclusion in the post-install report that the upgrade installer generates. You can reference the post-install report while merging customization files back into your installation after upgrading your Pentaho products.
  * For a manual installation, reviewing customizations helps you know which backup files to compare to post-upgrade files so that you can manually merge customization files back into your installation.
* If you are upgrading a manual installation, back up the following files and folders in the `<root installation directory>/Pentaho__Installation` folder of your manual installation:
  * `pentaho.war`
  * `pentaho-style.war`
  * Content and folders inside the `pentaho-server/pentaho-solutions` folder
* If you are using Hadoop clusters with your Pentaho products, review and back up your `site.xml` files.

  **Note:** The upgrade process does not retain the drivers for your Hadoop clusters. You must re-install your drivers after completing the upgrade process. For instructions on installing Hadoop clusters, see [Install drivers for your Hadoop clusters](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/install-drivers-for-your-hadoop-clusters-post-upgrade-tasks).
* If you are using plugins with your Pentaho products, review and back up your plugins to a separate directory structure. The upgrade process does not retain your plugins. You must re-apply your plugins after completing the upgrade process. For instructions on applying plugins, see [Apply your plugins](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-your-plugins-post-upgrade-tasks).
* Verify that no users are logged on to the server. As a best practice, plan to perform the upgrade process of the Pentaho Server during off-business hours to minimize the impact on your day-to-day operations.
* Before installing the Pentaho Upgrade Installer, verify that you have the most recent version of Java installed and that the JAVA\_HOME environment variable is set to that version of Java. To verify Java version requirements, see [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference).
