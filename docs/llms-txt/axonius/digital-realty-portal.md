# Source: https://docs.axonius.com/docs/digital-realty-portal.md

# Digital Realty

Digital Realty is a data center management platform that provides colocation, interconnection, and customized data solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Digital Realty server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information on how to obtain these credentials, see the [Access Token How to Guide](https://developer.digitalrealty.com/api-catalog/accesstoken/how-guide).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Digital Realty Portal](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Digital%20Realty%20Portal.png)

## APIs

Axonius uses the [Digital Realty Accounts API](https://developer.digitalrealty.com/api-catalog/accounts-v1#/Accounts/accounts).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.32.1