# Source: https://docs.port.io/usage-dashboard.md

# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/usage-dashboard.md

# Usage dashboard

The usage dashboard provides visibility into how your Port environment is being used across your organization.<br /><!-- -->Use these insights to optimize adoption, identify engagement opportunities, and maximize the value your teams get from Port.

The dashboard tracks key metrics across five areas:

* **User activity** - monitor user activation and engagement patterns.
* **Entities** - track catalog growth and entity distribution.
* **Actions & automations** - measure self-service adoption.
* **Data sources** - understand integration usage.
* **AI & MCP** - analyze AI agent and MCP interactions.

Multi-organization support

The dashboard is only available for customers who have completed the migration to the [multi-organization](/sso-rbac/multi-organization.md) structure.

## Access the dashboard[â](#access-the-dashboard "Direct link to Access the dashboard")

To access the usage dashboard:

1. Go to the [Builder page](https://app.getport.io/settings/data-model) of your portal.
2. In the left sidebar, select **Usage dashboard**.

## Dashboard tabs[â](#dashboard-tabs "Direct link to Dashboard tabs")

The usage dashboard is organized into five tabs, each providing specific insights into different aspects of your Port environment usage.

All metrics are aggregated at the company level across all organizations. Individual tables include detailed breakdowns by organization, allowing you to drill down into organization-specific data when needed.

### Users activity[â](#users-activity "Direct link to Users activity")

The users activity tab provides insights into user adoption and engagement patterns across your organization. This includes active seats tracking, team engagement metrics, individual user activity, and page visit analytics.

### Entities[â](#entities "Direct link to Entities")

The entities tab provides visibility into your software catalog growth and composition. View entity counts over time, distribution across blueprints, and detailed logs by organization.

### Actions & automations[â](#actions--automations "Direct link to Actions & automations")

The actions and automations tab tracks self-service action and automation usage across your organization. Monitor automation runs, action executions, and view detailed breakdowns by organization, user, role, team, etc.

### Data sources[â](#data-sources "Direct link to Data sources")

The data sources tab provides visibility into your connected integrations. Track the number of data sources over time and view detailed logs including type, name, and creation date per organization.

### AI & MCP[â](#ai--mcp "Direct link to AI & MCP")

Port's AI interfaces provide intelligent assistance across your entire software development lifecycle.<br /><!-- -->Note that all AI features are currently in **open beta**, to learn more about AI capabilities in Port, see the [AI interfaces](/ai-interfaces/overview.md) documentation.

The AI and MCP tab provides analytics on AI agent usage and MCP interactions. View monthly interaction trends, invocation sources, and usage per user.

"Other" category in AI invocations

The "Other" category in the "AI invocations by source" report refers to AI invocations that didn't include the source key as part of the API call, such as invocations from custom automations or direct API calls.

## Export data[â](#export-data "Direct link to Export data")

All tables and visualizations in the usage dashboard can be exported for further analysis.

**Export individual reports:**

To export a specific table or chart:

1. Click the `...` button in the top right corner of any table or chart.
2. Click **Download results**.
3. Choose the format to download: **csv**, **xlsx**, or **json**.
4. Click **Download**.
5. The file will be downloaded locally in the chosen format.

**Export entire dashboard:**

To export the entire dashboard tab:

1. Click on the download button in the top right corner of the usage dashboard window.
2. The dashboard will be downloaded in PDF format.

## Limitations[â](#limitations "Direct link to Limitations")

* The dashboard is only available for customers who have completed the migration to the [multi-organization](/sso-rbac/multi-organization.md) structure.
* The dashboard is available to organization admins with enterprise account only.
* Usage data is not currently available via the API.
* Entity count data is available from **November 2025** onwards.
* User activity data is available from **July 2025** onwards.

## FAQs[â](#faqs "Direct link to FAQs")

**Why don't I see the complete history for total monthly entities or user activity? (click to expand)**

Historical data availability varies by metric:

* **Entity count data** is available from November 2025 onwards.
* **User activity data** is available from July 2025 onwards.

Data from before these dates is not available in the system.

**What is the "Other" category in the "AI invocations by source" report? (click to expand)**

"Other" refers to AI invocations that didn't include the "source" key as part of the API call. This typically includes invocations from custom automations or direct API calls in your code.

**Can I filter the dashboard by organization, timeframe, or team? (click to expand)**

Currently, the dashboard is static and does not support filtering by organization, timeframe, or team.

As a workaround, you can export the data (CSV, XLSX, or JSON) and apply filters locally using your preferred tools.

**Is usage data available via API or MCP? (click to expand)**

Usage dashboard data is not currently available via API or MCP.

Some related data is available through Port's regular API, such as:

* [Data sources list](/api-reference/get-all-integrations.md).
* [Run history (via the audit log)](/api-reference/get-audit-logs.md).
