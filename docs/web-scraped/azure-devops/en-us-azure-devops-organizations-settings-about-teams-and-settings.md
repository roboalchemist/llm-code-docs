# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops&toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json

Title: About Teams and Agile Tools - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-teams-and-settings?view=azure-devops&toc=/azure/devops/organizations/toc.json

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Learn how you can structure and use your teams and Agile tools to support your growing organization. When your team grows beyond its intended size—typically anywhere from 6-to-9 members—you might consider moving from a one-team structure to a two-team structure. You can then set up a hierarchical team structure, which provides several advantages to managers for tracking progress across teams. For more information, see [Create or add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops).

Depending on the size of your organization and your tracking needs, you can set up a team structure similar to the following diagram. Do so by defining teams and their associated area paths.

[![Image 1: Diagram showing how each team has its own view of the work.](https://learn.microsoft.com/en-us/azure/devops/boards/plans/media/pm-team-structure.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/boards/plans/media/pm-team-structure.png?view=azure-devops#lightbox)

The following scenarios apply:

*   Each feature team can be associated with a single feature area path—such as _Customer Profile_, _Shopping Cart_, _Email_—or several area paths.
*   Each management team, which focuses on a set of features, can choose several area paths to monitor.
*   Each feature team has its distinct backlog to plan, determine priority, and track work.
*   Portfolio or product owners can create their vision, roadmap, and goals for each release, monitor progress across their portfolio of projects, and manage risks and dependencies. For more information, see [Portfolio management](https://learn.microsoft.com/en-us/azure/devops/boards/plans/portfolio-management?view=azure-devops).

Area paths serve the following purposes in Azure Boards:

*   **Filter work items:** Determine which work items appear on a team backlog or board.
*   **Apply additional filtering:** Further refine the work items that appear on a backlog or board. For details, see [Filter and focus your work in Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/filter-backlogs-boards-plans?view=azure-devops).
*   **Group related work:** Organize work that shares a relationship, such as belonging to the same product, feature, or other work-level grouping.
*   **Restrict access:** Set permissions to restrict modification of work items based on area path. Permissions can be configured for security groups.

Teams make their selections as follows:

*   **Feature teams:** Choose one or more area paths to specify which work items appear on their backlogs and boards.
*   **Management teams:** Typically select all area paths that their feature teams work on. They might focus on Features and Epics, while feature teams concentrate on product backlog items such as User Stories (Agile), Product Backlog Items (Scrum), and Requirements (CMMI).

For more information, see [Define area paths and assign to a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops).

Each new project is configured with a default team named after the project. For example, the _Fabrikam_ project is automatically configured with the _Fabrikam_ team.

Backlogs, boards, and dashboards are set up for this default team, allowing you to start defining work items and your backlog immediately.

You can rename the default team and assign a different team as the default if needed.

Each team you create gains access to a suite of Agile tools and team assets. These tools enable teams to work autonomously while collaborating with other teams across the enterprise. Each team can configure and customize these tools to support their unique workflows and processes.

[![Image 2: Diagram showing Agile tools and team assets.](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/agile-tools/agile-tools-team-assets-post-2018.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/agile-tools/agile-tools-team-assets-post-2018.png?view=azure-devops#lightbox)

These tools automatically filter the set of work items they display by referencing the following items:

*   Default area path
*   Iteration path
*   Selected sprints

For more information about each tool and its configuration settings, see the following articles.

**Area**

**Tool**

**Team configuration tasks**

Backlogs

*   [Product backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops)
*   [Features backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops)
*   [Epics backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops)
*   [Forecast](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/forecast?view=azure-devops)

*   [Configure area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops)
*   [Select active iteration paths (sprints)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)
*   [Select backlog levels](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/select-backlog-navigation-levels?view=azure-devops)
*   [Show bugs on backlogs & boards](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops)

Sprints and Scrum

*   [Sprint backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/assign-work-sprint?view=azure-devops)
*   [Sprint capacity](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/set-capacity?view=azure-devops)
*   [Taskboard](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/task-board?view=azure-devops)
*   [Sprint burndown](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/sprint-burndown?view=azure-devops)

*   [Select active iteration paths (sprints)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)

Boards

*   [Kanban board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview?view=azure-devops)
*   [Features board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-epics-features-stories?view=azure-devops)
*   [Epics board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-epics-features-stories?view=azure-devops)
*   [Cumulative flow](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/cumulative-flow?view=azure-devops)

*   [Configure area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops)
*   [Select default iteration path](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)
*   [Select backlog levels](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/select-backlog-navigation-levels?view=azure-devops)
*   [Show bugs on backlogs & boards](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops)

Widgets

*   [New work item](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#new-work-item-widget)
*   [Sprint burndown](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#burndown-widget)
*   [Sprint capacity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-capacity-widget)
*   [Sprint overview](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-overview-widget)
*   [Team members](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#team-members-widget)

*   [Configure area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops)
*   [Select active iteration paths (sprints)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops)
*   [Add team members](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops)

Other tools

*   [Favorites](https://learn.microsoft.com/en-us/azure/devops/project/navigation/set-favorites?view=azure-devops)
*   [Work item templates](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/work-item-template?view=azure-devops)
*   [Delivery plans](https://learn.microsoft.com/en-us/azure/devops/boards/plans/review-team-plans?view=azure-devops)
*   [Queries](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops)
*   [Velocity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/team-velocity?view=azure-devops)
*   [Dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops)
*   [Alerts](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications?view=azure-devops)

Not applicable

Many of these tools are built from system queries that reference the team's area path. For example, a team's default area path filters the work items that appear on the team's backlog. Work items created using an Agile tool automatically assign areas and iterations based on team defaults.

Work items that appear on team backlogs and boards are determined by the team's _area paths_ and _iteration paths_. When you add work items to a backlog or board, team defaults are used to assign field values.

When you define a team, you specify the following:

*   Selected area paths
*   Default area path
*   Selected iteration paths
*   Backlog iteration path
*   Default iteration path

All Agile tools reference the area paths defined for a team. The set of work items that appear on a backlog or board depends on the current **State** of a work item or its parent-child status.

Several tools also reference the team's default and selected Iteration Path or sprints. When you add a new work item from a team's backlog or board, the system assigns the team's **Default Area Path** and **Default Iteration Path** to it.

Note

New work items added through the **Work Items** page or the **New Work Items** widget on a team dashboard don't reference the **Default Iteration Path** assigned to the team. Instead, new work items are assigned the last **Iteration Path** selected by the user. New work items added through a team's **Sprints** backlog or taskboard are always assigned the **Iteration Path** associated with the selected sprint backlog or taskboard.

**Agile tool**

**Area path (see note 1)**

**Iteration path**

**State**

* * *

Portfolio or product backlogs

Selected area paths

Active (corresponds to a Proposed or InProgress state category, see notes 2, 3)

Boards (see note 4)

Selected area paths

Any state (see notes 3, 5)

Sprint backlogs (see note 4)

Selected area paths

Team's selected iteration paths

Any state (see notes 3, 5)

Task boards (see note 4)

Selected area paths

Team's selected iteration paths

Any state (see notes 3, 5)

New work item widget

Default area path

Default iteration path

n/a

Note

1.   Agile tools filter items based on the team's selected area paths. Teams can choose [whether to include or exclude items assigned to subarea paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops#set-team-area-paths).
2.   Work items whose **State** equals _Closed_, _Done_, or _Removed_ (corresponding to a _Completed_ category state) don't appear on portfolio and product backlogs.
3.   You can add custom workflow states and assign them to one of three state categories. The [state categories](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/workflow-and-state-categories?view=azure-devops) determine which work items appear on backlog and board views.
4.   Boards, sprint backlogs, and taskboards only show the last node in a hierarchy, called the leaf node. For example, if you link items within a hierarchy that is four levels deep, only the items at the fourth level appear on the board, sprint backlog, and task board. For more information, see [parent-child links between items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/resolve-backlog-reorder-issues?view=azure-devops).
5.   Work items whose **State** equals _Removed_ don't appear on boards.

Although there's no concept of subteams, you can create teams whose area paths are under another team, which effectively creates a hierarchy of teams. For more information, see [Create or add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops).

Also, the following articles walk you through the steps for configuring teams, area paths, and iterations to support portfolio management or enterprise organizations:

*   [Manage product and portfolio backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/plans/portfolio-management?view=azure-devops)
*   [Implement Scaled Agile Framework in Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/plans/scaled-agile-framework?view=azure-devops)

When you add a team, a security group is automatically created with the team name. You can use this group to filter queries. The name of team groups follows the pattern _[Project Name]\Team Name_. For example, the following query finds work assigned to members of the _[Fabrikam Fiber]\Email_ team group.

![Image 3: Screenshot of the Web portal, Queries page, with a query that uses In Group operator and team group name.](https://learn.microsoft.com/en-us/azure/devops/boards/plans/media/query-in-group-email-team-work-in-progress.png?view=azure-devops)

You can also use the _@mention_ control within discussions and pull requests to notify all members of a team. Start entering the name of a team or a security group, select the search icon, and then select from the options listed. For more information, see [Use @mentions to further discussion](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/at-mentions?view=azure-devops).

Can a user account belong to more than one team?

Yes. You can add user accounts as members of the project or to one or more teams added to the project. If you work on two or more Scrum teams, make sure you [specify your sprint capacity for each team you work on](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/set-capacity?view=azure-devops).

By default, team members inherit the permissions afforded to members of the project Contributors group. Members of this group can add and modify source code, create and delete test runs, and create and modify work items. Team members can [collaborate on a Git project](https://learn.microsoft.com/en-us/azure/devops/repos/git/gitquickstart?view=azure-devops) or [check in work to the team's code base](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/check-your-work-team-codebase?view=azure-devops).

[![Image 4: Diagram showing the default permissions assigned to team contributors.](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/add-team/default-permissions-assigned-to-team-contributors.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/media/add-team/default-permissions-assigned-to-team-contributors.png?view=azure-devops#lightbox)

For more information about limiting access, see [Set work tracking permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops).

*   Each team owns its own backlog. To create a new backlog, [Create or add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops).
*   Each backlog has a corresponding [board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview?view=azure-devops) to track progress and update status.
*   The team's specified area and iteration paths determine which work items appear on the backlog and board. You can easily decide to include or exclude work items under a specific area path.
*   Each team can control how [bugs show up on their backlogs and boards](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops).
*   For an overview of all team assets and how to configure them, see [Manage teams and configure team tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops).
*   To have work done by several teams roll up into a portfolio backlog, [set up the team hierarchy](https://learn.microsoft.com/en-us/azure/devops/boards/plans/portfolio-management?view=azure-devops).
*   To add fields or work item types, see [Customize your work tracking experience](https://learn.microsoft.com/en-us/azure/devops/reference/customize-work?view=azure-devops).

*   [Create or add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops)
*   [Manage and configure team tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops)
*   [Work across projects](https://learn.microsoft.com/en-us/azure/devops/project/navigation/work-across-projects?view=azure-devops)
