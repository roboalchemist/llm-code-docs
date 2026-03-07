# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-4/01-including-thread-1-4-features-in-soc-applications.md

# Including Thread 1.4 features in SoC Applications

Silicon Labs provides a number of sample SoC OpenThread applications. You can modify these to include Thread 1.4 features (most of which are enabled by default). This chapter assumes you are familiar with creating and modifying OpenThread projects in Simplicity Studio. If you need more information, see the Simplicity Studio and the [OpenThread Quick Start Guide](/openthread/{build-docspace-version}/openthread-quick-start-guide).

As an example, the following procedure shows how to configure 1.4 features:

1. Create a project based on the example: **OpenThread – SoC CLI (FTD)**.
2. On the **SOFTWARE COMPONENTS** tab, search for and select the **Stack (FTD)** entry. Depending on your application, you may have to do this on a **Stack (MTD)** or **Stack (RCP)** component (this example is for an FTD application).  
   ![software components](/configuring-openthread-apps-for-thread-1-4/0.1/images/sld863-image1.png)
3. In the stack component, make sure to configure the **Thread Stack Protocol Version** to 1.4.  
   ![Thread Stack Protocol Version](/configuring-openthread-apps-for-thread-1-4/0.1/images/sld863-image2.png)

The following are border router features defined in the 1.4 specification of the Thread standard. The OpenThread stack allows configuration of these features for any Thread stack protocol version and on any router. However, a Thread 1.4 compliant border router device must enable these features.

- Ephemeral Key (ePSKc) support for Credential Sharing  
  - Mandatory and applicable to border routers only
- Extended Mesh Diagnostics  
  - Mandatory for border routers  
  - Can also be enabled on any router capable device
- DHCPv6 Prefix Delegation support  
  - Mandatory and applicable to border routers only

**There is one exception that is omitted from configuration**:

- Thread Commissioning over Authenticated TLS (TCAT over Bluetooth)  
  - Optional as a commercial feature, and not required for Thread 1.4 certification

Additional information about these features is included in the following table.

<table>
    <thead>
        <tr>
            <th>Flag</th>
            <th>Note</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Ephemeral Key for Credential Sharing(OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE) </td>
            <td> Enables setting an ephemeral PSKc to allow a commissioner (from a different network or ecosystem for example) to establish a secure connection with a border router. Once a connection is established with an ePSKc, the commissioner can set or program a different network active dataset, thus allowing multiple Thread networks to form a single, larger ranging mesh.<br><br> This feature is only meant for devices with a border agent, such as a Thread border router. <br><br> For more information, see: <br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README.md#ba-ephemeralkey">https://github.com/openthread/openthread/blob/main/src/cli/README.md#ba-ephemeralkey</a>
            </td>
        </tr>
        <tr>
            <td> Mesh Diagnostics (OPENTHREAD_CONFIG_MESH_DIAG_ENABLE) </td>
            <td> Allow sending diagnostic requests and queries to other nodes and process the responses. Includes support for enhanced network diagnostics in Thread 1.4 to enable better insight into network topology and neighbor links, helping one visualize network state. <br><br> For more information, see commands starting at: <br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README.md#meshdiag-topology-ip6-addrs-children">https://github.com/openthread/openthread/blob/main/src/cli/README.md#meshdiag-topology-ip6-addrs-children</a>
            </td>
        </tr>
        <tr>
            <td> DHCP6 PD feature(OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE) </td>
            <td> Supports handling platform generated ND messages. The prefix can be allocated by other software on the interface, which will advertise the assigned prefix to the thread interface via router advertisement messages. </td>
        </tr>
        <tr>
            <td> Thread Commissioning over Authenticated TLS (implemented over Bluetooth) (OPENTHREAD_CONFIG_BLE_TCAT_ENABLE) </td>
            <td> This is an optional feature meant only for commercial networks. <br><br> To read more about Thread Commissioning at Scale, see example client at: <br>
                <a href="https://github.com/openthread/openthread/tree/main/tools/tcat_ble_client">https://github.com/openthread/openthread/tree/main/tools/tcat_ble_client</a>
            </td>
        </tr>
    </tbody>
</table>