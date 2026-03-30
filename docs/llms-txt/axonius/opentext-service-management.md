# Source: https://docs.axonius.com/docs/opentext-service-management.md

# OpenText Service Management (SMAX)

OpenText Service Management (SMAX) is a solution that provides AI‑powered automation for IT service management, asset lifecycle tracking, and enterprise service workflows.

### Asset Types Fetched

* Tickets

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [OpenText Case Exchange REST API](https://docs.microfocus.com/doc/205/saas/caseexchangeapi).

**Authentication**:

Access to the Case Exchange API requires authentication via:
`/auth/authentication-endpoint/authenticate/token`

**Authorization**:

Access to the Case Exchange API is restricted to the Authorized Users of the configured External Systems.

* Unauthorized users are rejected.
* For GET calls: The authenticated user must match the Authorized User for the system URL parameter.
* For POST calls: The authenticated user must match the Authorized User defined in the `ExternalSystem` under `ext_properties`.
* Integration users cannot access the EMS API directly and must use the Case Exchange API.

### Permissions

**Configuration**:

Each External System record must be configured with an Authorized User. Only tenant administrators can create or update External System records, including the Authorized User.

**Best practices**:

* Use special integration users for external integrations, not regular users.
* Use a different integration user per external integration.
* Grant integration users only the minimum necessary permissions.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the OpenText Service Management (SMAX) server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="OpenText Service Management (SMAX).png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OpenText%20Service%20Management%20(SMAX).png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [SMAX - Create Ticket](https://docs.axonius.com/axonius-help-docs/docs/create-opentext-service-management-ticket)
* [SMAX - Update Ticket](https://docs.axonius.com/axonius-help-docs/docs/update-opentext-service-management-ticket)