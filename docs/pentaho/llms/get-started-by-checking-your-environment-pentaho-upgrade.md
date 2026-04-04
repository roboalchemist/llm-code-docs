# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/get-started-by-checking-your-environment-pentaho-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/get-started-by-checking-your-environment-pentaho-upgrade.md

# Get started by checking your environment

Perform the following steps to start the Pentaho Upgrade Installer and check your environment.

1. Exit out of any Pentaho products you currently have running and stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Run the update executable file for the Pentaho Upgrade Installer that you downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us). After processing, the Introduction window opens.
3. Click **Next**.
4. In the License Terms window, read through the license agreement and select the check box at the end of the agreement to acknowledge the terms.
5. Click **Next**.
6. In the Welcome window, select **Upgrade** to upgrade your Pentaho products and then click **Next**.
7. (Optional) If you would like to restore a backup of an original installation before upgrading, select **Restore** and see [Restoring a Pentaho Upgrade Installer backup of archive installation](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/restoring-a-pentaho-upgrade-installer-backup-of-archive-installation-pentaho-upgrade-cp) for instructions.
8. In the **Folder** text box of the Choose Folder window, specify the root directory of your Pentaho installation, and then click **Next**.

   For example, if you originally installed your Pentaho products in the default location on Windows, then you would specify `C:\Pentaho`. **Restore Default Folder** returns the value in the **Folder** text box to the default specified by the Pentaho Upgrade Installer.
9. In the next Pentaho Upgrade Installer window, update the `white_list.csv` file by following the instructions in the [Specify customized items to address after upgrading](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/specify-items-to-include-or-exclude-pentaho-upgrade) topic below. After finishing this procedure, click **Next**.
10. When prompted for the location of the hash files zip archive, specify the path to the archive, select the archive, and then click **Next**.

    **Note:** You can download the hash files zip archive from the [Support Portal](https://support.pentaho.com/home)

The upgrade installer performs an environment check to determine what Pentaho products are installed in the root directory that you specified and whether your environment is compatible for upgrading these products to Pentaho 10.2.

For example, if you are upgrading a server, the environment check may appear similar to the following example:

![Enviroment check while upgrading a Pentaho Server](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-c164b117eebf461346ce200f4e65c1ee2e5a4996%2FssPentahoUpgradeInstaller9-2AndLater_EnvironmentCheck_Server.png?alt=media)

If you are upgrading a workstation, the Environment Check may appear similar to the following sample:

![Environment check while upgrading Pentaho client tools](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-d2617d6cce79f54714354332275b32d30036911a%2FssPentahoUpgradeInstaller9-2AndLater_EnvironmentCheck_DesignTools.png?alt=media)

**Note:** The Pentaho Upgrade Installer is designed to work for the Pentaho 8.3 or later products you have installed in a specified root directory and all the related subdirectories. If you have installed Pentaho products in a root directory separate from the one specified, you must also run the Pentaho Upgrade Installer against that separate root directory to upgrade those other products.
