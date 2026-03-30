# Source: https://docs.axonius.com/docs/agent-coverage-dashboards.md

# Agent Coverage Dashboards

After you finish [setting up your device scopes and policies](/docs/initial-settings-and-policies), you can generate a **dashboard** for each tool in the **Agents Deployment Status** table.

The charts in each dashboard are dynamic: they visualize posture, KPIs and trends that are synchronized with real-time changes in configuration and policies, updated in the Agent Coverage page.

<Callout icon="💡" theme="warn">
  Important

  * All Agent Coverage dashboard are **managed by Axonius**. That means that you cannot edit any of the charts on the dashboard. You can only make edits to your scopes and policies in the Agent Coverage page, and these which will automatically reflect in the dashboard charts.

  * You can add custom charts to each dashboard, however, these charts **will not** be automatically updated when you make changes to the Agent Coverage page.
</Callout>

## Generating a Dashboard

To generate a tool-specific dashboard, go to the **Agents deployment status** table and from the **Actions** column, select **Dashboard**.
The **Dashboard** option is available only for tools whose configuration status is Done, which means you've completed all configurations required to define this tool's coverage scope. When the status is Incomplete Setup, the **Dashboard** button isn't clickable. See the difference:

<Image border={false} alt="DashboardButtonDoneVsIncompleteSetup" src="https://files.readme.io/9d03b26ed0a366aeb853129361808f49ab95cb85c0f37a2f670fae3c123698da-image.png" />

The dashboard opens in a new tab.

To access dashboards directly, from the **Dashboards** general page, navigate to **Managed by Axonius** > **Agent Coverage**.

## Exploring Dashboard Data

Each dashboard shows the following data and insights:

### Scope Diversity and Scale

The charts here show the distribution and count of in-scope and out-of-scope devices across different categories. In the following example, the **Servers Distribution** chart shows the total counts of in-scope and out-of-scope Windows Servers (Cloud). Hover over the chart to see the exact numbers.

<Image align="center" border={false} width="600px" alt="ServersDistributionChart" src="https://files.readme.io/f174fdb1fd3d5e1651b5fcc75f1800258434fd537bf9d6d1ae5040341e8790f4-image.png" />

<Image align="center" border={false} width="600px" alt="ServersDistributionChartHoverDetail" src="https://files.readme.io/69d5e62772f81c650b17e6c55ea225ee28c27ca3ace91ac94251d320139dc07f-image.png" />

<br />

### Coverage Status

The charts here show the distribution and count of devices based on their overall health status. For example - out of all Windows Cloud Workstations, how many devices are active, inactive, missing, or headless.

### Coverage Health Trends Over Time

The chart here helps you identify historical trends, spikes, or gradual degradation in coverage health. For example, you can specifically identify changes in the counts of inactive or missing agents over time.

### Add Custom Charts

See [Working with Charts](https://docs.axonius.com/axonius-help-docs/docs/working-with-dashboards) for more information on creating and managing custom charts.

**Reminder:** custom charts are *not* managed by Axonius, therefore, they are not automatically updated when you make changes to the settings on the Agent Coverage page.

<br />