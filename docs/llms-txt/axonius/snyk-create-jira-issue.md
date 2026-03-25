# Source: https://docs.axonius.com/docs/snyk-create-jira-issue.md

# Snyk - Create Jira Issue

**Snyk - Create Jira Issue** creates a new ticket in Jira for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from the YYY adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a \[YYY]\(add link to the adapter docs) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name** or **IP Address** *(default: `https://api.snyk.io`)* - The hostname or IP address of the Snyk server.

  * **API Token** - An API Token associated with a user account that has the permissions to fetch assets. Refer to [Snyk API](https://docs.snyk.io/snyk-api-info) for information on how to obtain the API Key.

  * **API Prefix** *(default: Standard (api/v1)* - Select between *Standard (api/v1)* and *Alternate (v1)*.

  * **Group ID** - Snyk Group ID. Either use a Group ID or an Organization ID. Using a group ID will fetch all users in the group (across all organizations).

  * **Organzation ID** - Snyk Organization ID. Either use a Group ID or an Organization ID. Using an organization ID will fetch all users in the organization.

  <Callout icon="📘" theme="info">
    **Note**

    If both are supplied, the group ID is used
  </Callout>

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Project (JSON)** - The project field in the request body in JSON format.

* **Issue Type (JSON)** - The issuetype field in the request body in JSON format.

* **Summary** - The summary field in the request body.

* **Description (JSON)** - The description field in the request body in JSON format.

* **Map Security Finding fields into the description** - Dynamic values to add to the description field in the request body. See [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping)

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Ports

* TCP port 80/443

## APIs

Axonius uses the [Snyk API](https://snyk.docs.apiary.io/#).

You must have a Snyk Business or Enterprise plan to access the API. For more information, see [Snyk API documentation](https://docs.snyk.io/snyk-api-info).

## Required Permissions

The value supplied in [API Token](#required-parameters) must be associated with credentials that have Group Viewer (when using Group ID) permissions or Organization Collaborator (when using Org ID) permissions, in order to fetch assets.

In order to fetch devices View Project, View Project Snapshot permissions are required.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).