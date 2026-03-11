# Source: https://docs.axonius.com/docs/silverfort.md

# Silverfort

Silverfort is a unified identity protection platform that integrates with IAM solutions to provide secure access to company resources.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Silverfort server.

2. **App User ID** and **App User Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Risk API Key (External Access)** *(optional)* - An API key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. Use this API key in third party systems to access the Silverfort risk score.

4. **Policy API Key (External Access)** *(optional)* - An API key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. Use this API key in third-party systems to access the Silverfort policy data.

<Callout icon="📘" theme="info">
  Note

  All four pieces of the above information are generated through the UI of Silverfort and instructions can be found in the Silverfort REST API Reference.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Silverfort](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Silverfort.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Users with Service Accounts** - Toggle on to enrich users with service accounts.
2. **Enrich Users with Policies** - Toggle on to enrich users with MFA policies.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Silverfort REST API.

## Required Permissions

The value supplied in [Risk API Key](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1