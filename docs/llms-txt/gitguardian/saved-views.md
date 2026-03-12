# Source: https://docs.gitguardian.com/platform/collaboration-and-sharing/saved-views.md

# Saved views

> Create and manage saved views to filter and organize secret incidents in the GitGuardian dashboard.

Saved views allow users to save and share customized filter sets, making it easier to collaborate and maintain consistent views across teams.

## Key benefits
- Shared views: Workspace managers can create shared views accessible to all team members, enabling smoother workflows and reducing the time spent configuring filters.
- Personalized experience: While the primary focus is on sharing, members can also create private views tailored to their individual needs. Each user can then customize their session by adding or hiding views according to their preferences.
- Dynamic filtering: The "Current user" filter enables views to dynamically adjust and display relevant data for each user, such as "My Incidents," providing a personalized and relevant experience even in shared views.
![Filter on current user](/img/platform/collaboration-and-sharing/saved-views/current-user-filter.png)

## How to create a new view
1. Set your desired filters in an existing view.
2. Click "Save" > "Save as new view."
3. Enter a name for the view and save.

:::info
If youâre a workspace manager, choose whether it should be available to everyone or just to you. Members can only create private views.
:::

![Save as new view](/img/platform/collaboration-and-sharing/saved-views/save-as-new-view.png)
![Create view modal for manager](/img/platform/collaboration-and-sharing/saved-views/create-new-view-manager.png)

## GitGuardian views
In addition to user-created views, GitGuardian provides pre-configured views with recommended filter sets. These views help users quickly access common data configurations. While these views can be hidden, they cannot be edited or deleted. Learn more about:
- [Views for the incidents page](../../internal-monitoring/remediate/prioritize-incidents.md#1-prioritize-with-the-incidents-table)
- [Views for the perimeter page](../../internal-monitoring/integrate-sources/monitored-perimeter.md)

## AI Filters

AI Filters transforms how you create filters by using natural language queries. Instead of manually configuring complex filter combinations, simply describe what you're looking for in plain English.

**Available in:** Incidents, Perimeter, and Audit Logs

**How to use:**
1. Type your request in natural language (e.g., "Show me critical incidents from last week")
2. AI automatically converts your query into the appropriate filters
3. Results appear instantly, and filters work alongside your existing settings
4. Save successful queries as views for future use

**Key benefits:**
- **Save time**: No more navigating complex filter menus
- **Natural language**: Ask questions as you would to a colleague
- **Smart filtering**: AI understands context and applies the right filters
- **Works with saved views**: Save AI-generated filters for team sharing

For self-hosted customers, you can bring your own AI key (BYOK) for complete data control. Learn more about [self-hosted configuration](../../self-hosting/management/application-management/admin-area#ai-filters).
