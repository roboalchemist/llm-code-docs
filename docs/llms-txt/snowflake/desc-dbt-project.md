# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-dbt-project.md

# DESCRIBE DBT PROJECT

Describes the properties of a [dbt project object](../../user-guide/data-engineering/dbt-projects-on-snowflake.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE DBT PROJECT](create-dbt-project.md), [ALTER DBT PROJECT](alter-dbt-project.md), [EXECUTE DBT PROJECT](execute-dbt-project.md), [DROP DBT PROJECT](drop-dbt-project.md), [SHOW DBT PROJECTS](show-dbt-projects.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } DBT PROJECT <name>
```

## Parameters

`name`
:   Specifies the identifier for the dbt project object to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `name` | The identifier (name) of the dbt project object. |
| `owner` | The role that was used to create the dbt project object. |
| `comment` | The comment associated with the dbt project object. |
| `dbt_version` | The version for the dbt Project. If no value is specified, the system uses version 1.9.4 by default. |
| `dbt_snowflake_version` | The Snowflake version the dbt project object is on. |
| `default_target` | The default execution target (for example, `prod` or `dev`) used by dbt commands executed through Snowflake. |
| `external_access_integrations` | The name of the external access integrations the dbt Project is permitted to use to pull remote dependencies from dbt package hub or GitHub. |

The following columns provide the value of a deprecated parameter:

| Column | Description |
| --- | --- |
| `default_version` | The version of the dbt project object:   *`LAST`: The most recent version of the dbt project object.* `FIRST`: The oldest version of the dbt project object. |
| `default_version_name` | The version identifier in the form `VERSION$num`, where `num` is a positive integer, for example: `VERSION$1`.  The version number begins at `1` when you create a dbt project object and increments by one with each new version of the dbt project object.  Snowflake increments the version identifier when you perform the following tasks:   *Redeploy dbt project from a workspace (runs the ALTER command with the ADD VERSION option).* Update the project by using the [ALTER DBT PROJECT](alter-dbt-project.md) command. * Run the Snow CLI `snow dbt deploy` command with the `--force` option.   Snowflake resets the version identifier to `1` and removes all version aliases when you run the CREATE DBT PROJECT command with the OR REPLACE option. |
| `default_version_alias` | The custom version name alias that you created for a specific version of the dbt project object using the ALTER DBT PROJECT command with the ADD VERSION option. A version name alias always maps to a specific version identifier, such as `VERSION$3`. |
| `default_version_location_uri` | The location URI of the default version. This is read only. |
| `default_version_source_location_uri` | The location URI of the default version’s source files in its Git object. If the dbt project object is not connected to a Git object, this is null. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| MONITOR | dbt project |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

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

## Examples

The following example describes the dbt project object named `my_dbt_project`:

```sqlexample
DESCRIBE DBT PROJECT my_dbt_project;
```

```output
+----------------+--------------+------------+-------------+-----------------+----------------------+-----------------------+---------------------------------------------------------------+-------------------------------------+-----------------------+----------------+------------------------------+
|      name      |    owner     |  comment   | dbt_version | default_version | default_version_name | default_version_alias | default_version_location_uri                                  | default_version_source_location_uri | dbt_snowflake_version | default_target | external_access_integrations |
+----------------+--------------+------------+-------------+-----------------+----------------------+-----------------------+---------------------------------------------------------------+-------------------------------------+-----------------------+----------------+------------------------------+
| my_dbt_project | ACCOUNTADMIN | My comment | 1.9.4b      | LAST            | VERSION$1            | null                  | snow://dbt/MY_DB.MY_SCHEMA.my_dbt_project/versions/version$1/ | @s1                                 | null                  | dev            | null                         |
+----------------+--------------+------------+-------------+-----------------+----------------------+-----------------------+---------------------------------------------------------------+-------------------------------------+-----------------------+----------------+------------------------------+
```
