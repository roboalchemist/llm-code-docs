Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_upgrade

# slack upgrade

Checks for available updates to the CLI or SDK

## Description {#description}

Checks for available updates to the CLI or the SDKs of a project

If there are any, then you will be prompted to upgrade

The changelog can be found at [https://docs.slack.dev/changelog](https://docs.slack.dev/changelog)

```text
slack upgrade [flags]
```

## Flags {#flags}

```text
  -h, --help   help for upgrade
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```text
slack upgrade  # Check for any available updates
```

## See also {#see-also}

* [slack](/tools/slack-cli/reference/commands/slack) - Slack command-line tool
