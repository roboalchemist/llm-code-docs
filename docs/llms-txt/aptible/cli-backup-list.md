# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-backup-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible backup:list

This command lists all [Database Backups](/core-concepts/managed-databases/managing-databases/database-backups) for a given [Database](/core-concepts/managed-databases/overview).

<Note>
  The option, `max-age`, defaults to effectively unlimited (99y years) lookback. For performance reasons, you may want to specify an appropriately narrow period for your use case, like `3d` or `2w`.
</Note>

## Synopsis

```
Usage:
  aptible backup:list DB_HANDLE

Options:
  --env, [--environment=ENVIRONMENT]
  [--max-age=MAX_AGE]          # Limit backups returned (example usage: 1w, 1y, etc.)
                               # Default: 99y

```

# Examples

```shell  theme={null}
aptible backup:list "$DB_HANDLE"
```
