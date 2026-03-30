# Source: https://docs.gitguardian.com/platform/collaboration-and-sharing/users.md

# Add and manage users

> Invite and manage users in your GitGuardian workspace via email, SSO Just-In-Time provisioning, or SCIM.

:::info
In addition to inviting users via email or SSO Just-In-Time (JIT) provisioning, you can now automatically provision users via SCIM if your workspace has SCIM enabled. When SCIM is configured, users added in your Identity Provider (IdP) will be automatically created in your GitGuardian workspace.

Learn more and see setup instructions in the [SCIM documentation](../enterprise-administration/scim-configuration).
:::

## Adding new users

### Inviting via email

As a workspace Owner or Manager, you can invite via email other users to join your GitGuardian workspace.

1. Navigate to Settings > User management > [Members](https://dashboard.gitguardian.com/settings/user/members)
2. Simply submit the email address of the person you want to invite. If you are under a Business plan, you will be able to specify the teams of your new invitee.
3. The invited user will receive and email with an invitation link. If you have performed an SSO integration, the invitation link will redirect to your dedicated SSO login URL.

![Invitation form](/img/platform/collaboration-and-sharing/invitation-via-email-form.png)

There is no limit to the number of users on your workspace.

### Pointing to SSO login URL

If you have configured SSO, you can simply let the Just-In-Time provisioning do the work.

1. Make sure the people you want to add to your GitGuardian workspace are part of the allowed IdP group
2. Point those people to the SSO login URL dedicated to your workspace. This URL is accessible by workspace Manager in the [Authentication settings section](https://dashboard.gitguardian.com/settings/workspace/auth/saml).

![SSO login url](/img/platform/enterprise-administration/sso_login_url.png)

### Manage pending invitations

Once invited, the new user appears in the "Pending" list in the [Members section](https://dashboard.gitguardian.com/settings/user/members) of your workspace. There, you can choose the access level they will be attributed upon sign up.

You can delete a pending invitation, which invalidates the sent invitation link.

## Access levels

Each user has its own user account and can be member of one or multiple workspaces.
Thus, user membership is handled at the workspace level. Each member is assigned a access level that defines its privileges on the workspace at stake.

| Action                                                                                                                             |       Owner        |      Manager       |       Member       |                           Restricted                           |
| :--------------------------------------------------------------------------------------------------------------------------------- | :----------------: | :----------------: | :----------------: | :------------------------------------------------------------: |
| Can access incidents and act on them according to their incident permissions (share, assign, resolve, ignore, export)              | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark:, only to incidents they are given access to |
| Can create/delete API personal access tokens                                                                                       | :white_check_mark: | :white_check_mark: | :white_check_mark: |           :white_check_mark:, only with `scan` scope           |
| Can create/delete API service accounts (Business only)                                                                             | :white_check_mark: | :white_check_mark: |        :x:         |                              :x:                               |
| Can launch historical scans                                                                                                        | :white_check_mark: | :white_check_mark: | :white_check_mark:, based on team perimeter assignments |   :x:                     |
| Can add/remove/change members                                                                                                      | :white_check_mark: | :white_check_mark: |        :x:         |                              :x:                               |
| Can join/leave/request access to teams                                                                                             | :white_check_mark: | :white_check_mark: | :white_check_mark: |                              :x:                               |
| Can see [workspace settings](../enterprise-administration/workspace-settings)                                                      | :white_check_mark: | :white_check_mark: | :white_check_mark: |                              :x:                               |
| Can change workspace settings (SSO, detection capabilities,...)                                                                    | :white_check_mark: | :white_check_mark: |        :x:         |                              :x:                               |
| Can configure integrations (VCS and notifiers)                                                                                     | :white_check_mark: | :white_check_mark: |        :x:         |                              :x:                               |
| Can access [analytics](../analytics/overview)                                                                                      | :white_check_mark: | :white_check_mark: | :white_check_mark:, only with `Full access` on the All-incidents team |        :x:         |
| Can delete workspace                                                                                                               | :white_check_mark: |        :x:         |        :x:         |                              :x:                               |
| Can change [secret occurrences grouping](../../internal-monitoring/detect/secrets-occurrences#grouping-of-occurrences-into-secret-incidents) | :white_check_mark: |        :x:         |        :x:         |                              :x:                               |

### Owner

- The Owner has unrestricted access and all rights over the entire workspace.
- Each workspace must have one and only one Owner.
- When the Owner deletes their user account, it also deletes their workspace and members.

### Manager

- A Manager has the same level of access as the Owner except they cannot delete the workspace.
- A Manager can manage workspace settings and fellow members of the workspace.
- A Manager can access all the incidents.

Managers are the people responsible for managing the GitGuardian workspace. These may be security or technology managers, depending on your own organization.

### Member

- A Member can view the workspace settings but cannot act on them.
- A Member can access the incidents.
- A Member can be part of teams.

Members are people in your organization (Developers, Ops, Security) that you want to collaborate to remediate incidents.

:::info
Memberships with Viewers have been migrated to access level Member with [`Can view`](./teams#define-their-incident-permissions) incident permissions on all the incidents.
:::

### Restricted

- A Restricted can only access a certain set of incidents defined by the Manager or the Member on an ad-hoc basis.
- A Restricted cannot be part of a team.
- A Restricted can list members and teams to assign or share incidents they have access to.

Restricted are typically people outside of your organization who you want to allow access only to very specific incidents.

#### Promote a Restricted to Member

When promoting a Restricted to Member access level:

1. They have read access to the workspace settings
2. They are able to request to join teams in the workspace

#### Demote a Member to Restricted

When demoting a Member (or a Manager) to Restricted access level:

1. They are removed from all the teams they belong to
2. Only incidents to which they are granted access to manually are accessible.
3. All open incidents they were assigned to are unassigned

:::info
The Restricted access level is only accessible to workspaces under the Business plan.
:::

## Delete or deactivate members

As a workspace Owner or Manager, you can remove or deactivate a member from the workspace. Deactivating a member temporarily restricts their access to the workspace without permanently deleting their account or data, allowing you to reactivate them later if needed. In contrast, removing a member permanently revokes their access and deletes their association with the workspace. However, note that the Owner of the workspace cannot be removed or deactivated by any user.

1. Navigate to Settings > User management > [Members](https://dashboard.gitguardian.com/settings/user/members)
2. To the right of the person's name, click the ![platform icon](/img/icons/three-dots-menu.svg) menu, then select Delete or Deactivate.
3. Confirm your action.

This person will instantly lose access to your workspace and all of its data. Personal access tokens belonging to that person will also be revoked.

![Removing a member](/img/platform/collaboration-and-sharing/removing-a-member.png)

## [Self-hosting] Access to the Admin Area

If you are using GitGuardian in a self-hosted environment, you will have access to the Admin Area for managing your system. For additional information, please refer to the [Admin Area User Management](/self-hosting/management/application-management/admin-area) page.
