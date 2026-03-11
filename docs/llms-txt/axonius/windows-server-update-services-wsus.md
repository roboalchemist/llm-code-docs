# Source: https://docs.axonius.com/docs/windows-server-update-services-wsus.md

# Windows Server Update Services (WSUS)

Windows Server Update Services (WSUS), previously Software Update Services (SUS), enables administrators to manage the distribution of updates and hotfixes released for Microsoft products.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Authentication** - Select Authentication method, either **NTLM** (default) or **Kerberos**. If you select Kerberos, the following optional fields for authentication may be configured:
   * **Kerberos AES Key** *(optional)* - A cryptographic key, either 128 or 256 bits in length, used to secure communication by encrypting and decrypting messages exchanged between the client and the server.
   * **Kerberos Host (KDC)** *(optional)* - The Kerberos Key Distribution Center (KDC) that will be used to authenticate. If this parameter is not specified, the domain will be used.

2. **WSUS Server** *(required)* - The IP/FQDN hostname of the Windows Server Update Services (WSUS) server.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to execute PowerShell code which queries the WSUS server for information on the systems managed by that server.

4. **WSUS Service Port** *(optional, default: 8530)* - Specify the WSUS Database Service port to connect to. By default, WSUS is configured to use HTTP (non-SSL) over port 8530, and HTTPS (SSL) over port 8531.
   * If **WSUS Service Port** is left blank and **Use SSL for WSUS Service Connection** is not selected,  port **8530** is used.
   * If **WSUS Service Port** is left blank and **Use SSL for WSUS Service Connection** is selected,  port **8531** is used.
   * This configuration is overridden when **Do Not Pass Arguments to Get-WsusServer** is selected. In that case, the PowerShell command displays "Get-WsusServer", regardless of the Service Port configuration.

5. **Use SSL for WSUS Service Connection** *(optional, default: False)* - Use SSL for the PowerShell connection to the WSUS server (by default, uses port 8531). If not selected, uses the port 8530 (or the configured service port) and no SSL.
   * When selected, the PowerShell command displays: Get-WsusServer -Name `{hostname}` -Port `{port or 8531}` -UseSsl
   * When not selected, the PowerShell command displays: Get-WsusServer -Name `{hostname}` -Port `{port or 8530}`
   * This setting is overridden when **Do Not Pass Arguments** is selected. In that case, the PowerShell command displays “Get-WsusServer” regardless of the **Use SSL setting**.

6. **Do Not Pass Arguments to Get-WsusServer** *(optional, default: False)* - Select this option for older versions of the WSUS server that do not support **WSUS Service Port** or **Use SSL for WSUS Service Connection** options.
   * When selected, the PowerShell command displays "Get-WsusServer" with no arguments, regardless of the values of the **WSUS Service Port** and **Use SSL for WSUS Service Connection** options.
   * When not selected, the PowerShell command is modified according to the **WSUS Service Port** and **Use SSL for WSUS Service Connection** options.

