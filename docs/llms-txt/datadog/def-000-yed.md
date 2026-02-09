# Source: https://docs.datadoghq.com/security/default_rules/def-000-yed.md

---
title: OpenSearch domains should have Audit Logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domains should have Audit
  Logging enabled
---

# OpenSearch domains should have Audit Logging enabled
 
## Description{% #description %}

This check determines if `audit` logging is enabled for Amazon OpenSearch Service domains, and is configured to send logs to Amazon CloudWatch Logs. Audit logs are crucial for recording detailed information about access and changes to OpenSearch resources, enabling you to track user activities, detect suspicious behavior, and ensure compliance with security policies and regulatory requirements.

## Remediation{% #remediation %}

To enable audit logging for an Amazon OpenSearch Service domain, refer to the [Configuring Amazon OpenSearch Service to Enable Audit Logging](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html) section of the Amazon OpenSearch Service Developer Guide.
