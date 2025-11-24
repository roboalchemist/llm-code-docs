# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config-unset.md

# aptible config:unset

This command is used to remove [Configuration](/core-concepts/apps/deploying-apps/configuration) variables from an [App](/core-concepts/apps/overview).

> 📘 Tip

> You can also use [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) to set and remove Configuration variables at the same time by passing an empty value:

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        VAR_TO_ADD=some VAR_TO_REMOVE=
```

# Examples

```shell  theme={null}
aptible config:unset --app "$APP_HANDLE" \
        VAR_TO_REMOVE
```

# Synopsis

```
Usage:
  aptible config:unset [VAR1] [VAR2] [...]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]

Remove an ENV variable from an app
```
