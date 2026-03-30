# Source: https://docs.axonius.com/docs/securithings.md

# SecuriThings

SecuriThings is a platform that enables organizations to proactively manage, automate, and secure their entire physical security infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SecuriThings server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Organization** *(required)* - The organization name defined in the customer’s account.

3. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permission to fetch assets. For information on how to obtain these credentials, see [Authentication](https://developer.securithings.com/guides/authentication).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SecuriThings.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecuriThings.png)

## APIs

Axonius uses the following APIs:

* [https://developer.securithings.com/introduction](https://developer.securithings.com/introduction)
* [https://developer.securithings.com/api](https://developer.securithings.com/api)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.59.0