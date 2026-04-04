# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database/step-1-set-up-quartz-on-postgresql.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/configure-postgresql-pentaho-repositorydatabase/step-1-set-up-quartz-on-postgresql.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database/step-1-set-up-quartz-on-postgresql.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/configure-postgresql-pentaho-repositorydatabase/step-1-set-up-quartz-on-postgresql.md

# Step 1: Set up Quartz on PostgreSQL

Event information, such as scheduled reports, is stored in the Quartz JobStore. During the installation process, you must indicate where the JobStore is located by modifying the `quartz.properties` file.

1. Open the `pentaho/server/pentaho-server/pentaho-solutions/system/scheduler-plugin/quartz/quartz.properties` file in any text editor.
2. Locate the **#\_replace\_jobstore\_properties** section and set the **org.quartz.jobStore.driverDelegateClass** as shown:

   ```xml
   org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.PostgreSQLDelegate
   ```
3. Save the file and close the text editor.
