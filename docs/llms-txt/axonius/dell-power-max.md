# Source: https://docs.axonius.com/docs/dell-power-max.md

# Dell PowerMax

Dell PowerMax is an NVMe-based (Non-Volatile Memory Express), mission-critical data storage offering.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Dell PowerMax server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. For more information, see [Setting up user authentication](https://developer.dell.com/apis/4458/versions/9.2/docs/Tasks/setting_up_user_authentication.md).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dell%20PowerMax](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dell%20PowerMax.png)

## APIs

Axonius uses the following PowerMax APIs:

* [List Arrays](https://developer.dell.com/apis/4458/versions/9.2/openapi.json/paths/~192~1sloprovisioning~1symmetrix/get)
* [Get Array](https://developer.dell.com/apis/4458/versions/9.2/openapi.json/paths/~192~1sloprovisioning~1symmetrix~1%7BsymmetrixId%7D/get)
* [List Hosts](https://developer.dell.com/apis/4458/versions/9.2/openapi.json/paths/~192~1sloprovisioning~1symmetrix~1%7BsymmetrixId%7D~1host/get)
* [Get Host](https://developer.dell.com/apis/4458/versions/9.2/openapi.json/paths/~192~1sloprovisioning~1symmetrix~1%7BsymmetrixId%7D~1host~1%7BhostId%7D/get)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| Dell PowerMax V9.2 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0