# Bluetooth Mesh Profile v1.1

## Abstract

This Bluetooth specification defines fundamental requirements to enable an interoperable mesh networking solution for Bluetooth low energy wireless technology.

## Overview

The Bluetooth Mesh Profile specification defines the fundamental requirements for an interoperable mesh networking solution for Bluetooth Low Energy (BLE) technology. This specification covers the complete mesh protocol stack, including network architecture, provisioning, security, transport mechanisms, and model definitions.

## Table of Contents

1. 1. Introduction
2. 1.3. Language
3. 1.3.1. Language conventions
4. 1.4. Table conventions
5. 2. Mesh system architecture
6. 2.1. Layered architecture
7. 2.2. Overview of mesh operation
8. 2.3. Architectural concepts
9. 2.3.3. Messages
10. 2.3.10. Security
11. 3. Mesh networking
12. 3.1. Conventions
13. 3.1.1. Endianness and field ordering
14. 3.3. Bearers
15. 3.4. Network layer
16. 3.4.2. Addresses
17. 3.4.4. Network PDU
18. 3.4.5. Network interfaces
19. 3.4.6. Network layer behavior
20. 3.5. Lower transport layer
21. 3.5.2. Lower Transport PDU
22. 3.5.3. Segmentation and reassembly
23. 3.5.4. Lower transport layer behavior
24. 3.6. Upper transport layer
25. 3.6.2. Upper Transport Access PDU
26. 3.6.4. Upper transport layer behavior
27. 3.6.5. Transport Control messages
28. 3.6.6. Friendship
29. 3.6.7. Heartbeat
30. 3.6.8. Directed forwarding
31. 3.7. Access layer
32. 3.7.2. Access message
33. 3.7.3. Access layer behavior
34. 3.7.4. Unacknowledged and acknowledged messages
35. 3.7.5. Publish and subscribe
36. 3.7.6. Example message sequence charts
37. 3.8. Model layer
38. 3.9. Mesh security
39. 3.9.2. Security toolbox
40. 3.9.5. Nonce

## Key Concepts and Architecture

### Mesh System Architecture

The Bluetooth Mesh system employs a layered architecture that separates concerns across multiple protocol layers:

- **Model Layer:** Defines application behaviors and device capabilities through standardized models
- **Foundation Model Layer:** Provides essential mesh functions like configuration and health monitoring
- **Access Layer:** Encrypts application data using encryption keys and manages device bindings
- **Upper Transport Layer:** Handles message segmentation, reassembly, and replay protection
- **Lower Transport Layer:** Manages network segment delivery across mesh nodes
- **Network Layer:** Routes messages through the mesh using flooding and relay mechanisms
- **Bearer Layer:** Provides physical transmission using BLE advertisement channels

### Provisioning

Provisioning is the secure process of adding devices to a Bluetooth Mesh network. It involves:

- Device discovery and selection
- Out-of-band authentication (optional)
- Network key and device key distribution
- Address assignment
- Security establishment between devices

### Security

Bluetooth Mesh implements multiple layers of security:

- **Network Security:** Network key (NetKey) protects all messages at the network layer
- **Application Security:** Application key (AppKey) encrypts application-level data
- **Device Security:** Device key (DevKey) enables secure device-to-device communication
- **Encryption:** AES-CCM encryption with 128-bit keys
- **Authentication:** Message authentication codes prevent tampering

### Message Types and Transmission

- **Unicast:** Point-to-point communication to a specific device
- **Group:** Messages sent to multiple devices in a group
- **Virtual Addresses:** Logical addresses for device groups
- **Broadcast:** Messages sent to all devices in the network

### Relay and Friendship

- **Relay:** Allows devices to forward messages to extend network range
- **Friendship:** Low-power mode for battery-constrained devices (LPN - Low Power Node)
- **Friend Node:** Collects messages for associated low power nodes

### Foundation Models

Foundation models provide standardized behaviors for common mesh functions:

