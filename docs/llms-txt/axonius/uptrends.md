# Source: https://docs.axonius.com/docs/uptrends.md

# Uptrends

Uptrends is a cloud-based solution for monitoring websites, servers, APIs, and network performance. Integrate Uptrends with the Axonius Cybersecurity Asset Management Platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Uptrends server.

2. **User Name** and **Password** *(required)* - The credentials for an API account, that has the permissions to fetch assets. Refer to [Uptrends Operator API account management ](https://www.uptrends.com/support/kb/operators/operator-API-management) for information of how to create the API account.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Uptrends" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Uptrends.png" />

## APIs

Axonius uses the [Uptrends API version 4](https://www.uptrends.com/support/kb/api/v4).

## Required Permissions

The value supplied in [User Name](#parameters) must have an Uptrends **API** account (this is not the same as an Uptrends account)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| Uptrends API version 4 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8