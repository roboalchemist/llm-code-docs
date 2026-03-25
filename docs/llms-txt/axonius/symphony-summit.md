# Source: https://docs.axonius.com/docs/symphony-summit.md

# SymphonyAI Summit

SymphonyAI Summit is an ITSM solution that provides automation libraries for automating repetitive and manual tasks.

**Related Enforcement Actions**

* [SymphonyAI Summit - Create Ticket](/docs/create-symphony-ticket)
* [SymphonyAI Summit - Create Ticket per Entity](/docs/create-symphony-ticket-per-entity)
* [SymphonyAI Summit - Create or Update Assets](/docs/create-or-update-symphony-asset)
* [SymphonyAI Summit - Create or Update CMDB Assets](/docs/create-or-update-symphony-cmdb-asset)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Tickets

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SymphonyAI Summit server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate the API key, see [API Authentication and Authorization](https://docs.symphonysummitai.com/display/TAH/API+Authentication+and+Authorization).

3. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SymphonyAI\_Summit\_Adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SymphonyAI_Summit_Adapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices from AM\_GetAssetDetails endpoint** - By default Axonius fetches devices from the `AM_GetAssetDetails` endpoint. Clear this option to not fetch devices from this endpoint.
2. **Fetch devices from CMDB CI (CMDB\_LoadCIRecords) by Instance Name** - Enter a comma-separated list of instance names in order to fetch devices from CMDB CI (CMDB\_LoadCIRecords).
3. **Ignore devices from CMDB CI by Classification ID** - Enter a comma-separated list of classification IDs in order to ignore devices from CMDB CI.
4. **Fetch Tickets** -  Toggle on this option to fetch tickets.
   1. **Fetch Tickets from the past X Days** *(optional, default: 10)* - Select the number of days back from which to fetch tickets.
   2. **Tickets per page** *(optional, default: 500)* - Select the number of tickets per page.
   3. **Workgroup Name** - Enter the workgroup name.
   4. **Instance Name** - Enter the name of your SymphonyAI Summit instance.
   5. **Ticket Status to fetch** - Select the ticket status to fetch from the dropdown.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SymphonyAI Summit API](https://docs.symphonysummitai.com/display/TAH/API+Authentication+and+Authorization).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following port:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.0