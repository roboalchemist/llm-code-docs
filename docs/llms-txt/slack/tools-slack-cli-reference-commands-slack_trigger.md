Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_trigger

# slack trigger

List details of existing triggers

## Description {#description}

List details of existing triggers

```text
slack trigger [flags]
```

## Flags {#flags}

```text
  -h, --help   help for trigger
```

## Global flags {#global-flags}

```text
  -a, --app string           use a specific app ID or environment      --config-dir string    use a custom path for system config directory  -e, --experiment strings   use the experiment(s) in the command  -f, --force                ignore warnings and continue executing command      --no-color             remove styles and formatting from outputs  -s, --skip-update          skip checking for latest version of CLI  -w, --team string          select workspace or organization by team name or ID      --token string         set the access token associated with a team  -v, --verbose              print debug logging and additional info
```

## Examples {#examples}

```bash
# Select who can run a trigger$ slack trigger access$ slack trigger create                           # Create a new trigger# Delete an existing trigger$ slack trigger delete --trigger-id Ft01234ABCD# Get details for a trigger$ slack trigger info --trigger-id Ft01234ABCD# List details for all existing triggers$ slack trigger list# Update a trigger definition$ slack trigger update --trigger-id Ft01234ABCD
```

## See also {#see-also}

* [slack](/tools/slack-cli/reference/commands/slack) - Slack command-line tool
* [slack trigger access](/tools/slack-cli/reference/commands/slack_trigger_access) - Manage who can use your triggers
* [slack trigger create](/tools/slack-cli/reference/commands/slack_trigger_create) - Create a trigger for a workflow
* [slack trigger delete](/tools/slack-cli/reference/commands/slack_trigger_delete) - Delete an existing trigger
* [slack trigger info](/tools/slack-cli/reference/commands/slack_trigger_info) - Get details for a specific trigger
* [slack trigger list](/tools/slack-cli/reference/commands/slack_trigger_list) - List details of existing triggers
* [slack trigger update](/tools/slack-cli/reference/commands/slack_trigger_update) - Updates an existing trigger
