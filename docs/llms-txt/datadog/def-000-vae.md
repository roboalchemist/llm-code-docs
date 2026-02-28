# Source: https://docs.datadoghq.com/security/default_rules/def-000-vae.md

---
title: IAM users should have assigned permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM users should have assigned
  permissions
---

# IAM users should have assigned permissions

## Description{% #description %}

IAM Users without permissions can lead to potential security risks and misconfigurations. Users without assigned policies should be investigated and removed if not needed.

## Remediation{% #remediation %}

See the [Managing IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) and [Assigning Permissions to IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) documentation for steps on how to assign appropriate permissions to IAM users. If a user is no longer required, refer to the [Removing IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting_inline-policies) documentation to safely delete the user.
