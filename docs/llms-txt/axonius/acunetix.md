# Source: https://docs.axonius.com/docs/acunetix.md

# Acunetix 360

Acunetix is an automated web application security testing tool that checks for vulnerabilities like SQL Injection, Cross-site scripting, and other exploitable vulnerabilities.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg) Aggregated Security Findings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Acunetix API server that Axonius can communicate with via the [Required Ports](#required-ports).
   * For  the online version of Acunetix, use `https://online.acunetix360.com/`
   * For the on-premises version, use the link for the API on the server

2. **Acunetix User ID** - The credentials for a user account that has the permissions to fetch assets.
   To generate the User ID, see [API Settings](https://online.acunetix360.com/account/ApiSettings/).

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate the API Key, see [API Settings](https://online.acunetix360.com/account/ApiSettings/).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Acunetix" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Acunetix.png" />

## APIs

Axonius uses the [Acunetix 360 API v1](https://online.acunetix360.com/docs/index).

## Required Ports

The following is applicable only if using the on-premises Acunetrix 360 API:

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the port of the Acunetrix API server.

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to read-only list of users, list of websites, list of scans, and reports for scans.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| v2.2.0.0 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7