# Source: https://docs.port.io/ai-interfaces/slack-app.md

# Slack Application

Port's Slack app brings your developer portal experience into your team's daily communication flow â allowing you to interact with Port directly from Slack and receive real-time notifications from Port right where your team collaborates. The Slack app uses the [Port AI API](/ai-interfaces/port-ai/overview.md) to provide intelligent answers about your software catalog, similar to the [Port AI Assistant](/ai-interfaces/port-ai-assistant.md).

![](/img/ai-agents/AIAgentsSlackExample.png)

## Use-cases[â](#use-cases "Direct link to Use-cases")

### Manage notifications[â](#manage-notifications "Direct link to Manage notifications")

The Slack app allows you to send messages to any Slack channel directly from Port, without the need to create a separate webhook for each channel.

This can be used to communicate important notifications to people in your organization, such as:

* A new PagerDuty incident has been created.
* A new GitHub issue has been created.
* A GitLab merge request has been merged.

### Interact with AI capabilities[â](#interact-with-ai-capabilities "Direct link to Interact with AI capabilities")

Another powerful use-case of the Slack app is to interact with Port's AI capabilities directly from Slack. The Slack app uses the **[Port AI API](/ai-interfaces/port-ai/overview.md)** (similar to the **[Port AI Assistant](/ai-interfaces/port-ai-assistant.md)**) to provide intelligent answers about your software catalog.

This can be used to get quick answers to questions about your resources, such as:

* Which services had an incident in the last 30 days?
* How many open Jira tickets are there for the service 'x'?
* What is the status of the deployment 'y'?

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* A Port account with **admin** permissions.

## Installation[â](#installation "Direct link to Installation")

To install the Slack app, follow these steps:

