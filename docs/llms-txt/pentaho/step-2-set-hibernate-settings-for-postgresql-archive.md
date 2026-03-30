# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/configure-postgresql-pentaho-repositorydatabase/step-2-set-hibernate-settings-for-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/configure-postgresql-pentaho-repositorydatabase/step-2-set-hibernate-settings-for-postgresql-archive.md

# Step 2: Set Hibernate settings for PostgreSQL

Modify the Hibernate settings file to specify where Pentaho should find the Pentaho Repository’s Hibernate configuration file. The Hibernate configuration file specifies driver and connection information, as well as dialects and how to handle connection closes and timeouts.

**Note:** The Hibernate database is also where the Pentaho Server stores the audit logs that act as source data for the Pentaho Operations Mart.

The files in this section are located in the `pentaho/server/pentaho-server/pentaho-solutions/system/hibernate` directory.

Perform the following steps to specify where Pentaho can find the Hibernate configuration file.

1. Open the `hibernate-settings.xml` file in a text editor. Find the **\<config-file>** tags and confirm that it is configured for PostgreSQL.

   From:

   ```xml
   <config-file>system/hibernate/postgresql.hibernate.cfg.xml</config-file>
   ```
2. Save the file if you made changes, then close the file.
