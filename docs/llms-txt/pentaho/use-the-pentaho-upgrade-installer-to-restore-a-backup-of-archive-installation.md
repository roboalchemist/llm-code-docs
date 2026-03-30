# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/restoring-a-pentaho-upgrade-installer-backup-of-archive-installation-pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-restore-a-backup-of-archive-installation.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/restoring-a-pentaho-upgrade-installer-backup-of-archive-installation-pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-restore-a-backup-of-archive-installation.md

# Use the Pentaho Upgrade Installer to restore a backup of archive installation

You can use the Pentaho Upgrade Installer to restore a backup that was created while creating an archive installation. The following instructions describe the user interface that opens and guides you through the process for restoring a backup generated from a previous upgrade of Pentaho products from an earlier version to version 10.2.

**Note:** Verify that the JAVA\_HOME environment variable is set to the current version of Java that you have installed on your machine before starting the Pentaho Upgrade Installer.

Perform the following steps to restore a Pentaho Upgrade Installer backup of your earlier version of Pentaho products.

1. Exit out of any Pentaho products you currently have running.

   If you are upgrading your Pentaho Server, stop the server. For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Run the update executable file you downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us). After processing, the Pentaho Upgrade Installer interface opens to the Introduction window.
3. Click **Next**
4. In the License Terms window, read through the license agreement and select the checkbox to acknowledge the terms.
5. Click **Next**.
6. In the Welcome window, select **Restore** to restore your Pentaho products and click **Next**.
7. In the table of the Environment Check window, select which archive backup of the environment you want to restore, as shown in the following example:

   ![Using Pentaho Upgrade Installer to restore a selected environment](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-16fabd7c63f5744a96271b8e4bdd7288b85136c9%2FUpgrade_Installer_Restore_Archive.png?alt=media)
8. Click **Next**. You are prompted to confirm that you are replacing the current installation with the selected backup.

   After installation and configuration updates, the upgrade installer shows a Restore Complete message. If errors occur, examine the log files for details about how to resolve the error. Depending on the error, you might need to contact your support representative for help. The default location of the log file is `<*root installation directory*>/*Pentaho\_\_Installation*/logs`.
9. Click **Done** to exit the Pentaho Upgrade Installer.
10. Restart the Pentaho Server.

    For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
