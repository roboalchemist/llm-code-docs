# Source: https://docs.axonius.com/docs/forcepoint-one.md

# Forcepoint ONE

Forcepoint ONE provides data protection that monitors real-time traffic and prevents data loss.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* Activities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://portal.bitglass.com`)* - The hostname or IP address of the Forcepoint ONE server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Token** *(optional)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ForcepointONE](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ForcepointONE.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Backward Days for Log Fetch Start** *(default: 30)* - Specify how many days back the system began fetching logs.
2. **Max Rate Limit Sleep Hours** *(default: 3)* - Specify the maximum number of hours to wait before resending the request after reaching the rate limit. If the connection continues to fail, the fetch stops.
3. **Log types to fetch as devices** - From the dropdown, select one or more log types to fetch as devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Forcepoint ONE Deployment Guide - Exporting access (proxy) logs - examples](https://help.forcepoint.com/fpone/deploy/rhtml/guid-a75358a9-6df2-4f83-8d95-a36eab30bed6.html) API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443/80**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0