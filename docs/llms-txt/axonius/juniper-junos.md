# Source: https://docs.axonius.com/docs/juniper-junos.md

# Juniper Junos

Juniper Junos connects to Juniper switches and routers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Network/Firewall Rules, Network Routes

## Parameters

### Required Parameters

1. **Host Name** *(required)* - The host name of the Juniper Junos server.
2. **User Name** and **Password** - The user name and the password of a read-only user.
3. **Protocol Port** - Specify if the connection needs to be on a non-standard port.
4. **SSH Configurations File** - Provides the ability to use a custom SSH config file.
5. **Disable RPC** - Select this option to disable the RPC (Remote Procedure Call) client and use SNMP only for data collection. This provides flexibility for environments where RPC access is restricted or unavailable, while still maintaining device visibility through SNMP. Enable this setting when:
   * RPC access to Juniper devices is restricted or unavailable in your environment
   * You want to rely exclusively on SNMP for data collection
   * Security policies prevent RPC connections to network devices
     Important: When Disable RPC is enabled, SNMP must be properly configured. The adapter will validate that SNMP is enabled and working before proceeding. If SNMP is not configured or fails to connect, the adapter will return an error.

### Optional Parameters

1. **Add additional SNMP Connection** *(default: No)* - Select **Yes** to add SNMP-based authentication to the connection. When you enable this option, the following fields appear:
   1. **SNMP User Name**
   2. **SNMP Version** - Select a version from the list.
   3. **SNMP Port** - The default is 161.
   4. **SNMPv3 Authentication Type (authProtocol)** - Select from the menu.
   5. **SNMPv3 Privacy Type (privProtocol)** - Select from the menu.
   6. **SNMPv3 Security Level (level)** - Select from the menu.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![screenshot of Juniper Junos connection screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/JuniperJunos_AddConnection.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Firewalls** - Select this option to fetch firewalls.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />