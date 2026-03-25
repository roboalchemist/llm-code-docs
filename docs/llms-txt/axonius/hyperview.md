# Source: https://docs.axonius.com/docs/hyperview.md

# Hyperview DCIM

Hyperview DCIM is a data center infrastructure management solution that provides real-time monitoring, asset management, and capacity planning for data centers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Hyperview DCIM server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for  a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Hyperview DCIM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Hyperview%20DCIM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Asset Types** *(optional)* - From the dropdown, select one or more asset types to fetch.
2. **Enrich Assets Endpoint with Component Asset Endpoint** - By default, this adapter enriches the assets endpoint with the component asset endpoint. Toggle off to not enrich the assets endpoint with the component asset endpoint.
3. **Enrich Assets Endpoint with Software Endpoint** - By default, this adapter enriches the assets endpoint with the software endpoint. Toggle off to not enrich the assets endpoint with the software endpoint.
4. **Enrich Assets Endpoint with IP Properties Endpoint** - By default, this adapter enriches the assets endpoint with the IP properties endpoint. Toggle off to not enrich the assets endpoint with the IP properties endpoint.
5. **Enrich Assets Endpoint with Host Properties Endpoint** - Toggle on to enrich the assets endpoint with the host properties endpoint.
6. **Enrich Assets Endpoint with Asset Properties Endpoint** - Toggle on to enrich the assets endpoint with the asset properties endpoint.
7. **Enrich Assets Endpoint with Asset Summaries Endpoint** - Toggle on to enrich the assets endpoint with the asset summaries endpoint.
8. **Enrich Assets Endpoint with Asset Lifecycle Endpoint** - Toggle on to enrich the assets endpoint with the asset lifecycle endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Hyperview API 4.0](https://docs.hyperviewhq.com/redoc-static.html#tag/Assets/paths/~1api~1asset~1assets/get).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must be associated with credentials that have `HyperviewManagerApi` permissions in order to fetch assets. For more information, see [Returns a list of assets](https://docs.hyperviewhq.com/redoc-static.html#tag/Assets/paths/~1api~1asset~1assets/get).

## Supported From Version

Supported from Axonius version 6.1.38.2