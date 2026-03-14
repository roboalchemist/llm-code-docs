# Source: https://docs.snowflake.com/en/developer-guide/native-apps/event-manage-provider.md

# Set up and manage an event table in the provider account

This topic describes how providers can set up an event table and manage event sharing for an app.

## Set up an event table in the provider organization in every region

To collect the log messages and trace events that a consumer shares, a provider must set up an event
table by performing the following:

1. Set an account as the event account.
2. Create an event table in the event account.
3. Set the event table as the active event table in event account.

> **Important:**
>
> If a provider does not have an event account and active event table withing the region where the app is installed
> before the consumer installs an app, trace events and log messages are discarded.

### Set an account as the events account

To store shared logs and events, a provider must select an account to hold an event table. This can be any
account that a provider can access. However, if an organization has multiple providers publishing
application packages, consider using a Snowflake account that is dedicated to storing shared events from the
consumer.

The following restrictions apply to accounts used to store shared events:

* You must use an [organization administrator role](../../user-guide/organization-administrators.md) to set an account as the account used
  to store events.
* The account must have an active event table.
* The specified account cannot be any of the following:

  * A locked or suspended account.
  * A reader account.
  * A trial account.
  * A Snowflake managed account.

> **Note:**
>
> A provider can collect logs and shared events only in the same region where a consumer installs an app.
> Providers must set up an event account to store shared events in every region where consumers configure event
> sharing for an app.

To set an account to be the events account for a region, call the [SYSTEM$SET_EVENT_SHARING_ACCOUNT_FOR_REGION](../../sql-reference/functions/system_set_event_sharing_account_for_region.md)
system function as shown in the following example:

```sqlsyntax
SELECT SYSTEM$SET_EVENT_SHARING_ACCOUNT_FOR_REGION('<snowflake_region>', '<region_group>', '<account_name>')
```

Where:

`snowflake_region`
:   Specifies the region where the account is located, for example: `AWS_US_WEST_2, AWS_US_EAST_1`.

`region_group`
:   Specifies the region group, for example: `PUBLIC`. Refer to
    [Region groups](../../user-guide/admin-account-identifier.md) for details.

`account_name`
:   Specifies the account name. If another account is already set as the events account in the
    specified region, running this command changes the events account to be the account
    specified here.

### Create an event table in the event account

To create an event table, run the [CREATE EVENT TABLE](../../sql-reference/sql/create-event-table.md) command as shown in the
following example:

```sqlexample
CREATE EVENT TABLE event_db.event_schema.my_event_table;
```

This command specifies the database and schema that contain the event table.

## Set the event table as the active event table

An account can have multiple event tables, but only one can be set as the active event table in a
Snowflake account at a time. Without an active event table, log messages and trace events that the consumer
shares are discarded.

After creating the event table, use [ALTER ACCOUNT … SET EVENT_TABLE](../../sql-reference/sql/alter-account.md)
to specify that the event table is the active table for the account:

```sqlexample
ALTER ACCOUNT SET EVENT_TABLE=event_db.event_schema.my_event_table;
```

## Unset an account as the events account

To unset an account to be the events account for a region, call the
[SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION](../../sql-reference/functions/system_unset_event_sharing_account_for_region.md) system function:

```sqlsyntax
SELECT SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION('<snowflake_region>', '<region_group>', '<account_name>')
```

Where:

`snowflake_region`
:   Specifies the region where the account is located, for example: `AWS_US_WEST_2`.

`region_group`
:   Specifies the region group, for example: `PUBLIC`.

`account_name`
:   Specifies the account name.

## View the event accounts in an organization

To show events accounts in a provider’s organization, call the
[SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS](../../sql-reference/functions/system_show_event_sharing_accounts.md) system function:

```sqlexample
SELECT SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS()
```

> **Note:**
>
> You must use an [organization administrator role](../../user-guide/organization-administrators.md) to call this function.

This system function returns a string in JSON format containing a list of event accounts within the organization.
Because the metadata takes some time to propagate to all regions, this function might have a short delay before
showing the most current events account after the user sets or unsets the event account for the organization.

## View the logging and trace event levels defined in an application package

Use the [SHOW VERSIONS IN APPLICATION PACKAGE](../../sql-reference/sql/show-versions.md) command to view the logging level of the app versions
defined in an application package, as shown in the following example:

```sqlexample
SHOW VERSIONS
  IN APPLICATION PACKAGE HelloSnowflake;
```

## View the logs and events in the event table

To view the logs and events stored in the event table, use the [SELECT](../../sql-reference/sql/select.md) command as shown
in the following example:

```sqlexample
SELECT * FROM EVENT_DB.EVENT_SCHEMA.MY_EVENT_TABLE
```

For more information on querying the event table, see the following:

* [Viewing log messages](../logging-tracing/logging-accessing-messages.md)
* [Viewing trace data](../logging-tracing/tracing-accessing-events.md)

See [Event table columns](../logging-tracing/event-table-columns.md) for information on the columns
in the event table.

## Shared event information available to the provider

The following sections describe the information that the Native Apps Framework shares with providers.

### App event context shared with the provider

To help providers easily identify the source of the shared events, the following fields are populated into the
`RESOURCE_ATTRIBUTES` column of the event table when they are shared with the provider:

* `snow.application.package.name`
* `snow.application.consumer.organization`
* `snow.application.consumer.name`
* `snow.listing.name`
* `snow.listing.global_name`

### Fields that are not shared with the provider

To protect consumer information, the following fields from the `RESOURCE_ATTRIBUTES` column are
not shared with provider:

* `snow.database.id`
* `snow.database.name`
* `snow.schema.id`
* `snow.executable.id`
* `snow.owner.name`
* `snow.owner.id`
* `snow.warehouse.name`
* `snow.warehouse.id`
* `snow.query.id`
* `snow.session.id`
* `snow.session.role.primary.name`
* `snow.session.role.primary.id`
* `snow.user.name`
* `snow.user.id`
* `db.user`

Instead of directly sharing the `snow.database.name` and `snow.query.id` fields with the provider, Snowflake
shares the hash values (SHA-1) of these two fields as the following fields:

* `snow.database.hash`
* `snow.query.hash`

Snowflake provides the [SHA-1 function](../../sql-reference/functions/sha1.md) used to mask these attributes.
Consumers can calculate the hash values for the database name and query id, and use them as reference values when
contacting the provider.
