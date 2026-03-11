# Source: https://docs.axonius.com/docs/canva.md

# Canva

Canva is a graphic design platform that offers tools for creating visual content.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Authentication Token

### APIs

Axonius uses the [Canva SCIM API](https://www.canva.dev/docs/scim/).

### Permissions

**Role-Based Access Control (RBAC)**:
Access to the Canva SCIM API is restricted to organizations with a Canva Enterprise subscription for single teams. Additionally, only team administrators and owners of Canva for Teams or Canva for Education have access to generate the required SCIM access token. This token grants the necessary permission to perform all supported provisioning operations, including fetching Users.

#### Supported From Version

Supported from Axonius version 7.0.12

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Canva server.
2. **Authentication Token**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

![Canva.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Canva.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).