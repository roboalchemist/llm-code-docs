# Source: https://docs.axonius.com/docs/mimecast-v2.md

# Mimecast - V2

Mimecast provides a mail management system designed to protect email, ensure access and simplify the tasks of managing email.

<Callout icon="📘" theme="info">
  Note

  This adapter supports Mimecast API 2.0. If you are using Mimecast API 1.0 use the [Mimecast - V1](/docs/mimecast) adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Mimecast server. Select the Base URL that corresponds to your region. The default hostname should be: `https://api.services.mimecast.com`

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Internal Domain** *(required)* - The name of the domain the client wants to get the internal users from.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Mimecast%20-%20V2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mimecast%20-%20V2.png" />

## APIs

Axonius uses [Mimecast API 2.0](https://developer.services.mimecast.com/apis).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 80, 443 or the port configured.

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions in order to fetch assets:

* Must be a Mimecast administrator with at least the Directories | Internal | Read permission in order to fetch Internal Users.

### Related Enforcement Actions

* [Add MimecastV2 Group Members ](/docs/add-mimecast-v2-group-members)

## Supported From Version

Supported from Axonius version 6.1