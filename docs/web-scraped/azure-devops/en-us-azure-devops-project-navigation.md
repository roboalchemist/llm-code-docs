# Source: https://learn.microsoft.com/en-us/azure/devops/project/navigation/

Title: Navigating within the web portal - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/project/navigation/

Published Time: Wed, 18 Feb 2026 02:05:23 GMT

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

The Azure DevOps web portal is organized into various services, administrative pages, and task-specific features like the search box. Service labels vary depending on whether you’re using Azure DevOps Services or an on-premises version.

Important

![Image 1: Select a version from Azure DevOps Content Version selector.](https://learn.microsoft.com/en-us/azure/devops/media/version-selector.png?view=azure-devops)

Each service offers multiple pages with numerous features and functional tasks. Within each page, you can choose options to select or add specific artifacts.

Here's what you need to know to start using the web portal effectively.

*   [**Open a service, page, or settings**](https://learn.microsoft.com/en-us/azure/devops/project/navigation/go-to-service-page?view=azure-devops): Use to switch to a different [service or functional area](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops)
*   [**Add an artifact or team**](https://learn.microsoft.com/en-us/azure/devops/project/navigation/add-artifact-team?view=azure-devops): Use to quickly add a work item, Git repo, build or release pipelines, or a new team
*   [**Open another project or repo**](https://learn.microsoft.com/en-us/azure/devops/project/navigation/work-across-projects?view=azure-devops): Use to switch to a different project or access work items and pull requests defined in different projects, or your favorite items
*   [**Open team artifacts, use breadcrumbs, selectors and directories**](https://learn.microsoft.com/en-us/azure/devops/project/navigation/use-breadcrumbs-selectors?view=azure-devops): Use to navigate within a service, open other artifacts, or return to a root function
*   [**Work with favorites**](https://learn.microsoft.com/en-us/azure/devops/project/navigation/set-favorites?view=azure-devops): Mark your favorite artifacts for quick navigation
*   [**Search box**](https://learn.microsoft.com/en-us/azure/devops/project/search/get-started-search?view=azure-devops): Use to find code, work items, or wiki content
*   [**Your profile menu**](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-your-preferences?view=azure-devops&toc=%2Fazure%2Fdevops%2Fproject%2Fnavigation%2Ftoc.json&bc=%2Fazure%2Fdevops%2Fproject%2Fnavigation%2Fbreadcrumb%2Ftoc.json): Use to set personal preferences, notifications, and enable preview features
*   [**Settings**](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops#project-administrator-role-and-managing-projects): Use to add teams, manage security, and configure other project and organization level resources.

Note

Only enabled services are visible in the user interface. For example, if **Boards** is disabled, then **Boards** or **Work** and all pages associated with that service don't appear. To enable or disable a service, see [Turn an Azure DevOps service on or off](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops).

Select services—such as **Boards**, **Repos**, and **Pipelines**—from the sidebar and pages within those services.

![Image 2: Screenshot shows vertical sidebar.](https://learn.microsoft.com/en-us/azure/devops/project/navigation/media/gif-images/vertical-nav.gif?view=azure-devops)

Now that you understand the user interface structure, it’s time to start using it. You can find a wide range of features and functionalities to explore.

If all you need is a code repository and bug tracking solution, then start with [Get started with Git](https://learn.microsoft.com/en-us/azure/devops/repos/git/gitquickstart?view=azure-devops) and [Manage bugs](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/manage-bugs?view=azure-devops).

To start planning and tracking work, see [About Agile tools](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards?view=azure-devops&context=vsts%2Fdefault).

You connect to the web portal through a supported web browser—such as the latest versions of Microsoft Edge, Chrome, Safari, or Firefox. Only users [added to a project](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users?view=azure-devops) can connect, which is typically done by the organization owner.

Five account users are free as are Visual Studio subscribers and stakeholders. After that, you need to [pay for more users](https://learn.microsoft.com/en-us/azure/devops/organizations/billing/buy-basic-access-add-users?view=azure-devops). Find out more about licensing from [Azure DevOps pricing](https://azure.microsoft.com/pricing/details/devops/azure-devops-services/).

Limited access is available to an unlimited number of stakeholders for free. For details, see [Work as a Stakeholder](https://learn.microsoft.com/en-us/azure/devops/organizations/security/get-started-stakeholder?view=azure-devops).

If data doesn't appear as expected, the first thing to try is to refresh your web browser. Refreshing your client updates the local cache with changes that were made in another client or the server. To refresh the page or object you're currently viewing, refresh the page or choose the ![Image 3: Refresh icon](https://learn.microsoft.com/en-us/azure/devops/media/icons/refresh.png?view=azure-devops)**Refresh** icon if available.

To avoid potential errors, you should refresh your client application in the following scenarios:

*   Process change applied
*   Work item type definition added, removed, renamed, or updated
*   Area or iteration path added, removed, renamed, or updated
*   User added or removed in security groups, or user permissions updated
*   New shared query added or existing shared query updated
*   Build definition added or deleted
*   Team or project added or deleted

Although you can access source code, work items, and builds from both clients, some task specific tools are only supported in the web browser or an IDE but not in both. Supported tasks differ depending on whether you connect to a Git or TFVC repository from Team Explorer.

* * *

**Web portal**

**Visual Studio**

* * *

*   [Product backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops), [Portfolio backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-epics-features-stories?view=azure-devops), [Sprint backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/assign-work-sprint?view=azure-devops), [Taskboards](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/task-board?view=azure-devops), [Capacity planning](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/set-capacity?view=azure-devops)
*   [Boards](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview?view=azure-devops)
*   [Dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops), [Widgets](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops), [Charts](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/charts?view=azure-devops)
*   [Request feedback](https://learn.microsoft.com/en-us/previous-versions/azure/devops/project/feedback/get-feedback)
*   [Web-based Test Management](https://learn.microsoft.com/en-us/azure/devops/test/overview?view=azure-devops)
*   [Administration pages to administer accounts, team projects, and teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops)

*   Git: [Changes](https://learn.microsoft.com/en-us/azure/devops/repos/git/commits?view=azure-devops#stage-your-changes-and-commit), [Branches](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-branch?view=azure-devops), [Pull Requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops), [Sync](https://learn.microsoft.com/en-us/azure/devops/repos/git/pulling?view=azure-devops), [Work Items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-work-items?view=azure-devops), [Builds](https://learn.microsoft.com/en-us/previous-versions/ms181721(v=vs.140))
*   TFVC: [My Work](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/develop-code-manage-pending-changes?view=azure-devops), [Pending Changes](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/develop-code-manage-pending-changes?view=azure-devops) | [Source Control Explorer](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/develop-code-manage-pending-changes?view=azure-devops#use-solution-explorer-or-source-control-explorer-to-view-what-you-changed), [Work Items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-work-items?view=azure-devops) | [Builds](https://learn.microsoft.com/en-us/previous-versions/ms181721(v=vs.140))
*   Greater integration with work items and Office integration clients. You can open a work item or query result in an office supported client.

* * *

Note

Visual Studio 2019 version 16.8 and later provide a Git menu for managing the Git workflow with less context switching than Team Explorer. Procedures in this article under the Visual Studio tab describe how to use the Git experience and also Team Explorer. For more information, see [Side-by-side comparison of Git and Team Explorer](https://learn.microsoft.com/en-us/visualstudio/version-control/git-team-explorer-feature-comparison).

*   [Manage projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops)
*   [Manage settings for projects and organizations](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops#project-administrator-role-and-managing-projects)
