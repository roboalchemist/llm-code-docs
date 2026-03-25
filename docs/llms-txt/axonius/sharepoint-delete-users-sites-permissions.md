# Source: https://docs.axonius.com/docs/sharepoint-delete-users-sites-permissions.md

# SharePoint - Delete Users Sites Permissions

**Sharepoint - Delete users sites permissions** deletes all user permissions for:

* Assets (users) returned by the selected query or assets selected on the relevant asset page.

This Enforcement Set fetches all sites accessed by the user and deletes the user's permissions for them. This list of sites is available under the Sites field for each User asset. The list represents a historical site access and is not updated after permission removal.

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

* **Use stored credentials from Sharepoint adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [SharePoint](/docs/en/sharepoint) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** (default: graph.microsoft.com) - The host name or IP address of a SharePoint server.

  * **Tenant ID** - Enter the tenant ID.

  * **Client ID** - Enter the client ID.

  * **Client Secret** - Enter the client secret.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Microsoft Login Environment** - Select the API environment go login to. The options are either Microsoft Public Login or Microsoft Gov Login.

  The following fields are mandatory for running the Enforcement Set:

  * **Enable Certificate-Based Authentication** - Enable this so that Axonius can use certificate-based authentication on Microsoft required APIs. Certificate-Based Authentication by Microsoft uses a digital certificate to verify the identity of a user or application accessing APIs. Instead of passwords, the certificate’s public and private keys sign and validate requests. This method enhances security as certificates are harder to compromise than traditional passwords.

  * **Private Key File (.pem)** - Click **Upload File** to upload a client private key file in PEM format..

  * **Certificate File (.pem)** - Click **Upload File** to upload a public key file in PEM format.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [SharePoint API](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service?tabs=csom).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Sites.FullControl.All - To be able to call the API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).