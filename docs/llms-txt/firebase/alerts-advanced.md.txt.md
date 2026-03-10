# Source: https://firebase.google.com/docs/crashlytics/alerts-advanced.md.txt

<br />

Firebase offers two options for configuring alerts and sending them to custom
notification channels.

- ***(Recommended)* [Set up and send custom alerts to custom notification channels](https://firebase.google.com/docs/crashlytics/alerts-advanced#cloud-monitoring)**

  You can use Cloud Monitoring to send **fully customized alerts** to custom
  notification channels based on Crashlytics data and (optionally)
  Firebase sessions data that you've exported to Cloud Logging.
- **[Send default Crashlytics alerts to custom notification channels](https://firebase.google.com/docs/crashlytics/alerts-advanced#cloud-functions)**

  You can use Cloud Functions to send the **default Crashlytics alerts**
  to custom notification channels.

<br />

*** ** * ** ***

## *(Recommended)* Set up and send custom alerts to custom notification channels

Firebase offers default Crashlytics alerts (see the
[alerting overview page](https://firebase.google.com/docs/crashlytics/alerts)).
However, these default alerts and their notification channels may not be
sufficient for your needs.

In these cases, you can use Cloud Monitoring to send
**custom alerts to custom notification channels** based on Crashlytics data
(and optionally Firebase sessions data) that you've exported to
Cloud Logging.

To use Cloud Monitoring for custom alerts, you set up an *alerting policy*,
which describes the circumstances under which you want to be alerted and how you
want to be notified.

For example, if your crash-free rate goes below a specific threshold,
Cloud Monitoring can send a customized alert message to a specific email
address or post it to a third-party service, like Discord, Slack, or Jira.
You can also fully customize the information sent in the alert, like including
helpful deep-links into the Firebase console or company-specific
troubleshooting information.

In the Google Cloud documentation, learn more about
[Cloud Monitoring and alerts](https://docs.cloud.google.com/monitoring/alerts),
including
[pricing](https://docs.cloud.google.com/monitoring/alerts#pricing).

### Prerequisites

1. Make sure your Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).

2. [Set up export to Cloud Logging of Crashlytics data and (optionally) Firebase sessions data.](https://firebase.google.com/docs/crashlytics/cloud-logging-export)

3. [Set up notification channels.](https://docs.cloud.google.com/monitoring/support/notification-options)

### Set up an alerting policy

The following are high-level instructions; for detailed instructions, see the
Google Cloud documentation (for example:
[Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)
or
[Use PromQL to create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-promql)).

As part of running queries, you can set up either a log-based alert or a
SQL-based alert:

- **Set up a log-based alert:**

  1. Run a query in
     [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  2. Click the **Add alert** button that appears.

  3. Follow the on-screen instructions to add a log-based alert.

- **Set up a SQL-based alert:**

  1. Run a query in
     [Logs Analytics](https://docs.cloud.google.com/logging/docs/log-analytics#analytics).

  2. Click the **Add alert** button that appears.

  3. Follow the on-screen instructions to add a SQL-based alert.

Alternatively, you can set up alerts for your
[log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-work-with-data#use-logs-based-metrics)
by using the
[policy configuration tool](https://console.cloud.google.com/monitoring/alerting/policies/create)
in the Google Cloud console, where you can choose one of the following options:

- **Builder**:
  The console UI provides a guided workflow to build the alerting policy.

- **PromQL**:
  You provide a PromQL query for your alerting policy

  <br />

  Example PromQL query

  <br />

  For example, say that you've created two log-based metrics for your
  exported Crashlytics and Firebase sessions data:
  - One metric named `firebase/crashlytics_events`
    with a label of `errorType`,
    and it's defined as:

    `logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"`
  - Another metric named `firebase/session_events`
    with a label of `eventType`,
    and it's defined as:

    `logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fsession_events"`

  Here's an example PromQL query using these log-based metrics to alert when
  your crash-free drops below 70%:

  ```
  1 - (sum by (project_id) (rate({__name__="logging.googleapis.com/user/firebase/crashlytics_events", errorType="FATAL"}[5m])) /
  sum by (project_id) (rate({__name__="logging.googleapis.com/user/firebase/session_events", eventType="SESSION_START"}[5m]))
  ) < 0.7
  ```

  <br />

  <br />

<br />

*** ** * ** ***

## Send default Crashlytics alerts to custom notification channels

Firebase offers default Crashlytics alerts (see the
[list on the alerting options overview page](https://firebase.google.com/docs/crashlytics/alerts)).
However, the information in these default alerts and their notification channels
may not be sufficient for your needs.

In these cases, you can use Cloud Functions for Firebase to send these
**default Crashlytics alerts to custom notification channels**.
For example, you can write a function that captures an alert event for velocity
alerts and posts the alert information to a third-party service, like Discord,
Slack, or Jira.

With this advanced alerting mechanism, you can also customize the information
sent to the third-party service. For example, in addition to the default
information provided by Firebase, you can also include helpful deep-links into
the Firebase console or company-specific troubleshooting information.

> [!NOTE]
> **Note:** To use advanced alerting capabilities, your Firebase project needs to use the [Blaze pricing plan](https://firebase.google.com/pricing).

To set up advanced alerting capabilities using Cloud Functions for Firebase, follow these steps:

1. [Set up Cloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started),
   which includes the following tasks:

   1. Set up a development environment for Node.js or Python.
   2. Install and sign into the Firebase CLI.
   3. Initialize Cloud Functions for Firebase using the Firebase CLI.
2. [Write and deploy a function](https://firebase.google.com/docs/functions/alert-events) that
   captures an alert event from Crashlytics and handles the event
   payload (for example, posts the alert information in a message on Discord).

To learn about all the Crashlytics alert events that you can capture, go to
the reference documentation for
[Crashlytics alerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics).

Learn more about
[handling Crashlytics alerts using Cloud Functions for Firebase](https://firebase.google.com/docs/functions/alert-events)