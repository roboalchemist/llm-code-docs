# Source: https://docs.axonius.com/docs/parsec.md

# Parsec

Parsec App is a remote desktop application primarily used for playing games through video streaming.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Parsec server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more details, see [Generate API Key](https://support.parsec.app/hc/en-us/articles/32361349089044-Access-Controls-for-API-Keys).

3. **Tenant ID** *(required)* - The ID of the Team being managed.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Parsec_Adapter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Parsec_Adapter.png" />

## APIs

Axonius uses the [Teams REST API Version 1.0](https://parsec.app/docs/teams-api).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| Parsec Tams v1 | Yes       | --    |

## Supported From Version

Supported from Axonius version 5.0.