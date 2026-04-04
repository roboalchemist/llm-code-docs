# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-backup-orphaned.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible backup:orphaned

This command lists all [Final Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal).

<Note>
  The option, `max-age`, defaults to effectively unlimited (99y years) lookback. For performance reasons, you may want to specify an appropriately narrow period for your use case, like `1w` or `2m`.
</Note>

# Synopsis

```
Usage:
  aptible backup:orphaned

Options:
  --env, [--environment=ENVIRONMENT]
  [--max-age=MAX_AGE]          # Limit backups returned (example usage: 1w, 1y, etc.)
                               # Default: 99y
```
