# Source: https://docs.axonius.com/docs/update-ldap-attributes-of-users-or-devices-in-ms-ad.md

# Microsoft AD - Add or Update LDAP Attributes of Assets

**Microsoft AD - Add or Update LDAP Attributes of Assets** adds new or updates object LDAP attributes of existing Active Directory entries for:

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

* **Use stored credentials from the Active Directory adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

<Callout icon="📘" theme="info">
  NOTE

  If **Use stored credentials from the Active Directory adapter** is toggle off, the following fields need to be configured:
</Callout>

* **Action type** *(defualt: Update attributes)* - Select whether to add new or to update existing LDAP attributes.
* **Select data input method to use** - Select the source of the LDAP attributes:
  * **Use data from user input** - Manually input LDAP attributes.
  * **Use data from Axonius** - Use the data in Axonius fields to configure LDAP attributes. See [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping) for details on mapping Axonius fields to external fields.

<Callout icon="📘" theme="info">
  NOTE

  If the Aggregated adapter is selected, aggregated fields may contain data as a list. Active Directory does not accept lists.
</Callout>

* **LDAP Attributes`-`Attribute name** and **Attribute value** *(required, default: empty)* - Specify a single set or a list of LDAP attribute names and values to be updated for the Active Directory entity. Click the `+` to add multiple LDAP attribute sets. Click the trashcan icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIconBlackonWhite.png) to delete an attribute set.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

* **User** and **Password** *(optional)* - Provide credentials to connect and to execute the command on the windows device: user name and password.

<Callout icon="📘" theme="info">
  NOTE

  If **Use stored credentials from the Active Directory adapter** is toggled on, the above fields do not need to be configured.
</Callout>

* **Skip Axonius value if empty** - If the value of the Axonius field is empty or 0 (zero), the assignment of that specific attribute will be skipped.

## Permissions Required

The user/connection configured in this enforcement action must have the **Write all properties** permission enabled  in order to perform this action.
If the user/connection is part of the Domain Admins group or Account Operators group it should already have all the required permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).