Source: https://docs.slack.dev/changelog/2025/12/04/slack-cli

# Release: Slack CLI v3.10.0

December 4, 2025

Version `3.10.0` of the developer tools for the Slack platform is here!

* We've added the [`slack app unlink`](/tools/slack-cli/reference/commands/slack_app_unlink) command, which removes an existing App ID from your project (it will not delete the app from Slack).
* We've added support for read-only app collaborators (applicable to deployed [Deno apps](/tools/deno-slack-sdk/guides/deploying-to-slack) only):
  * To add a new collaborator as read-only, use the `slack collaborator add --permission-type=reader` command.
  * To update an existing collaborator to be read-only, use the `slack collaborator update --permission-type=reader` command.
  * To assign a collaborator as an owner, use the `--permission-type=owner` flag.

**Tags:**

* [Release](/changelog/tags/release)
* [Slack CLI](/changelog/tags/slack-cli)
