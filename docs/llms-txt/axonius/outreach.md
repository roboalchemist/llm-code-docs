# Source: https://docs.axonius.com/docs/outreach.md

# Outreach

Outreach is a sales engagement platform that provides automation and analytics for sales teams.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Outreach server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permission to fetch assets. For information on authorization, see [Requesting access token](https://developers.outreach.io/api/oauth/#requesting-access-token).

3. **Refresh Token** *(required)* - The token used to obtain a new access token once the original expires.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Outreach.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Outreach.png)

## APIs

Axonius uses the [Outreach API](https://developers.outreach.io/api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.53