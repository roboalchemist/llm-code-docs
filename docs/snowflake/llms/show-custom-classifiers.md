# Source: https://docs.snowflake.com/en/sql-reference/classes/custom_classifier/commands/show-custom-classifiers.md

# SHOW CUSTOM_CLASSIFIER

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER

See also:
:   [Using custom classifiers to implement custom semantic categories](../../../../user-guide/classify-custom-using.md)

Lists all custom classification instances that you can access.

SHOW SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER INSTANCES is an alias for SHOW SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER.

## Syntax

```sqlsyntax
{
  SHOW SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER           |
  SHOW SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER INSTANCES
}
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

## Usage notes

The order of results is not guaranteed.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | The custom classification instance. | Users with the ACCOUNTADMIN admin role can list instances with this command. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Output

Provides custom classifier instance properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| created_on | Date and time when the custom classification instance was created. |
| name | Name of the custom classification instance. |
| database_name | Database that stores the custom classification instance. |
| schema_name | Schema that stores the custom classification instance. |
| current_version | The version of the custom classification instance. Snowflake automatically updates the version number. |
| comment | Comment for the custom classification instance. |
| owner | The role that owns the custom classification instance. |

## Examples

List all of the custom classifiers that you can access:

```sqlexample
SHOW SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER;
```

Returns:

```output
+----------------------------------+---------------+---------------+-------------+-----------------+---------+-------------+
| created_on                       | name          | database_name | schema_name | current_version | comment | owner       |
+----------------------------------+---------------+---------------+-------------+-----------------+---------+-------------+
| 2023-09-08 07:00:00.123000+00:00 | MEDICAL_CODES | DATA          | CLASSIFIERS | 1.0             | None    | DATA_OWNER  |
+----------------------------------+---------------+---------------+-------------+-----------------+---------+-------------+
```
