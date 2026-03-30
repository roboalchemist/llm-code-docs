# Source: https://docs.axonius.com/docs/tanium-comply.md

# Tanium Comply

Tanium Comply conducts vulnerability and compliance assessments against operating systems, applications, security configurations, and policies.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Tanium Comply server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name or API Token ID** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the ID of the API token. The Token ID column in Tanium may be hidden.

3. **Password or API Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the API token string.

<Callout icon="📘" theme="info">
  More information on API Tokens

  * When connecting to a Tanium Cloud instance, an API token **must** be used.
  * When creating an API token in Tanium, the default value for "Expire in Days" is 7. It is recommended to set this value to the maximum allowed value of 365.
  * Please see the Tanium Documentation on [Managing API tokens](https://www.tanium.com/blog/getting-data-out-of-tanium-with-the-api-gateway-and-graphql/) for more information.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="TaniumComply" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TaniumComply.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch compliance findings** - Select this option to fetch compliance findings.
2. **Fetch installed software** - Select this option to fetch installed software.
3. **Fetch driver details** - Select this option to fetch driver details.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Tanium Gateway](https://help.tanium.com/bundle/ug_gateway_cloud/page/gateway/overview.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name/API Token ID](#parameters) must have ReadOnly permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Tanium Comply V2.11 | Yes       | --    |

<Callout icon="📘" theme="info">
  Note

  Some Tanium data may only be available with certain versions of Tanium and Tanium API.
</Callout>

## Supported From Version

Supported from Axonius version 5.0