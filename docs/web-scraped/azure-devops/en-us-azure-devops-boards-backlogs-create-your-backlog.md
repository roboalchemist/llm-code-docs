# Source: https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops

Title: Create and manage your product backlog - Azure Boards

URL Source: https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

The product backlog is your project plan, which shows what your team intends to deliver. It contains user stories, backlog items, or requirements that you add to it. Your backlog is a flat list of work items, as the following image illustrates, which shows a Scrum process for Azure Boards. For the Agile, Basic, and Capability Maturity Model Integration (CMMI) process models, the **Backlog items** selection appears as **Stories**, **Issues**, and **Requirements**.

Your product backlog is one of three classes of backlogs available to you: _backlogs_, _boards_, and _plans_.

![Image 1: Screenshot of a Backlog of Scrum process product backlog items.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/intro-image.png?view=azure-devops)

| Category | Requirements |
| --- | --- |
| Project access | [Project member](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops). |
| Permissions | - Member of the **Contributors** or **Project Administrators** security group. - To view or modify work items: **View work items in this node** and **Edit work items in this node** permissions set to **Allow**. By default, the **Contributors** group has this permission set to **Allow**. For more information, see [Set work tracking permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops). |
| Access levels | To add or modify work items: At least **Basic** access. Users with **Stakeholder** access for public projects have full access to backlog and board features, like users with **Basic** access. For more information, see [Stakeholder access quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops). |
| Defined iterations | To use the **Planning** pane: Ensure your team administrator [defined iteration paths (sprints) and configure team iterations](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops). |

| Category | Requirements |
| --- | --- |
| Project access | [Project member](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops). |
| Permissions | - Member of the **Contributors** or **Project Administrators** security group. - To view or modify work items: **View work items in this node** and **Edit work items in this node** permissions set to **Allow**. By default, the **Contributors** group has this permission set to **Allow**. For more information, see [Set work tracking permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops). |
| Access levels | To add or modify work items: At least [**Basic** access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops). |
| Defined iterations | To use the **Planning** pane: Ensure your team administrator [defined iteration paths (sprints) and configure team iterations](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops). |

Your product **Backlog**, **Board**, and sprint backlogs display work items based on the following criteria:

| Process | Work Item Type | Backlog Name |
| --- | --- | --- |
| [Basic](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops) | Issue | Issues |
| [Agile](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops) | User Story | Stories |
| [Scrum](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process?view=azure-devops) | Product Backlog Item | Backlog items |
| [CMMI](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process?view=azure-devops) | Requirement | Requirements |

More filtering criteria:

*   **Area Path** matches one of your team's selected Area Paths
*   **Iteration Path** is under your team's Default Iteration Path

