# Source: https://docs.axonius.com/docs/cisco-ucs-manager.md

# Cisco UCS Manager

Cisco UCS Manager supports the entire Cisco UCS server and Cisco HyperFlex Series hyperconverged infrastructure portfolios. It enables server, fabric, and storage provisioning as well as device discovery, inventory, configuration, diagnostics, monitoring, fault detection, auditing, and statistics collection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Adapter Parameters

1. **Cisco UCSM IP** *(required)* - The Cisco UCS Manager server IP address.
2. **Cisco UCSM Port** *(optional)* - Optional port.
3. **User Name** and **Password** *(required)* - The user name and password for an account that has read access to the Cisco UCS Manager.
4. **Secure Connection Supported** *(optional)* - Select whether to use a secure connection when communicating with the Cisco UCS Manager server.
5. **Proxy** *(optional)* - A proxy to use when connecting to **Cisco UCSM IP**.

<Image alt="CiscoUCS manager.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoUCS%20manager.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Equipment Chassis** *(optional)* - Select whether to fetch chassis equipment information as devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>