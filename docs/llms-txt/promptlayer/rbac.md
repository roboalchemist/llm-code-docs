# Source: https://docs.promptlayer.com/why-promptlayer/rbac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# RBAC

**Role-based Access Control (RBAC)** provides fine-grained permission management for your workspaces. With RBAC enabled, you can define roles at the organization level and apply them to workspace members, giving you precise control over who can do what in each workspace.

## How RBAC Works

RBAC operates on a simple but powerful principle: **roles are defined at the organization level, but applied at the workspace level**. This means you can create a set of roles once for your organization and reuse them across all your workspaces, while still maintaining workspace-specific access control.

### Role Definition (Organization Level)

Roles belong to your organization and can be used across all workspaces. You have two options:

* **Default Roles**: System-provided roles available to all organizations (`Contributor`, `Publisher`, `Developer`, `Admin`)
* **Custom Roles**: Organization-specific roles you create to match your team's needs

Each role consists of a name and a set of permissions that define what actions that role allows.

### Role Application (Workspace Level)

When you assign roles to workspace members, you're granting them specific permissions within that workspace. A user can have different roles in different workspaces, and can even have multiple roles in the same workspace. When a user has multiple roles, their effective permissions are the combination of all permissions from their assigned roles.

For example, if Alice has both `Contributor` and `Publisher` roles in Workspace A, she can edit prompts and deploy them to production. But if she only has the `Contributor` role in Workspace B, she can edit prompts there but cannot deploy them.

## Default Roles

<img src="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=41bca5cc969522fbcfe3f4fea5793daa" alt="RBAC Roles" data-og-width="2092" width="2092" data-og-height="628" height="628" data-path="images/rbac-roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=280&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=50e98f544d7bea83721cc90e59069c21 280w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=560&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=659ab9e7d886e9177bd29f296341d913 560w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=840&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=d6c15c2d6440c5851f80b25ddbc8b2b3 840w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=1100&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=f753c88be9011ebc5a0bc44b811ae600 1100w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=1650&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=14896253da69af195154462771809d3f 1650w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-roles.png?w=2500&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=de49ad4209df1b44f64ef6be3b8b7a30 2500w" />

PromptLayer provides four default roles that cover most common use cases:

### Contributor

**What they can do**: Create and edit content

* **Prompt templates and versions**: Create, update, rename, delete, move, and duplicate prompt templates and versions
* **Workflows**: Create, update, rename, delete, move, and duplicate workflows and workflow versions
* **Datasets**: Create, update, rename, delete, move, and duplicate datasets and dataset groups
* **Reports**: Create, update, rename, delete, move, and duplicate reports and evaluations
* **Metadata**: Edit metadata associated with requests and entities

**Best for**: Team members who need to create and iterate on prompts, workflows, and evaluations, but don't need to deploy changes to production.

### Publisher

**What they can do**: Deploy changes to production

* Create and manage prompt labels
* Deploy prompt changes through changelogs
* Create and manage workflow labels
* Move labels between versions

**Best for**: Team members who need to deploy changes to production. Typically combined with `Contributor` for users who need both editing and deployment capabilities.

### Developer

**What they can do**: Manage API access

* Create, view, and delete API keys

**Best for**: Developers who need to manage API keys for programmatic access to your prompts and workflows.

### Admin

**What they can do**: Everything

* All permissions from other roles
* Manage workspace member roles and permissions
* Approve protected label changes
* Full administrative access

**Best for**: Workspace administrators who need complete control over the workspace.

<Warning color="yellow">
  Users with the `Admin` role can perform destructive workspace-wide actions,
  including inviting and removing other members from the workspace, even other
  admins. Grant this role only to trusted team members who need full
  administrative control.
</Warning>

## Custom Roles

<img src="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=659b2c462ca59aaa50373399891bf5f3" alt="Create Custom Role" data-og-width="1176" width="1176" data-og-height="1352" height="1352" data-path="images/rbac-create-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=280&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=bdb37598bf23154606d33ab72e621373 280w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=560&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=25692cffcd905d5ecd28449ea403691f 560w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=840&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=f6dd73e79baea7125f5bae2e106c1635 840w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=1100&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=f92ff77d9a4a9a1a33fd10ee7ba922a1 1100w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=1650&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=18b57fb622421ea7faf38cb874e04d72 1650w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-create-role.png?w=2500&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=6e7d73a247a2bb76a2ea1064914590e7 2500w" />

