# Source: https://docs.axonius.com/docs/change-users-devices-ou.md

# Microsoft AD - Change Asset OU

**Microsoft AD - Change Asset OU** moves the assets retrieved from the saved query supplied as a trigger (or assets that were selected in the asset table) from one Organizational Unit (OU) to another in Microsoft Active Directory (AD).

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

* **Use stored credentials from the Active Directory adapter**   - Select this option to use the first connected Active Directory adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure an [Active Directory](/docs/microsoft-active-directory-ad) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Organization Unit string (OU**) -  Enter the Organization Unit string. In the string, instead of the name of the Organization Unit set OU=Disabled.

For example if the user DN (distinguished name) is: “CN=user1,OU=Users,DC=ad-test,DC=com” you need to enter the string in this format “OU=Disabled,DC=ad-test,DC=com“.  A user can also be moved to an Organization Unit in a different domain.

For all cases make sure you enter the full path for the OU to which you want to move the user.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

  <br />

  ## Additional Fields

These fields are optional.

1. **User Name** and **Password** - The credentials for the AD user account to perform the action.

<Callout icon="📘" theme="info">
  Note

  When **Use stored credentials from the adapter** is toggled off, this field needs to be configured:
</Callout>

2. **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [ldap3 MODIFY\_DN Operation API](https://ldap3.readthedocs.io/en/latest/modifydn.html).

## Required Permissions

The value supplied in [User Name](#connections-settings) must have permission to change users and computers in  AD.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).