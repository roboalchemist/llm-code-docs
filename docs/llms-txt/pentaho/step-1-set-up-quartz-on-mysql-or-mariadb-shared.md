# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-1-set-up-quartz-on-mysql-or-mariadb-shared.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-1-set-up-quartz-on-mysql-or-mariadb-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-1-set-up-quartz-on-mysql-or-mariadb-shared.md

# Step 1: Set up Quartz on MySQL or MariaDB

Event information, such as scheduled reports, is stored in the Quartz JobStore. During the installation process, you must indicate where the JobStore is located by modifying the `quartz.properties` file.

1. Open the `pentaho/server/pentaho-server/pentaho-solutions/system/scheduler-plugin/quartz/quartz.properties` file in any text editor.
2. Locate the **#\_replace\_jobstore\_properties** section and set the **org.quartz.jobStore.driverDelegateClass** as shown:

   ```xml
   org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.StdJDBCDelegate
   ```
3. Save the file and close the text editor.
