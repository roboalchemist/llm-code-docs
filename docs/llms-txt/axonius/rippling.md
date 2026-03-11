# Source: https://docs.axonius.com/docs/rippling.md

# Rippling

Rippling provides an HR software used to collect, maintain, and analyze data for hiring, onboarding employees, and managing company culture.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.rippling.com`)* - The hostname or IP address of the Rippling server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To create an API Key, see [Creating Your API Key](https://developer.rippling.com/docs/rippling-api/8f924ad751580-customers).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Rippling" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rippling.png" />

## APIs

Axonius uses the [Rippling API](https://developer.rippling.com/docs/rippling-api/2e740d9c3405b-rippling-s-api).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have access to the **employee** scope and one of the following Read-only permissions:

| Permission Name        | Extent of Access                                                 |
| ---------------------- | ---------------------------------------------------------------- |
| employee:read          | Access to all employee information                               |
| employee:\<FIELD>:read | Limited access to a specific field, such as `employee:name:read` |

For additional information, see [Scopes](https://developer.rippling.com/docs/rippling-api/6d3fa31f65d60-scopes).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1.0    | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7