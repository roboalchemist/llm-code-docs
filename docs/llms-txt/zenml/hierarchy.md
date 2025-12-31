# Source: https://docs.zenml.io/pro/core-concepts/hierarchy.md

# Hierarchy

In ZenML Pro, there is a slightly different entity hierarchy as compared to the open-source ZenML\
framework. This document walks you through the key differences and new concepts that are only available for Pro users.

![Image showing the entity hierarchy in ZenML Pro](https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-50407b7a33c3a0583aa7cff1f7d1b991f627d40d%2Forg_hierarchy_pro.png?alt=media)

{% hint style="info" %}
s**Note**: Workspaces were previously called "Tenants" in earlier versions of ZenML Pro. We've updated the terminology to better reflect their role in organizing MLOps resources.
{% endhint %}

The image above shows the hierarchy of concepts in ZenML Pro.

* At the top level is your [**Organization**](https://docs.zenml.io/pro/core-concepts/organization). An organization is a collection of users, teams, and workspaces.
* Each [**Workspace**](https://docs.zenml.io/pro/core-concepts/workspaces) (formerly `tenant`) is an isolated deployment of a ZenML server (with some pro features). It contains multiple projects and their resources.
* Each [**Project**](https://docs.zenml.io/pro/core-concepts/projects) is a logical subdivision within a workspace that provides isolation for MLOps resources like pipelines, artifacts, and models. Projects have their own roles and access controls.
* [**Teams**](https://docs.zenml.io/pro/core-concepts/teams) are groups of users within an organization. They help in organizing users and managing access to resources at organization, workspace, and project levels.
* **Users** are single individual accounts on a ZenML Pro instance.
* [**Roles**](https://docs.zenml.io/pro/access-management/roles) exist at organization, workspace, and project levels to control what actions users can perform.

More details about each of these concepts are available in their linked pages below:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Organizations</strong></td><td>Learn about managing organizations in ZenML Pro.</td><td><a href="organization">organization</a></td><td><a href="https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-3f4630a906a4871d6d36e3134d0b6a90b371460e%2Fpro-organizations.png?alt=media">pro-organizations.png</a></td></tr><tr><td><strong>Workspaces</strong></td><td>Understand how to work with workspaces in ZenML Pro.</td><td><a href="workspaces">workspaces</a></td><td><a href="https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-c004d0f51396ca4e93254c5cc87c7e16ed0a8e9e%2Fpro-workspaces.png?alt=media">pro-workspaces.png</a></td></tr><tr><td><strong>Projects</strong></td><td>Learn about managing projects and their resources.</td><td><a href="projects">projects</a></td><td><a href="https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-81257a2f218866f9623df4ca3520ec8cd3e9279e%2Fpro-projects.png?alt=media">pro-projects.png</a></td></tr><tr><td><strong>Teams</strong></td><td>Explore team management in ZenML Pro.</td><td><a href="teams">teams</a></td><td><a href="https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-5cc1ccc85c6d027aca074dd297e91300490d5ad6%2Fpro-teams.png?alt=media">pro-teams.png</a></td></tr><tr><td><strong>Roles &#x26; Permissions</strong></td><td>Learn about role-based access control in ZenML Pro.</td><td><a href="../access-management/roles">roles</a></td><td><a href="https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-b8eca15363896683d019a696c0942c20dacb8241%2Fpro-roles.png?alt=media">pro-roles.png</a></td></tr></tbody></table>
