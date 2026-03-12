# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-a-report-from-report-designer.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-a-report-from-report-designer.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-a-report-from-report-designer.md

# Link a report from Report Designer

The instructions that follow show you how a link inside a Report Designer report (`.prpt`) can drive a parameter in content on another dashboard panel. You must adjust the instructions when working with your own data.

You must have a report (`.prpt`) that contains a hyperlink before you can complete this task. See **Pentaho Report Designer** for instructions about adding hyperlinks to a report.

1. Create a simple dashboard that contains a `.prpt` report and a data table.

   At this point, none of the content has been linked and you have a "static" dashboard. Notice the report (`.prpt`) in the example. You want dashboard consumers to click a territory (APAC, EMEA, etc.), hyperlink and update the data table with information about that specific territory.

   ![Report Designer content linking](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-082be73b5837eb88ff05e60efe9eedffcb137974%2FPDD_PRPT_content_linking_ONYX.png?alt=media)
2. Under **General Settings**, choose the report (`.prpt`) and click the **Content Linking** tab.
3. Click the checkbox next to the field you want used for content linking.
4. Add a parameterized condition to the query for the data table by specifying a parameter name in curly braces in the **Value** text box; then, provide a default value for that parameter in the **Default** text box.

   In the example, a parameter called **TERRITORY** with a default value of **NA** has been created.

   ![Filter parameter](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-73a40922ec305ddc13ded7a33a670c960264ee74%2FPDD_PRPT_filterparm_sample_ONYX.png?alt=media)

   Parameterizing a query, as described here, allows you to pass values dynamically and update the data table based on events triggered by other elements of the dashboard such as a user choosing an item from a filter control or following links defined in content associated with another panel in the dashboard.
5. Under **General Settings**, choose the data table and click the **Content Linking** tab.
6. Click the drop-down arrow, in the **Source** text box to display another source for the parameter you created.

   In the example, notice that **Product Line Share by Territory - Territory**, (this is the name of the dashboard panel that contains the `.prpt`), is now selected as a source for the **Territory** parameter.

   ![Select parameter](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-51c1d8a4e4d1b6ec906f6040cb74d99c8b6d5e06%2FPDD_PRPT_content_linking_select_parm_ONYX.png?alt=media)
7. Save your dashboard.

   See [Saving Dashboards](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/save-a-dashboard).

When content linking is achieved, the data table updates when a link in the report (`.prpt`) is clicked as shown in the example.

![Linked report](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e289f85da0262d64731bbe04f96a7bd4cfe5aaa9%2FPDD_PRPT_content_linking_final_result_ONYX.png?alt=media)
