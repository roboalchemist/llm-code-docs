# Source: https://docs.axonius.com/docs/add-users-devices-in-ms-ad.md

# Microsoft AD - Add Assets to Group

**Microsoft AD - Add Assets to Group** adds the assets retrieved matching the parameters of the saved query (or assets that have been selected in the asset table) to an Active Directory group.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from the Active Directory adapter** - Select this option to use the first connected Active Directory adapter credentials.

<Callout icon="📘" theme="info">
  Note

  * To use this option, you must successfully configure an [Active Directory](/docs/microsoft-active-directory-ad) adapter connection.

  * The user name and the password used for the adapter connection must have the [Required Permissions](/docs/microsoft-active-directory-ad#required-permissions) to fetch assets.
</Callout>

* **Group Distinguished Name (DN)** - The distinguished name of the group to which to add the users.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **User Name** and **Password** - The credentials for a user account that has the permissions to perform this action.

## Required Ports

Axonius must be able to communicate with the value supplied in [DC Address](/docs/microsoft-active-directory-ad#parameters) via the following ports:

* TCP/UDP port 389.

If you choose to use the stored credentials from the adapter then refer to [Required Ports ](/docs/microsoft-active-directory-ad#required-ports) for information about all additional ports required.

## Required Permissions

The value supplied in [User name](#connections-settings) must have permission to modify the group listed.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).