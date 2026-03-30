# Bluetooth Mesh Profile v1.1 Specification

This directory contains comprehensive documentation for the **Bluetooth Mesh Profile v1.1** specification from the Bluetooth Special Interest Group (SIG).

## About Bluetooth Mesh

Bluetooth Mesh is a standardized mesh networking protocol designed specifically for Internet of Things (IoT) and smart home applications. Unlike traditional point-to-point Bluetooth connections, mesh topology enables:

- **Many-to-many communication:** Messages can travel through multiple hops via relay nodes
- **Extended range:** Network coverage extends beyond direct radio range of individual devices
- **Reliability:** Flooding-based message delivery with multiple paths
- **Low power:** Designed to support battery-powered devices through friendship mode
- **Scalability:** Support for thousands of devices in a single mesh network
- **Interoperability:** Standard models and interfaces ensure device compatibility

## Document Contents

### Main Files

- **index.md** - Complete Bluetooth Mesh Profile specification covering:

  **Architecture & Layers:**
  - Model Layer - Application behaviors and capabilities
  - Foundation Model Layer - Standard mesh functions
  - Access Layer - Application data encryption
  - Upper & Lower Transport Layers - Message fragmentation and delivery
  - Network Layer - Message routing and relaying
  - Bearer Layer - BLE physical transmission

  **Core Concepts:**
  - Mesh network topology and principles
  - Device provisioning and onboarding
  - Security architecture and encryption
  - Message types (unicast, group, broadcast)
  - Relay and multi-hop forwarding
  - Friendship for low-power devices

  **Advanced Topics:**
  - Foundation models (Config, Health, OnOff, Level, etc.)
  - Lighting and HVAC control models
  - Sensor data models
  - Proxy protocol for gateway functionality
  - Beacons and network administration
  - Configuration and management procedures

## Key Technical Concepts

### Provisioning

The process of securely adding devices to a mesh network:

- Out-of-band authentication
- Capability exchange
- Network key distribution
- Unique address assignment
- Device key establishment

### Security Model

Multi-layer security architecture:

- **Network Layer:** NetKey protects all mesh messages
- **Application Layer:** AppKey encrypts application-specific data
- **Device Layer:** DevKey enables secure device-to-device communication
- **Encryption:** AES-CCM with 128-bit keys
- **Authentication:** MIC (Message Integrity Check) on all messages

### Message Types

- **Unicast messages:** Sent to specific device addresses
- **Group messages:** Sent to group addresses with multiple recipients
- **Virtual addresses:** Logical address sets for complex group structures
- **All-nodes messages:** Broadcast to entire network

### Network Operation

- **Flooding:** Messages propagated through network via relay nodes
- **Relay:** Devices forward messages to extend range
- **TTL (Time To Live):** Controls message propagation depth
- **Friendship:** Low-power mode with friend node proxy delivery

## Device Roles

### Full Node

- Maintains full mesh functionality
- Processes all incoming messages
- Participates in relay
- Typically always-on devices

### Relay Node

- Forwards messages from other devices
- Extends network coverage
- Combines full node features

### Low Power Node (LPN)

- Battery-optimized operation
- Maintains friendship with friend node
- Reduced radio activity
- Stores messages from friend node

### Friend Node

- Collects messages for associated LPN devices
- Maintains friendship relationship
- Stores buffered messages

### Proxy Node

- Gateway functionality
- Connects non-mesh devices to mesh network
- Bridges between mesh and other transports (BLE, GATT)

## Foundation Models

Standard device models implemented by most mesh devices:

- **Configuration Server** - Device configuration and network management
- **Configuration Client** - Network administration tools
- **Health Server** - Device health monitoring and diagnostics
- **Health Client** - Query device health status
- **Generic OnOff** - Standard on/off control
- **Generic Level** - Numeric level control (brightness, temperature, etc.)
- **Generic Default Transition Time** - Default transition durations
- **Generic OnPowerUp** - Behavior when powered on
- **Lighting Lightness** - Brightness control
- **Lighting Color Control** - Color and color temperature control
- **Sensor Models** - Environmental sensors and data publishing
- **Time and Scene** - Scheduling and scene management

## Standards and Conformance

This specification defines:

1. **Mandatory Requirements** - Must be implemented by all devices
2. **Optional Features** - Implementation choices for specific use cases
3. **Conditional Requirements** - Depend on device capabilities
4. **Foundation Models** - Standard behaviors for interoperability

## Message Flow Example

```text
Application Model
       ↓
Access Layer (AppKey encryption)
       ↓
Upper Transport (Segmentation, SAR)
       ↓
Lower Transport (Network Segment Assembly)
       ↓
Network Layer (NetKey encryption, relay)
       ↓
Bearer Layer (BLE Advertisement Channels)
```

## Use Cases

### Smart Lighting

- Large installation lighting control
- Scene management
- Color and brightness control
- Automated scheduling

### Building Automation

- HVAC control
- Environmental monitoring
- Energy management
- Access control integration

### Industrial IoT

- Asset tracking
- Sensor networks
- Predictive maintenance
- Remote monitoring

### Smart Home

- Device coordination
- Home automation scenes
- Multi-room systems
- Integration with other protocols

## Related Specifications

- **Bluetooth Core Specification** - Foundation for all Bluetooth technologies
- **Bluetooth Low Energy** - Physical/link layer basis for mesh
- **OpenThread** - Alternative mesh protocol (IEEE 802.15.4)
- **Matter** - IoT application layer protocol
- **Zigbee** - Alternative mesh networking standard
- **Z-Wave** - Proprietary mesh protocol
- **Thread** - IPv6 mesh for IoT

## Implementation References

When implementing Bluetooth Mesh:

1. **Network Setup:** Follow provisioning procedures for new device onboarding
2. **Security:** Implement all required encryption and authentication
3. **Addressing:** Understand unicast, group, and virtual address usage
4. **Models:** Implement appropriate foundation and application models
5. **Transport:** Handle segmentation and reassembly correctly
6. **Relay:** Configure relay parameters for network coverage
7. **Power Management:** Optimize for target device power budget

## Specification Versions

- **v1.0** - Initial Bluetooth Mesh specification
- **v1.0.1** - Clarifications and corrections
- **v1.1** - This specification - Enhanced features and refinements

## Additional Resources

### Official Bluetooth SIG

- **Website:** https://www.bluetooth.com/
- **Specifications:** https://www.bluetooth.com/specifications/specs/
- **Documentation:** https://www.bluetooth.com/specifications/specs/html/

### Typical File Size

- Specification content: ~500KB-1MB when converted to markdown
- Implementation guides often significantly longer (specifications + examples)

### Format Notes

- Original format: HTML with DocBook structure
- Converted to: GitHub-flavored Markdown
- All section hierarchies preserved
- Cross-references maintained where possible
- Tables converted to markdown table format

## Document Maintenance

This markdown version is a conversion from the original Bluetooth SIG HTML specification for easier:

- Integration with documentation systems
- Version control tracking
- Content searching and analysis
- Integration with developer tools
- Offline access and reading

Always refer to the official Bluetooth SIG specification for authoritative technical details in production implementations.

---

**Conversion Date:** 2026-03-07
**Original Format:** HTML (Docbook)
**Source:** https://www.bluetooth.com/specifications/specs/html/
**Copyright:** Bluetooth SIG - All rights reserved
