# Source: https://docs.axonius.com/docs/qualys-was.md

# Qualys WAS

Qualys WAS is a web application scanning tool for identifying vulnerabilities in web applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Vulnerabilities
* SaaS Applications
* Application Services
* Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Qualys WAS server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. For more information, see [Get Started>Qualys user account](https://cdn2.qualys.com/docs/qualys-was-api-user-guide.pdf).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Qualys WAS" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Qualys%20WAS.png" />

## APIs

Axonius uses the [Qualys Web Application Scanning API](https://cdn2.qualys.com/docs/qualys-was-api-user-guide.pdf).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The following permissions are required:

* Make sure the WAS module is enabled
* The user account needs to have these permissions: Access Permission “API Access”
* The data fetched only includes findings in the user’s scope

## Supported From Version

Supported from Axonius version 6.1

### Related Enforcement Actions

[Qualys WAS - Add or Remove Tags to Assets](https://docs.axonius.com/axonius-help-docs/docs/qualys-was-add-or-remove-tags-to-assets)