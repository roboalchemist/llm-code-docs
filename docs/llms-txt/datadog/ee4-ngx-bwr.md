# Source: https://docs.datadoghq.com/security/default_rules/ee4-ngx-bwr.md

---
title: Access keys granting 'root' should be removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Access keys granting 'root' should be
  removed
---

# Access keys granting 'root' should be removed

## Description{% #description %}

The root account is the most privileged user in an AWS account, and AWS Access Keys provide programmatic access to this account. Datadog recommends that you remove all access keys associated with the root account to enhance security. Removing these keys limits the vectors by which the account can be compromised and encourages the creation and use of role-based accounts that adhere to the principle of least privilege. Note that the root IAM User account for GovCloud (US) regions is not enabled by default. However, upon request, AWS support has the ability to enable root access solely via access keys (CLI, API methods) for regions within the AWS GovCloud.

## Remediation{% #remediation %}

For instructions on removing access keys from the root account, refer to [Managing Access Keys for Your AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_keys).
