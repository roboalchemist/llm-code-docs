# Source: https://docs.axonius.com/docs/control-up.md

# ControlUp

ControlUp is a digital workspace management platform that provides real-time monitoring and troubleshooting for virtual desktop infrastructure (VDI) environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.controlup.com`)* - The hostname or IP address of the ControlUp server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Organization ID** *(required)* - Specify your ControlUp organization ID.

3. **Devices Index** \_(required, default: *devices)* - Enter an index of devices to fetch.

4. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ControlUp.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ControlUp.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Devices Endpoint with Software Endpoint** - Toggle on to enrich the devices endpoint with the software endpoint. If this setting is enabled, the settings below may be configured.
   * **Software Index** *(optional)* - Enter an index of software to fetch.
2. **Enrich Devices Endpoint with Vulnerabilities Endpoint** - Toggle on to enrich the devices endpoint with the vulnerabilities endpoint. If this setting is enabled, the settings below may be configured.
   * **Vulnerabilities Index** *(optional)* - Enter an index of vulnerabilities to fetch.
3. **Enrich Devices Endpoint with App Usage Single Endpoint**  - Toggle on to enrich devices with per-user application usage data. If this setting is enabled, the settings below may be configured.
   * **Query time from** - Enter the number of days ago from which to start querying application usage data. Default: 30.
   * **Query time to** - Enter the number of days ago up until which to query application usage data. Default: 0 (today).
4. **App Usage All - applies context on the following endpoints: App Usage Single** -  This fetches all application usage data from ControlUp and supplies it to the App. Usage Single endpoint. The following settings control the query time range.
   * **Query time from**   - Enter the number of days ago from which to start querying application usage data. Default: 30.
   * **Query time to**   - Enter the number of days ago up until which to query application usage data. Default: 0 (today).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ControlUp APIs](https://api.controlup.io/reference/how-to-create-api-keys).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v1  | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1.55.0