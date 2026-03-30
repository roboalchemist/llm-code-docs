# Source: https://docs.firehydrant.com/docs/slack-integration.md

# Slack

<Image align="center" src="https://files.readme.io/d629ddf-slack-enterprise.jpg" />

FireHydrant's Slack and Slack Enterprise Grid integration enables you to drive incidents end-to-end without leaving your collaboration tool. This provides convenience and reduces context switching and toil so your responders can focus on the incident.

## Configuring Slack (non-Enterprise Grid)

To connect your Slack workspace:

1. Go to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations), search for the Slack tile, and click the plus "+."
2. Click "Authorize Application" and follow the on-screen prompts
3. Verify that the FireHydrant workspace is selected from the drop-down in the top right corner of the Slack installation page
4. Follow the Slack prompts. That's it! Now, you'll be able to run any of Slack's commands.

After you set up the integration, we'll automatically link your Slack account to your FireHydrant account.

## Configuring Slack (Enterprise Grid)

> 🚧 Note:
>
> If you've already installed the FireHydrant integration into a Slack workspace and would like to move it to enterprise grid, make sure you uninstall the Integration before continuing.

FireHydrant works great with Slack Enterprise Grid; you can connect your FireHydrant organization to multiple Slack workspaces to leverage creating incidents across a broader set of your organization.

### Installing FireHydrant as an Org-level Integration

If you are a Slack administrator with access to approve Slack apps for the entire organization, this guide is for you!

First, make sure you're [logged in to FireHydrant](https://app.firehydrant.io/sessions/new) and navigate to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations). From there, find the Slack tile and click "+" and then "Authorize Application."

Follow the on-screen prompts **ensuring you select your organization, not an individual workspace** from the dropdown in the top right.

<Image alt="Installing Slack Enterprise Grid" align="center" width="650px" src="https://files.readme.io/a32d1d4-installation-animation.gif">
  Installing Slack Enterprise Grid
</Image>

This will install FireHydrant as an Org-level integration into the selected Slack organization.

### Adding FireHydrant to workspaces

Once FireHydrant has been added to an organization, you must add the integration to the workspaces you'd like to have access to the integration. This enables the members of that workspace to run commands such as `/fh new` to declare incidents.

<Image alt="Adding FireHydrant's bot to multiple workspaces" align="center" width="650px" src="https://files.readme.io/2f11223-adding-to-workspaces.gif">
  Adding FireHydrant's bot to multiple workspaces
</Image>

### Choosing the default workspace

Now for the fun part. When FireHydrant creates channels for incidents, posts into your `#incidents` channel, etc., we need to know which Slack workspace we should do that in!

