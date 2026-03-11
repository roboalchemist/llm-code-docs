# Source: https://docs.axonius.com/docs/cdw.md

# CDW

CDW is a multi-brand technology solutions provider.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* SaaS data

## Parameters

1. **Host Name or IP Address** *(required, default: `https://www.cdw.com`)* - The hostname or IP address of the CDW server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **2FA Secret Key** *(optional)* - The secret generated in the adapter for setting up 2-factor authentication for the adapter user created to collect SaaS data.

4. **Custom Login URL** *(optional)* - The URL as it appears in the browser's address bar after signing-in, if using  a custom SSO provider.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CDW" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CDW.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Custom Report Name** - Enter a name in this field to fetch  expense data from that specific report. This is useful when a custom report contains more fields than the default one. When left empty, Axonius fetches data from the default "Current Year Report" which may not include all the required fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permission for software and reporting   to in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0