# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-git-repository.md

# DROP GIT REPOSITORY

Removes the specified Snowflake Git repository clone from the current/specified schema.

See also:
:   [ALTER GIT REPOSITORY](alter-git-repository.md), [CREATE GIT REPOSITORY](create-git-repository.md), [DESCRIBE GIT REPOSITORY](desc-git-repository.md), [SHOW GIT BRANCHES](show-git-branches.md),
    [SHOW GIT REPOSITORIES](show-git-repositories.md), [SHOW GIT TAGS](show-git-tags.md)

## Syntax

```sqlsyntax
DROP GIT REPOSITORY [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the Git repository clone to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Usage notes

* Dropped Git repositories can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

> ```sqlexample
> DROP GIT REPOSITORY my_repository;
> ```
>
> ```output
> +-------------------------------------+
> |                status               |
> +-------------------------------------+
> | MY_REPOSITORY successfully dropped. |
> +-------------------------------------+
> ```
