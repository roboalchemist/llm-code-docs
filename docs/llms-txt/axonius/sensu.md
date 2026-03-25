# Source: https://docs.axonius.com/docs/sensu.md

# Sensu

Sensu is a cloud monitoring solution that provides monitoring workflows automation and visibility into multi-cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Sensu Domain** *(required)* - The hostname or IP address of the Sensu server.
2. **API Version** *(default Version 1)* - Select the API Version, either Version 1 or Version 2. When you choose Version 2 authentication with an API Key is required.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  **User Name** and **Password** are required when you choose 'API Version 1'.
</Callout>

5. **API Key** *(required)* - The APi Key. Refer to [Sensu Docs](https://docs.sensu.io/sensu-go/latest/api/#configure-an-environment-variable-for-api-key-authentication) for information on obtaining the API Key.
6. **Namespace** *(optional)* - The Namespace. Namespaces are used to partition resources within Sensu as described in [Namespaces reference](https://docs.sensu.io/sensu-go/latest/operations/control-access/namespaces/)

<Callout icon="📘" theme="info">
  Note

  **API Key** is required and **Namespace** is optional when you choose 'API Version 2'.
</Callout>

8. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

9. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sensu](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sensu.png)

## APIs

Axonius uses:
For Version 2:[Sensu backend REST API v2](https://docs.sensu.io/sensu-go/latest/api/core/entities/).
For Version 1:[Sensu API version 1](https://docs.sensu.io/sensu-core/latest/api/overview/)

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
For details about creating a read-only user, see [Sensu Docs - Create a read-only user with RBAC](https://docs.sensu.io/sensu-go/latest/guides/create-read-only-user/).