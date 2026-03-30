# Source: https://docs.axonius.com/docs/spiceworks.md

# Spiceworks

Spiceworks provides network monitoring to capture, analyze, and monitor network traffic.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Spiceworks Domain** *(required)* - The hostname or IP address of the Spiceworks server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1786\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Spiceworks server in parallel at any given point.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>