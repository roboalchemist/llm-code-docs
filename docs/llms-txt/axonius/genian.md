# Source: https://docs.axonius.com/docs/genian.md

# Genian

Genian NAC identifies and monitors all hardware and software in the network environment to determine each device’s security state then establish the appropriate level of access to ensure compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Genian server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate an API Key from the Genian NAC web console, go to **Management** `>` **User** `>` **Administration** tab `>` **API Key**.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Genians" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Genians.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Ingest Only Active** - Select this option to ingest only devices with ACTIVE status.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [getUsers Genian REST API](https://docs.genians.com/release/api/#api-Users-getUsers).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **Port 8443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7