# Source: https://docs.axonius.com/docs/hypr-passwordless.md

# HYPR Passwordless

HYPR Passwordless provides passwordless security solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HYPR Passwordless server.

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets.

3. **Application ID** **(optional)** - Enter an application ID to fetch devices.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HYPRUpdated](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HYPRUpdated.png)

## APIs

Axonius uses the [HYPR Passwordless APIs](https://apidocs.hypr.com/).
The API Token can be created according to the guidelines described at [HYPR Passwordless documentation site](https://docs.hypr.com/docs/auth/authInstallCfg/authInstallCfgAppMgmt/auth-install-cfg-app-mgmt-access-tokens/#create-an-access-token).