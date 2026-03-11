# Source: https://docs.axonius.com/docs/update-jira-insight-asset.md

# Jira Service Management - Update Insight Asset

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Premium or Enterprise license.
</Callout>

**Jira Service Management - Update Insight Asset** (previously Jira Service Desk - Update Insight Asset/Update Jira Insight Asset) updates a Jira Insight asset for the asset retrieved from the saved query supplied as a trigger (or from the asset selected in the asset table).

This is intended for use with Jira Service Management.

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

* **Use stored credentials from Jira Service Management (Service Desk) adapter** - Select this option to use the Jira Service Management (Service Desk) adapter credentials. When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [ServiceDesk](/docs/atlassian-jira-service-desk) adapter connection.
  </Callout>

## Required Fields

These fields are required to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Static Attributes** - Define the static Jira field IDs and their values. Click `+` to add a static attribute. Multiple static attributes can be added.

  <Callout icon="📘" theme="info">
    Note

    * Mapped field values change based on the values of the devices.
    * Static field values are inserted to all devices without regard of the given device’s values.
  </Callout>

* **Create Reference Object If Not Exist** -
  * Some Jira objects might contain attributes that refer to other objects in Jira. The Enforcement Action searches for these reference objects by their name in Jira. If they exist, their name is converted into their objectKey and the original object is updated in Jira accordingly. If the objects don’t exist, the action is marked as failed.
  * When this option is selected and the referenced object doesn’t exist, Axonius creates the referenced object (only with its name) and then continues with the update of the original object. When not selected, the action is marked as failed.

* **Alternative IQL query to search for referenced fields** - Enter the IQL lookup query used to find related data from field attributes.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address**   - The hostname or IP address of the Jira Service Management  server.

  * **Jira Service Management API version** - The Jira Service Management API  number.

  * **User Name** and **API Token**  - The credentials for a user account that has the permissions to read and write.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Use Cloud API** - Select this option to explicitly specify that the enforcement should use the Cloud API instead of Jira Server API.  When the user is using the cloud API the default host name or IP address should be [https://api.atlassian.com](https://api.atlassian.com). Even when left unselected, the action will attempt to use the cloud API if the domain specified is “api.atlassian.com”.

## APIs

Axonius uses the [The Insight REST API](https://developer.atlassian.com/cloud/insight/rest/api-group-object/#api-object-create-post).

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* **TCP port 443**
* **TCP port 80**

## Required Permissions

The values supplied in [Connection Settings](#connection-settings) must have permissions to read and write.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| Jira Insights 1.0 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).