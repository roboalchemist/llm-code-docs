# Source: https://docs.axonius.com/docs/moogsoft.md

# Moogsoft

Moogsoft is an AI-driven observability platform for monitoring solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Moogsoft server.

2. **User Name** *(required)* - The user name for an account that has read access to the API.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to create an API Key, see [Manage API keys](https://api.docs.moogsoft.com/docs/latest/branches/main/6553f9391961d-manage-api-keys).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Moogsoft" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Moogsoft.png" />

## APIs

Axonius uses the following API endpoints:

* For users: [https://api.docs.moogsoft.com/docs/latest/branches/main/0ae8aab105288-get-all-users-in-the-system](https://api.docs.moogsoft.com/docs/latest/branches/main/0ae8aab105288-get-all-users-in-the-system)
* For devices: [https://api.docs.moogsoft.com/docs/latest/aaacfa68d228d-get-all-known-collectors](https://api.docs.moogsoft.com/docs/latest/aaacfa68d228d-get-all-known-collectors)

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0