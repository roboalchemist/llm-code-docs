# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt.md

# Create a list prompt

When you create a metadata list, you are defining a query to retrieve a list of display names and corresponding values from a metadata data source provided by your administrator.

**Note:** You must have a data table or chart which contains at least one parameter for your prompt control to function correctly.

![Filter dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-f4f22b798569a3f227c4328d6bdb4d11c4c46c77%2FPDD_PROMPTS_filter_props_metadata_ONYX.png?alt=media)

1. In the dashboard page, under **General Settings**, select **Prompts**.

   The Prompt Editor appears on the right. No prompts are listed if this is the first time you are assigning prompts.
2. To display a prompt toolbar to users of the dashboard, enable **Show Prompt Toolbar**.

   A placeholder for the prompt toolbar appears at the top of the dashboard.
3. Click the **Add** icon to add a prompt.

   The Prompts dialog box appears.
4. In the Prompts dialog box, enter a **Name** for your prompt.
5. Under **Data Type**, choose **Metadata List**.
6. Click **Select** to choose the data source which contains the content you need to set options from the drop-down list and click **OK**.

   The Query Editor opens.
7. In the Query Editor, build a query to choose either a single column (which represents both a name and a value), or two columns representing the display names and corresponding values.

   If a single column query is defined, the values of that column will be used for both the display names and the values.
8. Click **OK** to exit the Query Editor.

   Your options appear under **Selected Items** in the Prompts dialog box.
9. Under **Control Properties**, enter a default **Label** and **Value** for the initially selected option in your prompt control.
10. Select a **Label** to display in the prompt control.

    This is the user-friendly name which users will see in the dashboard.
11. Select the **Value**.

    This is the value in the database which is associated with the label you selected in the previous step.
12. If applicable, choose your **Display** type from the list.

    Some prompt controls allow you to choose the position of your prompt options. If you have a long list of options, such as a list of cities, options may not appear correctly in the user console unless you change the **Display** type to **Horizontal**.
13. Click **OK**.

The list of values appears in the prompts toolbar in the dashboard.
