# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/initialize-postgresql-pentaho-repository-database/step-2-run-sql-scripts-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-2-run-sql-scripts-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-2-run-sql-scripts-postgresql-archive.md

# Step 2: Run SQL scripts

To use PostgreSQL as the database for your Pentaho Repository, you must initialize the Jackrabbit, Quartz, Hibernate, and Operations Mart components used by the Pentaho Repository to work with PostgreSQL. You can run SQL scripts developed by Pentaho to create and initialize these components.

When upgrading from previous Pentaho versions, including 10.2.0.0 GA to 10.2.0.1 and later, you must manually initialize a new Quartz database. A new Quartz library is created in the repository database as a result. Always follow best practices and backup your data prior to proceeding. If you want to keep your existing Quartz library data, you can migrate the current tables to the new tables.

Perform the following steps to run the PostgreSQL-specific initialization SQL scripts provided in the Pentaho Data Integration and Analytics software distribution.

**Note:** You may need administrator permissions to run these scripts on the host OS server.

1. Backup your data. See [Back up your existing Pentaho products and install Pentaho 10.2](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/using-the-pentaho-upgrade-installer/use-the-pentaho-upgrade-installer-to-upgrade-archive-installation/back-up-your-pentaho-products-and-install-pentaho-9.1-pentaho-upgrade).
2. If the Pentaho Server is currently running, stop it.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
3. Make sure that your PostgreSQL instance is up and running.
4. Open a PSQL Console window from a terminal and run the following SQL creation scripts in the order shown:

   1. `<*your pentaho directory*>pentaho-server/data/postgresql/create_quartz_postgresql.sql`
   2. `<*your pentaho directory*>pentaho-server/data/postgresql/create_jcr_postgresql.sql`
   3. `<*your pentaho directory*>pentaho-server/data/postgresql/create_repository_postgresql.sql` to initialize Hibernate
   4. `<*your pentaho directory*>pentaho-server/data/postgresql/pentaho_mart_postgresql.sql`

   The Quartz database, Jackrabbit and Postgresql repositories, and Pentaho Operations Mart are created. The new Quartz scheduler table prefixed with `QRTZ6_` is created. Any existing `QRTZ5_` scheduler database is retained. However, starting the Pentaho Server at this point will result in an empty schedule.
5. If you want to retain your existing scheduler database, using any text editor, open the `migrate_old_quartz_data_postgresql.sql` file.
6. As needed, modify the migration script according to your existing setup for the user, password, database and other required information and then save and close the file.
7. Run the migration script:

   `<*your pentaho directory*>pentaho-server/data/postgresql/migrate_old_quartz_data_postgresql.sql`

The original Quartz scheduler database is migrated to the new Quartz database.

**Note:** The original `QRTZ5_` data is retained. You can delete it at your discretion after confirming the migration was successful and complete within the Pentaho Server repository.

**Note:** You unpacked the Pentaho Operations Mart SQL file while preparing your environment for the archive installation process. Depending on your environment, see [Prepare your Windows environment for an archive install](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Archive%20installation/Archive%20installation%20process/Prepare%20your%20Windows%20environment%20for%20an%20archive%20install=GUID-B3F10607-0F15-48A2-9000-586C36CE7811=2=en=.md) or [Prepare your Linux environment for an archive install](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install) for details.
