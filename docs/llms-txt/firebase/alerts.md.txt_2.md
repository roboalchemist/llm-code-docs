# Source: https://firebase.google.com/docs/crashlytics/alerts.md.txt

Crashlytics offers different alerts and different ways to receive these
alerts.

Firebase can send Crashlytics alerts based on the following event types:

- **New fatal issues** : triggered when your app experiences a crash or ANR
  that Crashlytics hasn't seen before.

- **New non-fatal issues** : triggered when your app experiences a non-fatal
  issue Crashlytics hasn't seen before.

- **Regressed issues**: triggered when your app experiences a crash that you'd
  previously marked closed.

- **Trending issues**: triggered when an issue is emerging or trending.

- **Increasing-velocity issues**: triggered when a single crash or ANR type
  impacts a percentage of users in a 30-minute period for a given app version.

Here are the options for receiving default Crashlytics alerts. Each option
allows progressively more configurability and customization.

- [Alerting by email or in the Firebase console](https://firebase.google.com/docs/crashlytics/alerts#default)

- [Basic alerting integrations with Slack, Jira, and PagerDuty](https://firebase.google.com/docs/crashlytics/alerts#basic-integrations)

- [Advanced alerting to custom notification channels](https://firebase.google.com/docs/crashlytics/alerts#advanced)

> [!NOTE]
> In addition to the above listed "default" Crashlytics alerts sent by Firebase, you can also [set up **custom alerts** using Cloud Monitoring](https://firebase.google.com/docs/crashlytics/alerts-advanced#cloud-monitoring).

## Alerting by email or in the Firebase console

Firebase can send all default Crashlytics alerts to your email.
For *regressed issues* and *increasing-velocity issues* , Firebase can also show
alerts in the Firebase console.

- Alerts for *regressed* and *trending* issues do not require any configuration
  and are ***sent by default*** when you set up Crashlytics.

- Alerts for new *non-fatals* , *fatals* , *ANRs* , and
  *increasing-velocity issues* are ***not sent by default***. To receive these
  alerts, you must (at minimum) select your preferred alerting channel.

All alert types offer some configuration. For example, you can turn alerts on
or off for your own account, and for *increasing-velocity issues* , you can set
thresholds for when alerts are sent. You can view and configure these alerts in
the
[**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts)
in the Firebase console.

[Learn more about alerting by email or in-console](https://firebase.google.com/docs/crashlytics/alerts-default)

## Basic alerting integrations with Slack, Jira, and PagerDuty

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

[Learn more about basic alerting integrations with Slack, Jira, and PagerDuty](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations)

## Advanced alerting to custom notification channels

Firebase offers two options for configuring alerts and sending them to custom
notification channels.

#### *(Recommended)* Set up and send custom alerts using Cloud Monitoring

You can use Cloud Monitoring to send **fully customized alerts** to custom
notification channels based on Crashlytics data and (optionally)
Firebase sessions data that you've exported to Cloud Logging.
For example, if your crash rate exceeds a specific threshold, you can send a
customized message to a specific email address or post it to a third-party
service, like Discord, Slack, or Jira.

[Learn more about setting up and sending custom alerts using Cloud Monitoring](https://firebase.google.com/docs/crashlytics/alerts-advanced#cloud-monitoring)

#### Send default Crashlytics alerts using Cloud Functions

You can use Cloud Functions to send the **default Crashlytics alerts**
(see the list at the top of this page) to custom notification channels.
For example, you can write a function that captures an alert event for velocity
alerts and posts the alert information to a third-party service, like Discord,
Slack, or Jira.

[Learn more about sending Crashlytics alerts using Cloud Functions for Firebase](https://firebase.google.com/docs/crashlytics/alerts-advanced#cloud-functions)