# Source: https://docs.axonius.com/docs/asset-table-chart.md

# Asset Data Chart

The **Asset Data** chart allows you to visualize asset field values with each asset displayed as a row in a table or an individual asset card. You can view data for all assets of a particular type, or you can filter the data using a new or saved query.

![AssetDataOptions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetDataOptions.png)

## Visualization Options

You can select to display the asset data in Table or Card view.

### Table View

The Table view generates a table to display the data according to the query and fields you select. If you select a saved query, the table's columns will be the same as those used in the query.

<Callout icon="📘" theme="info">
  Note

  When you select adapter data in Asset Data tables, the tables only present them in aggregated rows. The table cannot be expanded to individual rows per adapter entity.
</Callout>

### Card View

In the Card view, each asset is presented as a separate card. You can choose as many fields as you want. The cards change size to accommodate the number of fields or allow for scrolling within each card.
![AssetDataCards](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetDataCards.png)

If the cards you create contain only one field, the cards display the field values without the label, so make sure the chart's title clearly describes the data represented by the field values. If the field includes just a single value, the text is displayed in a larger size to emphasize it in your dashboard. This is especially relevant for dashboards that analyze a single asset.
![AssetData\_SingleAsset](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetData_SingleAsset.png)

## Refine Data

You can refine the data displayed in the chart for both Table and Card views, with refinements applied separately for each field, just as you can [refine data on Asset pages](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows). When you refine data, the query's asset count remains the same, even though Assets containing certain values do not appear on the chart.

When you click from the Dashboard to the relevant asset page, the configured refinement is applied to the asset page. However, when you refine data in a saved query and use it as the base query in the chart configuration, the chart does not automatically apply that refinement to its displayed data.

![AssetData\_Refinement.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetData_Refinement.png)

## Create or Edit the Asset Data Chart

You can create or edit the Asset Data chart in the Chart wizard.

To configure an **Asset Data** chart:

1. In the **Chart title** text box, enter a title for the chart.
2. *(Optional)* In the **Description** text box, you can add a description.
3. From the **Widget** list, select **Asset Data**.
4. In the **Visualization** area, select **Table** or **Cards**.
5. Under **Select Query**, select an asset type module and a query from the **Query** list.
   When an asset module is selected, but no query is selected, values are displayed for all assets of the selected module.
   The fields section shows the default fields for the chart, based on the selected asset or the saved query.
6. *(Optional)* To add a filter to the query, click the Filter icon ![Filtericon(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Filtericon\(1\).png) and configure the filter(s) you want.
7. *(Optional)* To change a field displayed in the chart, in the **Fields** section, select aggregated data or an adapter, and the field you want to appear.
8. *(Optional)* To add fields to this chart, click the Add button ![AddFields\_Button](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddFields_Button.png) and select the fields you want to display.
9. *(Optional)* To refine the values displayed for a field, click the Filter icon ![Filtericon(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Filtericon\(1\).png) corresponding to that field and configure the refinement in the dialog that appears.
10. *(Optional)* To set the sorting by a specific field click the Sorting icon ![FieldSort](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldSort.png) next to that field. Click it again to change if the assets are sorted in ascending or descending order for that field's values.

<Callout icon="📘" theme="info">
  Note

  The table sorting cannot be changed from the Dashboard.
</Callout>

![AddSortFields](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddSortFields.png)

12. (*Optional)* To reset the field list to the default for the selected query, click **Reset to Query**.

13. (*Optional)* To reset the field list to the default for the selected asset, click **Reset to Asset**.

14. *(Optional)* Set the chart to display results from a relative or fixed historical date. See [Viewing Query Results from a Historical Date](/docs/historical-query-results).

15. *(Optional)* To split rows with multiple values for complex tables so each value is displayed in its own row, enable the **Split by complex table** option and select the table you want to split. Any time that complex table contains multiple values, a separate row is created for that value.
    ![AssetData\_SplitBy.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetData_SplitBy.png)

16. Click **Save** to save the configuration and add the chart to the dashboard.

<Callout icon="📘" theme="info">
  Note

  The chart displays up to 20 assets instead of all assets. If users want to explore more assets, they can drill down from the chart to the specific asset page.
</Callout>

![AssetTableChart-Sample.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetTableChart-Sample.png)

The Table visualization is based on the assets tables, meaning any asset table functionality will apply.

Click on the asset link at the bottom of the page to view the Asset summary for the displayed assets. Click the **Asset Page** to view the assets at their relevant Asset page.