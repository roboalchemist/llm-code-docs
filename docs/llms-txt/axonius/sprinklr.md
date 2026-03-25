# Source: https://docs.axonius.com/docs/sprinklr.md

# Sprinklr

Sprinklr is a customer experience management platform that offers social media monitoring, engagement, and marketing solutions for enterprises.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Activities

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Sprinklr server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Environment** *(required)* - The Sprinklr environment, such as Prod0, prod2, etc.

4. **Refresh Token** *(required)* - The token used for the connection.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sprinklr](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sprinklr.png)

## APIs

Axonius uses the following APIs:

* [Search Users](https://developer.sprinklr.com/docs/read/api_20/scim_20/Search_User)
* [Audit API](https://developer.sprinklr.com/docs/read/api_20/audit_api/Audit_API)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.41.0