# Source: https://docs.axonius.com/docs/wazuh.md

# Wazuh

Wazuh is a free, open source and enterprise-ready security monitoring solution for threat detection, integrity monitoring, incident response and compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Wazuh Domain** – Enter the hostname of the Wazuh server.
2. **Port** *(required, default: 55000)* - Enter the port to be used in the connection.
3. **User Name** and **Password** *(required)* – The username and password for an account that has Read access to the API.
4. **Use API V4** - Select to use API version 4, which allows fetching vulnerabilities data. When cleared, API V3 is selected.
5. **API Rate Limit (Calls per Minute)**  (default 300) - Configure the API rate per minute (the number of API calls being made).
6. **Is Cloud** - Select if you're using Wazuh Cloud instead of an on-premises version of Wazuh.
7. **Verify SSL** – Select whether to verify the SSL certificate of the server.
8. **HTTPS Proxy** *(optional)* – Connect the adapter to a proxy instead of directly connecting it to the domain.

<Image alt="wazuh.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/wazuh.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** - Select to fetch vulnerabilities for each agent.

<Callout icon="📘" theme="info">
  Note

  Verify that **Use API V4** is selected, as API V3 doesn't support this option.
</Callout>

2. **Include agent extra items** - Select this option to fetch extra information about the asset such as system inventory items, or the scan database.
3. **Fetch policy checks** - Select this option to fetch  policy checks related to the SCA database items.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Wazuh API](https://documentation.wazuh.com/current/user-manual/api/reference.html#operation/api.controllers.agent_controller.get_agents).

## Supported From Version

Supported from Axonius version 4.5