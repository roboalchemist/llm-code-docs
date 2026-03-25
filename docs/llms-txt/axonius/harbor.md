# Source: https://docs.axonius.com/docs/harbor.md

# Harbor

Harbor is an open-source container image registry that provides vulnerability scanning and role-based access control.

### Asset Types Fetched

* Vulnerabilities, SaaS Applications, Compute Images

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Harbor API](https://github.com/container-registry/harbor-api-client/blob/master/harbor_swagger_openapi3.yaml).

### Permissions

The User Name/Password must be granted the appropriate permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Harbor server.
2. **User Name** and **Password**  - The credentials for a user account that has the permissions to fetch assets.

![Harbor.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Harbor.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).