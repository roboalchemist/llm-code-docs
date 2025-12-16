# Source: https://www.metabase.com/docs/latest/installation-and-operation/configuring-application-database

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

# Configuring the Metabase application database

The application database is where Metabase stores information about user accounts, questions, dashboards, and any other data needed to run the Metabase application. This app DB is distinct from the database where you store your data, also known as your data warehouse. For connecting to your data warehouse, see [Connecting to a supported database](../databases/connecting).

For production, we recommend using PostgreSQL as your Metabase application database.

-   [PostgreSQL](#postgresql) (recommended for production)
-   [MySQL or MariaDB](#mysql-or-mariadb) (also works for production)
-   [H2](#h2-application-database) (default for local demos - AVOID in production)

Metabase will read the connection configuration information when the application starts up. You can't change the application database while the application is running.

## PostgreSQL

We recommend that you use [PostgreSQL](https://www.postgresql.org/) for your Metabase application database. Metabase supports the oldest supported version of PostgreSQL through the latest stable version. See [PostgreSQL versions](https://www.postgresql.org/support/versioning/).

You can use [environment variables](../configuring-metabase/environment-variables) to set a Postgres database as Metabase's application database. For example, the following commands tell Metabase to use a Postgres database as its application database:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabase
export MB_DB_PORT=5432
export MB_DB_USER=<username>
export MB_DB_PASS=<password>
export MB_DB_HOST=localhost
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Metabase will not create a Postgres database for you. Example command to create the database:

``` highlight
createdb --encoding=UTF8 -e metabase
```

If you have additional parameters, Metabase also supports providing a full JDBC connection string:

``` highlight
export MB_DB_CONNECTION_URI="jdbc:postgresql://localhost:5432/metabase?user=<username>&password=<password>"
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

If you want to pass the connection URI, user, and password credentials separately from the JDBC connection string (useful if the password contains special characters), you can use the `MB_DB_CONNECTION_URI` [environment variable](../configuring-metabase/environment-variables) in combination with `MB_DB_USER` and `MB_DB_PASS` variables:

``` highlight
export MB_DB_CONNECTION_URI="jdbc:postgresql://localhost:5432/metabase"
export MB_DB_USER=<username>
export MB_DB_PASS=<password>
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

## MySQL or MariaDB

We recommend [PostgreSQL](#postgresql), but you can also use [MySQL](https://www.mysql.com/) or [MariaDB](https://www.mariadb.org/).

The minimum recommended version is MySQL 8.0.17 or MariaDB 10.2.2. The `utf8mb4` character set is required.

We don't support ApsaraDB MySQL. You can instead use ApsaraDB PostgreSQL.

You can change the application database to use MySQL using environment variables like so:

``` highlight
export MB_DB_TYPE=mysql
export MB_DB_DBNAME=metabase
export MB_DB_PORT=3306
export MB_DB_USER=<username>
export MB_DB_PASS=<password>
export MB_DB_HOST=localhost
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Metabase won't create this database for you. Example SQL statement to create the database:

``` highlight
CREATE DATABASE metabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

The following command will tell Metabase to look for its application database using the supplied MySQL connection information. Metabase also supports providing a full JDBC connection string if you have additional parameters:

``` highlight
export MB_DB_CONNECTION_URI="jdbc:mysql://localhost:3306/metabase?user=<username>&password=<password>"
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

As with Postgres, `MB_DB_CONNECTION_URI` can also be used in combination with `MB_DB_USER` and/or `MB_DB_PASS` if you want to pass one or both separately from the rest of the JDBC connection string:

``` highlight
export MB_DB_CONNECTION_URI="jdbc:mysql://localhost:5432/metabase"
export MB_DB_USER=<username>
export MB_DB_PASS=<password>
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

## H2 application database

> **For production installations of Metabase we recommend that people [replace the default H2 database with PostgreSQL](./migrating-from-h2)**. Postgres offers a greater degree of performance and reliability.

By default, Metabase ships with an [H2 database](https://www.h2database.com/) to make it easy to demo Metabase on your local machine. **Avoid using this default database in production**.

If when launching Metabase you don't provide environment variables that specify connection details for a production database, Metabase will attempt to create a new H2 database in the same directory as the Metabase JAR.

H2 is a file-based database, and you can see these H2 database files from the terminal:

``` highlight
ls metabase.*
```

You should see the following files:

``` highlight
metabase.db.h2.db  # Or metabase.db.mv.db depending on when you first started using Metabase.
metabase.db.trace.db
```

If you want to use an H2 database file in a particular directory, use the `MB_DB_TYPE` and `MB_DB_FILE` environment variables:

``` highlight
export MB_DB_TYPE=h2
export MB_DB_FILE=/the/path/to/my/h2.db
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Note that H2 automatically appends `.mv.db` or `.h2.db` to the path you specify; exclude those extensions in your path! In other words, `MB_DB_FILE` should be something like `/path/to/metabase.db`, rather than something like `/path/to/metabase.db.mv.db` (even though the latter is the file that Metabase will create).

## Migrating from H2

If you've started out using the default, H2 database, but you want to preserve the content you've created and move to a production application database, Metabase provides limited support for [migrating from H2 to PostgreSQL](migrating-from-h2).

## Upgrading from a Metabase version pre-0.38 

If you're upgrading from a previous version of Metabase, note that for Metabase 0.38 we've removed the use of the PostgreSQL `NonValidatingFactory` for SSL validation. It's possible that you could experience a failure either at startup (if you're using a PostgreSQL application database) or when querying a PostgreSQL data warehouse.

You can resolve this failure in one of two ways:

1.  Configuring the PostgreSQL connection to use SSL certificate validation,
2.  Or manually enabling the `NonValidatingFactory`. WARNING: this method is insecure. We're including it here only to assist in troubleshooting, or for situations in which security is not a priority.

How you configure your connection depends on whether you're using Postgres as Metabase's application database or as a data warehouse connected to Metabase:

### SSL certificate validation for Postgres *application* databases

To use SSL certificate validation, you'll need to use the `MB_DB_CONNECTION_URI` environment variable to configure your database connection. Here's an example:

``` highlight
export MB_DB_CONNECTION_URI="postgres://localhost:5432/metabase?user=<username>&password=<password>&sslmode=verify-ca&sslrootcert=<path to CA root or intermediate root certificate>"
```

If you can't enable certificate validation, you can enable the `NonValidatingFactory` for your application database:

``` highlight
export MB_DB_CONNECTION_URI="postgres://localhost:5432/metabase?user=<username>&password=<password>&ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory"
```

### SSL certificate validation for Postgres *data warehouse* databases

Add the following to the end of your JDBC connection string for your database:

``` highlight
&sslmode=verify-ca&sslrootcert=<path to CA root or intermediate root certificate>
```

If that fails, you can enable `NonValidatingFactory` by adding the following to the end of your connection URI for your database:

``` highlight
&ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory
```

For more options to further tune the SSL connection parameters, see the [PostgreSQL SSL client documentation](https://jdbc.postgresql.org/documentation/ssl/#configuring-the-client).

## Further reading

-   [Environment variables](../configuring-metabase/environment-variables)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/configuring-application-database.md) ]