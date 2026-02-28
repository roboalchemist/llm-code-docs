# Source: https://docs.datadoghq.com/security/default_rules/def-000-zdh.md

---
title: Azure managed identity has a large permissions gap
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure managed identity has a large
  permissions gap
---

# Azure managed identity has a large permissions gap

## Description{% #description %}

To mitigate the impact of credential exposure or compromise, role assignments should be scoped down to the least level of privilege needed to perform their responsibilities. This rule identifies when a managed identity is assigned a role that has permissions that are more broad than what is regularly used. Datadog considers a permissions gap to be large when the number of unused permissions is greater than 40% of the total permissions count.

## Rationale{% #rationale %}

By comparing what actions a managed identity has performed in the last 15 days with what their roles permit, we can identify a permissions gap. This gap should be removed to mitigate the impact of a potential compromise.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions assigned to user to the minimum necessary for them to fulfill their duties. Azure Activity Logs provide a comprehensive view of actual user actions. These actions should be compared with the permissions sets allocated to the user and the permissions adjusted more tightly to accord with actual activity.
