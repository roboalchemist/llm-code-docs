# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/initialize-postgresql-pentaho-repository-database.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/initialize-postgresql-pentaho-repository-database.md

# Initialize PostgreSQL Pentaho Repository database

The sections in this article take you through the steps to initialize the PostgreSQL Pentaho Repository database.

To initialize PostgreSQL so that it serves as the Pentaho Repository, you will need to run several SQL scripts to create the Hibernate, Quartz, Jackrabbit (JCR), and Pentaho Operations Mart components.

**CAUTION:**

Use the ASCII character set when you run these scripts. Do not use UTF-8 because there are text string length limitations that might cause the scripts to fail.

**CAUTION:**

If you have a different password or user, make sure that you change the password or port number in these examples to match the ones in your configuration.

**CAUTION:**

Pentaho 10.2.0.0 and earlier versions use Quartz 1.x library, which is designated with a `QRTZ5_` prefix in the database. Newer versions, beginning with 10.2.0.1, use Quartz 2.x library, which is designated with a `QRTZ6_`prefix in the database. When upgrading from a previous version to Pentaho 10.2.0.1 and later, you must create the `QRTZ6_` prefixed table in the database by repeating the procedure for Quartz database creation, and then optionally migrating the existing Quartz schedules to the new Quartz database using the migration script. During this upgrade procedure, executing the SQL create script resets the corresponding Quartz database without loss of the original data. However, the other associated repository databases in 10.2.0.1 will be reset by SQL scripts if run and data will be potentially deleted. Always follow best practices and backup your data prior to proceeding.

**Important:** Failure to complete the Quartz upgrade results in a Pentaho Server error at start-up. In addition to the server error, the following exception message is generated in the `catalina.log` file:

```
Missing Quartz library database error
```
