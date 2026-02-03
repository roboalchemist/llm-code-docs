# Source: https://docs.datadoghq.com/security/default_rules/def-000-lic.md

---
title: IAM role has trust policy containing external principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM role has trust policy containing
  external principal
---

# IAM role has trust policy containing external principal
 
## Description{% #description %}

This control examines whether IAM roles have trust policies that allow access to principals in external AWS accounts. External accounts are defined as accounts that are not onboarded to Datadog, or operated by Datadog for integration purposes. The control will fail if the following conditions are true:

- The role's trust policy contains an `Allow` statement
- The statement references a principal from an AWS account that is not onboarded to Datadog, or operated by Datadog for integration purposes

**Note**: The impact of `Condition` elements of statements in the role trust policy is not assessed by this control.

External principals in trust policies can potentially grant unintended access to AWS resources, especially if the external account is compromised or malicious. Following the principle of least privilege, trust policies should only include principals from known, trusted accounts.

**Note**: If the role trust policy intentionally provides access to a trusted third-party AWS account that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

Review the IAM role's trust policy to ensure that external principals are intentional and necessary.

For guidance on modifying IAM role trust policies, refer to the [Update a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-trust-policy.html) section of the AWS Identity and Access Management User Guide.
