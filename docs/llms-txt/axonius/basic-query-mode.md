# Source: https://docs.axonius.com/docs/basic-query-mode.md

# Working with Basic Query Mode

There are two modes you can use to create a query: the Wizard mode and Basic mode. Use the Wizard mode to create queries with the Query Wizard. Use Basic mode to create a simple query by selecting filters. The assets that match the selected filters are displayed in the list below.

The default mode for all asset pages is the Wizard mode where you can build a query either using the [Query Wizard](/docs/query-wizard-and-query-filter) or writing your query in the query bar. Once you select **Basic** on an asset page, it will remain in this mode, until you change it to Wizard for the Query Wizard. You can use Basic mode for one asset type, while using the Query Wizard for other types.

**To use Basic mode:**

1. In the query area of the asset page, click **Basic**. If a query is already in the Query Wizard, you may need to clear it to use Basic mode. The first time Basic mode is used, some default filters are pre-selected.
2. To select different filters, click **+ Filter** and select the filters you want. Selected filters are marked with a checkmark. Only aggregated fields can be used as filters. To remove a filter, select it again. In the **+Filter** list, under All fields, fields are sorted by the most frequently used first.
3. From each selected filter list, select the fields you want to filter by or enter the value appropriate for that field. You can select multiple fields from some lists and enter multiple values in some fields.. Selected fields are marked with a checkmark. To remove a field, select it again.

For example, **Amazon Web Services** adapter connections, **User Name** for user name, **Is Admin**, and **Last Seen** are selected as filters.
![QueryBasicModeExample.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryBasicModeExample.png)

* Click **Wizard**. The selected filters are also populated in the Query Wizard. However, there is no automatic conversion from **Wizard** mode to **Basic** mode.
  ![QueryWizardExample.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardExample.png)
* When in Wizard mode, click **Query Wizard** to see the query details in the Query Wizard.
  ![QueryWizardExampleFull.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardExampleFull.png)

Basic queries can be saved like regular [saved queries](/docs/saved-queries-devices). You can see the query details in the Saved Query drawer, including the selected fields.

<Callout icon="📘" theme="info">
  Note

  Administrators can define default query fields (filters) for each asset type based on user roles. These fields appear by default in Basic Query Mode on each Assets page. See [Defining Basic Query Mode Fields per Role](/docs/manage-roles#defining-basic-query-mode-fields-per-role) for more details.
</Callout>