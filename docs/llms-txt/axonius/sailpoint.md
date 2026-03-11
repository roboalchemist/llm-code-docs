# Source: https://docs.axonius.com/docs/sailpoint.md

# SailPoint Identity Manager

SailPoint provides access governance and identity management.

**Related Enforcement Actions**

* [Sailpoint - Disable Users](/docs/disable-sailpoint-user)
* [Sailpoint Identity Manager - Add/Remove User From Group](/docs/sailpoint-add-remove-user-from-group)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Permissions

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SailPoint server.

2. **Client ID** and **Client Secret** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For details, see [API Authentication](https://documentation.sailpoint.com/identityiq/help/systemconfig/api_authentication.html).

3. **Auth Method** - Select Authentication method, either OAuth (default) or OAuth 2.0.

4. **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SailPoint Identity Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SailPoint%20Identity%20Manager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Identify ID as Employee ID** -  Select this option to use the Identity ID as the user's Employee ID.
2. **Fetch Users** - Select to fetch users from **Accounts** or **Public Identities**.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SailPoint - SaaS API](https://developer.sailpoint.com/idn/api/v3).

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with ORG\_ADMIN authority permissions.

### Obtaining the Client ID and Client Secret.

**To generate a Client ID and Client Secret**

1. Access IdentityNow
2. In preferences. create a new Personal Token.

For full details refer to Authentication in the [ SailPoint API Reference Guide](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens).

## Supported From Version

Supported from Axonius version 4.5