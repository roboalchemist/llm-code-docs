# Source: https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?view=azure-devops

Title: Get Started as a Project Administrator - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

With most Azure DevOps Services, you can start using the service and configure resources as you go. No up-front work is required. Most settings define defaults.

If you created a project or you're added to the **Project Administrators** group, get familiar with the administrative tasks you're charged with. There are a few tasks you might want to do to ensure a smooth operational experience.

| Category | Requirements |
| --- | --- |
| **Permissions** | Member of the **Project Administrators** security group. |

Note

This article provides an overview of tasks a member of the **Project Administrators** group should review and attend to. For information on tasks to be performed by members of the **Project Collection Administrators** group, see [Manage your organization or project collection](https://learn.microsoft.com/en-us/azure/devops/user-guide/manage-organization-collection?view=azure-devops).

You add users to a team or project so they can contribute to the team and project. Users can be added to multiple teams and projects.

Users who are added to an organization, can easily be added to a project by adding them to a team or inviting them to contribute to a project.

Team administrators can add users to their team, which automatically adds them to the project. By adding users to a team, the users become visible to team-specific tools like the team security group, Team Members widget, and sprint capacity planning tools. To learn more about teams, see [About teams and Agile tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops).

Members of the **Project Administrators** group can add users to a project. Adding users to a team or project automatically adds them to the project's **Contributors** group. Members of this group have permissions to most features needed to contribute to work items, code, builds, and releases. For an overview of default permissions, see [Default permissions quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops).

After users are added to a project or organization, you can browse for their display name or user name (email alias) from any people-picker tool. Users can connect to a project and access features available through a supported client or the web portal.

For more information, see the following articles:

*   [Add users or groups to a team or project](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Manage your organization or project collection, Add users to your organization](https://learn.microsoft.com/en-us/azure/devops/user-guide/manage-organization-collection?view=azure-devops)
*   [Connect to a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/connect-to-projects?view=azure-devops)

Each project has a summary page that's useful for sharing information through **README** files. You can also redirect users to a project Wiki. For users who are new to your project, a good approach is to [set up your project summary page](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops) or [prepare a Wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/wiki-create-repo?view=azure-devops). Use these features to share established processes and procedures for your project.

To simplify the web portal user interface, you can disable specific services. Suppose you use a project only to log bugs. In this scenario, you might disable all services except for **Boards**. For more information, see [Turn a service on or off](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops).

The following example shows the **Test Plans** service disabled:

![Image 1: Screenshot that shows the Test Plans service disabled in the Project Settings page for Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/user-guide/media/services/set-service-visibility.png?view=azure-devops)

Permissions and security groups control access to specific tasks. To quickly understand the defaults configured for your project, see [Default permissions and access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops).

The following table lists the permissions assigned at the project-level. All these permissions are granted to members of the **Project Administrators** group, except for the **Delete shared Analytics views** and **Edit shared Analytics views** permissions. For a description of each permission, see [Permissions and groups reference, Groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#project-level-permissions).

Note

Permissions associated with Analytics require that the Inherited process model is selected for an on-premises project collection.

**General**

*   Delete team project
*   Edit project-level information
*   Manage project properties
*   Rename team project
*   Suppress notifications for work item updates
*   Update project visibility
*   View project-level information

*   Delete team project
*   Edit project-level information
*   Manage project properties
*   Rename team project
*   Suppress notifications for work item updates
*   View project-level information

**Boards**

*   Bypass rules on work item updates
*   Change process of team project
*   Create tag definition
*   Delete and restore work items
*   Move work items out of this project
*   Permanently delete work items

**Analytics**

*   Delete shared Analytics views
*   Edit shared Analytics views
*   View analytics

**Test Plans**

*   Create test runs
*   Delete test runs
*   Manage test configurations
*   Manage test environments
*   View test runs

For more information about security and setting permissions at the project-level, review the following articles:

*   [Get started with permissions, access, and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Change permissions at the project-level](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)

The person who creates a project is automatically added as a member to the **Project Administrators** group. Members of this group have permissions to manage project configuration, repositories, pipeline resources, teams, and all project-level permissions.

It's a good practice to assign administrative privileges to more than one team member. You can add a user to this group by following the instructions in [Change permissions at the project level, Add members to the Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops#add-members-to-the-project-administrators-group).

Permissions are managed at the following three levels and through role-based assignments:

*   object
*   project
*   organization or collection

As a member of the **Project Administrators** group, you can grant or restrict permissions for all objects at the project-level. To delegate specific tasks to others, a good approach is to add the users to a built-in or custom security group, or add them to a specific role. For more information, see the following articles:

*   [Use role-based permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#role-based-permissions)
*   [Add/remove users or groups, manage security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-remove-manage-user-group-security-group?view=azure-devops)
*   [Manage access to specific features and functions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/restrict-access?view=azure-devops)
*   [Set object-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-object-level-permissions?view=azure-devops)

Several notifications are predefined for each project you add. Notifications are based on subscription rules. Subscriptions arise from the following areas:

*   [Out-of-the-box or default subscriptions](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/oob-built-in-notifications?view=azure-devops).
*   [Team, project, and organization or collection subscriptions](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications?view=azure-devops) defined by a team administrator or member of the **Project Administrators** or **Project Collection Administrators** groups.

If users report receiving too many notifications, you can direct them to [opt out of a subscription](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-your-personal-notifications?view=azure-devops).

![Image 2: Screenshot that shows how users can opt out of various types of notifications.](https://learn.microsoft.com/en-us/azure/devops/user-guide/media/services/personal-notifications.png?view=azure-devops)

If you use most Azure DevOps Services, such as Azure Boards, Azure Repos, Azure Pipelines, and Azure Test Plans, you probably want to alert your teams to the features that support end-to-end traceability. You can get started by reviewing the following articles:

*   [Cross-service integration and collaboration overview](https://learn.microsoft.com/en-us/azure/devops/cross-service/cross-service-overview?view=azure-devops)
*   [End-to-end traceability](https://learn.microsoft.com/en-us/azure/devops/cross-service/end-to-end-traceability?view=azure-devops)

Set policies to support collaboration across your teams and automatically remove obsolete files. To set policies that govern Azure Repos, Azure Pipelines, and Azure Test Plans, review the following articles:

*   [Manage branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops)
*   [Add Team Foundation Version Control (TFVC) check-in policies](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/add-check-policies?view=azure-devops)
*   [Set build and release pipeline retention policies](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops)
*   [Set test retention policies](https://learn.microsoft.com/en-us/azure/devops/test/how-long-to-keep-test-results?view=azure-devops)

You can configure and customize Azure Boards to support many business requirements for planning and tracking work. At a minimum, you should configure the following elements:

*   **Area paths** to group work items by team, product, or feature area
*   **Iteration paths** to group work into sprints, milestones, or other event-specific or time-related periods

If you're new to Azure Boards and want an in-depth overview of what you can configure and customize, see [Configure and customize Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/configure-customize?view=azure-devops).

If you support several products, you can assign work items according to feature area by defining [area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops). To assign work items to specific time intervals, also known as _sprints_, you configure [iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops). To use the Scrum tools like sprint backlogs, taskboards, and team capacity, you need to configure several sprints. For an overview, see [About areas and iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations?view=azure-devops).

The following image shows default iteration paths for Scrum processes:

![Image 3: Screenshot showing default iterations for Scrum processes.](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/areas/areas-iterations-iterations-intro-ts-2016.png?view=azure-devops)

The following image shows a set of sample area paths:

![Image 4: Screenshot showing a set of sample area paths.](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/areas/areas-iterations-areas-intro-ts-2016.png?view=azure-devops)

You and your team can start using all work-tracking tools immediately after you create a project. But often, some users want to customize the experience to meet various business needs. You can customize the process easily through the user interface. It's a good practice to establish a methodology for which users can manage the updates and evaluate requests.

Note

By default, organization owners and users added to the **Project Collection Administrators** security group are granted permission to create, edit, and manage processes used to customize the work-tracking experience. If you want to lock down who is able to perform these tasks, you can set permissions at the organization-level to **Deny**.

For more information, see the following articles:

*   [About process customization and inherited processes](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model?view=azure-devops)
*   [Customize a project](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/customize-process?view=azure-devops)
*   [Add and manage processes](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/manage-process?view=azure-devops)

Azure DevOps supports integration with Azure, GitHub, and many other services. As a member of the **Project Administrators** group, you can configure integration with many of these services. For more information, see the following articles.

| Service integration | Resources |
| --- | --- |
| **Azure DevOps and GitHub** | [Azure DevOps and GitHub integration overview](https://learn.microsoft.com/en-us/azure/devops/cross-service/github-integration?view=azure-devops) |
| **Azure Boards and GitHub** | [Azure Boards and GitHub integration](https://learn.microsoft.com/en-us/azure/devops/boards/github/?view=azure-devops) |
| **Microsoft Teams** | - [Azure Boards with Microsoft Teams](https://learn.microsoft.com/en-us/azure/devops/boards/integrations/boards-teams?view=azure-devops) - [Azure Repos with Microsoft Teams](https://learn.microsoft.com/en-us/azure/devops/repos/integrations/repos-teams?view=azure-devops) - [Azure Pipelines with Microsoft Teams](https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/microsoft-teams?view=azure-devops) |
| **Slack** | - [Azure Boards with Slack](https://learn.microsoft.com/en-us/azure/devops/boards/integrations/boards-slack?view=azure-devops) - [Azure Repos with Slack](https://learn.microsoft.com/en-us/azure/devops/repos/integrations/repos-slack?view=azure-devops) - [Azure Pipelines with Slack](https://learn.microsoft.com/en-us/azure/devops/pipelines/integrations/slack?view=azure-devops) |
| **Azure DevOps service hooks** | [Integrate with service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops) |

As your organization grows, it's a good practice to add teams to scale your project. Each team gets [access to their own set of customizable Agile tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops).

[![Image 5: Diagram of Agile tools and team assets organized to support planning - tracking, monitoring - learning, and collaboration.](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/agile-tools/agile-tools-team-assets-post-2018.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/agile-tools/agile-tools-team-assets-post-2018.png?view=azure-devops#lightbox)

For more information, see the following articles:

*   [About projects and scaling your organization](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops)
*   [Add a team, move from one default team to several teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops)
*   [Add a team administrator](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-team-administrator?view=azure-devops)

*   [View and update project summary page](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops)
*   [Get started managing your organization or project collection](https://learn.microsoft.com/en-us/azure/devops/user-guide/manage-organization-collection?view=azure-devops)
*   [About user, team, project, and organization-level settings](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops)
