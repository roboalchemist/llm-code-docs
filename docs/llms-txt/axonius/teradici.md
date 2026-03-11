# Source: https://docs.axonius.com/docs/teradici.md

# HP Anyware

HP Anyware supports hybrid work environments allowing users to access their digital workspaces without a VPN.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HP Anyware server.

2. **User Name** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="HPAnyware" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPAnyware.png" />

## APIs

Axonius uses the [Anyware Manager V1](https://cas.teradici.com/api/docs) API.

You can use the following API calls:

* GET Users - `https://cam.teradici.com/api/v1/auth/users`

* GET a single user - `https://cam.teradici.com/api/v1/auth/users/\{id}`

* GET activity logs - `https://cam.teradici.com/api/v1/logs`

* Get anyware connector per id - `https://cam.teradici.com/api/v1/deployments/connectors/\{id}`

* Get anyware connector in general - `https://cam.teradici.com/api/v1/deployments/connectors`

## Supported From Version

Supported from Axonius version 6.0