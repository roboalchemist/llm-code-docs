# Source: https://docs.axonius.com/docs/micro-focus-groupwise.md

# Micro Focus GroupWise

Micro Focus GroupWise is a collaboration software solution that provides email, calendaring, and instant messaging.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Micro Focus GroupWise server that Axonius can communicate with.
2. **Port** *(required, default: 9710)* - The port to be used in the connection.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![MicrofocusGRoupWise.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicrofocusGRoupWise.png)

## APIs

Axonius uses the [GroupWise API](https://www.novell.com/documentation/groupwise2014r2/gwsdk_admin_rest_api/data/b12ypr4w.html).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                              | Supported | Notes |
| ------------------------------------ | --------- | ----- |
| GROUPWISE 2014 R2                    | Yes       |       |
| Micro Focus GroupWise version 18.2.1 | Yes       |       |