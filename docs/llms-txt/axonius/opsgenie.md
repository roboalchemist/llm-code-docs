# Source: https://docs.axonius.com/docs/opsgenie.md

# Opsgenie

Opsgenie is an alerting and incident response tool.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Opsgenie server.

2. **GenieKey** *(required)* - An API Key associated with a user account that has [permissions](#permissions) to fetch assets. To get an API key, see [Opsgenie API Key Management](https://support.atlassian.com/opsgenie/docs/api-key-management/).

3. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Opsgenie" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Opsgenie.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Teams** - Toggle on to fetch teams as Group assets. Each group has a link to its roles and members (users).
  * **Fetch Teams Roles** - Enable this option to fetch the roles of each team as Role assets. This option is available only when **Fetch Teams** is toggled on.

## APIs

Axonius uses the [User API](https://docs.opsgenie.com/docs/user-api#get-user).

The following API endpoints are used to fetch teams, their roles, and their members:

* [List Teams](https://docs.opsgenie.com/docs/team-api#list-teams)(parse as Groups)
* [Get Team](https://docs.opsgenie.com/docs/team-api#get-team)
* [Team Role API](https://docs.opsgenie.com/docs/team-role-api)(parse as SecurityRoles).

## Permissions

The value supplied in [GenieKey](#parameters) must be associated with credentials that have Read and Configuration permissions to fetch the assets.

## Supported From Version

Supported from Axonius version 4.5