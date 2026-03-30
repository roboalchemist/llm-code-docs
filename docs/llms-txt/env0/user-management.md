# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/user-management.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Users

> Add, invite, and manage users in your env zero organization with SSO and identity provider support

## Create users in env zero

When a new user logs into env zero for the first time, either by starting a trial or accepting an invitation to join an existing Organization, a user profile is created. Profile details are taken from the Google, Github, BitBucket, or Microsoft account that was used to log in. Users are identified by their email address.

<Info>
  **Single Sign-On (SSO)**

  env zero supports Single Sign-On with Azure Active Directory (Microsoft Entra ID) and SAML 2.0 for enterprise authentication. With SSO enabled, users authenticate through your identity provider and are automatically provisioned in env zero.

  You can configure SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for setup instructions.

  For automated user provisioning and deprovisioning that doesn't depend on login events, see [SCIM Provisioning](/guides/sso-integrations/scim-provisioning).
</Info>

When a user profile is created, a Default Organization is set up for them, and they become its administrator. This Default Organization is used for testing and evaluation. Users can be part of multiple [Organizations](/guides/admin-guide/organizations) and can also accept invitations to join other organizations.

## Manage Organization Users

Organization Administrators have the capability to oversee user management within the organization. This includes assigning users to roles directly or via teams, offering flexibility in how permissions are distributed across the organization, project, and environment.

To access the user management interface, navigate to the Users screen located under the Settings tab. This area is exclusively available to Organization Administrators.

<Info>
  **Note**

  Selecting an Active Project changes the context of the Users screen to project-specific user management, rather than organization-wide settings.
</Info>

Organization Administrators can modify roles, invite new users, or remove existing users from the organization. Direct changes to a user's organization role or their removal from the organization are actions restricted to Organization Administrators only.

## Invite Users to an Organization

Any Organization Administrator can invite other users to join their organization.

Click Invite User, enter a valid email address for the invited user, and then click Send Invitation.

A user can be invited to an organization whether or not they have an active env zero profile. A user is created in env zero for the invitee (if they are not already a user). The invitation email is sent to the user at their email address and the user status is set to Invited.

If the user is new to env zero, a user profile is created when they log in for the first time.

The admin can track the user status in the Users screen, and see when the user has accepted the invitation and joined the organization.

Organization Administrators can revoke an invitation to a user at any time. Click on the garbage can icon next to the user in the Users tab. Once revoked, the user disappears from the list and they can no longer accept the invitation.

## Understanding Roles

env zero uses Role-Based Access Control (RBAC) to manage permissions. Users can be assigned roles at the organization, project, or environment level.

**Organization-level roles** include:

* **[Organization User](/guides/admin-guide/user-role-and-team-management/default-roles#organization-user)** - Basic access to view organization resources
* **[Organization Admin](/guides/admin-guide/user-role-and-team-management/default-roles#organization-admin)** - Full administrative access across the entire organization

For detailed information about all available roles and their permissions, see [Default Roles](/guides/admin-guide/user-role-and-team-management/default-roles). You can also [create custom roles](/guides/admin-guide/user-role-and-team-management/custom-roles) tailored to your organization's needs.

## Project Users

In order to have access to a project, users need to be associated with it.\
Each user associated with a project has a specific project Role assigned to them.

Managing access to a project can be done in 2 ways:

1. **Managing a team's access to a project:**\
   If a user is a member of a team that is assigned to the project, the team's role will cascade onto the user. See the [Teams section](/guides/admin-guide/user-role-and-team-management/teams/#managing-team-access-to-a-project) for more information.

2. **Manage a user's access directly:**\
   A user can also be given a specific role in a project outside of a team. This can be used to give a user additional permissions beyond those assigned by their team, or when the user is not part of any team. Managing users this way requires the Administrator role for that project.\
   Go to Project Settings and then select the Users tab. There you'll see a list of all the organization users. Select users from this list to assign to this project. For each, set a role within the specific project.

If the user has multiple roles that originate from their teams or from their specific role for the project, the highest role will be the one to take effect.

## Project Roles

**Project-level roles** include:

* **[Project Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#project-viewer)** - Read-only access to project resources
* **[Project Planner](/guides/admin-guide/user-role-and-team-management/default-roles#project-planner)** - Can plan deployments but requires approval
* **[Project Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#project-deployer)** - Can deploy and manage environments
* **[Project Admin](/guides/admin-guide/user-role-and-team-management/default-roles#project-admin)** - Full administrative access to the project

Organization Admins automatically have admin access to all projects. For complete details about project roles and their permissions, see [Default Roles](/guides/admin-guide/user-role-and-team-management/default-roles). You can also [create custom roles](/guides/admin-guide/user-role-and-team-management/custom-roles) with specific permissions.

## Environment Access

Users can be assigned roles at the environment level for granular access control. **Environment-level roles** include:

* **[Environment Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-viewer)** - Read-only access to a specific environment
* **[Environment Planner](/guides/admin-guide/user-role-and-team-management/default-roles#environment-planner)** - Can plan changes but requires approval
* **[Environment Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-deployer)** - Can deploy changes to the environment
* **[Environment Admin](/guides/admin-guide/user-role-and-team-management/default-roles#environment-admin)** - Full administrative access to the environment

You can assign different permission levels at different scopes. For example, a user might have Viewer access at the project level but Admin access to a specific environment within that project.

For complete details about environment roles and permissions, see [Default Roles](/guides/admin-guide/user-role-and-team-management/default-roles). To create roles with specific permissions, see [Custom Roles](/guides/admin-guide/user-role-and-team-management/custom-roles).

## Next Steps

Now that you understand user management, continue with team management and access control:

<CardGroup cols={2}>
  <Card title="Manage Teams" icon="users" href="/guides/admin-guide/user-role-and-team-management/teams">
    Learn how to create and manage teams to simplify permission management
  </Card>

  <Card title="Default Roles" icon="shield-check" href="/guides/admin-guide/user-role-and-team-management/default-roles">
    Learn about built-in roles and their permissions at organization, project, and environment levels
  </Card>

  <Card title="Custom Roles" icon="settings" href="/guides/admin-guide/user-role-and-team-management/custom-roles">
    Create and manage custom roles with tailored permissions
  </Card>

  <Card title="Assigning Roles" icon="user-plus" href="/guides/admin-guide/user-role-and-team-management/role-assignment">
    Step-by-step guides for assigning roles to users and teams
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
