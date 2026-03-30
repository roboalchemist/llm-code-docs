# Source: https://docs.axonius.com/docs/bmc-atrium-onprem.md

# BMC Atrium CMDB onPrem

BMC Atrium CMDB stores information about the configuration items (CIs) in your IT environment and the relationships between them.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BMC Atrium CMDB server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![BMC\_Atrium\_CMDB\_onPrem](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BMC_Atrium_CMDB_onPrem.png)

## APIs

Axonius uses the [BMC Atrium Core 9.0 API](https://docs.bmc.com/docs/ac9000/rest-api-502997627.html).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| BMC Atrium CMDB 9.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5