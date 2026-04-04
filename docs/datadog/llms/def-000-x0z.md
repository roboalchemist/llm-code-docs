# Source: https://docs.datadoghq.com/security/default_rules/def-000-x0z.md

---
title: DocumentDB clusters should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DocumentDB clusters should be encrypted
  at rest
---

# DocumentDB clusters should be encrypted at rest

## Description{% #description %}

This evaluation determines if an Amazon DocumentDB cluster has encryption enabled at rest. The evaluation will fail if the cluster is not encrypted at rest.

Data at rest encompasses all information stored on permanent, non-volatile storage devices, regardless of the duration. Encrypting this data helps safeguard its confidentiality by minimizing the likelihood of unauthorized access. It is advisable to enable encryption at rest for Amazon DocumentDB clusters to enhance security. Amazon DocumentDB utilizes the 256-bit Advanced Encryption Standard (AES-256) for data encryption, using keys managed in the AWS Key Management Service (AWS KMS).

## Remediation{% #remediation %}

Encryption at rest can be activated when you initially create an Amazon DocumentDB cluster. It is important to note that you cannot modify encryption settings after the cluster has been established. For further details, refer to the section titled [Enabling encryption at rest for an Amazon DocumentDB cluster in the Amazon DocumentDB Developer Guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/encryption-at-rest.html#encryption-at-rest-enabling).
