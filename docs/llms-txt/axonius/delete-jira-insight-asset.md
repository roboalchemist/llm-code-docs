# Source: https://docs.axonius.com/docs/delete-jira-insight-asset.md

# Jira Service Management - Remove Insight Asset

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Premium or Enterprise license.
</Callout>

**Jira Service Management - Remove Insight Asset** removes the Jira Insight assets retrieved by the saved query supplied as a trigger (or from the asset selected in the asset table) from Jira Service Management.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

<Callout icon="📘" theme="info">
  Note:

  **To find the correct schema and the Jira Insight Fields IDs:**

  1. Go to your Jira instance and then click **Assets** then **Schema**.
  2. In **Schema**, select the object type and then click **Attributes**. The field IDs are listed here.

  Only users with admin privileges can see this menu.
</Callout>

## Required Fields

These fields are required to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Jira Service Management (Service Desk) adapter** - Select this option to use the Jira Service Management (Service Desk) adapter credentials. When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [ServiceDesk](/docs/atlassian-jira-service-desk) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

* **Target Jira Cloud Workspace ID** - The Jira Workspace ID from where assets will be removed. Only entities from this workspace will be processed.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: `https://.atlassian.net/`)* - Enter the host name or IP address of the Jira Service Management server.

  * **Jira Service Management API version** *(default: 1.0)* - Use the version of the API that matches the version of the Jira Service Management server.

  * **User Name** and **API Token** - The credentials for a user account that has the permissions to remove Insight assets. Note: The API Token is not the same as the Admin Key.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Use Cloud API** - Use this option to add support for cloud-based installations of Jira Service Management (Service Desk) with Jira Insight. When using the cloud API, the default host name or IP address is: [https://api.atlassian.com](https://api.atlassian.com)
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [The Insight REST API](https://developer.atlassian.com/cloud/insight/rest/api-group-object/#api-object-create-post).

This is the correct one for cloud: [https://developer.atlassian.com/cloud/assets/rest/api-group-object/#api-object-id-delete](https://developer.atlassian.com/cloud/assets/rest/api-group-object/#api-object-id-delete)
And this is for on-prem: [https://docs.atlassian.com/assets/REST/9.1.16/#object-deleteObject](https://docs.atlassian.com/assets/REST/9.1.16/#object-deleteObject)

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* **TCP port 443**
* **TCP port 80**

## Required Permissions

The account used to connect to Jira Service Management must have permissions to read, write, and remove Insight assets.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| Jira Insights 1.0 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).