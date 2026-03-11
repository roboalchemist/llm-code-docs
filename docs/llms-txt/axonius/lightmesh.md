# Source: https://docs.axonius.com/docs/lightmesh.md

# LightMesh

LightMesh is a network management tool that offers comprehensive visibility and control over network infrastructure.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Lightmesh GraphQL API](https://api-documentation.lightmesh.com/).

### Permissions

To access the necessary data via the API, ensure that the API key used has sufficient permissions. This typically involves assigning appropriate roles to the API key within the LightMesh platform. If certain queries return permission errors, verify the roles and permissions associated with the API key.

#### Supported From Version

Supported from Axonius version 6.1.73

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the LightMesh server.
2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

![LightMesh.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LightMesh.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).