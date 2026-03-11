# Source: https://docs.axonius.com/docs/xcp-ng.md

# XCP-ng

XCP-ng is an open-source virtualization platform that offers enterprise-grade features for managing virtual machines.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Token

### APIs

Axonius uses the [Xen Orchestra API](https://docs.xcp-ng.org/management/manage-at-scale/xo-api/).

### Permissions

To retrieve task and activity data from the Xen Orchestra API, the API token must be associated with an account that has sufficient rights to:

* Access the Xen Orchestra REST API
* View infrastructure-wide task execution and VM operations
* Retrieve task history and real-time task updates using `watch`, `ndjson`, or `wait` parameters

If the account does not have the appropriate role-based access (RBAC), the REST API requests to activity or task endpoints will return permission errors (`401 Unauthorized` or `403 Forbidden`), or no data.

**Recommended Steps**:

* Ensure the account generating the API token has Admin-level access in Xen Orchestra.

* Verify the API token is valid and included in the `Cookie` header as `authenticationToken=<your_token>`.

* Confirm that activity-related endpoints such as `/rest/v0/tasks`, `/rest/v0/tasks/{uuid}`, and related query parameters (`watch`, `ndjson`, `wait`) are accessible by the authenticated account.

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the XCP-ng server.
2. **Token**  - An API Token associated with a user account that has the Required Permissions to fetch assets.

<Image alt="XCP-ng.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/XCP-ng.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).