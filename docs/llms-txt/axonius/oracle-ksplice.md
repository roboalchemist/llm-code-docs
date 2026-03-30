# Source: https://docs.axonius.com/docs/oracle-ksplice.md

# Oracle Ksplice

Oracle Ksplice provides fast secure kernel and userspace patching without the need for reboots.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Oracle Ksplice server.

2. **User Name**   *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Generate the API Key using the Oracle Ksplice console

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![OracleKsplice](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OracleKsplice.png)

## APIs

Axonius uses the [Oracle Ksplice Uptrack API](https://ksplice.oracle.com/uptrack/api)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 80, 443

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permission for the List Machines endpoint permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version          | Supported | Notes |
| ---------------- | --------- | ----- |
| Oracle Kspice v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7