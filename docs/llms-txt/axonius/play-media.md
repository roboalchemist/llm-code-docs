# Source: https://docs.axonius.com/docs/play-media.md

# 3Play Media

3Play Media offers video accessibility services through transcription, captioning, and audio description.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the 3Play Media server.

2. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![3Play%20Media](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/3Play%20Media.png)

## APIs

Axonius uses the [3Play Media API](https://docs.3playmedia.dev/docs/introduction).

## Supported From Version

Supported from Axonius version 6.1