1. Visit the [integrations page](https://app.firehydrant.io/organizations/integrations) in your FireHydrant account
2. Search for the Slack tile and click the pencil icon
3. Under workspace, select which workspace we should use
4. Click save!

<Image alt="Selecting which workspace FireHydrant posts into in settings" align="center" width="650px" src="https://files.readme.io/9afcf5d-configuring-default-workspace.gif">
  Selecting which workspace FireHydrant posts into in settings
</Image>

> 📘 Note:
>
> Workspaces may take a few minutes to sync (we've configured it to be about every 5 minutes), so grab a coffee, read Hacker News for a few, and smash refresh on this page.

## Opening an incident

If you've added FireHydrant to 1 workspace, or 5, or 50, you can now run the same command from any of them and declare a new incident: `/fh new`.

<Image alt="Voila! New Incidents in Slack" align="center" width="650px" src="https://files.readme.io/835abb8-new-incident.gif">
  Voila! New Incidents in Slack
</Image>

And that's it! You're prepared to declare and manage incidents in your Slack Enterprise Grid organization. Now, brush up on our [Slack Commands](https://docs.firehydrant.com/docs/slack-commands) to get the most value from the Slack integration.

## Linking Users

For users' activities in Slack to be associated with their accounts in FireHydrant, they will need to be linked. FireHydrant will attempt to auto-link users by matching email addresses between Slack and FireHydrant, and this auto-linking will occur in a couple of different scenarios:

* When a user tries to run any `/fh` command from Slack.
* When a user joins an incident channel, whether manually or by [Runbook step](https://docs.firehydrant.com/docs/runbook-step-invite-to-incident-channel)

If auto-linking fails for some reason, users should be able to manually run the `/fh link` command. They can confirm whether their Slack accounts are linked to their FireHydrant accounts by checking their [user profile settings](https://app.firehydrant.io/account/edit).

For organizations with Signals enabled, they will find the **Linked Accounts** section at the bottom of their profile. For orgs without Signals enabled, they will need to go to their User Profile linked above and then click again on their Organization name on the left-hand side.

## Slack integration settings

### Configuration Settings

FireHydrant's Slack integration allows configuring various parameters to make it more powerful and easier to use.

* **Default channel for alerts** - FireHydrant posts a notification message whenever an external system posts an alert to FireHydrant via [Alert Routing](https://docs.firehydrant.com/docs/alert-routing). This default channel will be used to post those notifications\*.
* **Starred event emojis** - When working through incidents, you can "star" or respond to messages from Slack with emojis to mark them as critical items. FireHydrant sets these to `:flag:`, `:flags:`, and `:star:` by default, but you can modify this. To learn more, visit [Incident Timeline](https://docs.firehydrant.com/docs/incident-timeline) docs.
* **Starred confirmation emoji** - When you "star" an event using one of the emojis above, the FireHydrant bot responds by also emoji-responding to that message. By default, it is `:fire:` but this can also be configured.
* **Task emojis** - When [managing tasks](https://docs.firehydrant.com/docs/managing-tasks) via Slack, you can respond to a Slack message with an emoji to automatically turn it into a Task. By default, the emoji is `:ballot_box_with_check:`.
* **Follow up emojis** - Same as with Tasks, you can [manage follow-ups](https://docs.firehydrant.com/docs/managing-follow-ups) from Slack and also similarly create follow-ups with emojis. The default is `:clipboard:`.
* **Enable tutorial command** - You can enable/disable a `/fh tutorial` command, which will execute a [Tutorial-specific Runbook](https://docs.firehydrant.com/docs/tutorial-runbooks).
* **Broadcast incident creation** - By default, when declaring an incident in a channel, FireHydrant will post a [Notify Slack Channel](https://docs.firehydrant.com/docs/runbook-step-notify-slack-channel) card containing information about that incident including name, severity, responders, and links. If you don't want FireHydrant to post anything where a responder declares (the Runbook step linked above will still work), you can disable this.
* **Allow everyone to open incidents?** - By default, FireHydrant allows anyone in your Slack workspace to declare an incident with `/fh new`. Disabling this setting will only allow users with FireHydrant licenses to declare.

> 📘 \*Note:
>
> When you first install FireHydrant, we will try to find a `#incidents` channel in your workspace, and we will use it if it exists. If it does not exist, we will create it. However, you can change the default channel setting here.

### Channel Notification Preferences

[FireHydrant]() posts all incident updates into the incident Slack channel, from details to tasks and more. This can be a little noisy and overwhelming for some organizations, so you may choose to customize which notifications you want in the Slack channel.

1. Navigate to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Slack tile. Click the pencil.
2. In Slack settings, click the **Channel Notification Preferences** tab.
3. Tweak the notification preferences and settings on this page as desired.

<Image alt="Notification Preferences in Slack settings" align="center" width="650px" src="https://files.readme.io/4a92b8f-image.png">
  Notification Preferences in Slack settings
</Image>

### Command Extensions

FireHydrant allows custom commands that either return templated responses (helpful in providing quick, on-the-go rules or resources) or make webhook requests (useful for taking actions in external systems).

To learn more, visit the documentation for [Command Extensions](https://docs.firehydrant.com/docs/command-extensions).

## Slack Connect and Multi-Channel Guests

If you have shared workspaces between multiple Slack organizations, you can have Slack Connect users be a part of incident channels. However, there will be limitations because only one organization/FireHydrant account can own incidents and channels (e.g., you can't "share" one incident between multiple orgs).

* **FireHydrant will track messages and attachments from guest users in shared incident channels.** For example, if Org A owns an incident channel and a guest from Org B joins it, that guest user's messages will be tracked in the timeline. Images and attachments posted by all users in Slack incident channels, including viewers and guests, now correctly appear in the incident timeline regardless of their role or whether RBAC is enabled.
* **But FireHydrant cannot automatically invite Slack Connect users to the incident channel.** This must be done manually. Users have done this by having the FireHydrant bot [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-channel) into a Shared Slack channel with both workspaces' users so they know there's an incident. Users can then manually join/request to join the incident channel.
* **Slack Connect users cannot perform commands on the incident.** If Org A owns the incident channel and a guest user joins that channel from Org B, that guest cannot modify the incident, be assigned roles or tasks, etc.

## Next Steps

Now that your Slack integration is set up, you can start controlling FireHydrant directly from within Slack. You can also configure Runbooks to notify or create specific Slack channels.

Learn more about using FireHydrant and Slack together in these articles:

* [Slack Responder Guide](https://docs.firehydrant.com/docs/slack-responder-guide)
* [Slack Commands](https://docs.firehydrant.com/docs/slack-commands)
* [Command Extensions](https://docs.firehydrant.com/docs/command-extensions)