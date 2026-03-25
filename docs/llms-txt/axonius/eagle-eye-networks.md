# Source: https://docs.axonius.com/docs/eagle-eye-networks.md

# Eagle Eye Networks

Eagle Eye Networks provides cloud-based video surveillance products for physical security and business operations applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Eagle Eye Networks server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Eagle%20Eye%20Networks(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Eagle%20Eye%20Networks\(1\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - Click the arrow.
  * **Enrich Device with Extra Device Info** - Toggle on to enrich the device with extra device information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Eagle Eye Video API Platform](https://developer.eagleeyenetworks.com/).

## Supported From Version

Supported from Axonius version 6.0