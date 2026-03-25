# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/mandatory-quartz-upgrade-for-versions-10.2.0.1-and-later/initialize-quartz-for-oracle.md

# Initialize Quartz for Oracle

Follow the steps below to initialize a new Quartz database for an Oracle Pentaho Server repository.

**Note:** You may need administrator permissions to run these scripts on the host OS server.

1. Backup your data. See [Back up your existing Pentaho products and install Pentaho 10.2](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/back-up-your-pentaho-products-and-install-pentaho-9.1-pentaho-upgrade).
2. If the Pentaho Server is currently running, stop it.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
3. Make sure that your Oracle instance is up and running.
4. Browse to the `<*your pentaho directory*>/pentaho-server/data/oracle` folder and using any text editor, open the `create_quartz_ora.sql` file.
5. As needed, modify the create script according to your existing setup for the user, password, database, and other required information and then save and close the file.
6. Open a Command Prompt window or a terminal window that runs SQL\*Plus, and then run the creation script:

   `<*your pentaho directory*>/pentaho-server/data/oracle/create_quartz_ora.sql`

   The new Quartz scheduler table prefixed with `QRTZ6_` is created. Any existing `QRTZ5_` scheduler database is retained. However, starting the Pentaho Server at this point will result in an empty schedule.
7. If you want to retain your existing scheduler database, using any text editor, open the `migrate_old_quartz_data_oracle.sql` file.
8. As needed, modify the migration script according to your existing setup for the user, password, database and other required information and then save and close the file.
9. Run the migration script:

   `<*your pentaho directory*>/pentaho-server/data/oracle/migrate_old_quartz_data_oracle.sql`
10. Restart the Pentaho Server.

The original Quartz scheduler database is migrated to the new Quartz database.

**Note:** The original `QRTZ5_` data is retained. You can delete it at your discretion after confirming the migration was successful and complete within the Pentaho Server repository.
