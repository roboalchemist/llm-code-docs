# Source: https://docs.axonius.com/docs/google-tag-manager.md

# Google Tag Manager

Google Tag Manager is a tag management system for web pages that allows marketers and developers to manage and deploy marketing tags and other code snippets on their websites.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Google Tag Manager server.

2. **Client ID** and **Private Key** *(required)* - The Client ID and Private Key used to connect to Google Tag Manager. For more information, see the [Google API Console](https://console.developers.google.com/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Google Tag Manager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Google%20Tag%20Manager.png" />

## APIs

Axonius uses the [Google Tag Manager API](https://developers.google.com/tag-platform/tag-manager/api/v2).

## Supported From Version

Supported from Axonius version 6.1