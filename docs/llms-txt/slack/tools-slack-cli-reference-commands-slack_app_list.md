Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_app_list

# slack app list

List teams with the app installed

## Description {#description}

List all teams that have installed the app

```text
slack app list [flags]
```

## Flags {#flags}

```text
      --all-org-workspace-grants   display all workspace grants for an app                                   installed to an organization  -h, --help                       help for list
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```text
slack app list  # List all teams with the app installed
```

## See also {#see-also}

* [slack app](/tools/slack-cli/reference/commands/slack_app) - Install, uninstall, and list teams with the app installed
