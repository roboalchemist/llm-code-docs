# Source: https://docs.firehydrant.com/docs/runbook-step-invite-to-slack-incident-channel.md

# Invite to Slack Incident Channel

This Runbook step allows you to automatically invite Slack users to the incident channel using either their emails or their Slack Usernames (see note below), as well as Slack User Groups.

You can invite multiple users and groups and mix and match values by separating them with commas. For example, `@this-group, patchy@example.com, @that-group, @patchys_buddy`.

> 📘 Note:
>
> Slack **Usernames** are not the same as **Display Names**. This Runbook step will not work with Display Names. See the Configuration section below for more details.

## Configuration

1. In the Runbook edit page, click "+ Add Step" and search for "invite".
2. Click on the **Invite to incident channel** step.

<Image alt="Invite to Incident Channel step" align="center" width="650px" src="https://files.readme.io/b4ee5b8-image.png">
  Invite to Incident Channel step
</Image>

3. In the Slack **Identifiers** field, enter comma-delimited emails, Slack usernames, or Slack Groups you'd like invited to the channel.

### Slack Usernames vs. Display Names

When using Slack day-to-day, you will typically mention people by using their Display Names (e.g. `@John Smith` or whatever they set). A Username is a different parameter with different requirements (`e.g. jsmith_123`) and exists for technical reasons we don't know about. Slack does not have an API available today to look up users by Display Names.

To retrieve Slack Usernames, users can visit their profiles by navigating to Slack at **Home Page > Account Settings > Username** or navigating to `YOUR_WORKSPACE.slack.com/account/settings#username` and clicking "Expand" next to **Username**. Alternatively, these values can be retrieved via [Slack's API](https://api.slack.com/methods/users.list).

<Image alt="Where to find your username in Slack" align="center" width="650px" src="https://files.readme.io/b7356e9-slack-username.png">
  Where to find your username in Slack
</Image>