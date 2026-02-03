# Source: https://docs.datadoghq.com/security/default_rules/def-000-2mt.md

---
title: IAM users should not have both Console access and Access Keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM users should not have both Console
  access and Access Keys
---

# IAM users should not have both Console access and Access Keys
 
## Description{% #description %}

AWS IAM users should be granted the minimum necessary access according to the principle of least privilege. Having both Console access and Access Keys simultaneously can increase the risk surface if either credential type is compromised. Best practices recommend restricting IAM users to only one method of access based on their job functions to minimize security vulnerabilities.

## Remediation{% #remediation %}

See the [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and [Enabling a Sign-in Console Password for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user.html) documentation for console remediation steps to remove either Console access or Access Keys.
