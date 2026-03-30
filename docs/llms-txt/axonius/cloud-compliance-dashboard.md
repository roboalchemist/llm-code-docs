# Source: https://docs.axonius.com/docs/cloud-compliance-dashboard.md

# Cloud Compliance Dashboard

The  Cloud Compliance Dashboard is available  to users who have purchased the [Cloud Asset Compliance](/docs/cloud-asset-compliance-overview) add-on. It displays information about Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure and Oracle Cloud, depending on the cloud adapters that you have connected.
To ensure that the Cloud Compliance Dashboard fetches the compliance data, verify that:

* At least one of the AWS, GCP, Microsoft Azure or Oracle Cloud adapters is connected.
* You ran the Discovery Cycle. For more information, see [Discovery Cycle](/docs/discovery-cycle).

## Cloud Compliance Charts

The following charts are displayed for each cloud provider:

* **CIS Benchmark Score** - is calculated as the percentage of passed rules out of all selected rules. The score is calculated and aggregated on all accounts currently filtered. Other filters do not affect the benchmark score.

* **CIS Benchmark Score over Time** - shows the change over time. By default, the last 30 days are displayed. You can perform the following actions:
  * View a different date range. To show results of a different date range, refer to the **Change date range in charts** option in [Actions](/docs/cloud-compliance-dashboard#actions).
  * Review detailed compliance information by clicking a date point to open the Cloud Compliance page on that date.

* **CIS Benchmark Results** - a pie chart showing the results. You can perform the following actions:
  * Mouse over a segment of the pie chart to view the number of rules that passed, failed, have errors, or are excluded.
  * Show benchmark results of a particular date by clicking ![filter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/filter.png), selecting a date in the datepicker, and clicking **Show Results**.
  * Click a segment of the pie chart to drill down and open the filtered results in the Cloud Asset Compliance Center. For more information, see [Viewing Benchmark Results](/docs/cloud-asset-compliance-page).

* **Top failed controls by affected users** - displays failed control by affected users. By default, results are displayed from highest to lowest number of failed controls. Click the horizontal bar of a specific failed control to view the list of affected users.

* **Top failed controls by affected devices** - displays failed control by affected devices. By default, results are from highest to lowest number of failed controls. Click the horizontal bar of a specific failed control to view the list of affected devices.

<Image alt="CloudDashboard3" width="650px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudDashboard3.png" />

<Callout icon="📘" theme="info">
  Note

  * You cannot delete, move or copy the Cloud Compliance dashboard.

  * You can export a report of the entire dashboard in PDF format. For more information, see [Reports Page](/docs/reports-page).
</Callout>

## Working with Cloud Compliance Dashboard

By default, the Cloud Compliance dashboard is displayed for all users who can access the Cloud Compliance view and Dashboard view, regardless of permissions. If you are an Admin or user with the 'Add and edit dashboards' permission, you can configure the system to not display this dashboard. For more information, see [Working with Dashboards](/docs/working-with-dashboard-spaces).

Depending on the chart and your permissions, you can perform the following actions:

| Option                           | Description                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Change chart title / description | 1. From ![kebab](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/kebab.png)   dropdown, select **Edit**. The Chart Wizard is displayed.  2. Navigate to **Chart title** or **Description** to modify the text.                                                                                                     |
| Change date range in charts      | 1. From ![kebab](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/kebab.png)   dropdown, select **Edit**. The Chart Wizard is displayed.  2. Select either **Show results in the last *X*** or **Show results in date range**, and select the desired duration or date range.                                       |
| Export to CSV                    | From ![kebab](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/kebab.png)   dropdown, select **Export to CSV**. A chart in CSV format is downloaded. **Note:** This option is available for the **CIS Benchmark Score Over Time** and **Top failed controls by affected users/devices** charts.                     |
| Filter results                   | Show benchmark results of a particular date by clicking ![filter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/filter.png), selecting a date in the datepicker, and clicking **Show Results**.                                                                                                                  |
| View last updated                | Mouse over  ![clock](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/clock.png) to view the time last updated. The displayed time represents when the fetching stage is completed and the data from all rules is calculated. The displayed score remains until the next fetch cycle and calculation are completed. |
| Sort by Name or Value            | 1. From ![kebab](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/kebab.png)   dropdown, select **Sort**.  2. Select either **Sort by Name** or **Sort by Value**.  3. Select either **Descending** or **Ascending**.                                                                                               |

For more information, see [Chart Actions](/docs/chart-actions).