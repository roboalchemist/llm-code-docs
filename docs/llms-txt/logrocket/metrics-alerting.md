# Source: https://docs.logrocket.com/docs/metrics-alerting.md

# Alerting on Timeseries

Alerts on [Timeseries](https://docs.logrocket.com/docs/timeseries-1) charts allow you to trigger notifications when the value of one of your timeseries charts exceeds or drops below a threshold that you have configured. You can create up to 100 alerts and distribute them across any combination of your timeseries charts. You can add alerting to any timeseries chart type except for "Total Events."

<Image align="center" border={true} src="https://files.readme.io/eac2ab0ff67d4383f27e0324bbc540ee9976e498d2b10e9279abd126d8c042f3-Alerting_on_Timeseries.png" className="border" />

## Configuring an alert

Alerts are configured when creating or editing a chart. Currently, alerts are only supported for [Timeseries charts](https://docs.logrocket.com/docs/timeseries-1).

Each alert associated with a chart can have a different type, destination, and a rule that triggers it. LogRocket supports four types of alerts:

## 1. Email alerts

Email alerts will send a message to an email address when an alert is triggered or resolved. You can use these alerts to notify a single user, or a distribution list within your organization. Emails are sent from *[alerts@logrocket.com](mailto:alerts@logrocket.com)*.

## 2. PagerDuty alerts

LogRocket’s timeseries alerts can be used to trigger and resolve incidents in PagerDuty.

For full details, view the [PagerDuty integration](https://docs.logrocket.com/docs/pagerduty) page and follow the in-app instructions.  You will need to enable this via the Integrations page before the option appears within the timeseries alert dropdown.

## 3. Slack alerts

The Slack alert type will deliver a rich message to Slack. Configure an [incoming webhook integration](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) in Slack, and paste that URL generated for that integration into the alert’s target URL.

## 4. Webhook alerts

Webhook alerts allow you to deliver an information payload to an arbitrary URL when an alert is triggered or resolved. The webhook payload contains the following fields:

| Field                           | Type    | Description                                                                                                                                                                       |
| :------------------------------ | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`                        | string  | `"triggered"` or `"resolved"`                                                                                                                                                     |
| `alert_id`                      | string  | A unique ID for an alert. This ID remains the same between multiple triggerings and resolutions of the same alert. Thus, it can be used to track the state of an alert over time. |
| `project_url`                   | url     | A link to the LogRocket project                                                                                                                                                   |
| `dashboard_url`                 | url     | A link to the dashboard containing the chart where this timeseries chart is defined                                                                                               |
| `metric_url`                    | url     | A link to the chart describing this timeseries                                                                                                                                    |
| `reason`                        | string  | A human-readable description of the alert definition (based on the values in the `alert_settings` object)                                                                         |
| `alert_settings.threshold`      | integer | The timeseries chart threshold defined for the alert                                                                                                                              |
| `alert_settings.operator`       | string  | `"LT"` (less than) or `"GT"` (greater than)                                                                                                                                       |
| `alert_settings.threshold_unit` | string  | The unit of evaluation for the timeseries chart                                                                                                                                   |
| `alert_settings.interval`       | string  | The time interval to evaluate the timeseries chart over                                                                                                                           |
| `alert_settings.interval_unit`  | string  | The unit of the time interval: `"MINUTES"` or `"HOURS"`                                                                                                                           |

<br />

## Alerts Dashboard

You can view and manage all of your Metric Alerts from across all of your charts on our Alerts Dashboard, available within the 'Alerts' tab in Settings:

<Image align="center" src="https://files.readme.io/1c458b607cbde47c393cedd037c707cf25930c1dcd8a4d5ff206fa9d37a04700-Screenshot_2026-03-10_at_2.24.04_PM.png" />

Note that you can also view your [Issues alerts](https://docs.logrocket.com/docs/issues-alerts) here.