- **Configuration Server:** Device configuration and management
- **Health Server:** Device health monitoring
- **Generic OnOff:** Standard on/off control model
- **Generic Level:** Level control for dimmers and similar devices
- **Lighting Models:** Color, brightness, and lighting control
- **Sensor Models:** Environmental and sensor data

### Proxy Protocol

The proxy protocol allows non-mesh devices (like smartphones) to communicate with mesh networks through a gateway device that implements proxy functionality.

## Detailed Specification Sections

### Note

Note: When factoring in a 32-bit MIC and the size of the hash, there is only a 1/246=1.42×10-14 likelihood that two matching virtual addresses using the same application key but different Label UUIDs will collide.

### Note

Note: The segment sizes are different for Upper Transport Access PDUs and Upper Transport Control PDUs.

Segmentation is performed by the lower transport layer of the transmitting node. The lower transport layer checks if an Upper Transport PDU fits into a single Lower Transport PDU. If the Upper Transport PDU fits, it is sent in a single Lower Transport PDU. If the Upper Transport PDU doesn’t fit, the lower transport layer divides the Upper Transport PDU into two or more Lower Transport PDUs.

Delivery of a segmented message is acknowledged by the lower transport layer of the receiving node. Delivery of an unsegmented message is not acknowledged. An Upper Transport PDU that fits into one Lower Transport PDU can be sent as a single-segment segmented message when acknowledgment by the lower transport layer is required.

Example: Using a single-segment segmented message can decrease the air traffic, for example, in a situation when a long multi-segment message (e.g., an Upper Transport PDU which was divided into many Lower Transport PDUs) has been transmitted, but the application acknowledgment message sent as a response to this multi-segment message was lost. Sending the application acknowledged message as a single segmented message can improve the reliability of delivery and can remove the risk associated with retransmitting the whole, long multi-segment message.

Each segment of an Upper Transport Access PDU shall be 12 octets long with the exception of the last segment, which may be shorter.

### Note

Note: The reception of a Segment Acknowledgment message with the OBO field set to 1 does not mean that the segmented message has been delivered to the final destination, but only that the segmented message has been delivered to the Friend of that Low Power node. The message is stored in the Friend Queue, but the message can be discarded if other messages are received for that Low Power node or the Friendship is terminated.

### Note

Note: An implementation may have to discard multiple messages to fit the new message into the Friend Queue.

If the message that is being stored is a Segment Acknowledgment message and the Friend Queue contains another Segment Acknowledgment message that has the same source and destination addresses, and the same SeqAuth value, but a lower IV Index or sequence number, then the older Segment Acknowledgment message shall be discarded.

When a Friend node becomes aware of a security update, for example by receiving a valid Secure Network beacon or a Mesh Private beacon, or as a result of a change in the Key Refresh Phase state, the Friend node shall add a Friend Update message to the Friend Queue.

When the Low Power node requests a message from the Friend Queue, the oldest entry shall be sent. Once that message has been acknowledged by the Low Power node, that entry shall be discarded.

If the Friend node is polled for a message from a Low Power node using a Friend Poll, and the Friend Queue for that node is empty, then the Friend node shall generate a new Friend Update message and add that message to the Friend Queue before sending the response, so that this Friend Update message can be sent in response to the Friend Poll message.

### Note

Note: Transport Control messages do not have a TransMIC field.

### Note

Note: The above requirement implies that a Low Power node should collect all stored messages at least once every 96 hours, otherwise the Friend node may discard the stored messages before the Low Power node can receive them.

Each message shall be sent after a minimum of ReceiveDelay milliseconds and before a maximum of the sum of ReceiveDelay and ReceiveWindow milliseconds, from the reception of the Friend Poll message from a friend Low Power node.

If no Friend Poll, Friend Subscription List Add, or Friend Subscription List Remove messages are received by the Friend node before the PollTimeout timer expires, the friendship is terminated and the Friend node shall discard all entries in the Friend Queue.

