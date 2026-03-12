# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-failover-group.md

# ALTER FAILOVER GROUP

Modifies the properties for an existing [failover group](../../user-guide/account-replication-intro.md).

From the source account, you can perform the following actions:

* Rename the failover group.
* Reset the list of specified object types enabled for replication and failover.
* Set or update the replication schedule for automatic refresh of secondary failover groups.
* Add or remove account objects of the following types to or from a failover group:

  * Databases
  * External volumes
  * Shares
  * Security integrations
  * API integrations
  * Storage integrations
  * External access integrations
  * Certain types of notification integrations (see [Integration replication](../../user-guide/account-replication-intro.md))
* Add or remove target accounts enabled for replication and failover.
* Move shares or databases to another failover group.

From the target account, you can perform the following actions:

* Refresh objects in the target account from the source account.
* Promote a secondary failover group to primary (that is, fail over the failover group of objects).
* Suspend scheduled replication.
* Resume scheduled replication.

See also:
:   [CREATE FAILOVER GROUP](create-failover-group.md) , [DROP FAILOVER GROUP](drop-failover-group.md) , [SHOW FAILOVER GROUPS](show-failover-groups.md),
    [SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH](../functions/system_schedule_async_replication_group_refresh.md)

## Syntax

**Source Account**

```sqlsyntax
ALTER FAILOVER GROUP [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  [ OBJECT_TYPES = <object_type> [ , <object_type> , ... ] ]
  [ ALLOWED_DATABASES = <db_name> [ , <db_name> , ... ] ]
  [ ALLOWED_EXTERNAL_VOLUMES = <external_volume_name> [ , <external_volume_name> , ... ] ]
  [ ALLOWED_SHARES = <share_name> [ , <share_name> , ... ] ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  OBJECT_TYPES = INTEGRATIONS [ , <object_type> , ... ]
  ALLOWED_INTEGRATION_TYPES = <integration_type_name> [ , <integration_type_name> ... ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  COMMENT = '<string_literal>'

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  REPLICATION_SCHEDULE = '{ <num> MINUTE | USING CRON <expr> <time_zone> }'

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  ERROR_INTEGRATION = <integration_name>

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SET
  TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name> UNSET
  { COMMENT | REPLICATION_SCHEDULE | ERROR_INTEGRATION } [ , ... ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name> UNSET
  TAG <tag_name> [ , <tag_name> ... ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  ADD <db_name> [ , <db_name> ,  ... ] TO ALLOWED_DATABASES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  MOVE DATABASES <db_name> [ , <db_name> ,  ... ] TO FAILOVER GROUP <move_to_fg_name>

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  REMOVE <db_name> [ , <db_name> ,  ... ] FROM ALLOWED_DATABASES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  ADD <external_volume_name> [ , <external_volume_name> ,  ... ] TO ALLOWED_EXTERNAL_VOLUMES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  MOVE EXTERNAL VOLUMES <external_volume_name> [ , <external_volume_name> ,  ... ] TO FAILOVER GROUP <move_to_fg_name>

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  REMOVE <external_volume_name> [ , <external_volume_name> ,  ... ] FROM ALLOWED_EXTERNAL_VOLUMES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  ADD <share_name> [ , <share_name> ,  ... ] TO ALLOWED_SHARES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  MOVE SHARES <share_name> [ , <share_name> ,  ... ] TO FAILOVER GROUP <move_to_fg_name>

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  REMOVE <share_name> [ , <share_name> ,  ... ] FROM ALLOWED_SHARES

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  ADD <org_name>.<target_account_name> [ , <org_name>.<target_account_name> ,  ... ] TO ALLOWED_ACCOUNTS
  [ IGNORE EDITION CHECK ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name>
  REMOVE <org_name>.<target_account_name> [ , <org_name>.<target_account_name> ,  ... ] FROM ALLOWED_ACCOUNTS
```

**Target Account**

