# Source: https://docs.axonius.com/docs/ivanti-patch-management.md

# Ivanti Patch Management

Ivanti Neurons for Patch Management continuously senses, discovers, and remediates security threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain** *(required, default: `https://neurons-for-patch-management.p.rapidapi.com`)* - The hostname or IP address of the Ivanti Patch Management server that Axonius can communicate with.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permissions to fetch assets. You can obtain these when the user registers an API in the [Ivanti Neurons Console](https://help.ivanti.com/ht/help/en_US/CLOUD/api/Patch-Mgmt/patch-authenication.htm).

3. **Tenant ID**  - The registered tenant ID

4. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IvantiPatchManagement](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IvantiPatchManagement.png)

## APIs

Axonius uses the [ivanti Patch Management API](https://help.ivanti.com/ht/help/en_US/CLOUD/api/patch-mgmt/patch-mgmt-overview.htm)

## Supported From Version

Supported from Axonius version 6.0