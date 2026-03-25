# Source: https://docs.axonius.com/docs/f-secure-psb.md

# F-Secure Protection Service for Business (PSB)

F-Secure Protection Service for Business (PSB) is a central management portal for managing VPN, mobile device management, software update management, workstation, and server security.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - Use the URLs that matches your PSB server URL:

| PSB URL                                                            | API URL                                                  |
| ------------------------------------------------------------------ | -------------------------------------------------------- |
| [https://emea.psb.f-secure.com/](https://emea.psb.f-secure.com/)   | [https://eu1.psb.fsapi.com/](https://eu1.psb.fsapi.com/) |
| [https://amer.psb.f-secure.com/](https://amer.psb.f-secure.com/)   | [https://us2.psb.fsapi.com/](https://us2.psb.fsapi.com/) |
| [https://apac.psb.f-secure.com/](https://apac.psb.f-secure.com/)   | [https://jp3.psb.fsapi.com/](https://jp3.psb.fsapi.com/) |
| [https://emea2.psb.f-secure.com/](https://emea2.psb.f-secure.com/) | [https://eu4.psb.fsapi.com/](https://eu4.psb.fsapi.com/) |

2. **Company ID** *(required)* - The company ID to fetch data from.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
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
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1636\).png)

## APIs

Axonius uses the [PSB Management API](https://help.f-secure.com/product.html#business/psb-rest-api/1.0.0/en).

## Required Permissions

The value supplied in [User Name](#parameters) must be an administrator that has permissions to fetch assets.

* PSB uses a role-based authorization strategy, where full access to the Management API requires the "securityAndSubscriptionManagementRights" role.
* Administrators should get access to companies to which they are assigned.

For more details, see [PSB Management API - Authorization](https://help.f-secure.com/product.html#business/psb-rest-api/1.0.0/en/concept_F01C8E2DC6054DD3B71D699F8343473D-1.0.0-en).