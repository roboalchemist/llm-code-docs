# Source: https://docs.acceldata.io/documentation/notifications-and-notification-groups.md

# Notifications and Notification Groups

The **Notifications** page allows you to set up alert groups and integrate ADOC with your existing communication tools.

**Notification groups** serve the purpose of ensuring that the right alerts reach the right people at the right time. They define **where alerts are sent** (for example, Slack, Teams, or email) and **who should receive them**. By grouping notifications, you can:

- Reduce noise by routing only relevant alerts to each team.
- Prioritize responses by mapping critical alerts to incident-response teams and lower-priority alerts to monitoring channels.
- Ensure accountability by clearly assigning ownership of alerts.

You can also customize groups by **alert type** (for example, compute alerts, pipeline alerts) and **priority level**, so teams know when immediate action is required.

In addition, **notifications** connect ADOC to third-party platforms like ServiceNow and Jira. This provides a **single place to manage alerts across multiple systems**, making it easier for teams to track, act on, and resolve incidents without switching between tools.

Note If you do not see the Notifications section in the Setting page, including Notification Groups and Notification Integrations, make sure your account has the **Viewer** role permission enabled.

## Notification Groups

A Notification Group is a collection of one or more channels (such as Email, Slack, Google Chat, Webhook, or Microsoft Teams) where ADOC sends alerts. Groups make it easier to manage who receives alerts and through which tools.

You can use notification groups when configuring alerts in Compute or Data Reliability (assets and policies).

## Create a Notification Group

1. In ADOC, navigate to **Settings &gt; Notification Channels**.
2. Click **Create Notification Group**.
3. Enter a name in the **Notification Group Name** field.
4. (Optional) In the **Notification Group Description** field, provide a short summary of the group’s function or target audience.
5. Under **Select Notification Template Group**, choose the template set you want this group to use.
    - By default, **System Default Template Group** is selected.
    - You can select a **custom template group** if one has been configured under [Notification Templates](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/notification-templates).

