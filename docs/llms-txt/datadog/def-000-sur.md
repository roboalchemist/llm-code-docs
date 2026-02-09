# Source: https://docs.datadoghq.com/security/default_rules/def-000-sur.md

---
title: IAM customer managed policies should not allow wildcard actions for services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM customer managed policies should
  not allow wildcard actions for services
---

# IAM customer managed policies should not allow wildcard actions for services
 
## Description{% #description %}

IAM customer managed policies that allow wildcard actions for services (for example, `"Action": "*"`) can lead to unintended security risks by providing overly broad permissions. Best practices dictate that policies should be as specific as possible, granting only the necessary permissions required for a task. By avoiding wildcards in actions, you can significantly reduce the risk of unauthorized access and actions within your AWS environment.

## Remediation{% #remediation %}

See the [IAM Policies and Wildcards](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_wildcards) and [Modifying Customer Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) documentation for steps on how to identify and rectify policies that use wildcard actions.
