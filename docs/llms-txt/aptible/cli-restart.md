# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-restart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible restart

This command restarts an [App](/core-concepts/apps/overview) and all its associated [Services](/core-concepts/apps/deploying-apps/services).

# Synopsis

```
Usage:
  aptible restart [--app APP]

Options:
      [--simulate-oom], [--no-simulate-oom]  # Add this flag to simulate an OOM restart and test your app's response (not recommended on production apps).
      [--force]                              # Add this flag to use --simulate-oom in a production environment, which is not allowed by default.
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```

# Examples

```shell  theme={null}
aptible restart --app "$APP_HANDLE"
```
