# Source: https://docs.axonius.com/docs/adapter-connections.md

# Adapter Connections

From the **Adapters** page, click **Adapter Connections** to open the **Connections** page. Right click **Adapter Connections** to open it in a new tab. You can also open this page from any single adapter.
Use the adapter **Connections** page to see a centralized summary of  information about all adapters and their connections. You can see the discovery schedule of each adapter and any adapter connections that have custom discovery schedules as well as some of the advanced settings configured.  In addition, you can see the polling schedule for each adapter.
From the **Connections** page you can add connections, and you can also perform actions on a single connection or in bulk on a number of selected connections.

<Image alt="Adapter Connections Page  " border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ConnectionsPageUP.png" />

The following information is displayed:

1. **Adapter Name**  - The name of the adapter.
2. **Gateway** - The name of the gateway through which the connection is made.
3. **Data Scope** - If the adapter connection is restricted by a data scope, the name of the data scope.
4. **Connection Label** - The connection label (if configured).
5. **Custom Adapter Value** - A custom value added to the adapter (if configured).
6. **Date Created** - The time and date the connection was created.
7. **Created by** - The user who created the connection.
8. **Last Modified** - The time and date the connection was last modified.
9. **Connection ID** - The connection ID.
10. **Compute Node** - The specific compute node the adapter and connection were initiated from.
11. **Connection Status** – The status of the connection: 'Active and connected', 'Active with errors',   'Inactive', 'Active for enrichment' or 'Partially connected'
    * 'Partially connected'  means that the adapter is partially connected, it has begun to fetch data, but is not fetching all the assets that it can. Click on the adapter connection to see an explanation (available for specific adapters).
    * 'Active for enrichment' Signifies when a CSV or SQL adapter is being used for Custom Enrichment. Even if the adapter is not connected, the connected can still be used for uploading a CSV file used for custom enrichment. When you clear the “Active connection” toggle, the system confirms that the adapter will still be used for enrichment
12. **Last Fetch Status** - Displays the status of the last fetch as displayed on the  **Adapter Fetch History** page:
    * Connection failed
    * Fetch ended successfully
    * Fetch ended with errors
    * Fetch failed
    * Fetch skipped
    * Fetch started
    * Fetch terminated
13. **Last Successful Fetch** - Shows the time and date of the last fetch that was successful for this connection.
14. **Discovery  Schedule (UTC)** – This shows the discovery schedule.  While some adapters are set to the default discovery, others may have custom discovery settings that were set using the **Advanced Configuration** tab for the connection. If adapters are set for real time discovery, this is also displayed.
15. **Advanced Configuration** - Shows if advanced discovery for each adapter connection is set separately, or the same configuration is used for all connections. Settings may be, 'Adapter Level', 'None' or 'Connection Level'.
16. **Connection Configuration** - Displays the configuration of each adapter connection in  JSON format.

<Callout icon="📘" theme="info">
  Note

  Sensitive data, such as passwords and private keys, aren’t displayed in the JSON.
</Callout>

14. **Adapter Configuration Advanced Settings**
    The following fields display values set in the **Adapter Configuration Advanced Settings** for the adapter. Refer to [Adapter Advanced Settings](/docs/advanced-settings) for detailed information about each setting.
    1. **Ignore Not Seen Devices (hours)** – Displays the number of hours set in the 'Ignore devices that have not been seen by the source in the last X hours' field in the  **Advanced Settings** for this adapter or connection (if custom settings set).
    2. **Ignore Not Seen Users (hours)** – Displays the number of hours set in the 'Ignore users that have not been seen by the source in the last X hours' field in the  **Advanced Settings** for this adapter  or connection (if custom settings set).
    3. **Hold before Fetching (hours)** – Displays the number of hours set in the 'Override the global discovery schedule for this adapter to wait X hours before fetching' field in the  **Advanced Settings** for this adapter.
    4. **Wait for Response (seconds)** – Displays the number of hours set in the 'Wait for a response from the source for up to X seconds'  in the  **Advanced Settings** for this adapter.
    5. **Ignore Matching Assets** – Displays whether the 'Ignore matching assets from the source if a subsequent asset was seen by the source before the previously fetched asset' in the **Advanced Settings** for this adapter is set or not.
    6. **Delete not Seen Devices (hours)** –  Displays the number of hours set in the 'Delete devices that have not been returned from the source in the last X hours'  in the  **Advanced Settings** for this adapter or connection (if custom settings set).
    7. **Delete not Seen Users (hours)** –  Displays the number of hours set in the 'Delete users that have not been returned from the source in the last X hours'  in the  **Advanced Settings** for this adapter or connection (if custom settings set).
    8. **Wait for Connection (seconds)** – Displays timeout for how long to wait for the connection to the source in seconds.
    9. **Failed Connection Attempts before Inactive** – Displays the number of failed attempts to connect before setting the adapter or connection (if custom settings set) to inactive. This number includes all connections to the server, including  periodic connection updates  (if set in [Data Aggregation Settings](/docs/configuring-data-aggregation-settings)).
    10. **Failed Connection Attempts before Fetch Failure** - Displays the number of failed attempts to connect before fetch failure.
    11. **Terminate after X hours of an active fetch** - Displays the number of hours set in the 'Terminate after X hours of an active fetch' field in the **Advanced Settings** for this adapter.
