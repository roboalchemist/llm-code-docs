# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-data-tables-in-a-dashboard/add-a-data-table-to-a-dashboard.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-data-tables-in-a-dashboard/add-a-data-table-to-a-dashboard.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-data-tables-in-a-dashboard/add-a-data-table-to-a-dashboard.md

# Add a data table to a dashboard

Perform the following steps to add a data table to your dashboard:

1. Select a panel in the Dashboard Designer.
2. Click the **Insert** icon and select **Data Table**.

   The Select a Data Source dialog box appears.
3. Select a data source from the list of available data sources and click **OK**.

   The Query Editor opens.
4. Begin building your query. Click the Plus Sign next to the category name to display its associated table columns. When the column names appear, click to choose the column that contains the data you want displayed in your data table.
5. Click the small yellow arrow to place the column name under **Selected Columns**.
6. Now add the **Conditions**.

   These are your constraints that filter what you are choosing. You can add multiple conditions:

   1. Under **Combine**, you can choose your constraint (**and**, **or**, **and not**, **or not**) from the drop-down list.
   2. Under **Comparisons** you can click the drop-down list to display options for comparisons, =, <, >, and so on; (for example, where the customer number is equal to 144 or 145).
   3. You can also choose an aggregation type from the drop-down list for table columns that contain numeric data. The table below contains a definition for each aggregate type:

      | Aggregate Type | Description                      |
      | -------------- | -------------------------------- |
      | SUM            | Sums a column's values           |
      | COUNT          | Counts a column's values         |
      | AVG            | Averages a column's values       |
      | MIN            | Selects the minimum column value |
      | MAX            | Selects the maximum column value |

      Click **Preview** at any time to view the data associated with your query.
7. Add the columns that you want to **Order By**.

   The ordering of the selected data is accomplished by one or more columns in a table. For example, you can sort the data by customer name and address.
8. Click **OK** in the Query Editor when you are done.

   The data table appears in the dashboard panel.
