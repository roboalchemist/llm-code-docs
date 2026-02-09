# Source: https://docs.datadoghq.com/security/default_rules/def-000-z8a.md

---
title: IAM password policy should require user passwords to expire within 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM password policy should require user
  passwords to expire within 90 days
---

# IAM password policy should require user passwords to expire within 90 days
 
## Description{% #description %}

IAM password policies enforce rules for user passwords in AWS. One of these rules is defining the password expiration timeframe. Requiring user passwords to expire within 90 days is a best practice to enhance security. This policy reduces the risk of compromised accounts due to prolonged use of the same password, ensuring periodic updates that safeguard against potential threats.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

See the [Setting an AWS IAM Password Policy doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_password-policy.html#reset_iam_password_policy) for console remediation steps to enforce a 90-day expiration policy.
