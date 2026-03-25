# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight-data-databases-view.md

# Working with views in Snowsight

You can work with [views](views-introduction.md), [materialized views](views-materialized.md), and
[semantic views](views-semantic/overview.md) in SQL or in Snowsight.
For details about the available SQL commands for working with views, see [Table, view, and sequence commands](../sql-reference/commands-table.md).

In Snowsight, in the navigation menu, select Catalog » Database Explorer, and then search for or browse to the view.
Select the view to explore details about the view, the columns defined in the view, and preview the data in the view.

You must have the relevant privileges to access and manage the [view](security-access-control-privileges.md),
[materialized view](security-access-control-privileges.md), or [semantic view](security-access-control-privileges.md) in
Snowsight.

## Explore view details in Snowsight

After opening a view in Snowsight, you can do the following:

* Identify the type of view and when the view was last created. Hover over the time details to see the exact creation date and
  time.
* Review the SQL definition of the view on the View Details or Semantic View Details tab.
* Manage privileges for the view in the Privileges section of the View Details or Semantic View Details tab.
  To manage privileges, see [Manage object privileges with Snowsight](security-access-control-configure.md).
* For views and materialized views, review the name, type, ordinal (order of the column in the view), tags, and masking policies
  applied to the view on the Columns tab.

  To add tags and masking policies to a view, see [Use Snowsight to set tags](object-tagging/work.md).
* For semantic views, you can view details about the logical tables, relationships, facts, dimensions, and metrics by selecting
  the Semantic Information tab.

## Manage a view in Snowsight

You can perform the following basic management tasks for a view in Snowsight:

* To edit the view name or add a comment, select  » Edit.
* To drop the view, select  » Drop.
* To transfer ownership of the view to another role, select  » Transfer Ownership.
* To edit a semantic view, select the Semantic Information tab, and select Edit in Cortex Analyst.

## Preview data in a view

For views and materialized views, you can preview up to the first 100 rows of a view on the Data Preview tab for the view.

> **Note:**
>
> If your view is complex, you might not see a data preview. Snowsight queries the view for the data preview and waits
> for up to 300 seconds for results to be returned. If the query takes longer than 300 seconds to complete, Snowsight
> cancels the query and displays no preview data.

Select  to manipulate the preview data:

* Sort the data in ascending or descending order.
* Increase or decrease the decimal precision.
* Show thousands separators in numbers.
* Display the data in the column as percentages.

The options available to you depend on the type of data in the column.

> **Note:**
>
> The preview requires a warehouse. By default, Snowsight uses the default warehouse for your user profile, or you can
> select a different warehouse.
