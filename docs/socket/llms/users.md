# Source: https://docs.socket.dev/docs/users.md

# Users

# User Roles and Permissions in Socket

## Overview

Every user of Socket is associated with an email and may be part of one or more GitHub organizations. The organizations a user is associated with can be viewed in the dashboard. Adding a GitHub organization to a user is done by installing the Socket for GitHub application on a repository in that GitHub organization. Users can be invited to an organization by using the People tab in that organization's dashboard. Pending and existing users can be managed from the People tab as well.

## User Roles and Permissions

## Permissions Matrix

| Permission                     | Owner | Admin | Member | Contributor |
| ------------------------------ | ----- | ----- | ------ | ----------- |
| View Overview                  | ✅     | ✅     | ✅      | ✅           |
| View Org Alerts (new)          | ✅     | ✅     | ✅      | ✅           |
| View Org Alerts (old)          | ✅     | ✅     | ✅      | ✅           |
| View Dependencies              | ✅     | ✅     | ✅      | ✅           |
| View Repositories              | ✅     | ✅     | ✅      | ✅           |
| View Labels                    | ✅     | ✅     | ✅      | ✅           |
| View Full Scans                | ✅     | ✅     | ✅      | ✅           |
| View Analytics                 | ✅     | ✅     | ✅      | ✅           |
| View People                    | ✅     | ✅     | ✅      | ✅           |
| View Threat Feed               | ✅     | ✅     | ✅      | ✅           |
| View Webhooks                  | ✅     | ✅     | ✅      | ✅           |
| View Label Security Policy     | ✅     | ✅     | ✅      | ❌           |
| View Security Policy           | ✅     | ✅     | ✅      | ❌           |
| View License Policy            | ✅     | ✅     | ✅      | ❌           |
| View API Tokens                | ✅     | ✅     | ✅      | ❌           |
| View Triage                    | ✅     | ✅     | ✅      | ❌           |
| View Triage note               | ✅     | ✅     | ✅      | ❌           |
| Add Triage Note                | ✅     | ✅     | ✅      | ❌           |
| Add Labels                     | ✅     | ✅     | ✅      | ❌           |
| Add Label to Repo              | ✅     | ✅     | ✅      | ❌           |
| Modify Triage                  | ✅     | ✅     | ✅      | ❌           |
| Modify Labels                  | ✅     | ✅     | ✅      | ❌           |
| Modify Label Security Policy   | ✅     | ✅     | ✅      | ❌           |
| Delete Repository              | ✅     | ✅     | ❌      | ❌           |
| Delete Full Scan               | ✅     | ✅     | ❌      | ❌           |
| View Org API Tokens            | ✅     | ✅     | ❌      | ❌           |
| View Integrations              | ✅     | ✅     | ❌      | ❌           |
| View General Settings          | ✅     | ✅     | ❌      | ❌           |
| View Github Settings           | ✅     | ✅     | ❌      | ❌           |
| View Billing                   | ✅     | ✅     | ❌      | ❌           |
| View Audit Log                 | ✅     | ✅     | ❌      | ❌           |
| View Security                  | ✅     | ✅     | ❌      | ❌           |
| Invite people to org           | ✅     | ✅     | ❌      | ❌           |
| Delete Invite                  | ✅     | ✅     | ❌      | ❌           |
| Change default invite level    | ✅     | ✅     | ❌      | ❌           |
| Modify Security Policy         | ✅     | ✅     | ❌      | ❌           |
| Modify License Policy          | ✅     | ✅     | ❌      | ❌           |
| Modify General Settings        | ✅     | ✅     | ❌      | ❌           |
| Modify Github Settings         | ✅     | ✅     | ❌      | ❌           |
| Modify Security SSO Connection | ✅     | ✅     | ❌      | ❌           |
| Modify Security SSO Options    | ✅     | ✅     | ❌      | ❌           |
| Create API Tokens              | ✅     | ✅     | ❌      | ❌           |
| Edit API Tokens                | ✅     | ✅     | ❌      | ❌           |
| Modify Webhooks                | ✅     | ✅     | ❌      | ❌           |
| Transfer Ownership             | ✅     | ❌     | ❌      | ❌           |

**Note**: Members can only read API tokens with the visibility set to "organization members".

### Owner

* **Permissions**: Full access to all repositories and the team, including billing, adding, or removing members.
* **Responsibilities**: Manages the entire organization and has the highest level of control.

### Administrator

* **Permissions**: Access to all repositories and the team, including billing, adding, or removing members.
* **Responsibilities**: Helps manage the organization and maintain its settings.

### Member

* **Permissions**: Add and edit specific repositories.
* **Responsibilities**: Collaborates on specific repositories assigned by the Admin or Owner.

### Contributor

* **Permissions**: Limited access to contribute code but no team-level access or permissions to change repo-level settings.
* **Responsibilities**: Contributes code to repositories but cannot manage settings or team members.

## Managing Users

* **Inviting Users**: Admins and Owners can invite new users by sending invitations via the People tab.
* **Pending Invitations**: View and manage pending user invitations in the People tab.
* **Existing Users**: Manage roles and permissions of existing users from the People tab.

## People Tab

![](https://files.readme.io/8ffa9e6-Screenshot_2024-07-02_at_5.15.09_PM.png)\
The People tab allows you to manage users, view pending invitations, and adjust user roles.

## SSO and Default Member Role

* **SSO Configuration**: Enable SAML Single Sign-On for organization members via an Identity Provider.
* **Default Member Role**: Set the default role (Member or Contributor) for new members signing in via SSO in the Settings tab.

### Settings Tab

![](https://files.readme.io/d2202a9-Screenshot_2024-07-02_at_5.14.47_PM.png)\
The Settings tab provides options for configuring [SSO](https://docs.socket.dev/docs/single-sign-on) and setting default member roles for new sign-ins.

By understanding and utilizing these roles and permissions, organizations can effectively manage their teams and maintain a secure and collaborative environment using Socket.

[dashboard]: https://socket.dev/dashboard