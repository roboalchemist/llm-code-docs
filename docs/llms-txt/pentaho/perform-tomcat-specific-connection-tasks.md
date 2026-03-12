# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks.md

# Perform Tomcat-specific connection tasks

After your repository has been configured, you must configure the web application servers to connect to the Pentaho Repository. In this step, you will make JDBC and JNDI connections to the Hibernate, Jackrabbit, and Quartz components.

**Note:** By default, the Pentaho Server software is configured to be deployed and run on the Tomcat server. As such, connections have already been specified and the Tomcat `context.xml` file must be modified ONLY if you have changed the default ports or passwords.

The next couple of sections guide you through the process of working with the JDBC drivers and connection information for Tomcat.
