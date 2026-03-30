# Source: https://docs.axonius.com/docs/1e-tachyon.md

# 1E

1E is a remote endpoint management solution built on a single agent for speed, visibility, and control of all endpoints.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Methods**

Select an authentication method to connect the adapter based on your 1E environment:

| 1E Environment | Authentication Methods |
| :------------- | :--------------------- |
| Cloud          | User Name and Password |
| On-prem        | Access Token           |
| SaaS           | JWT Token              |

### APIs

Axonius uses the [Tachyon SDK](https://help.1e.com/TCN81/en/736741-739336-consumer-api-reference.html).

### Permissions

Consult with your vendor for permissions for reading the objects.

## Deploying the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the 1E server.
2. Select either of the following authentication methods based on your 1E environment (see [Authentication Methods](https://docs.axonius.com/docs/1e-tachyon#before-you-begin) for details):
   1. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.
   2. **Access Token** - An Access Token associated with a user account that has permissions to fetch assets.
   3. **JWT Token** - A Token associated with 1E's Non-Interactive Authentication flow. You can obtain a Token using a JWT you already have. To do so, make a POST request to either of the endpoints listed below. Your token needs to be wrapped in double quotes in the payload since the endpoint expects a string. If the JWT is valid, you receive a Token in return. See the [1E documentation](https://help.1e.com/SDK/en/exploring-the-api-using-the-web-browser.html) for more details.
      * `https://your.tachyon.server/Tachyon/api/Authentication/RequestJwtAuthentication`  (for versions 9.X and 23.X)
      * `https://your.platform.server/api/Authentication/RequestJwtAuthentication` (for versions 24.1 and newer)

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/1e_connect.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).