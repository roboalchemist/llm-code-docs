# Source: https://docs.axonius.com/docs/com-laude.md

# Com Laude

Com Laude is a domain name registrar, providing domain name management services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Com Laude server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Com%20Laude(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Com%20Laude\(1\).png)

## APIs

Axonius uses the [Com Laude API](https://api.comlaude.com/docs).

* [Login API](https://api.comlaude.com/docs#/Auth/apiLogin)
* [Domains API](https://api.comlaude.com/docs#/Domains/getDomainsIndex)
* [Resource Records API](https://api.comlaude.com/docs#/Resource%20Records/getDomainZoneRecords)
* [Users API](https://api.comlaude.com/docs#/Users/getUsersIndex)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.
The value supplied in [API Key](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0