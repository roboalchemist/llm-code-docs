# Source: https://docs.axonius.com/docs/citrix-adc.md

# Citrix ADC

Citrix ADC is an application delivery and load balancing solution for monolithic and microservices-based applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Load Balancers

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Citrix ADC server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CITRIX ADC.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CITRIX%20ADC.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Optional items to fetch** - From the dropdown, select one or more of the following: Load Balancer Virtual Server fields, Version fields, or License fields.
2. **Fetch Interfaces** *(default: true)* - Select whether to fetch interfaces.
3. **Fetch VPN Servers** *(default: true)* - Select whether to fetch VPN servers.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Citrix NetScaler Rest API](https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/12.0/api-reference/).

## Required Permissions

The value supplied in [User Name](#parameters) must have administrater permissions for the NetScaler appliance to fetch assets.
Refer to [Citrix NetScaler 12.0 NITRO API Reference](https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/12.0/before-you-begin/#prerequisites).

## Version Matrix

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Citrix NetScaler 12.0 | Yes       |       |

This adapter has only been tested with the versions marked as supported, but may work with lower versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.