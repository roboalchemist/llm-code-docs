# Source: https://docs.axonius.com/docs/acronis.md

# Acronis

Acronis is a backup solution providing data protection and recovery for servers and endpoints.

<Callout icon="📘" theme="info">
  Note

  The Acronis platform does not have an API for on-premise servers. Therefore Axonius cannot connect to Acronis on-premises deployments.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Datacenter URL** *(required, default: `https://eu2-cloud.acronis.com`)* - The hostname or IP address of the Acronis server.

2. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret associated with a user account that has permission to fetch assets.

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Acronis](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Acronis.png)

## APIs

Axonius uses the Acronis Agents API. For more details, see the following links:

* [Fetching a list of agents](https://developer.acronis.com/doc/agents/v2/guide/agents/fetching-agents.html)
* [Pagination](https://developer.acronis.com/doc/agents/v2/guide/overview/pagination.html)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v2  | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1