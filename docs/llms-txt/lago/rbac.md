# Source: https://getlago.com/docs/guide/security/rbac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# RBAC - Role Base Access Control

> Define user roles & permissions in Lago.

<Info>
  **PREMIUM ADD-ON** ✨

  RBAC is only available to licensed users. Please [**contact us**](mailto:hello@getlago.com) to get access to this premium add-on.
</Info>

## System roles in Lago

System roles are predefined by Lago and define the access scope and permissions granted to users within the Lago platform. Lago provides three primary system roles:

### Admin role

Admins wield full control over Lago, managing billable metrics, plans, customers, subscriptions, settings or financial analysis.
Typically, developers with admin roles handle all critical billing operations. By default, the account creator is assigned the Admin role.

### Account manager role

The Account manager role suits Sales or Customer Success Managers, enabling them to carry out billing tasks for customers.
Account Managers can assign subscriptions, coupons, add-ons, and override prices but are not permitted to modify metrics or plans.

Here is the [full list of permissions](https://github.com/getlago/lago-api/blob/main/config/permissions.yml) for this pre-built role.

### Finance & analyst role

The Finance & analyst role is view-only, restricted from creating or editing metrics and plans, or assigning core billing actions such as coupons,
subscriptions. It's ideal for analyzing financial data, reviewing invoices, and issuing credit notes as necessary.

Here is the [full list of permissions](https://github.com/getlago/lago-api/blob/main/config/permissions.yml) for this pre-built role.

## Custom roles and permissions

<Info>
  **PREMIUM ADD-ON** ✨

  This add-on is available on demand only. Please [**contact us**](mailto:hello@getlago.com) to get access to this premium add-on.
</Info>

Custom roles enable you to **define tailored permission sets that align with your organization's specific requirements**. There is no limit to the number of custom roles you can create. This feature is designed around the following principles:

* Updating the permissions of a role automatically updates the permissions for all users assigned to that role; and
* At least one role with administrative permissions must always exist.

[This document](https://github.com/getlago/lago-api/blob/main/config/permissions.yml) outlines all the potential permissions by object that can be assigned to a custom role.

To create a custom role:

1. Navigate to the **Settings** view in Lago;
2. Access the **Roles & Permissions** section;
3. Click on **Create Role**;
4. Define the role `name`, `code` and `description`;
5. Select the desired permissions from the list;
6. Save the new custom role; and
7. Assign users to the newly created custom role.

<Frame caption="Create a custom role">
  <img src="https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=0703c6268624b362d664839b5b07bb3b" data-og-width="1956" width="1956" data-og-height="1828" height="1828" data-path="guide/security/images/custom-role-definition.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=280&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=db3546ca651d4e98afecb26c09f863a3 280w, https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=560&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=c0d4ec98cb50c25fa396aed6ed6c2af7 560w, https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=840&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=b6e03d3c2ef6f8365db0b364ed96d335 840w, https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=1100&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=02191ea623b6ba2ebc3a5a979c7dcb36 1100w, https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=1650&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=5a1f06a9d122d32276d0c85879f1d670 1650w, https://mintcdn.com/lago-docs/jh5wplDIUjMHyJWN/guide/security/images/custom-role-definition.png?w=2500&fit=max&auto=format&n=jh5wplDIUjMHyJWN&q=85&s=4e27a5bd640eaf9fcfabcefc59d3f0d3 2500w" />
</Frame>
