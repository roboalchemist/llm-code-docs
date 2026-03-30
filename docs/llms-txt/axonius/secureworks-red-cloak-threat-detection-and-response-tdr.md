# Source: https://docs.axonius.com/docs/secureworks-red-cloak-threat-detection-and-response-tdr.md

# Secureworks Taegis XDR (Red Cloak TDR)

Secureworks Taegis XDR (formerly Red Cloak TDR) is an endpoint detection and response technology for the cloud, endpoints and the network.

**Related Enforcement Actions:**

* [Secureworks Taegis XDR - Add/Remove Tag](/docs/redcloak-tdr-add-remove-tag)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Client ID** and **Client Secret** *(required)* - The credentials for an account that has the permissions to fetch assets.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

6. **Secureworks Region** *(optional, default: US1)* - Select the region of your domain.

<Callout icon="📘" theme="info">
  Region Identification

  The following URLs are associated with each drop-down selection on the connection configuration panel:

  * **US1** - *[https://api.ctpx.secureworks.com](https://api.ctpx.secureworks.com)*

  * **US2** - *[https://api.delta.taegis.secureworks.com](https://api.delta.taegis.secureworks.com)*

  * **EU** - *[https://api.echo.taegis.secureworks.com](https://api.echo.taegis.secureworks.com)*
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SecureworksTaegis XDR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecureworksTaegis%20XDR.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use Only IngestTime As Last Seen** -  Select this option to use only IngestTime as last seen.
2. **Fetch Last Seen** - From the dropdown, select whether to parse lastSeenAt or datasource/lastSeen (default value) or to parse the latest time between lastSeenAt and ingest time.
3. **Exclude IPs older than 24 hours** *(required, default: False)* - Set this parameter to only add IP addresses if they were last seen in the last 24 hours. If there are no IP addresses seen in the last 24 hours, the single latest IP will be added, even if the last seen is older than 24 hours.
4. **Fetch DataSource data** - Select this option to add the DataSource data to each asset, if available.
5. **Filter Assets by Asset State** *(default: All)* - You can filter assets by choosing the asset state value. From the dropdown, select one or more asset state values.
6. **Calculate Agent Health** - Toggle on **Calculate Agent Health** to  add a calculated agent health for the selected module to each device. You can select as many modules as required. The agents status will return one value in the agent status field of either ‘Healthy’ or ‘Unhealthy’. If even one module out of all modules selected reported unhealthy the agent status will report as ‘Unhealthy’.

![TaegisModuelSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TaegisModuelSettings.png)

7. **Filter by tags** - Enter a comma-separated list of tags to filter devices during fetch.

## APIs

Axonius uses the [Secureworks Taegis XDR Assets GraphQL API](https://docs.ctpx.secureworks.com/apis/using_assets_api/).