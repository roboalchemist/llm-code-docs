# Source: https://docs.envzero.com/guides/admin-guide/env-zero-projects.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating & Managing Projects

> Organize environments, teams, and resources with projects and sub-projects for access control in env zero

## What are Projects?

Projects in env zero provide granular access control to environments and serve as organizational containers for your infrastructure deployments. Every environment in env zero exists under a project, and users are given access on a per-project basis.

Projects are also useful for managing multiple cloud accounts within a single organization and separating different environments (like dev, staging, production) with their own access rights and policies.

## Project Hierarchy

### Main Projects

Projects are created within an [Organization](/guides/admin-guide/organizations). Every new organization starts with a Default Organization Project, and additional projects can be added as needed.

### Sub Projects

As your organization's IaC use grows, you might find that a single hierarchy level is insufficient. Sub Projects help you better organize your projects, environments, and configurations within your organization.

Sub Projects are nested within other projects and can have their own environments, templates, variables, and user roles. Each sub project may have its own environments, templates, variables, etc., while users may be assigned different roles for different projects in the hierarchy.

## Working with Projects

### Active Project Context

Users typically work in the context of an Active Project, but can also work at the Organization level:

* **Project Context:** Shows only templates and environments associated with the current project
* **Organization Context:** Shows all projects the user has access to
* **Navigation:** Switch between contexts using the organization/project selector in the upper left

### Creating Projects

To create a new project:

1. Navigate to Organization context (no active project selected)
2. Select the Projects tab
3. Click "Create New Project"
4. Enter project name and description
5. Associate users and templates as needed

### Managing Templates

Only templates associated with the current project can be used to create environments:

* Select the Templates tab and click "Manage Templates"
* Choose from available organization templates
* Save associations to enable template usage

## Sub Project Management

### Navigation

* **Projects Page:** Shows parent projects; clicking navigates to sub projects or environments
* **Projects Menu:** Displays hierarchy with arrows for projects containing sub projects
* **Hover Navigation:** Hover over projects to see sub projects in the menu

### Creating Sub Projects

To create a sub project:

1. Hover over the desired parent project in the left navigation
2. Click the plus icon that appears
3. Enter sub project details

### Moving Sub Projects

Use the Move button in Project Settings to relocate sub projects:

* Select target project from the popup
* The project and its sub projects will be moved together
* Maintains hierarchy and relationships

## Access Control & Permissions

### Role-Based Access

Each sub project inherits roles from its parent project up to the root project. Users can navigate through the project hierarchy based on their permissions:

* **View Project Permission:** Required to access and navigate to projects
* **Inherited Permissions:** Sub projects inherit parent project roles
* **Granular Control:** Different roles for different projects in the hierarchy

### User Management

For detailed user access control management, see [Users & Roles](/guides/admin-guide/user-role-and-team-management/user-management/#project-users).

## Project Configuration

### Variables Inheritance

* **Variables:** Inherited from parent projects to sub projects
* **Templates:** Only affect the project where they're configured
* **Policies:** Project-specific, don't affect sub projects
* **Notifications:** Configured per project only
* **Costs:** Each project tracks only its own environments

### Project Identification

Find your project ID for:

* **Terraform Provider:** Use in env zero resource definitions
* **API Calls:** Reference in REST API requests
* **Integration:** Connect with external tools

Locate the ID under the General tab in Project Settings.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/4cf84ec-project_settings.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=9861f1931f97ec9fc2fa4fff83e2946a" alt="Project settings showing project ID location" width="2778" height="1386" data-path="images/guides/admin-guide/4cf84ec-project_settings.png" />
</Frame>

## Best Practices

### Project Organization

* **Environment Separation:** Use projects to separate dev, staging, and production
* **Team Structure:** Align projects with team responsibilities
* **Resource Management:** Group related environments and resources
* **Access Control:** Implement appropriate permissions per project

### Sub Project Strategy

* **Hierarchical Organization:** Use sub projects for complex organizational structures
* **Permission Inheritance:** Leverage inherited roles for simplified management
* **Resource Isolation:** Keep related environments grouped together
* **Scalability:** Plan for growth with flexible project hierarchies

This comprehensive project management system gives you the flexibility to organize your infrastructure deployments at any scale while maintaining proper access control and resource isolation.

Built with [Mintlify](https://mintlify.com).
