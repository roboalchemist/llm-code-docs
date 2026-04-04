Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_trigger_info

# slack trigger info

Get details for a specific trigger

## Description {#description}

Get details for a specific trigger

```text
slack trigger info --trigger-id <id> [flags]
```

## Flags {#flags}

```text
  -h, --help                help for info      --trigger-id string   the ID of the trigger
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```bash
# Get details for a specific trigger in a selected workspace$ slack trigger info --trigger-id Ft01234ABCD# Get details for a specific trigger$ slack trigger info --trigger-id Ft01234ABCD --app A0123456
```

## See also {#see-also}

* [slack trigger](/tools/slack-cli/reference/commands/slack_trigger) - List details of existing triggers
