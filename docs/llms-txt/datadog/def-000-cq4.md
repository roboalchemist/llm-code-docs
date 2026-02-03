# Source: https://docs.datadoghq.com/security/default_rules/def-000-cq4.md

---
title: Azure managed identity has access to a large number of resources
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure managed identity has access to a
  large number of resources
---

# Azure managed identity has access to a large number of resources
 
## Description{% #description %}

To mitigate the impact of credential exposure or compromise, role assignments should be scoped down to the least scope of access needed to perform their responsibilities. This rule identifies when a managed identity is assigned a role that has overly broad access to resources within a tenant. Datadog considers access large when the number of resources a user has access to is greater that 40% of the total resource count of the tenant.

## Rationale{% #rationale %}

By comparing the volume of resource a managed identity can access with the total resources of a tenant, we can identify overly large access. This access should be more tightly scoped to limit the impact of a potential compromise.

## Remediation{% #remediation %}

Datadog recommends reducing the scope of a role assigned to user to the minimum necessary for them to fulfill their duties. Azure Activity Logs provide a comprehensive view of actual resource interaction. These actions should be compared with the total allocated to the managed identity and the role assignment's scope adjusted more tightly to accord with necessary activity.
