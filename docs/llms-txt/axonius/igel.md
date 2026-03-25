# Source: https://docs.axonius.com/docs/igel.md

# IGEL Universal Management Suite (UMS)

IGEL Universal Management Suite (UMS) is a single management solution for decentralized endpoints.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IGEL UMS server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(optional, default: 8443)* - The port used for the connection. If no port is specified, Axonius will use **Port 8443** by default.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).

<Image alt="IGELUMS.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IGELUMS.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch thin devices** *(optional)* - Select to fetch all devices including thin clients and their monitors.
2. **Fetch only thin devices** *(optional)* - Select this option to only fetch thin clients and their monitors.
3. **Fetch monitors as devices** *(optional)* - Select this option to fetch monitors as devices.
4. **Use firmware as OS** *(optional)* - Select this option to fetch firmware information and parse it as OS.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8443**

## Supported From Version

Supported from version 4.4