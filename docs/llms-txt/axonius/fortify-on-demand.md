# Source: https://docs.axonius.com/docs/fortify-on-demand.md

# Fortify On Demand

Fortify On Demand delivers application security as a service, providing security testing and vulnerability management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Fortify On Demand server.

2. **API Key** and **Client Secret** - The API Key and Client Secret associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Fortify On Demand](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortify%20On%20Demand.png)

## APIs

Axonius uses the [Fortify on Demand Web API](https://api.ams.fortify.com/swagger/ui/index).

## Required Permissions

The following scopes are required:

* api-tenant, view-users - to fetch users
* api-tenant, view-apps - to fetch applications
* api-tenant, view-apps - to fetch releases
* api-tenant, view-issues - to fetch vulnerabilities

## Supported From Version

Supported from Axonius version 6.1