# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-4-verify-ms-sql-server-initialization.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-4-verify-ms-sql-server-initialization.md

# Step 4: Verify MS SQL Server initialization

**Note:** Unless you change it in Step 1, above, the default password for each username below is `password`.

After you run the scripts, perform the following steps to verify that databases and user roles have been created properly:

1. Open MS SQL Server Management Studio.
2. Log in as: *hibuser*
3. In the **Object Explorer** section, navigate to **hibernate** and verify that you can see the tables.
4. If you installed Pentaho Operations Mart, log in as: *pentaho\_operations\_mart*
5. In the **Object Explorer** section, navigate to **pentaho\_operations\_mart** and verify that you can see the tables.
6. Log in as: *jcr\_user*
7. In the **Object Explorer** section, navigate to **jackrabbit** and verify that you can see the tables.

   The jackrabbit tables may not appear until you have started Pentaho for the first time.
8. Log in as: *pentaho\_user*
9. In the **Object Explorer** section, navigate to **quartz** and verify that you can see the tables.
10. Exit from the MS SQL Server Management Studio tool.

You have initialized the MS SQL Server Pentaho Repository database.
