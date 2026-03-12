# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/initialize-oracle-pentaho-repository-database/step-3-verify-oracle-initialization.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/initialize-oracle-pentaho-repository-database/step-3-verify-oracle-initialization.md

# Step 3: Verify Oracle initialization

**Note:** Unless you change it in Step 1, above, the default password for each username below is `password`.

After you run the scripts, perform the following steps to verify that databases and user roles have been created properly:

1. Open a Terminal or Command Prompt window that is running SQL\*Plus or a similar client tool and connect to the Oracle database.
2. Log in as: *hibuser*
3. Verify that you can see the tables under **hibernate**.
4. If you installed Pentaho Operations Mart, verify that you can see the tables under **pentaho\_operations\_mart**.
5. Log in as: *jcr\_user*
6. Verify that you can see the tables under **jackrabbit**.

   The jackrabbit tables may not appear until you have started Pentaho for the first time.
7. Log in as: *pentaho\_user*
8. Verify that you can see the tables under **quartz**.
9. Exit from the tool.

You have initialized the Oracle Pentaho Repository database.
