Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_collaborator_remove

# slack collaborator remove

Remove a collaborator from an app

## Description {#description}

Remove a collaborator from an app by Slack email address or user ID

```text
slack collaborator remove [email|user_id] [flags]
```

## Flags {#flags}

```text
  -h, --help   help for remove
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```python
slack collaborator remove                # Remove collaborator on prompt$ slack collaborator remove bot@slack.com  # Remove collaborator by email$ slack collaborator remove USLACKBOT      # Remove collaborator using ID
```

## See also {#see-also}

* [slack collaborator](/tools/slack-cli/reference/commands/slack_collaborator) - Manage app collaborators
