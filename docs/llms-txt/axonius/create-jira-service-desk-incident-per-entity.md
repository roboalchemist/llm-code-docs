# Source: https://docs.axonius.com/docs/create-jira-service-desk-incident-per-entity.md

# Jira Service Management - Create Ticket per Asset

<Callout icon="💡" theme="warn">
  Notice

  This Enforcement Action replaces [Jira - Create Issue per Asset](/docs/create-jira-issue-per-entity), which was deprecated.
</Callout>

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Standard, Premium, or Enterprise license.
</Callout>

**Jira Service Management - Create Ticket per Asset** creates an incident in ServiceDesk for:

* **Each** asset returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

Details for all devices are included in the ticket message as well as the CSV.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Jira Service Desk adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Jira Service Management](/docs/atlassian-jira-service-desk) adapter connection.
</Callout>

* **Request description**  - Enter a description for the request. The maximum allowed length for this description is 30,000 characters. You can use field placeholders to create dynamic request descriptions that include field values from the assets being reported on. In the description text, wrap the field placeholder with double curly-braces: `{{ }}`. When the enforcement action runs, for each asset, the field values for that asset are populated into the ticket description. See the **Map Axonius fields to fields in the description** field below for more about how to use field mapping. For example, you can include a device hostname using this text in the description: `Hostname: {{hostname}}`.

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/enforcement_actions/JiraTicketPerAssetDescription.png" />
* **Request summary**  - Enter a summary for the created issue.

<Callout icon="📘" theme="info">
  Note

  You can replace text with parameters that can provide specific information to the Service Desk incident.
  The following parameters can be used:

  ```json
  {{HOSTNAME}}, {{USERNAME}}, {{FIRST_NAME}}
  ```
</Callout>

