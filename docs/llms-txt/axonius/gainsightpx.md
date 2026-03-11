# Source: https://docs.axonius.com/docs/gainsightpx.md

# Gainsight PX

Gainsight PX is a product experience platform that helps businesses understand and improve user engagement with their software products.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Gainsight server. Use one of the following values:
   * Accounts on the EU server - Use *[https://api-eu.aptrinsic.com/v1](https://api-eu.aptrinsic.com/v1)*
   * Accounts on the US server - Use either *[https://api.aptrinsic.com/v1](https://api.aptrinsic.com/v1)* OR *[https://api-us2.aptrinsic.com/v1](https://api-us2.aptrinsic.com/v1)*

2. **API Key** *(required)* - An Aptrinsic API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Gainsight PX](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Gainsight%20PX.png)

## APIs

Axonius uses the [Gainsight PX REST API](https://gainsightpx.docs.apiary.io/#).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v1  | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1