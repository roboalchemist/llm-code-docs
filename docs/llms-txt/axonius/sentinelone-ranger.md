# Source: https://docs.axonius.com/docs/sentinelone-ranger.md

# SentinelOne Ranger

SentinelOne Ranger creates visibility into your network by using distributed passive and active mapping techniques to discover running services, unmanaged endpoints, IoT devices, and mobiles.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP Address of the SentinelOne Ranger management server. This field format is '\[instance].sentinelone.net'.
2. **User Name** and **Password** *(optional, default: empty)* - The user name and password for an account that has site viewer access to the management server.

<Callout icon="📘" theme="info">
  Note

  If **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API token** *(optional, default: empty)* - The API token is created within the My User Profile of the account with viewer access to the management server.

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SentinelOneRanger.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SentinelOneRanger.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Account IDs** - Enter a comma-separated list of account IDs. Only devices from these accounts will be retrieved. To fetch from all accounts, leave this empty.
2. **Site IDs** - Enter a comma-separated list of site IDs. Only devices in these sites will be retrieved. To fetch from all sites, leave this empty.
3. **Deduplicate devices by internal ID** - Select this option to deduplicate devices and to keep only device for each internal ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>