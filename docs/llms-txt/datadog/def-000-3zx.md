# Source: https://docs.datadoghq.com/security/default_rules/def-000-3zx.md

---
title: IAM roles should be used within the last 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM roles should be used within the
  last 90 days
---

# IAM roles should be used within the last 90 days

## Description{% #description %}

Ensuring IAM roles are actively used within the last 90 days helps maintain a secure AWS environment. Inactive roles can pose security risks, such as outdated permissions lingering in the system, which can be exploited for unauthorized access.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

For detailed steps on managing IAM roles, refer to the [IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage.html).
