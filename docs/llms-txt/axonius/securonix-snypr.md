# Source: https://docs.axonius.com/docs/securonix-snypr.md

# Securonix SNYPR

Securonix SNYPR is a platform for security analytics, using machine learning to detect and respond to threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required, default: `https://snypr.domain.tld`)* - The hostname or IP address of the Securonix SNYPR server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **API Key**.
   * **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.
   * **API Key** - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Securonix SNYPR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Securonix%20SNYPR.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices from Assets** *(default: true)* - By default this adapter fetches devices. Toggle off to not fetch devices.
2. **Fetch Users from Users** *(default: true)* - By default this adapter fetches users. Toggle off to not fetch users.
3. **Fetch Incidents from Events** - Toggle on to fetch incidents from events. If this setting is enabled, the settings below may be configured.
   * **Resource Group Name Filter** - Enter resource group names to filter out of the fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Assets endpoint](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/rest-api-categories-asset.htm)
* [Users endpoint](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/rest-api-categories-users.htm)
* [Token Authentication](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm)
* [Activity endpoint](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/rest-api-categories-activity.htm)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1