Sprint backlogs and Taskboards apply these same filters plus the selected **Iteration Path**. You can only select Iteration Paths [preselected by your team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops#list-team-iterations). Sprint backlogs display only work items assigned to the selected sprint—child tasks assigned to other sprints aren't displayed.

![Image 2: Screenshot of Product backlog level, Backlog items, Stories, or Requirements.](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/media/assign-items-sprint/select-product-backlog-agile.png?view=azure-devops)

For more information, see [Define area paths and assign to a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths?view=azure-devops) and [Define sprint paths and configure team iterations](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops#list-team-iterations).

Every project includes a default team with backlogs. To support more teams, see [Create or add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops).

Each process defines the following specific backlog levels:

*   [Agile](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops): **Stories**, **Features**, and **Epics**
*   [Basic](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops): **Issues** and **Epics**
*   [Scrum](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process?view=azure-devops): **Backlog items**, **Features**, and **Epics**
*   [CMMI](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process?view=azure-devops): **Requirements**, **Features**, and **Epics**

From your web browser, follow these steps to open your product backlog.

1.   Sign in to your project (`https://dev.azure.com/{Your_Organization}/{Your_Project}`).

2.   Select **Boards**>**Backlogs**.

![Image 3: Screenshot of sequence selection for opening Backlogs in Boards.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/open-backlogs.png?view=azure-devops)

To select a different backlog, choose a different team or select the **View Backlog directory** option. You can also enter a keyword in the search box to filter the team backlogs for the project.

![Image 4: Screenshot showing team selection dropdown menu.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/backlog-team-selector.png?view=azure-devops)

Tip

Choose the ![Image 5](https://learn.microsoft.com/en-us/azure/devops/media/icons/icon-favorite-star.png?view=azure-devops) star icon to favorite a team backlog. Favorited artifacts (![Image 6](https://learn.microsoft.com/en-us/azure/devops/media/icons/icon-favorited.png?view=azure-devops) favorited icon) appear at the top of the team selector list. 
3.   Check that you selected **Stories** (for Agile), **Issues** (for Basic), **Backlog items** (for Scrum), or **Requirements** (for CMMI) as the backlog level.

![Image 7: Screenshot shows the option to Choose backlog level.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/backlog-selector.png?view=azure-devops)

4.   (Optional) To select which columns display and in what order, select the ![Image 8](https://learn.microsoft.com/en-us/azure/devops/media/icons/actions-icon.png?view=azure-devops) actions icon and **Column options**. For more information, see [Change column options](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/set-column-options?view=azure-devops).

![Image 9: Screenshot showing Column Options button selection.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/open-column-options.png?view=azure-devops)

Tip

Each team member has several tools to configure their backlog view: **Expand/Collapse one level**, **Column Options**, **Backlog level selector**, **View options**, and **Filter** toolbar. Options set for each backlog level are distinct and persist until changed. For more information, see [Configure your backlog view](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/configure-your-backlog-view?view=azure-devops).

Some teams track bugs along with requirements on the backlog. Other teams track bugs as tasks completed in support of a requirement, so bugs appear on their [Taskboard](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/task-board?view=azure-devops). Before you determine how to manage bugs, see [Bugs as requirements or tasks](https://learn.microsoft.com/en-us/azure/devops/boards/configure-customize?view=azure-devops#show-bugs) and [Show bugs on backlogs and boards](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops).

Your backlog shows work that you plan to do or that's in progress. As soon as the **State** of a work item is set to _Done_ or _Completed_, the work item doesn't appear on your backlog. You can use the [backlog controls](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops#product-backlog-controls) to filter or change your view.

If you already defined a long list of items, you don't need to reenter them one at a time. Instead, use [bulk work items with CSV files](https://learn.microsoft.com/en-us/azure/devops/boards/queries/import-work-items-from-csv?view=azure-devops) or [Microsoft Excel](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/office/bulk-add-modify-work-items-excel?view=azure-devops) to import them to your backlog.

1.   Before you add work items, select ![Image 10](https://learn.microsoft.com/en-us/azure/devops/media/icons/view-options-icon.png?view=azure-devops)**View options** and turn the slider for **Parents** and **Forecasting** to **Off**. Optionally, turn **In Progress Items** on or off.

![Image 11: Screenshot of view options parents turned off.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/view-options-parents-off.png?view=azure-devops)

2.   To add a work item, select ![Image 12](https://learn.microsoft.com/en-us/azure/devops/media/icons/blue-add-icon.png?view=azure-devops)**New Work Item** and enter a title. Select **Enter** or select **Add to top**. The default **Area Path** and **Iteration Path** selected for the team are assigned to work items. For more information, see [Manage and configure team tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops).

![Image 13: Screenshot of work item added by using New Work Item.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/add-new-items-agile.png?view=azure-devops)

Depending on whether you create your project with [Basic](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops), [Agile](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops), [Scrum](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process?view=azure-devops), or [CMMI](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process?view=azure-devops), the items in your backlog might be called issues, user stories, PBIs, or requirements. All of these terms describe the customer value to be delivered and the work to be performed.

By default, user stories appear on Agile backlogs, issues on Basic backlogs, PBIs and bugs appear on Scrum backlogs, and requirements appear on CMMI backlogs.

Reorder your items to create a prioritized list of work. Review and prioritize your backlog frequently to help your team know what's most important to deliver next.

You can't sort your backlog on a column. To view a sorted list, select **Create query**. Save and open the query, and sort the query results. For more information about queries, see [Use the query editor to list and manage queries](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops).

To reorder your backlog, drag the work items. Or, if you prefer to use the keyboard, hold down the **Alt** key and use the up and down arrows.

![Image 14: Screenshot of Reordered work items in the backlog.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/cyb-order-backlog.png?view=azure-devops)

Note

To reorder a backlog, have at least Basic access. If you have Stakeholder access, you can't reorder backlog items. For more information, see [Stakeholder access quick reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/stakeholder-access?view=azure-devops).

Backlogs that participate in portfolio management or that contain nested same-type child items might not allow you to reorder the items. For more information, see the following articles:

*   [Work with multi-team ownership of backlog items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops#multi-team)
*   [Troubleshoot reordering and nesting issues](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/resolve-backlog-reorder-issues?view=azure-devops)

Add detailed information to each backlog item. This information helps your team estimate effort and deliver successfully.

**To edit a work item:**

1.   Double-click the item or select **Enter** to open the work item form.
2.   Add descriptions, field values, or discussion notes.
3.   Use the ![Image 15](https://learn.microsoft.com/en-us/azure/devops/boards/media/icons/icon-attachments-tab-wi.png?view=azure-devops)**Attachments** tab to share supporting files.

Provide enough detail for your team to understand scope, estimate work, create tests, and deliver the expected outcome.

Note

You can only assign work to a single user. If you need to assign work to more than one user, add a work item for each user and distinguish the work to be done by title and description. The Assigned To field only accepts user accounts that have been [added to a project or team](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops).

*   [Agile process](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops#tabpanel_1_agile-process)
*   [Basic process](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops#tabpanel_1_basic-process)
*   [Scrum process](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops#tabpanel_1_scrum-process)
*   [CMMI process](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops#tabpanel_1_cmmi-process)

For example, assign the story to Raisa Pokrovskaya and add a discussion note that at-mentions Raisa.

![Image 16: Screenshot of User Story work item form, add details.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/user-story-form-add-details.png?view=azure-devops)

Select **Save & Close** when you're done.

Use these essential fields to estimate effort and define requirements for sprint planning:

| Field | Purpose |
| --- | --- |
| [Effort](https://learn.microsoft.com/en-us/azure/devops/boards/queries/query-numeric?view=azure-devops), [Story Points](https://learn.microsoft.com/en-us/azure/devops/boards/queries/query-numeric?view=azure-devops), [Size](https://learn.microsoft.com/en-us/azure/devops/boards/queries/query-numeric?view=azure-devops) | **Estimate work required** - Use relative sizing (powers of 2, Fibonacci sequence, or your team's preferred scale). These estimates calculate [velocity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/team-velocity?view=azure-devops) and [forecast sprints](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/forecast?view=azure-devops). |
| [Business Value](https://learn.microsoft.com/en-us/azure/devops/boards/queries/query-numeric?view=azure-devops) | **Set priority** - Assign relative value compared to other items. Higher numbers indicate greater business value. |
| [Description](https://learn.microsoft.com/en-us/azure/devops/boards/queries/titles-ids-descriptions?view=azure-devops) | **Define scope** - Provide clear details about user needs and requirements. Focus on what users want to accomplish and why. |
| [Acceptance Criteria](https://learn.microsoft.com/en-us/azure/devops/boards/queries/titles-ids-descriptions?view=azure-devops) | **Define "Done"** - Describe specific criteria for completion. Establish shared understanding between team and customers for acceptance testing. |
| [Impact Assessment](https://learn.microsoft.com/en-us/previous-versions/azure/devops/boards/work-items/guidance/cmmi/guidance-requirements-field-reference-cmmi) | **Assess risk (CMMI only)** - Document customer impact of not implementing the requirement. |

Use the **View options** selector to toggle **In Progress Items** visibility. When turned off, items in _Active_, _Committed_, or _Resolved_ states (or states that map to the [In Progress category state](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/workflow-and-state-categories?view=azure-devops)) don't appear in the backlog.

![Image 17: Screenshot shows the  View options selector with In progress selected.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/in-progress-control-2020.png?view=azure-devops)

**Hide** in progress items when [forecasting work](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/forecast?view=azure-devops).

Use the **View options** selector to toggle **Completed Child items** visibility based on your needs.

![Image 18: Screenshot shows the View options selector with Completed child items selected.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/create-backlog/completed-child-items-control-2020.png?view=azure-devops)

**Show** completed child items to [view rollup columns](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/display-rollup?view=azure-devops).

**Hide** completed child items when [forecasting work](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/forecast?view=azure-devops).

Note

Completed or closed work items don't display on the backlogs and boards after their **Changed Date** value is greater than 183 days (about a half a year). You can still list these items by using a query. If you want them to show up on a backlog or board, you can make a minor change to them, which resets the clock.

Note

Completed or closed work items don't display on the backlogs and boards after their **Changed Date** value is greater than a year old. You can still list these items by using a query. If you want them to show up on a backlog or board, you can make a minor change to them, which resets the clock.

If you don't see the work items you expect on your [product Backlog](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops) or [board](https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-quickstart?view=azure-devops), complete the following checks:

1.   Make sure you selected the team backlog or board of interest. To learn how, see [Use breadcrumbs and selectors to go to and open artifacts](https://learn.microsoft.com/en-us/azure/devops/project/navigation/use-breadcrumbs-selectors?view=azure-devops).

2.   [Create a query](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops) of your backlog items, specifying the work item types that belong to your Requirements category and the Area Path associated with your team, for example:

![Image 19: Screenshot shows Requirement category query.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/setup-backlog/requirements-query.png?view=azure-devops)

3.   Add the **State**, **Area Path**, and **Iteration Path** fields to the [column options](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/set-column-options?view=azure-devops).

4.   Check the query results and that the values of the work items you expect to show up on your backlog meet these criteria:

    *   **Area Path** belongs to your team's area path(s)
    *   **Iteration Path** belongs under your team's default iteration path
    *   **State** isn't Closed, Completed, Done, or Removed.

Note

You can also filter your product backlog to show or hide work items that are in an **In Progress** state category, corresponding to an Active, Resolved, Committed, Doing workflow state.

The following settings influence the type and number of work items that appear in your backlogs and boards.

*   In your board, newly added work items don't appear if they're stack ranked lower within the product backlog. By choosing **Show more items**, you can cause the board to refresh and display more work items.

![Image 20: Screenshot shows Boards, Show more items.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/setup-backlog/show-more-items.png?view=azure-devops)

*   If you turn off the **In Progress** view, work items where work has started don't appear in the backlog list.

![Image 21: Screenshot shows Backlogs, View Options, Hide In Progress sequence.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/setup-backlog/hide-in-progress-s155.png?view=azure-devops) 
*   Work items appear in the priority order in which you add or move them. You manage this order or sequence by the **Stack Rank** (Basic, Agile, and CMMI processes) or **Backlog Priority** (Scrum) field. For more information, see the Stack rank section in [Backlogs, portfolios, and Agile project management](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops#stack-rank).

*   Each backlog displays up to 999 work items. If your backlog exceeds this limit, consider adding a team and moving some of the work items to the other team's backlog.

*   Sprint backlogs show only those work items that meet the team's area path and the **Iteration Path** defined for the sprint.

*   Inheritance process model: If an administrator [disables or deletes a work item type](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/customize-process-work-item-type?view=azure-devops#enable-disable), it doesn't appear on backlogs and boards.

*   On-premises XML process model: If an administrator [deletes or destroys a work item type](https://learn.microsoft.com/en-us/azure/devops/reference/witadmin/witadmin-import-export-manage-wits?view=azure-devops), it doesn't appear on backlogs and boards.

If you configure the [Azure DevOps MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops), you can use AI assistants to manage your backlog by using natural language prompts.

| Task | Example prompt |
| --- | --- |
| Get backlog items | `Get list of work items for <Stories> backlog in <Contoso> project` |
| View my work items | `Get my work items for project <Contoso>` |
| Create work items | `Create a new user story in <Contoso> project with title '<Add search functionality>'` |
| Update work items | `Update work item <1234> with Story Points = <5> and State = <Active>` |
| Prioritize backlog | `Get all work items in the product backlog for <Contoso> and prioritize them for a <two-week> sprint with <three> developers` |
| Triage work | `List work items for <Stories> backlog, find all security-related bugs, and assign the first <4> to the current iteration` |
| Find backlog gaps | `List features in <Contoso> that have no child user stories` |
| Estimate effort | `Show all user stories in <Contoso> project that are active but have no story points assigned` |
| Backlog health check | `List all work items in <Contoso> backlog that have been in the New state for more than 30 days` |
| Split large items | `Show user stories in <Contoso> with story points greater than 13 that are still in the New state` |
| Balance workload | `Show the count of active backlog items per team member in area path <Contoso\\Frontend>` |
| Track dependencies | `List user stories in <Contoso> that have predecessor links to items that aren't yet completed` |

Tip

If you're using Visual Studio Code, [agent mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context#agent-mode) is especially helpful for troubleshooting complex backlog scenarios.

*   To avoid using stale or cached data from previous queries, add to your prompt, "Do not use previously fetched data."

With your backlog in place, your team can begin work on the top-priority items. Now it's time to decide how you want to work as a team. Choose your team's workflow: Scrum for structured sprints or Kanban for continuous flow. You can use these methods independently or together.

*   [Configure and customize Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/configure-customize?view=azure-devops)
*   [Bulk modify work items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/bulk-modify-work-items?view=azure-devops)
*   [Interactively filter backlogs, boards, queries, and plans](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/filter-backlogs-boards-plans?view=azure-devops)
*   [Backlog priority or stack rank order](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops#stack-rank)
*   [Add a team, move from one default team to several teams](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams?view=azure-devops)
