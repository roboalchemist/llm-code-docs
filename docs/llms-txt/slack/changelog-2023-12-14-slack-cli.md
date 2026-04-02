Source: https://docs.slack.dev/changelog/2023/12/14/slack-cli

# Release: Slack CLI v2.15.0

December 14, 2023

Version `2.15.0` of the developer tools for the Slack automations platform is home for the holidays!

* We've updated the _choose a workspace to grant access_ prompt to sort by team name rather than team ID.
* We've deprecated the `deno` command and removed its listing from the `help` command. The `deno` command is slated to be removed completely in an upcoming release.
* Endpoints at `api.slack.com` are no longer blocked by a permission error for local apps.
* We now have better error handling when appending a `(local)` tag to the display name of local apps.
* We've removed some extra blank lines and debug information from command outputs for a cleaner look and faster feel.
* We've provided prompts for possible trigger IDs for trigger commands that need them.

**Tags:**

* [Release](/changelog/tags/release)
* [Slack CLI](/changelog/tags/slack-cli)
