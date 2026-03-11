# Source: https://docs.axonius.com/docs/wrike.md

# Wrike

Wrike is software designed to help teams plan, organize, manage, and track tasks and projects.

**Related Enforcement Actions**
[Wrike - Create or Update Task](/docs/wrike-create-update-task)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Wrike server.

2. **Permanent Access Token** *(required)* - A permanent access token never expires, so you can obtain it once and then use it without the need to refresh or re-authenticate. For information on how to obtain a permanent access token, see [OAuth 2.0 Authorization](https://developers.wrike.com/oauth-20-authorization/) under **Permanent Access Token**.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Wrike" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Wrike.png" />

## APIs

Axonius uses the [Wrike API](https://developers.wrike.com/api/v4/contacts/).

## Required Permissions

The credentials supplied must be associated with the following scopes:

* Default
* wsReadOnly
* wsReadWrite

## Supported From Version

Supported from Axonius version 6.1