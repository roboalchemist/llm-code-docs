# Source: https://docs.datadoghq.com/security/default_rules/def-000-rnw.md

---
title: IAM groups should not have inline policies attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM groups should not have inline
  policies attached
---

# IAM groups should not have inline policies attached

## Description{% #description %}

IAM policies are rules that define the level of access granted to AWS resources. These policies can either be managed (reusable and centrally administered) or inline (embedded directly into a user, group, or role). It is a best practice to avoid using inline policies for IAM groups and instead attach managed policies. Using managed policies for IAM groups offers better manageability and reduces the complexity of policy administration. It ensures consistency in access management, provides an easier mechanism for policy updates, and simplifies auditing and compliance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

See the [Managed policies and inline policies documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#convert-inline-to-managed-policy) for console remediation steps.
