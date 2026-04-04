Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_delete

# slack delete

Delete the app

## Description {#description}

Uninstall the app from the team and permanently delete the app and all of its data

```text
slack delete [flags]
```

## Flags {#flags}

```text
  -h, --help   help for delete
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```bash
# Delete an app and app info from a team$ slack app delete# Delete a specific app from a team$ slack app delete --team T0123456 --app local
```

## See also {#see-also}

* [slack](/tools/slack-cli/reference/commands/slack) - Slack command-line tool
