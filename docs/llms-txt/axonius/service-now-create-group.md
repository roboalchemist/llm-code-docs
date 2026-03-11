# Source: https://docs.axonius.com/docs/service-now-create-group.md

# ServiceNow - Create Group

**ServiceNow - Create Group** creates a group in ServiceNow when triggered by a query.

<Callout icon="📘" theme="info">
  Note

  While a query is a mandatory field for triggering any Enforcement Action, in this particular Enforcement Set, the query parameters are not relevant as the Enforcement Set does not actually run on the query results. We recommend defining the query as **Devices** `>` **All Devices**.
</Callout>

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

* **Enforcement Set name (required)** - The name of the Enforcement Set. A default value is added by Axonius. You can change the name according to your needs.
* **Add description** - Click to add a description of the Enforcement Set. It is recommended to describe what the Enforcement Set does.
* **Run action on assets matching following query (required)** - Set to **Devices** `>` **All Devices** *(recommended)*. See the note at the beginning of this article.
* **Action name (required)** - The name of the Main action. A default value is added by Axonius. You can change the name according to your needs.
* **Configure Dynamic Values** - Toggle on to enter a Dynamic Value statement. See Creating Enforcement Action Dynamic Value Statements to learn more about Dynamic Value statement syntax.
* **Use stored credentials from Recorded Future adapter** - Select this option to use (the first) Recorded Future connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Name** - The name of the new group.
* **Description** - A description of the new group.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Draft** - When this option is enabled, the group is created **only** within Axonius and is **not** sent to ServiceNow via the adapter.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - The hostname or IP address of the ServiceNow server. This field format is 'https\://\[instance].service-now\.com'.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to add users.

  * **Client ID** and **Client Secret** - The OAuth Client ID and Client Secret for OAuth access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance.

  * **Apigee URL** - The URL of the domain that the get request is sent to for acquiring Apigee token.

  * **Resource Apigee** - The resources you want the Apigee to access.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Fetch devices updated in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only devices that have been updated in ServiceNow in the last specified number of hours.

  * **Fetch users updated in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only users that have been updated in ServiceNow in the last specified number of hours.

  * **Fetch users created in ServiceNow in the last X hours (0: All)** *(default: 0)* - Enter an amount of hours to fetch only users that have been created in ServiceNow in the last specified number of hours.

  * **Advanced configuration file** -  Upload an advanced configuration JSON file.

  * **Enable Client Side Certificate** - Select to enable Axonius to send requests using the  certificates uploaded to allow Mutual TLS configuration for this adapter. If you select this option, the following options are also available:

  * **Client Private Key File (.pem)** - Adds a private key to the connection (if the API/proxy requires identification). Click **Upload File** to upload a client private key file in PEM format.

  * **Client Certificate File (.pem)** - Adds a client side certificate to the connection. Click **Upload File** to upload a public key file in PEM format.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Permissions

The credentials used to connect to ServiceNow must have permission to create new groups.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).