```sqlsyntax
ALTER FAILOVER GROUP [ IF EXISTS ] <name> REFRESH

ALTER FAILOVER GROUP [ IF EXISTS ] <name> PRIMARY

ALTER FAILOVER GROUP [ IF EXISTS ] <name> SUSPEND [ IMMEDIATE ]

ALTER FAILOVER GROUP [ IF EXISTS ] <name> RESUME
```

## Parameters

**Source Account**

`name`
:   Specifies the identifier for the failover group.

`RENAME TO new_name`
:   `new_name`
    :   Specifies the new identifier for the failover group. The new identifier cannot be used if the identifier is already in place for a
        different replication or failover group.

        For more details, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Specifies properties to set for the failover group (separated by blank spaces, commas, or new lines).

    `OBJECT_TYPES = object_type [ , object_type , ... ]`
    :   Reset the list of object types for which you are enabling replication and failover from the source account to target
        account(s).

        > **Note:**
        >
        > For database, external volume, and share objects:
        >
        > * If DATABASES, EXTERNAL VOLUMES, or SHARES are included in the OBJECT_TYPES list, and remain in the OBJECT_TYPES list after
        >   the list is reset, the respective allowed objects list (ALLOWED_DATABASES, ALLOWED_EXTERNAL_VOLUMES, or ALLOWED_SHARES) remains
        >   unchanged.
        > * If the OBJECT_TYPES list is reset to add or remove DATABASES, the ALLOWED_DATABASES list is set to NULL.
        > * If the OBJECT_TYPES list is reset to add or remove EXTERNAL VOLUMES, the ALLOWED_EXTERNAL_VOLUMES list is set to NULL.
        > * If the OBJECT_TYPES list is reset to add or remove SHARES, the ALLOWED_SHARES list is set to NULL.
        > * Use the ADD, MOVE, and REMOVE clauses to modify the list of allowed database, external volume, or share objects.

        The following object types are supported:

        > ACCOUNT PARAMETERS:
        > :   All account-level parameters. This includes [account parameters](../parameters.md) and parameters that can be
        >     [set for your account](../../user-guide/admin-account-management.md).
        >
        > DATABASES:
        > :   Add database objects to the list of object types. If database objects were already included in the list of specified object
        >     types, the `ALLOWED_DATABASES` list remains unchanged. To modify the list of databases, use the
        >     ADD, MOVE, or REMOVE clauses.
        >
        > EXTERNAL VOLUMES:
        > :   Add external volume objects to the list of object types. If external volume objects are included in the list of specified object types,
        >     the `ALLOWED_EXTERNAL_VOLUMES` parameter must be set. To modify the list of external volumes, use the ADD, MOVE, or REMOVE clauses.
        >
        > INTEGRATIONS:
        > :   Currently, only security, API, storage, external access, and certain types of notification integrations are supported.
        >     For details, see [Integration replication](../../user-guide/account-replication-intro.md).
        >
        >     If integration objects are included in the list of specified object types, the
        >     `ALLOWED_INTEGRATION_TYPES` parameter must be set.
        >
        > NETWORK POLICIES:
        > :   All network policies in the source account.
        >
        > RESOURCE MONITORS:
        > :   All resource monitors in the source account.
        >
        > ROLES:
        > :   All roles in the source account. Replicating roles implicitly includes all grants for object types included in the failover group.
        >     For example, if `ROLES` is the only object type that is replicated, then only hierarchies of roles (that is, roles granted to
        >     other roles) are replicated to target accounts. If the `USERS` object type is also included, then role grants to users are
        >     also replicated.
        >
        > SHARES:
        > :   Add share objects to the list of object types. If share objects were already included in the list of specified object types, the
        >     `ALLOWED_SHARES` list remains unchanged. To modify the list of shares, use the ADD, MOVE, or REMOVE clauses.
        >
        > USERS:
        > :   All users in the source account.
        >
        > WAREHOUSES:
        > :   All warehouses in the source account.

        > **Note:**
        >
        > If you replicate users and roles, programmatic access tokens for users are replicated automatically.

    `ALLOWED_DATABASES = db_name [ , db_name , ... ]`
    :   Specifies the database or list of databases for which you are enabling replication and failover from the source account to the target
        account. In order for you to set this parameter, the `OBJECT_TYPES` list must include `DATABASES`.

        `db_name`
        :   Specifies the identifier for the database.

    `ALLOWED_EXTERNAL_VOLUMES = external_volume_name [ , external_volume_name , ... ]`
    :   [Preview Feature](../../release-notes/preview-features.md) — Open

        Available to all accounts.

        Specifies the external volume or list of external volumes for which you are enabling replication and failover from the source account
        to the target account. For you to set this parameter, the `OBJECT_TYPES` list must include `EXTERNAL VOLUMES`.

        `external_volume_name`
        :   Specifies the identifier for the external volume.

    `ALLOWED_SHARES = share_name [ , share_name , ... ]`
    :   Specifies the share or list of shares for which you are enabling replication and failover from the source account to the target account.
        For you to set this parameter, the `OBJECT_TYPES` list must include `SHARES`.

        `share_name`
        :   Specifies the identifier for the share.

    > **Note:**
    >
    > If the ALLOWED_DATABASES, ALLOWED_EXTERNAL_VOLUMES, or ALLOWED_SHARES lists are modified, any objects that were previously in the list and removed
    > will be dropped in any target account with a linked secondary failover group when the next refresh operation occurs.

    `ALLOWED_INTEGRATION_TYPES = integration_type_name [ , integration_type_name , ... ]`
    :   Type(s) of integrations for which you are enabling replication and failover from the source account to the target account.

        > This property requires that the `OBJECT_TYPES` list include `INTEGRATIONS` to set this parameter.
        >
        > The following integration types are supported:
        >
        > > SECURITY INTEGRATIONS:
        > > :   Specifies security integrations.
        > >
        > >     This property requires that the `OBJECT_TYPES` list include `ROLES`.
        > >
        > > API INTEGRATIONS:
        > > :   Specifies API integrations.
        > >
        > >     API integration replication requires additional set up after the API integration is replicated to the target account.
        > >     For more information, see [Updating the remote service for API integrations](../../user-guide/account-replication-config.md).
        > >
        > > STORAGE INTEGRATIONS:
        > > :   Specifies storage integrations.
        > >
        > > EXTERNAL ACCESS INTEGRATIONS:
        > > :   Specifies [external access integrations](../../developer-guide/external-network-access/creating-using-external-network-access.md).
        > >
        > >     For more information, see [Replication of stored procedures and user-defined functions (UDFs)](../../user-guide/account-replication-considerations.md).
        > >
        > > NOTIFICATION INTEGRATIONS:
        > > :   Specifies notification integrations.
        > >
        > >     Only some types of notification integrations are replicated. For details, see
        > >     [Integration replication](../../user-guide/account-replication-intro.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the failover group.

        Default:
        :   `NULL`

    `REPLICATION_SCHEDULE ...`
    :   Specifies the schedule for refreshing secondary failover groups.

        * `USING CRON expr time_zone`
          :   Specifies a cron expression and time zone for the secondary group refresh. Supports a subset of standard cron utility syntax.

              For a list of time zones, see the [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
              (in Wikipedia).

              The cron expression consists of the following fields:

              ```output
              # __________ minute (0-59)
              # | ________ hour (0-23)
              # | | ______ day of month (1-31, or L)
              # | | | ____ month (1-12, JAN-DEC)
              # | | | | __ day of week (0-6, SUN-SAT, or L)
              # | | | | |
              # | | | | |
                * * * * *
              ```

              The following special characters are supported:

              `*`
              :   Wildcard. Specifies any occurrence of the field.

              `L`
              :   Stands for “last”. When used in the day-of-week field, it allows you to specify constructs such as “the last Friday” (“5L”) of a
                  given month. In the day-of-month field, it specifies the last day of the month.

              `/n`
              :   Indicates the *nth* instance of a given unit of time. Each quanta of time is computed independently. For example, if `4/3` is
                  specified in the month field, then the refresh is scheduled for April, July and October (i.e. every 3 months, starting with the 4th
                  month of the year). The same schedule is maintained in subsequent years. That is, the refresh is not scheduled to run in
                  January (3 months after the October run).

              > **Note:**
              > + The cron expression currently evaluates against the specified time zone only. Altering the [TIMEZONE](../parameters.md) parameter value
              >   for the account (or setting the value at the user or session level) does not change the time zone for the refresh.
              > + The cron expression defines all valid run times for the refresh. Snowflake attempts to refresh secondary groups based on
              >   this schedule; however, any valid run time is skipped if a previous run has not completed before the next valid run time starts.
              > + When both a specific day of month and day of week are included in the cron expression, then the refresh is scheduled on days
              >   satisfying either the day of month or day of week. For example, `SCHEDULE = 'USING CRON 0 0 10-20 * TUE,THU UTC'`
              >   schedules a refresh at 0AM on any 10th to 20th day of the month and also on any Tuesday or Thursday outside of those dates.
        * `num MINUTE`
          :   Specifies an interval (in minutes) of wait time between refreshes. Accepts positive integers only.

              Also supports `num M` syntax.

              To avoid ambiguity, a *base interval time* is set:

              + When the object is created (using CREATE <object>) or
              + When a different interval is set (using ALTER <object> … SET REPLICATION_SCHEDULE)

              The base interval time starts the interval counter from the current clock time. For example, if an INTERVAL value of `10` is set and
              the scheduled refresh is enabled at 9:03 AM, then the refresh runs at 9:13 AM, 9:23 AM, and so on. Note that we make a best effort to
              ensure absolute precision, but only guarantee that refreshes do not execute before their set interval occurs (e.g. in the
              current example, the refresh could first run at 9:14 AM, but will definitely not run at 9:12 AM).

              > **Note:**
              >
              > The maximum supported value is `11520` (8 days). If the replication schedule has a greater `num MINUTE` value, the
              > refresh operation never runs.

        Default:
        :   `NULL`

    `ERROR_INTEGRATION = integration_name`
    :   Specifies the name of the notification integration to use to email/push notifications when refresh errors occur for the failover
        group. For more details, see [Error notifications for replication and failover groups](../../user-guide/account-replication-error-notifications.md).

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`ADD db_name [ , db_name ,  ... ] TO ALLOWED_DATABASES`
:   Specifies a comma-separated list of additional databases to enable for replication and failover. To add databases,
    DATABASES must be included in the list of specified object types. If the list of object types does not already include DATABASES, you must
    add it.

    > `db_name`
    > :   Specifies the identifier for the database.

`MOVE DATABASES db_name [ , db_name ,  ... ] TO FAILOVER GROUP move_to_fg_name`
:   Specifies a comma-separated list of databases to move from one failover group to another failover group. The failover group the databases
    are being moved to must include DATABASES in the list of specified object types.

    > `db_name`
    > :   Specifies the identifier for the database.
    >
    > `move_to_fg_name`
    > :   Specifies the identifier for the failover group the databases are being moved to.

`REMOVE db_name [ , db_name ,  ... ] FROM ALLOWED_DATABASES`
:   Specifies a comma-separated list of databases to remove from the list of databases enabled for replication and failover.

    > **Note:**
    >
    > When you remove a database from a primary failover group, the database is dropped in any target account with a linked secondary
    > failover group when the next refresh operation occurs.
    >
    > To avoid dropping databases in the target account, you can drop the secondary failover group *before* the next time the modified
    > primary failover group is replicated to the target account. When you drop the secondary failover group, read-only secondary
    > databases that were included in the group become standalone read-write databases in the target account.

`ADD external_volume_name [ , external_volume_name ,  ... ] TO ALLOWED_EXTERNAL_VOLUMES`
:   Specifies a comma-separated list of additional external volumes to enable for replication and failover. To add external volumes,
    EXTERNAL VOLUMES must be included in the list of specified object types. If the list of object types does not already include
    EXTERNAL VOLUMES, you must add it.

    > `external_volume_name`
    > :   Specifies the identifier for the external volume.

`MOVE EXTERNAL VOLUMES external_volume_name [ , external_volume_name ,  ... ] TO FAILOVER GROUP move_to_fg_name`
:   Specifies a comma-separated list of external volumes to move from one failover group to another failover group. The failover group the external volumes
    are being moved to must include EXTERNAL VOLUMES in the list of specified object types.

    > `db_name`
    > :   Specifies the identifier for the external volume.
    >
    > `move_to_fg_name`
    > :   Specifies the identifier for the failover group the external volumes are being moved to.

`REMOVE external_volume_name [ , external_volume_name ,  ... ] FROM ALLOWED_EXTERNAL_VOLUMES`
:   Specifies a comma-separated list of external volumes to remove from the list of external volumes enabled for replication and failover.

    > **Note:**
    >
    > When you remove an external volume from a primary failover group, the external volume is dropped in any target account with a
    > linked secondary failover group when the next refresh operation occurs.
    >
    > To avoid dropping external volumes in the target account, you can drop the secondary failover group *before* the next time the modified
    > primary failover group is replicated to the target account. When you drop the secondary failover group, read-only secondary
    > external volumes that were included in the group become standalone read-write external volumes in the target account.

`ADD share_name [ , share_name ,  ... ] TO ALLOWED_SHARES`
:   Specifies a comma-separated list of additional shares to enable for replication and failover. To add shares, SHARES must be included in
    the list of specified object types. If the list of object types doesn’t already include SHARES, you must add it.

    > `share_name`
    > :   Specifies the identifier for the share.

`MOVE SHARES share_name [ , share_name ,  ... ] TO FAILOVER GROUP move_to_fg_name`
:   Specifies a comma-separated list of shares to move from one failover group to another failover group. The failover group the shares
    are being moved to must include SHARES in the list of specified object types.

    > `share_name`
    > :   Specifies the identifier for the share.
    >
    > `move_to_fg_name`
    > :   Specifies the identifier for the failover group the shares are being moved to.

`REMOVE share_name [ , share_name ,  ... ] FROM ALLOWED_SHARES`
:   Specifies a comma-separated list of shares to remove from the list of shares enabled for replication and failover.

    > **Note:**
    >
    > When you remove a share from a primary failover group, the share is dropped in any target account with a secondary
    > failover group when the next refresh operation occurs.

`ADD org_name.target_account_name [ , org_name.target_account_name ,  ... ] TO ALLOWED_ACCOUNTS`
:   Specifies a comma-separated list of target accounts to add to the primary failover group to enable replication and failover of
    specified objects in the source account to the target account. Secondary failover groups in the target accounts in this list
    can be promoted to serve as the primary failover group in case of failover.

    > `org_name`
    > :   Name of your Snowflake organization.
    >
    > `target_account_name`
    > :   Target account to which you are enabling replication of the specified objects.

`REMOVE org_name.target_account_name [ , org_name.target_account_name ,  ... ] FROM ALLOWED_ACCOUNTS`
:   Specifies a comma-separated list of target accounts to remove from the primary failover group to disable replication
    of specified objects in the source account to the target account.
    Removing a target account disables failover from the current account to this target account.

    > `org_name`
    > :   Name of your Snowflake organization.
    >
    > `target_account_name`
    > :   Target account to which you are disabling replication of the specified objects.

`IGNORE EDITION CHECK`
:   Allows replicating objects to accounts in the following scenario:

    > The primary failover group is in a Business Critical (or higher) account and a signed business associate agreement is in place to
    > store PHI data in the account per HIPAA and [HITRUST](../../user-guide/intro-cloud-platforms.md) regulations. However, no such agreement is in place
    > for one or more of the accounts approved for replication, regardless if they are Business Critical (or higher) accounts.

    This scenario is prohibited by default.

**Target Account**

`name`
:   Specifies the identifier for the failover group.

`REFRESH`
:   Refreshes the objects in the target (current) account from the source account.

`PRIMARY`
:   Promote a secondary failover group and its specified objects in the target (current) account to primary (in case of
    failover).

`SUSPEND [ IMMEDIATE ]`
:   Suspend the scheduled refresh of the secondary failover group (if the primary failover group has scheduled refreshes using the
    `REPLICATION_SCHEDULE` property).

    The optional `IMMEDIATE` keyword cancels a scheduled refresh operation that is currently in progress for the secondary failover group
    (if there is one). Note that there might be a slight delay between the time that the statement returns and the time that the cancellation
    of the refresh operation is finished.

`RESUME`
:   Resume scheduled refresh of the secondary failover group (if the primary failover group has scheduled refreshes using the
    `REPLICATION_SCHEDULE` property).

`UNSET ...`
:   Specifies one (or more) properties to unset for the failover group, which resets them to the defaults:

    * `COMMENT`
    * `REPLICATION_SCHEDULE`
    * `ERROR_INTEGRATION`
    * `TAG tag_name [ , tag_name ... ]`

    You can reset multiple properties with a single ALTER statement; however, each property must be separated by
    a comma. Also, when resetting a property, you only specify the name; no value is required.

## Usage notes

* The following minimal privileges are required:

  * To refresh a secondary failover group using ALTER FAILOVER GROUP … REFRESH, the active, primary role must have either the OWNERSHIP or
    REPLICATE privilege on the failover group.
  * To fail over a secondary failover group using ALTER FAILOVER GROUP … PRIMARY, a role must have either the OWNERSHIP or FAILOVER
    privilege on the failover group.
  * To make any other changes to the failover group, only a role with the OWNERSHIP privilege on the group can execute this SQL command.
  * To add a database to a failover group, the active role must have the MONITOR privilege on the database.
  * To add an external volume to a replication group, the active role must have the USAGE privilege on the external volume.
  * To add a share to a failover group, the active role must have the OWNERSHIP privilege on the share.
* Identifiers for failover groups and replication groups in an account must be unique.
* Objects other than databases, external volumes, and shares must be in the same failover group.
* A database can only be added to one failover group.
* An external volume can only be added to one failover group.
* [Inbound shares](../../user-guide/data-share-consumers.md) (shares from providers) *cannot* be added to a replication or failover group.
* Promoting a secondary failover group to primary (in case of failover) fails if a refresh is in progress.
* If a refresh is in progress when the replication schedule is updated, the refresh continues until completion and the next refresh will
  use the new schedule.
* On failover, scheduled refreshes on all secondary failover groups are suspended. `ALTER FAILOVER GROUP ... RESUME` must be executed
  on each secondary to resume automatic refreshes.
* To move databases, external volumes, or shares from one failover group (the move-from group) to another failover group (the move-to group):

  * Both groups must be of the same type: FAILOVER GROUP.
  * If the last database in the move-from group is moved to another group, the `allowed_databases` property for the move-from group
    is set to NULL. The same behavior applies to shares and external volumes.
  * If the move-to group doesn’t have the object type that is being moved (`databases`, `external volumes`, or `shares`) in the `object_types`
    list, it must be explicitly added to the move-to group before you move the objects.
* If database, external volume, or share objects are removed from a primary failover group (by using the REMOVE parameter or SET parameter to
  modify the ALLOWED_DATABASES, ALLOWED_EXTERNAL_VOLUMES, or ALLOWED_SHARES lists), those objects are dropped in any target account when the next
  refresh operation occurs.

  To avoid dropping these objects in the target account, you can drop the secondary failover group *before* the next time the modified
  primary failover group is replicated to the target account.
* To retrieve the list of accounts in your organization that are enabled for replication, use the
  [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md) command.
* To retrieve the list of failover groups in your organization, use [SHOW FAILOVER GROUPS](show-failover-groups.md).
* Automatically [scheduled refresh operations](../../user-guide/account-replication-intro.md) are executed using the role with the OWNERSHIP
  privilege on the group. If a scheduled refresh operation fails due to insufficient privileges, grant the required privileges
  to the role with the OWNERSHIP privilege on the group.
* The ALTER FAILOVER GROUP … SUSPEND IMMEDIATE command doesn’t cancel an in-progress refresh operation if it was manually triggered.
  For information, see [Cancel an in-progress refresh operation that wasn’t automatically scheduled](../../user-guide/account-replication-failover-failback.md).
* Canceling an in-progress refresh operation that is in the SECONDARY_DOWNLOADING_METADATA or SECONDARY_DOWNLOADING_DATA phase might
  result in an inconsistent state on the target account. For more information see [View the current phase of an in-progress refresh operation](../../user-guide/account-replication-failover-failback.md).

* If you create a replication or failover group with a tag or modify a replication or failover group by setting a tag on it,
  [tag inheritance](../../user-guide/object-tagging/inheritance.md) does not apply to any objects that you specify in the replication or failover group.

  Tag inheritance is only applicable to objects with a [parent-child relationship](../../user-guide/security-access-control-overview.md), such
  database, schema, and table. There are no child objects of replication or failover groups.
* You cannot set a tag or modify a tag on a secondary replication or failover group because these objects are read
  only.
* When you refresh a secondary replication or failover group, any tags that are set on the primary group are then set on
  the secondary group.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

### Executed from the source account

Add `myorg.myaccount3` to the list of target accounts to which replication of specified objects and failover from the source
account is enabled.

```sqlexample
ALTER FAILOVER GROUP myfg ADD myorg.myaccount3 TO ALLOWED_ACCOUNTS;
```

Reset the object types list for replication in the source account and add database `db1`:

```sqlexample
ALTER FAILOVER GROUP myfg SET
  OBJECT_TYPES = USERS, ROLES, WAREHOUSES, RESOURCE MONITORS, DATABASES
  ALLOWED_DATABASES = db1;
```

Add databases `db2` and `db3` to the list of databases:

```sqlexample
ALTER FAILOVER GROUP myfg
  ADD db2, db3 TO ALLOWED_DATABASES;
```

Move database `db3` to another failover group, `myfg2`:

```sqlexample
ALTER FAILOVER GROUP myfg
  MOVE DATABASES db3 TO FAILOVER GROUP myfg2;
```

Move database `db2` in `myfg` to another failover group, `myfg3`, that currently has no databases:

> 1. First add `databases` to `object_types`:
>
>    ```sqlexample
>    ALTER FAILOVER GROUP myfg3 SET
>      OBJECT_TYPES = DATABASES, SHARES;
>    ```
>
> 2. Move `db2` to `myfg3`:
>
>    ```sqlexample
>    ALTER FAILOVER GROUP myfg
>      MOVE DATABASES db2 TO FAILOVER GROUP myfg3;
>    ```

Remove all databases from the list of databases in the source account for replication and failover:

```sqlexample
ALTER FAILOVER GROUP myfg
  SET ALLOWED_DATABASES = NULL;
```

> **Note:**
>
> Executing the statement above removes all databases from the list of databases to be replicated, but does not remove
> database objects from the list of specified object types for replication and failover.
>
> To disable replication and failover of all databases and remove databases from the list of specified object types:
>
> ```sqlexample
> ALTER FAILOVER GROUP myfg
>   REMOVE databases FROM OBJECT_TYPES;
> ```

Add (or modify) the interval for automatically scheduled refreshes:

```sqlexample
ALTER FAILOVER GROUP myfg
  SET REPLICATION_SCHEDULE = '15 MINUTE';
```

### Executed from the target account

Refresh objects in the failover group `myfg` in the target account:

```sqlexample
ALTER FAILOVER GROUP myfg REFRESH;
```

Promote the secondary failover group in the current target account to primary:

```sqlexample
ALTER FAILOVER GROUP myfg PRIMARY;
```

Suspend automatic refreshes:

```sqlexample
ALTER FAILOVER GROUP myfg SUSPEND;
```
