# Source: https://docs.axonius.com/docs/cisco.md

# Cisco

Cisco connects to Cisco switches and routers.  A separate connection entry is required for each switch that is being queried.

<Callout icon="📘" theme="info">
  Note

  The Cisco adapter supports Cisco Routers, Switches and Wireless Controllers leveraging IOS (Internetwork Operating System), and IOS-XE.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## &#x20;Selecting the Protocol to Use

The Cisco adapter supports multiple connection protocols. **You must choose ONE protocol per connection.** Different protocols fetch different types of data and have different requirements.

## Available Protocols

The Cisco adapter provides the following protocol options in the **Protocol** dropdown:

1. **SNMP** (SNMPv1) — Default, recommended for best performance
2. **SNMPv2** (SNMPv2c)
3. **SNMPv3**
4. **SNMPv3 with Fallback**
5. **SSH**
6. **Telnet**

***

## Protocol Comparison

<Tabs>
  <Tab title="SNMP Protocols (SNMP, SNMPv2, SNMPv3)">
    **Recommended for:** Network infrastructure discovery, switch port mapping, and best performance

    **What SNMP Fetches:**

    * **Devices** — Network devices (switches, routers, access points)
    * **Switch port information** — Port status, VLANs, port security
    * **Network topology** — CDP/LLDP neighbor data
    * **MAC address tables** — Connected device MAC addresses
    * **ARP tables** — IP-to-MAC mappings (when "Fetch ARP data" is enabled)
    * **Interface statistics** — Port utilization, errors
    * **VLAN information** — VLAN assignments and configurations

    **Requirements:**

    * **Port:** TCP 161 (SNMP)
    * **Credentials:**
      * **SNMP/SNMPv2:** SNMP Read Community string
      * **SNMPv3:** Username, Authentication Passphrase, Privacy Passphrase, Security Level, Auth Protocol, Priv Protocol

    **Advantages:**

    * **Fastest performance** — Optimized for bulk data collection
    * **Best for network discovery** — Fetches comprehensive switch port and topology data
    * **Lower resource impact** — Minimal load on network devices

    **Limitations:**

    * **Does not fetch detailed device configurations** — Limited to SNMP MIB data
    * **May fetch fewer total devices** — Focuses on network infrastructure rather than end devices
  </Tab>

  <Tab title="SSH Protocol">
    **Recommended for:** Detailed device configuration retrieval, Cisco IOS command execution

    **What SSH Fetches:**

    * **Devices** — Network devices accessible via SSH
    * **Detailed device configurations** — Running configurations, startup configurations
    * **Command output** — Results from Cisco IOS commands (show commands)
    * **Software versions** — Detailed IOS/firmware information
    * **Hardware inventory** — Module and component details

    **Requirements:**

    * **Port:** TCP 22 (SSH)
    * **Credentials:** Console username and password with appropriate privilege level

    **Advantages:**

    * **May fetch more total devices** — Can discover devices through command output (e.g., `show cdp neighbors`)
    * **Detailed configuration data** — Access to full device configurations
    * **Flexible command execution** — Can run custom show commands
    * **Supports MAC table entries** — Critical for discovering connected devices

    **Limitations:**

    * **Slower performance** — Sequential command execution takes longer than SNMP bulk queries
    * **Higher resource impact** — SSH sessions consume more device resources
    * **Requires console access** — Needs appropriate privilege level (typically privilege 15)
  </Tab>

  <Tab title=" Telnet Protocol">
    **Recommended for:** Legacy devices that do not support SSH

    **What Telnet Fetches:**

    * Similar to SSH (see above)

    **Requirements:**

    * **Port:** TCP 23 (Telnet)
    * **Credentials:** Console username and password

    **Security Warning:**

    * **Unencrypted protocol** — Credentials and data transmitted in clear text
      * **Use only when SSH is not available**
  </Tab>
</Tabs>

### Choosing the Right Protocol

<Tabs>
  <Tab title="SNMP">
    **Use SNMP (Recommended) when**:

    * You need **comprehensive network topology and switch port data**
    * You want **best performance and lowest resource impact**
    * You need to discover **devices connected to switch ports** (via MAC tables)
    * You are performing **network infrastructure discovery**
  </Tab>

  <Tab title="SSH">
    **Use SSH when**:

    * You need **detailed device configurations**
    * You want to **execute custom Cisco IOS commands**
    * You need **detailed hardware and software inventory**
    * SNMP is not available or restricted
  </Tab>

  <Tab title=" SNMPv3">
    **Use SNMPv3 when:**

    * You require **encrypted SNMP communication**
    * Your security policy mandates **authenticated and encrypted management protocols**
  </Tab>

  <Tab title="Telnet">
    **Use Telnet when**:

    * **SSH is not available** on legacy devices
    * **Only as a last resort** due to security concerns
  </Tab>
</Tabs>

<br />

<br />

<Callout icon="📘" theme="info">
  **Important Notes:**

  1. **One Protocol Per Connection:** Each connection uses **only one protocol**. You cannot combine protocols in a single connection.
  2. **Different Data Sets:** SNMP and SSH fetch **different types of data**. The same host configured with both protocols may return different device counts and data.
  3. **Multiple Connections Recommended:** For comprehensive coverage, create **two separate connections** to the same host:
     * **Connection 1:** SNMP (for network topology and switch ports)
     * **Connection 2:** SSH (for detailed configurations)
  4. **Performance Considerations:**
     * **SNMP** is significantly faster for bulk network discovery
     * **SSH** is slower but provides richer configuration data
</Callout>

***

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Cisco, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

**Host Name** - The hostname or IP address of the Cisco server.

1. **Protocol** *(default: SNMP)* - Select the desired protocol from the dropdown. The **SNMP** option refers to SNMPv2c.
   It is highly recommended to use SNMP for best network performance and to utilize the available adapter functionalities.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco.png)

<br />

### Optional Parameters

1. **User Name** and **Password** *(optional)* - The user name and password for the switch, if required.
2. **SNMP Read Community**   - Specify the SNMP read community string, if using SNMP.
3. **SNMPv3 Authentication Passphrase (authKey)**  -  Specify the user authentication key passphrase (authKey), if using SNMPv3.
4. **SNMPv3 Private Passphrase (privKey)**  - Select the user private key passphrase (privKey), if using SNMPv3.
5. **SNMPv3 Authentication Type (authProtocol)** *(default: hmac\_md5)* - Select the authentication type (authProtocol), if using SNMPv3.
6. **SNMPv3 Privacy Type (privProtocol)** *(default: aescfb128)* - Select the privacy type (privProtocol), if using SNMPv3.
7. **SNMPv3 Security Level (level)** *(optional, default: authPriv)* - Select the security level (level), if using SNMPv3.
8. **Protocol Port**  - Specify if the connection needs to be on a non-standard port.
9. **Description** - Enter a description for the connection.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch ARP data** *(required, default: true)* - Select to fetch ARP data from the Cisco server.
2. **SNMP timeout** - Specify the number of seconds that SNMP requests should wait for a response before timing out. If left empty, the default value is 15 seconds.
3. **Create assets from connected devices** - Select this option to fetch all connected devices with data from SNMP.
4. **Create assets from port security data** - Select this option to add all connected devices from the port security entities as assets with the same fields  as in **Create assets from connected devices**.
5. **Create assets from stacked switches** - Select this option to fetch each switch in the switch stack as a separate device.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

<br />

<br />