# Source: https://docs.axonius.com/docs/intigriti.md

# Intigriti

Intigriti is a platform for security testing that assesses risk to prioritize remediation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.intigriti.com`)* - The hostname or IP address of the Intigriti server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For more information, see [Client Credentials](https://intigriti.readme.io/reference/client-credentials).

3. **Refresh Token** *(optional)* - Access token obtained from Intigriti associated with an admin user. For details on how to obtain the refresh token, see [Authentication](https://intigriti.readme.io/reference/authentication-1).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. **Rate Limit Settings**
   a.   **Request Count per Seconds** *(optional, default: 6000)* - Specify the request count per seconds.
   b. **Seconds per Request Count** *(optional, default: 60)* - Specify the seconds per request count.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Intigriti](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intigriti.png)

## APIs

Axonius uses the Intigriti API. For more information, see the following links:

* [Introduction](https://intigriti.readme.io/reference/introduction)
* [Intigriti API v2.0 Swagger UI](https://api.intigriti.com/external/company/swagger/index.html)

## Required Permissions

Users can access submissions according to their role in the vendor, as seen [here](https://intigriti.readme.io/reference/submissions_getoverview) and below:

| Role                                     | Can access                                   |
| ---------------------------------------- | -------------------------------------------- |
| Company admin                            | All submissions                              |
| Program reader / member / editor / admin | All submissions to which the group was added |
| Group reader / member / admin            | All submissions to which the group was added |

## Supported From Version

Supported from Axonius version 6.1