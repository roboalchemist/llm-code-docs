Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_datastore_query

# slack datastore query

Query a datastore for items

## Description {#description}

Query a datastore for items.

This command is supported for apps deployed to Slack managed infrastructure but other apps can attempt to run the command with the --force flag.

```text
slack datastore query <expression> [flags]
```

## Flags {#flags}

```typescript
      --datastore string   the datastore used to store items  -h, --help               help for query      --output string      output format: text, json (default "text")      --show               only construct a JSON expression      --to-file string     save items directly to a file as JSON Lines      --unstable           kick the tires of experimental features
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```bash
# Collect a limited set of items from the datastore$ slack datastore query --datastore tasks '{"limit": 8}' --output json# Collect items from the datastore starting at a cursor$ slack datastore query --datastore tasks '{"cursor": "eyJfX2NWaV..."}'# Query the datastore for specific items$ slack datastore query --datastore tasks '{"expression": "#status = :status", "expression_attributes": {"#status": "status"}, "expression_values": {":status": "In Progress"}}'# Query the datastore for specific items with only an expression$ slack datastore query '{"datastore": "tasks", "expression": "#status = :status", "expression_attributes": {"#status": "status"}, "expression_values": {":status": "In Progress"}}'
```

## See also {#see-also}

* [slack datastore](/tools/slack-cli/reference/commands/slack_datastore) - Interact with an app's datastore
