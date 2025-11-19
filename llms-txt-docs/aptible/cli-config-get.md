# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config-get.md

# aptible config:get

This command prints a single value from the App's [Configuration](/core-concepts/apps/deploying-apps/configuration) variables.

# Synopsis

```
Usage:
  aptible config:get [VAR1]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```

# Examples

```shell  theme={null}
aptible config:get FORCE_SSL --app "$APP_HANDLE"
```
