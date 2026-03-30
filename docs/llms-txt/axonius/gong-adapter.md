# Source: https://docs.axonius.com/docs/gong-adapter.md

# Gong

Gong is a customer data management platform that automatically captures and updates data from integrated tools, allowing for consolidated visibility into all customer interactions, across all stages of the relationship.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Users, Licenses, Application Settings, SaaS Applications

## Required Permissions

To fetch Application Settings, you must have the following permissions:

* api:users:read
* api:workspaces:read
* api:flows:read

## Connection Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Gong server.

2. **API Key** and **API Secret** *(required)* - An API Key associated with a user account that has the permissions to fetch assets.

3. **Login URL** *(required to fetch Application Setting and Licenses)*- Your Gong login URL. The default value is `https://app.gong.io`.

4. **User Name** and **Password** *(required to fetch Application Setting and Licenses)* - The credentials for a user account that has admin permissions.

5. **2FA Secret Key** - *(relevant only for fetching Application Setting and Licenses)*- If you access Gong through an SSO solution that requires 2-factor authentication, you will need to generate a secret key in that solution and paste it here. See [Set Up Google Authenticator](/docs/okta#step-5-set-up-google-authenticator) in for the Okta adapter, for an example.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/gong_connect.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Settings** - Enable this to fetch Application Settings (disabled by default).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 5.0