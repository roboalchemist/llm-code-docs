# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/initialize-postgresql-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/initialize-oracle-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/initialize-oracle-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-1-change-default-passwords.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-1-change-default-passwords.md

# Step 1: Change default passwords

For your production server, follow best practices to change the default passwords in the following SQL script files to make the databases more secure.

**Note:** If you are evaluating Pentaho, you might want to skip this step.

1. Browse to the `<*your pentaho directory*>/pentaho-server/data/postgresql` folder.
2. Use any text editor to modify these create scripts as needed according to your existing setup for the user, password, database, and other required information:
   * `create_jcr_postgresql.sql`
   * `create_quartz_postgresql.sql`
   * `create_repository_postgresql.sql`
   * `pentaho_mart_postgresql.sql`
3. Save and close the files.
