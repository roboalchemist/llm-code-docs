# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/default-roles.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Default Roles

> Built-in default roles and their permissions at organization, project, and environment levels in env zero

Default roles are built-in, non-editable roles that come with every env zero organization. These roles provide standard permission sets for common use cases and cannot be modified or deleted.

## Organization-Level Default Roles

Organization roles apply across the entire organization and cascade down to all projects (including sub-projects) and environments.

### Organization User

The basic role for organization members. Provides:

* View organization variables, templates, and modules
* View modules from the private module registry
* View providers from the private provider registry

This is the default role assigned when a custom role is deleted from a user at the organization level.

### Organization Admin

Full administrative access to the organization. Includes all available permissions across the platform, including:

* All [Organization User](#organization-user) permissions
* Edit organization settings and variables
* Create and edit templates, modules, and providers
* Create and edit custom roles
* View and edit dashboards
* View audit logs
* Manage billing information
* Move environments between projects
* Manage credentials and VCS connections
* All project and environment permissions

## Project-Level Default Roles

Project roles apply to specific projects and cascade down to:

* All sub-projects within that project
* All environments within the project and its sub-projects

### Project Viewer

Read-only access to project resources. Provides:

* All [Organization User](#organization-user) permissions
* View project settings, templates, variables, and environments
* Read Terraform state files
* View drift causes

### Project Planner

Can create and plan deployments but cannot apply changes. Provides:

* All [Project Viewer](#project-viewer) permissions
* Run plans (create environments, redeploy, destroy - requires approval)

### Project Deployer

Can deploy and manage environments. Provides:

* All [Project Planner](#project-planner) permissions
* Run applies (deploy without requiring approval)
* Edit environment settings
* Write to Terraform state files
* Abort running deployments

### Project Admin

Full administrative access to the project. Provides:

* All [Project Deployer](#project-deployer) permissions
* Edit project settings and variables
* Manage project templates
* Archive environments
* Lock/unlock environments
* Override max TTL settings
* Create cross-project environments
* Force unlock workspaces
* Create new projects
* Assign roles on environments
* Create VCS environments
* Edit VCS environment settings
* Import environments
* Manage credentials and VCS connections

## Environment-Level Default Roles

Environment roles apply to specific environments only.

### Environment Viewer

Read-only access to a specific environment. Provides:

* All [Organization User](#organization-user) permissions
* View environment details, settings, variables, and logs
* Read Terraform state files
* View drift causes

### Environment Planner

Can plan changes to a specific environment. Provides:

* All [Environment Viewer](#environment-viewer) permissions
* Run plans (requires approval)

### Environment Deployer

Can deploy changes to a specific environment. Provides:

* All [Environment Planner](#environment-planner) permissions
* Run applies (deploy without requiring approval)
* Edit environment settings
* Write to Terraform state files
* Abort running deployments

### Environment Admin

Full administrative access to a specific environment. Provides:

* All [Environment Deployer](#environment-deployer) permissions
* Archive the environment
* Lock/unlock the environment
* Override max TTL settings
* Force unlock workspace
* Assign roles on the environment
* Edit allow remote apply settings

## Next Steps

<CardGroup cols={2}>
  <Card title="Manage Users" icon="user" href="/guides/admin-guide/user-role-and-team-management/user-management">
    Learn how to invite and manage users in your organization
  </Card>

  <Card title="Manage Teams" icon="users" href="/guides/admin-guide/user-role-and-team-management/teams">
    Learn how to create and manage teams to simplify permission management
  </Card>

  <Card title="Custom Roles" icon="settings" href="/guides/admin-guide/user-role-and-team-management/custom-roles">
    Create and manage custom roles with tailored permissions
  </Card>

  <Card title="Assigning Roles" icon="user-plus" href="/guides/admin-guide/user-role-and-team-management/role-assignment">
    Step-by-step guides for assigning these roles to users and teams
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
