# Source: https://docs.axonius.com/docs/frontline-vm.md

# Frontline VM

Frontline VM, a Frontline.Cloud system, is a vulnerability management application that performs comprehensive security assessments and helps prioritize and track the results, making remediation more efficient and effective.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Frontline VM server.
2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
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
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1639\).png)

## APIs

Axonius uses the \[Frontline VM Quick Connect API]\([https://help.frontline.cloud/vm/en-us/Topics\_IN/QuickConnect](https://help.frontline.cloud/vm/en-us/Topics_IN/QuickConnect) API\_IN.htm).

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have permissions to fetch assets.

### To generate a Frontline Vulnerability Manager API Key:

1. Log in to Frontline VM .
2. In the site header, select your name and choose **My profile**.
3. On the **API Tokens** tab, select **Create new token**.
4. In the **Add New Token** dialog, type the token name (it can be whatever you like) and select **OK**.
   Your token is created.
5. Below your token name, selecting **Click to show key** displays your API Key.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1640\).png)