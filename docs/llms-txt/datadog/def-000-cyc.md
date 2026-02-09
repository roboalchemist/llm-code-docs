# Source: https://docs.datadoghq.com/security/default_rules/def-000-cyc.md

---
title: >-
  AWS Organizations member accounts should not have root user credentials when
  centralized access is enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Organizations member accounts
  should not have root user credentials when centralized access is enabled
---

# AWS Organizations member accounts should not have root user credentials when centralized access is enabled
 
## Description{% #description %}

To ensure the security of your AWS environment, you should centrally manage root user credentials and sessions for all accounts within your AWS Organization. The root user has unrestricted access to all services and resources. By centralizing the management of root users, you can prevent unauthorized recovery and large-scale access, strengthening the security posture of your organization. After this feature is enabled, the "Delete root user credentials" action should be performed on all member accounts to ensure that centralized access cannot be bypassed. Performing this action deletes all root user access keys, passwords, and signing certificates.

## Remediation{% #remediation %}

For guidance on enabling centralized root credentials management and deleting root user credentials, refer to the [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) and [Perform a privileged task on an AWS Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html) sections of the AWS Identity and Access Management User Guide.