The Friend Subscription List Confirm message shall be sent after a minimum of ReceiveDelay milliseconds and before a maximum of the sum of ReceiveDelay and ReceiveWindow milliseconds, from the reception of the Friend Subscription List Add message or the Friend Subscription List Remove message.

In the Network PDU of a Friend Subscription List Confirm message, the TTL field shall be set to 0.

### Note

Note: If the message is received directly (for example, the InitTTL value and the received Network PDU TTL field value are the same), then the hops value would be 0x01. If the message has been delivered using the maximum length path, then InitTTL would be 0x7F and the received Network PDU TTL field value would be 0x01, and therefore hops would 0x7F.

If the hops value is lower than the Heartbeat Subscription Min Hops state, it shall be set as the new value of the Heartbeat Subscription Min Hops state. If the hops value is higher than the Heartbeat Subscription Max Hops state, it shall be set as the new value of the Heartbeat Subscription Max Hops state.

### Note

Note: A message with a fixed group address can be delivered to model instances on any element of the device, irrespective of any condition defined in Table 3.63, because the model subscription lists can contain one or more fixed group addresses.

all-directed-forwarding-nodes

Directed forwarding functionality is enabled

Proxy functionality is enabled

Friend functionality is enabled

### Note

Note: A message can be falsely identified as a valid message, passing the NetMIC and TransMIC fields authentication using a known network key and application key even though that message was sent using different keys. The decryption of that message using the wrong keys would result in a message that is not understood by the element. The probability of such a situation occurring is small but not insignificant.

A message that is not understood includes messages that have one or more of the following conditions:

The opcode field of the Access message is unknown by the receiving element.

The Access message size for the identified opcode is incorrect.

The parameters field of the Access message contains values that are Prohibited.

### Note

Note: A model is, in effect, always subscribed to its element unicast address as described in Section 3.7.3.2.

### Note

Note: A description of the CCM algorithm can also be found in the NIST Special Publication 800-38C [29].

This specification defines AES-CCM as a function that takes four inputs and results in two outputs.

The inputs to AES-CCM are:

m is the variable-length data to be encrypted and authenticated – also known as “plaintext”

a is the variable-length data to be authenticated – also known as “Additional Data”

### Note

Note: There are up to 2121 possible keys for each NID; therefore, the NID value can only provide an indication of the security material that has been used to secure this Network PDU.

The NID, EncryptionKey, and PrivacyKey are derived using the k2 function with security credentials as inputs.

The managed flooding security material is derived from the managed flooding security credentials using the following formula:

NID || EncryptionKey || PrivacyKey=k2(NetKey, 0x00)

The friendship security material is derived from the friendship security credentials using the following formula:

### Note

Note: The authentication and encryption of the Access message is not dependent on the TTL field value, meaning that as the Access message is relayed through a mesh network, the Access message does not need to be re-encrypted at each hop.

When using an application key and the destination address is a virtual address:

EncAccessMessage, TransMIC=AES-CCMAppKey (application nonce, Access message, Label UUID)

When using an application key and the destination address is a unicast address or a group address:

EncAccessMessage, TransMIC=AES-CCMAppKey (application nonce, Access message)

### Note

Note: The Configuration Manager’s device key is used only when another Configuration Manager is interacting with server models that require using the device key for the access layer security.

### Note

Note: The Mesh Proxy Service advertising depends on the NetKey value and will be updated upon transition from Phase 1 (see Section 7.2.2.2.1).

### Note

Note: When a device has been recently provisioned and does not have the old keys, it will not know the old keys and therefore will not be able to revoke the old keys.

A Relay node or Friend node, when it is in Phase 3 for a given NetKey, shall send Secure Network beacons or Mesh Private beacons for the new NetKey with the Key Refresh Flag set to 0.

