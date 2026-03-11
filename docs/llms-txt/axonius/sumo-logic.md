# Source: https://docs.axonius.com/docs/sumo-logic.md

# Sumo Logic

Sumo Logic is a cloud-based service for logs & metrics management for modern apps.

**Related Enforcement Actions**
[SumoLogic - Send Activities to SumoLogic SIEM](/docs/sumo-logic-siem-send-json-to-http-logs)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Sumo Logic Service URL** *(required, default: `https://service.sumologic.com`)* - The Sumo Logic Service Endpoint (Login URL). See more info at [Sumo Logic Endpoints](https://help.sumologic.com/APIs/General-API-Information/Sumo-Logic-Endpoints-and-Firewall-Security).
2. **Access ID** and **Access Key** *(required)* - The Access ID and Access key for a user account that has permissions to fetch assets. See more info at [Sumo Logic Access Key](https://help.sumologic.com/Manage/Security/Access-Keys)
3. **Search Query** *(required)* - The actual search to run in Sumo Logic. Each record (aggregation query result) that is returned from this search is presented as an asset.
4. **Data Contains Users Information** - Select this option to consider the data from Sumo Logic query results as users data.
5. **Data Contains Devices Information** - Select this option to consider the data from Sumo Logic query results as devices data.

<Callout icon="📘" theme="info">
  Note

  Use both of these options in order to consider the data from  Sumo Logic query results as both **devices** and **users** data in the same fetch.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SumoLogic](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SumoLogic.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of days to fetch** *(required, default: 30)* - The number of days to fetch devices.
2. **Maximum amount of messages for search** *(required, default: 100000)* -  Limitation on the amount of returned results .
3. **Consume raw messages** - Select whether to consume raw messages (query results) from Sumo Logic. If you select this option, each raw message is returned as an asset in Axonius. If not, only records are returned as assets.
4. **Fetch users** - Toggle on to fetch users. If enabled, the following setting may be configured.
   * **Fetch user roles** - Select this option to fetch user roles.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Search Job API.

## Required Ports

* **TCP port 443**