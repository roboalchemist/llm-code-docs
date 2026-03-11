# Source: https://docs.axonius.com/docs/freshdesk.md

# Freshdesk

Freshdesk is a cloud-based customer support platform that was founded with the mission of enabling companies of all sizes to provide great customer service.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Freshdesk server. It is typically in the format of *domain.freshdesk.com*.
2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. See the [Freshdesk Developer Guide](https://developer.freshdesk.com/api/#getting-started) for instructions on how to generate the API key.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

![Freshdesk connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NI06V37Y.png)

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Agents with Agent Groups** *(optional)* - Enabled by default. Use this option to fetch group data for Agent users.
2. **Enrich Agents with Agent Roles** *(optional)* - Enabled by default. Use this option to fetch agent data for Agent users.
3. Select the relevant option(s) to determine from where to fetch customer contact sub type. You can fetch from Unverified / Verified / Blocked / Deleted contacts (all optional):
   * **Fetch users of sub type Contact from Unverified Contacts**
   * **Fetch users of sub type Contact from Verified Contacts**
   * **Fetch users of sub type Contact from Blocked Contacts**
   * **Fetch users of sub type Contact from Deleted Contacts**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Freshdesk API](https://developer.freshdesk.com/api/#introduction).

## Supported From Version

Supported from Axonius version 6.1