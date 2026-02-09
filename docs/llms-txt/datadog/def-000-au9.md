# Source: https://docs.datadoghq.com/security/default_rules/def-000-au9.md

---
title: >-
  AWS IAM role with external cross-account trust relationship does not use an
  external ID
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM role with external
  cross-account trust relationship does not use an external ID
---

# AWS IAM role with external cross-account trust relationship does not use an external ID
 
## Description{% #description %}

To reduce the risk of [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) attacks, external vendors should use an [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) when assuming a role in your AWS account.

## Rationale{% #rationale %}

The use of external IDs mitigate the risk of confused deputy attacks.

## Remediation{% #remediation %}

Ensure all external identities use an external ID when assuming a role in your AWS account.
