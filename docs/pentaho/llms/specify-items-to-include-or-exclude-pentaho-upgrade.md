# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/specify-items-to-include-or-exclude-pentaho-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/specify-items-to-include-or-exclude-pentaho-upgrade.md

# Specify customized items to address after upgrading

While checking your environment for Pentaho products and compatibility, the Pentaho Upgrade Installer generates a pre-install report text file and a CSV file (`white_list.csv`) in the `<root installation directory>/Pentaho__Installation` directory. If you have changed items in the default Pentaho setup to apply customizations, you must make sure these items are specified in the `white_list.csv` file before you proceed with the upgrade process. If you have not applied any customizations, you can proceed to [Get started by checking your environment](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/get-started-by-checking-your-environment-pentaho-upgrade).

Customizations may include the following items:

* Configuration files you modified. If these files are listed in the white\_list.csv file, then no action is required.
* Plugins or other software you added to the product, which can include the following items:
  * Additional drivers
  * Custom plugins
  * Other end-user provided code

The upgrade installer uses your updated `white_list.csv` file to generate post-upgrade versions of the listed items separately from your existing versions of these items. After the upgrade process, you may need to merge content from both versions to retain your customizations.

**Note:** Custom directories are directories that you created and are not included in the default Pentaho installation. Custom directories at the `<root installation directory>` level of your Pentaho distributions are ignored by the Pentaho Upgrade Installer.

Perform the following steps to verify the items specified in the CSV file and adjust as needed:

1. Navigate to the `<root installation directory>/Pentaho__Installation` directory.
2. Verify items that you know have changed from the default Pentaho setup are listed in the `white_list.csv` including any drivers, plugins, and other software you added.

   **Note:** If you do not know which items in the report have been modified, contact your system administrator or the [Support Portal](https://support.pentaho.com/hc/en-us) for help.

   The `white_list.csv` file contains the following two comma-separated columns:

   * **Item type**

     The item can be a script, configuration file, JDBC driver, directory, KTR file, or KJB file.
   * **File or directory path**

     The location and file name (if the item is a file) within your Pentaho distribution. The **File or directory path** value can contain regular expressions.

     **Note:** If the item you want to include is a directory, specify the directory name without a directory separator at the end. For example: `<directory_path>/your-directory-name`.
3. After you have updated the `white_list.csv` file, click **Next** to proceed. When the environment check step has completed, review the `preInstallConfigReport.txt` file and verify that all your customizations are present.

   This report contains the following sections:

   * `Files that you must manually merge because they were changed before the upgrade and were also changed in this Pentaho update`
   * `Files that were not able to be automatically mapped. You may need to manually merge these files after the upgrade.`
   * `Files that are handled automatically because they were changed pre-upgrade, but are not changed in this Pentaho update`\
     For example, in a standard Pentaho Server installation, you may have made the following changes:
   * Set up LDAP authentication, and edited the following files:
     * `applicationContext-pentaho-security-ldap.xml`
     * `applicationContext-security-ldap.properties`
     * `applicationContext-spring-security-ldap.xml`
   * Added a custom LDAP authentication solution under `pentaho-solutions/system/my_ldap_solution`.
   * Added a third-party DB driver named `tomcat/webapps/pentaho/WEB-INF/lib/my_db_driver.jar`.
4. After you have completed the environment check, open the `preInstallConfigReport.txt` file and verify that the `applicationContext-pentaho-security-ldap.xml`, `applicationContext-security-ldap.properties`, and `applicationContext-spring-security-ldap.xml` files appear in the `Files that will be handled automatically because they were changed pre-upgrade, but are not changed in this Pentaho update` section.

   Their presence means that your changes to these files will be present after the upgrade, and no further action is required. If changes in the upgrade have impacted these files, they will appear in the `Files that will need manually merged because they were changed pre upgrade and changed in this Pentaho update` section.

   You should not see your `my_ldap_solution` directory or any of its contents listed in that section, nor should you see the `my_db_driver.jar` listed. To preserve your LDAP solution and database driver after the upgrade, you should add the following lines to the `<root_installation_directory>/Pentaho__Installation/white_list.csv` file:

   * `directory,my_ldap_solution`
   * `file,my_db_driver.jar`
5. Click **Previous** in Environment Check window then click **Next** to return to the Environment Check window.

   When you re-run the environment check step, the installer reads the `white_list.csv` again. If any changes were made, the results in the `preInstallConfigReport.txt` will be different.
6. When the environment check is complete, open the `<root installation directory>/Pentaho__Installation/preInstallConfigReport.txt` file again, to verify that your custom code is now listed in the `Files that could not be automatically mapped` section. These files may need to be manually merged after installation section

After the update process is complete, these files will be present in the same location as before the update.
