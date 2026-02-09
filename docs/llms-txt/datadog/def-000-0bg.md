# Source: https://docs.datadoghq.com/security/default_rules/def-000-0bg.md

---
title: >-
  AWS Organizations centralized root credentials management feature should be
  enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Organizations centralized root
  credentials management feature should be enabled
---

# AWS Organizations centralized root credentials management feature should be enabled
 
## Description{% #description %}

To ensure the security of your AWS environment, you should centrally manage the root user credentials for all accounts within your AWS Organization. The root user has unrestricted access to all services and resources. By centralizing the management of these credentials, you can prevent unauthorized recovery and large-scale access, strengthening the security posture of your organization.

## Remediation{% #remediation %}

For guidance on enabling centralized root credentials management, refer to the [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) section of the AWS Identity and Access Management User Guide
