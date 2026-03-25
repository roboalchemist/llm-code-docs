# Source: https://docs.axonius.com/docs/eracent.md

# Eracent

Eracent provides IT asset management and software asset management solutions to help customers inventory assets and optimize licensing costs.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Eracent server.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **Token** is required.
</Callout>

4. **Token** *(optional)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Token** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Eracent](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Eracent.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use LAN name as hostname** - Select this option to use the field "LanName" instead of "DnsName" for the Hostname field.
2. **Fetch device catalog** - Select this option to fetch catalog info for the device.
3. **Fetch device usage type** - Select this option to fetch the device usage type.
4. **Fetch device installed software** - Select this option to fetch installed software for devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Eracent IT Management Center API.

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to fetch assets.

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to access:

* Discovery Web API
* Lifecycle Web API
* Processes Web API

## Supported From Version

Supported from Axonius version 4.5