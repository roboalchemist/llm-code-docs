# Source: https://docs.axonius.com/docs/sccm-vmm.md

# Microsoft System Center Virtual Machine Manager

Microsoft System Center Virtual Machine Manager (VMM) is a unified management application for on-premises, service provider, and Azure cloud virtual machines.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: empty)* - The hostname or IP address of the Microsoft System Center VMM server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Proxy Host Name or IP Address** *(optional, default: empty)* - Provide a proxy server to connect the adapter to instead of directly to the SCVMM server. This is useful in some cases, for example, when the SCVMM server is a cluster, and then the adapter can't connect directly to it with WMI. In this case, you can connect to a proxy server and the proxy server will pass the commands to the SCVMM server.

3. **Port** *(required, default: 8100)* - The port used for the connection.

4. **User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address**.

5. **Password** *(optional, default: empty)* - The password to use when connecting to the server.

6. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image border={false} src="https://files.readme.io/8b4efbfb5d256e955b0dddb18036d2cd80d9f6959a479261eb85546896202b73-image.png" />

## APIs

Axonius uses the [Virtual Machine Manager API documentation](https://docs.microsoft.com/en-us/system-center/vmm/?view=sc-vmm-2019).

## Required Permissions

* The value supplied in [User Name](#parameters) must have  log on as a service permission on the VMM server to fetch assets.
* The user must have read-write access to the IPC$ and admin$ SMB shares to extract device data.

## Required Ports

* 135(RPC)
* 445 (SMB)
* 8100 (or other customer designated TCP port for REST API)
* Random port in the range 1024-65535

### Setting up a fixed port for WMI

The Microsoft System Center VMM adapter uses WMI.
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

## Supported From Version

Supported from Axonius version 4.5