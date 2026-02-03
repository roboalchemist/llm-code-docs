# Source: https://docs.datadoghq.com/account_management/rbac.md

---
title: Access Control
description: >-
  Manage user access with role-based permissions, custom roles, and granular
  access control for dashboards, monitors, and other Datadog resources.
breadcrumbs: Docs > Account Management > Access Control
---

# Access Control

## Overview{% #overview %}

Datadog offers a flexible access management system that allows you to customize the level at which you control access to your Datadog resources.

Users looking for basic functionality have access to OOTB roles with [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/). For more flexibility, create your own custom roles to combine permissions into new roles. Permissions attached to a custom role apply to all resources of a particular resource type.

Organizations and users that need maximum flexibility can control access to individual dashboards, notebooks, and other resources with [granular access control](https://docs.datadoghq.com/account_management/rbac/granular_access/).

## Role based access control{% #role-based-access-control %}

Roles categorize users and define what account permissions those users have, such as what data they can read or what account assets they can modify. By default, Datadog offers three roles, and you can create custom roles so you can define a better mapping between your users and their permissions.

By granting permissions to roles, any user who is associated with that role receives that permission. When users are associated with multiple roles, they receive all the permissions granted to each of their roles. The more roles a user is associated with, the more access they have within a Datadog account.

If a user in a [child organization](https://docs.datadoghq.com/account_management/multi_organization/) has `org_management` permission, it does not mean that they have the same permission in the parent org. Users' roles are not shared between parent and child organizations.

**Note**: If you use a SAML identity provider, you can integrate it with Datadog for authentication, and you can map identity attributes to Datadog default and custom roles. For more information, see [SAML group mapping](https://docs.datadoghq.com/account_management/saml/mapping/).

## Datadog default roles{% #datadog-default-roles %}

{% dl %}

{% dt %}
Datadog Admin Role
{% /dt %}

{% dd %}
Users have access to billing information and the ability to revoke API keys. They can manage users and configure [read-only dashboards](https://docs.datadoghq.com/dashboards/). They can also promote standard users to administrators.
{% /dd %}

{% dt %}
Datadog Standard Role
{% /dt %}

{% dd %}
Users are allowed to view and modify all monitoring features that Datadog offers, such as [dashboards](https://docs.datadoghq.com/dashboards/), [monitors](https://docs.datadoghq.com/monitors/), [events](https://docs.datadoghq.com/events/), and [notebooks](https://docs.datadoghq.com/notebooks). Standard users can also invite other users to organizations.
{% /dd %}

{% dt %}
Datadog Read Only Role
{% /dt %}

{% dd %}
Users do not have access to edit within Datadog. This comes in handy when you'd like to share specific read-only views with a client, or when a member of one business unit needs to share a [dashboard](https://docs.datadoghq.com/dashboards/) with someone outside their unit.
{% /dd %}

{% /dl %}

## Custom roles{% #custom-roles %}

The custom roles feature gives your organization the ability to create new roles with unique permission sets. Manage your custom roles through the Datadog site, the [Datadog Role API](https://docs.datadoghq.com/api/v2/roles/), or SAML directly. Find out below how to create, update, or delete a role. See [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/) for more information about available permissions. Only users with the User Access Manage permission can create or edit roles in Datadog.

### Enable custom roles{% #enable-custom-roles %}

1. Navigate to [Organization Settings](https://app.datadoghq.com/organization-settings/).
1. On the left side of the page, select **Roles**.
1. Click the gear in the upper right corner. The Custom Roles pop-up appears.
1. In the Custom Roles pop-up, click **Enable**.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/rbac/enable_custom_roles.0f2af1db8cb3cd34d2abe34751d9f541.png?auto=format"
   alt="Custom Roles pop-up with Enable button" /%}

Alternatively, making a POST call to the [Create Role API endpoint](https://docs.datadoghq.com/api/latest/roles/#create-role) automatically enables custom roles for your organization.

### Create a custom role{% #create-a-custom-role %}

{% tab title="Datadog application" %}
To create a custom role:

1. Go to your [Datadog Roles page](https://app.datadoghq.com/access/roles).
1. Select **New Role** in the upper right corner of the page.
1. Give a name to your role.
1. Assign a set of permissions to your role. See [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/) for more information about available permissions.

Once a role is created, you can [add the role to existing users](https://docs.datadoghq.com/account_management/users/#edit-a-user-roles).
{% /tab %}

{% tab title="API" %}
Find an example of how to create a role in [Create Role API Reference](https://docs.datadoghq.com/api/latest/roles/#create-role).
{% /tab %}

### Update a role{% #update-a-role %}

{% tab title="Datadog application" %}
To edit a custom role:

1. Go to your [Datadog Roles page](https://app.datadoghq.com/access/roles).
1. Select the edit button on the role you would like to modify.
1. Modify the set of permissions for your role. See [Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/) for more information about available permissions.
1. Save your changes.

Once a role is modified, permissions are updated for all users with the role.
{% /tab %}

{% tab title="API" %}
Find an example of how to update a role in [Update Role API Reference](https://docs.datadoghq.com/api/latest/roles/#update-a-role).
{% /tab %}

### Clone a role{% #clone-a-role %}

{% tab title="Datadog application" %}
To clone an existing role:

1. Go to your [Datadog Roles page](https://app.datadoghq.com/access/roles).
1. Hover over the role you would like to clone. A series of buttons appears to the right.
1. Select the clone button on the role you would like to clone.
1. Optionally modify the name or permissions of the role.
1. Click the **Save** button at the bottom.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/rbac/clone_role.a6f438b0fd8d62aa3d06fd2c15c4a010.png?auto=format"
   alt="List of two roles with Clone button highlighted" /%}

{% /tab %}

{% tab title="API" %}
Find an example of how to clone a role in the [Cloning A Role API reference](https://docs.datadoghq.com/api/latest/roles/#create-a-new-role-by-cloning-an-existing-role).
{% /tab %}

### Delete a role{% #delete-a-role %}

{% tab title="Datadog application" %}
To delete a custom role:

1. Go to your [Datadog Roles page](https://app.datadoghq.com/access/roles).
1. Hover over the role you would like to delete. A series of buttons appears to the right.
1. Select the delete button on the role you would like to delete.
1. Confirm your decision.

Once a role is deleted, permissions are updated for all users with the role. Users without any roles cannot use Datadog effectively, but still maintain limited access.
{% /tab %}

{% tab title="API" %}
Find an example of how to delete a role in the [Delete Role API reference](https://docs.datadoghq.com/api/latest/roles/#delete-role).
{% /tab %}

### Apply a role template{% #apply-a-role-template %}

When creating or updating a role on the Datadog site, use a Datadog role template to apply a prescribed set of permissions to the role.

1. On the New Role or Edit Role page, click the **Show Role Templates** button on the right.
1. A dropdown menu populated with role templates appears.
1. From the menu, select the role template whose permissions you would like to apply to your role.
1. Click the **Apply** button.
1. Optionally make additional changes to your role.
1. Click the **Save** button.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/rbac/role_templates.77463a85fb2912867212ae5acb42ab42.png?auto=format"
   alt="Role Templates dropdown menu with Datadog Billing Admin Role selected" /%}

## Further Reading{% #further-reading %}

- [Manage roles and permissions with the Roles API](https://docs.datadoghq.com/api/v2/roles/)
- [Manage your permissions with the Permissions API](https://docs.datadoghq.com/api/v2/roles/#list-permissions)
- [Discover the list of permissions available](https://docs.datadoghq.com/account_management/rbac/permissions)
- [Enable single sign on with SAML](https://docs.datadoghq.com/account_management/saml/)
- [Build compliance, governance, and transparency across your teams with Datadog Audit Trail](https://www.datadoghq.com/blog/compliance-governance-transparency-with-datadog-audit-trail/)
