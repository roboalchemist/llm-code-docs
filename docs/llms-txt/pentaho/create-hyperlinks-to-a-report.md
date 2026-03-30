# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-hyperlinks-to-a-report.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-hyperlinks-to-a-report.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-an-analyzer-report/create-hyperlinks-to-a-report.md

# Create hyperlinks to a report

Below are general instructions for creating content links in an Analyzer report, (inside a dashboard), that can be used to drive the [parameter values](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/getting-started-with-query-parameters-pdd) of content in other dashboard panels. You must adjust the instructions when working with your own data.

1. Create a simple dashboard that contains an Analyzer report and a data table.

   At this point, none of the content has been linked and you have a "static" dashboard.

   In the example here, when content linking is achieved, the list of territories (APAC, EMEA, Japan, and NA) will become hyperlinks that, when clicked, will update customer details data table. To get the correct filter display, a [parameterized query](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/add-query-parameters-to-analyzer-reports-task-article) that drives the content in the data table must be created.

   ![Content linking for a table](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-425d1fc68889ca28545eac7d289d997926e57d1f%2FAnalyzer_table_content_linking_ONYX.png?alt=media)
2. Add a parameterized condition to the query for the data table by specifying a parameter name in curly braces in the **Value** text box; then, provide a default value for that parameter in the **Default** text box.

   In the example here, a parameter called **TERRITORY** with a default value of **NA** has been created. Parameterizing a query, as described here, allows you to pass values dynamically and update the chart based on events triggered by other elements of the dashboard such as a user choosing an item from a filter control or following links defined in content associated with another panel in the dashboard.

   ![Query on territory](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-834172e68fc30d8f0ffcd9812f9ab7b5021d8e6d%2FAnalyzer_parameter_query_on_territory_ONYX.png?alt=media)
3. Under **General Settings**, choose the Analyzer report. Click the **Content Linking** tab then click the check box next to the field/column name you want enabled for content linking. Click **Apply**.

   In the Analyzer report, the values under the **Territory** become hyperlinks.

   ![Hyperlinks in Analyzer table](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-d7218eae10629955fb83a737cb08de2380fa58bf%2FAnalyzer_analyzer_hyperlinks_ONYX.png?alt=media)
4. Under **General Settings**, choose the data table and examine its available parameters. Click the drop-down arrow in the **Source** text box to display and choose a new source value for the available parameter, then click **Apply**.
5. Save your dashboard.

In the example below, content linking was applied. When users click a territory hyperlink in the Analyzer report, the data table updates and displays customer-related details associated with that specific territory exclusively.

![Content link in Analyzer table](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-37171d3f31f3ef75297b6caf8e9029b420c2f4c1%2FAnalyzer_table_content_linking_complete_ONYX.png?alt=media)
