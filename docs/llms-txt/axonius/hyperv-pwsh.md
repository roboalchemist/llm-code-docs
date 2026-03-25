# Source: https://docs.axonius.com/docs/hyperv-pwsh.md

# Microsoft Hyper-V (PSRemote)

Microsoft Hyper-V is a native hypervisor. It can create virtual machines on x86-64 systems running Windows.
This adapter uses PSRemoting over WinRM, with JEA capabilities.

#### About WinRm and JEA

**Windows Remote Management (WinRM)** is the Microsoft implementation of the WS-Management protocol, which is a standard, Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows interoperation between hardware and operating systems from different vendors.
**Just Enough Administration (JEA)** is a security technology that enables delegated administration for anything managed by PowerShell. JEA helps you improve your security posture by reducing the number of permanent administrators on your machines. JEA uses a PowerShell session configuration to create a new entry point for users to manage the system. Users who need elevated, but not unlimited, access to the machine to do administrative tasks can be granted access to the JEA endpoint. Since JEA allows these users to run administrative commands without having full administrator access, you can then remove these users from highly privileged security groups.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices (Virtual Machines)

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Microsoft Hyper-V server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Port** *(required, default: 5985)* - The port used for the connection.
4. **Use SSL for WinRM Connection** *(required, default: True)* - Select whether to use SSL for the WinRM connection.
5. **Verify Server Certificate** *(required, default: False)* - Select whether to verify the server's SSL certificate.
6. **Proxy** *(optional)* - Enter address of the proxy server used for the connection. For example, `http://proxy.example.com:8080/`.
7. **JEA Configuration Name** *(required)* - The Just Enough Administration (JEA) configuration name to use for the connection. The default name is `Microsoft.PowerShell`. Refer to [Required Permissions](/docs/microsoft-hyper-v-psremote#required-permissions) and [Configuring JEA For Minimum Permissions](/docs/microsoft-hyper-v-psremote#configuring-jea-for-minimum-permissions) for more information.
8. **Connection Timeout** *(required, default: 60)* - Set the timeout in seconds for establishing the WinRM connection.
9. **Read Timeout** *(required, default: 30)* - Set the timeout in seconds for reading data from the WinRM connection.
10. **Operation Timeout** *(required, default: 20)* - Set the timeout in seconds for each operation executed on the Hyper-V host. This value must be smaller than the **Read Timeout** value.

![HyperV PSREmote connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3FAE1TNA.png)

## APIs

Axonius uses the Microsoft's [Just Enough Administration](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/jea/overview?view=powershell-7.4) API. In addition, to configure permissions for WinRm, refer to [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 5985 (default)
* 5986

## Required Permissions

To fetch assets successfully:

* WinRM must be enabled on the Hyper-V host.
* The user provided for **User Name** must have permission to access WinRM and use PSRemote to execute scripts.
* It is recommended to configure JEA (Just Enough Administration) for executing the required PowerShell scripts. See example in [Configuring JEA For Minimum Permissions](/docs/microsoft-hyper-v-psremote#configuring-jea-for-minimum-permissions).

<Callout icon="📘" theme="info">
  Note

  If JEA is not configured, use the default `Microsoft.PowerShell` as the **JEA Configuration Name**. Note that in this case, the user requires administrative privileges for the Hyper-V host.
</Callout>

### Configuring JEA For Minimum Permissions

This adapter executes the following PowerShell script:

```

# PowerShell script to query virtual machines and their associated information

# get the host fqdn
$hostName = [System.Net.Dns]::GetHostByName($env:computerName).HostName

# Query for virtual machines
$vmQuery = "SELECT * FROM Msvm_ComputerSystem WHERE Caption='Virtual Machine'"
$vms = Get-WmiObject -Query $vmQuery -Namespace "root/virtualization/v2"

# Query for synthetic ethernet ports
$syntheticEthernetPortQuery = "SELECT * FROM Msvm_SyntheticEthernetPort"
$syntheticEthernetPorts = Get-WmiObject -Query $syntheticEthernetPortQuery -Namespace "root/virtualization/v2"

# Query for disk drives
$diskDriveQuery = "SELECT * FROM Msvm_DiskDrive"
$diskDrives = Get-WmiObject -Query $diskDriveQuery -Namespace "root/virtualization/v2"

# Query for processors
$processorQuery = "SELECT * FROM Msvm_Processor"
$processors = Get-WmiObject -Query $processorQuery -Namespace "root/virtualization/v2"

# Query for guest network adapter configurations
$networkAdapterConfigQuery = "SELECT * FROM Msvm_GuestNetworkAdapterConfiguration"
$networkAdapterConfigs = Get-WmiObject -Query $networkAdapterConfigQuery -Namespace "root/virtualization/v2"
$exclude_property = 'Scope', 'Path', 'Options', 'ClassPath', 'Properties', 'SystemProperties', 'Qualifiers'

# Combine the results

$vms | ForEach-Object {
    $vm = $_
    $vmName = $vm.Name

    # Add the HyperV host name to the VM

    $vm | Add-Member -MemberType NoteProperty -Name DeviceHost -Value $hostName

    # Add synthetic ethernet ports (Switches) to the VM

    $vm | Add-Member -MemberType NoteProperty -Name Switches -Value $null
    $vm.Switches = $syntheticEthernetPorts | Select-Object -Property * -ExcludeProperty $exclude_property | Where-Object { $_.SystemName -eq $vmName }

    # Add disk drives to the VM

    $vm | Add-Member -MemberType NoteProperty -Name DiskDrives -Value $null
    $vm.DiskDrives = $diskDrives | Select-Object -Property * -ExcludeProperty $exclude_property | Where-Object { $_.SystemName -eq $vmName }

    # Add processors to the VM

    $vm | Add-Member -MemberType NoteProperty -Name Cpus -Value $null
    $vm.Cpus = $processors | Select-Object -Property * -ExcludeProperty $exclude_property | Where-Object { $_.SystemName -eq $vmName }

    # Add network adapter configurations to the VM

    $vm | Add-Member -MemberType NoteProperty -Name Networks -Value $null
    $vm.Networks = $networkAdapterConfigs | Select-Object -Property * -ExcludeProperty $exclude_property | Where-Object { $_.InstanceID -like "*$vmName*" }
}

# Output the combined results

$vms | Select-Object -Property * -ExcludeProperty Scope, Path, Options, ClassPath, Properties, SystemProperties, Qualifiers | ConvertTo-Json -Depth 4
'''
```

Below is an example template of how to configure JEA for minimum permissions, while allowing the script to fully execute.  Ensure to replace `PUT_PATH_HERE` with actual paths.
This example can be further customized for specific needs or policies. To learn more, refer to the [JEA documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/overview).

```

# PowerShell script to create a Just Enough Administration (JEA) configuration for Hyper-V Adapter

# Create a role capability that allows the user to run the cmdlets required by the Hyper-V adapter
New-PSRoleCapabilityFile -Path PUT_PATH_HERE.psrc `
  -Description "Role capability for Hyper-V Adapter" `
  -VisibleCmdlets @{ `
    Name = 'Get-WmiObject'; `
    Parameters = @{ Name = 'Query'; `

      ValidatePattern = '^SELECT \\* FROM Msvm_(ComputerSystem|SyntheticEthernetPort|DiskDrive|Processor|GuestNetworkAdapterConfiguration)$' `
    }, `
    @{ Name = 'Namespace'; `
        ValidateSet = 'root/virtualization/v2' `
    } }, `
    @{ Name = 'Select-Object'; }, `
    @{ Name = 'Where-Object'; }, `
    @{ Name = 'ConvertTo-Json'; }, `
    @{ Name = 'Add-Member'; }, `
    @{ Name = 'ForEach-Object'; }

# Create a session configuration that uses the role capability
New-PSSessionConfigurationFile -Path PUT_PATH_HERE.pssc `
  -SessionType RestrictedRemoteServer `
  -Description "Session configuration for Hyper-V Adapter" `
  -RoleDefinitions @{ `
    'HyperVAdapterRole' = @{ `
      RoleCapabilities = 'HyperVAdapterRole' `
    } `
  } `
  -RunAsVirtualAccount $true

# Register the session configuration
Register-PSSessionConfiguration -Name "HyperVAdapter" -Path PUT_PATH_HERE.pssc

# Test the session configuration
Test-PSSessionConfigurationFile -Path PUT_PATH_HERE.pssc
```

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Windows Server 2016 | Yes       | --    |
| Windows Server 2019 | Yes       | --    |
| Windows Server 2022 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1