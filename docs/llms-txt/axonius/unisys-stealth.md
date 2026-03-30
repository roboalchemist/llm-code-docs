# Source: https://docs.axonius.com/docs/unisys-stealth.md

# Unisys Stealth

Unisys Stealth transforms existing networks—both on-premises and in the cloud—into a Zero Trust Network through identity-based microsegmentation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the  Unisys Stealth server.

2. **Port** *(required, default: 8448)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Stealth" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Stealth.png" />

## APIs

Axonius uses the [Unisys Stealth Ecosystem API v4.0.134.0](https://public.support.unisys.com/st3/docs/Stealth-4.0/82254186-002/index.html)

The API should be local with a default port of 8448. For example: `https://localhost:8448`

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7