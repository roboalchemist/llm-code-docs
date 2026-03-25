# Source: https://docs.axonius.com/docs/pdq-inventory.md

# PDQ Inventory

PDQ Inventory is a systems management tool that scans Windows computers to collect hardware, software, and Windows configuration data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

The adapter parameters are as same as the [SQLite](https://docs.axonius.com/docs/sqlite) adapter, which are also as same as the [CSV Legacy Remote File adapter parameters](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the PDQ Inventory adapter configuration.
In addition for the following parameters, note:
**File Name** -  Should contain the PDQ DB filename (i.e. database.db)
**Path to Resource** - Should contain the full network path with appended filename (\xxx.xxx.xxx.xxx\PDQ\database.db)

The functionality of this adapter is as same as the [SQLite](https://docs.axonius.com/docs/sqlite) adapter.

## Required Ports

* 135 (RPC)
* 445 (SMB)
* Random port in the range 1024-65535

### Setting up a fixed port for WMI

The PDQ Inventory adapter uses WMI.
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

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control on the performance of all connections of for this adapter.
2. **Do not fetch devices without a MAC address** *(optional)* - Select to avoid fetching devices that lack MAC address information.
3. **Tables to fetch** *(required, default: LocalGroups, LocalGroupMembers, Applications)* - Select one or more tables to enrich the device's information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>