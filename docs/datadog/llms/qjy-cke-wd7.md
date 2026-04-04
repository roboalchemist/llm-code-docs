# Source: https://docs.datadoghq.com/security/default_rules/qjy-cke-wd7.md

---
title: IAM policies should adhere to least-privilege
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM policies should adhere to
  least-privilege
---

# IAM policies should adhere to least-privilege

## Description{% #description %}

IAM policies define privileges granted to users, groups, or roles. Best practice recommends granting only the permissions necessary to perform specific tasks. Begin with minimal permissions, adding more as necessary, rather than starting with overly permissive settings. Granting full administrative privileges instead of essential permissions can expose resources to potential misuse or compromise. It's critical to remove policies with `"Effect": "Allow"` combined with `"Action": "*"` and `"Resource": "*"` to minimize security risks.

## Remediation{% #remediation %}

For guidance on removing overly permissive policies and properly configuring IAM policies, refer to [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
