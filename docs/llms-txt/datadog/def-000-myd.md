# Source: https://docs.datadoghq.com/security/default_rules/def-000-myd.md

---
title: IAM role has trust policy containing cross-organization principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM role has trust policy containing
  cross-organization principal
---

# IAM role has trust policy containing cross-organization principal
 
## Description{% #description %}

This control examines whether IAM roles have trust policies that allow access to principals from different AWS organizations. The control will fail if the following conditions are true:

- The role's trust policy contains an `Allow` statement
- The statement references a principal from an AWS account that is onboarded to Datadog
- AWS Organizations data is available for both the role account and the principal account
- The role account and the principal account belong to different AWS organizations

**Note**: The impact of `Condition` elements of statements in the role trust policy is not assessed by this control.

Cross-organization access in trust policies may introduce security risks by allowing access across deliberately isolated organizations. This type of access should be carefully controlled and limited to specific, well-documented business requirements.

Organizations should maintain strict organizational boundaries and only allow cross-organization access when there is a legitimate business need and proper security controls are in place.

## Remediation{% #remediation %}

Review the IAM role's trust policy to ensure that cross-organization principals are intentional and necessary.

For guidance on modifying IAM role trust policies, refer to the [Update a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-trust-policy.html) section of the AWS Identity and Access Management User Guide
