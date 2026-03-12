# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks/address-customizations-to-upgraded-manual-installation.md

# Address customizations to upgraded manual installation

Address customizations to your manual installation by reviewing modified configuration files in the backup folder that you created while upgrading the installation.

If the manual installation that you are upgrading has modified configuration files in the `pentaho-server/pentaho-solutions` backup folder, manage those modifications by completing the following steps:

1. Navigate to the files you backed up before upgrading.

   For the list of files that you backed up before upgrading, see [Before you begin](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/before-you-begin-pentaho-upgrade).
2. Identify the modifications that you made by comparing your backup configuration files to the current files in the `pentaho-server/pentaho-solutions` folder of your manual installation.
3. Merge modifications that you identify into the files in the `pentaho-server/pentaho-solutions` folder of your manual installation.
