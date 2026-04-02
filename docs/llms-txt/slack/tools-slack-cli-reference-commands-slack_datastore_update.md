Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_datastore_update

# slack datastore update

Create or update an item in a datastore

## Description {#description}

Create or update an item in a datastore.

This command is supported for apps deployed to Slack managed infrastructure but other apps can attempt to run the command with the --force flag.

```text
slack datastore update <expression> [flags]
```

## Flags {#flags}

```text
      --datastore string   the datastore used to store items  -h, --help               help for update      --show               only construct a JSON expression      --unstable           kick the tires of experimental features
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```bash
# Update the entry in the datastore$ slack datastore update --datastore tasks '{"item": {"id": "42", "description": "Create a PR", "status": "Done"}}'# Update the entry in the datastore with an expression$ slack datastore update '{"datastore": "tasks", "item": {"id": "42", "description": "Create a PR", "status": "Done"}}'
```

## See also {#see-also}

* [slack datastore](/tools/slack-cli/reference/commands/slack_datastore) - Interact with an app's datastore
