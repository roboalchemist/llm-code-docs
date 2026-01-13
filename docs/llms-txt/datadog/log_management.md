# Source: https://docs.datadoghq.com/account_management/billing/log_management.md

---
title: Log Management Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > Log Management Billing
source_url: https://docs.datadoghq.com/billing/log_management/index.html
---

# Log Management Billing

## Pricing{% #pricing %}

At the end of the month, Datadog computes the total number of log events that have been indexed:

- If you are below commitment, your bill stays the same.
- If you over-consume, the committed amount is subtracted and **on demand usage** is charged with a 50% premium.

### On demand{% #on-demand %}

With Datadog log management, you define a monthly commitment on indexed log events. However, during troubling times the number of logs can spike and you may go above your commitment. Because it's important to keep visibility on your infrastructure health, you are not limited to your monthly commitment.

Since commitments are monthly, if you over-generate log events for 1 day it may not cause overuse if your average daily log consumption is close to expectations for your commitment.

## Tracking log events{% #tracking-log-events %}

There are several places where you can see the number of log events you have sent to Datadog.

1. On the [Usage page](https://app.datadoghq.com/account/usage/hourly), there is a Month-to-Date and a graph named `Indexed Logs` and which shows the hourly number of indexed log events:

1. On the [Configuration page](https://app.datadoghq.com/logs/pipelines), double-click on an index to see the number of log events that were indexed in the past couple days.

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/billing/log-events02.62a24e4a9773c1b05656dd013bee3ba2.png?auto=format"
      alt="Log Events" /%}

1. In the [Log Explorer](https://app.datadoghq.com/logs), change the time-frame and check the count at the top of the list:

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/billing/log-events03.abc4bca18d11a15d58a48c47009a5734.png?auto=format"
      alt="Log Events" /%}

You can also use facets to see log count by any attribute or tag defined by your log events. This helps to identify which host, service, endpoint, etc., generate the most data.

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.
