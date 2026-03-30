# Source: https://docs.axonius.com/docs/advanced-asset-investigation.md

# Asset Investigation

Use **Asset Investigation** to view changes in the values of fields over a set period of time. The investigation data allows you to monitor the fields so you can identify abnormal behavior in a specific asset or in a set of assets on the system.

Asset Investigation runs every six hours. However, adapters that support differential fetches update asset data much more frequently, every 15 minutes. When these rapid fetches detect a change in asset values, those updates are immediately factored into the Asset Investigation's calculations.

You can either view Asset Investigation for a single asset from the [Asset Profile](/docs/asset-profile-page#/asset-investigation-tab) page or investigate all changes on all assets on the system from the **Asset Investigation** page.

The **Asset Investigation** page shows the changes over time for all assets in the system. When a security event in the organization happens, this often causes anomalies on more than one device. The **Asset Investigation** page enables you to see all changes on all assets on the system. You can use the **Asset Investigation** page to:

* Compare groupings of assets, more easily, from one central console.
* Accelerate incident response and alert triage.
* Track changes among assets.
* Identify unusual or risky patterns.

Asset Investigation is supported for all assets in the system except for Aggregated Security Findings, Vulnerability Repository, Software, and Activities.  From the relevant **Assets** page select **Asset Investigation**.

<Image alt="AssetInvestButton" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-FDHGV1QS.png" />

The  **Asset Investigation** page opens and shows all the assets on the system.
Use the filters to set a time period, adapter connections and fields to investigate.

<Image alt="AssetIvestMain" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-GBYAV57Q.png" />

## Events Table

The **Events** table shows changes in the values of pre-defined fields on all the assets displayed (or on the asset selected from the Asset Profile page).  Each row on the table represents a changed event on the asset and the time at which it happened.  The changes are displayed for each adapter source, and not on the aggregated value.  Events are displayed sorted by time with the newest events on the top.  The first time you open this page, the **Values Added** column is populated with the first value identified by Axonius, which is the value from which added/removed values will be calculated. These values are marked by an *i* icon.

The **Events** table shows the following information:

* **Date** – The date and the time stamp (in UTC) of the changed event.
* **Asset** - The name of the asset entity where a change happened. Click on the asset entity to open the [Asset Profile](/docs/device-profile-page-aggregated-tab) page to see more information about this asset.
* **Field Name** - The name of a field where a change happened.  Asset Investigation is defined for a pre-defined set of fields. You can see the fields available  for this asset type in the Field Name filter. An adapter icon shows on which adapter the field is.
* **Event Type** - The type of event.
  * Earliest Value Added  - The first value identified by Axonius, which is the value from which added/removed values will be calculated.
  * Value Added -  A value added to the field
  * Value Removed - A value removed from the field
  * Value  Changed - Both a value-added event and a value-removed event occurred as part of the same event
* **Values Added**  - Lists all the values added to the field. If more than 2 values were added, hover over to see all the values. The first 50 are displayed and can be scrolled through.
* **Values Removed** - lists all the values removed from the field. If more than 2 values were removed, hover over to see all the values.

### Asset Investigation Fields

Asset Investigation is supported for any common asset fields, adapter fields, custom fields, or tag fields. You can see the fields available for each asset type in the Field Name filter or on the [Asset Investigation Fields page](/docs/asset-investigation-fields). If a field is not compatible for Asset Investigation, an Indication icon (![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetInvestigations_Incompatable.png)) appears next to the field.

### Tags on Asset Investigation

You can use Asset Investigation to track changes made to tags on the system.  Support of tags  in Asset Investigation means that you can be updated when a tag is added or removed from an asset, whether this is done manually, or using an [Enforcement Action](/docs/add-remove-tag).  Using Tags on Asset Investigation you can track the state of an asset by the value of the tag.
From the **Field Names** drop down choose **Tags**. For each change to **Tags**, the system will show **Value Added** or **Values Removed**.

## Filtering

You can filter the values to be displayed in the table.  You can then use the filters to create System queries based on the filters and also save them as queries that can be used later on. [Read more about System Queries.](/docs/creating-queries-filters)

<Image alt="Filters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-LYHKQK32.png" />

**Search**  - Enter the value to search by. From the drop-down select which field to run the free search. You can choose 'Value Added', 'Value Removed', or 'Asset'. Select **Show Exact Results** to search for an exact value in a specific field.

<Image align="center" alt="ExactMatchSerach AI" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExactMatchSerach%20AI.png" />

* The following filters are available:

  * **Saved Query** - You can select an existing saved query  by which to filter the data so that the Asset Investigation will only run on entities that match the results of the saved query. Select a Saved query from the filter drop-down. The Asset Investigation data is displayed by the Saved query you selected. Note that events are displayed  only the for top 400k assets. When you save the Asset Investigation query, the Saved (asset) Query filter is saved as part of the Asset Investigation query.
  * **Adapter Connections** - Show assets from specific adapter connections. Click the arrow next to the adapter name to show the connections on the adapter.
  * **Field Names** - Show all assets containing a specific field.
  * **Event Type** - Filter by event type. You can choose to show values added, values removed, the earliest value added, or Value changed.   *Value changed* shows values when Values Added and Values Removed  were part of the same event.
  * **Time Range** - You can filter for specific assets by date with the date range picker or by a specified last number of days, weeks, months, or years, or for a time range prior to the number of days set.

  **To filter by date range:**

1. From the **Time Range** dropdown, select **In range**.
2. Select **Start date** and **End date** to indicate the date range to display results.
3. To filter results only for a specific date, select the same date twice.
4. If you want to include specific times in the date range, click **Select Time** in the date range picker.
5. Click **OK** to set the **Time Range** filter.

<Image align="center" border={false} src="https://files.readme.io/4a99c189562800f25a248d7a4365d148569aa631bb8188f466de83d7dde13d06-TimeRange.png" />

**To filter by the last number of hours, days, weeks, months, or years:**

1. From the **Time Range** dropdown, select **Last** and specify a value in the field next to **Last**.
2. By default, the value is the number of days. If you want to filter by hours/weeks/months/years, select the relevant option from the **days** dropdown.

<Image align="center" border={false} src="https://files.readme.io/463b27b594730e9231d2f7a9d1051023528b0d95da5b0f5612709b81d4bbaa59-TimeRangePeriod.png" />

<br />

**To filter by the number of days ago:**

You can set a Time Range to show only the events prior to the number of hours, days, weeks, months, or years set.

1. From the **Time Range** dropdown, select **Prior to**.
2. In the number field, enter a value or use the arrows to select the value you want.

* By default, the value is the number of days. If you want to filter by hours/weeks/months/years, select the relevant option from the **days** dropdown.

<Image align="center" border={false} src="https://files.readme.io/36c67deeb100cf2b603f534e257755c0a1625454ed6443ba9da09f8fdd815bab-TimeRangePriorto.png" />

* Click **Clear All** to clear all selections in a specific filter.

* Click **Reset**  to clear all filters and reset the display.

After you filter on an Asset, you can open the Asset on the relevant asset profile page and then track changes on  the  Asset Investigation  tab.

### Use Case Example

For instance, to check which assets were updated with a new agent version during the last week.

* Set a **Date Range** filter for the last 7 days.
* Set the **Field Name** filter to Agent Version.
* If you see changes of interest, click on the Asset link to open the Asset on the Devices page.
* For further investigation, click the [Asset Investigation](/docs/asset-investigation) tab on the Device Profile page.

### Saving Filters and Searches

You can save filters and searches you configure on the **Asset Investigation** page as Queries, Refer to [System Queries (Creating Queries Using Filters)](/docs/creating-queries-filters) for full details. Once you save a query, you can see it on the [Queries page](/docs/queries).
Use:

* **Save As** - to save the filters/search as a Query
* **Reset**  - to reset the display

## Notify on Asset Changes

Notify on Asset Changes provides users with notifications when a change occurs within an asset field, ensuring a proactive approach to asset management and security.
This is not available for the Asset Investigation tab on the Asset Profile page.
Once you save filters and searches you configure on this page as Queries, you can use them to create notifications using the Axonius Enforcement Center of changes to Assets.
The feature's integration with Axonius Enforcement Center Actions enables alerts through various channels, including System Notifications, SIEM, Email, and Slack. This ensures that you stay informed about critical changes, facilitating prompt and effective responses to potential security threats or abnormal changes in the IT space. Notifications can be tracked via the Findings screen or external systems.

On the Asset Investigation tab on the Asset Profile page, click **Comparison Report** to open the [Comparison Report](/docs/comparison-report-assets) dialog. The comparison report opens with the current device selected.

Choose **Export CSV** to export the table to a CSV file.