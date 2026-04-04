# Source: https://docs.datadoghq.com/security/default_rules/def-000-ee1.md

---
title: Privileged Azure Entra user is a guest account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Privileged Azure Entra user is a guest
  account
---

# Privileged Azure Entra user is a guest account

## Description{% #description %}

Guest accounts are users external to your organization that have been invited into your Azure tenant. They open an additional attack vector within your tenant. Guest accounts should be reviewed to ensure their level of access is the minimum required for their role and that they are removed when no longer required.

## Remediation{% #remediation %}

1. Review the access level of all guest accounts in your tenant.
1. Remove any guest accounts that do not require access to your tenant.
1. Ensure that the access level of guest accounts is the minimum required for their role.
