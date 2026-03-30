# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/rbac.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Role-Based Access Control (RBAC)

> Manage permissions for users and teams with role-based access control (RBAC) in env zero

env zero's Role-Based Access Control (RBAC) system allows you to manage permissions for users and teams across your organization, projects, and environments. This comprehensive access control system ensures that team members have the appropriate level of access to perform their responsibilities while maintaining security and governance.

## Understanding Roles in env zero

env zero provides two types of roles to manage access control within your organization:

### Default Roles vs. Custom Roles

**[Default Roles](/guides/admin-guide/user-role-and-team-management/default-roles)** are built-in, non-editable roles that come with every env zero organization. These roles provide standard permission sets for common use cases and cannot be modified or deleted. They are designed to cover the most common access patterns and ensure consistent security practices across organizations.

**[Custom Roles](/guides/admin-guide/user-role-and-team-management/custom-roles)** allow you to create tailored permission sets that match your organization's specific needs. These roles can be created, edited, and deleted as needed, giving you full flexibility to define exactly what permissions users should have.

### Role Assignment Levels and Inheritance

Roles can be assigned at three levels in env zero, and permissions cascade down the hierarchy:

* **Organization Level**: Roles assigned at the organization level apply to the entire organization and cascade down to all projects (including sub-projects) and environments within the organization.
* **Project Level**: Roles assigned at the project level apply to that specific project and cascade down to:
  * All sub-projects within that project
  * All environments within the project and its sub-projects
* **Environment Level**: Roles assigned at the environment level apply only to that specific environment.

<Info>
  **Permission Cascading**

  env zero's RBAC is cascading, top to bottom. If a user or team has a permission at the organization level, they have that permission on every project and environment in the organization. Similarly, project-level permissions apply to all sub-projects and environments within that project.

  However, this does not work in reverse - project permissions only apply to that specific project and its sub-projects, not to the parent project or organization.
</Info>

## RBAC Documentation

<CardGroup cols={2}>
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
