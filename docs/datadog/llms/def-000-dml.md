# Source: https://docs.datadoghq.com/security/default_rules/def-000-dml.md

---
title: 'IAM policies should not use ''Effect: Allow'' with ''NotAction'''
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM policies should not use 'Effect:
  Allow' with 'NotAction'
---

# IAM policies should not use 'Effect: Allow' with 'NotAction'

## Description{% #description %}

IAM policies using 'Effect: Allow' with 'NotAction' permits all actions except those explicitly denied, which can lead to unintended privilege escalation and broader access than intended. Instead, explicit permissions should be defined to enforce the principle of least privilege, ensuring users have only the access necessary for their roles.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

See the [IAM JSON Policy Elements: NotAction](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html) documentation for guidance on how to modify policies. Replace 'NotAction' with specific actions that should be allowed and ensure your policies adhere to the principle of least privilege.
