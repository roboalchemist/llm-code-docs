# Source: https://docs.axonius.com/docs/winrm-scan.md

# WMI - WinRM Scan

**WMI - WinRM Scan** scans devices, enriches them and fetches local users for:

* Devices (only) returned by the selected query or assets selected on the relevant asset page.

This action requires the User specified in the configuration (username/password) to be added to the ‘Local Admins’ Group on any individual machine that is being targeted by the action.

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Port** - Enter a port to connect to. The default is 5986.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Connection ID from Active Directory adapter** - Enter the ID of the Active Directory adapter connection you want to use to run this action.

* **Proxy Server Hostname** - Enter the address of the proxy server used for the connection. For example, `http://proxy.example.com:8080/`.

* **Use SSL** - Select whether to use SSL for the WinRM connection.

* **User Name** and **Password** - The credentials of a user account that has permission to scan assets.

* **Fetch software licenses information**

* **Fetch Local Users** - Enable to fetch local users. Then, select whether to fetch builtin administrators and/or logon policy.

* **Fetch Shares Permissions** - Enable to fetch share permissions for shared folders.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the following APIs:

* [https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance?view=powershell-7.5](https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance?view=powershell-7.5)
* [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1)
* [https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localuser?view=powershell-5.1](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localuser?view=powershell-5.1)
* [https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localgroup?view=powershell-5.1](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localgroup?view=powershell-5.1)
* [https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localgroupmember?view=powershell-5.1](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.localaccounts/get-localgroupmember?view=powershell-5.1)

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

**Permission to run the following Powershell cmdlets:**
Get-CimInstance, Get-WmiObject, Get-LocalUser, Get-LocalGroup, Get-LocalGroupMember

**Permission to secedit and query the following WMI tables:**
Win32\_UserProfile, Win32\_UserAccount, Win32\_GroupUser, Win32\_Processor, Win32\_BIOS, Win32\_OperatingSystem, Win32\_LogicalDisk, Win32\_QuickFixEngineering, Win32\_ComputerSystem, Win32\_Battery, Win32\_TimeZone, Win32\_BaseBoard, Win32\_NetworkAdapterConfiguration, Win32\_Process, Win32\_Service, Win32\_Share, MSFT\_NetTCPConnection, Win32\_PnPEntity, SoftwareLicensingProduct

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).