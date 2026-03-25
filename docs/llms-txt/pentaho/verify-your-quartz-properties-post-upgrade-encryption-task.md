# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/verify-your-quartz-properties-post-upgrade-encryption-task.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/verify-your-quartz-properties-post-upgrade-encryption-task.md

# Verify your Quartz properties

Event information, such as scheduled reports, is stored in the Quartz JobStore. Quartz must be set up with JNDI for password encryption to work.

Perform the following steps to verify the `quartz.properties` file has the correct JNDI information:

1. Stop the Pentaho Server.

   For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `server/pentaho-server/pentaho-solutions/scheduler-plugin/quartz` directory and open the `quartz.properties` file with any file editor.
3. Verify the following line of code appears in the file:

   `org.quartz.dataSource.myDS.jndiURL = Quartz`
4. If the line of code associated with JNDI does not appear in the `quartz.properties` file, perform the following action depending on whether you have any previous customizations to the `quartz.properties` file:
   * If you have not customized the `quartz.properties` file, add the line of code to the file.
   * If you have customized the `quartz.properties` file before upgrading and you have not already applied these customizations to the 10.2 version of the file, merge your customizations into the `quartz.properties` file. See [Apply customizations](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks) for instructions.
5. Close the `quartz.properties` file.
6. Restart the server and confirm no errors occurred.

   Depending on the error, you may need to contact your customer support representative for help.

Quartz is now set up with JNDI for password encryption to work.
