# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config.md

# aptible config

This command prints an App's [Configuration](/core-concepts/apps/deploying-apps/configuration) variables.

## Synopsis

```
Usage:
  aptible config

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```

> ❗️\*\* Warning:\*\* The output of this command is shell escaped, meaning if you have included any special characters, they will be shown with an escape character. For instance, if you set `"foo=bar?"` it will be displayed by [`aptible config`](/reference/aptible-cli/cli-commands/cli-config) as `foo=bar\?`.

> If the values do not appear as you expect, you can further confirm how they are set using the JSON output\_format, or by inspecting the environment of your container directly using an [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions).

# Examples

```shell  theme={null}
aptible config --app "$APP_HANDLE"
```
