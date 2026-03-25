# Source: https://docs.axonius.com/docs/add-tag-to-host-asset-in-qualys-cloud-platform.md

# Qualys - Add Tags to Host Asset

**Qualys - Add Tags to Host Asset** adds a specified list of tags to each device entity retrieved from the saved query supplied as a trigger (or to devices selected in the asset table) that is a host asset in Qualys.

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

* **Use stored credentials from the Qualys Cloud Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Qualys Cloud Platform](/docs/qualys-cloud-platform) adapter connection.
  </Callout>

* **Tags** - Specify at least one new or existing tag in Qualys to be associated with each of the host assets in Qualys. Tag names are case sensitive.

  <Callout icon="📘" theme="info">
    Note

    If Axonius will fail to create a tag or add tags to a host asset, Axonius will roll back the entire action and will fail it.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Qualys Cloud Platform Domain** - The hostname of the Qualys API (for example, qualysapi.apps.qualys.com). For more details on how to determine your Qualys API URL, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/).

  * **User name** and **Password** -  The credentials for a user account that has the [Required Permissions](#required-permissions) to add a specified list of tags to each host asset in Qualys.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Parent tag name** - Designate an existing Qualys tag to be the parent tag of the tags being added. Tag names are case sensitive. When no parent tag is supplied, the new tags are added without a parent.

  <Callout icon="📘" theme="info">
    Note

    The specified tag must exist in Qualys. If it does not exist in Qualys, Axonius will fail to run the action.
  </Callout>

* **Use all Qualys IDs** - Use all available Qualys IDs to add the new tags.

## Required Permissions

The value supplied in [User Name](#connection-settings) must be associated with one of the following user roles and with the following permissions:

1. Managers with full scope
2. Other roles with the following permissions:
   * Desired host assets in scope.
   * Access to the API.
   * Tag permission: "Create User Tag", "Delete User Tag"
   * Asset Management permission: "Read Asset", "Update Asset".

To enable user access to the API:

1. From Qualys, click the user button next to the Logout -> **User Profile**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(758).png" />
2. The **Edit User** screen opens. Click **User Role** ->  select the **API** checkbox to enable API Access.

   <Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(759).png" />
3. Save changes.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).