# Source: https://docs.axonius.com/docs/oracle-fusion-cloud-applications.md

# Oracle Fusion Cloud Applications

Oracle Fusion Cloud Applications is a suite that provides integrated cloud services for enterprise resource planning.

### Asset Types Fetched

* Users
* Roles

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the following API endpoints:

* [Get all users](https://docs.oracle.com/en/cloud/saas/applications-common/25b/farca/op-hcmrestapi-scim-users-get.html)
* [Users REST Endpoints](https://docs.oracle.com/en/cloud/saas/applications-common/25b/farca/api-users.html)

### Permissions

**Authentication**

* Oracle supports Basic Auth (username + password) and Bearer token (OAuth2), depending on your tenant setup.

**Roles & Entitlement**

* Every user calling SCIM REST endpoints must have the `ASE_REST_SERVICE_ACCESS_IDENTITY_INTEGRATION_PRIV` privilege.

* Your user must be assigned the business task ‘Manage Users’ (or an equivalent custom role that includes the entitlement). For more information, see [Use Cases](https://docs.oracle.com/en/cloud/saas/applications-common/24c/farca/Use_Cases.html).

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Oracle Fusion Cloud Applications server.
2. **Client ID** and **Client Secret** - The credentials for an account that has the Required Permissions to fetch assets.
3. **Scope** - The scope name.

<Image alt="Oracle Fusion Cloud Applications.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Oracle%20Fusion%20Cloud%20Applications.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [Oracle Fusion Cloud Applications - Create User](https://docs.axonius.com/axonius-help-docs/docs/create-oracle-fusion-cloud-applications-user)
* [Oracle Fusion Cloud Applications - Update User](https://docs.axonius.com/axonius-help-docs/docs/update-oracle-fusion-cloud-applications-user)
* [Oracle Fusion Cloud Applications - Deactivate/Delete User](https://docs.axonius.com/axonius-help-docs/docs/delete-deactivate-oracle-fusion-cloud-applications-user)