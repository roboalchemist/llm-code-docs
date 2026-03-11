# Source: https://docs.axonius.com/docs/bitwarden.md

# Bitwarden

Bitwarden is an open-source password manager.

## Types of Assets Fetched

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://identity.bitwarden.com/`)* - The hostname or IP address of the Bitwarden server.
2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For more information, see [Authentication](https://bitwarden.com/help/public-api/#authentication).

<Callout icon="📘" theme="info">
  Note

  * This adapter requires the 'organization' API credentials (Organization API key for **Client ID**; Secret for **Client Secret**).

  * The adapter also requires the API key to have a prefix of `organization.`.
</Callout>

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Bitwarden](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bitwarden.png)

## APIs

Axonius uses the [Bitwarden Public API](https://bitwarden.com/help/public-api/).

## Supported From Version

Supported from Axonius version 6.0