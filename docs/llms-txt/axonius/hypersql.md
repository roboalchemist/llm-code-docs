# Source: https://docs.axonius.com/docs/hypersql.md

# HyperSQL

The HyperSQL adapter imports device information from an HyperSQL database.

## Parameters

1. **HSQL Server Host** *(required)* - The hostname or IP address of the HyperSQL server.
2. **Port** *(required, default: 9001)* - The port of the HyperSQL server.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
4. **HSQL Server Database Name** *(required)* - The database to connect to.
5. **HSQL Server Table Name** *(required)* - The table name of the required SQL table.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HyperSQL.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HyperSQL.png)

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

## APIs

Axonius uses the [HyperSQL API](http://www.hsqldb.org/doc/2.0/guide/running-chapt.html).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| HyperSQL V2 | Yes       |       |