# Source: https://docs.axonius.com/docs/anecdotes.md

# Anecdotes

Anecdotes is a compliance management platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Anecdotes server.

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. To generate an API Token, go to **Your account** at the bottom of the Anecdotes left navigation bar `>` **Administration** `>` **API Tokens** `>` **Create new token**.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Anecdotes](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Anecdotes.png)

## APIs

Axonius uses the [Anecdotes Identity API](https://anecdotes-ai.readme.io/reference/libresttokenvalidate).

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have Administrator permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1