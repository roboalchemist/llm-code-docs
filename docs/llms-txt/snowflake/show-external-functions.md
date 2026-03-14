# Source: https://docs.snowflake.com/en/sql-reference/sql/show-external-functions.md

# SHOW EXTERNAL FUNCTIONS

Lists all the external functions created for your account.

For more information, see [Writing external functions](../external-functions.md).

See also:
:   [SHOW FUNCTIONS](show-functions.md) ,
    [SHOW USER FUNCTIONS](show-user-functions.md),
    [CREATE EXTERNAL FUNCTION](create-external-function.md) ,
    [ALTER FUNCTION](alter-function.md)

## Syntax

```sqlsyntax
SHOW EXTERNAL FUNCTIONS [ LIKE '<pattern>' ]
           [ IN { APPLICATION <application_name> | APPLICATION PACKAGE <application_package_name> }  ]
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

    `APPLICATION application_name`, . `APPLICATION PACKAGE application_package_name`
    :   Returns records for the named Snowflake Native App or application package.

## Usage notes

* The commands [SHOW FUNCTIONS](show-functions.md) and [SHOW USER FUNCTIONS](show-user-functions.md) also display information
  about external functions.

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

## Examples

Show all external functions:

> ```sqlexample
> SHOW EXTERNAL FUNCTIONS;
> ```

Show only external functions matching the specified regular expression:

> ```sqlexample
> SHOW EXTERNAL FUNCTIONS LIKE 'SQUARE%';
> ```
