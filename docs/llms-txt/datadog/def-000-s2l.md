# Source: https://docs.datadoghq.com/security/default_rules/def-000-s2l.md

---
title: Azure function has admin level privileges at the subscription scope
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure function has admin level
  privileges at the subscription scope
---

# Azure function has admin level privileges at the subscription scope
 
## Description{% #description %}

This rule identifies when an Azure Function has administrative level permissions at the subscription scope.

## Rationale{% #rationale %}

Administrative Azure role assignments at the subscription scope grant extensive privileges that can affect all resources within the subscription. This broad access increases the risk of accidental or malicious changes.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions and scope of a role assignment to the minimum necessary. Where possible, assign roles at the resource group or individual resource level and use built-in roles with limited privileges tailored to operational requirements.
