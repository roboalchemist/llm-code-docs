# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-toolbar-prompt/customize-toolbar-prompts.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-toolbar-prompt/customize-toolbar-prompts.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-toolbar-prompt/customize-toolbar-prompts.md

# Customize toolbar prompts

Perform the following steps to customize your toolbar prompts:

1. In the **Data** box, click **Add**.

   The List Value dialog box appears.
2. In the **Label** field, enter the option name as you want it to appear to dashboard users.
3. In the **Value** field, enter the parameter source name.

   If using the Steel Wheels sample, enter `Classic Cars`.
4. Add labels and values for each parameter you want to filter. Click **Close** to exit the List Value dialog box.

   If you are filtering an Analyzer report and using a static list, you can add the option **All**. This option drops the filter from the report and shows all values.
5. In the Control Properties box, under **Initially Selected**, choose which item you want to appear first in the prompt list.

   Choose **Use First Value** to set the default to the first value in the list, or you can choose **Specify** if you want a specific value to appear first.
6. Click **OK**.
7. In the **Objects** pane, choose the title of the report you want to filter. Click the **Parameters** tab and choose the correct **Source** for the parameter from the list.

   The source should be the name of your prompt.
8. Click **Save**.
