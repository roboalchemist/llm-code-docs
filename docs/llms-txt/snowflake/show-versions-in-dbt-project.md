# Source: https://docs.snowflake.com/en/sql-reference/sql/show-versions-in-dbt-project.md

# SHOW VERSIONS IN DBT PROJECT

Displays a list of all versions of a [dbt project object](../../user-guide/data-engineering/dbt-projects-on-snowflake.md).

See also:
:   [ALTER DBT PROJECT](alter-dbt-project.md), [DESCRIBE DBT PROJECT](desc-dbt-project.md), [EXECUTE DBT PROJECT](execute-dbt-project.md), [SHOW DBT PROJECTS](show-dbt-projects.md), [DROP DBT PROJECT](drop-dbt-project.md)

## Syntax

```sqlsyntax
SHOW VERSIONS IN DBT PROJECT <name>
  [ LIMIT <number> ]
```

## Parameters

`name`
:   String that specifies the identifier (that is, the name) for the dbt project object within Snowflake; must be unique for the schema in which
    the dbt project is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`LIMIT rows`
:   Optionally limits the maximum number of rows returned. The actual number of rows returned might be less than the specified limit. For
    example, the number of existing objects is less than the specified limit.

    Default: No value (no limit is applied to the output).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| USAGE | The dbt project object |
| MONITOR | The dbt project object |
| OWNERSHIP | The dbt project object |

## Usage notes

* The command doesn’t require a running warehouse to execute.
* The command only returns objects for which the current user’s current role has been granted at least one access privilege.
* The MANAGE GRANTS access privilege implicitly allows its holder to see every object in the account. By default, only the account
  administrator (users with the ACCOUNTADMIN role) and security administrator (users with the SECURITYADMIN role) have the
  MANAGE GRANTS privilege.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Output

The command output provides table properties and metadata about versions of dbt Projects in the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the dbt project object was created. |
| `name` | The auto-assigned name of the dbt project version. For example, `VERSION$1`. |
| `alias` | The alias for the dbt Project you assigned (for example, `ALTER DBT PROJECT <name> ADD VERSION <alias> FROM ...`). Null if not specified. |
| `location_uri` | Full URL of the dbt project version. |
| `is_default` | TRUE if the default version of the dbt project object points to this version. |
| `is_live` | TRUE if the dbt project version is a live version of the listing. |
| `is_first` | TRUE if the dbt Project is the first version. |
| `is_last` | TRUE if the dbt Project is the last version. |
| `comment` | Comment set on the dbt Project. |
| `source_location_uri` | The source location URI where this dbt project version is created from. |
| `git_commit_hash` | The git commit hash, if the dbt project version was created from a git source. |

## Examples

Show all versions of `my_dbt_project`:

```sqlexample
SHOW VERSIONS IN DBT PROJECT my_dbt_project;
```

```output
+---------------------------------+-----------+-------+----------------------------------------------------------------------+------------+---------+----------+---------+---------+---------------------+-----------------+
|             created_on          | name      | alias |  location_uri                                                        | is_default | is_live | is_first | is_last | comment | source_location_uri | git_commit_hash |
+---------------------------------+-----------+-------+----------------------------------------------------------------------+------------+--------------------+---------+---------+---------------------+-----------------+
|   2025-01-08 11:18:24.550 -0800 | VERSION$2 | null  |  snow://dbtproject/mydb.my_schema.my_dbt_project/versions/version$2/ | TRUE       | FALSE   | FALSE    |  TRUE   | null    | null                | null            |
|   2025-01-08 11:17:32.894 -0800 | VERSION$1 | null  |  snow://dbtproject/mydb.my_schema.my_dbt_project/versions/version$2/ | FALSE      | FALSE   | TRUE     |  FALSE  | null    | null                | null            |
+---------------------------------+-----------+------------------------------+-----------------------------------------------+------------+--------------------+---------+---------+---------------------+-----------------+
```
