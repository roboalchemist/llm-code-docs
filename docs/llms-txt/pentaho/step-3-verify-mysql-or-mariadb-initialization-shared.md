# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-3-verify-mysql-or-mariadb-initialization-shared.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-3-verify-mysql-or-mariadb-initialization-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-3-verify-mysql-or-mariadb-initialization-shared.md

# Step 3: Verify MySQL or MariaDB initialization

**Note:** Unless you change it in Step 1, above, the default password for each username below is `password`.

After you run the scripts, perform the following steps to verify that databases and user roles have been created properly:

1. Open the MySQL Workbench tool.

   MySQL Workbench is freely available at the MySQL development site.
2. Log in as: *hibuser*
3. Under **Schemas**, expand **hibernate** then expand **Tables** and verify that you can see the tables.
4. If you installed Pentaho Operations Mart, expand **pentaho\_operations\_mart** then expand **Tables** and verify that you can see the tables.
5. Log in as: *jcr\_user*
6. Under **Schemas**, expand **jackrabbit** then expand **Tables** and verify that you can see the tables.

   The jackrabbit tables may not appear until you have started Pentaho for the first time.
7. Log in as: *pentaho\_user*
8. Under **Schemas**, expand **quartz** then expand **Tables** and verify that you can see the tables.
9. Exit from MySQL Workbench.

You have initialized the MySQL or MariaDB Pentaho Repository database.
