# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-2-change-default-passwords.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-2-change-default-passwords.md

# Step 2: Change default passwords

For your production server, follow best practices to change the default passwords in the following SQL script files to make the databases more secure.

**Note:** If you are evaluating Pentaho, you might want to skip this step.

1. Browse to the `<*your pentaho directory*>/pentaho-server/data/sqlserver` folder.
2. Use any text editor to modify these create scripts as needed according to your existing setup for the user, password, database, and other required information:
   * `create_jcr_sqlServer.sql`
   * `create_quartz_sqlServer.sql`
   * `create_repository_sqlServer.sql`
   * `pentaho_mart_sqlserver.sql`
3. Save and close the files.
