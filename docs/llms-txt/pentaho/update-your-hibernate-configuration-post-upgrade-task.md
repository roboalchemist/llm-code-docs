# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/update-your-hibernate-configuration-post-upgrade-task.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/update-your-hibernate-configuration-post-upgrade-task.md

# Update your Hibernate configuration

The Hibernate configuration file specifies driver and connection information, as well as dialects and how to handle connection closes and timeouts. You must have the latest version of this file for password encryption to work.

Perform the following steps to update the Hibernate configuration file for Pentaho 10.2.

1. Stop the Pentaho Server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/hibernate` directory.
3. Perform the following action depending on whether you have previously customized the `hibernate.cfg.xml` file for your database type:
   * If you have not customized the `hibernate.cfg.xml` file, replace the existing version of the file with the `hibernate.cfg.xml.merge.post-upgrade` file. The `hibernate.cfg.xml.merge.post-upgrade` file is the 10.2 version of the file.
   * If you have customized the `hibernate.cfg.xml` file before upgrading and you have not yet applied these customizations to the 10.2 version of the file, merge your customizations into the `hibernate.cfg.xml` file. See [Apply customizations](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks) for instructions.
4. Restart the server and confirm no errors occurred.

   Depending on the error, you may need to contact your customer support representative for help.

Hibernate now has the Pentaho 10.2 version of this file for password encryption to work.

After setting up Tomcat, Quartz, and Hibernate to work with password encryption, you can now use encrypted passwords with Pentaho 10.2 products. See [Use password encryption with Pentaho](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho) for instructions.
