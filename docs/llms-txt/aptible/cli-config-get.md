# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible config:get

This command prints a single value from the App's [Configuration](/core-concepts/apps/deploying-apps/configuration) variables.

# Synopsis

```
Usage:
  aptible config:get [--app APP] [VAR1]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```

# Examples

```shell  theme={null}
aptible config:get FORCE_SSL --app "$APP_HANDLE"
```
