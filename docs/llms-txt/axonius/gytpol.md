# Source: https://docs.axonius.com/docs/gytpol.md

# Gytpol

GYTPOL is a security configuration management solution providing both visibility of devices and automation of the hardening process.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Gytpol server.

2. **Token** *(required)* - A  Token associated with a user account that has permissions to fetch assets. The token is received from the vendor.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Gytpol](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Gytpol.png)

## APIs

Axonius uses the GYTPOL API.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version   | Supported | Notes |
| --------- | --------- | ----- |
| Gyptol v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8