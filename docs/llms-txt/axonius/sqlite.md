# Source: https://docs.axonius.com/docs/sqlite.md

# SQLite

The SQLite adapter imports device information from an SQLite database.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

<Callout icon="📘" theme="info">
  Note

  This adapter is part of the upload file scheme and as such the rest of the adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv) and are not required for the functionality of the adapter.
</Callout>

1. **SQL Server Table Name** *(required)* - The table name of the required SQL table.
2. **Server Tag** *(optional)* - Add a desired tag to the server to be queryable.
3. **File name** *(required)* - A unique name for the adapter connection. The value supplied here will be populated in the **File name** field for the data supplied by a specific adapter connection.

<Callout icon="📘" theme="info">
  Note

  The specified File Name does not need to be the actual imported file name. This field is an identifier for use in the Query Wizard.
</Callout>

4. **Upload file** *(optional)* - Select a local SQL file to import

<Callout icon="📘" theme="info">
  Note

  * When using this option, the data imported from the SQL table will never be fetched again, as the file is static.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SQLite.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SQLite.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections for this adapter.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>