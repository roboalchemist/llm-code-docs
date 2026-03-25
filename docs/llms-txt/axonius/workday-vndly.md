# Source: https://docs.axonius.com/docs/workday-vndly.md

# Workday VNDLY

Workday VNDLY is a workforce management platform that provides contingent labor procurement, onboarding workflows, and vendor management functionality.

### Asset Types Fetched

* Users, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the Workday VNDLY Program Services API.

### Permissions

* **Authentication**
  The API uses token-based authentication. Each user must generate an API Token and include it in the Authorization header using the format:
  `Authorization: Token <your_api_token>`

* **User-Specific Access**
  API tokens are tied to individual users, and all access is audited per user identity. Each user’s access is limited to their assigned permissions.

* **Rate Limits**
  Request throttling is enforced per API token:
  * List GET: 1000 requests per minute
  * All GET: 5000 requests per minute
  * POST, PATCH, PUT: 1000 requests per minute

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Workday VNDLY server.
2. **API Token**  - An API Token associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Workday VNDLY.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Workday%20VNDLY.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).