# Source: https://docs.axonius.com/docs/automox.md

# Automox

Automox is a cloud-based patch and configuration management solution for Windows, Linux, Mac, and third-party software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

## Parameters

1. **Automox Domain** *(required)* - The hostname or IP address of the Automox server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Organization IDs** *(optional)* - Enter Organization IDs from which to fetch data. If left blank, the adapter will fetch data from all organizations IDs. To enter values, enter a value and press Enter.

4. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Automox Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Automox Domain**.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Automox Domain** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Automox Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Automox" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Automox.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Last Seen will prioritize Last Disconnect Time when not empty** - When selected, Last Disconnect Time will be the priority when calculating Last Seen.
2. **Do not include Public IPs in Network Interfaces** - When selected, Public IP addresses won't appear in the Network Interfaces of the fetched devices.
3. **Enrich devices with server data** - Select this option to enrich devices with server data from this endpoint:  [https://developer.automox.com/openapi/axconsole/operation/getServerGroup/](https://developer.automox.com/openapi/axconsole/operation/getServerGroup/)
4. **Entities per page** *(default: 500)* - Set the number of entities returned per page request (Minimum: 10; Maximum: 500).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [API Key](#parameters) must have read access to devices.

From the Automox console **Settings** page, select the **API** tab to access your API keys. Then generate and copy an API key.

## Related Enforcement Actions

* [Automox - Change Policy](/docs/automox-policy-change)
* [Automox- Install Update](/docs/automox-install-update)
* [Automox - Run Worklet per Asset](/docs/automox-run-worklet-per-asset)
* [Automox - Update Server](https://docs.axonius.com/axonius-help-docs/docs/automox-update-server)
* [Automox - Delete Server](https://docs.axonius.com/axonius-help-docs/docs/automox-delete-server)

##