# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/alerts_mg/alerts-send.md

# Send Alerts

## Overview

Get instant notifications on the sending metrics that matter most, configured specifically for your unique business needs and assets. Route these alerts to the channels your team relies on. Stay on top of sending performance without the need to manually monitor.

Info
Alerts are configured by region (Mailgun [US](https://app.mailgun.com/settings/optimize/alerts) or Mailgun [EU](https://app.eu.mailgun.com/settings/optimize/alerts)). Alerts can operate on both regions concurrently, but for each region, you will need to perform the steps configuring notification channels and setting up alerts

### How Send Alerts Work

Alerts trigger when the metric break the threshold you set. To keep things simple, we use 1 hour periods to measure your metrics used in alert analysis. The alert will indicate the specific dimension that has broken the alert threshold (e.g. sending domain, IP pool, or subaccount).

An alert will trigger once when the threshold is broken. Should the metric go back under threshold and then breach in the next calculated period, another alert will trigger.

Alerts are independent for each filter so if an alert is tracking your sending domains and two sending domains breach threshold you will receive two separate alerts indicating the domains that have broken your alert threshold.

## Metrics, Rates, and Filters

### Metrics to Track

- Complaint rate
- Delivery rate
- Hard bounce rate
- Temporary fail rate


### Thresholds and Filters

Set conditions for the metrics your business cares about. Customize the threshold rate that makes the most sense for your use case and implement up to 10 filters to get really tactical on what you want Mailgun to monitor and alert. To get started easily, our default threshold rates are presented in the UI setup based on feedback from our won deliverability experts.

### Filters

- Sending Domains
- Dedicated IPs
- IP Pools
- Subaccounts: Track Primary and all subaccounts, any subaccount, or specific subaccounts.
- Mailbox Providers