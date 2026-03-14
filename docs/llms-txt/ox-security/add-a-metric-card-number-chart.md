# Source: https://docs.ox.security/generate-reports/custom-reports/add-a-metric-card-number-chart.md

# Add a Metric Card (Number Chart)

Use a **Metric Card** (called **Number Chart** in the UI) to display a single aggregated value, such as the number of issues, applications, or resolved items in a defined time range. Metric Cards are useful for highlighting KPIs and high-level counters in a custom report.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2c11e0ba95f6f35a452936fe79dfe373f5232b0f%2Fadd_widget_metric%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Area        | Description                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Widget name | The name of the widget appears as the title on the report tile.                                                                                    |
| Data source | Dataset used to calculate the value, such as Issues, SBOM, Applications, Pipeline Issues, Resolved Issues, or Removed Issues.                      |
| Date range  | <p>Time window for the calculation.<br>Available for the following data sources:<br>- Pipeline Issues<br>- Resolved Issues<br>- Removed Issues</p> |
| Filters     | Widget-level filters that limit which items are counted. These filters apply only to this widget and are saved with it.                            |
| Preview     | Live preview of the calculated value based on the current configuration.                                                                           |

**To add a Metric Card:**

1. In **Custom Reports**, select **ADD WIDGET > Number Chart**.
2. In **Widget name**, enter a clear title that reflects both the metric and the time window, for example, *Resolved issues – last 90 days*.
3. In the **Data source**, select the dataset to count.
4. If available for the selected source, configure the **Date range**.

> **Note:**\
> The global date range overrides the widget’s saved date range. When no global date range is selected, the widget uses its own configuration.

1. Open **Filters** and apply any widget-level filters needed to narrow the count.
2. Review the **Preview** to confirm the value.
3. Select **SAVE WIDGET**.