* **Issue type**  - Indicate the issue type.
* **Project Key**  - Specify the desired project in Service Desk where the issue will be created.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address**  - The hostname or IP address of the Jira Service Management server.

  * **Jira Service Management API version**  - Specify the Jira Service Management API version.

  * **User Name** and **API Token** - The credentials to connect to Jira Service Management. **User Name** is optional when not using the Cloud API, such as for an on-prem connection.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Use Cloud API** - Select this option to explicitly specify that the enforcement should use the Cloud API instead of Jira Server API. When the user uses the cloud API the default host name or IP address should be [https://api.atlassian.com](https://api.atlassian.com). Even when left unselected, the action will attempt to use the cloud API if the domain specified is “api.atlassian.com”.
</Callout>

* **Use full URL** - Select this option if the URL references to a specific endpoint. For example: `https://my-jira.com/jira`

* **Assignee** - Enter a user name or email address to which to assign the incident. It is recommended to use the user's email address.

* **Use assignee name instead of ID** - When **Assignee** has a value, Jira Service Management will search for the assignee by username or email address, depending on which is entered. When not selected, enter the user ID in the **Assignee** field.

* **Labels** - Comma-separated labels that will be added to the tickets.

* **Components** - Comma-separated components that will be added to the tickets.

* **Include missing adapters in description** *(default: enabled)* - Select to add to the  description of the issue all the adapters that aren’t connected to the asset.

* **Add asset fields to issue description** - Select to add a list of fields from the asset entity to the description of the issue.

* **Add asset description to issue description** - Select to add the aggregated ‘description’ field from the asset to the issue description.

* **Add asset host name to issue description** - Select to add the aggregated hostname field value to the description of the issue.

* **Add fields to issue description** - Select field values to add to the description of the issue. You can select multiple additional fields. The values of the selected fields are added to the **Request description**.

* **Map Axonius fields to fields in the description** - Use this field together with the **Request description** field to create dynamic ticket descriptions that include field values from the assets being reported on. In **Request description**, enter a description template that includes field placeholders for field mapping.

  Then, in **Map Axonius fields to fields in the description**, enter the field placeholder name on the left and on the right, select the Axonius field that contains the value you want included in the description. The value of the Axonius field is populated into the description in place of the placeholder text.

  In the example below, the fields selected under **Axonius fields** are mapped into the placeholders *Hostname*, *IP Address*, and *Serial*. Each asset that matches the query parameters will have its data added to the request description.

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/c9f302401ca18c4174af117d39616af70b02bb71/img/enforcement_actions/JiraTicketPerAssetMapFieldsToDesc.png" />

* **Custom fields (JSON format)** - Custom fields to add to this incident in JSON format.

<Callout icon="📘" theme="info">
  Note

  If a custom field is already configured by this Enforcement Action, the new custom value is ignored.
</Callout>

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Related parent ticket key** - Enter the key of the related parent ticket. The key usually includes the project key (string) and a sequential number, for example, "CT-1960".

* **Fetch created issue to Axonius** *(default: enabled)* - Select this option to enable the system to automatically retrieve information about newly created Jira issues and ingest that data into Axonius.

* **Create ticket as flavor** - Select this option to fetch ticket updates from the Jira Service Management Fetch Tickets adapter if you don't have a Jira Service Desk license. This requires enabling the **Fetch EC Action ticket updates** option in the [Jira Service Management (Service Desk) Fetch Tickets adapter](/docs/jira-fetch-tickets).

* **Send CSV data** - Select to include a CSV file with the query results in the issue created. For Vulnerabilities, the first row shows the vulnerability information, and the next rows show the linked devices.

**Additional CSV Settings**

* **Split by asset entities**  -  Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection.

  * If supplied, each value on a device or user is shown as a separate row.
  * If not supplied all values on a device are in the same cell on the CSV file.

* **Export CSV delimiter to use for multi-value fields** *(default:**Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[GUI Settings](/docs/gui-settings#system-settings)**)* - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.

* **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.

* **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each Software or Aggregated Security Finding. When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.

  * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Click the bin icon to remove a device field.

* **Group Security Findings by CVE ID** (default: disabled) - Enable this to have the Enforcement Action create one ticket per unique CVE ID. When you enable this, the following field appears:

  * **Fields to include in description** - Add fields you want to include in the CSV. Only nested fields of the **Security Findings** complex object field are available for selection.

  <Callout icon="🚧" theme="warn">
    **Important Notes about this Setting**

    When enabling **Group Security Findings by CVE ID**:

    * The assets or query selected for the Enforcement Action must be from the Security Findings module. Otherwise, the action will fail.
      * It is recommended to select only vulnerability-specific fields from the **Fields to include in description** selector, because it is not designed to aggregate individual assets that are part of a group.
        * For example, while fields like "CVE Severity" or “Vulnerability Remediation” are good choices, a field like “Associated Asset ID” is not, as it will only show the first Asset ID.
    * The action ignores the following fields even if they are selected:
      * Include missing adapters in description
      * Add asset fields to issue description
      * Add asset description to issue description
      * Add asset host name to issue description
      * Add fields to issue description
      * Axonius to Jira field mapping
    * The **Request summary** always ends with  ` - {CVE ID}`. For example, if the configured summary is “Vulnerability detected on multiple assets”, the summary for CVE-1234 is: `Vulnerability detected on multiple assets - CVE-1234`.
    * The **Request Description** includes, in addition to the provided description:
      * A section displaying the CVE ID
      * The first (up to) 10 asset host names in the group
    * When **Send CSV data** is also selected, the action attaches a single CSV to each ticket, containing all the columns selected in the trigger view (query or manual selection). The CSV in each ticket only includes information on assets in that group (with that specific CVE ID).
    * It is not recommended to use Dynamic Values (IFTTT) while enabling **Group Security Findings by CVE ID**, as that may cause unexpected behavior.
  </Callout>

* **Jira Cloud Workspace ID** - Enter a unique identifier for your Jira Cloud instance or "workspace."

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Action privileges

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).