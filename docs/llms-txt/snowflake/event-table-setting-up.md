# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up.md

# Event table overview

As your Snowflake objects—including procedures and UDFs—emit telemetry data, Snowflake collects the data in an event table whose
data is available for queries. Snowflake includes an event table by default, but you can also create a new one.

To collect telemetry data, you must have an active event table and have
[set telemetry levels](logging-tracing-overview.md) to allow data collection. If you don’t already have an active event table,
Snowflake makes the default event table the active event table.

When collecting telemetry data, you incur costs. To understand these costs—or to reduce or avoid these costs—see
[Costs of telemetry data collection](logging-tracing-billing.md).

## What is an event table?

An event table is a special kind of database table with a predefined set of columns. The table’s [structure](event-table-columns.md)
supports the data model for [OpenTelemetry](https://opentelemetry.io/), a framework for handling telemetry data. When an
event table is active, Snowflake collects telemetry data in the table—including data that
Snowflake itself generates and data that you emit by instrumenting your handler code using certain APIs. You can view the collected data
by executing SQL queries.

After installation, Snowflake includes a default event table called
SNOWFLAKE.TELEMETRY.EVENTS. This event table is active and collects data until you deactivate it. You can also
create your own.

## Use the default event table

If you do not set an active event table, Snowflake uses as the active event table a default event table named SNOWFLAKE.TELEMETRY.EVENTS.
You can also create your own event tables for specific uses.

By default, Snowflake also includes a predefined view called [SNOWFLAKE.TELEMETRY.EVENTS_VIEW view](../../sql-reference/telemetry/events_view.md),
with which you more securely make event table data available to a range of users. You can manage access to the view with
a row access policy.

> **Note:**
>
> The default event table supports only a subset of DDL commands supported for event tables you create or for regular tables. For more
> information, see [Working with event tables](event-table-operations.md).

### Roles for access to the default event table and EVENTS_VIEW

Snowflake includes the following predefined application roles you can use to manage access to the default event table and EVENTS_VIEW view:
A person with the ACCOUNTADMIN role can access the default event table and EVENTS_VIEW view and can grant the roles described here
to other roles for access to them.

You must grant these roles to other roles, rather than to a user. For example, you might grant the EVENTS_ADMIN role to another admin
role you’ve created for broader administrative use.

```sqlexample
GRANT APPLICATION ROLE SNOWFLAKE.EVENTS_ADMIN TO ROLE my_admin_role;

GRANT APPLICATION ROLE SNOWFLAKE.EVENTS_VIEWER TO ROLE my_analysis_role;
```

EVENTS_VIEWER:
:   Role with privileges to execute a SELECT statement on the [EVENTS_VIEW view](../../sql-reference/telemetry/events_view.md).

EVENTS_ADMIN:
:   Role with the following privileges:

    * SELECT, TRUNCATE, DELETE on the default event table.
    * SELECT on the [EVENTS_VIEW view](../../sql-reference/telemetry/events_view.md) of the default event table.
    * USAGE on the following stored procedures:

      + [ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](../../sql-reference/stored-procedures/snowflake_telemetry_add_row_access_policy_on_events_view.md)
      + [DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](../../sql-reference/stored-procedures/snowflake_telemetry_drop_row_access_policy_on_events_view.md)
    * This role also has privileges to execute a stored procedure to apply a row access policy (RAP) on the EVENTS_VIEW view
      whose data is based on the default event table.

### Manage access to the EVENTS_VIEW view

You can manage access to data in the [EVENTS_VIEW](../../sql-reference/telemetry/events_view.md) view with
[row access policies](../../user-guide/security-row-intro.md). Snowflake provides stored procedures you can use to add and remove a row
access policy to the EVENT_VIEW view.

* [ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(VARCHAR, ARRAY)](../../sql-reference/stored-procedures/snowflake_telemetry_add_row_access_policy_on_events_view.md)—Binds
  a row access policy to the specified columns in the EVENTS_VIEW.
* [DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(VARCHAR)](../../sql-reference/stored-procedures/snowflake_telemetry_drop_row_access_policy_on_events_view.md)—Deletes
  the specified row access policy bound to the EVENTS_VIEW.

> **Note:**
>
> You must have the [EVENTS_ADMIN role](../../user-guide/security-access-control-overview.md) to execute these procedures.
>
> Using row access policies on the EVENT_VIEW view is an [Enterprise Edition](../../user-guide/intro-editions.md) feature.

## Use a custom event table

To create a new event table, execute the [CREATE EVENT TABLE](../../sql-reference/sql/create-event-table.md) command and specify a name for the event table.

> **Note:**
>
> If you don’t create an event table, Snowflake uses the default event table to collect telemetry data.

1. Create an event table by executing the [CREATE EVENT TABLE](../../sql-reference/sql/create-event-table.md) command,
   specifying a name for the event table.
2. Associate the event table with an object by executing the
   [ALTER <object>](../../sql-reference/sql/alter.md) command on the object, setting the [EVENT_TABLE](../../sql-reference/parameters.md) parameter to the name of your event table.

   This sets the scope of data captured by the event table to the object with which you’re associating the table.

### Create an event table

To create an event table, execute the [CREATE EVENT TABLE](../../sql-reference/sql/create-event-table.md) command.

When you create an event table, you do not specify the columns in the table. An event table already has a set of predefined
columns, as described in [Event table columns](event-table-columns.md).

1. Ensure that you’re using a role that has the CREATE EVENT TABLE [privilege](../../user-guide/security-access-control-privileges.md).
2. Execute the [CREATE EVENT TABLE](../../sql-reference/sql/create-event-table.md) command to create the event table, specifying a name for the event table.

   You use the event table name to associate the table with an object, such as a database.

   For example, to create an event table with the name `my_events`, execute the following statement:

   ```sqlexample
   CREATE EVENT TABLE my_database.my_schema.my_events;
   ```

> **Note:**
>
> Replication of event tables is not currently supported. Any event tables that are contained in primary databases
> are skipped during replication.

### Associate an event table with an object

To specify the object for which an event table is active, execute the [ALTER <object>](../../sql-reference/sql/alter.md) command on the object.

Associating an event table with a database is an [Enterprise Edition](../../user-guide/intro-editions.md) feature.

1. Ensure that you’re using a role that has the required privileges.
2. Execute the [ALTER <object>](../../sql-reference/sql/alter.md) command on the object, setting the [EVENT_TABLE](../../sql-reference/parameters.md) parameter to the name of
   your event table.

   Setting this parameter sets the object as the scope within which events will be collected in the specified event table.

   For example, to associate the event table with a database, use ALTER DATABASE, as in the following example:

   ```sqlexample
   ALTER DATABASE my_database SET EVENT_TABLE = my_database.my_schema.my_events;
   ```

   In this example, Snowflake—depending on how you’ve [specified telemetry levels](telemetry-levels.md)—captures
   telemetry data for procedures and UDFs in `my_database` in the `telemetry_database.telemetry_schema.my_events` event table.

#### Supported objects

The following table lists the objects with which you can associate an event, along with the privileges required to make the association.

| Object | Privileges required | Scope of objects whose data is collected |
| --- | --- | --- |
| Account | *ACCOUNTADMIN role.* OWNERSHIP privilege for the account. * [OWNERSHIP or INSERT privileges for the event table](../../user-guide/security-access-control-privileges.md). | Procedures and UDFs in the account. Use this for the broadest scope. |
| Database | *ACCOUNTADMIN role.* [OWNERSHIP or INSERT privileges for the event table](../../user-guide/security-access-control-privileges.md). | Procedures and UDFs in the specified database. |

An order of precedence determines which event table is used to collect telemetry data for an object. In that precedence order, an event
table associated with a database takes precedence over an event table associated with an account.

* Account » Database

In other words, if you have event tables associated with both your account and a database `my_database`, telemetry data generated by
objects in `my_database` will be collected in the database’s event table. For other databases in the account that don’t have an
associated event table, telemetry data will be collected in the event table associated with the account.

### Set the event table for the account

> **Note:**
>
> To execute this command, you must use the ACCOUNTADMIN role.
>
> In addition, you must have both of the following privileges:
>
> * OWNERSHIP privilege for the account.
> * [OWNERSHIP or INSERT privileges for the event table](../../user-guide/security-access-control-privileges.md).
>
> See the [documentation on the ALTER ACCOUNT command](../../sql-reference/sql/alter-account.md) for more information on the
> privileges needed to execute ALTER ACCOUNT.

For example, to set up the event table named `my_events` in the schema `my_schema` in the database `my_database` as
the active event table for your account, execute the following statement:

```sqlexample
ALTER ACCOUNT SET EVENT_TABLE = my_database.my_schema.my_events;
```

As shown above, you must specify the [fully-qualified name](../../sql-reference/name-resolution.md) of the event table.

To disassociate an event table from an account, execute the ALTER ACCOUNT command and unset the EVENT_TABLE parameter. For example:

```sqlexample
ALTER ACCOUNT UNSET EVENT_TABLE;
```

You can confirm the EVENT_TABLE value with the [SHOW PARAMETERS](../../sql-reference/sql/show-parameters.md) command:

```sqlexample
SHOW PARAMETERS LIKE 'event_table' IN ACCOUNT;
```

### Set the event table for a database

To set up the event table named `my_events` in the schema `my_schema` in the database `my_database` as
the active event table for the database `my_database`, execute the following statement:

```sqlexample
ALTER DATABASE my_database SET EVENT_TABLE = my_database.my_schema.my_events;
```

To disassociate an event table from a database, execute the ALTER DATABASE command and unset the EVENT_TABLE parameter. For example:

```sqlexample
ALTER DATABASE my_database UNSET EVENT_TABLE;
```

You can confirm the EVENT_TABLE value with the [SHOW PARAMETERS](../../sql-reference/sql/show-parameters.md) command:

```sqlexample
SHOW PARAMETERS LIKE 'event_table' IN DATABASE my_database;
```
