# Source: https://docs.axonius.com/docs/qualys-update-asset-name.md

# Qualys - Update Asset Names to Host Names

**Qualys - Update Asset Names to Host Names**  updates the Asset Name to be the same as the Host Name for:

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

* **Use stored credentials from the Qualys Cloud Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a [Qualys Cloud Platform](/docs/qualys-cloud-platform) adapter connection.
    * The user name and the password used for the adapter connection must have the [Required Permissions](#required-permissions) listed below.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## APIs

Axonius uses the [Qualys API  - Update API](https://www.qualys.com/docs/qualys-asset-management-tagging-api-v2-user-guide.pdf).

## Required Permissions

The value supplied in User Name must be associated with one of the following user roles and with the following permissions:

* Manager role with full scope.
* Non-manager role with the following permissions:

  * Access Permission "API Access".
  * Asset Management Permission "Update Asset".

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).