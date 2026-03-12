# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database.md

# Configure PostgreSQL Pentaho Repository database

Now that you have initialized your repository database, you will need to configure Quartz, Hibernate, Jackrabbit, and Pentaho Operations Mart for a PostgreSQL database.

**Note:** PostgreSQL is configured by default; if you keep the default passwords and port, you will not need to set up Quartz, Hibernate, Jackrabbit or the Pentaho Operations Mart. You can skip ahead to the [Tomcat-specific connection tasks](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks).

By default, the examples in this section are for a PostgreSQL database that runs on port 5432. The default password is also in these examples.

**CAUTION:**

If you have a different port or different password, make sure that you change the password and port number in these examples to match the ones in your configuration.
