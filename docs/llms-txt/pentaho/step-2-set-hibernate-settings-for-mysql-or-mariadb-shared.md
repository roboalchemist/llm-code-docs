# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-2-set-hibernate-settings-for-mysql-or-mariadb-shared.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-2-set-hibernate-settings-for-mysql-or-mariadb-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-2-set-hibernate-settings-for-mysql-or-mariadb-shared.md

# Step 2: Set Hibernate settings for MySQL or MariaDB

Modify the Hibernate settings file to specify where Pentaho should find the Pentaho Repository’s Hibernate configuration file. The Hibernate configuration file specifies driver and connection information, as well as dialects and how to handle connection closes and timeouts.

**Note:** The Hibernate database is also where the Pentaho Server stores the audit logs that act as source data for the Pentaho Operations Mart.

The files in this section are located in the `pentaho/server/pentaho-server/pentaho-solutions/system/hibernate` directory.

Perform the following steps to specify where Pentaho can find the Hibernate configuration file.

1. Open the `hibernate-settings.xml` file in a text editor. Find the **\<config-file>** tags and change `postgresql.hibernate.cfg.xml` to `mysql5.hibernate.cfg.xml` as shown.

   From:

   ```xml
   <config-file>system/hibernate/postgresql.hibernate.cfg.xml</config-file>
   ```

   To:

   ```xml
   <config-file>system/hibernate/mysql5.hibernate.cfg.xml</config-file>
   ```
2. Save and close the file.
3. (MariaDB only) Open the file `mysql5.hibernate.cfg.xml` in a text editor. Find the driver class and change it from MySQL to MariaDB as shown.

   From:

   ```
   <property name="connection.driver_class">com.mysql.jdbc.Driver</property>
   ```

   To:

   ```
   <property name="connection.driver_class">org.mariadb.jdbc.Driver</property>
   ```
