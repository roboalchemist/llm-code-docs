# Source: https://docs.datadoghq.com/security/cloud_siem/guide/monitor-authentication-logs-for-security-threats.md

---
title: Monitor Authentication Logs for Security Threats
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Cloud SIEM Guides > Monitor
  Authentication Logs for Security Threats
---

# Monitor Authentication Logs for Security Threats

## Overview{% #overview %}

Being able to log, monitor, and analyze all authentication events is key for identifying security threats and managing customer records for compliance purposes. Authentication logs from different sources and parts of your environment might have different formats and be managed by different teams or implemented using multiple third-party services.

This guide walks you through best practices and tips for managing and formatting authentication logs so you can use authentication log data to monitor and detect security threats with [Datadog Security and Compliance Monitoring](https://docs.datadoghq.com/cloud_siem/).

## Prerequisites{% #prerequisites %}

Log collection must be enabled to use Security and Compliance Monitoring. This guide recommends log collection enabled at the [application level](https://docs.datadoghq.com/logs/log_collection/?tab=application#application-log-collection).

## Manage and format authentication logs{% #manage-and-format-authentication-logs %}

Before you begin monitoring for security threats, follow the best practices below to ensure you have sufficient log data flowing into Datadog.

### Log events from all login flows{% #log-events-from-all-login-flows %}

To gain visibility into all of your authentication activity, ensure log events for all login flows are at the application level. This eliminates gaps in your monitoring coverage. It also gives you more control over how you log authentication events and what data you are collecting.

### Ensure your logs contain useful data{% #ensure-your-logs-contain-useful-data %}

By logging all authentication events at the application level, you can ensure that your logs contain the most useful data for monitoring and detecting security threats.

```bash
2020-01-01 12:00:01 google oauth login success by John Doe from 1.2.3.4
```

Logs that contain the "who" (John Doe), "what" (login success), and when (2020-01-01 12:00:01) of an event provide the best level of detail for you to perform complex analysis in Datadog.

### Log in a standard, parsable format{% #log-in-a-standard-parsable-format %}

Ensure your application writes logs in a key-value format using `=` as a separator. Using this format means that a key-value parser, such as Datadog's [Grok Parser](https://docs.datadoghq.com/logs/log_configuration/processors/#grok-parser), can process them. For example, if a log is in the following format:

```bash
INFO 2020-01-01 12:00:01 usr.id="John Doe" evt.category=authentication evt.name="google oauth" evt.outcome=success network.client.ip=1.2.3.4
```

Datadog can then parse this as the following JSON:

```json
{
  "usr": {
    "id": "John Doe"
  },
  "evt": {
    "category": "authentication",
    "name": "google oauth",
    "outcome": "success",
  },
  "network": {
    "client": {
      "ip": "1.2.3.4"
    }
  }
}
```

It's important to use a [standard naming convention](https://www.datadoghq.com/blog/logs-standard-attributes/) for the attributes in your logs to ensure that you can search and aggregate data across all attributes, regardless of where they come from. It is recommended that your authentication logs include the following [standard attributes](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention):

- [`usr.id`](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#user-related-attributes)
- [`evt.category`](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#events)
- [`evt.name`](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#events)
- [`evt.outcome`](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#events)
- [`network.client.ip`](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#web-access)

Use the same format across all of your authentication logs so you can properly use log attributes to filter and organize log data in Datadog. For example, with standard attributes you can look for which users (`usr.id`) have the highest number of failed logins (`evt.outcome:failure`).

A key-value format also simplifies the process to add custom attributes to logs. For example, you could add a [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) score to identify possible bot activity. Use quotes to wrap any attribute values that may contain spaces. This ensures that you capture the full value in a way that is parsable.

## Monitor and detect security threats{% #monitor-and-detect-security-threats %}

To properly monitor and detect security threats, there are key patterns you should take note of. For example, if you see a significant number of failed login attempts from a single user within a short period of time, it could indicate a [**brute force attack**](https://app.datadoghq.com/security/configuration/rules?product=siem&query=brute%20force%20attack&sort=rule). If those failed login attempts are followed by a successful one, it could be a successful account takeover that you should investigate immediately.

Another common authentication attack technique is [**credential stuffing**](https://app.datadoghq.com/security/configuration/rules?product=siem&query=credential%20stuffing%20attack&sort=rule). Credential stuffing is when an attacker mixes and matches breached login credentials to try to match a real user account. To detect this type of attack, look for logins using multiple `usr.id` values all coming from the same `network.client.ip`.

Datadog offers pre-configured [Detection Rules](https://docs.datadoghq.com/cloud_siem/default_rules/) that scan your ingested logs in real time for common attacker techniques like the two mentioned above. If any log triggers one of these rules, Datadog automatically generates a [Security Signal](https://docs.datadoghq.com/cloud_siem/explorer). This signal includes key data about the event, such as the type of attack detected and suggestions on how to respond and remedy the situation. You can view, filter, and sort all of your Security Signals in the explorer to triage them and see where to best focus your efforts.

For signals triggered from the `Credential Stuffing Attack` Detection Rule, there is an [out-of-the-box runbook](https://app.datadoghq.com/notebook/credentialstuffingrunbook) available to help with response and remediation. This runbook guides you through investigating a potential credential stuffing attack and includes graphs of related logs. To use this runbook, save a copy and set the time frame, document your investigation in markdown, and share it with teammates [for commenting](https://docs.datadoghq.com/notebooks/#commenting).

### Use dashboards to investigate{% #use-dashboards-to-investigate %}

Datadog provides out-of-the-box dashboards, such as the [IP investigation dashboard](https://app.datadoghq.com/screen/integration/security-monitoring-ip-investigation) and [user investigation dashboard](https://app.datadoghq.com/screen/integration/security-monitoring-user-investigation). These correlate key data from your authentication logs with relevant data from the rest of your environment to assist in your investigations.

For example, if a specific IP address or user is triggering multiple security signals, click on the IP address or user in a dashboard list or graph and select **View related Security Signals**. This populates all triggered security signals for that IP address or user in the Security Signals Explorer. If the data permits, this view is helpful when trying to correlate an IP address to a specific user, or vice versa. From here, you can examine and verify each rule to remediate attacks. Click on any rule and review the triage and response information in the **Rule Details** tab to properly assess and remediate the issue.

You can also create custom dashboards to visualize key authentication data like counts of logins by source and outcome. This provides you with a high-level view of activity across your entire user base and helps you see trends to identify suspicious spikes that you should investigate.

### Use Log Rehydrationâ¢ for future investigations{% #use-log-rehydration-for-future-investigations %}

Datadog ingests and analyzes [all of your logs](https://www.datadoghq.com/blog/logging-without-limits/), ensuring that you can detect threats across your entire environment. You can archive any logs that you [don't want to index](https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters), and then quickly [rehydrate them](https://www.datadoghq.com/blog/efficient-log-rehydration-with-datadog/) in the future for investigations, audits, and compliance purposes.

## Further reading{% #further-reading %}

- [Learn more about monitoring authentication logs](https://www.datadoghq.com/blog/how-to-monitor-authentication-logs/)
