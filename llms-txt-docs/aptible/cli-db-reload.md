# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-reload.md

# aptible db:reload

This command reloads a [Database](/core-concepts/managed-databases/managing-databases/overview) by replacing the running Database [Container](/core-concepts/architecture/containers/overview) with a new one.

<Tip> Reloading can be useful if your Database appears to be misbehaving.</Tip>

<Note> Using [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) is faster than [`aptible db:restart`](/reference/aptible-cli/cli-commands/cli-db-restart), but it does not let you [resize](/core-concepts/scaling/database-scaling) your Database. </Note>

# Synopsis

```
Usage:
  aptible db:reload HANDLE

Options:
  --env, [--environment=ENVIRONMENT]
```
