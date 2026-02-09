# Source: https://docs.datadoghq.com/security/default_rules/def-000-zyi.md

---
title: >-
  IAM customer managed policies should not allow decryption actions on all KMS
  keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM customer managed policies should
  not allow decryption actions on all KMS keys
---

# IAM customer managed policies should not allow decryption actions on all KMS keys
 
## Description{% #description %}

This control examines whether the default versions of IAM customer-managed policies permit principals to use AWS KMS decryption actions on all KMS resources. The control will fail if the policy allows any of the following actions on all KMS keys:

- `kms:*`
- `kms:Decrypt`
- `kms:ReEncryptFrom`

The control specifically checks the Resource element of the policy and does not consider any conditions specified in the Condition element. It evaluates IAM policies meeting any of the following criteria:

- Customer-managed policies attached to any IAM resource as a permissions policy
- Customer-managed policies not attached to any IAM resource

It does not evaluate IAM policies meeting any of the following criteria:

- Customer-managed policies attached to any IAM resource but used only as a boundary
- Inline policies
- AWS-managed policies

To enhance security, instead of granting permissions for all KMS keys, identify the specific keys that principals need to access encrypted data. Design policies to restrict user permissions to only those keys. For example, instead of allowing kms:Decrypt on all KMS keys, grant this permission only for keys in a particular region relevant to your account. Applying the principle of least privilege helps reduce the risk of unintentional data exposure.

## Remediation{% #remediation %}

See the [IAM Policies and Wildcards](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_wildcards) and [Modifying Customer Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) documentation for steps on how to identify and rectify policies that contain overly permissive KMS permissions.
