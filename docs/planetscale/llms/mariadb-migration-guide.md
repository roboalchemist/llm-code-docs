# Source: https://planetscale.com/docs/vitess/imports/mariadb-migration-guide.md

# MariaDB migration guide

## Overview

In this article, you’ll learn how to migrate a database from MariaDB, a fork of MySQL, into PlanetScale.

<Warning>
  The steps outlined in this guide used MariaDB version 10.6.12 on an Ubuntu host. Depending on the version of MariaDB you are using, your results may vary. Don't hesitate to [reach out to us](https://planetscale.com/contact) for further assistance.
</Warning>

We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

### Prerequisites

* A PlanetScale account
* A MariaDB server with traffic permitted from our [import tool IP addresses](/docs/vitess/imports/import-tool-migration-addresses)

## Configure MariaDB

Before you can start migrating data, there are a number of configuration options that need to be in place for our import tool to work properly:

* `binlog_format`
* `log_bin`
* `sql_mode`

You may run the following query to check these values:

```sql  theme={null}
SHOW variables WHERE Variable_name IN ('binlog_format','log_bin','sql_mode');

+---------------+-------------------------------------------------------------------------------------------+
| Variable_name | Value                                                                                     |
+---------------+-------------------------------------------------------------------------------------------+
| binlog_format | MIXED                                                                                     |
| log_bin       | OFF                                                                                       |
| sql_mode      | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+-------------------------------------------------------------------------------------------+
```

In the results listed above, none of the options are configured properly, so let’s set them up now. The exact path to your configuration file varies by operating system. This demo uses Ubuntu, so the MariaDB configuration file is located at `/etc/mysql/mariadb.conf.d/50-server.cnf`. Edit the configuration file and add the following values at the end of the file:

```
binlog_format = ROW
log_bin = /var/log/mysql/mysql-bin.log
sql_mode = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,ONLY_FULL_GROUP_BY'
```

With the configuration updated, restart the MariaDB service. The exact command varies by the service manager you are using on your host, with this demo using `systemctl`:

```bash  theme={null}
sudo systemctl restart mariadb
```

## Configure a migration account

The PlanetScale import tool requires a user account with a specific set of permissions on the database you wish to migrate, as well as the server itself to set up the necessary database that tracks replication changes. To create a user named `migration_user`, run the following:

```sql  theme={null}
CREATE USER 'migration_user'@'%' IDENTIFIED BY '<SUPER_STRONG_PASS>';
```

Next, configure the proper grants to allow `migration_user` to set up replication:

```sql  theme={null}
GRANT PROCESS, REPLICATION SLAVE, REPLICATION CLIENT, RELOAD ON *.* TO 'migration_user'@'%';
```

Now you can configure the necessary permissions on the database you wish to migrate. Replace `<DATABASE_NAME>` with the name of your database in MariaDB:

```sql  theme={null}
GRANT SELECT, INSERT, UPDATE, DELETE, SHOW VIEW, LOCK TABLES ON `<DATABASE_NAME>`.* TO 'migration_user'@'%';
```

Finally, you’ll need to configure permissions for a database named `ps_import_<id>` (the last portion of the name will vary) that will be created by the import tool to track replication between MariaDB and PlanetScale.

```sql  theme={null}
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON `ps\_import\_%`.* TO 'migration_user'@'%';
```

For a full explanation on what each of these grants do, [our article on configuring a migration account for MySQL databases](/docs/vitess/imports/import-tool-user-requirements) details each requirement.

## Importing your database

Now that your MariaDB database is configured and ready, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use the following information:

* **Host name** - Your MariaDB server hostname or IP address
* **Port** - 3306 (default for MariaDB)
* **Database name** - The exact database name to import
* **Username** - `migration_user` (created in previous section)
* **Password** - The password you set for the migration user
* **SSL verification mode** - Select based on your MariaDB SSL configuration

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your MariaDB database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt