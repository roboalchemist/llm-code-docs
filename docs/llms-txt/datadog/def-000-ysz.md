# Source: https://docs.datadoghq.com/security/default_rules/def-000-ysz.md

---
title: IAM groups should have at least one user attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM groups should have at least one
  user attached
---

# IAM groups should have at least one user attached

## Description{% #description %}

IAM groups help manage user permissions by bundling policies that can be applied to multiple users simultaneously. If you have IAM groups that are no longer needed, it is best to remove them to avoid potential security risks. Groups with no users may indicate misconfiguration or potential security oversight, reducing the effectiveness of your access management strategy.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

See the [Remove IAM Groups documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_remove.html) for detailed steps on how to delete IAM groups.
