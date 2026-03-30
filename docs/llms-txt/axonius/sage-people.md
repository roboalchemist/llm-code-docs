# Source: https://docs.axonius.com/docs/sage-people.md

# Sage People

Sage People is a people management platform that provides employee record management, payroll processing and management, talent management, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Sage People server.
2. **Token** *(required)* - A  Token associated with a user account that has permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

* If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
* If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details about the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![SagePeopleUP.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SagePeopleUP.png)

## APIs

Axonius uses the [Sage People API (4.7)](https://developer.sage.com/api/people/api-reference/#operation/employees).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions.  Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Sage People API (4.7) | Yes       |       |

## Supported From Version

Supported from Axonius version 4.4