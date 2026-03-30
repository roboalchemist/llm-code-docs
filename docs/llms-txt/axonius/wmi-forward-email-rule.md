# Source: https://docs.axonius.com/docs/wmi-forward-email-rule.md

# WMI - Forward Email Rule

**WMI - Forward Email Rule** can be configured to do the following for Users that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined, or users selected on the Users page:

* Update the email configuration with a forwarding email address so that messages are forwarded automatically to that address.
  For example: This can be used on users who terminate employment and are no longer to receive emails to their company email addresses but to their private email addresses.
* Unset forwarding.
  For example: This can be used after a period of time, when you want to stop forwarding emails to past employees.

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

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on Users only.
</Callout>

<Callout icon="📘" theme="info">
  Note

  To use this action, you must successfully configure a [Windows Management Instrumentation (WMI)](/docs/wmi) adapter connection. This enforcement action uses the adapter connection to talk to the Exchange Server on a domain.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
* **Exchange server address** - The URL address of the Microsoft Exchange (mail) Server 2003 by WMI.[Exchange PowerShell](https://learn.microsoft.com/en-us/powershell/module/exchange/?view=exchange-ps) must be installed in the exchange server that the Enforcement Action runs on.
* **Mailbox Forwarding Action** - Select one of the following:
  * **Set Forwarding Address** *(default)* - When this option is selected, the enforcement action updates the user with the forwarding address entered in the following field that opens:
    * **Forwarding Address** - Enter the forwarding email address.
  * **Unset Forwarding Address** - When this option is selected, the enforcement action erases the forwarding configuration.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **DNS servers** - *(default: empty)* - Specify a comma-separated list of DNS servers to be used to resolve the hostnames. If not supplied or if no response has been received from any of the specified DNS servers, the default DNS server is used.
* **Use NBNS** - *(default: disabled)* - Enable this option to verify the server's name via NetBios for this connection.

## Required Permissions

The Microsoft Exchange (mail) Server 2003 by WMI must have Read-only permissions.
The user credentials used for this enforcement action must have permissions to execute the **Set-Mailbox** command.You can [use PowerShell to find the permissions required to run a cmdlet](https://learn.microsoft.com/en-us/powershell/exchange/find-exchange-cmdlet-permissions?view=exchange-ps#use-powershell-to-find-the-permissions-required-to-run-a-cmdlet).

For more details about other enforcement actions available, see [Action Library](/docs/action-library).