# Source: https://docs.axonius.com/docs/adcs.md

# Active Directory Certificate Service (AD CS)

Active Directory Certificate Services (AD CS) is a Windows Server feature that allows you to build and manage PKI certificates used in software security systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **Authentication** - Select Authentication method, either **NTLM** (default) or **Kerberos**. If you select Kerberos, the following optional fields for authentication may be configured:
   * **Kerberos AES Key** *(optional)* - A cryptographic key, either 128 or 256 bits in length, used to secure communication by encrypting and decrypting messages exchanged between the client and the server.
   * **Kerberos Host (KDC)** *(optional)* - The Kerberos Key Distribution Center (KDC) that will be used to authenticate. If this parameter is not specified, the domain will be used.

2. **ADCS Server** *(required)* - The hostname of the domain controller with the ADCS service.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to execute PowerShell code which queries the ADCS server for information on the systems managed by that server. When using Kerberos the user name must be in the format `username/domain/realm`

4. **Custom Share Name** *(optional)* - The name of the Windows Share on the specified host, for example, `AxoniusShare$`. If you do not specify a name, the adapter will use `Admin$`. For more information, see [Creating a Custom Share](/docs/windows-server-update-services-wsus#creating-a-custom-share).

5. **Custom Files Directory** *(optional)* - The name of the directory to use within the specified Share, for example, `AxoniusDirectory`. If you do not specify a name, the adapter will use `axonius`.

6. **Custom Working Directory** *(optional)* - If file sharing is restricted in the domain, specify the physical path of the share specified in **Custom Share Name**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Active Directory Certificate Service (AD CS)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Active%20Directory%20Certificate%20Service%20(AD%20CS).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Filter Certificates By Template (semi-colon separated)** - Enter a semicolon-separated list of templates to exclude from the fetch.
2. **Filter Certificates by Expiration Date in the next X days** - Specify a numerical value to set a future expiration date to filter certificates by.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Certutil module](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **135 (RPC)**
* **445 (SMB)**
* **Random port in the range 1024-65535**

### Setting up a fixed port for WMI

The Active Directory Federation Service (AD CS) adapter uses WMI.
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
netsh advfirewall firewall add portopening TCP 24158 WMIFixedPort
```

<Callout icon="📘" theme="info">
  Note

  If you are running an old Windows Server version, it might need to run the deprecated command version (`netsh firewall`).
</Callout>

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

   * Distributed COM Users
   * Remote Management Users

3. Create a directory for Axonius to use to store temporary files and to serve as a working directory, for example: C:\axonius
   The name of this directory may be used later in the adapter configuration for AD CS in Axonius.

4. Grant the following permissions to the local user:

   * Read
   * Write
   * Modify
   * Execute (or full control) permissions on the custom directory, subdirectories, and files

5. Share the directory that you created by using Sharing or Advanced Sharing. Verify that the local user has full permissions for this share. Specify a descriptive name for the shared directory, preferably a name which ends with a dollar-sign, such as: AxoniusShare$
   The name of this share will be used later in the adapter configuration for AD CS in Axonius.

6. Open WMI Management (wmimgmt.msc). Under **Security**, select **Root (minimal: root/cimv2)** namespace.

7. Click **Security**. Add the local user.

8. Click **Advanced**.

9. From the **Applies to** dropdown, select **This namespace and subnamespaces**.

10. Under the **Allow** column for the local user, select the **Execute Methods**, **Enable Account**, and **Remote Enable** options, and then click **OK**.

11. In Axonius, verify that the **Custom Share Name** and **Custom Files Directory** parameters are configured. The adapter will attempt to create the specified directory under the share.

12. If the above step fails, it means some sharing options are not enabled on the server. In such a case, add the full path to the share under **Custom Working Directory**.

**Note:** When using Custom Working Directory, this directory must be identical to all Active Directory Federation Service (AD CS) adapter connections, and needs to be specified in all adapter connections, even if using a local admin. Only use this option as a last resort.

## Required Permissions

The value supplied in [User Name and Password](#parameters) must be able to execute PowerShell code which queries the ADCS server for information on the systems managed by that server. The configured user must have permission to run the following PowerShell commands:

* (Get-Service -Name CertSvc).Status
* certutil -view csv

The configured user must have Read permission in the Certificate Authority.
To enable this permission:

1. Open the **Certification Authority** management console (certsrv.msc).
2. Right-click the CA name and select **Properties**.
3. Click the **Security** tab.
4. Check the user or group that requires access.
5. Ensure that the Read permission is enabled.

The value supplied in [User Name and Password](#parameters) must have the following permissions in order to fetch assets:

* Local admin permissions.
* Access RPC on the ADCS server.
* Execute PowerShell on the ADCS server and access the IPC$ share on the ADCS server.
* Read and Write Access to ADMIN$ share on the ADCS server. Alternatively, create an 'axonius' folder inside the \localhost\ADMIN$\ directory and ensure the Axonius account has Full Permissions to read and write to this newly created folder.

## Supported From Version

Supported from Axonius version 6.1