Upon receiving a Secure Network beacon or a Mesh Private beacon or a Friend Update message with the Key Refresh Flag set to 0 or a Config Key Refresh Phase Set message with the Transition parameter set to 0x03, the node shall revoke the old keys and shall send Secure Network beacons or Mesh Private beacons for the new NetKey with the Key Refresh Flag set to 0. The node will only transmit and receive using the new keys. It shall ignore Secure Network beacons, Mesh Private beacons, and Friend Update messages secured using the new NetKey with the Key Refresh Flag set to 1. After old keys are revoked, the Key Refresh state will be 0.

The Configuration Manager should be aware that Low Power nodes may have a very high latency, and therefore Low Power nodes may take additional time to receive the Key Refresh Flag information from a Friend node.

### Note

Note: Nodes that send messages less frequently are less likely to initiate the IV Update procedure.

On a subnet with a key index different from 0x000, at least one node shall meet all of the following conditions:

Either the Secure Network Beacon state is set to 1 or the Private Beacon state is set to Enable (0x01).

The node is a member of the primary subnet.

The node is receiving Secure Network beacons or Mesh Private beacons on the primary subnet.

### Note

Note: If the Publish TTL state is set to 1, the outgoing messages are published to local elements only, as defined in Section 3.4.5.

### Note

Note: If the Heartbeat Publication Destination is set to the unassigned address, the Heartbeat messages are not being sent.

### Note

Note: It is possible to read all supported Composition Data Pages by reading 0xFF first, and then reading one less than the returned page number until the page number is 0x00.

### Note

Note: When an element receives a Config NetKey Add message that identifies a NetKey that has already been added to the NetKey List, it responds with Success, because the result of adding the key again, with the same NetKey value, using the same NetKeyIndex will be the same as the result of adding the key the first time.

(see Assigned Numbers document [4])

The NetKey identified by NetKeyIndex is already stored in the node and the new NetKey value is different

Key Index Already Stored

The key identified by NetKeyIndex is not valid for this device for Config NetKey Update message

### Note

Note: When an element receives a Config AppKey Add message that identifies an AppKey that has already been added to the AppKey List, it responds with Success, because the result of adding the key again, with the same AppKey value, using the same AppKeyIndex will be the same as the result of adding the key the first time.

(see Assigned Numbers document [4])

The AppKey identified by AppKeyIndex is already stored in the node and the new AppKey is different

Key Index Already Stored

The node cannot store the new key due to insufficient resources

### Note

Note: Using heartbeat with LPN nodes as destinations is not recommended as it may cause the Friend Queue to overflow. However, if the subscribing element is within a Low Power Node, it should update the Friend Subscription List (see Section 3.6.6.4.3).

### Note

Note: After adding a previously not known group address to one of the node's subscription lists, the node is not protected against a replay attack utilizing messages to that new group address. It is therefore strongly recommended that the Configuration Client run, for a brief period of time, a Heartbeat Subscription procedure on the node and a Heartbeat Publication procedure on all nodes that publish to the new group address to initialize the replay protection list of the node with the current value of the sequence numbers for all affected publishers.

Upon receiving a Config Model Subscription Status message, a Configuration Client can determine the status that can be either a Success or an error (see Table 4.315). If it’s Success, the Configuration Client may determine the address that was used to change the Subscription List state of a particular model within the element. If it’s an error, the Status field will contain the error condition.

To determine the Subscription List state of a particular SIG Model within the element, a Configuration Client shall send a Config SIG Model Subscription Get message. The response is a Config SIG Model Subscription List message that contains a status and may contain the Subscription List state.

To determine the Subscription List state of a particular Vendor Model within the element, a Configuration Client shall send a Config Vendor Model Subscription Get message. The response is a Config Vendor Model Subscription List message that contains a status and may contain the Subscription List state.

