# Source: https://docs.datadoghq.com/security/default_rules/def-000-hwc.md

---
title: No more than one active SSH public key should be assigned to a single user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > No more than one active SSH public key
  should be assigned to a single user
---

# No more than one active SSH public key should be assigned to a single user

## Description{% #description %}

This control ensures that no more than one active SSH public key is assigned to a single IAM user.

Limiting the number of active SSH public keys per user helps reduce the attack surface and minimizes the complexity of managing user access. This practice strengthens security by ensuring better control over user credentials.

## Remediation{% #remediation %}

To enforce a policy of having only one active SSH public key per IAM user, review and manage SSH keys through the AWS Management Console, CLI, or API. Refer to the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html) for instructions on managing user credentials and SSH keys.
