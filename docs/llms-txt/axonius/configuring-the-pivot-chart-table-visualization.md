# Source: https://docs.axonius.com/docs/configuring-the-pivot-chart-table-visualization.md

# Configuring the Pivot Chart Table Visualization

The Pivot chart Table visualization can display data of simple configurations as well as complex data configurations.

The table has the following capabilities:

* **Expand/collapse rows** - All rows with sub-rows can be expanded.

  <Image align="center" alt="TableChartExpandRows.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/TableChartExpandRows.png" />
* **Column and row sorting** - *(available in the chart wizard)* Click on a column header to sort the rows according to the values in that column. In the chart preview, hover over a column to see the sorting arrows and then click to sort by **ascending/descending**. Sorting in another column sorts all rows according to the values in that column.

  <Image align="center" alt="PivotTableSortPreview" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/PivotTableSortPreview.png" />
* **Adjust column width** - Column width can be adjusted.
* **Configure unlimited dimensions** - You can configure as many dimensions as you need.
* **Infinite scroll** - When a table displays large amounts of data it will scroll indefinitely.
* **CSV export** - Table data can be [exported to CSV](https://docs.axonius.com/axonius-help-docs/docs/exporting-chart-data-to-csv).
* **Resize the chart preview** -   The chart preview can be resized so you can see more detail.

  <Image align="center" alt="ChartConfigWindowResize.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/ChartConfigWindowResize.png" />
* **Click-through on each cell** - Click on a table cell to open a drawer listing all assets represented in that table cell. In the drawer, click **Asset Page** to open the Asset page listing the same assets for further investigation. The drawer can be expanded as well.

  <Image align="center" alt="TableChartCellDrawer.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/TableChartCellDrawer.png" />

<Callout icon="📘" theme="info">
  Note

  When a table has more than 1 million segement calculations, performance may be slower than expected.
</Callout>

**To configure a Pivot chart with the Table presentation:**

1. On any editable dashboard, click **Add Chart** or edit an existing chart.

2. In the **Name** field, enter a descriptive name for the chart.

3. From the **Widget** list, select **Pivot Chart**.

4. Under **Visualization**, select **Table**.

5. Under **Data**, select an asset module and the query that will define which assets to include.

6. Under **Dimensions Row**, select the field whose values will be on the rows of the chart. You can select multiple dimensions.

7. Under **Dimensions Column**, select the fields whose values will constitute the columns.

8. Under **Metrics**, select the fields whose value is measured per the axis and the function. Multiple metrics can be configured.

9. Under **Calculation**, you can configure these options:

   * [**Use historical data**](https://docs.axonius.com/axonius-help-docs/docs/historical-query-results)

   * [**Include entities with no value**](https://docs.axonius.com/axonius-help-docs/docs/including-entities-with-no-value)
     * **Display Name** - When **Included entities with no value** is selected, you can set a custom value to display in that table cell.

   * **Include rows and columns with only zero values** -

10. Under **Presentation**, you can configure these options:

    * [**Set threshold colors**](https://docs.axonius.com/axonius-help-docs/docs/asset-cnt-thshld-color)
    * **Show Grand total for rows** - At the end of each row, the grand total of all counts are accumulated and displayed.
    * **Show Grand total for columns** -  At the end of each column, the grand total of all counts are accumulated and displayed.
    * **Show title** - The chart title in the **Name** field is displayed on the chart.

11. Click **Save**.

## Example of a Table Chart showing Complex Data

For example, you would like to know the number of instances of each specific software application for each CVE Severity Level.

**To configure a table chart with complex data:**

1. On any editable dashboard, click **Add Chart** or edit an existing chart.
2. In the **Name** field, enter a descriptive name for the chart.
3. From the **Widget** list, select **Pivot Chart**.
4. Under **Visualization**, select **Table**.
5. Under **Data**, select the Devices module and the query that will define which assets to include.
6. Under **Dimensions Row**, select the fields whose values will be on the axis of the chart. These are the rows. There will be 2 columns to label the rows. One for each CVE Severity and one for each Software Name.
   1. `Vulnerable Software: CVE Severity`
   2. `Vulnerable Software: Software Name`
7. Under **Dimensions Column**, select how to separate the values in columns. This will create columns for each OS type with the number of instances of the software with each CVE Severity.
   1. `OS: Type`
8. Under **Metrics**, select the Measures fields whose values are measured per the axis. This is what will be counted. Under each OS Type will be two columns: one showing the total number of that software, and one showing those that have reached EOS.
   1. `Assets` with a function of `Count`
   2. `Preferred OS: Is End of Support` with a function of `Count True`
9. Set **Calculation** preferences.
10. Set **Presentation** preferences.
11. Click **Save**.

<br />