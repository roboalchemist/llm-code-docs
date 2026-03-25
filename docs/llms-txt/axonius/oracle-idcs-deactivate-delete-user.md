# Source: https://docs.axonius.com/docs/oracle-idcs-deactivate-delete-user.md

# Oracle IDCS - Deactivate/Delete User

**Oracle IDCS - Deactivate/Delete User** deactivates or deletes a user in Oracle IDCS for:

* Users returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

<Callout icon="📘" theme="info">
  **Note:**

  To use this enforcement action, you must successfully configure a [Oracle Identity Cloud Service (IDCS)](https://docs.axonius.com/axonius-help-docs/docs/oracle-idcs) adapter connection.
</Callout>

* **User ID** - The ID of the user to deactivate or delete.
* **Deactivate or Delete** - Select the action to perform.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Host Name or IP Address** - The hostname or IP address of the Oracle Fusion Cloud Applications server.

* **Client ID** and **Client Secret** - The credentials for an account that has the Required Permissions to fetch assets.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the following APIs:

* [REST API for Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsa/toc.htm)
* [IDCS APIs (OCI Identity Domains)](https://www.postman.com/oracledevs/oracle-identity-cloud-service-idcs-rest-apis/request/u2slgk5/list-all-users)

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* **Authentication** - Requires OAuth 2.0 Client Credentials Grant with a confidential application.
* **App Type** - You must create a confidential client application in Oracle IDCS. It must be enabled for Client Credentials grant type.
* **Roles Required** - The client application must be assigned administrative roles that allow reading users, such as:
  * `Identity Domain Administrator`
  * `User Administrator`
  * or custom roles with `GET` permission for the relevant APIs.
* **RBAC Applies** - If the associated user or client app lacks the proper role, the response will be limited or denied (403).
* **API Endpoint Version** - Use `/admin/v1/Users`, not `/v1/Users`, to access admin-level attributes and filtering.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).