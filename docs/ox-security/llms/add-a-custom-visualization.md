# Source: https://docs.ox.security/generate-reports/custom-reports/add-a-custom-visualization.md

# Add a Custom Chart

Create a chart that shows grouped counts from a data source. Use it for aggregated views such as Issues by Severity or Issues by Application.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d321cef3f72b1d66b58113bf0edf603647626543%2Fadd_widget_charts%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Screen areas

| Area             | Description                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Widget name      | Title for the chart tile. Edit before adding.                                                                                                      |
| Data source      | Dataset to visualize, for example Issues.                                                                                                          |
| Group by         | Primary field that buckets the counts, for example Severity, Application, Category.                                                                |
| Add sub-group by | Optional second split that creates series within each group.                                                                                       |
| Date range       | <p>Time window for the calculation.<br>Available for the following data sources:<br>- Pipeline Issues<br>- Resolved Issues<br>- Removed Issues</p> |
| Filters          | Values that limit data for this widget only. Common filters: Application, Severity, Category, App Tag. Select Additional filters to see more.      |
| Preview          | Live chart preview. The preview may show only the top results.                                                                                     |
| Chart type       | Picker for pie, column, area, or line.                                                                                                             |
| Add widget       | Adds the configured chart to the report.                                                                                                           |

**To create a custom visualization:**

1. In **Custom Reports**, select **ADD WIDGET > Custom Chart**.
2. In **Widget name**, enter a clear title.
3. In the **Data source**, select the dataset.
4. In the **Group by**, select the primary field.
5. To split each group into series, select **Add sub-group by** and choose a field.
6. If available for the selected source, configure the **Date range**.

   > **Note:**\
   > The global date range overrides the widget’s saved date range. When no global date range is selected, the widget uses its own configuration.
7. Open **Filters** and set any values you need for this widget.
8. In the chart picker, choose pie, column, area, or line.
9. Review the **Preview** to confirm the layout.
10. Select **ADD WIDGET**.
