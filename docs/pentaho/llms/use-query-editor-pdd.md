# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/create-a-chart/use-query-editor-pdd.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-query-editor-pdd.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-query-editor-pdd.md

# Use Query Editor

Learn how to use the Query Editor to retrieve dynamic data from a data source so that you can include the data in a new dashboard chart.

Complete the following steps to select a source and define data from that source to use in the Orders by Country {parm} chart. The Orders by Country {parm} chart is shown in the sample dashboard containing sales performance data for the example company, Steel Wheels.

1. Navigate to the User Console Home page.
2. Click **Browse Files**.
3. In the Folders pane, click to expand the **Public** folder, and then click the **Steel Wheels** folder.

   The content of the **Steel Wheels** folder opens in the Files pane.
4. In the Files pane, select **Sales Performance (dashboard)**.
5. In the File Actions pane, click **Edit**.

   The **Editing: Sales Performance (dashboard)** tab opens.
6. In the **Editing: Sales Performance (dashboard)** tab, navigate to the Orders by Country {parm} pane.
7. Click the **Insert Content** icon, and then click **Chart**.

   The following image shows the **Insert Content** icon and the **Chart** option.

   ![Location of the Insert Icon and Chart list option in the Query Editor.](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-6918cdecee6acab96017ca5ace32dcdf3cbe18de%2FPUC_query_editor_insert_icon.png?alt=media)

   | Item | Name           |
   | ---- | -------------- |
   | 1    | Insert Content |
   | 2    | Chart          |

   A warning opens for discarding current content.
8. Click **OK**.

   The Select a Data Source window opens.
9. Select **Orders** and click **OK**.

   The Query Editor window opens.
10. In the Categories / Columns pane, click to expand the **Customer** list.
11. Select **Territory**, and then click the top right arrow to add the Territory column to the top right table.

    The following image shows the **Territory** option that you select in the Categories / Columns pane, the top right arrow that you click to add the Territory column to the top right table, and the top right table where you add the Territory column.

    ![Location of the Territory option, top right arrow, and Territory column in the Query Editor.](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-4dd23233b6cb2651914c88e261fc12f3de5bd1f7%2FPUC_chart_designer_insert_territory_category.png?alt=media)
12. In the Categories / Columns pane, click to expand the **Orders** list.
13. Select **Total**, and then click the middle right arrow to add the Total column to the middle right table.
14. Click **Preview** to preview the table with data from the source that you selected in the columns that you added.

    The following image shows the Preview window that contains a table with order data in the Territory and Total (SUM) columns.

    ![Preview window in the Query Editor.](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-88f904342509964922f299217e14394b7f7ae6dc%2FPUC_query_editor_preview.png?alt=media)
15. Click **Close** to close the Preview window.
16. Click **OK**.

    The Chart Designer window opens.

Learn how to create a chart in the tutorial, [Use Chart Designer](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-chart-designer-pdd).
