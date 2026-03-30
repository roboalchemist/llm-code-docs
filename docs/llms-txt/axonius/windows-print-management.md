# Source: https://docs.axonius.com/docs/windows-print-management.md

# Windows Print Management

Windows Print Management is a tool that offers centralized management and control of print services within a network.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**
Axonius must be able to communicate with the value supplied in [Host Name or IP Address](/docs/windows-print-management#required-parameters) via the following ports:

* 5985 (default)
* 5986

### APIs

Axonius uses the [ Microsoft Get-Printer API](https://learn.microsoft.com/en-us/powershell/module/printmanagement/get-printer?view=windowsserver2025-ps).

### Permissions

The following permissions are required:

* WinRM must be enabled on the Hyper-V host.
* The user provided for [**User Name**](/docs/windows-print-management#required-parameters) must have permission to access WinRM and use PSRemote to execute scripts.
* It is recommended to configure JEA (Just Enough Administration) for executing the required PowerShell scripts. See example in [Configuring JEA For Minimum Permissions](/docs/microsoft-hyper-v-psremote#configuring-jea-for-minimum-permissions).

#### Supported From Version

Supported from Axonius version 6.1.66

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Microsoft server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.
3. **Port** *(required, default: 5985)* - The port used for the connection.
4. **Use SSL for WinRM Connection** - Select whether to use SSL for the WinRM connection.
5. **Verify Server Certificate** - Select whether to verify the server's SSL certificate.
6. **Proxy** *(optional)* - Enter address of the proxy server used for the connection. For example, `http://proxy.example.com:8080/`.
7. **JEA Configuration Name** - The Just Enough Administration (JEA) configuration name to use for the connection. The default name is `Microsoft.PowerShell`. Refer to [Configuring JEA For Minimum Permissions](/docs/microsoft-hyper-v-psremote#configuring-jea-for-minimum-permissions) for more information.
8. **Connection Timeout** *(default: 60)* - Set the timeout in seconds for establishing the WinRM connection.
9. **Read Timeout** *(default: 30)* - Set the timeout in seconds for reading data from the WinRM connection.
10. **Operation Timeout** *(default: 20)* - Set the timeout in seconds for each operation executed on the Hyper-V host. This value must be smaller than the **Read Timeout** value.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DRBX2PTL.png)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Windows Server 2016 | Yes       | --    |
| Windows Server 2019 | Yes       | --    |
| Windows Server 2022 | Yes       | --    |