# Source: https://docs.envzero.com/guides/integrations/notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Notifications

> Configure env zero deployment notifications for Slack, Email, Microsoft Teams, and webhooks

env zero can send notifications for deployment events to your Slack, Email or Microsoft Teams workspace.\
You can define several Notification Targets, corresponding to different channels.\
You can also associate these Notification Targets to different env zero projects, controlling which events go to which channel.

To Configure your notification please follow the [Slack](/guides/integrations/notifications/slack), [Microsoft Teams integration](/guides/integrations/notifications/microsoft-teams) or [Webhooks](/guides/integrations/notifications/webhooks), and afterward, follow the steps below 👇

## Configuring Notifications

### Add a Notification Target

🔒 Only organization Admins can set up new Notification Targets.

1. Navigate to your **Organization Settings**, and open the **Notifications** tab
2. Click on **Add Notification Target**
3. Enter any name you'd like, chose the **Slack**, **Microsoft Teams** or **Email** type, and enter the Email Addresses or Webhook URL you saved earlier under **Webhook URL**
4. Click **Add Notification Target** to save

### Configure your project to send notifications

🔒 Only project Admins can configure project notifications

1. Navigate to your **Project Settings**, and open the **Notifications** tab.
2. Find the **Notification Target** you've previously added and click on the edit icon (✏️) next to it.
3. Select the events you'd like to get notified of, from this project to this notification target.
4. Click Save

Built with [Mintlify](https://mintlify.com).