1. Go to the [Builder page](https://app.getport.io/settings/data-model) of your portal.

2. Click on `Organization settings` in the sidebar.

3. Select the `Slack App` tab.

4. Click on the **Add to Slack** button.

5. Select the workspace where you'd like to install the app, then click **Allow**.

6. Once installed, you will receive a Slack message from Port's bot with a summary of the app's capabilities:

   ![](/img/ai-agents/SlackAppInstallMessage.png)

## Display channel names in catalog[â](#display-channel-names-in-catalog "Direct link to Display channel names in catalog")

Once you install the Port Slack app, Port automatically enriches any Slack channel URL in your catalog with the actual channel name. This makes it easier to understand context, ownership, and communication paths at a glance.

![Slack channel names displayed in catalog](/img/ai-agents/SlackAppChannelNameInCatalog.png)

The feature works automatically with no additional configuration required. Install the Slack app from the `Slack App` tab in your organization settings (**Builder** â **Organization Settings** â **Slack App**), and channel names will appear wherever Slack URLs are present in your catalog.

## Send notifications from Port[â](#send-notifications-from-port "Direct link to Send notifications from Port")

### Slack app bot token[â](#slack-app-bot-token "Direct link to Slack app bot token")

Once the app is installed into the Slack workspace, a new system secret will be created in your Port organization named `__SLACK_APP_BOT_TOKEN_T<team_id>`, where `<team_id>` is the ID of the Slack workspace.<br /><!-- -->You can copy it and use it in actions & automations to send messages to a specific Slack channel.

System secrets

To view your system secrets, click on the `...` button in the top right corner of your Port application, select `Credentials` and then click on the `Secrets` tab.

### Usage example[â](#usage-example "Direct link to Usage example")

The following snippet defines an automation that sends a Slack message to a specific channel when a new PagerDuty incident is created in Port, using the Slack app's bot token:

Create in Port

```
{
  "identifier": "pagerduty_incident_to_slack",
  "title": "PagerDuty incident to slack",
  "icon": "pagerduty",
  "description": "Sends a Slack message on new incident",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_CREATED",
      "blueprintIdentifier": "pagerdutyIncident"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://slack.com/api/chat.postMessage",
    "synchronized": true,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json; charset=utf-8",
      "Authorization": "Bearer {{ .secrets.\"__SLACK_APP_BOT_TOKEN_T123\" }}"
    },
    "body": {
      "blocks": [
        {
          "type": "markdown",
          "text": "There is a new incident!\nTitle: {{ .event.diff.after.title }}\nOwner: {{ .event.diff.after.properties.assignees }}"
        }
      ],
      "channel": "C06BUh123"
    }
  },
  "publish": true
}
```

### Customize messages[â](#customize-messages "Direct link to Customize messages")

You can customize messages with blocks following the [Slack formatting guidelines](https://slack.com/help/articles/202288908-Format-your-messages).

## Interact with Port from Slack[â](#interact-with-port-from-slack "Direct link to Interact with Port from Slack")

### New user authentication flow[â](#new-user-authentication-flow "Direct link to New user authentication flow")

When a new team member first tries to use the Slack app, a private message with a "Connect to Port" button will be sent to them:

![](/img/ai-agents/SlackAppNewUserMessage.png)

<br />

<br />

Once the user is authenticated, they can:

* Mention `@Port` in any channel it's invited to.
* Start interacting with Port directly from Slack.

### Slash commands[â](#slash-commands "Direct link to Slash commands")

The Slack app responds to the `/port` slash command with these options:

* `/port` (or `/port help`) - Shows general help and available actions.

To ask the app a question, simply mention `@Port` and ask away, for example:

```
@Port is there an active incident for the service 'x'?
```

### Use the Slack AI assistant interface[â](#use-the-slack-ai-assistant-interface "Direct link to Use the Slack AI assistant interface")

On paid Slack workspaces, you can also interact with Port through Slack's AI assistant interface, which provides enhanced features:

1. Chat history for previous interactions with Port is available when using direct messages with the app.

   ![Slack app chat history with Port](/img/ai-agents/SlackAppAgentChat.png)

2. You can start a new conversation easily using the "New Chat" button in the top-right corner.

3. For quicker access, add Port to your Slack top bar by clicking the three dots menu and selecting "Add assistant to top bar".

   ![Adding Port to Slack top bar](/img/ai-agents/SlackAppAddTopBar.png)

4. Once added, you can access Port from anywhere in Slack through a side panel, without leaving your current conversation.

   ![Interacting with Port through Slack side panel](/img/ai-agents/SlackAppAgentInteraction.png)

This provides a more seamless way to interact with your Port AI capabilities while working in Slack.

## Advanced configuration[â](#advanced-configuration "Direct link to Advanced configuration")

### Renaming the Slack Bot[â](#renaming-the-slack-bot "Direct link to Renaming the Slack Bot")

You can rename the Port Slack bot in your workspace. This can be useful if you want the bot to have a name that is more recognizable to your organization, instead of the default "Port".

Follow these steps to rename the bot:

1. In your Slack workspace, find the Port app. Right-click on it and select "View app details".

   ![View Port App Details in Slack](/img/ai-agents/SlackAppViewAppDetails.png)

2. In the app details view, click on the "Configuration" tab. This will open a new page in your web browser. Scroll down to the "Bot User" section.

   ![Slack App Configuration Page - Bot User Section](/img/ai-agents/SlackAppEditBot.png)

3. Click on the "Edit" button next to the bot user. In the modal that appears, enter the new desired name for your bot and click "Save Changes". The change will apply immediately.

   ![Edit Bot Name Modal in Slack](/img/ai-agents/SlackAppEditBotModal.png)

## Limitations[â](#limitations "Direct link to Limitations")

* The Slack app can only operate in channels it's invited to and in private DMs with the bot.

* Users must authenticate individually.

* You can install only one Slack app, related to one Port organization, in each Slack workspace.

* When sending a message from Port to Slack, up to 50 `blocks` can be used, and each `text` value can be up to 3000 characters long.
