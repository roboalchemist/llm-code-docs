# Source: https://docs.datadoghq.com/cloudcraft/api/users.md

# Source: https://docs.datadoghq.com/account_management/users.md

---
title: User Management
description: Add or remove users in your organization. Modify user roles.
breadcrumbs: Docs > Account Management > User Management
source_url: https://docs.datadoghq.com/users/index.html
---

# User Management

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
The Datadog for Government site only supports SAML login.
{% /alert %}

{% /callout %}

Datadog's **User** tab in **Organization Settings** allows you to manage your users and their associated roles. Switch between list and grid views by clicking **List View** or **Grid View** on the right.

## Add new members and manage invites{% #add-new-members-and-manage-invites %}

To add members to your organization:

1. Go to the Organization Settings page, then click the **Users** tab.
1. Click **Invite Users** in the upper right corner of the page.
1. Enter the email address of the user you wish to invite to your Datadog account.
1. Assign one or more [user roles](https://docs.datadoghq.com/account_management/users/default_roles/) to the users. **Note**: Users with the Invite User permission can invite a user to any role they have themselves. Users with both the Invite User and Access Management permissions can invite a user to any role.
1. Click **Send Invites**.

The new user receives an email with a link to log in. This link is valid for 48 hours. The user is marked with the status `Invite Pending` until they log in. To cancel their invite before they log in, click the **Delete Invite** button on the right of the user line in list view, or on the user box in grid view.

To resend an invite in list view, click the user to open the user side panel and click **Resend Invite**. Or in grid view, hover over the user box and click **Resend Invite**.

## Edit a user's roles{% #edit-a-users-roles %}

Only users with the User Access Management permission, such as users with the Datadog Admin Role, can change another user's role.

To edit a user's roles:

1. Go to the **Users** tab of **Organization Settings**.
1. Select the **Edit** button on the right of the user line.
1. Select the new [user roles](https://docs.datadoghq.com/account_management/rbac/) for this user, or click the 'X' next to an existing role to remove it.
1. **Save** the new settings.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/users/user_role_update.4a37397e24bf18f2e6f0bcf76ebf5d30.png?auto=format"
   alt="User role update" /%}

To discover all of the roles available and how to create custom ones, see the [Role Based Access Control documentation](https://docs.datadoghq.com/account_management/rbac/).

## Edit a user's login methods{% #edit-a-users-login-methods %}

Only users with the User Access Management permission, such as users with the Datadog Admin Role, can change another user's login methods.

Default login methods for an organization can be set through the Login Methods page. There you can allow or disallow all users in your organization to use a Datadog username and password, to sign in with Google, or to sign in with SAML. In User Management you can override on a per-user basis to allow a specific user to use one method or multiple methods. This is helpful in circumstances where you want all users to use SAML but need to enable a set of users to log in with username and password in an emergency.

To edit a user's login methods:

1. Go to the **Users** tab of **Organization Settings**.
1. Click **Edit** on the right of the user line.
1. Switch the toggle beside **Override Default Login Methods** to enable or disable overrides for the user.
1. If enabling overrides, choose a set of login methods that the user can use to access Datadog. This can be a single option or all options that are configured for your organization.
1. Click **Save**.

**Note**: Overrides can be set only to valid login methods. If you have not configured SAML, you cannot choose that login method as an override for a user.

## Disable existing members{% #disable-existing-members %}

Only users with the Access Management permission, such as users with the Datadog Admin Role, can disable members. You cannot permanently remove users, as they might have authored dashboards or monitors, and their user ID is used to keep a record of their actions. When a user is disabled, any application keys they had generated are automatically revoked.

1. Go to the **Users** tab of **Organization Settings**.
1. Select the **Edit** button on the right of the user line.
1. Click on the **Disable** toggle.
1. **Save** the changes.
1. Confirm the action.

**Note**: By default, disabled users are filtered out from the list of users in the User Management Page. If you have the correct permissions, you can filter by users with the status `Disabled` and re-enable them.

## Further Reading{% #further-reading %}

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
- [Learn how to create, update and delete a Role](https://docs.datadoghq.com/account_management/rbac/)
- [Discover the list of permissions available](https://docs.datadoghq.com/account_management/rbac/permissions/)
- [Manage your users with the USER API](https://docs.datadoghq.com/api/v1/users/)
