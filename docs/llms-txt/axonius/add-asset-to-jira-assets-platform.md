# Source: https://docs.axonius.com/docs/add-asset-to-jira-assets-platform.md

# Jira Assets Platform - Add Assets

<Callout icon="❗️" theme="error">
  Notice

  [Jira](https://community.developer.atlassian.com/t/shutdown-notice-update-on-deprecation-of-the-external-assets-platform/81193) has deprecated this solution. Consequently, this Enforcement Action is no longer available in Axonius.
</Callout>

**Jira Assets Platform - Add Assets** creates a new asset or updates an existing asset in Jira Assets Platform for each of the assets that are the results of the   saved query supplied as a trigger (or devices that were selected in the asset table).

<Callout icon="📘" theme="info">
  NOTE

  Updating an asset will overwrite its properties with the properties defined in the request object from Axonius.
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

<Callout icon="📘" theme="info">
  Note:

  **To find the correct schema and the Jira Insight Fields IDs:**

  1. Go to your Jira instance and then click **Assets** then **Schema**.
  2. In **Schema**, select the object type and then click **Attributes**. The field IDs are listed here.

  Only users with admin privileges can see this menu.
</Callout>

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Jira Domain** *(required)* - The hostname or IP address of the Atlassian Jira Assets Platform server.

* **User Name** and **API key** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to read, add and to update assets.

* **Asset type appKey** and **Asset type originId** *(required, default: AxoniusEC | axonius-enforcement)* - Specify the appKey and the originId of an Asset Type you have created on your JIRA Assets Platform project.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **Assignee account ID** *(optional, default: empty)* - Specify the Atlassian account id for the assignee.
  * If supplied, the new/updated asset will be assigned to the specified account.
  * If not supplied and **Assignee email** is not supplied, the new/updated asset will not be assigned.

* **Assignee email** *(optional, default: empty)* - Specify the email address for the assignee. The email must be associated with a valid Atlassian account id.
  * If supplied and there is an account id associated with this email address, the new/updated asset will be assigned to the specified account.
  * If not supplied, or if supplied and there is no account id associated with this email address, the new/updated asset will not be assigned.

<Callout icon="📘" theme="info">
  NOTE

  If both **Assignee account ID** and **Assignee email** are supplied, the action will fail.
</Callout>

## APIs

Axonius uses the [Atlassian Jira Asset Platform - Create or Update Asset API](https://developer.atlassian.com/cloud/assetsapi/rest/#api-asset-put).

## Required Permissions

The value supplied in [User Name](#parameters) and in [API Key](#parameters) must have read, add and update access to devices.

To integrate Axonius with Jira, you need to do the following :

1. Create a user in Atlassian with access to Jira. The user should be part of the most basic group which is jira-software-users.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(420\).png)

2. Log in to Jira using the created user and generate an API token.
   For cloud based Atlassian sites, use the following URL to generate an API token: [https://id.atlassian.com/manage/api-tokens#](https://id.atlassian.com/manage/api-tokens#)

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(421\).png)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).