7. **Custom Share Name** *(optional)* - The name of the Windows Share on the specified host, for example, `AxoniusShare$`. If you do not specify a name, the adapter will use `Admin$`. For more information, see [Creating a Custom Share](/docs/windows-server-update-services-wsus#creating-a-custom-share).

8. **Custom Files Directory** *(optional)* - The name of the directory to use within the specified Share, for example, `AxoniusDirectory`. If you do not specify a name, the adapter will use `axonius`.

9. **Custom Working Directory** *(optional, default: False)* - If file sharing is restricted in the domain, specify the physical path of the share specified in **Custom Share Name**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Callout icon="📘" theme="info">
  Note

  The WSUS adapter uses WMI
</Callout>

![Windows%20Server%20Update%20Services%20(WSUS)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Windows%20Server%20Update%20Services%20\(WSUS\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **Number of assets to fetch per page** *(required, default: 20)* - Set the number of results per page, to gain better control on the performance of all connections of for this adapter.
* **Disable SMB Dialects during negotiation** - From the drop-down select the versions of the SMB dialects to be disabled during the negotiation of the SMB connection.
* **Fetch Downstream Servers** - Select to fetch Downstream Servers and the client computers attached to each of them. To enable this setting, ensure of the following:
  * WSUS API ports are open in Downstream Servers (default: 8530 for HTTP, or 8531 for HTTPS).
  * The WSUS admin console is installed on the Upstream Server.
  * The Upstream Server can resolve Downstream Servers by hostname (DNS or hosts file).
  * The Upstream Server can reach Downstream Servers over the required port. You can test this with `Test-NetConnection DownstreamServer -Port 8530`.
  * The user running the command has permissions on Downstream Server's WSUS.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

* 135(RPC)
* 445 (SMB)
* Random port in the range 1024-65535

### Setting up a fixed port for WMI

The WSUS adapter uses WMI.
You need to set up a fixed port to work with WMI.
WMI runs as part of a shared service host with ports assigned through DCOM by default. However, you can set up the WMI service to run as the only process in a separate host and specify a fixed port. For more details, see [Microsoft Documentation - Setting Up a Fixed Port for WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi?redirectedfrom=MSDN).

To set up a fixed port for WMI:

1. At the command prompt, type:

```
winmgmt -standalonehost
```

2. Stop the WMI service by typing:

```
net stop "Windows Management Instrumentation"
```

or:

```
 net stop winmgmt
```

3. Restart the WMI service again in a new service host by typing:

```
net start "Windows Management Instrumentation" 
```

or:

```
net start winmgmt
```

4. Establish a new port number for the WMI service by typing (e.g. the following example will establish port TCP 24158):

```
netsh firewall add portopening TCP 24158 WMIFixedPort
```

To undo any changes you make to WMI, type:

```
winmgmt /sharedhost
```

Then stop and start the *winmgmt* service again.

### Creating a Custom Share

You can create a custom share and directory instead of ADMIN$ \ axonius. A custom share that is properly configured enables you to not require full local admin permissions to fetch data.

To create a custom share:

1. Create a local user, such as ‘axonius-usr’.

2. Add the user to the following groups:

   * WSUS Administrators
   * WSUS Reporters
   * Distributed COM Users
   * Remote Management Users

3. Create a directory for Axonius to use to store temporary files and to serve as a working directory, for example: C:\axonius
   The name of this directory may be used later in the adapter configuration for WSUS in Axonius.

4. Grant the following permissions to the local user:

   * Read
   * Write
   * Modify
   * Execute (or full control) permissions on the custom directory, subdirectories, and files

5. Share the directory that you created by using Sharing or Advanced Sharing. Verify that the local user has full permissions for this share. Specify a descriptive name for the shared directory, preferably a name which ends with a dollar-sign, such as: AxoniusShare$
   The name of this share will be used later in the adapter configuration for WSUS in Axonius.

6. Open WMI Management (wmimgmt.msc). Under **Security**, select **Root (minimal: root/cimv2)** namespace.

7. Click **Security**. Add the local user.

8. Click **Advanced**.

9. From the **Applies to** dropdown, select **This namespace and subnamespaces**.

10. Under the **Allow** column for the local user, select the **Execute Methods**, **Enable Account**, and **Remote Enable** options, and then click **OK**.

11. In Axonius, verify that the **Custom Share Name** and **Custom Files Directory** parameters are configured. The adapter will attempt to create the specified directory under the share.

12. If the above step fails, it means some sharing options are not enabled on the server. In such a case, add the full path to the share under **Custom Working Directory**.

**Note:** When using Custom Working Directory, this directory must be identical to all WSUS adapter connections, and needs to be specified in all adapter connections, even if using a local admin. Only use this option as a last resort.

## Required Permissions

The value supplied in [**User Name** and **Password**](#parameters) must be able to execute PowerShell code which queries the WSUS server for information on the systems managed by that server.
The supplied [**User Name**](#parameters) must have the following permissions:

* Local admin permissions.
* Access RPC on the WSUS server.
* Execute PowerShell on the WSUS server and access the IPC$ share on the WSUS server.
* Read and Write Access to ADMIN$ share on the WSUS server. Alternatively, create an 'axonius' folder inside the \localhost\ADMIN$\ directory and ensure the Axonius account has Full Permissions to read and write to this newly created folder.