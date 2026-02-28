# Source: https://docs.datadoghq.com/security/default_rules/def-000-t5f.md

---
title: Neptune DB clusters should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB clusters should be encrypted
  at rest
---

# Neptune DB clusters should be encrypted at rest

## Description{% #description %}

This check verifies if a Neptune DB cluster has encryption enabled for data at rest.

Data at rest includes any information stored in persistent, non-volatile storage for any length of time. Encryption enhances data confidentiality by minimizing the risk of unauthorized access. Enabling encryption for your Neptune DB clusters safeguards both data and metadata from unauthorized access, while also meeting compliance standards for encrypting production file systems.

## Remediation{% #remediation %}

For guidance on enabling at-rest encryption, please refer to the [Encrypting Neptune resources at rest](https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html) section of the Neptune User Guide.
