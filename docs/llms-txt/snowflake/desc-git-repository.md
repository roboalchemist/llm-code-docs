# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-git-repository.md

# DESCRIBE GIT REPOSITORY

Describes an existing Snowflake [Git repository clone](../../developer-guide/git/git-overview.md).

See also:
:   [ALTER GIT REPOSITORY](alter-git-repository.md), [CREATE GIT REPOSITORY](create-git-repository.md), [DROP GIT REPOSITORY](drop-git-repository.md), [SHOW GIT BRANCHES](show-git-branches.md),
    [SHOW GIT REPOSITORIES](show-git-repositories.md), [SHOW GIT TAGS](show-git-tags.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } GIT REPOSITORY <name>
```

## Parameters

`name`
:   Specifies the identifier for the Git repository clone to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command output includes properties in the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date the Git repository clone was created. |
| `name` | Name of the Git repository clone. |
| `database_name` | Name of the database containing this Git repository clone. |
| `schema_name` | Name of the schema containing this Git repository clone. |
| `origin` | URL of the remote Git repository’s origin. |
| `api_integration` | Name of the API integration included in this Git repository clone. |
| `git_credentials` | Name of the secret object in this Git repository clone. |
| `owner` | Role used when this Git repository clone was created. |
| `owner_role_type` | Type of role that owns the object, either ROLE or DATABASE_ROLE. |
| `comment` | Comment specified when this Git repository clone was created. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Git repository | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

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

The following example generates a description of the `snowflake_extensions` Git repository clone:

```sqlexample
DESCRIBE GIT REPOSITORY snowflake_extensions;
```

The preceding command generates output such as the following:

```output
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| CREATED_ON                    | NAME                 | DATABASE_NAME | SCHEMA_NAME | ORIGIN                                                 | API_INTEGRATION     | GIT_CREDENTIALS           | OWNER        | OWNER_ROLE_TYPE | COMMENT |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 2023-06-28 08:46:10.886 -0700 | SNOWFLAKE_EXTENSIONS | MY_DB         | MAIN        | https://github.com/my-account/snowflake-extensions.git | GIT_API_INTEGRATION | MY_DB.MAIN.GIT_SECRET     | ACCOUNTADMIN | ROLE            |         |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
