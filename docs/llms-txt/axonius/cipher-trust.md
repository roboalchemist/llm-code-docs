# Source: https://docs.axonius.com/docs/cipher-trust.md

# CipherTrust Manager

Thales CipherTrust Manager is a key management solution for the CipherTrust Data Security Platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Licenses
* SaaS Applications
* Compute Services

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CipherTrust Manager server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CipherTrust%20Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CipherTrust%20Manager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - By default the adapter enriches users via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Fetch Devices of sub type device2 from Clients Endpoint** - Toggle on to fetch devices of the subtype device2 from the Clients endpoint. When enabled, the following setting can be configured:
    * **Enrich Clients Endpoint with Client Guard Status** - Toggle on to enrich the clients endpoint with client guard status.
  * **Fetch ComputeServices from Clusters Summary Endpoint** - Toggle on to fetch compute services from the Cluster Summary endpoint.
  * **Fetch Licenses from Licensing Features Endpoint** - Toggle on to fetch licenses from the Licensing Features endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [CipherTrust Manager Administration REST API](https://thalesdocs.com/ctp/cm/2.13/admin/cm_admin/rest-api/index.html).

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0