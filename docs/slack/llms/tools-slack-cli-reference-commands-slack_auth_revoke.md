Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_auth_revoke

# slack auth revoke

Revoke an authentication token

## Description {#description}

Revoke an authentication token

```text
slack auth revoke [flags]
```

## Flags {#flags}

```text
  -h, --help   help for revoke
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```text
slack auth revoke --token xoxp-1-4921830...  # Revoke a service token
```

## See also {#see-also}

* [slack auth](/tools/slack-cli/reference/commands/slack_auth) - Add and remove local team authorizations
