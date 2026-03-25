# Source: https://docs.axonius.com/docs/akeyless.md

# Akeyless

Akeyless is a SaaS-based solution that provides secrets management and zero-trust access.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Roles

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Akeyless server.

2. **Port** *(optional)* - The port used for the connection.

3. **Access ID** *(required)* - An ID for Akeyless.

4. **Access Key** *(required)* - The key used to unseal the vault.

<Callout icon="📘" theme="info">
  Note

  Refer to [Akeyless API Key](https://docs.akeyless.io/docs/api-key) for details on how to generate the Access ID and Key.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
![Akeyless](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Akeyless.png)

## APIs

Axonius uses the [Akeyless API](https://docs.akeyless.io/reference/assocroleauthmethod).

## Required Permissions

The value supplied in [Access ID](#parameters) must be associated with credentials that have Read and List permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0