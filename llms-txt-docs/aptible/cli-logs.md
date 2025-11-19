# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-logs.md

# aptible logs

This command lets you access real-time logs for an [App](/core-concepts/apps/overview) or [Database](/core-concepts/managed-databases/managing-databases/overview).

# Synopsis

```
Usage:
  aptible logs [--app APP | --database DATABASE]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--database=DATABASE]
```

# Examples

## App logs

```shell  theme={null}
aptible logs --app "$APP_HANDLE"
```

## Database logs

```shell  theme={null}
aptible logs --database "$DATABASE_HANDLE"
```
