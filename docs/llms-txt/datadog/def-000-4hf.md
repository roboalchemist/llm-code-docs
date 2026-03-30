# Source: https://docs.datadoghq.com/security/default_rules/def-000-4hf.md

---
title: Route 53 public hosted zones should log DNS queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route 53 public hosted zones should log
  DNS queries
---

# Route 53 public hosted zones should log DNS queries

## Description{% #description %}

This control verifies whether DNS query logging is activated for an Amazon Route 53 public hosted zone.

Enabling DNS query logging enhances security and compliance by providing greater visibility into DNS activity. The logs capture details such as the queried domain or subdomain, timestamp of the query, DNS record type, and response code. When this feature is enabled, Route 53 delivers the log files to Amazon CloudWatch Logs for further analysis and monitoring.

## Remediation{% #remediation %}

For guidance regarding Route53 query logging, refer to the [Configuring logging for DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html#query-logs-configuring) section of the Amazon Route 53 Developer Guide.
