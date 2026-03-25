# Source: https://docs.axonius.com/docs/sysaid.md

# SysAid

SysAid is an integrated ITSM, Service Desk and Help Desk software solution.

**Related Enforcement Actions**

* [SysAid - Create Incident](/docs/create-sysaid-incident)
* [SysAid - Update Ticket](/docs/sysaid-update-ticket)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **SysAid Domain** *(required)* - The hostname or IP address of the SysAid server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SysAid" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SysAid.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Fetch users** *(required, default: true)* - Select this option to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SysAid REST API](https://documentation.sysaid.com/docs/rest-api-details#service-requests).

## Permissions

Administrator, with permission to access the mobile app.