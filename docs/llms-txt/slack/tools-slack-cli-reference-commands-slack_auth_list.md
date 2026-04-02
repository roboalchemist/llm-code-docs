Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_auth_list

# slack auth list

List all authorized accounts

## Description {#description}

List all authorized accounts

```text
slack auth list [flags]
```

## Flags {#flags}

```text
  -h, --help   help for list
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```text
slack auth list  # List all authorized accounts
```

## See also {#see-also}

* [slack auth](/tools/slack-cli/reference/commands/slack_auth) - Add and remove local team authorizations
