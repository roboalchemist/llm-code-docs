# Source: https://docs.snowflake.com/en/sql-reference/sql/show-notebook-projects.md

# SHOW NOTEBOOK PROJECTS

Lists the notebook projects (Snowflake `NOTEBOOK` objects) visible to the current role.

You can use this command to list objects in the current database and schema for the session, a specified database or schema, or
your entire account.

The output includes the metadata and properties for each object. The objects are sorted lexicographically by database, schema,
and object name (see Output in this topic for descriptions of the output columns). The order of rows in the results is important
to note if you want to filter the results.

See also:
:   [CREATE NOTEBOOK PROJECT](create-notebook-project.md), [EXECUTE NOTEBOOK PROJECT](execute-notebook-project.md), [SHOW NOTEBOOKS](show-notebooks.md), [DESCRIBE NOTEBOOK](desc-notebook.md)

## Syntax

```sqlsyntax
SHOW NOTEBOOK PROJECTS;

SHOW NOTEBOOK PROJECTS IN SCHEMA <database_name>.<schema_name>;

SHOW NOTEBOOK PROJECTS IN DATABASE <database_name>;

SHOW NOTEBOOK PROJECTS IN ACCOUNT;
```

## Parameters

`IN SCHEMA <database_name>.<schema_name>`
:   Lists notebook projects in the specified schema.

`IN DATABASE <database_name>`
:   Lists notebook projects in all schemas of the specified database.

`IN ACCOUNT`
:   Lists all notebook projects in the account that are visible to the current role.

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | Timestamp of creation. |
| `name` | Name of the notebook project. |
| `database_name` | Database containing the notebook project. |
| `schema_name` | Schema containing the notebook project. |
| `owner` | The role that owns the notebook project. |
| `comment` | Comment associated with the notebook project. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE or OWNERSHIP | Database | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| USAGE or OWNERSHIP | Schema | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

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

* The command returns a maximum of ten thousand records for the specified object type, as dictated by the access privileges for the role
  used to execute the command. Any records above the ten thousand records limit aren’t returned, even with a filter applied.

  To view results for which more than ten thousand records exist, query the corresponding view (if one exists) in the [Snowflake Information Schema](../info-schema.md).

* Returns all Snowflake `NOTEBOOK` objects visible to the current role.
* Use [DESCRIBE NOTEBOOK](desc-notebook.md) or `GET_DDL('NOTEBOOK', ...)` to inspect contents.
* Identifiers containing special characters must be double-quoted.

## Examples

List all notebook projects visible to the current role:

```sqlexample
SHOW NOTEBOOK PROJECTS;
```

List notebook projects in a specific schema:

```sqlexample
SHOW NOTEBOOK PROJECTS IN SCHEMA TESTDB.TESTSCHEMA;
```

List notebook projects in a specific database:

```sqlexample
SHOW NOTEBOOK PROJECTS IN DATABASE TESTDB;
```

List notebook projects in the account:

```sqlexample
SHOW NOTEBOOK PROJECTS IN ACCOUNT;
```
