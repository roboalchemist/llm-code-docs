# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules.md

---
title: Custom Detection Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Detect and Monitor > Custom Detection
  Rules
---

# Custom Detection Rules

## Overview{% #overview %}

Out-of-the-box detection rules help you cover the majority of threat scenarios, but you can also create custom detection rules for your specific use cases. See [Create Rule](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/real_time_rule/) for instructions on how to create a custom rule.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/custom_detection_rules_ui.e91bb5f573b43cf98418922fa60802cf.png?auto=format"
   alt="The create a rule page showing the detection types and methods you can create" /%}

## Rule types{% #rule-types %}

You can create the following types of custom detection rules:

- Real-time rule: Continuously monitors and analyzes incoming logs.
- Scheduled rule: Runs at pre-scheduled intervals to analyze log data.
- Historical job: Backtest detections by running detections against historical logs.

## Detection methods{% #detection-methods %}

The following detection methods are available when you create a custom detection rule or historical job:

- Threshold: Detects when events exceed a user-defined threshold.
- New value: Detects when an attributes changes to a brand new value.
- Anomaly: Detects when a behavior deviates from its historical baseline.
- [Content anomaly](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/content_anomaly/): Detects when an event's content is an anomaly compared to the historical baseline
- [Impossible travel](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/impossible_travel/): Detects if impossible speed is detected in user activity logs.
- Third party: Maps third-party security logs to signals, setting the severity based on log attributes.
- Signal correlation: Combines multiple signals together to generate a new signal so you can alert on more complex use cases and reduce alert fatigue.

## Filter logs based on Reference Tables{% #filter-logs-based-on-reference-tables %}

{% alert level="warning" %}
Reference Tables containing over 1,000,000 rows cannot be used to filter events. See [Add Custom Metadata with Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables/) for more information on how to create and manage Reference Tables.
{% /alert %}

Reference Tables allow you to combine metadata with logs, providing more information to resolve application issues. When you define a query for a rule, you can add a query filter based on a Reference Table to perform lookup queries. For more information on creating and managing this feature, see the [Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables/) guide.

In the following example, a Reference Table containing product information is used to filter and enrich logs:

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/filter-by-reference-table.aba6e4777546fd022262f84f7aa4dde1.png?auto=format"
   alt="The log detection rule query editor with the reference table search options highlighted" /%}

## Unit testing{% #unit-testing %}

Use unit testing to test your rules against sample logs and make sure the detection rule is working as expected. This can be helpful when you are creating a detection rule for an event that hasn't happened yet, so you don't have actual logs for the event. For example: You have logs with a `login_attempt` field and want to detect logs with `login_attempt:failed`, but you only have logs with `login_attempt:success`. To test the rule, you can construct a sample log by copying a log with `login_attempt:success` and changing the `login_attempt` field to `failed`.

## Further Reading{% #further-reading %}

- [Create a custom detection rule](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/real_time_rule/)
- [Configure default Cloud SIEM detection rules](https://docs.datadoghq.com/cloud_siem/default_rules/)
- [Learn about the Security Signals Explorer](https://docs.datadoghq.com/cloud_siem/explorer/)
- [Detect unauthorized third parties in your AWS account](https://www.datadoghq.com/blog/detect-unauthorized-third-parties-aws/)
- [Detect security threats with anomaly detection rules](https://www.datadoghq.com/blog/anomaly-detection-rules-datadog/)
- [Learn more about Security notification variables](https://docs.datadoghq.com/security/notifications/variables/)
- [Monitor Cloudflare Zero Trust with Datadog Cloud SIEM](https://www.datadoghq.com/blog/monitor-cloudflare-zero-trust/)
- [Monitor 1Password with Datadog Cloud SIEM](https://www.datadoghq.com/blog/monitor-1password-datadog-cloud-siem/)
- [Detect anomalies beyond spikes and new values with Content Anomaly Detection in Cloud SIEM](https://www.datadoghq.com/blog/content-anomaly-detection-cloud-siem/)
