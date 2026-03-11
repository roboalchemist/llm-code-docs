# Source: https://docs.axonius.com/docs/secureworks-taegis-vdr.md

# Secureworks Taegis VDR

Secureworks Taegis VDR is a cloud-based vulnerability management solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://us2.vdr.secureworks.com`)* - The credentials for an account that has the [required permissions](/docs/secureworks-taegis-vdr#required-permissions) to fetch assets.

2. **Authorization Code** *(optional)* - The authorization code to connect to Secureworks Taegis VDR.

3. **Client Key** and **Client Secret** *(optional)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to create these credentials, see [XDR GraphQL APIs Authentication](https://docs.taegis.secureworks.com/apis/api_authenticate/).

4. **Verify SSL**  - Select to verify the SSL certificate offered by the server. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Secureworks Taegis VDR" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Secureworks%20Taegis%20VDR.png" />

## APIs

Axonius uses the [Secureworks Taegis VDR API v2](https://us2.vdr.secureworks.com/api/v2/spec).

## Required Permissions

The value supplied in [Host Name or IP Address](#parameters) must have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5