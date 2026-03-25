# Source: https://docs.axonius.com/docs/zerofox.md

# ZeroFox

ZeroFox is an intelligence-based analysis and remediation engine used to detect digital risks such as phishing, malware, impersonation, and piracy targeted at digital assets. Integrate ZeroFox with the Axonius Cybersecurity Asset Management Platform.

<Callout icon="📘" theme="info">
  Note

  Not all ZeroFox plans include API access. Please contact your ZeroFox account representative to ensure it is available on your account to use with this adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ZeroFox server.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

5. **Verify SSL** *(required, default: false)* - Select to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ZeroFox(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZeroFox\(1\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch alert for users** *(optional, default: false)* - Select to fetch alerts for the account and attach any of the alerts to their respective users.
2. **Async chunks in parallel** *(optional, default: 50)* - Specify the number of chunks to split asynchronous requests.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ZeroFox API](https://api.zerofox.com/1.0/docs/).

## Supported From Version

Supported from Axonius version 4.5