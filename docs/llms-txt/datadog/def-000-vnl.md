# Source: https://docs.datadoghq.com/security/default_rules/def-000-vnl.md

---
title: Elasticsearch domains should encrypt data transmitted between nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Elasticsearch domains should encrypt
  data transmitted between nodes
---

# Elasticsearch domains should encrypt data transmitted between nodes

## Description{% #description %}

This control verifies if node-to-node encryption is enabled for an Elasticsearch domain. The control will not pass if the Elasticsearch domain lacks node-to-node encryption. Additionally, it will generate failed findings if the Elasticsearch version does not support node-to-node encryption checks.

Using HTTPS (TLS) is recommended to prevent attackers from intercepting or altering network traffic through person-in-the-middle or similar attacks. Only encrypted connections via HTTPS (TLS) should be permitted. Enabling node-to-node encryption for Elasticsearch domains ensures that communication within the cluster is encrypted during transit.

There may be performance costs associated with this configuration. It is advisable to be aware of and evaluate the performance trade-offs before enabling this feature.

## Remediation{% #remediation %}

For details on how to enable node-to-node encryption for both new and existing domains, refer to the section [Enabling node-to-node encryption in the Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html#enabling-ntn).
