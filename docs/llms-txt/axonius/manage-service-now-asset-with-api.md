# Source: https://docs.axonius.com/docs/manage-service-now-asset-with-api.md

# ServiceNow - Manage Assets with Scripted REST API

**ServiceNow - Manage Assets with Scripted REST API** executes a custom REST API endpoint on assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from the [ServiceNow](/docs/servicenow) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note:

    To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
  </Callout>

* **API endpoint** *(default: api/now/table/cmdb\_ci\_computer)* - The endpoint to execute.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - The full URL for your ServiceNow instance.

  * **User Name** and **Password** - To connect to ServiceNow, you need to create a user with action privileges to create and manage assets.

  * **OAuth Client ID** and **OAuth Client Secret** - The credentials for OAuth-based access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **OAuth Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance. This token is used to obtain new access tokens without requiring the user to reauthenticate.

  * **OAuth Custom Endpoint Path** - Specify a custom endpoint path to be used instead of the default `oauth_token.do`.

  * **Enable sending OAuth requests as JSON** -  Enable sending the request in JSON format instead of the standard `www-form-urlencoded` format.

  * **Apigee URL** - The URL of the domain that the GET request is sent to for acquiring the Apigee token.

  * **Resource Apigee** - The specific resources that the Apigee token is configured to access.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Split by field values** - Select a field to split assets by in the Assets table. Each incident will be split into multiple rows where each row lists a single field value - for example, a row with an incident per Security Finding (vulnerability) per Device.

* **Additional fields** - Specify additional fields to be added as part of the ServiceNow asset as key/value pairs in JSON format. For example:

  ```json
  {"field1": "value1", "field2": "value2"}
  ```

  You can also use functions within the field value either by themselves or embedded within larger text strings. In this example, the `{{CURRENT_DATE}}` function is embedded into the field value for the field **Date of Update**:

  ![AdditionalFieldsFunctionsCurrentDate.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdditionalFieldsFunctionsCurrentDate.png)

  * Use the `{{CURRENT_DATE}}` function to add the current date:

    * Using `{{CURRENT_DATE}}` with no format codes is the same as using the format codes: `%B %d, %Y`. This produces a date string like this: August 09, 2022.
    * Use format codes to specify a date format. For example, in the string *AX VM Update - `{{CURRENT_DATE:%m/%d/%Y}}`*, the *`%m/%d/%Y`* format codes will be replaced with 08/09/2022. The full string will be *AX VM Update - 08/09/2022*. The available format codes are described here: [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

* **Number of parallel requests** *(default: 10)* - The number of requests allowed at the same time.

* **Retry count** *(default: 1)* - If the action fails, Axonius will retry to execute it this many times for each device.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).