# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/link-dashboard-prompts-to-analyzer-parameters.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/link-dashboard-prompts-to-analyzer-parameters.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/link-dashboard-prompts-to-analyzer-parameters.md

# Link dashboard prompts to Analyzer parameters

The instructions below explain how to parameterize an Analyzer report.

**Note:** This process only applies to dashboards which include parameterized Analyzer reports. You must have a query parameter in the Analyzer report to proceed.

1. In your Analyzer report, right-click a field you want to link to, then select **Filter**.

   The Filter dialog box opens. In the example below, data will be filtered by **Territory**.

   ![Analyzer filter](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-dd681d330da3b3567191627cf43f6ff4373ca00c%2FPDD_PROMPTS_Analyzer_filter_redo.png?alt=media)
2. Enter a name for the parameter in the **Parameter Name** text box and select its corresponding check box to enable it.
3. Select the values you want associated with the parameter. Use the arrow buttons to add and remove values.
4. When finished, click **OK** to save your selections and close the Filter dialog box. Be sure to save your report.
5. In the upper-left corner of the report, you can see that a filter is in use. Optionally, click the **Edit** (pencil) icon to make changes to your filter, or the **Delete** (X) icon to remove the filter.
6. Create a dashboard and drag the Analyzer report into a panel.

   The name of the parameter appears in the lower portion of the dashboard under **Parameters**. If a Between operator is parameterized, two parameters will be automatically created with the suffixes `_START` and `_END`.
7. Add a filter to the dashboard based on the parameter you created in your Analyzer report.

   The filter appears in the dashboard.
