# Source: https://docs.axonius.com/docs/adminbyrequest.md

# Admin by Request

Admin By Request provides centralized and auditable management of local admin rights.

**Related Enforcement Actions:**

* [Admin By Request - Approve or Deny Ticket](/docs/admin-by-request-approve-or-deny-ticket)
* [Admin By Request - Delete Computer](/docs/admin-by-request-delete-computer)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications
* Tickets

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Admin by Request server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AdminbyRequest.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdminbyRequest.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Hide network information** - Select this option to hide network information of a device.
2. **Fetch tickets** - Select this option to fetch tickets as assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Admin By Request Inventory API](https://www.adminbyrequest.com/InventoryAPI).

<Callout icon="📘" theme="info">
  Note

  Admin by Request has quota rules. If quotas are passed, access is blocked for the tenant until the next business day.
  Daily quota: 10,000 API calls
  Rate limit: 100 API calls per minute
</Callout>

## Required Permissions

### Obtaining the API Key

To obtain the API key:

1. From the **Admin By Request Settings** menu, select the **API Access** tab.
2. Copy the API Key.

<Image alt="AdmnbyREquestAPI.png" width="675px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdmnbyREquestAPI.png" />

## Supported From Version

Supported from Axonius version 4.5