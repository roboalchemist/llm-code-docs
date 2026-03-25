# Source: https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops

Title: Plan and track work in Azure Boards - Azure Boards

URL Source: https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Use Azure Boards to plan and track work with the Agile, Basic, Scrum, or Capability Maturity Model Integration (CMMI) processes. For more information about process choices, see [About processes and process templates](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/choose-process?view=azure-devops).

*   [Agile process](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops#tabpanel_1_agile-process)
*   [Basic process](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops#tabpanel_1_basic-process)
*   [Scrum process](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops#tabpanel_1_scrum-process)
*   [CMMI process](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops#tabpanel_1_cmmi-process)

The Agile process uses user stories, tasks, bugs, features, and epics to plan and track work. Add user stories and group them into features when you need higher-level planning. Add tasks to a user story to track smaller units of work.

| Work item types | Backlog hierarchy |
| --- | --- |
| ![Image 1: Screenshot showing Agile process work item types in a hierarchy.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/about-boards/agile-process-wits.png?view=azure-devops) | ![Image 2: Screenshot showing Agile process hierarchical backlog.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/about-boards/agile-hierarchy.png?view=azure-devops) |

Use the work item form to describe the work, assign owners, track status, and collaborate with the team through the **Discussion** section. This article shows how to add user stories, create child tasks, and update work items from the web portal.

| Category | Requirements |
| --- | --- |
| Access levels | - Add work items and use board features: at least [**Basic** access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops). - Private project: to view boards, open and modify work items, and add child tasks: at least **Stakeholder** access (Stakeholders can't reorder or reparent backlog items or update fields on cards). - Public project: for full access to all Boards features: at least **Stakeholder** access. |
| Permissions | Member of the **Contributors** or **Project Administrators** group. |

For more information, see [Default permissions and access for Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/permissions-access-boards?view=azure-devops).

A team board exists for each team in a project. To open a board:

1.   Sign in to your organization at `https://dev.azure.com/{Your_Organization}` and go to your project.
2.   Select **Boards**>**Boards**. ![Image 3: Screenshot showing navigation to Boards in the project menu.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/open-boards.png?view=azure-devops)
3.   Select a board from the **All Team Boards** dropdown. ![Image 4: Screenshot showing the All Team Boards dropdown.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/select-from-all-team-boards-dropdown-menu.png?view=azure-devops)

Boards automatically assign the team's default **Area Path** and **Iteration Path** to new work items. See [Manage and configure team tools](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/manage-teams?view=azure-devops) for team settings.

To add items:

*   Agile: On the Stories board, choose **New item**, type a title, and press Enter. ![Image 5: Screenshot showing adding a new user story on the Stories board.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/new-user-story-kanban-board.png?view=azure-devops)
*   Basic: On the Issues board, choose **New item**, type a title, and press Enter. ![Image 6: Screenshot showing adding a new issue on the Issues board.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/track-issues/issues-board-new-item.png?view=azure-devops)
*   Scrum: On the Backlog items board, choose **New item**, type a title, and press Enter. ![Image 7: Screenshot showing adding a new backlog item on the Backlog items board.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/new-scrum-item-kanban-board.png?view=azure-devops)
*   CMMI: On the Requirements board, choose **New item**, type a title, and press Enter. ![Image 8: Screenshot showing adding a new requirement on the Requirements board.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/new-user-story-kanban-board-cmmi.png?view=azure-devops)

The system assigns an ID when you create the work item.

Tip

To add features and child items quickly, choose **Features** from the board selector.

![Image 9: Screenshot showing the Features board selector.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/choose-features-board.png?view=azure-devops)

To track implementation details, create tasks from a parent work item.

1.   Open the parent card's actions menu and choose **Add Task** (the green plus icon). ![Image 10: Screenshot showing Add Task from a work item card menu.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/add-child-task.png?view=azure-devops)

2.   Type the task title and press Enter. ![Image 11: Screenshot showing entering a task title.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/prep-images-task.png?view=azure-devops)

3.   To add multiple tasks quickly, continue typing titles and press Enter after each.

Tasks inherit the parent's **Area Path** and **Iteration Path** and appear on sprint taskboards.

You can:

    *   Mark a task complete by selecting its checkbox (State changes to **Done**).

![Image 12: Screenshot showing tasks marked as done.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/mark-tasks-as-done.png?view=azure-devops)

    *   Reorder or reparent tasks by dragging them in the checklist.

![Image 13: Screenshot showing reordering a task.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/reorder-task.png?view=azure-devops)

    *   Expand or collapse a task checklist.

![Image 14: Screenshot showing a collapsed task checklist.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/collapse-task-list.png?view=azure-devops)

To edit a work item, select its title. Update field values, add a description, or add a discussion note. Use the **Attachments** tab to upload files by drag-and-drop. ![Image 15: Screenshot showing details on a user story work item form.](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/media/plan-track-work/user-story-form-add-details.png?view=azure-devops)

When you finish editing, select **Save & Close**.

Drag work item cards between columns to update their State.

You can use these fields on backlog items and tasks to support planning and capacity tracking.

Note

Tasks show "h" for hours on the taskboard, but you can track work in any unit your team prefers.

**Field**

**Usage**

* * *

The discipline for CMMI tasks (for example, Analysis, Development, Test).

The estimated work required to complete a task.

The amount of work left to finish a task. Use hours or days. Update this field as work progresses; it's used by capacity charts and the sprint burndown.

The time spent implementing a task. Enter this value when you complete the task.

Select the appropriate task type for CMMI tasks (for example, Corrective Action, Mitigation Action, Planned).

Use the **Discussion** section to add and review comments made about the work being performed.

![Image 16: Screenshot of Discussion section within a work item form.](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/media/discussion-section.png?view=azure-devops)

The rich text editor toolbar appears under the text entry area when you place your cursor in any text box that supports text formatting.

![Image 17: Screenshot of Discussion section, Rich Text Editor toolbar.](https://learn.microsoft.com/en-us/azure/devops/boards/queries/media/share-plans/discussion-rich-text-editor-toolbar.png?view=azure-devops)

Note

A Discussion work item field doesn't exist. To query work items with comments from the Discussion area, filter on the [History field](https://learn.microsoft.com/en-us/azure/devops/boards/queries/history-and-auditing?view=azure-devops). The full content of the text entered in the Discussion text box is added to the History field.

Select one of the following icons to open a menu of recent entries where you mentioned someone, linked to a work item, or linked to a pull request:

*   ![Image 18](https://learn.microsoft.com/en-us/azure/devops/media/icons/at-mention.png?view=azure-devops)
*   ![Image 19](https://learn.microsoft.com/en-us/azure/devops/media/icons/work-id.png?view=azure-devops)
*   ![Image 20](https://learn.microsoft.com/en-us/azure/devops/media/icons/pr-id.png?view=azure-devops)

You can open the same menu by using keyboard shortcuts: at-mention **@**, hash tag **#**, and exclamation point **!**.

![Image 21: Screenshot of Discussion section, at-mention drop-down menu people-picker.](https://learn.microsoft.com/en-us/azure/devops/boards/media/discussion-at-mention.png?view=azure-devops)

Enter a name or number to filter the menu list to match your entry. Select the entry you want to add. To bring a group into the discussion, enter the **at** symbol **@** followed by the group name, such as a team or security group.

To edit or delete any of your discussion comments, select **Edit**![Image 22](https://learn.microsoft.com/en-us/azure/devops/media/icons/edit.png?view=azure-devops) or **More actions** (![Image 23](https://learn.microsoft.com/en-us/azure/devops/media/icons/actions-icon.png?view=azure-devops) ) and then select **Delete**:

![Image 24: Screenshot of Discussion section where you can choose Edit or Delete actions.](https://learn.microsoft.com/en-us/azure/devops/boards/media/discussion-edit-delete.png?view=azure-devops)

After you update the comment, select **Update**. To delete the comment, confirm the deletion. The **History** tab on the work item form maintains a full audit trail of all edited and deleted comments.

Add one or more reactions to a comment by choosing an emoji icon at the top right of any comment. Choose from the icons at the bottom of a comment next to any existing reactions. To remove your reaction, choose the reaction on the bottom of your comment. The following image shows an example of the experience of adding a reaction, and the display of reactions on a comment.

![Image 25: Screenshot of Discussion section, add a reaction to a comment.](https://learn.microsoft.com/en-us/azure/devops/boards/media/discussion-comments-reactions.png?view=azure-devops)

Note

This feature is available starting in Azure DevOps Server 2022.1.

If you only have permissions to add to the **Discussion** of a work item, then you can do so by saving comments. This permission is controlled by Area Path nodes and the **Edit work item comments in this node** permission. For more information, see [Set work tracking permissions - Create child nodes, modify work items under an area or iteration path](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops#set-permissions-area-path).

When you save the comments, you don't need to save the work item.

![Image 26: Screenshot of Discussion section, save comment.](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/media/view-add/save-comments-discussion-control.png?view=azure-devops)

Note

When you save changes made to the **Discussion** control, only the comment is saved. No [work item rules](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/rule-reference?view=azure-devops) defined for the work item type are executed.

If you have the [Azure Boards MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops) connected to your AI agent in agent mode, you can use natural language prompts to create and manage work items.

| Task | Example prompt |
| --- | --- |
| Create a work item | `Create a user story called 'Add search functionality to the product page' and assign it to <me>` |
| Add child tasks | `Add three tasks to user story #1234: design the UI mockup, implement the backend API, and write unit tests` |
| Create a bug | `Create a new bug titled 'Login timeout on slow connections' with priority 1 and assign it to the current sprint` |
| Update a work item | `Update the state of task #5678 to Done and set Completed Work to 4 hours` |
| Get a daily summary | `Show all work items assigned to <me> grouped by state with remaining work totals` |
| Plan a new feature | `Create a feature called 'Dark mode support' in <Contoso> with 4 child user stories for settings UI, theme engine, persistence, and accessibility testing` |
| Review sprint readiness | `List all user stories in the next sprint for <Contoso> that are still missing story points or acceptance criteria` |
| Track team progress | `Show the count of work items by state for each team member in the current sprint for <Contoso>` |
| Quick standup report | `Show what <me> completed yesterday, what's in progress today, and any items tagged 'blocked' in <Contoso>` |
| Set up a new project | `Create an epic called 'Mobile App v2' in <Contoso> with 3 child features for authentication, dashboard, and notifications, each with 2 user stories` |

Note

Agent mode and the MCP Server use natural language, so you can adjust these prompts or ask follow-up questions to refine the results.

*   [Review Azure Boards FAQs](https://learn.microsoft.com/en-us/azure/devops/boards/faqs?view=azure-devops)
*   [Add tags to issues or tasks](https://learn.microsoft.com/en-us/azure/devops/boards/queries/add-tags-to-work-items?view=azure-devops)
