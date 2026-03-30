# Source: https://docs.axonius.com/docs/sharepoint-create-list-item.md

# SharePoint - Create Item In List

**SharePoint - Create Item In List** creates a list item on a SharePoint site sends it to a specific path on SharePoint for:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action requires an adapter connection using the [SharePoint](/docs/sharepoint) adapter.
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

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from SharePoint adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [SharePoint](/docs/en/sharepoint) adapter connection.
  </Callout>

* **Site ID** - Enter the SharePoint Site ID

* **List ID** - Enter the ID of the list in which to create items.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: graph.microsoft.com)* - The host name or IP address of a SharePoint server.

  * **Tenant ID** - Enter the tenant ID.

  * **Client ID** - Enter the client ID.

  * **Client Secret** - Enter the client secret.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Microsoft Login Environment** - Select the API environment go login to. The options are either Microsoft Public Login or Microsoft Gov Login.
</Callout>

## APIs

Axonius uses the [SharePoint REST operations via the Microsoft Graph REST API](https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph)
Refer to [Get access without a user](https://learn.microsoft.com/en-us/graph/auth-v2-service?view=graph-rest-1.0) for details on obtaining credentials.

To fetch users Axonius uses the [SharePoint List Users endpoint.](https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0\&tabs=http#optional-query-parameters)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* TCP port 80/443

## Required Permissions

The credentials used to run this Enforcement Action require the following SharePoint permission:

* `Sites.FullControl.All`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).