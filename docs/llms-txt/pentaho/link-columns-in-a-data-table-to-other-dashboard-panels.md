# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-columns-in-a-data-table-to-other-dashboard-panels.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-columns-in-a-data-table-to-other-dashboard-panels.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-columns-in-a-data-table-to-other-dashboard-panels.md

# Link columns in a data table to other dashboard panels

The instructions below show you how to link a chart to a column in a data table. You must adjust the instructions when working with your own data.

1. Create a simple dashboard that contains a data table and a bar chart. At this point, none of the content has been linked and you have a "static" dashboard.

   Notice the data table in the example here. You want dashboard consumers to click a product in the **Product Line** column and have the bar chart update with information about sales by territory for that specific product line.

   ![Link on column](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-bce7cd6428eff3f29be80e0162ffe29282c45871%2FCL_content_link_on_column_ONYX.png?alt=media)
2. Add a parameterized condition to the query for the bar chart by specifying a parameter name in curly braces in the **Value** text box; then, provide a default value for that parameter in the **Default** text box.

   In the example here, a parameter called **Productline** with a default value of **Classic Cars** has been created.

   ![Parameter query](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ec50c622193d0027912266265fcce88d30a4cd2c%2FCL_content_linking_parm_query_ONYX.png?alt=media)
3. In the Chart Designer, set the data definitions for the series, category and values columns associated with your bar chart and click **OK**.
4. Under **General Settings**, choose the data table and click the **Content Linking** tab. Enable content linking on the column in your data table that will filter content in your chart.

   Each of the columns in a data table are able to broadcast values to other dashboard components.

   ![Value as link](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-b5f125f45e0378ea68be2e52dba24bfa2db73b79%2FCL_parm_value_for_linking_2_ONYX.png?alt=media)
5. Under **General Settings**, choose the chart and click the **Parameters** tab. Click the down arrow in the **Source** text box to display another source for the parameter you created.

   In the example below, notice that **Order Details - Product Line** , (this is the name of the dashboard panel that contains the data table), can now be selected as a source for the **Productline** parameter.

   ![Select a new source](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-5d5760e930cc45be05f2a0ffd3cc8d3302cf1b65%2FCL_parm_new_source_ONYX.png?alt=media)
6. Save your dashboard.
7. In the data table, choose an item in the column that has content linking enabled.

   The content in the chart updates in response to the item that was clicked in the data table.

In the example below, the **Product Line** column was enabled for content linking.

![Bar chart with links](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-bc13e4c0befc9e7903dee0b167b861c4dbe92e13%2FCL_completed_linked_bar_chart_ONYX.png?alt=media)
