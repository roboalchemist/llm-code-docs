# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/initialize-postgresql-pentaho-repository-database/step-3-verify-postgresql-initialization-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-3-verify-postgresql-initialization-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database/step-3-verify-postgresql-initialization-reuse.md

# Step 3: Verify PostgreSQL initialization

**Note:** Unless you change it in Step 1, above, the default password for each username below is `password`.

After you run the scripts, perform the following steps to verify that databases and user roles have been created properly:

1. Open the pgAdminIII tool or a similar client tool.
2. Log in as: *hibuser*
3. Verify that you can see the tables under **hibernate**.
4. If you installed Pentaho Operations Mart, verify that you can see the tables under **pentaho\_operations\_mart**.
5. Log in as: *jcr\_user*
6. Verify that you can see the tables under **jackrabbit**.

   The jackrabbit tables may not appear until you have started Pentaho for the first time.
7. Log in as: *pentaho\_user*
8. Verify that you can see the tables under **quartz**.
9. Exit from the tool.

You have initialized the PostgreSQL Pentaho Repository database.
