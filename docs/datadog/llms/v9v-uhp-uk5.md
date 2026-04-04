# Source: https://docs.datadoghq.com/security/default_rules/v9v-uhp-uk5.md

---
title: The 'root' account should not be used for daily tasks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The 'root' account should not be used
  for daily tasks
---

# The 'root' account should not be used for daily tasks

## Description{% #description %}

With the creation of an AWS account, a root user is established that cannot be disabled or deleted. This user has unrestricted access to and control over all resources in the account. Datadog highly recommends that you avoid using this account for everyday tasks to adhere to security best practices.

The root user's unrestricted access is inconsistent with the principles of least privilege and separation of duties, which can lead to unnecessary harm due to errors or account compromise. In GovCloud (US) regions, the root user is not enabled by default but can be enabled upon request with access granted only through access-keys (CLI, API methods).

## Remediation{% #remediation %}

For instructions on managing the root user account to prevent it from being used for daily activities, refer to [AWS Best Practices for Managing Root User Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html).
