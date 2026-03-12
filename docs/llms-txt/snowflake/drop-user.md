# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-user.md

# DROP USER

Removes the specified user from the system.

See also:
:   [CREATE USER](create-user.md) , [ALTER USER](alter-user.md) , [SHOW USERS](show-users.md) , [DESCRIBE USER](desc-user.md)

## Syntax

```sqlsyntax
DROP USER [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the user to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Dropped users cannot be recovered; they must be recreated.

  If you want to disable a user, use [ALTER USER](alter-user.md) and set `DISABLED = TRUE` instead.
* If there is a conflict between a local user object and an [organization user](../../user-guide/organization-users.md), a user that
  corresponds to the organization user is automatically created when you drop the local user.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

> **Important:**
>
> When you drop a user, the folders, worksheets, and dashboards owned by that user become inaccessible and **do not** transfer to another user
> unless sharing is enabled.
>
> Share recipients with [View, View + Run, and Edit permissions](../../user-guide/ui-snowsight-worksheets.md)
> will retain their assigned permissions and can still access the shared folders, worksheets, and dashboards. However, only users with Edit
> permissions can modify or delete the shared folders, worksheets, and dashboards. If you don’t give Edit permissions to at least one other
> user before you drop the owner, that owner’s folders, worksheets, and dashboards cannot be deleted.
>
> If a dropped user’s worksheets do not have sharing enabled, an administrator can [recover up to 500 worksheets owned by the user](../../user-guide/ui-snowsight-worksheets.md).

> **Caution:**
>
> Any worksheets in the Classic Console will be permanently deleted, and dashboards will be inaccessible if they were not previously shared
> with another user.

## Examples

> ```sqlexample
> DROP USER user1;
> ```
