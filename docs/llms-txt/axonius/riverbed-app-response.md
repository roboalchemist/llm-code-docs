# Source: https://docs.axonius.com/docs/riverbed-app-response.md

# Riverbed AppResponse

Riverbed AppResponse is a network performance monitoring tool that offers deep packet inspection and analysis.

### Asset Types Fetched

* Devices
* Certificates

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Riverbed AppResponse REST APIs](https://support.riverbed.com/apis/_products/AppResponse/index.html).

### Permissions

To retrieve SSL-related activity data and session-level vulnerability details, the API user account must have sufficient privileges on the AppResponse appliance to:

* Access the SSL Module, SSL DH Keys, and SSL Key Store features.
* View traffic analysis and encryption session metadata.
* Retrieve Diffie-Hellman key exchange details and SSL certificate records.
* Query per-session cipher suite usage and protocol version information.

If the user account lacks appropriate permissions (due to role-based access control restrictions or insufficient licensing), API calls will return incomplete results, permission errors, or HTTP 403 resp.

**Recommended Steps**:

1. Ensure the user account used for API authentication has read-level or admin access to the following AppResponse modules:
   * NPM SSL Module
   * NPM SSL Diffie Hellman Keys
   * NPM SSL Key Store

2. Verify that the account has permission to:
   * Execute the following endpoints:
     * `/api/npm.ssl_module/1.0/ssl-servers`
     * `/api/npm.ssl_dh_keys/1.1/dh-keys`
     * `/api/npm.ssl_key_store/1.0/ssl-certificates`
   * View or download session-level metadata.

3. For best results, use a local AppResponse administrator account, or ensure proper RBAC mapping if using external auth like RADIUS or TACACS+.

#### Supported From Version

Supported from Axonius version 6.1.70

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Riverbed AppResponse server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets. For more information, see [Authentication](https://support.riverbed.com/apis/_products/AppResponse/authentication.html).

<Image alt="Riverbed AppResponse.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Riverbed%20AppResponse.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).