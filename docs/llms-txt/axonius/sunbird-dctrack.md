# Source: https://docs.axonius.com/docs/sunbird-dctrack.md

# Sunbird

Sunbird dcTrack is a data center infrastructure monitoring product that provides dashboards and KPIs for remote data center management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Sunbird server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Sunbird.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sunbird.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Device statuses to ignore (comma separated)** *(optional)* - Enter a comma-separated list of device statuses to ignore.

2. **tiClass types to fetch** *(required, default: Device)* - Select one or more tiClass types to fetch.

## APIs

Axonius uses the [dcTrack 8.0.0. REST API](https://www.sunbirddcim.com/help/dcTrack/v800/API/en/Default.htm).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80** (default system port)

## Required Permissions

The value supplied in [User Name](#parameters) uses the Username and password for the dcTrack GUI.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                         | Supported | Notes |
| ------------------------------- | --------- | ----- |
| Sunbird versions 8.0.0 - 8.0.99 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.6