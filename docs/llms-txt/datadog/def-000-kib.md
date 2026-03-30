# Source: https://docs.datadoghq.com/security/default_rules/def-000-kib.md

---
title: Azure custom administrator roles should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure custom administrator roles should
  be disabled
---

# Azure custom administrator roles should be disabled

## Description{% #description %}

Avoid the use of custom administrator roles, as they are error prone. Instead, use Azure's built-in least privilege 'job' roles. Audit and remove custom roles if at all possible.

## Remediation{% #remediation %}

To remove a [custom role](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) in Azure using the portal, follow the steps below:

1. Log into the [Azure portal](https://portal.azure.com) and navigate to **Subscriptions**.
1. Select the specific subscription, then under **Settings**, click **Access control (IAM)**.
1. In the **Roles** section, find and select the custom role you want to remove.
1. Click **Delete** and confirm by clicking **Yes**.

**Note:** Removing roles can impact access for users and groups assigned to these roles.
