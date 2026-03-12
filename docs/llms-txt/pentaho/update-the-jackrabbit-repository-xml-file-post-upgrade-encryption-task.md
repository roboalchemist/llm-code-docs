# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/update-the-jackrabbit-repository-xml-file-post-upgrade-encryption-task.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/update-the-jackrabbit-repository-xml-file-post-upgrade-encryption-task.md

# Update the Jackrabbit Repository XML file

The Jackrabbit component contains the solution repository, examples, security data, and content data from reports that you create in Pentaho. You must use the latest version of the `repository.xml` file if you plan to apply password encryption.

Perform the following steps to update the `repository.xml` file to use password encryption.

1. If you are using a database other than Postgres for your Pentaho Repository, perform the following substeps:
   1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/jackrabbit` directory and open the `repository.xml` file with any file editor.
   2. Comment out any references to databases other than the database you are using for the Pentaho Repository in each of the following sections, and uncomment the sections that apply to your database:
      * Repository
      * DataStore
      * Workspaces
      * PersistenceManager (1st part)
      * Versioning
      * PersistenceManager (2nd part)
      * DatabaseJournal
   3. Save and close the `repository.xml` file.
2. If your `repository.xml` file contained any customizations before upgrading and you have not yet applied these customizations to the 10.2 version of the file, merge your customizations into the `repository.xml` file. See [Address customizations to upgraded archive installation](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks/address-customizations-to-upgraded-archive-installation-post-upgrade-customization-task) for instructions.
3. Stop and restart the server to confirm no errors occurred.

   For instructions on stopping and starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).

   Depending on the error, you may need to contact your customer support representative for help.
