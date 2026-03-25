# Source: https://docs.axonius.com/docs/team-dynamix.md

# TeamDynamix

TeamDynamix is an ITSM/ESM and project portfolio management solution with enterprise integration and automation.

## Types of Assets Fetched

Devices, Users

## Before You Begin

### &#x20;APIs

Axonius uses the [TeamDynamix Web API](https://solutions.teamdynamix.com/TDWebApi/).

### Permissions

Refer to your vendor for detailed information about the Roles and Permissions required to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TeamDynamix server. This should be in the format of the full domain including the API path and look like this `https://customerdomain.teamdynamix.com/{API_Prefix}`

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

<Image alt="TEamDynamix" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/TeamDynanix.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users** - By default this adapter fetches users, clear this option to not fetch users.
2. **Fetch EC Action ticket updates** - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the **Tickets** table showing information on all tickets in the system (**Assets> Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).
   <br />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

## Supported From Version

Supported from Axonius version 4.8

**Related Enforcement Actions:**

* [TeamDynamix - Create Ticket](/docs/create-team-dynamix-ticket)
* [TeamDynamix - Create or Update Asset](/docs/teamdynamix-create-or-update-asset)