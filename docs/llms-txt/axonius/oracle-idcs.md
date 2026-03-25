# Source: https://docs.axonius.com/docs/oracle-idcs.md

# Oracle Identity Cloud Service (IDCS)

Oracle IDCS is an identity and access management service that provides user provisioning, SSO, and authentication across hybrid IT environments.

### Asset Types Fetched

* Users
* Roles
* Groups
* Permissions

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the following APIs:

* [REST API for Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsa/toc.htm)
* [IDCS APIs (OCI Identity Domains)](https://www.postman.com/oracledevs/oracle-identity-cloud-service-idcs-rest-apis/request/u2slgk5/list-all-users)

### Permissions

The following permissions are required:

* **Authentication** - Requires OAuth 2.0 Client Credentials Grant with a confidential application.

* **App Type** - You must create a confidential client application in Oracle IDCS. It must be enabled for Client Credentials grant type.

* **Roles Required** - The client application must be assigned administrative roles that allow reading users, such as:
  * `Identity Domain Administrator`
  * `User Administrator`
  * or custom roles with `GET` permission for the relevant APIs.

* **RBAC Applies** - If the associated user or client app lacks the proper role, the response will be limited or denied (403).

* **API Endpoint Version** - Use `/admin/v1/Users`, not `/v1/Users`, to access admin-level attributes and filtering.

#### Supported From Version

Supported from Axonius version 7.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Oracle Identity Cloud Service (IDCS) server.
2. **Client ID** and **Client Secret** - The credentials for a user account that has the  Required Permissions to fetch assets. For more information, see [Working with OAuth 2 to Access the REST API](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsa/OATOAuthClientWebApp.html).

<Image alt="Oracle IDCS.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Oracle%20IDCS.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [Oracle IDCS - Create User](https://docs.axonius.com/axonius-help-docs/docs/oracle-idcs-create-user)
* [Oracle IDCS - Grant/Revoke AppRole to User](https://docs.axonius.com/axonius-help-docs/docs/oracle-idcs-grant-revoke-role)
* [Oracle IDCS - Deactivate/Delete User](https://docs.axonius.com/axonius-help-docs/docs/oracle-idcs-deactivate-delete-user)