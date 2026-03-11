# Source: https://docs.axonius.com/docs/activate-servicenow-user.md

# ServiceNow - Activate User

**ServiceNow - Activate User** activates a ServiceNow user account for:

* User assets that match the results of the selected saved query, and match the Enforcement Action Dynamic Value statement, if defined, or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from ServiceNow adapter** - Select this option to use [Workspace](/docs/servicenow) adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **First Name** - The user's first name.
* **Last Name** - The user's last name.
* **Email** - The users email address.
* **Username** - The username by which the user will be known in ServiceNow.
* **First-login password generation method** - The method used to generate the first login password for the user to gain access. When **Manual password** is selected, enter a password in the **Password** field. This password will be used by all new users created by this Enforcement Action until they change it.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - The hostname or IP address of the ServiceNow server. This field format is 'https\://\[instance].service-now\.com'.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to add users.

  * **Client ID** and **Client Secret** - The OAuth Client ID and Client Secret for OAuth access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Fetch devices updated in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only devices that have been updated in ServiceNow in the last specified number of hours.

  * **Fetch users updated in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only users that have been updated in ServiceNow in the last specified number of hours.

  * **Fetch users created in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only users that have been created in ServiceNow in the last specified number of hours.

  * **Advanced configuration file** -  Upload an advanced configuration JSON file.

  * **Enable Client Side Certificate** - Select to enable Axonius to send requests using the  certificates uploaded to allow Mutual TLS configuration for this adapter. When you select this option, 2 more fields are displayed:

  * **Client Certificate File (.pem)** - Adds a client side certificate to the connection.

  * Click **Choose file** next  to **Client Certificate File** to upload a public key file in PEM format

  * **Client Private Key File (.pem)** - Adds a private key to the connection (if the API/proxy requires identification).

  * Click **Choose file** next  to **Client Private Key File** to upload a client private key file in PEM format

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Permissions

The credentials used to connect to ServiceNow must have permission to create new users.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).