Beyond the default roles, you can create custom roles tailored to your organization's specific needs. Custom roles are defined at the organization level and can be reused across all workspaces.

Only organization owners can create custom roles. When creating a custom role, you select which permissions to include, allowing you to create roles that match your team's workflow exactly. For example, you might create a "QA Tester" role that can only edit reports and datasets, or a "Deployment Manager" role that combines `Publisher` and `Developer` permissions.

## Permissions

RBAC uses fine-grained permissions that control specific actions:

* **`PROMPT_EDIT`**: Edit prompt templates, create versions, modify metadata
* **`PROMPT_DEPLOY`**: Create labels, deploy changes, move labels between versions
* **`WORKFLOW_EDIT`**: Edit workflows, create versions, modify structure
* **`WORKFLOW_DEPLOY`**: Create workflow labels, deploy workflow changes
* **`DATASET_EDIT`**: Create and manage datasets and dataset groups
* **`REPORT_EDIT`**: Create, edit, and run reports and evaluations
* **`METADATA_EDIT`**: Edit metadata associated with requests
* **`MANAGE_API_KEYS`**: Create and delete API keys
* **`ADMIN`**: Full administrative access, including managing member roles

<Warning color="yellow">
  The `ADMIN` permission grants full administrative access and allows users to
  perform destructive workspace-wide actions, including inviting and removing
  other members from the workspace, even other admins. Grant this permission
  only to trusted team members who need full administrative control.
</Warning>

## Enabling RBAC

RBAC is enabled per organization. When RBAC is disabled, all workspace members receive default permissions (all permissions except `ADMIN`) automatically. When RBAC is enabled, workspace members have no permissions by default and must be explicitly assigned roles to gain access.

This secure-by-default approach ensures that when RBAC is enabled, users only get the permissions they need, following the principle of least privilege.

## Managing Roles

Users with the `ADMIN` permission in a workspace can assign roles to members of that workspace. Organization owners can assign roles to members in any workspace within their organization.

To manage a member's roles:

1. Go to your organization settings
2. Select your organization
3. Navigate to Workspaces
4. Select the workspace
5. Click the three dots menu next to the member
6. Choose "Manage roles"

<img src="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=bde48f21be15ded9880036a5575d16b2" alt="Manage Roles" data-og-width="2116" width="2116" data-og-height="976" height="976" data-path="images/rbac-manage-roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=280&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=d45d13353503dd91c3ea4eb41c3377ce 280w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=560&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=51eec05ecb5c0dc4d788302c1424fc69 560w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=840&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=b2956f2a6f76e0fc4753c564ea66255b 840w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=1100&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=cda68bd3688fceceeba38a4d6c4a8eac 1100w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=1650&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=39d6738b333e4bdc0aa188806c14c40a 1650w, https://mintcdn.com/promptlayer/dtjmcYBF4LTyu-O-/images/rbac-manage-roles.png?w=2500&fit=max&auto=format&n=dtjmcYBF4LTyu-O-&q=85&s=59634094c67bca8a6fef5ebf7020e2ef 2500w" />

When assigning roles, remember that:

* Roles are assigned to workspace members (not directly to users)
* Effective permissions are the union of all permissions from assigned roles
* Role assignments are workspace-specific

## Best Practices

* **Start with default roles**: The default roles cover most common scenarios. Use them before creating custom roles.
* **Follow least privilege**: Only grant the minimum permissions needed for each team member to do their job.
* **Combine roles strategically**: Assign multiple roles when users need permissions from different roles (e.g., `Contributor` + `Publisher` for someone who edits and deploys).
* **Review regularly**: Periodically review role assignments to ensure they still match your team's needs as roles and responsibilities evolve.
* **Use custom roles thoughtfully**: Create custom roles when you have a recurring pattern that doesn't fit the default roles, not for one-off cases.
