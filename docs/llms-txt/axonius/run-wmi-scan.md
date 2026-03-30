# Source: https://docs.axonius.com/docs/run-wmi-scan.md

# Axonius - Run Windows WMI Scan

**Axonius - Run Windows WMI Scan** runs a WMI (Windows Management Instrumentation) scan on each of the query results entities, which are windows devices.

As part of the WMI scan, Axonius reaches out to devices directly and execute commands on them in memory, without installing anything or leaving any traces. The WMI scan retrieves important information about the device, including (but not limited to):

* Hostname
* Network Interfaces - including MAC addresses, IP addresses and subnets
* Operating system, kernel version and distribution
* List of installed software
* Users and admin users
* Hard drives and file systems
* CPUs and RAM
* Hardware details, including serial numbers

This action requires the User specified in the configuration (username/password) to be added to the ‘Local Admins’ Group on any individual machine that is being targeted by the action.

If **Run WMI Scan** action was executed on specific device, **Windows Management Instrumentation (WMI)** adapter is also listed as one of the device different adapters listed under the **Adapter Connections** tab, on the **Device Profile** page. Most of the WMI scan information is also displayed under the various **Aggregated** tables.
For more details, see [Asset Profile page](/docs/asset-profile-page).

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

**Use stored credentials from the Active Directory adapter** - Select this option to use the first connected Microsoft Active Directory (AD) adapter credentials.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Active Directory (AD)](/docs/microsoft-active-directory-ad) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

**Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **User name** and **Password**   - Provide credentials to connect and to execute the command on the windows device: user name and password.

  <Callout icon="📘" theme="info">
    Note

    If **Use stored credentials from the Active Directory adapter** is disabled, this fields are required.
  </Callout>

  * **DNS Servers**   - Specify a comma-separated list of DNS servers to be used to resolve the hostnames in the saved query supplied as a trigger (or devices that have been selected in the asset table).

    * If supplied, Axonius will use the specified DNS server to resolve the devices' hostnames. For each asset, the first response will be the one to be used.

    * If not supplied or if no response has been received from any of the specified DNS servers, the default DNS server will be used.

  * **Use NBNS** - Use the NetBIOS Name Service.
</Callout>

* **Registry keys to check for existence**   - Specify the registry keys that you want to check whether they exist. These values are stored in the 'Validated Registry Keys - Existing' or 'Validated Registry Keys - Not Existing' fields of the device depending whether they exist  or not.
* **Registry keys to get key-value pairs** - Enter Registry keys for which the system will search for the values on specific registries of the windows computer and stores them in a field called 'Validated Registry Keys - Existing Values' in the device.
* **Fetch software licenses information** *(default: false)* - Select this option to fetch software licensing product information from each host. The results are presented in a list field called 'Software Licensing Product Information'.
* **Fetch Remote Desktop client access licensing information** *(default: false)* - Select this option to fetch information from the Remote Desktop Client Access Licensing Server. This setting  only  works for RDS Licensing Server hosts. Refer to [Activate the Remote Desktop Services license server](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-activate-license-server) to learn how to activate this on a host.
* **Fetch SQL Server License information** - Set this option to search for Microsoft SQL Server license information on the machine’s registries and fetch it
* **Fetch installed software from Win32\_Product class**  - Select this option to fetch data from the Win32\_Product class.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).