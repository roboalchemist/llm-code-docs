# Source: https://docs.axonius.com/docs/create-jira-insight-asset-per-entity.md

# Jira Service Management - Create Insight Asset per Asset

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Premium or Enterprise license.
</Callout>

**Jira Service Management - Create Insight Asset per Asset** (previously **Jira Service Desk - Create Insight Asset per Asset**) creates a Jira Insight asset for **each** asset retrieved from the saved query supplied as a trigger (or from the assets selected in the asset table).

When creating Jira assets, no adapter connection is required. To be able to update assets in Jira, you must configure the Jira Service Management adapter.

**Jira Service Management - Create Insight Asset per Asset** also updates the asset if it already exists. The action works as follows:

* For each asset returned:
  * Assets not previously fetched using the Jira Service Management adapter are created as new assets in Jira.
  * Assets previously fetched using the Jira Service Management adapter that have a **Workspace ID** and an **Object Type ID** as defined in the action configuration are updated in Jira.
  * Assets previously fetched using the Jira Service Management adapter, with the **Workspace ID** as defined in the action configuration but with a different **Object Type ID** from that defined in the action configuration are skipped.

The system returns appropriate messages for each operation.

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

* <br />
  * **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Use stored credentials from Jira Service Management (Desk) adapter** - Select this option to use the Jira Service Management (Desk) adapter credentials. When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Jira Service Management (Desk)](/docs/atlassian-jira-service-desk) adapter connection.
  </Callout>
* **Object Type ID** - The type of asset to create.

<Callout icon="📘" theme="info">
  Note:

  **To find the correct schema and the Jira Insight Fields IDs:**

  1. Go to your Jira instance and then click **Assets** then **Schema**.
  2. In **Schema**, select the object type and then click **Attributes**. The field IDs are listed here.

  Only users with admin privileges can see this menu.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Target Jira Cloud Workspace ID** - The Jira Workspace ID where assets will be created. Only entities from this workspace will be processed.
* **Map Axonius fields to Jira Insight fields ID** - Maps one or more Axonius fields to the selected Jira Insight fields. Enter the ID of a Jira Insight field, the adapter and the Axonius field. Field mapping can also be specified by uploading a CSV according to the template or in JSON format.
  * Click **Template** to download the CSV template.
  * Click **Import CSV** to upload the field mapping as a CSV file according to the dowloaded template format.
  * Click **JSON view/Wizard view** to toggle between **Wizard view** and **JSON view**. The field mapping can be written in JSON format and pasted into the text box.
  * In the **Wizard view**, click **+ Add Field** to add another field mapping.

    <Image border={false} src="https://files.readme.io/c0f35fc6f6a8049d534166d1b505a46183c43d12ff0da52b9c781461ecc47e3b-image.png" />

    <br />
* **Static Attributes** - Define the static Jira field IDs and their values. Click `+` to add a static attribute. Multiple static attributes can be added.

<Callout icon="📘" theme="info">
  Note

  * Mapped field values change based on the values of the devices.
  * Static field values are inserted to all devices without regard of the given device’s values.
</Callout>

* **Don't return failed if assets are not created because of unique attributes**  -  An attribute in Jira can be defined as 'unique'. It is not possible to create a new asset  in Jira if it has the same attribute with the same value as an attribute that is 'unique’.
  You can select this option to define that when the reason that  Jira assets are not created is because they have a unique attribute, the enforcement action will be defined as a success, (however, a message will show that the asset was not created).
  When the checkbox is not selected, if the reason an action is not able to create a Jira asset is because it has a unique attribute, the enforcement action will be defined as 'failed'.

* **Create Reference Object If Not Exist** -
  * Some Jira objects might contain attributes that refer to other objects in Jira. The Enforcement Action searches for these reference objects by their name in Jira. If they exist, their name is converted into their objectKey and the original object is created in Jira accordingly. If the objects don’t exist, the action is marked as failed.
  * When this option is selected and the referenced object doesn’t exist, Axonius creates the referenced object (only with its name) and then continues with the creation of the original object. When not selected, the action is marked as failed.

* **Alternative IQL query to search for referenced fields** - Enter the IQL lookup query used to find related data from field attributes.

<Callout icon="📘" theme="info">
  Note

  If **Use stored credentials from the [Jira Service Management (Desk)](/docs/atlassian-jira-service-desk) adapter**  is not enabled, the following fields are required.
</Callout>

* **Host Name or IP Address**  - The hostname or IP address of the Jira Service Desk server.

* **Jira Service Management API version** - The version number of the Jira Service Management API.

* **User Name** and **API Token**  - The credentials for a user account that has the permissions to read and write.

* **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**

* **HTTPS Proxy Password**  - The password to use when connecting to the server using the **HTTPS Proxy**.

* **Use Cloud API** - Select this option to explicitly specify that the enforcement should use the Cloud API instead of Jira Server API.  When the user is using the cloud API the default host name or IP address should be [https://api.atlassian.com](https://api.atlassian.com). Even when left unselected, the action will attempt to use the cloud API if the domain specified is “api.atlassian.com”.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

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