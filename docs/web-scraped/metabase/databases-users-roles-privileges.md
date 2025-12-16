# Source: https://www.metabase.com/docs/latest/databases/users-roles-privileges

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

# Database users, roles, and privileges

We recommend creating a `metabase` database user with the following database roles:

-   [`analytics` for read access](#minimum-database-privileges) to any schemas or tables used for analysis.
-   Optional [`metabase_actions` for write access](#privileges-to-enable-actions-and-editable-table-data) to tables used for Metabase actions.
-   Optional [`metabase_model_persistence` for write access](#privileges-to-enable-model-persistence) to the schema used for Metabase model persistence.

Bundling your privileges into roles based on use cases makes it easier to manage privileges in the future (especially in [multi-tenant situations](#multi-tenant-permissions)). For example, you could:

-   Use the same `analytics` role for other BI tools in your [data stack](/learn/grow-your-data-skills/data-fundamentals/data-landscape) that need read-only access to the analytics tables in your database.
-   Revoke the write access for `metabase_model_persistence` without affecting the write access for `metabase_actions`.

## Minimum database privileges

In order to view and query your tables in Metabase, you'll have to give Metabase's database user:

-   `CONNECT` to your database.
-   `SELECT` privileges to any schemas or tables that you want to use in Metabase.

To organize these privileges (and make maintenance easier down the line):

-   Create a database role called `analytics`.
-   Create a database user called `metabase`.
-   Add `metabase` to the `analytics` role.
-   Add privileges to the `analytics` role.

For example, if you're using a Postgres database, you'd log in as an admin and run the SQL statements:

``` highlight
-- Create a role named "analytics".
CREATE ROLE analytics WITH LOGIN;

-- Add the CONNECT privilege to the role.
GRANT CONNECT ON DATABASE "your_database" TO analytics;

-- Create a database user named "metabase".
CREATE USER metabase WITH PASSWORD "your_password";

-- Give the role to the metabase user.
GRANT analytics TO metabase;

-- Add query privileges to the role (options 1-4):

-- Option 1: Uncomment the line below to let users with the analytics role query ALL DATA (In Postgres 14 or higher. See [Predefined Roles](https://www.postgresql.org/docs/current/predefined-roles.html#PREDEFINED-ROLES)).
-- GRANT pg_read_all_data TO analytics;

-- Option 2: Uncomment the line below to let users with the analytics role query anything in the DATABASE.
-- GRANT USAGE ON DATABASE "your_schema" TO analytics;
-- GRANT SELECT ON DATABASE "your_schema"  TO analytics;

-- Option 3: Uncomment the line below to let users with the analytics role query anything in a specific SCHEMA.
-- GRANT USAGE ON SCHEMA "your_schema" TO analytics;
-- GRANT SELECT ON ALL TABLES IN SCHEMA "your_schema" TO analytics;

-- Option 4: Uncomment the line below to let users with the analytics role query anything in a specific TABLE.
-- GRANT USAGE ON SCHEMA "your_schema" TO analytics;
-- GRANT SELECT ON "your_table" IN SCHEMA "your_schema" TO analytics;
```

Depending on how you use Metabase, you can also additionally grant:

-   `TEMPORARY` privileges to create temp tables.
-   `EXECUTE` privileges to use stored procedures or user-defined functions.

Remember that when you grant privileges to a role, all users with that role will get those privileges.

## Grant all database privileges

If you don't want to structure your database privileges yet:

-   Create a `metabase` database user.
-   Give `metabase` all privileges to the database.

``` highlight
-- Create a database user named "metabase".
CREATE USER metabase WITH PASSWORD "your_password";

-- Give the user read and write privileges to anything in the database.
GRANT ALL PRIVILEGES ON "database" TO metabase;
```

This is a good option if you're connecting to a local database for development or testing.

## Privileges to enable actions and editable table data

Both [actions](../actions/introduction) and the [editable table data](../data-modeling/editable-tables) let Metabase write back to specific tables in your database.

In addition to the [minimum database privileges](#minimum-database-privileges), you'll need to grant write access to any tables you want to be able to write to.

-   Create a new role called `metabase_writer`.
-   Give the role `INSERT`, `UPDATE`, and `DELETE` privileges to the relevant tables.
-   Give the `metabase_writer` role to the `metabase` user.

``` highlight
-- Create a role to bundle database privileges for Metabase writing to your database.
CREATE ROLE metabase_writer WITH LOGIN;

-- Grant write privileges to the TABLE
GRANT INSERT, UPDATE, DELETE ON "your_table" IN SCHEMA "your_schema" TO metabase_writer;

-- Grant role to the metabase user.
GRANT metabase_writer TO metabase;
```

## Privileges to enable model persistence

[Model persistence](../data-modeling/model-persistence) lets Metabase save query results to a specific schema in your database. Metabase's database user will need the `CREATE` privilege to set up the dedicated schema for model persistence, as well as write access (`INSERT`, `UPDATE`, `DELETE`) to that schema.

In addition to the [minimum database privileges](#minimum-database-privileges):

-   Create a new role called `metabase_model_persistence`.
-   Give the role `CREATE` access to the database.
-   Give the role `INSERT`, `UPDATE`, and `DELETE` privileges to the schema used for model persistence.
-   Give the `metabase_model_persistence` role to the `metabase` user.

``` highlight
-- Create a role to bundle database privileges for Metabase model persistence.
CREATE ROLE metabase_model_persistence WITH LOGIN;

-- If you don't want to give CREATE access to your database,
-- add the schema manually before enabling modeling persistence.
GRANT CREATE ON "database" TO metabase_model_persistence;

-- Grant write privileges to the SCHEMA used for model persistence.
GRANT USAGE ON "your_schema" TO metabase_model_persistence;
GRANT INSERT, UPDATE, DELETE ON "your_model's_table" IN SCHEMA "your_schema" TO metabase_model_persistence;

-- Grant role to the metabase user.
GRANT metabase_model_persistence TO metabase;
```

## Privileges to enable uploads

You can [upload CSVs](../databases/uploads) to supported databases. Metabase's database user should have write access (`INSERT`, `UPDATE`, `DELETE`) to the schema where you want to store the uploads.

You'll first need to create a schema to store uploads (or use an existing schema) and tell Metabase that you want to [use that schema to store uploads](./uploads#select-the-database-and-schema-that-you-want-to-store-the-data-in).

In addition to the [minimum database privileges](#minimum-database-privileges):

-   Create a new role called `metabase_uploads`.
-   Give the role `INSERT`, `UPDATE`, and `DELETE` privileges to the schema where you want to store uploads.
-   Give the `metabase_uploads` role to the `metabase` user.

``` highlight
-- Create a role to bundle database privileges for uploads.
CREATE ROLE metabase_uploads WITH LOGIN;

-- Grant write privileges to the SCHEMA used for uploads.
GRANT USAGE ON "your_schema" TO metabase_uploads;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA "your_schema" TO metabase_uploads;

-- Grant role to the metabase user.
GRANT metabase_uploads TO metabase;
```

## Multi-tenant permissions

If you're setting up multi-tenant permissions for customers who need SQL access, you can [create one database connection per customer](../permissions/embedding#granting-customers-native-sql-access-to-their-schema). That means each customer will connect to the database using their own database user.

Let's say you have customers named Tangerine and Lemon:

-   Create new database users `metabase_tangerine` and `metabase_lemon`.
-   Create a `customer_facing_analytics` role with the `CONNECT` privilege.
-   Create roles to bundle privileges specific to each customer's use case. For example:
    -   `tangerine_queries` to bundle read privileges for people to query and create stored procedures against the Tangerine schema.
    -   `lemon_queries` to bundle read privileges for people to query tables in the Lemon schema.
    -   `lemon_actions` to bundle the write privileges needed to create [actions](#privileges-to-enable-actions-and-editable-table-data) on a Lemonade table in the Lemon schema.
-   Add each user to their respective roles.

``` highlight
-- Create one database user per customer.
CREATE USER metabase_tangerine WITH PASSWORD "orange";
CREATE USER metabase_lemon WITH PASSWORD "yellow";

-- Create a role to bundle privileges for all customers.
CREATE ROLE customer_facing_analytics;
GRANT CONNECT ON DATABASE "citrus" TO customer_facing_analytics;
GRANT customer_facing_analytics TO metabase_tangerine, metabase_lemon;

-- Create a role to bundle analytics read access for customer Tangerine.
CREATE ROLE tangerine_queries;
GRANT USAGE ON SCHEMA "tangerine" TO tangerine_queries;
GRANT SELECT, EXECUTE ON ALL TABLES IN SCHEMA "tangerine" TO tangerine_queries;
GRANT tangerine_queries TO metabase_tangerine;

-- Create a role to bundle analytics read access for customer Lemon.
CREATE ROLE lemon_queries;
GRANT USAGE ON SCHEMA "lemon" TO lemon_queries;
GRANT SELECT ON ALL TABLES IN SCHEMA "lemon" TO lemon_queries;
GRANT lemon_queries TO metabase_lemon;

-- Create a role to bundle privileges to Metabase actions for customer Lemon.
CREATE ROLE lemon_actions;
GRANT INSERT, UPDATE, DELETE ON TABLE "lemonade" IN SCHEMA "lemon" TO lemon_actions;
GRANT lemon_actions TO metabase_lemon;
```

We recommend bundling privileges into roles based on use cases per customer. That way, you can reuse common privileges across customers while still being able to grant or revoke granular privileges per customer. For example:

-   If customer Tangerine needs to query the Tangerine schema from another analytics tool, you can use the `tangerine_queries` role when setting up that tool.
-   If customer Lemon decides that they don't want to use Metabase actions anymore (but they still want to ask questions), you can simply revoke or drop the `lemon_actions` role.

## Further reading

-   [Permissions strategies](/learn/metabase-basics/administration/permissions/strategy)
-   [Permissions introduction](../permissions/introduction)
-   [People overview](../people-and-groups/start)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/databases/users-roles-privileges.md) ]