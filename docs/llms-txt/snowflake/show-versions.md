# Source: https://docs.snowflake.com/en/sql-reference/sql/show-versions.md

# SHOW VERSIONS IN APPLICATION PACKAGE

Lists the versions defined in the specified application package.

See also:
:   [ALTER APPLICATION](alter-application.md), [CREATE APPLICATION](create-application.md), [DESCRIBE APPLICATION](desc-application.md), [DROP APPLICATION](drop-application.md)

## Syntax

```sqlsyntax
SHOW VERSIONS [ LIKE <pattern> ]
  IN APPLICATION PACKAGE <name>;
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

`IN APPLICATION PACKAGE name`
:   Specifies the identifier for the application package whose versions you want to view.

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

## Example

```sqlexample
SHOW VERSIONS IN APPLICATION PACKAGE hello_snowflake_app;
```

```output
+----------------+-------+---------+---------+-------------------------------+------------+-----------+-------------+-------+---------------+
| version        | patch | label   | comment | created_on                    | dropped_on | log_level | trace_level | state | review_status |
|----------------+-------+---------+---------+-------------------------------+------------+-----------+-------------+-------+---------------|
| V1_0           |     0 | NULL    | NULL    | 2023-05-10 17:11:47.696 -0700 | NULL       | OFF       | OFF         | READY | NOT_REVIEWED  |
+----------------+-------+---------+---------+-------------------------------+------------+-----------+-------------+-------+---------------+
```
