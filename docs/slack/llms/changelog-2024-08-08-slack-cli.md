Source: https://docs.slack.dev/changelog/2024/08/08/slack-cli

# Release: Slack CLI v2.29.1

August 8, 2024

Version 2.29.1 of the developer tools for the Slack automations platform has arrived!

* We updated the shell called in Windows commands from `pwsh` to `powershell` for better backwards compatibility.
* We added the ability to retrieve manifest information using the `--source` flag with the [`manifest info`](/tools/slack-cli/reference/commands/slack_manifest_info) command. The flag can be set to either `project` or `remote`.
* We fixed an issue to raise any errors in the Slack CLI that may occur when running the `npm install` command.
* We fixed a bug to replace the `--workspace` flag recommendation with a `--team` flag recommendation.

**Tags:**

* [Release](/changelog/tags/release)
* [Slack CLI](/changelog/tags/slack-cli)
