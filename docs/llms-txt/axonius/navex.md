# Source: https://docs.axonius.com/docs/navex.md

# NAVEX

NAVEX is a governance, risk, and compliance management platform for employee, third-party, and business processes management.

### Asset Types Fetched

* Devices, Users, Groups

## Before You Begin

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the NAVEX IRM API.

### Permissions

The authentication account must have:

* Fetch Users: Administrative Access - Read permissions to Administer - Users
* Fetch groups: Administrative Access - Read permissions to Administer - Groups
* Assign group to users: Administrative Access - Read and Update permissions to Administer - Groups
* Create User: Administrative Access - Create and Read permissions to Administer - Users
* Update User: Administrative Access - Read and Update permissions to Administer - Users
* Delete User: Administrative Access - Read and Delete permissions to Administer - Users

#### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address (Instance Name)** - The hostname or IP address of the NAVEX server.
2. **Port** - The port used for the connection.
3. **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.
4. **Report ID** - The ID for the desired report.

<Image alt="NAVEX" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NAVEX.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**\* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users from Users** - Enable this option to fetch users.
2. **Fetch Groups from Groups** - Enable this option to fetch groups.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [NAVEX - Create User](/docs/navex-create-user)
* [NAVEX - Delete User](/docs/navex-delete-user)
* [NAVEX - Assign User Group](/docs/navex-update-users-groups)
* [NAVEX - Update User Details](/docs/navex-update-user)