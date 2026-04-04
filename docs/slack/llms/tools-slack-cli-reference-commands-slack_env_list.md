Source: https://docs.slack.dev/tools/slack-cli/reference/commands/slack_env_list

# slack env list

List all environment variables for the app

## Description {#description}

List all of the environment variables of an app deployed to Slack managed infrastructure.

This command is supported for apps deployed to Slack managed infrastructure but other apps can attempt to run the command with the --force flag.

```text
slack env list [flags]
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
slack env list  # List all environment variables
```

## See also {#see-also}

* [slack env](/tools/slack-cli/reference/commands/slack_env) - Add, remove, or list environment variables
