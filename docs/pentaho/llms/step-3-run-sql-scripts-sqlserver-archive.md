# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-3-run-sql-scripts-sqlserver-archive.md

# Step 3: Run SQL scripts

When upgrading from previous Pentaho versions, including 10.2.0.0 GA to 10.2.0.1 and later, you must manually initialize a new Quartz database. A new Quartz library is created in the repository database as a result. Always follow best practices and backup your data prior to proceeding. If you want to keep your existing Quartz library data, you can migrate the current tables to the new tables.

Run the SQL creation scripts.

**Note:** You may need administrator permissions to run these scripts on the host OS server.

1. Backup your data. See [Back up your existing Pentaho products and install Pentaho 10.2](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/back-up-your-pentaho-products-and-install-pentaho-9.1-pentaho-upgrade).
2. If the Pentaho Server is currently running, stop it.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
3. Make sure that your MS SQL Server instance is up and running.
4. Open a sqlcmd utility window, or from Microsoft SQL Server Management Studio, run the following SQL creation scripts in the order shown:

   1. `<*your pentaho directory*>/pentaho-server/data/sqlserver/create_jcr_sqlServer.sql`
   2. `<*your pentaho directory*>/pentaho-server/data/sqlserver/create_quartz_sqlServer.sql`
   3. `<*your pentaho directory*>/pentaho-server/data/sqlserver/create_repository_sqlServer.sql`
   4. `<*your pentaho directory*>/pentaho-server/data/sqlserver/pentaho_mart_sqlserver.sql`

   The Quartz database, Jackrabbit and MS SQL Server repositories, and Pentaho Operations Mart are created. The new Quartz scheduler table prefixed with `QRTZ6_` is created. Any existing `QRTZ5_` scheduler database is retained. However, starting the Pentaho Server at this point will result in an empty schedule.
5. If you want to retain your existing scheduler database, using any text editor, open the `migrate_old_quartz_data_sqlserver.sql` file.
6. As needed, modify the migration script according to your existing setup for the user, password, database, and other required information and then save and close the file.
7. Run the migration script:

   `<*your pentaho directory*>/pentaho-server/data/sqlserver/migrate_old_quartz_data_sqlserver.sql`

The original Quartz scheduler database is migrated to the new Quartz database.

**Note:** The original `QRTZ5_` data is retained. You can delete it at your discretion after confirming the migration was successful and complete within the Pentaho Server repository.

**Note:** You unpacked the Pentaho Operations Mart SQL file while preparing your environment for the archive installation process. Depending on your environment, see [Prepare your Windows environment for an archive install](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Archive%20installation/Archive%20installation%20process/Prepare%20your%20Windows%20environment%20for%20an%20archive%20install=GUID-B3F10607-0F15-48A2-9000-586C36CE7811=2=en=.md) or [Prepare your Linux environment for an archive install](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install) for details.
