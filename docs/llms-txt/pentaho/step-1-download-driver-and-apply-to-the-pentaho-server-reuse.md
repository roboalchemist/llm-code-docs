# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-1-download-driver-and-apply-to-the-pentaho-server-reuse.md

# Step 1: Download driver and apply to the Pentaho Server

To connect to a database, including the Pentaho Repository database, you will need to download and copy a JDBC driver to the appropriate places for the Pentaho Server as well as on the web application server.

**Note:** Due to licensing restrictions, Pentaho cannot redistribute some third-party database drivers. You must download and install the file yourself.

1. Download a JDBC Driver JAR from your database vendor or a third-party driver developer.

   The [JDBC drivers reference](https://docs.pentaho.com/install/10.2-install/jdbc-drivers-reference) has a list of supported drivers.
2. Copy the JDBC driver JAR you just downloaded to the `pentaho/server/pentaho-server/tomcat/lib` folder.
3. Copy the [`hsqldb-2.3.2.jar`](https://sourceforge.net/projects/hsqldb/files/hsqldb/hsqldb_2_3/) file to `pentaho-server/tomcat/lib` if you want to retain the sample provided by Pentaho.
