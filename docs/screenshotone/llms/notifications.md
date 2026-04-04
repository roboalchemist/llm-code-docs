# Source: https://screenshotone.com/docs/notifications/

# Notifications

When you reach 90% or 100% of your screenshot limit, you will receive a notification to your email and/or Slack.

## Email

By default, you will receive an email notification when you reach 90% or 100% of your screenshot limit. You can disable these notifications in the [dashboard](https://dash.screenshotone.com/notifications), but they are enabled by default:

![Email notifications](./notifications.png)

## Slack

You can also enable Slack notifications in the [dashboard](https://dash.screenshotone.com/notifications), in addition to the email notifications.

To enable Slack notifications, you need to specify a Slack webhook URL in the [dashboard](https://dash.screenshotone.com/notifications):

![Slack notifications](./slack-webhook-url-input.png)

To configure a Slack webhook URL, you need to create a new webhook in your Slack workspace.

### 1. Create a Slack application

[Create a new Slack application](https://api.slack.com/apps/new).

![Create a Slack application](./1-create-slack-app.png)

### 2. Enable incoming webhooks

Go to [your application settings](https://api.slack.com/apps) and enable incoming webhooks:

![Enable incoming webhooks](./2-enable-incoming-webhooks.png)

### 3. Add new webhook to your workspace

Click on the "Add New Webhook to Workspace" button:

![Add new webhook](./3-add-new-webhook-to-workspace.png)

And then choose the target channel:

![Incoming webhook channel](./3-incoming-webhook-channel.png)

### 4. Copy the webhook URL

![Copy webhook URL](./4-copy-webhook-url.png)

In this example, the webhook URL is:

```
https://hooks.slack.com/services/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
```

### 5. Save and test the webhook URL

Paste the webhook URL in the [dashboard](https://dash.screenshotone.com/notifications):

![Paste webhook URL](./5-paste-webhook-url.png)

And check the integration test message in the target channel:

![Integration test message](./6-check-integration-message.png)

### 6. Get notifications when you reach limits

Once you reach your limit, you will receive a notification in the target channel like this or similar:

![Limit example message](7-limit-example-message.png)

## Summary

These are the most important notifications you need to recieve from ScreenshotOne. If you have more ideas or issues with configuring or receiving notifications, please, reach out to us via `support@screenshotone.com`.