# Source: https://docs.anyscale.com/administration/organization/projects.md

# What is a project?

[View Markdown](/administration/organization/projects.md)

# What is a project?

An Anyscale project is an isolated collection of resources and assets within an Anyscale cloud. Use projects to isolate developer teams, separate environments, and organize resources in the same Anyscale cloud.

Projects offer the most granular control to resources in Anyscale. You set permissions for users at the project level for all workspaces, jobs, and services in that project. See [Project roles](/administration/organization/permissions.md#projects).

When you configure a new Anyscale cloud, Anyscale creates a default project named `default` in the cloud.

note

Project names are unique within a cloud, but you can reuse a project name in multiple clouds in the same organization. When launching a workload, ensure you're using the correct cloud and project name.

## Private vs. public projects[​](#private-vs-public-projects "Direct link to Private vs. public projects")

Anyscale recommends using private projects to manage access to resources.

note

In public projects, all cloud users have implicit write permissions. To enforce read-only access, convert the project to private.

The following table describes public and private projects:

| Project type | Description                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Public       | All users with access to the containing cloud can access resources in the project with write permissions. Only users with explicitly granted access appear when reviewing permissions for the project. |
| Private      | Only users with explicit privileges on a project can view or interact with the project.                                                                                                                |

## Create a project[​](#create-a-project "Direct link to Create a project")

Any collaborator in a cloud can create a project.

To create a new project in the Anyscale console, do the following:

1. Click your user icon.
2. Select **Projects**.
3. Click **+ Create**.
4. Enter a name for the project.
   <!-- -->
   * Project names must be unique within a cloud, but don't need to be unique across an organization.
5. (Optional) To create a public project, select **Allow all users in this cloud to view and edit this project**.
6. Click **Create**.

You are an owner for projects you create.

## Manage projects[​](#manage-projects "Direct link to Manage projects")

Project owners can perform the following tasks:

* Add users to a project.
* Manage user permissions for the project.
* Convert a project between private and public.
* Delete a project.

## Specify a cloud when creating clusters[​](#specify-a-cloud-when-creating-clusters "Direct link to Specify a cloud when creating clusters")

Each cloud has a public default project that Anyscale creates during cloud creation. By default, when a user creates a cluster without specifying a project, Anyscale creates it in a default public project, making it accessible to all users with access to the associated cloud.

The Anyscale console shows your active cloud and project in the header. You can select a new cloud or project to change the active scope for new clusters created with the console.

Users can specify a project name in job and service CLI commands or with the `ANYSCALE_PROJECT_NAME` environment variable.
