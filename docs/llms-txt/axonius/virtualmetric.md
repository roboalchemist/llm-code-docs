# Source: https://docs.axonius.com/docs/virtualmetric.md

# VirtualMetric

VirtualMetric is a monitoring solution that offers real-time insights into IT infrastructure performance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the VirtualMetric server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![VirtualMetric](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VirtualMetric.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Choose field to populate Host Name field** *(optional, default: FQDN)* - From the dropdown, select a field to populate the Host Name field, either **FQDN** or **HostIP**.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [VirtualMetric Developer API](https://demoapi.virtualmetric.com/).

## Required Permissions

* VirtualMetric uses Oauth2 to authenticate users from external applications.
* Authenticated users can only access data in their own scopes.
* Only System Admin users can access all scopes.

## Supported From Version

Supported from Axonius version 6.1.41.0