Upon receiving a Config SIG Model Subscription List message or a Config Vendor Model Subscription List message, a Configuration Client can determine the status that can be either a Success or an error (see Table 4.315). If it’s Success, the Configuration Client can also determine the current Subscription List state of a particular model within the element. If it’s an error, the Status field will contain the error condition, and the Addresses field will be set to a zero-length (empty) list.

### Note

Note: The error conditions in Table 4.375 imply that the Opcodes Aggregator Server model is implicitly bound to the node’s device key. Additionally, the Configuration Manager should bind the same application key to the Opcodes Aggregator Server model and to one or more desired models on one or more elements on a node for which the OPCODES_AGGREGATOR_SEQUENCE message will be sent; otherwise, the Opcodes Aggregator Server could encounter the WrongAccessKey error condition while executing this procedure.

### Note

Note: After processing the Provisioning Data PDU from the Provisioner, the 96-hour time limits for changing the IV Update procedure state, as defined in the IV Update procedure, do not apply.

Upon receiving the Provisioning Complete PDU from the Provisionee, the Provisioner shall assume that the provisioning process is completed successfully and the Provisionee is using a consecutive range of address starting from the value of the unicast address. The length of the address range is reported to the Provisioner in Provisioning Capabilities PDU (see Section 5.4.1.2). As a final step in procedure, the Provisioner shall disconnect the provisioning bearer. The Provisionee is now a node in the mesh network.

The Provisioner shall not reuse unicast addresses that have been allocated to a Provisionee and sent in a Provisioning Data PDU unless the node to which the unicast addresses were previously assigned has been removed from the network and the current IV Index (in use during the Node Removal procedure) has been updated, as required in Section 3.11.7, or the Node Address Refresh procedure was executed and the current IV Index (in use during the Node Address Refresh procedure) has been updated, as required in Section 3.11.8.5.

### Note

Note: For additional information about public key validation, see NIST Special Publication 800-56A, Revision 3 [11].

### Note

Note: The benefit of reading the Certificate-Based Provisioning Base URI with a Device UUID from a barcode is that the user has a tangible physical object associated with the device that is being provisioned (the device itself, its packaging, or, for example, a paper slip in the packaging), which might be preferable to choosing a beaconing device in the Provisioner’s user interface.

After the Provisioner has acquired both the Certificate-Based Provisioning Base URI and the Device UUID, the Provisioner shall proceed with establishing a provisioning session for the device identified by the Device UUID and retrieving OOB data over the Internet as defined in Sections 5.6.1 through 5.6.4.

By choosing the most efficient encoding that is able to output all of the characters required for the URI (including semicolons and slashes needed for the schema), the implementation can reduce the physical space needed for the 2D barcode.

### Note

Note: Each address in the AddressArray is a 16-bit value and therefore the 16-bit virtual address and not the Label UUID is used.

### Note

Note: Each address in the AddressArray is a 16-bit value and therefore the 16-bit virtual address and not the Label UUID is used.


---

## Document Information

- **Specification:** Bluetooth Mesh Profile v1.1
- **Organization:** Bluetooth Special Interest Group (SIG)
- **Type:** Technical Specification
- **Source:** https://www.bluetooth.com/specifications/specs/
- **Format:** HTML specification converted to Markdown
- **Scope:** Covers network architecture, provisioning, security, models, beacons, proxy protocol, friendship, relay, and transport mechanisms

## Related Specifications

- **Bluetooth Core Specification:** Foundation for all Bluetooth technologies
- **Bluetooth Low Energy:** Physical and link layer for mesh networks
- **OpenThread:** Alternative mesh protocol based on IEEE 802.15.4
- **Matter:** Application layer protocol for smart home devices
- **Zigbee:** Alternative mesh networking protocol

## Key Use Cases

- **Smart Home Lighting:** Large-scale lighting control with many fixtures
- **Building Automation:** HVAC, sensors, and control systems
- **Industrial IoT:** Asset tracking and sensor networks
- **Wearable Networks:** Multiple device coordination
- **Venue Coverage:** Extending range through mesh relay
