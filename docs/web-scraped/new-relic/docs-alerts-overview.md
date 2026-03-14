# Source: https://docs.newrelic.com/docs/alerts/overview/

Title: Introduction to alerts

URL Source: https://docs.newrelic.com/docs/alerts/overview/

Markdown Content:
New Relic is a flexible system that allows you to get informed about issues for any entity or stream of telemetry data. You define the data to watch, the thresholds that if exceeded mean an issue, who is notified, and how. Alerts empower your team with dynamic tools to proactively detect and address potential problems. By pinpointing unusual activity, linking related issues, and aiding in root cause analysis, alerts enable swift action to keep your systems running smoothly.

New Relic's alerts help you to know what's critical, manage the suppressed noise, and mitigate alert fatigue.

With alerts, you can:

*   Configure any signal to be evaluated against a [threshold](https://docs.newrelic.com/docs/new-relic-solutions/get-started/glossary/#alert-threshold), or if it exhibits abnormal behavior.
*   Organize alerts through [tagging](https://docs.newrelic.com/docs/new-relic-solutions/new-relic-one/core-concepts/use-tags-help-organize-find-your-data/#query-tags).
*   Identify [anomalies](https://docs.newrelic.com/docs/alerts-applied-intelligence/applied-intelligence/anomaly-detection/anomaly-detection-applied-intelligence/) before they become broader issues.
*   Route issues to the correct system or team using [notifications](https://docs.newrelic.com/docs/alerts-applied-intelligence/notifications/intro-notifications/).
*   Enable the [Predictive capability](https://docs.newrelic.com/docs/alerts/create-alert/set-thresholds/predictive-alerts/) to anticipate and respond proactively to possible threshold breaches in the future. (Available with the public preview of Predictive Alerts).

New Relic alerts allow you to:

*   [Enrich](https://docs.newrelic.com/docs/alerts/get-notified/alert-event-workflows/#enrichments) your issue's notifications with additional New Relic data.
*   Normalize your data, group related alert events, and establish relationships between them.
*   [Correlate](https://docs.newrelic.com/docs/alerts/organize-alerts/change-applied-intelligence-correlation-logic-decisions/#what-is-correlaton) incoming alert events.
*   Provide a [root cause analysis](https://docs.newrelic.com/docs/alerts/alert-event-management/Issues-and-alert-event-management-and-response/#root-cause-analysis).
*   Reduce and [suppress noisy alerts](https://docs.newrelic.com/docs/alerts/organize-alerts/change-applied-intelligence-correlation-logic-decisions/#configure-correlation).

[![Image 1: Alerts main page](https://docs.newrelic.com/images/alerts_screenshot-full_alerts-and-ai-overview-page.webp)](https://docs.newrelic.com/images/alerts_screenshot-full_alerts-and-ai-overview-page.webp)

To open view your alerts, go to **[one.newrelic.com](https://one.newrelic.com/all-capabilities)> Alerts**.

There are some steps you need to take in order to set up an alert condition and receive notifications. Check out our [tutorial series](https://docs.newrelic.com/docs/tutorial-create-alerts/create-new-relic-alerts/) for all steps you need to get started.

Want to get started making your first alert? See how to [create your first alert](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/get-started/your-first-nrql-condition/).

Alerting concepts and terms
---------------------------

An alert event is generated when an active alert condition's threshold has been met. You can correlate similar or related alert events to an issue and group alert conditions together to create an alert policy.

You can configure notifications through Workflows to inform you about the triggering of alert conditions. These notifications include the option of sending them to various channels to reach the right group of people and help them triage the issue.

To get the most of alerting, it's essential to understand some basic terms and concepts.

This diagram shows how alerts work: you create an alert policy that includes an alert condition or several alert conditions. Alert conditions include a defined threshold and when that threshold is breached, an alert event triggers. If you've configured a workflow, then you'll receive a notification. You can group alert events into issues and issues into decisions to have better management of your alerts.

[![Image 2: A diagram showing some basic concepts and terms for New Relic alerting](https://docs.newrelic.com/images/accounts_diagram_alerting-concepts.webp)](https://docs.newrelic.com/images/accounts_diagram_alerting-concepts.webp)

| Term | Explanation |
| --- | --- |
| **[Condition](https://docs.newrelic.com/docs/alerts/create-alert/create-alert-condition/alert-conditions/#create-alert-condition/)** | Configuration of one or more thresholds applied to a signal. An alert event is created when the thresholds are breached. |
| **[Decision](https://docs.newrelic.com/docs/alerts-applied-intelligence/applied-intelligence/incident-intelligence/change-applied-intelligence-correlation-logic-decisions/)** | Logical operation that group alert events into larger issues. There are built-in decisions and you can also create your own custom decisions. |
| **[Destination](https://docs.newrelic.com/docs/alerts-applied-intelligence/notifications/destinations/)** | Service by which you get notified. It's a unique identifier for a third-party system that you use. |
| **[Event](https://docs.newrelic.com/docs/data-apis/understand-data/new-relic-data-types/#events-new-relic)** | Indicate a state change or trigger defined by your New Relic alerts conditions or external monitoring systems. An event contains information about the affected entity. |
| **[Alert event](https://docs.newrelic.com/docs/alerts/alert-event-management/view-alert-event-details/)** | Event generated when a condition threshold is breached. It's an individual event that details a symptom of a problem. |
| **[Issue](https://docs.newrelic.com/docs/new-relic-solutions/get-started/glossary/#issue)** | Collection of one or more alert events that requires attention and investigation and causes a notification. |
| **[Notification](https://docs.newrelic.com/docs/alerts-applied-intelligence/notifications/intro-notifications/)** | Message that you receive when an alert event opens, is acknowledged, or closes. |
| **[Policy](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/alert-policies/create-edit-or-find-alert-policy/)** | Group of alert conditions that you configure to get notified when an alert event occurs. |
| **[Threshold](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/advanced-alerts/advanced-techniques/set-thresholds-alert-condition/)** | Value that a data source must pass to trigger an alert event and the time-related settings that define an alert event. |
| **[Workflow](https://docs.newrelic.com/docs/alerts/get-notified/alert-event-workflows/)** | Definition of when and where you want to receive notifications about issues. You can enrich your notifications with additional and related New Relic data. |

Ready to try New Relic for yourself? [Sign up for your free New Relic account](https://newrelic.com/signup) and follow our [quick launch guide](https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/#get-started) so you can start maximizing your data today! If you need any help, check out our [tutorial series](https://docs.newrelic.com/docs/tutorial-create-alerts/create-new-relic-alerts/) on creating alerts to get started.
