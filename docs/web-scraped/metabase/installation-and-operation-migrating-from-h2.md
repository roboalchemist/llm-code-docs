# Source: https://www.metabase.com/docs/latest/installation-and-operation/migrating-from-h2

<div>

1.  [Home](/docs/latest/)
2.  [Installation and Operation](/docs/latest/installation-and-operation/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Migrating to a production application database

This page covers how to convert a Metabase that's been using the built-in application database, H2, to a production-ready instance PostgreSQL. For more on why you should use Postgres as your app DB, check out [How to run Metabase in production](/learn/metabase-basics/administration/administration-and-operation/metabase-in-production).

If you'd rather move to Metabase Cloud, check out [Migrate to Metabase Cloud](../cloud/migrate/guide).

## Metabase's application database

The main difference between a local installation and a production installation of Metabase is the application database. This application database keeps track of all of your Metabase data: your questions, dashboards, collections, and so on.

Metabase ships with an embedded H2 application database that you should avoid using in production. The reason Metabase ships with the H2 database is because we want people to spin up Metabase on their local machine and start playing around with asking questions.

If you want to run Metabase in production, you'll need to use a production-ready application database to store your application data. You can switch from using the default H2 application database at any time, but if you're planning on running Metabase in production, the sooner you migrate to a production application database, the better. If you keeping running Metabase with the default H2 application database, and you don't regularly back it up, the application database could get corrupted, and you could end up losing all of your questions, dashboards, collections, and other Metabase data.

The migration process is a one-off process. You can execute the migration script from any computer that has the H2 application database file.

### Avoid migrating and upgrading at the same time

One important thing here is that the version of Metabase you use during the migration process must be the same. Meaning, the Metabase you use to run the migration command must be the same one that was last used to create or update H2 file, which must be the same version you'll be using in production. Only *after* completing the migration should you consider upgrading.

You could also choose to run Metabase on a [Metabase Cloud](/pricing/) plan, which takes care of all of this stuff for you. If you have an existing Metabase, here's how you can [migrate to Metabase Cloud](../cloud/migrate/guide).

## Supported databases for storing your Metabase application data

We recommend using PostgreSQL for your application database.

-   [PostgreSQL](https://www.postgresql.org/). Minimum version: `12`. Postgres is our preferred choice for Metabase's application database.
-   [MySQL](https://www.mysql.com/). Minimum version: `8.0.17`. Required settings (which are the default): `utf8mb4_unicode_ci` collation, `utf8mb4` character set, and `innodb_large_prefix=ON`.
-   [MariaDB](https://mariadb.org/). Minimum version: `10.4.0`. Required settings (which are the default): `utf8mb4_unicode_ci` collation, `utf8mb4` character set, and `innodb_large_prefix=ON`.

## JAR: How to migrate from H2 to your production application database

> You must use the same version of Metabase throughout the migration process.

Metabase provides a custom migration command for migrating to a new application database. Here's what you'll do:

-   [1. Confirm that you can connect to your target application database](#1-confirm-that-you-can-connect-to-your-target-application-database)
-   [2. Shut down your Metabase instance](#2-shut-down-your-metabase-instance)
-   [3. Back up your H2 application database](#3-back-up-your-h2-application-database)
-   [4. Run the Metabase data migration command](#4-run-the-metabase-data-migration-command)
-   [5. Start your Metabase](#5-start-your-metabase)

### 1. Confirm that you can connect to your target application database 

You must be able to connect to the target application database in whatever environment you're running this migration command in. So, if you're attempting to move the data to a cloud database, make sure you can connect to that database.

### 2. Shut down your Metabase instance 

You don't want people creating new stuff in your Metabase while you're migrating. Ideally, if you're running the Metabase JAR in production, you're [running Metabase as a service](./running-metabase-as-service).

### 3. Back up your H2 application database 

Safety first! See [Backing up Metabase Application Data](backing-up-metabase-application-data).

### 4. Run the Metabase data migration command 

Run the migration command, `load-from-h2`, using the appropriate [environment variables](../configuring-metabase/environment-variables) for the target database you want to migrate to.

You can find details about specifying databases at [Configuring the application database](configuring-application-database).

Here's an example command for migrating to a Postgres database:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_CONNECTION_URI="jdbc:postgresql://<host>:5432/metabase?user=<username>&password=<password>"
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar load-from-h2 /path/to/metabase.db # do not include .mv.db
```

Here's an example command for migrating to a MySQL database using Java parameter instead of environment variables:

``` highlight
java -DMB_DB_TYPE=mysql -DMB_DB_CONNECTION_URI="jdbc:mysql://<host>:3306/metabase?user=<username>&password=<password>" -jar metabase.jar load-from-h2 metabase.db
```

Note that the file name of the database file itself might be `/path/to/metabase.db.mv.db`, but when running the `load-from-h2` command, you need to truncate the path to `/path/to/metabase.db`.

Metabase expects that you'll run the command against a brand-new (empty) database; it'll create the database schema and migrate the data for you.

### 5. Start your Metabase 

Start your Metabase (with the db connection info, but without the `load-from-h2` and H2 file migration command), and you should be good to go. For example, if you're using Postgres, your command to start Metabase would look something like:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_CONNECTION_URI="jdbc:postgresql://<host>:5432/metabase?user=<username>&password=<password>"
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

You should, however, keep your old H2 file just for safe-keeping, or as a heirloom, or talisman, or whatever.

## Docker: how to migrate from H2 to your production application database

> You must use the same version of Metabase throughout the migration process.

Metabase provides a custom migration command for migrating to a new application database. Here's what you'll do:

-   [1. Confirm that you can connect to your target application database](#1-confirm-that-you-can-connect-to-your-target-application-database-1)
-   [2. Back up your H2 application database](#2-back-up-your-h2-application-database)
-   [3. Stop the existing Metabase container](#3-stop-the-existing-metabase-container)
-   [3. Download the JAR](#3-download-the-jar)
-   [4. Run the migration command](#4-run-the-migration-command)
-   [5. Start a new Docker container that uses the new app db](#5-start-a-new-docker-container-that-uses-the-new-app-db)
-   [7. Remove the old container that was using the H2 database](#7-remove-the-old-container-that-was-using-the-h2-database)

### 1. Confirm that you can connect to your target application database 

You must be able to connect to the target application database in whatever environment you're running this migration command in. So, if you're attempting to move the data to a cloud database, make sure you can connect to that database.

### 2. Back up your H2 application database 

Safety first! See [Backing up Metabase Application Data](backing-up-metabase-application-data).

If you don't back up your H2 database, and you replace or delete your container, you'll lose all of your questions, dashboards, and other Metabase data, so be sure to back up before you migrate.

### 3. Stop the existing Metabase container 

You don't want people creating new stuff in your Metabase while you're migrating.

### 3. Download the JAR 

In the directory where you saved your H2 file (that is, outside the container), [download the JAR](https://github.com/metabase/metabase/releases) for your current version.

Make sure you use the same version of Metabase you've been using. If you want to upgrade, perform the upgrade after you've confirmed the migration is successful.

### 4. Run the migration command 

Create another copy of your H2 file that you extracted from the container when you backed up your app db (step 2).

From the directory with your H2 file and your Metabase JAR, run the migration command, `load-from-h2`. Use the appropriate connection string or [environment variables](../configuring-metabase/environment-variables) for the target database you want to migrate to. The command would look something like:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_CONNECTION_URI="jdbc:postgresql://<host>:5432/metabase?user=<username>&password=<password>"
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar load-from-h2 /path/to/metabase.db # do not include .mv.db
```

Metabase will start up, perform the migration (meaning, it'll take the data from the H2 file and put it into your new app db, in this a Postgres db), and then exit.

See [Configuring the application database](configuring-application-database).

### 5. Start a new Docker container that uses the new app db 

With your new application database populated with your Metabase data, you can start a new container and tell the Metabase in the container to connect to the appdb. The command will looks something like this:

``` highlight
docker run -d -p 3000:3000 \
  -e "MB_DB_TYPE=postgres" \
  -e "MB_DB_DBNAME=<your-postgres-db-name>" \
  -e "MB_DB_PORT=5432" \
  -e "MB_DB_USER=<db-username>" \
  -e "MB_DB_PASS=<db-password>" \
  -e "MB_DB_HOST=<your-database-host>" \
  --name metabase metabase/metabase
```

### 7. Remove the old container that was using the H2 database 

If you have your H2 file backed up somewhere safe, go ahead and remove the old container. See [Docker docs](https://docs.docker.com/engine/reference/commandline/rm/) for removing containers.

## Running Metabase application database migrations manually

When Metabase is starting up, it will typically attempt to determine if any changes are required to the application database, and, if so, will execute those changes automatically. If for some reason you wanted to see what these changes are and run them manually on your database then we let you do that.

Simply set the following environment variable before launching Metabase:

``` highlight
export MB_DB_AUTOMIGRATE=false
```

When the application launches, if there are necessary database changes, you'll receive a message like the following which will indicate that the application cannot continue starting up until the specified upgrades are made:

``` highlight
2015-12-01 12:45:45,805 [INFO ] metabase.db :: Database Upgrade Required

NOTICE: Your database requires updates to work with this version of Metabase.  Please execute the following sql commands on your database before proceeding.

-- *********************************************************************
-- Update Database Script
-- *********************************************************************
-- Change Log: migrations/liquibase.yaml
-- Ran at: 12/1/15 12:45 PM
-- Against: @jdbc:h2:file:/Users/agilliland/workspace/metabase/metabase/metabase.db
-- Liquibase version: 3.4.1
-- *********************************************************************

-- Create Database Lock Table
CREATE TABLE PUBLIC.DATABASECHANGELOGLOCK (ID INT NOT NULL, LOCKED BOOLEAN NOT NULL, LOCKGRANTED TIMESTAMP, LOCKEDBY VARCHAR(255), CONSTRAINT PK_DATABASECHANGELOGLOCK PRIMARY KEY (ID));

...

Once your database is updated try running the application again.

2015-12-01 12:46:39,489 [INFO ] metabase.core :: Metabase Shutting Down ...
```

You can then take the supplied SQL script and apply it to your database manually. Once that's done just restart Metabase and everything should work normally.

## Troubleshooting migration issues

Check out [this troubleshooting guide](../troubleshooting-guide/loading-from-h2).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/migrating-from-h2.md) ]