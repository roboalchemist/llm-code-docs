# Source: https://docs.datadoghq.com/security/default_rules/8sx-i8v-y8v.md

---
title: Symmetric CMKs should have encryption key rotation enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Symmetric CMKs should have encryption
  key rotation enabled
---

# Symmetric CMKs should have encryption key rotation enabled

## Description{% #description %}

AWS Key Management Service (KMS) allows for backing key rotation, which involves updating the key material tied to a Customer Managed Key (CMK). Rotation of symmetric keys is recommended to minimize the risk of key compromise, as it ensures new data is encrypted with a fresh key. Prior backing keys are retained for seamless decryption of previously encrypted data. Symmetric key rotation is automated annually, though it is not available for asymmetric keys.

## Remediation{% #remediation %}

For instructions on enabling CMK key rotation in AWS KMS, refer to the [AWS Key Rotation Guide](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).
