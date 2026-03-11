# Source: https://docs.axonius.com/docs/cloudflare-zero-trust.md

# Cloudflare Zero Trust

Deliver Zero Trust Network Access on Cloudflare's Edge.

**Related Enforcement Actions**
[Cloudflare Zero Trust - Revoke User Session](/docs/cloudflare-zero-trust-revoke-user-session)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

**Related Enforcement Actions**

* [Cloudflare Zero Trust - Remove Member](/docs/cloudflare-zero-trust-remove-member)
* [Cloudflare Zero Trust - Revoke User Session](/docs/cloudflare-zero-trust-revoke-user-session)

## Parameters

1. **Host Name or IP Address** *(optional)* - The hostname or IP address of the Cloudflare Zero Trust server.
2. **User Email** *(required)* - Enter the user email.
3. **API Key / API Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](/docs/cloudflare-zero-trust#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  Cloudflare highly recommends using an API token instead of an API key.

  * To create an API token (recommended), see [Create an API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

  * To obtain an API key (legacy), see [Get API Keys (legacy)](https://developers.cloudflare.com/fundamentals/api/get-started/keys/).
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CloudFlare_Zero_Trust" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudFlare_Zero_Trust.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - Click the arrow.
  * **Enrich Devices with Gateway Location**  - Toggle on this option to add subdomain data for each device.
  * **Fetch Devices of sub type deleted\_device from Deleted Devices** - Toggle on to include data on deleted devices.
  * **Fetch Devices of sub type revoked\_device from Deleted Devices** - Toggle on to include data on revoked devices.
  * **Enrich Users with Policies** - Toggle on this option to add policy data for each user.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Cloudflare API v4](https://api.cloudflare.com/).

## Required Permissions

The value supplied in [API Key/Token](#parameters) must be associated with credentials that have permissions to fetch assets.

If an **API Token** (recommended method) is provided, the following permissions are required:

* Account: Zero Trust: Read
* Account: Access: Audit Logs: Read
* Account: Account Settings: Read

If an **API Key** (legacy method) is provided, it will have the same permissions as the user and will have access to **all** of a user’s resources.

## Supported From Version

Supported from Axonius version 4.5