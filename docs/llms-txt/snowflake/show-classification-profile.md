# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/commands/show-classification-profile.md

# SHOW CLASSIFICATION_PROFILE

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE

Lists all classification profile instances.

## Syntax

```sqlsyntax
SHOW SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  [ LIKE <pattern> ]
  [ IN
    {
      ACCOUNT                  |

      DATABASE                 |
      DATABASE <database_name> |

      SCHEMA                   |
      SCHEMA <schema_name>     |
      <schema_name>
    }
  ]
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

`[ IN ... ]`
:   Optionally specifies the scope of the command. Specify one of the following:

    `ACCOUNT`
    :   Returns records for the entire account.

    `DATABASE`, . `DATABASE db_name`
    :   Returns records for the current database in use or for a specified database (`db_name`).

        If you specify `DATABASE` without `db_name` and no database is in use, the keyword has no effect on the output.

        > **Note:**
        >
        > Using SHOW commands without an `IN` clause in a database context can result in fewer than expected results.
        >
        > Objects with the same name are only displayed once if no `IN` clause is used. For example, if you have table `t1` in
        > `schema1` and table `t1` in `schema2`, and they are both in scope of the database context you’ve specified (that is, the database
        > you’ve selected is the parent of `schema1` and `schema2`), then SHOW TABLES only displays one of the `t1` tables.

    `SCHEMA`, . `SCHEMA schema_name`
    :   Returns records for the current schema in use or a specified schema (`schema_name`).

        `SCHEMA` is optional if a database is in use or if you specify the fully qualified `schema_name` (for example, `db.schema`).

        If no database is in use, specifying `SCHEMA` has no effect on the output.

    If you omit `IN ...`, the scope of the command depends on whether the session currently has a database in use:

    * If a database is currently in use, the command returns the objects you have privileges to view in the database. This has the
      same effect as specifying `IN DATABASE`.
    * If no database is currently in use, the command returns the objects you have privileges to view in your account. This has the
      same effect as specifying `IN ACCOUNT`.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege/role | Object | Notes |
| --- | --- | --- |
| <classification_profile>!PRIVACY_USER [instance role](../../../snowflake-db-classes.md) | n/a |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Output

Provides custom classifier instance properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| created_on | Date and time when the classification profile instance was created. |
| name | Name of the classification profile instance. |
| database_name | Database that stores the classification profile instance. |
| schema_name | Schema that stores the classification profile instance. |
| current_version | The version of the classification profile instance. Snowflake automatically updates the version number. |
| comment | Comment for the classification profile instance. |
| owner | The role that owns the classification profile instance. |

## Examples

List the classification profiles that you can access:

```sqlexample
SHOW SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE;
```
