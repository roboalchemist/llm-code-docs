# Source: https://learn.microsoft.com/en-us/azure/devops/report/dashboards/overview

Title: Understand dashboards, charts, reports, and widgets - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/report/dashboards/overview

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Gain visibility into your team's progress by adding one or more widgets or charts to your dashboard. Customizable, highly configurable dashboards provide you and your teams with the flexibility to share information, monitor progress and trends, and improve your workflow processes. Each team can tailor their dashboards to share information and monitor their progress.

If you're just starting out, read [Add, rename, and delete dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops). Looking for instructions on a specific task, in-context chart, widget, or report? See [Dashboards, charts, and quick reference](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/quick-ref?view=azure-devops). For more information, see the [Reporting roadmap](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/reporting-roadmap?view=azure-devops).

Important

![Image 1: Select a version from Azure DevOps Content Version selector.](https://learn.microsoft.com/en-us/azure/devops/media/version-selector.png?view=azure-devops)

Access to Azure DevOps web portal features are managed through access levels assigned to users.

The following features provide support for viewing Azure DevOps data through the web portal:

*   **Dashboards**: Customizable interactive signboards that provide real-time information. Dashboards are associated with a team or a project and display configurable charts and widgets.
*   **Charts**: Query-based status or trend charts derived from a work item query or test results.
*   **Widgets**: Items that display configurable information and charts on dashboards. The widget catalog provides brief descriptions of those widgets available to you. Also, you can add widgets provided through [Azure DevOps Marketplace](https://marketplace.visualstudio.com/azuredevops).
*   **In-context reports**: System-generated charts that support specific services. Examples are team velocity, sprint burndown, the Cumulative Flow Diagram (CFD), and the **Test failures** report. These reports are displayed on the **Analytics** tab for a specific service and derive data from Analytics.

The following features provide support for viewing Azure DevOps data by using Power BI:

*   **Analytics views**: Provide a simplified way to specify the filter criteria for a Power BI report based on Analytics data for Azure Boards data. For more information, see [About Analytics views](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/what-are-analytics-views?view=azure-devops).
*   **Power BI reports**: Allow users to create rich, customized Power BI reports or other reports using OData queries of Analytics data and the returned JSON data. For on-premises Azure DevOps environments, project collections must be configured to support the Inherited process.

Note

Open Data Protocol (OData) is an ISO/IEC approved, OASIS standard that defines a set of best practices for building and consuming REST APIs. For more information, see [OData documentation](https://learn.microsoft.com/en-us/odata/).

Users with **Stakeholder** access get restricted privileges, granting them access to only those features outlined in the following table. For more information, see [About access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops). In addition to access levels, certain features require permissions to execute.

**Supported features and tasks**

**Stakeholder**

**Basic**

* * *

Dashboards (View)

✔️

✔️

Dashboards (Create and edit)

✔️

Charts, Widgets (View)

✔️

✔️

Charts, Widgets (Add and configure)

✔️

In-context reports

✔️

✔️

Analytics views

✔️

Power BI reports

✔️

✔️

SQL Server reports

✔️

✔️

* * *

**Task**

**Readers**

**Contributors**

**Team admins**

**Project admins**

* * *

View team and project dashboards

✔️

✔️

✔️

✔️

Add and configure project dashboards

✔️

✔️

* * *

For Power BI Integration and Analytics views, you set [permissions](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/analytics-security?view=azure-devops) for the service at the project level, and for shared Analytics views at the object level.

**Task**

**Readers**

**Contributors**

**Project admins**

* * *

View Analytics

✔️

✔️

✔️

View a shared Analytics view

✔️

✔️

Add a private or shared Analytics view

✔️

✔️

Edit and delete shared Analytics views

✔️

* * *

With dashboards, you can configure an array of charts and widgets.

Each team can [add and configure multiple dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops) to:

*   Share information.
*   View status, progress, and trends.
*   Access quick links and other functions.

Easily add and rearrange widgets on the dashboard to show recent changes made to view build status, bug trends, and more.

![Image 2: Screenshot that shows an example dashboard.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/dashboard-view-with-widgets.png?view=azure-devops)

Select one of the following boxes to open the corresponding article.

[![Image 3: Diagram is a link to Add dashboard article.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-add-dashboard.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards?view=azure-devops)[![Image 4: Diagram is a link to Add widget article.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-add-widget.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/add-widget-to-dashboard?view=azure-devops)

With flat-list queries, you can create various charts to monitor status, progress, and trends. Before you monitor work progress and trends, [plan your project and make progress on work you're tracking](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops).

You can open a shared query, create a chart, and add it to the dashboard. After the chart is added to the dashboard, you can change the **Chart for work items** widget configuration to resize or change the chart parameters. Or, from the dashboard, you can add a **Chart for work items** widget and choose a shared query and set the chart parameters. You have multiple chart types from which to choose. Status charts include pie, bar, column, stacked bar, and pivot. Trend charts include stacked area, line, and area.

For more information, see [Define a query](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops) and [Track progress with status and trend query-based charts](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/charts?view=azure-devops).

![Image 5: Screenshot that shows Active bug charts added to dashboards.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/overview/active-bug-charts-on-dashboards-2019.png?view=azure-devops)

Select one of the following boxes to open the corresponding article.

[![Image 6: Diagram that is a link to Edit query article.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-chart-query.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops)[![Image 7: Diagram is a link to create a chart article.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-chart-create.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/add-charts-to-dashboard?view=azure-devops)[![Image 8: Diagram is a link to Add chart to dashboard article.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-chart-add-dashboard.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/add-charts-to-dashboard?view=azure-devops)

The steps to creating charts that track manual testing progress and results are similar to the ones for tracking work. The starting point is the test plan rather than a query. For example, you can find out how many test cases are ready to run, or how many tests are passing and failing in each test suite. And, just like work item query-based charts, you can add these charts to a dashboard.

For more information, see:

*   [Create test plans and test suites](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops)
*   [Create manual test cases](https://learn.microsoft.com/en-us/azure/devops/test/create-test-cases?view=azure-devops)
*   [Track testing progress](https://learn.microsoft.com/en-us/azure/devops/test/track-test-status?view=azure-devops#charts)

![Image 9: Screenshot that shows the Web Team test plan is a chart showing counts of tests in various stages, with tests broken down by suite.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/gs-monitor-test-charts.png?view=azure-devops)

You add widgets to a dashboard to display a chart, information, or set of links. Most widgets are configurable. For a description of each supported widget for your platform and version, see the [Widget catalog](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops). Here are the widgets that support the indicated service.

Widgets are annotated as follows:

*   **Analytics**: Widget derives data from [Analytics data](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/what-is-analytics?view=azure-devops).
*   **Build**: Widget derives data for a selected build pipeline.
*   **Project**: Widget indicates you can select the project and team when you configure the widget.
*   **Release**: Widget derives data for a selected release pipeline.
*   **Team**: Widget is scoped to a single team.
*   **Teams**: Widget is scoped to one or more teams.
*   **User**: Widget is scoped to the signed-in user account.

* * *

**Boards**

*   [Assigned to Me](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#assigned-to-me-widget) (User)
*   [Burndown](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#burndown-analytics-widget) (Analytics, Project, Teams)
*   [Burnup](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#burnup-analytics-widget) (Analytics, Project, Teams)
*   [Chart for Work Items](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#chart-wit-widget)
*   [Cumulative Flow Diagram](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#cfd-widget) (Team)
*   [Cycle Time (Analytics)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#cycle-time-widget) (Analytics, Team)
*   [Lead Time (Analytics)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#lead-time-widget) (Analytics, Team)
*   [New Work Item](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#new-work-item-widget)
*   [Query Results](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#query-results-widget)
*   [Query Tile](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#query-tile-widget)
*   [Sprint Burndown](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-burndown-analytics-widget) (Analytics, Team)
*   [Sprint Burndown - Legacy](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#burndown-widget) (Team)
*   [Sprint Capacity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-capacity-widget) (Team)
*   [Sprint Overview](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-overview-widget) (Team)
*   [Velocity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#velocity-widget) (Analytics, Team)
*   [Work Links](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#work-links-widget)

* * *

**Code**

*   [Code Tile](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#code-tile-widget) (Repository, Branch, Folder)
*   [Pull Request](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#pull-request-widget) (Team)

* * *

[![Image 10](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-sprint-capacity.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-capacity-widget)[![Image 11](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-sprint-burndown.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops#sprint-burndown-analytics-widget)

There's no chart or widget that tracks changes to sprint scope. However, you can determine work items added to a sprint or moved out of a sprint by using the Query Editor. For more information, see [Query sprint scope changes](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/scrum-overview?view=azure-devops#sprint-scope-change).

![Image 12: Screenshot that shows a Cumulative Flow Diagram widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/cfd-example-rolling-30-days.png?view=azure-devops)

With the code tile widgets, you can monitor the activity occurring within a repository or branch folder. Build history displays a histogram of all builds run for a specific build pipeline. Bar colors use green for completed, red for failed, and yellow for completed without tests.

![Image 13: Screenshot that shows a Code tile widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-code-tile.png?view=azure-devops)

![Image 14: Screenshot that shows a Pull request widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-catalog-pull-request.png?view=azure-devops)

![Image 15: Screenshot that shows a Build history widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-deployment-status.png?view=azure-devops)

![Image 16: Screenshot that shows a Deployment status widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/widget-build-history-chart.png?view=azure-devops)

The Analytics service is the reporting platform for Azure DevOps. As described in [What is Analytics?](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/what-is-analytics?view=azure-devops), it replaces the previous platform based on SQL Server Reporting Services. The Analytics service supports Analytics widgets, [in-context Analytics reports](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/overview#work-tracking-analytics), and Analytics views for Power BI reporting. For more information, see [About Analytics views](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/what-are-analytics-views?view=azure-devops).

![Image 17: Screenshot that shows a Lead time widget.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/lead-time-control-chart.png?view=azure-devops)

For more information, see [Widgets based on Analytics data](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/analytics-widgets?view=azure-devops) and [Add an Analytics widget to a dashboard](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/add-widget-to-dashboard?view=azure-devops#add-analytics-widget).

Azure Boards provides several in-context reports that derive from Analytics data. From your backlog or board, you can view the Cumulative Flow Diagram and team Velocity reports by selecting the **Analytics** tab. Each report provides interactive controls to provide each user the view of interest to them. From a Sprint backlog, you can view the Sprint Burndown Trend.

Use the interactive controls to choose the time frame, swimlanes, and workflow states or board columns.

[![Image 18: Screenshot that shows open CFD analytics.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/cfd/analytics-cfd-azure-devops.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/cfd/analytics-cfd-azure-devops.png?view=azure-devops#lightbox)

Use the interactive controls to choose the count or sum field and number of iterations.

![Image 19: Screenshot that shows open Velocity analytics.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/velocity/analytics-velocity-azure-devops.png?view=azure-devops)

Use the interactive controls to choose the start and end of the sprint and count or sum field to use in the burndown. If you don't track Remaining Work in tasks, you can view burndown based on a count of work items or tasks.

[![Image 20: Screenshot that shows Burndown Trend based on Remaining Work.](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/media/burndown/analytics-burndown-remaining-work.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/boards/sprints/media/burndown/analytics-burndown-remaining-work.png?view=azure-devops#lightbox)

You can add the in-context reports to a dashboard by using the copy to dashboard option from the report's context menu.

![Image 21: Screenshot that shows an Analytics in-context report with the Copy to dashboard action.](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/media/add-charts/add-analytics-chart-abbreviated.png?view=azure-devops)

For more information about these reports, see:

*   [Cumulative flow](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/cumulative-flow?view=azure-devops)
*   [Team velocity](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/team-velocity?view=azure-devops)
*   [Sprint burndown](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/configure-sprint-burndown?view=azure-devops)

Several in-context reports are provided for Azure Pipelines. These reports derive from Analytics data. Open a pipeline or release summary for **Test failures** to view the reports and select the **Analytics** tab. Select **View full report** on a summary card for a detailed report.

![Image 22: Screenshot that shows the Analytics tab.](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/media/pipelines-reports/analyticstab.png?view=azure-devops)

For more information on each in-context Analytics report for pipeline runs, see:

*   [Historical graph for agent pools (preview)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pool-consumption-report?view=azure-devops)
*   [Pipeline pass rate report](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops#pipeline-pass-rate-report)
*   [Test pass rate report](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops#test-failures-report)
*   [Pipeline duration report](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops#pipeline-duration-report)
*   [Test analytics for builds](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-analytics?view=azure-devops)
*   [Test analytics for releases](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-analytics?view=azure-devops)

The **Pipeline pass rate** report provides a trend of pipeline failure and task failure of the pipeline. You can view the pass rate of the pipeline over a configurable period of time, for example, 7, 14, or 30 days. Find more details in **Task failure details**, which not only highlights the trend but also lists the top failing tasks.

![Image 23: Screenshot that shows a summary of the pipeline pass rate report.](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/media/pipelines-reports/top-failing.png?view=azure-devops)

For more information, see [Pipeline pass rate report](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops#pipeline-pass-rate-report).

The **Test failures** report provides a granular view of the top failing tests in the pipeline, along with the failure details. Summary charts are also provided for builds that indicate code coverage and test failures or success.

[![Image 24: Screenshot that shows a Test analytics detail view.](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/media/test-analytics/test-failures.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/media/test-analytics/test-failures.png?view=azure-devops#lightbox)

For more information, see [Test failures report](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-analytics?view=azure-devops#test-failures).

The **Pipeline duration** report provides the duration trend of a pipeline. It also highlights the average run time of the total successful runs over a period of time, for example, for 7, 14, or 30 days. The report also provides insights on the tasks that affected the duration of the pipeline.

![Image 25: Screenshot that shows pipeline duration summary.](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/media/pipelines-reports/duration-summary.png?view=azure-devops)

![Image 26: Screenshot that shows a pipeline duration trend.](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/media/pipelines-reports/duration-trend.png?view=azure-devops)

For more information, see [Pipeline duration report](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops#pipeline-duration-report).

In addition to the widgets available in the widget catalog, you might find interesting widgets in the [Marketplace](https://marketplace.visualstudio.com/search?term=webpage%20widget&target=VSTS&sortBy=Relevance).

Or, you can create your own widget by using the REST API. For more information, see [Add a dashboard widget](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-dashboard-widget?view=azure-devops).

Azure provides various reporting tools and services to help you monitor and analyze the usage and performance of your resources, such as Virtual Machines (VMs), services, and overall usage.

Azure Monitor is a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments. It helps you understand how your applications are performing and proactively identifies issues affecting them and the resources they depend on.

For more information, see [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview).

Azure Resource Graph lets you explore and query your Azure resources at scale. It lets you query across subscriptions and management groups, which makes it easier to manage large environments.

For more information, see [What is Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview).

Azure Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments. It analyzes your resource configuration and usage, and then recommends solutions to help improve the cost-effectiveness, performance, high availability, and security of your Azure resources.

For more information, see [Introduction to Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview).

*   [FAQs on Azure DevOps dashboards, charts, and reports](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/faqs?view=azure-devops)
*   [Widget catalog](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog?view=azure-devops)
*   [Best practices for Agile project management](https://learn.microsoft.com/en-us/azure/devops/boards/best-practices-agile-project-management?view=azure-devops)
*   [Cross-service overview](https://learn.microsoft.com/en-us/azure/devops/cross-service/cross-service-overview?view=azure-devops)
