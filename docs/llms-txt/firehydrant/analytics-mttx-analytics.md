# Source: https://docs.firehydrant.com/docs/analytics-mttx-analytics.md

# MTTx Analytics

MTTx is shorthand for **Mean Time To\_\_\_\_** , a set of metrics used to help determine the overall health of incident management processes. This Analytics page groups and visualizes these metrics so you can understand overall health by entities like teams, impacted services, and more.

## Groupings and Filters

FireHydrant's analytics offer the ability to filter and group by various aspects:

* **Grouped by** - Selecting different groupings will change the results shown in subsequent graphs and tables
  * Service
  * Environment
  * Functionality
  * Team
  * Severity
  * User
  * \[Custom Field]
* **Date Range** - You can tailor your results to specific time ranges. The range selector allows a visual selection of date range as well as selecting pre-configured ranges and typing them in
* **Incident Name** - You can also search and filter analytics according to incident names
* **\[Other Filters]** - Any filters available on your [Incidents](https://app.firehydrant.io/incidents) page are also available here for paring down datasets

## Baseline Metrics

<Image alt="Example baseline metrics" align="center" width="650px" src="https://files.readme.io/d6a7a7de608aa4e06ffb9aa0013fa6e440f8a4ff8e26a748be5be06d640336ba-CleanShot_2025-01-06_at_14.46.25.png">
  Example baseline metrics
</Image>

FireHydrant offers the following MTTx metrics out-of-box:

* **<Glossary>MTTA</Glossary>** - Mean Time To Acknowledgement
* **<Glossary>MTTD</Glossary>** - Mean Time To Detection
* **<Glossary>MTTM</Glossary>** - Mean Time To Mitigation
* **<Glossary>MTTR</Glossary>** - Mean Time To Resolution

However, you can customize your MTTx metrics by defining custom measures. For more information, visit [Custom Milestones](https://docs.firehydrant.com/docs/custom-milestones).

This panel also shows the number of resolved incidents for the selected timeframe and filters. You can click on **View Incidents** in the leftmost box to view the full list of incidents for the selected filter on the Incidents page.

## Top Impacted

<Image alt="Top impacted by grouping" align="center" width="650px" src="https://files.readme.io/40bc061f7105c64e88d25ddb91a25802caa1ed5a3a0355d3f82d2937090a2f76-CleanShot_2025-01-06_at_17.11.01.png">
  Top impacted by grouping
</Image>

Depending on what Grouping you've selected above, these graphs will show a breakdown of incident count by value along with MTTx values. The chart on the left shows **Top impacted\[component] by incident count** while the right side shows the same components' MTTx values.

Each bar or bar cluster can be clicked on to filter to that specific data set on the Incidents page.

## Milestone Metrics

<Image alt="Milestone metrics graphs" align="center" width="650px" src="https://files.readme.io/922bb2410b54db5ac4e1c1537aef07046dcefa8488186fcd2238cfd9e0875886-CleanShot_2025-01-07_at_15.44.15.png">
  Milestone metrics graphs
</Image>

These graphs will show milestone metrics for all of the incidents that match selecting filtering and groupings above.

The left chart shows a **Time period vs. Number of incidents** chart with different lines showing each milestone and the number of incidents that reached that milestone within each time period.

The right chart is a graph of Tasks and Followups created within each time periods according to the selected groupings and filters.

You can hover over each axis point of data to see in-depth information.

<Image alt="Hovering over a specific data point" align="center" width="400px" src="https://files.readme.io/0e59bb0bdd930c50a17b782fe7d55f65d659404b77415b0c5ec11a9642922fea-Untitled-2024-04-19-1118.png">
  Hovering over a specific data point
</Image>

## Groupings Table

<Image alt="Table of components with various metrics" align="center" width="650px" src="https://files.readme.io/30bee899d531c311cad0053d6dca60282d96433c977fbccbda20696f4e88c43d-CleanShot_2025-01-07_at_15.48.35.png">
  Table of components with various metrics
</Image>

The table displays each component within the selected grouping along with incident count, healthiness measure, and any configured MTTx metrics you have for each row.

Within each table row, you'll also see bars that indicate that service's times for each metric in comparison to averages across all of the shown incidents for a selected filter and time range. You can use this to do compare things, for example, "How quickly issues (MTTD) are detected in Service A vs. other services" or "How fast does Team 1 acknowledge an incident (MTTA) in comparison to other teams," etc.

<Image alt="For example, `app-ios` service has much slower than average MTTx times, while `int-zendesk` has much faster than average" align="center" width="650px" src="https://files.readme.io/a5878e273c96c2a9a9ba4c7348b156d62f7346cea4fe579022a9ff6480666306-CleanShot_2025-01-07_at_15.51.17.png">
  For example, `app-ios` service has much slower than average MTTx times, while `int-zendesk` has much faster than average
</Image>

For each row, you can also click on **View Details** to expand a side drawer showcasing that component's specific MTTx metrics and incident count/MTTx over time graphs.

<Image alt="Expanding the side drawer on each individual component in the table" align="center" width="400px" src="https://files.readme.io/7ed91ccdcea02ae1753637553ea82453f4d9c226332d9f2d3daa98330c25df64-CleanShot_2025-01-07_at_16.03.13.png">
  Expanding the side drawer on each individual component in the table
</Image>

## Next Steps

* [Custom Milestones and Metrics](https://docs.firehydrant.com/docs/custom-milestones) - For understanding and customizing your milestones and MTTx metrics
* [Intro to Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) - Setting up and customizing your service catalog and components
* [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) - Configuring custom fields for your incidents