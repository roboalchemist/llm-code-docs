# Source: https://docs.axonius.com/docs/netdocuments.md

# NetDocuments

NetDocuments is a content management platform that provides document and email management, workflow automation, and search capabilities for legal environments.

### Asset Types Fetched

* Users, Groups

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID / Client Secret / Repository ID

### APIs

Axonius uses the [NetDocuments Rest API Version 2](https://vault.netvoyage.com/v2/swagger/ui/index#/).

### Permissions

The required scopes for the access token are `read` and `admin`.

**Authentication**:

* Uses OAuth 2.0 protocol.

* Each API call must include an access token in the header:
  `Authorization: Bearer `

* Access tokens expire after inactivity (45-90 minutes) or maximum lifetime (24-48 hours).

* Calls with expired tokens return HTTP 401 Unauthorized.

#### Supported From Version

Supported from Axonius version 7.0.9

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Region** *(default: US - [https://api.vault.netvoyage.com](https://api.vault.netvoyage.com))* - The hostname or IP address of the NetDocuments server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the  Required Permissions to fetch assets.
3. **Repository ID** - The ID of the repository that the adapter is allowed to access.

![NetDocuments.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetDocuments.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).