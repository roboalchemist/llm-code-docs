# Source: https://docs.axonius.com/docs/metasys.md

# Metasys

Metasys is a building management system that provides integrated control and monitoring of facility operations.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Metasys REST API](https://jci-metasys.github.io/api-landing/api/v6-14-1).

### Permissions

To retrieve equipment data using the `/equipment` endpoint, the API token must be associated with a Metasys account that has sufficient rights to:

* Access the Metasys API (authenticated via `/login`).
* View equipment objects within the system's object tree.

If the account lacks the appropriate role-based access control (RBAC) permissions, the `/equipment` request will return partial results or omit equipment objects entirely.

**Recommended Steps**:

* Ensure the account generating the API token has a role (e.g., Administrator or equivalent) with object access rights to the relevant equipment.

* Verify the equipment objects are part of the site's object space as seen by the configured Site Director.

#### Supported From Version

Supported from Axonius version 6.1.73

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Metasys server.
2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets. For information on authentication, see [Request access token](https://jci-metasys.github.io/api-landing/api/v6-14-1#tag/authentication/operation/createToken).

![Metasys.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Metasys.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).