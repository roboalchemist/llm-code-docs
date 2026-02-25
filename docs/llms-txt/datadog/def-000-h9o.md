# Source: https://docs.datadoghq.com/security/default_rules/def-000-h9o.md

---
title: OpenSearch domains should encrypt data sent between nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domains should encrypt data
  sent between nodes
---

# OpenSearch domains should encrypt data sent between nodes

## Description{% #description %}

This check determines if node-to-node encryption is activated for OpenSearch domains. Using HTTPS (TLS) can help prevent potential attackers from intercepting or altering network traffic through man-in-the-middle or similar attacks. Only secure connections via HTTPS (TLS) should be permitted. Activating node-to-node encryption for OpenSearch domains ensures that intra-cluster communications are securely encrypted while in transit.

Enabling this feature may come with a performance impact. It's critical to understand and evaluate the performance implications before enabling this option.

## Remediation{% #remediation %}

To activate node-to-node encryption for an OpenSearch domain, refer to [Enabling node-to-node encryption in the Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html#enabling-ntn).
