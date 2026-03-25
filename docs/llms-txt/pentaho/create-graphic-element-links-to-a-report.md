# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-graphic-element-links-to-a-report.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-graphic-element-links-to-a-report.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-graphic-element-links-to-a-report.md

# Create graphic element links to a report

You can create content-to-content links between an Analyzer chart and any other parameterized report such as a Report Designer report, a data table, or another Analyzer report.

Below are general instructions for linking an Analyzer chart to a report. You must adjust the instructions when working with your own data.

1. Create a simple dashboard that contains an Analyzer chart and a parameterized report.

   The example here displays an Analyzer chart and an Analyzer report displayed as a table view. At this point, none of the content has been linked and you have a "static" dashboard.

   Hypothetically, if you want users to be able to click a bar in the bar chart and update the Analyzer table view, the table must contain at least one parameter. In the example below, there are two parameters, (LINE and TERRITORY), associated with the Analyzer table.

   ![Parameter created for LINE](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-215662b9606892c263767202dafd4e06dfed79bf%2FAnalyzer_param_on_line_ONYX.png?alt=media)
2. Under **General Settings**, choose the Analyzer chart, then click the **Content Linking** tab.
3. Click the check box (or check boxes) next to the field/column name you want enabled for content linking, and then click **Apply**.

   ![Chart content linking](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-8ce47ffc9e982fd133a4a1eb96c56518bef7bcc7%2FAnalyzer_chart_content_linking_sample_ONYX.png?alt=media)
4. Under **General Settings**, choose the Analyzer report (table view) and click the **Parameters** tab.
5. Click the down arrow in the **Source** text box to display another source for the parameters you created.

   In the example below, notice that **Sales by Line**, (this is the name of the dashboard panel that contains the chart), can now be selected as a source for both the **TERRITORY** and **LINE** parameters.

   ![Select source on Parameters tab](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-b2e6167c1291da2aa6a949594f3b9ab6b77408b3%2FAnalyzer_content_linking_selections_territory_ONYX.png?alt=media)
6. Save your dashboard.

   See [Saving Dashboards](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/save-a-dashboard) for steps.

In this example, content linking is applied when users double-click a bar in the bar chart. The data table updates and displays sales details for a product line in a specific territory.

![Content linking example](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e02769be3e7dba08bd38a869a4ae152eac7bb6e9%2FAnalyzer_chart_content_linking_final_ONYX.png?alt=media)
