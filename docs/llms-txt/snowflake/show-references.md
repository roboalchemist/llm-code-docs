# Source: https://docs.snowflake.com/en/sql-reference/sql/show-references.md

# SHOW REFERENCES

Lists the references defined for an application in the manifest file and the references the
consumer has associated to the application.

## Syntax

```sqlsyntax
SHOW REFERENCES IN APPLICATION <name>
```

## Parameters

`name`
:   Specifies the name of the application.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Application | To run this command you must have the ownership privilege on the app. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

This command displays the following information about the references defined for the application:

| Column | Description |
| --- | --- |
| name | The name of the reference. |
| label | The label of the reference as specified in the manifest file. |
| description | A description of the reference and what it does. |
| privileges | The privileges that the reference requires. Refer to [Object types and privileges that a reference can contain](../../developer-guide/native-apps/requesting-refs.md) for the list of privileges that a reference can require for an object. |
| object_type | The type of object associated with the reference. Refer to [Object types and privileges that a reference can contain](../../developer-guide/native-apps/requesting-refs.md) for a list of the supported objects for a reference. |
| multi-valued | Indicates if the reference requires more than one type of object. |
| object_name | The name of the object specified by the reference after the consumer associates the object with the application. |
| schema_name | The name of the schema of the object associated with this reference or NULL if no object has been associated or if the associated object is an account object. |
| database_name | The name of database of the object associated with this reference or NULL if one of the following is true:   *No object is specified in the reference definition.* The object is not a database or database object. |
| alias | A name that uniquely identifies a reference to an object, including the object name, scope and privileges |

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
