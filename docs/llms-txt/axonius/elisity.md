# Source: https://docs.axonius.com/docs/elisity.md

# Elisity

Elisity is a security platform that provides identity-based microsegmentation and zero trust access control for managing network access to critical assets.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the Elisity API v2.

### Permissions

* **Access Roles (RBAC)**: Elisity uses Role-Based Access Control (RBAC) to manage what each API client can do. Each client is assigned a role:
  * Tenant User – read-only access (can fetch data)
  * Tenant Admin – full access (can fetch and modify data)
  * Make sure your client is assigned the correct role for your use case.

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Elisity server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the  Required Permissions to fetch assets.

<Image alt="Elisity.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Elisity.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).