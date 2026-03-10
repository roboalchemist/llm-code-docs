# Source: https://render.com/docs/enterprise-orgs.md

# Enterprise Organizations — Manage users and services across multiple workspaces.

With a Render Enterprise plan, you can manage all of your team's users, workspaces, and services in a single *organization* (or *org*):

[image: Diagram of a Render Enterprise org]

Each organization member can belong to any combination of workspaces, based on which services they need to access. You can also add [guests](#member-types) that receive access to a single workspace.

You can integrate your org with your identity provider (IdP) to enable [SAML single sign-on](saml-sso) (SSO), along with member management via SCIM.

## Creating an org

As part of setting up your Enterprise account, the Render team works with you directly to create your organization. If you have any existing Render workspaces, we'll help you transfer them into your org for centralized management.

Each member of each transferred workspace becomes a member of your org.

## Adding workspaces

### Creating a new workspace

> Only org members with the *Enterprise Owner* role can create new workspaces in the org.

1. From your organization's Workspaces page in the [Render Dashboard](https://dashboard.render.com), click *+ New Workspace*.

2. Provide a name for the workspace.

3. Set the workspace's privacy setting to *Public* or *Invite-only*.

   - *Public*: Any org member can add themselves to the workspace.
   - *Invite-only*: Only admins of the workspace can invite other org members.

4. Click *Create Workspace*.

You're all set! Render creates the workspace and adds you as its first admin. You can immediately start creating services and inviting members.

### Transferring an existing workspace

As part of creating your org, the Render team helps you transfer any of your existing workspaces into it.

If you later need to transfer a different workspace into your org, please [reach out to our support team](https://dashboard.render.com?contact-support) in the Render Dashboard.

## Access management

### The Enterprise Owner role

During org creation, the Render team assigns at least one member of your org the *Enterprise Owner* role. Members with this role can do the following:

- Manage all org-level settings, such as integrating your IdP for SSO and SCIM
- Create new workspaces in the org
- Add or remove the Enterprise Owner role from other org members
- Add themselves to any workspace as an admin
  - Enterprise Owners are not _automatically_ added to any workspaces in the org.

Other org members do not have an organization-level role or associated permissions. Workspace-level permissions depend on a [member's role within each workspace](team-members#member-roles).

### Member types

> *This section assumes you've enabled [*SAML SSO*](saml-sso) for your org.*
>
> If you _haven't_ enabled SSO, workspace admins can invite any Render user to any org-managed workspace. These users automatically become standard members of the org.

| Member Type | Description |
| --- | --- |
| *Standard member* | Any user with an email address managed by your IdP. Standard members automatically join your org the first time they log in to Render via SSO. After joining, they can then add themselves to any public workspace in the org and receive invitations to invite-only workspaces. You can optionally manage standard members via [SCIM](saml-sso#member-management-setup-scim). |
| *Guest* | Any user with an email address that _isn't_ managed by your IdP (which prevents them from logging in via SSO). Invite guests to collaborate with individuals outside your company, such as consultants. Workspace admins can invite guests to individual workspaces in the org. Guests can't access any org resources _except_ those in the single workspace they're invited to. Guests are billed identically to standard members. |

### Per-workspace access

Each workspace in an org has one of two privacy settings: *public* or *invite-only*. Newly added workspaces are invite-only by default. Workspace admins can change a workspace's privacy setting from the workspace's Settings page in the Render Dashboard.

- Standard org members can add themselves to any public workspace (guests cannot).
- Invite-only workspaces require an invitation from a workspace admin.

When you add an org member to a workspace, you can assign them any [member role.](team-members#member-roles)

#### The Billing role

> *This role is available only for Enterprise orgs.*

When you add an org member to an individual workspace, you can assign them the *Billing* role:

[image: Assigning the Billing role to an org member]

Members with this role can view and manage the workspace's billing and payment settings. They also receive _view-only_ access to non-sensitive details of the workspace's resources (such as service names).

If an org member has the *Billing* role in _every_ org-managed workspace they belong to, your org is _not_ charged for their seat. See three example scenarios below:

| Role in Workspace A | Role in Workspace B | Org charged for seat? |
| --- | --- | --- |
| Billing | Billing | No |
| Billing | None (not assigned to workspace) | No |
| Billing | Developer | *Yes* |

Each Enterprise org supports up to two total members with the *Billing* role.