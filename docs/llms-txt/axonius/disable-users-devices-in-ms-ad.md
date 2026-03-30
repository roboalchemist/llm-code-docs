# Source: https://docs.axonius.com/docs/disable-users-devices-in-ms-ad.md

# Microsoft AD - Disable Assets

**Microsoft AD - Disable Assets** disables and blocks assets returned by the selected query or assets selected on the relevant asset page, which are Microsoft Active Directory (AD) managed devices or users.

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
* **Use stored credentials from Microsoft Active Directory (AD) Adapter** - Select this option to use [Microsoft Active Directory (AD)](/docs/microsoft-active-directory-ad) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use these actions, you must successfully configure a [Microsoft Active Directory (AD)](/docs/microsoft-active-directory-ad) adapter connection.
</Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Username** and **Password** - If you want to use different credentials to perform this action, enter the desired username and password.
</Callout>

* **Should re-fetch asset if action is successful** - When enabled, after each successful run, the action will also re-fetch and update the asset in Axonius. For example, if a device was successfully disabled, it will be updated in the Devices page and the field `device.disabled` will be True.

## Permissions Required

The user/connection configured in this enforcement action must have the **Write account restrictions** permission enabled in order to perform this action.
If the user/connection is part of the Domain Admins group or Account Operators group it should already have all the required permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).