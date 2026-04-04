# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/back-up-your-pentaho-products-and-install-pentaho-9.1-pentaho-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/back-up-your-pentaho-products-and-install-pentaho-9.1-pentaho-upgrade.md

# Back up your existing Pentaho products and install Pentaho 10.2

Perform the following steps in the Pentaho Upgrade Installer to back up your existing installation and apply the new Pentaho 10.2 installation:

1. If you have any customizations, after you verify the items in the `white_list.csv`file, return to the Pentaho Upgrade Installer and click **Next** to back up your existing Pentaho installation.

   **Note:** Contact customer support if your expected Pentaho products do not appear in the list. The Pentaho Upgrade Installer backs up your existing versions of the Pentaho products, which you can use to restore the earlier version after upgrading to version 10.2. If you decide to restore the backup, see [Restoring a Pentaho Upgrade Installer backup of archive installation](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/restoring-a-pentaho-upgrade-installer-backup-of-archive-installation-pentaho-upgrade-cp) for instructions.
2. In the Backup window, after the backup completes to 100%, click **Next**.

   The Pre-Installation Summary window appears, as shown in the following example:

   ![Pre-Installation Summary in Pentaho Upgrade Installer](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-c6446d22e180c942a902bbfbcc2df939422d096d%2FssPentahoUpgradeInstaller_PreInstallationSummary.png?alt=media)

   **Note:** If you cancel the upgrade process after the backup of your environment is created but before the 10.2 installation, the backup is not used by the Pentaho Upgrade Installer in any future upgrade process. To remove the backup ZIP file, navigate to the `~/.pentaho/backup` directory and delete the ZIP file related to the date when the backup was performed.
3. Verify the information in the Pre-Installation Summary window, and then click **Install**.

   If the summary information is not what you expected, click **Previous** to modify any previous settings.
4. After the installation and configuration updates complete in the Installing Pentaho window, click **Next**.

   If errors occur, examine the log files for details about how to resolve the error. Depending on the error, you may need to contact customer support for help. The default location of the log files is `<root installation directory>/Pentaho__Installation/logs`.

   After the installation part of the upgrade process, a post-install report is generated to specify which files may have been modified from the default Pentaho setup for customizations.
5. In the Install Complete window, click **Done** to exit the Pentaho Upgrade Installer.
6. Apply the version 10.2 licenses to your upgraded Pentaho products.

   See the **Administer Pentaho Data Integration and Analytics** document for instructions on managing licenses.
7. (Optional) If you have modified any items from the default Pentaho setup for customizations, use the post-install report to determine which items need to be merged.

   See the [Apply customizations](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks) post-upgrade task for instructions.
8. Restart the Pentaho Server.

   For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).

After you upgrade your Pentaho products, complete these [Post-upgrade tasks](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp) to verify that your Pentaho configuration is ready to use.
