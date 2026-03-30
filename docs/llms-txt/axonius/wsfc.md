# Source: https://docs.axonius.com/docs/wsfc.md

# Windows Server Failover Clustering (WSFC)

Windows Server Failover Clustering (WSFC) is a feature of the Windows Server platform for improving the high availability (HA) of applications and services. WSFC is the successor to Microsoft Cluster Service (MSCS).

<Callout icon="📘" theme="info">
  NOTE

  See also [How to set up and manage a Hyper-V Failover Cluster, Step by step](https://www.altaro.com/hyper-v/failover-cluster-manager/).
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Failover Cluster Domain** *(required)* - The hostname or IP address of the Windows Server Failover Clustering (WSFC) server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Failover Cluster Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#/ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Failover Cluster Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Failover Cluster Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Failover Cluster Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Failover Cluster Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Failover Cluster Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1472).png" />

## Required Ports

* 135(RPC)
* 445 (SMB)
* Random port in the range 1024-65535

### Setting up a fixed port for WMI

The WSFC adapter uses WMI.
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

## Required Permissions

The value supplied in [**User Name** and **Password**](#parameters) must be able to execute PowerShell code which queries the WSFC server for information on the systems managed by that server.
The supplied [**User Name**](#parameters) must have the following permissions:

* Access RPC on the WSFC server.
* Execute PowerShell on the WSFC server and access the IPC$ share on the WSFC server.
* Access ADMIN$ share on the WSFC server (preferred permissions).
* RSAT-Clustering-PowerShell must be installed on each system to be queried.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                              | Supported | Notes |
| ---------------------------------------------------- | --------- | ----- |
| Windows Server 2012 R2, Windows Server 2012 or newer | Yes       |       |