# Source: https://docs.axonius.com/docs/socket.md

# Socket

Socket is a developer-first platform that provides real-time monitoring and static analysis to prevent supply chain attacks in open source dependencies.

### Asset Types Fetched

* Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Socket API](https://docs.socket.dev/reference/introduction-to-socket-api).

### Permissions

Access to specific endpoints depends on token scopes:

* `full-scans:list` is required for full-scan endpoints.
* `repo:list` is required for repository-related endpoints.

#### Supported From Version

Supported from Axonius version 7.0.9

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Socket server.
2. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.
3. **Organization Slug** - The slug of the organization.

![Socket.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Socket.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).