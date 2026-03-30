# Source: https://docs.axonius.com/docs/add-remove-delegate-control-tasks.md

# Microsoft AD - Add/Remove Delegate Control Tasks to/from Assets

**Microsoft AD - Add/Remove Delegate Control Tasks to/from Assets** adds a delegate control task to or removes a delegate control task from:

* Assets returned by the selected query or assets selected on the relevant asset page.

A Delegate Control task refers to the process of assigning a range of administrative tasks to  users, groups and other entities.

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

* **Hostname** - A domain controller with WinRM access.

* **User Name** and **Password** - Credentials to access the domain controller with WinRM access.

* **Target Distinguished Name** - The object that is the target of the delegate control task, for example: user, group, organizational unit, domain, etc.

* **Delegate Control Task** - From the dropdown list of permissions, select the permission to add or remove.

* **Role** -  From the dropdown list of roles, select the role to add or remove.

* **Action Type** - Add or Remove.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

**Example**
If the assets selected in the query are Users, and the following parameters are selected:

* **Target Distinguished Name** - Users
* **Delegate Control Task** - Change Password
* **Role** - WriteOwner
* **Action Type** - Add
  Then, this Enforcement Action will add to all Users a WriteOwner role and a Change Password permission, and users will be the target of the delegate control task. Meaning, this Enforcement Action assigns users a role and a permission to change password to other users.

## Additional Fields

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the following Microsoft PowerShell APIs:

* [Set-Acl](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-acl?view=powershell-7.5)
* [Get-Acl](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl?view=powershell-7.5)

## Required Ports

Axonius must be able to communicate to the WinRM service via the following ports:

* 5985 or 5986

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permission to run the following PowerShell commands:
  * Get-ADObject
  * Get-ADDomain
  * Get-Acl
  * Set-Acl

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).