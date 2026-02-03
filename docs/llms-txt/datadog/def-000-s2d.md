# Source: https://docs.datadoghq.com/security/default_rules/def-000-s2d.md

---
title: Elasticsearch domains should have error logging to CloudWatch Logs enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Elasticsearch domains should have error
  logging to CloudWatch Logs enabled
---

# Elasticsearch domains should have error logging to CloudWatch Logs enabled
 
## Description{% #description %}

This control confirms whether Elasticsearch domains are configured to forward error logs to CloudWatch Logs.

It's recommended to enable error logging for Elasticsearch domains and forward these logs to CloudWatch Logs for retention and analysis. Error logs from the domain can play a key role in security and access audits and can help in diagnosing availability issues.

## Remediation{% #remediation %}

For details on how to activate log publishing, refer to the [Enabling log publishing (console) section in the Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-slow-logs-console).
