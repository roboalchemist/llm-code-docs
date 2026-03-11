# Source: https://docs.axonius.com/docs/unimus.md

# Unimus

Unimus is a network configuration and automation tool which provides information on devices, backups, and configurations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Unimus server.

2. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to [Generate Unimus API Token](https://wiki.unimus.net/display/UNPUB/Full+API+v.2+documentation#FullAPIv.2documentation-Security)

3. **API Version** *(required)* - Select the API version, the default is V2

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Unimus" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Unimus.png" />

## APIs

Axonius uses the:

* [Unimus REST API](https://wiki.unimus.net/display/UNPUB/API+documentation).
* [Unimus Get Devices](https://wiki.unimus.net/display/UNPUB/Full+API+v.2+documentation#FullAPIv.2documentation-Devices-getdevices)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Unimus 1.9.0 or newer | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7