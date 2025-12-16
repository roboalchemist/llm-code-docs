# Source: https://www.metabase.com/docs/latest/databases/connections/mysql

<div>

1.  [Home](/docs/latest/)
2.  [Databases](/docs/latest/databases/start)

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

# MySQL

> This page covers connecting to MySQL as a *data warehouse*. For using MySQL as Metabase's *application database*, see [Configuring the Metabase application database](../../installation-and-operation/configuring-application-database).

To add a database connection, click on the **gear** icon in the top right, and navigate to **Admin settings** \> **Databases** \> **Add a database**.

## Supported versions

Metabase supports the oldest supported version through the latest stable version. See [MySQL end-of-life dates](https://endoflife.software/applications/databases/mysql).

## Edit connection details

You can edit these settings at any time. Just remember to save your changes.

### Connection string

Paste a connection string here to pre-fill the remaining fields below.

### Display name

The display name for the database in the Metabase interface.

### Host

Your database's IP address, or its domain name (e.g., esc.mydatabase.com).

### Port

The database port. E.g., 3306.

### Username

The database username for the account that you want to use to connect to your database. You can set up multiple connections to the same database using different user accounts to connect to the same database, each with different sets of [privileges](../users-roles-privileges).

### Password

The password for the username that you use to connect to the database.

### Use a secure connection (SSL)

You can paste your server's SSL certification chain.

### Use an SSH tunnel

See our [guide to SSH tunneling](../ssh-tunnel).

### Unfold JSON Columns

For MySQL databases, Metabase can unfold JSON columns into component fields to yield a table where each JSON key becomes a column. JSON unfolding is on by default, but you can turn off JSON unfolding if performance is slow.

If you turn on JSON unfolding, you can also toggle the unfolding for individual columns in [table metadata](../../data-modeling/metadata-editing#unfold-json).

### Additional JDBC connection string options

You can append options to the connection string that Metabase uses to connect to your database.

### Re-run queries for simple explorations

Turn this option **OFF** if people want to click **Run** (the play button) before applying any [Summarize](../../questions/query-builder/summarizing-and-grouping) or filter selections.

By default, Metabase will execute a query as soon as you choose an grouping option from the **Summarize** menu or a filter condition from the [drill-through menu](/learn/metabase-basics/querying-and-dashboards/questions/drill-through). If your database is slow, you may want to disable re-running to avoid loading data on each click.

### Choose when syncs and scans happen

See [syncs and scans](../sync-scan#choose-when-syncs-and-scans-happen).

### Periodically refingerprint tables

> Periodic refingerprinting will increase the load on your database.

Turn this option **ON** to scan a sample of values every time Metabase runs a [sync](../sync-scan#how-database-syncs-work).

A fingerprinting query examines the first 10,000 rows from each column and uses that data to guesstimate how many unique values each column has, what the minimum and maximum values are for numeric and timestamp columns, and so on. If you leave this option **OFF**, Metabase will only fingerprint your columns once during setup.

## Connecting to MySQL 8+ servers

Metabase uses the MariaDB connector to connect to MySQL servers. The MariaDB connector lacks support for MySQL 8's default authentication plugin. To connect, you'll need to change the plugin used by the Metabase user:

``` highlight
mysql_native_password`: `ALTER USER 'metabase'@'%' IDENTIFIED WITH mysql_native_password BY 'thepassword';
```

### Unable to log in with correct credentials

**How to detect this:** Metabase fails to connect to your MySQL server with the error message "Looks like the username or password is incorrect", but you're sure that the username and password is correct. You may have created the MySQL user with an allowed host other than the host you're connecting from.

For example, if the MySQL server is running in a Docker container, and your `metabase` user was created with `CREATE USER 'metabase'@'localhost' IDENTIFIED BY 'thepassword';`, the `localhost` will be resolved to the Docker container, and not the host machine, causing access to be denied.

You can identify this issue by looking in the Metabase server logs for the error message:

``` highlight
Access denied for user 'metabase'@'172.17.0.1' (using password: YES).
```

Note the host name `172.17.0.1` (in this case a Docker network IP address), and `using password: YES` at the end.

You'll see the same error message when attempting to connect to the MySQL server with the command-line client: `mysql -h 127.0.0.1 -u metabase -p`.

**How to fix this:** Recreate the MySQL user with the correct host name:

``` highlight
CREATE USER 'metabase'@'172.17.0.1' IDENTIFIED BY 'thepassword';
```

Otherwise, if necessary, a wildcard may be used for the host name:

``` highlight
CREATE USER 'metabase'@'%' IDENTIFIED BY 'thepassword';
```

That user's permissions will need to be set:

``` highlight
GRANT SELECT ON targetdb.* TO 'metabase'@'172.17.0.1';
FLUSH PRIVILEGES;
```

Remember to drop the old user:

``` highlight
DROP USER 'metabase'@'localhost';
```

If you can't connect to the database, but the user, host, and password are correct, try adding `trustServerCertificate=true` to the additional JDBC options. This option will tell the Metabase driver to trust the server certificate even though it lacks a root certificate, and it should establish a secure connection.

## Syncing records that include JSON

**Metabase will infer the JSON "schema" based on the keys in the first five hundred rows of a table.** MySQL JSON fields lack schema, so Metabase can't rely on table metadata to define which keys a JSON field has. To work around the lack of schema, Metabase will get the first five hundred records and parse the JSON in those records to infer the JSON's "schema". The reason Metabase limits itself to five hundred records is so that syncing metadata doesn't put unnecessary strain on your database.

The problem is that, if the keys in the JSON vary record to record, the first five hundred rows may not capture all the keys used by JSON objects in that JSON field. To get Metabase to infer all the JSON keys, you'll need to add the additional keys to the JSON objects in the first five hundred rows.

## Raising a MySQL Docker container of MySQL 8+

If you are spinning up a new MySQL container, and:

-   you want Metabase to connect to the container without having to manually create the user or change the authentication mechanism,
-   or you're facing a `RSA public key is not available client side (option serverRsaPublicKeyFile not set)` error,

Use the `['--default-authentication-plugin=mysql_native_password']` modifiers when you run the container, like so:

-   a simple docker run: `docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=xxxxxx mysql:8.xx.xx --default-authentication-plugin=mysql_native_password`

-   or in docker-compose:

``` highlight
mysql:
  image: mysql:8.xx.xx
  container_name: mysql
  hostname: mysql
  ports:
    - 3306:3306
  environment:
    - "MYSQL_ROOT_PASSWORD=xxxxxx"
    - "MYSQL_USER=metabase"
    - "MYSQL_PASSWORD=xxxxxx"
    - "MYSQL_DATABASE=metabase"
  volumes:
    - $PWD/mysql:/var/lib/mysql
  command: ["--default-authentication-plugin=mysql_native_password"]
```

## Limitations with Vitess-based databases

-   When querying Vitess databases (like Planetscale), you should add a `LIMIT` clause inside each subquery.

    The reason: typically, Metabase applies limits (e.g., 2000 or 10000 rows) to the final query results. But due to a known bug in Vitess, Vitess might apply these limits to subqueries, which can lead to unexpected results (for example, not all rows of results will be displayed within Metabase). The workaround is to add limits to each of your subqueries.

-   You may want to check in with the vendor that's hosting the platform, as Vitess can run into issues returning metadata from the information schema. Metabase needs this metadata to populate its application database; if Metabase can't get that metadata, fields may not appear (or appear empty).

## Passwords with special characters

If your password contains characters that aren't UTF-8, then you might need to add an additional variable to the connection string `passwordCharacterEncoding=<your_encoding_here>`. This ensures that MySQL understands the special characters in the password during authentication.

## Model features

Choose whether to enable features related to [Metabase models](../../data-modeling/models). These features will often require that the database user account, the one you use to connect to your database, has both read and write privileges.

### Model actions

Turn this setting on to allow [actions](../../actions/introduction) from models created from this data to be run. Actions can read, write, and delete data. Your database user will need write permissions.

### Model persistence

We'll create tables with model data and refresh them on a schedule you define. To enable [model persistence](../../data-modeling/model-persistence), you need to grant this connection's credentials read and write permissions on a schema Metabase provides.

## Editable table data

Turn this setting **ON** to enable editing of table data directly within Metabase. When enabled, Admins can create, update, and delete records in your tables through Metabase's interface.

Your database connection will need Write permissions to enable this feature. Meaning: the database user account that you use to connect Metabase to your database must have appropriate privileges to modify data in the tables you want to make editable.

See [privileges](../users-roles-privileges).

## Database routing

With database routing, an admin can build a question once using one database, and the question will run its query against a different database with the same schema depending on who is viewing the question.

See [Database routing](../../permissions/database-routing).

## Danger zone

See [Danger zone](../danger-zone).

## Further reading

-   [MariaDB](./mariadb)
-   [Managing databases](../../databases/connecting)
-   [Metadata editing](../../data-modeling/metadata-editing)
-   [Models](../../data-modeling/models)
-   [Setting data access permissions](../../permissions/data)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/databases/connections/mysql.md) ]