6. Select one or more channels:
    1. **Email**: Enter recipients. You can add CC and BCC addresses. Separate multiple addresses with the Enter key.
    2. **Slack**: Enter the Slack channel URL. [See Notifications via Slack](https://api.slack.com/messaging/webhooks)
    3. **Google Chat**: Enter the Chat channel URL.
    4. **Webhook**: Enter the Webhook URL. You can also integrate Webhooks with ticketing systems. See [Webhook Integration](https://docs.acceldata.io/documentation/notification-group#tab-webhook:webhooks)
    5. **Teams**: Enter the [Microsoft Teams Webhook](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet) URL. See below for setup instructions.
    6. **ServiceNow**
    7. **Jira**

7. Click **Create Group**.

### Configure Microsoft Teams Webhooks

You can add a Teams channel using one of two methods.

#### Method 1: Private Teams Channel

1. Open the Teams channel.
2. Select … (More options) &gt; **Connectors**.
3. Search for **Incoming Webhook** and click **Configure**.
4. Provide a name and click **Create**.
5. Copy the generated **Webhook URL**.
6. In ADOC, navigate to Notification Channels &gt; Teams and paste the URL.
7. Click **Create Channel**.

#### Method 2: Public Teams Channel

1. In Teams, select **Apps** from the left menu.
2. Search for **Incoming Webhook**.
3. Click **Add** to a team and choose the channel.
4. Provide a name and click **Create**.
5. Copy the generated **Webhook URL**.
6. In ADOC, navigate to **Notification Channels** &gt; **Teams** and paste the URL.
7. Click **Create Channel**.

### Configure Slack

To send ADOC alerts to a Slack channel, you need to set up a Webhook in Slack and connect it in ADOC.

**Prerequisite:** You must have access to a Slack workspace and a Slack channel where you want to receive alerts.

Steps

1. In your browser, navigate to **Slack Apps**.
2. Click **Create an App**.
3. In the dialog, select **From Scratch**.
4. Enter a name for your app, choose the workspace, and click **Create App**.
5. On the **Basic Information** page, select **Incoming Webhooks**.
6. **Toggle Activate Incoming Webhooks** to On.
7. Click **Add New Webhook to Workspace**.
8. Choose the Slack channel where alerts should appear, then click **Allow**.
9. Copy the generated **Webhook URL**.
10. In ADOC, navigate to **Settings** &gt; **Notification Channels**.
11. Select **Slack** and paste the **Webhook URL** into the **Slack URL** field.
12. Click **Create Channel**.

Your **Slack Webhook** is now connected. All alerts sent to this notification group will appear in the selected **Slack** channel.

### Configure Webhook

Webhooks in ADOC let you send alerts directly to external systems in real time. By integrating webhooks with tools such as Jira or ServiceNow, you can automatically create tickets and streamline incident management without manual intervention.

Webhooks also support dataplane routing, which allows alerts to be delivered even in restricted network environments.

#### Prerequisites

- ADOC account with admin privileges.
- Access to the Notification Groups section in ADOC.
- An external system such as Jira or ServiceNow that supports webhook integrations.
- (Optional, for restricted networks) An active dataplane and firewall rules updated to allow ADOC communication.

#### Steps to Integrate ADOC Webhooks with Jira

**1. Access Webhook Settings in ADOC**

1. Log in to ADOC.
2. Navigate to **Settings &gt; Notification Groups**.
3. Open the **Webhook** configuration panel.

**2. Create a Webhook in Jira**

1. In **Jira**, navigate to **System Settings &gt; Webhooks**.
2. Click **Create** **a Webhook**.
3. Name the webhook (e.g., ADOC Alerts).
4. In the URL field, paste the ADOC webhook endpoint URL.
5. Save the webhook.

**3. Configure the Webhook in ADOC**

1. In ADOC, click **Add New Webhook**.
2. Enter a name for the webhook.
3. Paste the **Jira Webhook URL**.
4. Select which alerts or events should trigger this webhook.

**4. Customize Alert Data**

1. Add key details like incident ID, summary, and severity. Ensure the data format matches Jira’s ticket creation API.

**5. Test the Integration**

1. Save your settings.
2. Trigger a test alert in ADOC.
3. Confirm that a Jira ticket is created with the correct details.

**6. Monitor and Adjust**

1. Observe alerts for a few days.
2. Update webhook configurations in ADOC or Jira if necessary.

#### Webhook Configuration with Dataplane

In restricted networks (e.g., behind a proxy or firewall), direct incident creation may not be possible. ADOC supports routing webhook requests through a dataplane to ensure alerts still reach external platforms such as ServiceNow or Jira.

**Key Benefits**

- Network compliance: Requests follow approved internal routes.
- Seamless automation: Incidents are still created automatically.
- Flexibility: Headers and routing can be customized per policy.

#### Steps: Configure Webhooks via Dataplane

1. In ADOC, navigate to **Notification Groups &gt; Create Notification Group**.
2. Enter a name and description.
3. Select Webhook as the notification channel.
4. Enter the Webhook URL.
5. Optional Configurations:
    1. Add Headers: Provide key–value pairs (can be edited or removed later).
    2. **Route via Dataplane**:
        1. Check the box to enable routing.
        2. Select a Dataplane Name from the dropdown (powered by the Data Reliability API).

    3. Secret Manager (v4.0.0+):
        1. If a secret manager is selected, any header values marked as secret will be stored securely.
        2. At runtime, ADOC replaces these keys with the actual secret values from the manager.

6. (Optional) To add more webhooks, click **Add Webhook** and repeat the configuration.
7. Click **Save**.

Alerts will now be routed through the dataplane, ensuring compliance and uninterrupted incident creation.

## Best Practices

**1. Use Meaningful Names**

Name notification groups and channels clearly (e.g., Data Reliability Errors - Email, Pipeline Monitoring - Slack). Avoid generic names like Group1 or Default.

**2. Segregate by Purpose**

Create separate groups for critical alerts (e.g., production failures) vs. informational alerts (e.g., success notifications). This helps prevent alert fatigue.

**3. Leverage Multiple Channels**

Add more than one channel per group (e.g., Email + Slack + Webhook). Ensures redundancy if one channel fails.

**4. Minimize Noise**

Do not route all alerts to all users. Assign groups only to the teams responsible (for example, Data Engineering team vs. Infrastructure team).

**5. Keep Auditability in Mind**

Use Email or Webhook channels to maintain a record of important alerts.Helps with post-incident review and compliance tracking.