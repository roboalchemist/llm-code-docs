# Source: https://docs.axonius.com/docs/bluewater-control.md

# Bluewater Control

Bluewater is a network management tool that monitors and optimizes network performance.

### Asset Types Fetched

* Devices, Users, Networks

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Bluewater Connect API.

### Permissions

To access the API, authentication is required using one of the following methods:

* **OAuth 2.0 (Bearer Token)** – Obtain a token via `POST /oauth/token`, then include it in the Authorization header as:
  `Authorization: Bearer {token}`

* **Basic Authentication with API Key** – Use Basic Auth with the username `ApiKey` and the password as your API key. The header should look like:
  `Authorization: Basic {base64(ApiKey:your_api_key)}`

All endpoints are protected under the `Authorization: all` security scheme, meaning valid authorization is mandatory for all operations. The token or API key used must have permissions associated with the `all` scope.

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Bluewater Control server.
2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.

![Bluewater Control.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bluewater%20Control.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).