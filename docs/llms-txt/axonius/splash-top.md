# Source: https://docs.axonius.com/docs/splash-top.md

# Splashtop

Splashtop is a remote access and remote support tool.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Splashtop server.
2. **Client ID** and **Client Secret** *(optional)* - Credentials associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **Client ID** and **Client Secret** are required.
</Callout>

3. **MFA Code** *(optional)* - The code provided in the query params of the OAuth2 redirection.
4. **Redirect URI** *(optional)* - The URL that is registered in the product as the URI that should be using the token.
5. **API Key** *(optional)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is supplied, no other authentication fields are necessary.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Splashtop(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Splashtop\(1\).png)

## APIs

Axonius uses the [Splashtop Open APIs](https://support-splashtopbusiness.splashtop.com/hc/en-us/articles/16772899906459-Spashtop-Open-APIs__;!/)

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with the following scopes   in order to fetch assets:

* users

* team\_computers

* inventory

* logs

## Supported From Version

Supported from Axonius version 6.0