# Source: https://docs.axonius.com/docs/trace3-lamp.md

# Trace3 LAMP

Trace3 Technology Lifecycle Management Platform (LAMP) is an IT Asset Management (ITAM) platform.

**Related Enforcement Actions:**

* [Trace3 Lamp - Update Device](/docs/trace3-lamp-update-device)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `http://lampapi.trace3.com`)* - The hostname or IP address of the Trace3 LAMP server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Trace3%20LAMP](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trace3%20LAMP.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Additional fields to parse** - Enter a list of field names from the raw data of a device to be dynamically parsed into the device fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Trace3 LAMP Connect API.

<Callout icon="📘" theme="info">
  Note

  Make sure the API returns Hostname for devices to arrive.
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **80/443**

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1