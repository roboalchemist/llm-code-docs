# Source: https://docs.axonius.com/docs/microsoft-hyper-v.md

# Microsoft Hyper-V

Microsoft Hyper-V is a native hypervisor; it can create virtual machines on x86-64 systems running Windows.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name** *(required)* - The hostname or IP address of the Hyper-V server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Microsoft Hyper-V.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Microsoft%20Hyper-V.png)

## Required Ports

* The instance must be able to interact with the Hyper-V host:
  * 135 (RPC)
  * 445 (SMB)
  * Random port in the range 1024-65535

### Setting up a fixed port for WMI

WMI runs as part of a shared service host with ports assigned through DCOM by default. However, you can set up the WMI service to run as the only process in a separate host and specify a fixed port. Refer to [Setting up a fixed port for WMI](/docs/wmi#setting-up-a-fixed-port-for-wmi) for details of how to do this.

## Required Permissions

* The value supplied in [**User Name** and **Password**](#parameters) must be able to execute PowerShell code which queries the Hyper-V server for information on the systems managed by that server.
* The supplied [**User Name**](#parameters) must be added to the local “Hyper-V Administrators” group on each Hyper-V Hypervisor.
* The supplied [**User Name**](#parameters) must have the following permissions:
  * Execute PowerShell on the Hyper-V server and access the IPC$ share on the WSUS server.
  * Access ADMIN$ share on the Hyper-V server (preferred permissions).