# Source: https://docs.datadoghq.com/security/default_rules/def-000-s0m.md

---
title: AWS Organizations root sessions feature should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Organizations root sessions feature
  should be enabled
---

# AWS Organizations root sessions feature should be enabled
 
## Description{% #description %}

Enabling the AWS Organizations Root Sessions feature increases security by centralizing control and minimizing the attack surface associated with highly privileged root user credentials. This feature allows you to remove long-term root access keys for member accounts and instead grant temporary, time-bound, and task-scoped permissions for essential administrative actions. By doing so, you eliminate the risks of compromised root credentials and ensure that powerful permissions are only used when absolutely necessary and in a monitored, auditable manner.

## Remediation{% #remediation %}

For guidance on enabling centralized root sessions, refer to the [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) section of the AWS Identity and Access Management User Guide
