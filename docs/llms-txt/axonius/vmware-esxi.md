# Source: https://docs.axonius.com/docs/vmware-esxi.md

# VMware ESXi and vSphere

VMware ESXi is an enterprise-class, type-1 hypervisor for deploying and serving virtual computers.
VMware vSphere is VMware's cloud computing virtualization platform.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Users, Compute Services, Compute Images

## Use cases the adapter solves

The Axonius VMware ESXi adapter is the window into all virtualized workloads under VMware. It  provides full details of each guest system including OS, IP, ‘hardware’ parameters, network allocation, and VMware tools are installed.

**Data retrieved by VMware ESXi and vSphere**

ESXi is focused only on devices, and each system (whether on or off) can be reported in Axonius together with Interfaces, IP addresses, MAC, OS details, operational status, etc.

## Before You Begin

### Permissions

The vCenter user integrated with Axonius must have the 'Read-only' global permission.

### APIs

Axonius uses the vCenter API to fetch information about virtual devices, ESX hosts and local accounts.

### Creating a User in vCenter

1. Log in to vCenter as an administrator.

<Callout icon="📘" theme="info">
  Note

  The screenshots below were taken from the vSphere Client.
</Callout>

2. Select **Menu** `>` **Administration**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(41\).png)
3. From the left menu, click **Users and Groups**. Under the **Users** tab, from the **Domain** field, select the domain. Then click **Add User**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(834\).png)
4. Fill in the relevant details.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(837\).png)
5. From the left menu, click **Global Permissions** and add a 'Read-only' permission to the created user. Select the **Propagate to children** checkbox. To fetch Users (Local Accounts) a super administrator role is required.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(836\).png)

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host** - The hostname of a specific ESX server or of the vSphere server.
   If a vSphere server hostname is supplied, the connection for this adapter will pull information about all ESX servers managed by that vSphere server.

2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets. The user name format is **user\@domain**.
   For details, see the [Creating a User in vCenter](#creating-a-user-in-vcenter) section.

<Image alt="esxi" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-TFD3WZZ0.png" />

### Optional Parameters

1. **vCenter REST API URL** - The URL of the vCenter, created using input from the Host value. It should be in the format `https://{vcenter_server_ip_or_dns}/api`

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users And Local Accounts** - By default, this adapter fetches users and local accounts. Clear this option to not fetch users and local accounts.

   <Callout icon="📘" theme="info">
     **Note**

     vAPI-based features (such as Tags, Categories, Appliance Version, and Local Accounts) are available only when connecting to vCenter. When connecting directly to an ESXi host (HostAgent), these vAPI features are skipped by design.
   </Callout>
2. **Fetch only turned on machines** - Select whether to fetch only ESXi devices in which their power state is turned on.
3. **Exclude IPv6 addresses** - Select whether to fetch IPv6 addresses.
   * If enabled, all connections for this adapter will fetch only IPv4 addresses.
   * If disabled, all connections for this adapter will fetch both IPv4 and IPv6 addresses.
4. **Use UUID as manufacturer serial number** - Select whether to fill the 'device\_manufacturer\_serial' field with the value of the UUID.
5. **Use formatted UUID as manufacturer serial number for the following node types** - Select the specific node types for which you want to format the UUID as the manufacturer's serial number.

<Callout icon="📘" theme="info">
  Note

  Only one of the two above settings (**Use UUID as manufacturer serial number** or **Use formatted UUID as manufacturer serial number for the following node types**) should be selected because they assign data to the same field.
</Callout>

6. **Fetch snapshots** - Select this option to fetch snapshots from Virtual Machines.
7. **Parse all tags as fields** - When this is enabled, all connections for this adapter will parse any tag associated with a fetched asset as:
   * Values of the Adapter Tags field.
   * Designated field with the name of the tag key and the value of the tag value.
8. **List of tags to parse as fields** - Enter a comma-separated list of tag keys to be parsed as device or user fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.
   * The tag is only parsed on VirtualMachineresource types by default.
     * Tags with case-sensitive values are supported. Enter tags with case-sensitive values with double-quotes, e.g.  ` VirtualMachine:"DEVELOP”`
     * To specify a different resource type, enter the tag name in the form `vmware_resource_type:tag_name` Example: `ComputerResource:CR`, `VirtualMachine:VM`, `HostSystem:HS`
9. **Force use of SerialNumberTag as serial** - Select this option to force parsing the serial number from the 'SerialNumberTag' field.
10. **List of hostnames to be replaced by asset name** - Enter a list of hostnames that, if the asset name matches either of them, it can replace them. For example - if the asset name is X and there is a Y hostname in the list, X will replace the value of Y in the Host Name field.
11. **List of hostnames patterns to be replaced by asset name** - Enter a list of hostnames **in regex pattern** that, if the asset name matches either of them, it can replace them.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                   | Supported | Notes                                        |
| ------------------------- | --------- | -------------------------------------------- |
| VMWare Versions 6.0 - 7.0 | Yes       | Users supported from vCenter 6.7 and higher. |
| VMWare Version  8         | Yes       |                                              |