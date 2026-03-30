# Source: https://docs.axonius.com/docs/vulcan.md

# Vulcan Cyber

The Vulcan Cyber ExposureOS is designed to help information security teams aggregate, correlate, prioritize, and remediate exposure risk across all attack surfaces, from one platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

### Required Permissions

The owner of the API Token must have permissions to the Standard role or greater to fetch assets.

### Acquiring an API Token

You can acquire an API token from your Vulcan Cyber account.

To acquire an API Token:

1. From the Vulcan Account page, click your avatar icon in the upper right corner and navigate to the API token.
2. Specify a name for the token in the relevant field.
3. Specify an expiration date. By default, the token expires one year from the token creation.
4. Click **Generate Token** to generate an OAuth 2 token.
5. Copy and paste the API token in the **API Token** parameter of the Vulcan adapter for Axonius.

<Callout icon="📘" theme="info">
  Note

  You can revoke any of your tokens if needed by clicking the **Revoke** button.
</Callout>

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Vulcan Cyber server.

2. **API Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. To acquire an API Token, see [Acquiring an API Token](/docs/vulcan#acquiring-an-api-token).

3. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Vulcan](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vulcan.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** - Select this option to fetch Aggregated Security Findings.
2. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Vulcan Cyber server in parallel at any given point.
3. **Fetch assets from export** - Select this option to fetch assets and findings from the export endpoints.
4. **Minutes to wait for the export data** *(optional, default: 20)* - Specify the number of minutes for the adapter to wait for the export process to finish.
5. **Findings export advanced settings** - Enable this option to define specific fields or attributes to fetch. For example, you can specify Findings fields to export, exclude/include specific fields, and more.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 4.5