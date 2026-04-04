# Source: https://firebase.google.com/docs/crashlytics/alerts-basic-integrations.md.txt

Firebase can send a variety of default Crashlytics alerts (see the
[alerting overview page](https://firebase.google.com/docs/crashlytics/alerts)).
Firebase offers basic alerting integrations to send the default Crashlytics
alerts to Slack, Jira, and PagerDuty.

At a high-level, here's how to set up and configure these integrations in the
Firebase console:

1. Follow the guided workflow for each service in the
   [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/)
   in your
   **Project settings**.

2. Select which configuration is used for individual apps and configure the
   destination of other alerts on the Crashlytics card of the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts)
   in your
   **Project settings**.

> [!NOTE]
> **Note:** If you want more control and customization for setting up and sending alerts to *any* third-party service (not limited to only Slack, Jira, or PagerDuty), check out the options in [Set up advanced alerting to custom notification channels](https://firebase.google.com/docs/crashlytics/alerts-advanced). You can even set up fully customized alerts beyond the default Crashlytics alerts.

<br />

The rest of this page describes in detail how to set up each basic
alerting integration.

[Slack](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#slack)
[Jira](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#jira)
[PagerDuty](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#pagerduty)

<br />

*** ** * ** ***

## **Slack**: Set up integration with Slack

![Example of a Crashlytics alert to a Slack channel](https://firebase.google.com/static/docs/crashlytics/images/crashlytics-slack-alert-example.png)

After setting up the Firebase integration with Slack, your project can post to
your Slack workspace in response to events reported by Crashlytics, like
new, regressed, or increasing-velocity issues.

### **Step 1**: Set up a Slack webhook

Before you set up the integration in Firebase, you need to add an incoming
webhook in Slack to handle communications from Firebase.

To learn how to do this, read the Slack documentation about
[Sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks).

### **Step 2** : Set up the Slack integration in the Firebase console

After you've set up the appropriate webhook, you're ready to set up the
integration for Crashlytics:

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Integrations** tab](https://console.firebase.google.com/u/0/project/_/settings/integrations).

4. On the **Slack** integration card, click **Install**.

5. Set up the integration by setting values in the following fields:

   - **Webhook URL**: Paste the webhook URL from your Slack settings page.

   - **Default channel**: Enter a channel name. You can override this default
     later on a per-app or per-alert basis.

   - **Name of posting user**: Enter a name to send the messages under.

6. Click **Verify \& save**.

After verifying and saving the Slack integration, you should see a confirmation
message in the default channel you selected.

### **Step 3**: Configure alert settings for Slack

You can configure alerts by app and event type. For example, you can turn off
alerts in your testing app or route high-priority alerts in your production app
to an `#urgent` channel.

#### Event types

The Firebase integration with Slack lets you send alerts in response to the
following event types:

- **New fatal issues** : triggered when your app experiences a crash or ANR
  that Crashlytics hasn't seen before.

- **New non-fatal issues** : triggered when your app experiences a non-fatal
  issue Crashlytics hasn't seen before.

- **Regressed issues**: triggered when your app experiences a crash that you'd
  previously marked closed.

- **Trending issues**: triggered when an issue is emerging or trending.

- **Increasing-velocity issues**: triggered when a single crash or ANR type
  impacts a percentage of users in a 30-minute period for a given app version.

#### Configure settings for each app

> [!NOTE]
> **Note:** By default, the Firebase integration with Slack ***automatically*** sends alerts for *regressed issues* and *increasing-velocity issues* to your specified Slack channels.

Here's how to configure alerts for each app in your Firebase project:

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

4. Go to the **Crashlytics** alerts card. Select the app you want to
   configure from the drop-down menu.

5. Select the Slack channel where you want to send alerts for this app.

6. For each type of alert, select from the drop-down whether you want to send
   that type of alert to Slack.

7. Repeat these steps for each app that you want to configure.

That's it! Firebase will send alerts to your specified Slack channels if your
apps have new, regressed, or increasing-velocity issues.

<br />

*** ** * ** ***

## **Jira**: Set up integration with Jira

After setting up the Firebase integration with Jira, your Firebase project can
post to a Jira project in response to events reported by Crashlytics, like
new, regressed, or increasing-velocity issues. You can also link individual
Crashlytics issues to Jira issues.

### **Step 1**: Prepare Jira for integration with Firebase

> [!NOTE]
> **Note:** This Firebase integration supports *Jira Software Cloud* (both Cloud and Server) but ***not*** Jira *on-premise* implementations.

#### Create an API token (Jira Cloud only)

Before you set up the integration in Firebase, you need to generate an API token
in Jira Cloud.

1. In the Jira console, open the
   [API tokens settings](https://id.atlassian.com/manage/api-tokens).

2. Click **Create API token**.

3. Save this API token somewhere secure, as you'll need it later.

#### Create a "Bug" issue type

The Firebase integration with Jira creates issues with the type `Bug`. You
need to create this issue type in your Jira project (if it doesn't already
exist).

1. In the Jira console, navigate to **Project Settings**.

2. Click **Issue types**.

3. Click **Add issue type**.

4. Select "Bug", or enter it manually.

### **Step 2** : Set up the Jira integration in the Firebase console

Set up your Jira integration for *Jira Cloud* or for *Jira Server*.

#### Jira Cloud

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Integrations** tab](https://console.firebase.google.com/u/0/project/_/settings/integrations).

4. On the **Jira** integration card, click **Install**.

5. Click **Set up Jira integration**.

6. Enter your Jira project URL in the following format:
   `https://WORKSPACE_NAME.atlassian.net/projects/PROJECT_KEY`

7. Enter your Jira login email and your API token.

8. Click **Verify \& save**.

#### Jira Server

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Integrations** tab](https://console.firebase.google.com/u/0/project/_/settings/integrations).

4. On the **Jira** integration card, click **Install**.

5. Click **Set up Jira integration**.

6. Enter your Jira project URL in the following format:
   `https://SERVER_NAME.com/projects/PROJECT_KEY`

7. Enter your Jira login email and your API token.

8. Click **Verify \& save**.

> [!TIP]
> **Tip:** For more information on how to get your Jira project key, visit the [Jira Core Support site](https://confluence.atlassian.com/jiracorecloud/editing-a-project-s-details-938021482.html).

### **Step 3**: Configure alert settings for Jira

You can configure alerts by app and event type. For example, you can turn off
alerts in your testing app or route alerts about different apps to different
Jira projects.

#### Event types

The Firebase integration with Jira lets you send alerts in response to the
following event types:

- **New fatal issues** : triggered when your app experiences a crash or ANR
  that Crashlytics hasn't seen before.

- **New non-fatal issues** : triggered when your app experiences a non-fatal
  issue Crashlytics hasn't seen before.

- **Regressed issues**: triggered when your app experiences a crash that you'd
  previously marked closed.

- **Trending issues**: triggered when an issue is emerging or trending.

- **Increasing-velocity issues**: triggered when a single crash or ANR type
  impacts a percentage of users in a 30-minute period for a given app version.

#### Configure settings for each app

> [!NOTE]
> **Note:** By default, the Firebase integration with Jira does ***not*** post any kind of alert to your specified Jira projects.

Here's how to configure alerts for each app in your Firebase project:

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

4. Go to the **Crashlytics** alerts card. Select the app you want to
   configure from the drop-down menu.

5. Select the Jira project where you want to send alerts for this app.

6. For each type of alert, select from the drop-down whether you want to send
   that type of alert to Jira.

7. Repeat these steps for each app that you want to configure.

That's it! Firebase will send alerts to your specified Jira projects if your
apps have new, regressed, or increasing-velocity issues.

### *(Optional)* Link Crashlytics issues and Jira issues

In addition to the automatically-created Jira issues that Firebase creates, it's
possible to link your Crashlytics issues to existing Jira issues. You can
also create a new Jira issue from the Firebase console. You'll need to enable
the Jira integration before using this feature.

1. Navigate to the Crashlytics issue you'd like to link to a Jira issue.

2. Click **Link to Jira**.

3. Either click **Create issue in Project**, or paste your Jira issue URL or
   issue key in the provided field.

#### Unlink a Crashlytics issue from a Jira issue

1. Navigate to the Crashlytics issue you'd like to unlink from Jira.

2. Click **Linked Issue**.

3. Click **More** , and select **Unlink**.

<br />

*** ** * ** ***

## **PagerDuty**: Set up integration with PagerDuty

After setting up the Firebase integration with PagerDuty, your Firebase project
lets PagerDuty page your on-call responders in response to events reported by
Crashlytics, like new, regressed, or increasing-velocity issues.

### **Step 1** : Set up the PagerDuty integration in the Firebase console

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Integrations** tab](https://console.firebase.google.com/u/0/project/_/settings/integrations).

4. On the **PagerDuty** integration card, click **Install**.

5. Follow the on-screen instructions to set up the integration.

6. Click **Verify \& save**.

### **Step 2**: Configure alert settings for PagerDuty

You can configure alerts by app and event type. For example, you can turn off
alerts in your testing app or route alerts about different apps to different
PagerDuty projects.

#### Event types

The Firebase integration with PagerDuty lets you send alerts in response to the
following event types:

- **New fatal issues** : triggered when your app experiences a crash or ANR
  that Crashlytics hasn't seen before.

- **New non-fatal issues** : triggered when your app experiences a non-fatal
  issue Crashlytics hasn't seen before.

- **Regressed issues**: triggered when your app experiences a crash that you'd
  previously marked closed.

- **Trending issues**: triggered when an issue is emerging or trending.

- **Increasing-velocity issues**: triggered when a single crash or ANR type
  impacts a percentage of users in a 30-minute period for a given app version.

#### Configure settings for each app

> [!NOTE]
> **Note:** By default, the Firebase integration with PagerDuty ***automatically*** sends alerts for *regressed issues* and *increasing-velocity issues* to your specified PagerDuty services.

Here's how to configure alerts for each app in your Firebase project:

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

4. Go to the **Crashlytics** alerts card. Select the app you want to
   configure from the drop-down menu.

5. Select the PagerDuty service where you want to send alerts for this app.

6. For each type of alert, select from the drop-down whether you want to send
   that type of alert to PagerDuty.

7. Repeat these steps for each app that you want to configure.

That's it! Firebase will post bugs to your specified PagerDuty service if your
apps have new, regressed, or increasing-velocity issues.