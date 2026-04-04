# Source: https://docs.datadoghq.com/security/default_rules/def-000-aw5.md

---
title: OpenSearch domains should have encryption at rest enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domains should have
  encryption at rest enabled
---

# OpenSearch domains should have encryption at rest enabled

## Description{% #description %}

This check ensures an OpenSearch domain has encryption-at-rest enabled. To enhance security for sensitive information, it's important to configure your OpenSearch Service domain for encryption at rest. With this setup, AWS Key Management Service (KMS) stores and manages your encryption keys, utilizing the Advanced Encryption Standard 256-bit algorithm (AES-256) for encryption. For additional details, refer to the section on [data encryption at rest for Amazon OpenSearch Service in the Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html).

## Remediation{% #remediation %}

For a guide on enabling encryption at rest for both new and existing OpenSearch domains, please refer to the [Enabling encryption of data at rest section in the Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html#enabling-ear).
