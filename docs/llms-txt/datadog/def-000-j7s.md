# Source: https://docs.datadoghq.com/security/default_rules/def-000-j7s.md

---
title: Redshift clusters should enforce encryption in transit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should enforce
  encryption in transit
---

# Redshift clusters should enforce encryption in transit
 
## Description{% #description %}

This control verifies whether Amazon Redshift cluster connections require encryption during transit. The parameter `require_ssl` must be set to `True`.

Using TLS helps protect against potential attacks, such as person-in-the-middle attempts, by securing network traffic from being intercepted or altered. Only TLS encrypted connections should be permitted. Keep in mind that encrypting data in transit may impact performance. Datadog recommends testing your application with TLS enabled to evaluate its performance and understand the potential effects.

## Remediation{% #remediation %}

For guidance on configuring Redshift parameters, please refer to the [Modifying a parameter group](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-parameter-groups-console.html#parameter-group-modify) section of the Amazon Redshift Management Guide.