15. **Notes** - Any notes added on the **Adapter Connection Configuration** page.

### Setting Page Columns  Display

Use **[Edit Columns](/docs/setting-page-columns-display#changing-columns-displayed)** to set the columns displayed on the page and save them as a **[Saved View](/docs/setting-page-columns-display#saved-views)** and thus see fields most relevant to you.
Drag and drop columns on the table to arrange them in the order you want.

## Filtering the Display

You can filter the display by the following fields:

<Image alt="Adapter Connection filters.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Connection%20filters.png" />

* **Adapter name**  - The name of the adapter. Once you filter by adapter name, the Connection label, Connection ID and Compute node displayed are those relevant for that adapter.

* **Gateway** - The name of the gateway through which the connection is made.

* **Compute Node**  - The name of the compute node.

* **Connection Status** – The status of the connection: 'Active and connected', 'Active with error', 'Partially Connected' or 'Inactive'.

* **Last Fetch Status** - The status of the last fetch as displayed on the  **Adapter Fetch History** page.

* **Connection Label**  - The connection label (if configured).

* **Connection ID**  - The connection ID.

* **Discovery Schedule** – The discovery schedule, this is ‘Global', 'Custom’  or 'Real time'.

* **Search Connection Configuration** -  Search adapter connections by a key, value or combination of a key and string value of an adapter connection configuration. Note that all values are searched as string values. To search multiple values, they must be adjacent, and with the exact syntax that appears in the **Connection Configuration** column.

* **Search Notes** - Search **Notes**.

* **Last Successful Fetch** - Set a time range for the last successful fetch, to display only fetches in that time zone.

* **Data Scope** - If the adapter connection is restricted by a data scope, the name of the data scope.

* You can use **Select all**, and **Clear all** in any of the filters to select or clear all of the options.

* Click **Reset** to clear all filters.

## Sorting the Display

Click on a column to sort by a specific value. <br />
For instance, you can sort by **Connection Status**.

<Image alt="Adapter Sort Connection columns.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Sort%20Connection%20columns.png" />

## Editing Connection Information for a Specific Adapter Connection

You can edit connection information for a specific adapter connection.

1. Click on a connection.
2. Click anywhere in the row (except on the adapter name).
3. The **Connection** drawer opens with the configuration information for this connection

<Image alt="ConnectorSeeDetails2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConnectorSeeDetails2.png" />

4. Edit this information as required.

## Adding a New Connection

You can add a new adapter connection either from the Adapters page or from the Connections page.
Learn more about [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Connection Actions

You can perform actions on a single connection or in bulk on a number of selected connections.

### Fetching Adapter Connections

1. You can run fetch on one or more adapter connections.
2. Hover over one adapter, or select one or more adapters.

<Image alt="Adapter Connections Bulk Fetch.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Connections%20Bulk%20Fetch.png" />

3. Select **Fetch**.

### Activating Adapter Connections

1. You can activate one or more adapter connections.
2. Hover over one connection, or select one or more connections.  You can only select connections that were already configured previously.

<Image alt="Adapter Connections Bulk Activate.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Connections%20Bulk%20Activate.png" />

3. Select **Activate**. The selected connections are activated according to their configuration in the adapter connection drawer. If for any reason it is not possible to activate all the connections, the system shows an appropriate message.

### Deleting Connections

1. You can delete one or more adapter connections.
2. Hover over one adapter, or select one or more adapters.

<Image alt="Adapter Connections Delete New.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Connections%20Delete%20New.png" />

3. Select **Delete**.
4. A dialog box opens asking you to confirm. You can select to 'Also delete all asset entities that were fetched by this connection'. When you select this option, the assets on this connection begin to be deleted immediately. If a fetch is in progress it is not terminated, so you might have to run delete again to make sure everything is deleted.

## Exporting Adapter Connections to CSV

You can export the Adapter Connections table data to a CSV file. To export the results to a CSV file:

In the **Adapter Connections** page, click **Export CSV** on the right side of the page just above the table.

The CSV file is automatically downloaded with a name format of:
*`adapters_connections_< date >T< time >UTC.csv`*

Depending on your operating system settings, you may be able to edit the file name.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).