# Source: https://docs.axonius.com/docs/alemba-vfire.md

# Alemba Service Manager

Alemba is an ITIL-aligned IT Service Management (ITSM) platform focusing on request fulfillment.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Alemba server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Client ID** *(optional)* - A client ID associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Alemba Service Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Alemba%20Service%20Manager.png)

## APIs

Axonius uses the [Alemba API](https://www.alemba.help/help/content/topics/alemba%20api/aa%20programmers%20guide.htm) as well as the following APIs:

* Login - /alemba.web/oauth/login
* Configuration item - /preprod/alemba.api/api/v2/configuration-item

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.31.0