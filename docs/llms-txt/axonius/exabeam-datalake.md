# Source: https://docs.axonius.com/docs/exabeam-datalake.md

# Exabeam Data Lake

Exabeam Data Lake (previously known as Exabeam Log Manager) is a cloud-native data lake architecture to securely ingest, parse, and store security data at scale from any location, across multi-year data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Exabeam Data Lake server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Username** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Exabeam_Datalake" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Exabeam_Datalake.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **The query for the visualization request** *(required, default: Vendor.keyword:"Microsoft" AND Product:"Microsoft Windows")* - Enter a query to filter by the visualization request.
2. **The default label for the visualization request** *(optional, default: WinEvtx)* - Enter the default label for the visualization request.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the:

* Exabeam Web Commons API
* Exabeam Log Management API

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8080**

## Supported From Version

Supported from Axonius version 4.7