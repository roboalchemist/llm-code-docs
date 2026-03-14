# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops&toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json

Title: About projects and scaling your organization - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops&toc=/azure/devops/organizations/toc.json

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

A project in Azure DevOps provides a space for users to plan, track progress, and collaborate on building software solutions. It serves as a fundamental container for storing data and source code.

When you create a project, Azure DevOps automatically creates a team with the same name, which is sufficient for small organizations. For enterprise-level organizations, you might need to scale up by creating more teams and projects. Azure DevOps supports up to 1,000 projects within an organization.

An organization with multiple projects allows teams to configure tools to suit their needs and complete administrative tasks at the appropriate levels. As your organization grows, your tools can scale to support a [culture of team autonomy and organizational alignment](https://learn.microsoft.com/en-us/azure/devops/boards/plans/agile-culture?view=azure-devops).

For more information, see [Work tracking, process, and project limits](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/object-limits?view=azure-devops) and [Plan your organizational structure](https://learn.microsoft.com/en-us/azure/devops/user-guide/plan-your-azure-devops-org-structure?view=azure-devops).

When you connect to Azure DevOps, you connect to an organization. Within this organization, you can define one or more projects. At least one project must be created to use the system.

You can scale your organization in the following ways:

*   **Add projects**: Support different business units.
*   **Add teams**: Create teams within a project.
*   **Add repositories and branches**: Manage your source code.
*   **Add agents, agent pools, and deployment pools**: Support continuous integration and deployment.
*   **Manage access**: Use Microsoft Entra ID to handle a large number of users.

You can scale your on-premises Azure DevOps deployment in the following ways:

*   **Add server instances**: Increase performance.
*   **Add project collections and projects**: Support different business units.
*   **Add teams**: Create teams within a project.
*   **Add repositories and branches**: Manage your source code.
*   **Add agents, agent pools, and deployment pools**: Support continuous integration and deployment.
*   **Manage access**: Use Active Directory to handle a large number of users.

View the projects defined for your organization by opening the **Projects** page.

1.   Select ![Image 1](https://learn.microsoft.com/en-us/azure/devops/media/icons/project-icon.png?view=azure-devops)**Azure DevOps** to open **Projects**.

![Image 2: Screenshot showing projects page.](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/media/about-projects/projects-hub-vert.png?view=azure-devops)

2.   Choose a project from the list of projects.

For more information, see [Create a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops).

By default, users added to an organization can view all organization and project information and settings. For more information, see [Limit user visibility for projects and more](https://learn.microsoft.com/en-us/azure/devops/user-guide/manage-organization-collection?view=azure-devops#limit-user-visibility-for-projects-and-more) and [Change project visibility to public or private](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/make-project-public?view=azure-devops).

All project members can view identities added to comments, discussions, or assignments. For example, everyone in the project (even users with new restrictions) can still see a user's name assigned to a work item when the user is no longer part of the project. The same applies to @mentions in PRs, comments, discussions, and more.

One recommended approach is to use a single project to support your organization or enterprise. A single project can help minimize the maintenance of administrative tasks and provides the most optimized and flexible [cross-link object](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-link?view=azure-devops) experience.

Even if you have many teams working on hundreds of different applications and software projects, you can easily manage them within a single project. A project isolates the data stored within it, and moving data from one project to another results in the loss of associated history.

For more information, see [How many projects do you need?](https://learn.microsoft.com/en-us/azure/devops/user-guide/plan-your-azure-devops-org-structure?view=azure-devops#how-many-projects-do-you-need).

Another feasible approach is to have multiple projects. This approach is recommended if your organization needs to:

*   Prohibit or manage access to the information contained within a project for select groups
*   Support custom work tracking processes for specific business units within your organization
*   Support entirely separate business units that have their own administrative policies and administrators
*   Test customization activities or add extensions before rolling out changes to the working project
*   Support an open-source software (OSS) project

You might want to add another project in the following instances:

*   Prohibit or manage access to the information contained within a project
*   Support custom work tracking processes for specific business units within your organization
*   Support entirely separate business units that have their own administrative policies and administrators
*   Test customization activities or add extensions before rolling out changes to the working project

You can have both private and public projects. You can also [change the visibility of a project from either one to the other](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/make-project-public?view=azure-devops).

**Private projects**:

*   Require adding and managing user access.
*   Require users to sign in to gain access even for read-only access.
*   Provide all project members access to the project and organization information.

For more information, see [Resources granted to project members](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/resources-granted-to-project-members?view=azure-devops).

Important

Only organizations with the **Allow public project policy** already enabled can create projects or change the visibility of a project to public. The policy is no longer available to organizations that aren't using it already. Microsoft recommends using [GitHub](https://github.com/) for all your public project needs.

**Public projects**:

*   Don't require users to sign in for read-only access to many services.
*   Support sharing code with others.
*   Support continuous integration/continuous deployment (CI/CD) of open-source software.

For more information, see [Change visibility of a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/make-project-public?view=azure-devops).

Git repositories can be browsed and cloned only via HTTPS. SSH and GVFS endpoints are unavailable. Clients like Visual Studio and IntelliJ work with the HTTPS clone URL but don't offer the connected experience linking to work items and other collateral.

The following dashboard widgets don't display any useful information for nonmembers.

*   Assigned to me
*   Code tile
*   New work item
*   Pull request
*   Query results
*   Requirements quality
*   Sprint burndown
*   Sprint capacity
*   Sprint overview
*   Team members
*   Welcome
*   Work links
*   Other links

For more information, see [Add widgets to a dashboard](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/add-widget-to-dashboard?view=azure-devops) and [FAQs about dashboards, charts, and reports](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/faqs?view=azure-devops).

Use the following elements to structure your project to support your business needs:

*   [Create a Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/creatingrepo?view=azure-devops) for each subproject or application, or [create root folders within a TFVC repository](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/branch-folders-files?view=azure-devops) for each subproject. If you're using TFVC and heading toward a combined project model, create root folders for different teams and projects, just as you would create separate repos in Git. Secure folders as needed and control which segments of the repo you're actively using with workplace mappings.
*   [Define area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops) to support different subprojects, products, features, or teams.
*   [Define iteration paths (also known as sprints)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops) that can be shared across teams.
*   [Add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops) for each product team that develops a set of features for a product. Each team you create automatically creates a security group for that team, which you can use to manage permissions for a team. For more information, see [Portfolio management](https://learn.microsoft.com/en-us/azure/devops/boards/plans/portfolio-management?view=azure-devops).
*   [Manage access to specific features and functions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/restrict-access?view=azure-devops) using custom security groups.
*   [Create query folders](https://learn.microsoft.com/en-us/azure/devops/boards/queries/organize-queries?view=azure-devops) to organize queries for teams or product areas into folders.
*   [Define or modify notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/about-notifications?view=azure-devops) set at the project level.

You can configure and customize most services and applications to support your business needs or the way your teams work. Within each project, you can do the following tasks. For a comprehensive view of which resources can be configured, see [About team, project, and organizational-level settings](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-settings?view=azure-devops).

*   **Dashboards**: Each team can [configure their set of dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops) to share information and monitor progress.
*   **Source control**: For each [Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/?view=azure-devops), you can apply branch policies and define branch permissions. For TFVC repositories, you can [set check-in policies](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/add-check-policies?view=azure-devops).
*   **Work tracking**: You can add fields, change the workflow, add custom rules, and add custom pages to the work item form of most work item types. You can also add custom work item types. For more information, see [Customize an inheritance process](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model?view=azure-devops).
*   **Azure Pipelines**: You can fully customize your build and release pipelines, and define build steps, release environments, and deployment schedule. For more information, see [Build and release](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops).
*   **Azure Test Plans**: You can define and configure test plans, test suites, test cases, and test environments. You can also add test steps within your build pipelines. For more information, see [Exploratory and manual testing](https://learn.microsoft.com/en-us/azure/devops/test/?view=azure-devops) and [continuous testing for your builds](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#run-your-tests).

As your organization grows, you can add teams equipped with configurable Agile tools to meet each team's workflow. For more information, see the following articles.

*   [Scale Agile to large teams](https://learn.microsoft.com/en-us/devops/plan/scaling-agile)
*   [About teams and Agile tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops)
*   [Manage a portfolio of backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/plans/portfolio-management?view=azure-devops) and see progress.
*   [Use delivery plans](https://learn.microsoft.com/en-us/azure/devops/boards/plans/review-team-plans?view=azure-devops) to scheduled work items by sprint (iteration path) of selected teams against a calendar view.
*   [Incrementally adopt practices that scale](https://learn.microsoft.com/en-us/azure/devops/boards/plans/practices-that-scale?view=azure-devops) to create greater rhythm and flow within your organization, engage customers, improve project visibility, and develop a productive workforce.
*   [Structure projects to gain visibility across teams](https://learn.microsoft.com/en-us/azure/devops/boards/plans/visibility-across-teams?view=azure-devops) or to support [epics, release trains, and multiple backlogs to support the Scaled Agile Framework](https://learn.microsoft.com/en-us/azure/devops/boards/plans/scaled-agile-framework?view=azure-devops).

Aside from connecting via a web browser, you can connect to a project from the following clients:

*   [Visual Studio (Professional, Enterprise, Test Professional)](https://visualstudio.microsoft.com/vs/compare/)
*   [Visual Studio Code](https://code.visualstudio.com/Docs)
*   [Visual Studio Community](https://www.visualstudio.com/products/visual-studio-community-vs.aspx)
*   [Office Excel](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/office/bulk-add-modify-work-items-excel?view=azure-devops)
*   [Test & Feedback extension](https://learn.microsoft.com/en-us/azure/devops/test/request-stakeholder-feedback?view=azure-devops)
*   [Microsoft Feedback Client](https://learn.microsoft.com/en-us/previous-versions/azure/devops/project/feedback/give-feedback)

For more information, see [Compatibility with Azure DevOps Server versions](https://learn.microsoft.com/en-us/azure/devops/server/compatibility).

Use the following index to quickly access concepts and tasks related to managing projects and teams.

*   [About projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops)
*   [About teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops)
*   [Access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops)
*   [Area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations?view=azure-devops)
*   [Dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/overview?view=azure-devops)
*   [Notifications and subscriptions](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/about-notifications?view=azure-devops)
*   [GitHub connections](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)
*   [Iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations?view=azure-devops)

*   [Permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Process (Inherited)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model?view=azure-devops)
*   [Project resources viewable by members](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/resources-granted-to-project-members?view=azure-devops)
*   [Project Wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/provisioned-vs-published-wiki?view=azure-devops)
*   [Project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#project-level-permissions)
*   [Project-level security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#project-level-groups)

*   [Project and process object limits](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/object-limits?view=azure-devops)
*   [Projects page](https://learn.microsoft.com/en-us/azure/devops/project/navigation/work-across-projects?view=azure-devops)
*   [Public vs private projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops)
*   [Security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)
*   [Service visibility](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops)
*   [Summary page](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops)

*   [About projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects?view=azure-devops)
*   [About teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops)
*   [Access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops)
*   [Area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations?view=azure-devops)
*   [Dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/overview?view=azure-devops)
*   [Notifications and subscriptions](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/about-notifications?view=azure-devops)
*   [GitHub connections](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)
*   [Iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations?view=azure-devops)

*   [Permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Process (Inherited)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model?view=azure-devops)
*   [Process (On-premises XML)](https://learn.microsoft.com/en-us/azure/devops/reference/on-premises-xml-process-model?view=azure-devops)
*   [Project and process object limits](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/object-limits?view=azure-devops)
*   [Project resources viewable by members](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/resources-granted-to-project-members?view=azure-devops)
*   [Project Wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/provisioned-vs-published-wiki?view=azure-devops)

*   [Project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#project-level-permissions)
*   [Project-level security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#project-level-groups)
*   [Projects page](https://learn.microsoft.com/en-us/azure/devops/project/navigation/work-across-projects?view=azure-devops)
*   [Security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops)
*   [Service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)
*   [Service visibility](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops)
*   [Summary page](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops)

Several of the following tasks require permissions granted to a member of the Project Administrators group or a team administrator.

*   [Add Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-new-repo?view=azure-devops)
*   [Add project administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Add project dashboard](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops#add-a-dashboard)
*   [Add project members](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Add security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-ad-aad-built-in-security-groups?view=azure-devops)
*   [Add team administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-team-administrator?view=azure-devops)
*   [Add team members](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Add/manage service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)
*   [Connect to a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/connect-to-projects?view=azure-devops)
*   [Connect to GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)

*   [Create project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
*   [Delete project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/delete-project?view=azure-devops)
*   [Edit project Summary](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops)
*   [Enable/disable project services](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops)
*   [Export list of projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
*   [Export list of teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops#list-teams)
*   [Manage notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications?view=azure-devops)
*   [Manage your project](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?view=azure-devops)
*   [Navigate the Web portal](https://learn.microsoft.com/en-us/azure/devops/project/navigation/?view=azure-devops)
*   [Remove team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/rename-remove-team?view=azure-devops)

*   [Rename project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
*   [Rename team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/rename-remove-team?view=azure-devops)
*   [Restore project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/delete-project?view=azure-devops#restore-a-deleted-project)
*   [Change user access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-organization-users?view=azure-devops)
*   [Search across projects](https://learn.microsoft.com/en-us/azure/devops/project/search/get-started-search?view=azure-devops)
*   [Set area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops)
*   [Set favorites](https://learn.microsoft.com/en-us/azure/devops/project/navigation/set-favorites?view=azure-devops)
*   [Set iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)
*   [Set project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Set project visibility](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/make-project-public?view=azure-devops)
*   [Switch project, repository, team](https://learn.microsoft.com/en-us/azure/devops/project/navigation/go-to-project-repo?view=azure-devops)

*   [Add Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-new-repo?view=azure-devops)
*   [Add project administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Add project members](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Add security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-ad-aad-built-in-security-groups?view=azure-devops)
*   [Add team members](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)
*   [Add team administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-team-administrator?view=azure-devops)
*   [Add/manage service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)
*   [Change access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels?view=azure-devops)
*   [Connect to a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/connect-to-projects?view=azure-devops)
*   [Connect to GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)

*   [Create project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
*   [Delete project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/delete-project?view=azure-devops)
*   [Edit project Summary](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/project-vision-status?view=azure-devops)
*   [Enable/disable project services](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops)
*   [Manage notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications?view=azure-devops)
*   [Manage your project](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?view=azure-devops)
*   [Navigate the Web portal](https://learn.microsoft.com/en-us/azure/devops/project/navigation/?view=azure-devops)
*   [Remove team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/rename-remove-team?view=azure-devops)

*   [Rename project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
*   [Rename team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/rename-remove-team?view=azure-devops)
*   [Restore project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/delete-project?view=azure-devops#restore-a-deleted-project)
*   [Search across projects](https://learn.microsoft.com/en-us/azure/devops/project/search/get-started-search?view=azure-devops)
*   [Set area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops)
*   [Set favorites](https://learn.microsoft.com/en-us/azure/devops/project/navigation/set-favorites?view=azure-devops)
*   [Set iteration paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)
*   [Set project-level permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops)
*   [Switch project, repository, team](https://learn.microsoft.com/en-us/azure/devops/project/navigation/go-to-project-repo?view=azure-devops)

**A:** Yes, but not without losing data. You can manually copy resources and leave some behind, or use a non-Microsoft tool.

**A.** See [Projects REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects).

*   [Get started as an administrator](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?view=azure-devops)
*   [Navigate the web portal](https://learn.microsoft.com/en-us/azure/devops/project/navigation/?view=azure-devops)
*   [Features and services included with Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops&toc=%2Fazure%2Fdevops%2Forganizations%2Fprojects%2Ftoc.json&bc=%2Fazure%2Fdevops%2Forganizations%2Fprojects%2Fbreadcrumb%2Ftoc.json)
