# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-ssh.md

# aptible ssh

This command creates [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) to [Apps](/core-concepts/apps/overview) running on Aptible.

# Synopsis

```
Usage:
  aptible ssh [COMMAND]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--force-tty], [--no-force-tty]

Description:
  Runs an interactive command against a remote Aptible app

  If specifying an app, invoke via: aptible ssh [--app=APP] COMMAND
```

# Examples

```shell  theme={null}
aptible ssh --app "$APP_HANDLE"
```
