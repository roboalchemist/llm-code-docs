# Source: https://docs.datadoghq.com/security/access_control.md

---
title: Access Control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Access Control
---

# Access Control
Available for:
{% icon name="icon-siem" /%}
 Cloud SIEM |
{% icon name="icon-cloud-security-management" /%}
 Workload Protection |
{% icon name="icon-app-sec" /%}
 App and API Protection
## Overview{% #overview %}

Datadog's access management system uses role-based access control, enabling you to define the level of access users have to Datadog resources. Users are assigned to roles that define their account permissions, including what data they can read and which account assets they can modify. When permissions are granted to a role, any user who is associated with that role receives those permissions. See the [Account Management Access Control](https://docs.datadoghq.com/account_management/rbac/#role-based-access-control) documentation for more information.

For Datadog Security products, [granular access control](https://docs.datadoghq.com/account_management/rbac/granular_access/) is available for detection rules and suppressions, allowing you to restrict access by teams, roles, or service accounts.

## Permissions{% #permissions %}

See the [list of permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#cloud-security-platform) for Security products.

## Restrict access to detection rules{% #restrict-access-to-detection-rules %}

By default, all users have view and edit access to the detection rules. To use granular access controls to limit the [roles](https://docs.datadoghq.com/account_management/rbac/#role-based-access-control) that may edit a single rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restrict Access**. The dialog box updates to show that members of your organization have **Viewer** access by default. Use that dropdown menu to select one or more roles, teams, or users that may edit the security rule.
1. Use the dropdown menu to select one or more roles, teams, or users that may edit the security rule.
1. Click **Add**.
1. Click **Save**.

**Note:** To maintain your edit access to the rule, Datadog requires you to include at least one role that you are a member of before saving.

To restore access to a rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restore Full Access**.
1. Click **Save**.

## Restrict access to suppression rules{% #restrict-access-to-suppression-rules %}

By default, all users have view and edit access to [suppressions](https://docs.datadoghq.com/security/suppressions/). To use granular access controls to limit the roles that may edit a suppression rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restrict Access**. The dialog box updates to show that members of your organization have **Viewer** access by default. Use that dropdown menu to select one or more roles, teams, or users that may edit the suppression rule.
1. Click **Add**.
1. Click **Save**.

**Note**: To maintain your edit access to the rule, Datadog requires you to include at least one role that you are a member of before saving.

To restore access to a rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restore Full Access**.
1. Click **Save**.
