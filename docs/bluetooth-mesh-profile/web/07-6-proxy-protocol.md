# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 6. Proxy protocol

The Proxy protocol enables nodes to send and receive Network PDUs, mesh beacons, proxy configuration messages and Provisioning PDUs over a connection-oriented bearer.

For example, a node could support GATT but not be able to advertise the Mesh Message AD Type. This node will establish a GATT connection with another node that supports the GATT bearer and the advertising bearer, using the Proxy protocol to forward messages between these bearers.

### 6.1. Endianness

Unless stated otherwise, all multiple-octet numeric values in this protocol shall be big-endian, as described in [Section 3.1.1.1](index-en.html#UUID-09eb591f-3609-5d59-4423-ca116ea147c4 "3.1.1.1. Big-endian").

### 6.2. Proxy PDU roles

The Proxy protocol defines two main roles: the Proxy PDU Server role and the Proxy PDU Client role.

The Proxy PDU Server role supports a connection-oriented bearer server and Proxy protocol. The Proxy PDU Client role supports a connection-oriented bearer client and Proxy protocol.

#### 6.2.1. Mesh GATT bearer roles

This section defines Proxy PDU roles that are specific to the mesh GATT bearer (see [Section 3.3.2](index-en.html#UUID-2d60af03-4443-f026-58fe-b2ce0261f42b "3.3.2. GATT bearer")).

The Proxy Server is a node that supports the Proxy PDU Server role, the Mesh Proxy Service (see [Section 7.2](index-en.html#UUID-27102d68-3ce7-da1c-30c7-0363cb0671be "7.2. Mesh Proxy Service")), a mesh bearer using the Proxy protocol, and at least one other mesh bearer.
For example, the Proxy Server can forward mesh messages between the advertising bearer and the GATT bearer.

The Proxy Client supports the Proxy PDU Client role and a mesh bearer using the Proxy protocol. For example, the Proxy Client can use the GATT bearer to send mesh messages to a node that supports the advertising bearer.

##### 6.2.1.1. Directed Proxy roles

Two roles are defined for directed proxy functionality: the Directed Proxy Server role and the Directed Proxy Client role.

The Directed Proxy Server is a Proxy Server that supports directed proxy functionality (see [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality")). The Directed Proxy Server shall support processing of the
DIRECTED_PROXY_CAPABILITIES_STATUS and DIRECTED_PROXY_CONTROL messages (see [Section 6.7.1](index-en.html#UUID-10475ad4-589c-ed2b-b15f-a727a8093ebb "6.7.1. Directed Proxy Server behavior")).

The Directed Proxy Client is a Proxy Client that supports behavior described in [Section 6.8.1](index-en.html#UUID-0d2bfd0f-8e71-f702-6fa7-731ed4643b0d "6.8.1. Directed Proxy Client behavior"). The Directed Proxy Client shall support processing of the
DIRECTED_PROXY_CAPABILITIES_STATUS and DIRECTED_PROXY_CONTROL messages.

The Directed Proxy Client may support directed forwarding. If a Proxy Client is a Directed Proxy Client and it does not support directed forwarding, it can act as a dependent node (see [Section 3.6.8.3](index-en.html#UUID-0c0fc10c-4a72-e0d8-2944-e1408b1d2734 "3.6.8.3. Node dependence in directed forwarding")) of a Directed Proxy Server to establish and maintain paths.

If the Proxy Client supports directed forwarding, it shall support the Directed Proxy Client role (i.e., processing of the DIRECTED_PROXY_CAPABILITIES_STATUS and DIRECTED_PROXY_CONTROL messages).

#### 6.2.2. Provisioning PB-GATT bearer roles

This section defines Proxy PDU roles that are specific to the PB-GATT provisioning bearer (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")).

The Provisioning Server is a node that supports the Proxy PDU Server and Mesh Provisioning Service (see [Section 7.1](index-en.html#UUID-ac25d497-815b-be56-7af4-fc105dfc1873 "7.1. Mesh Provisioning Service")).

The Provisioning Client is a node that supports the Proxy PDU Client and supports transporting Provisioning PDUs using the Proxy protocol.

### 6.3. Proxy PDU

A Proxy PDU Client and a Proxy PDU Server exchange Proxy PDUs. Proxy PDUs can contain Network PDUs, mesh beacons, proxy configuration messages or Provisioning PDUs. A single Proxy PDU can contain a full message or a segment of a message. The size of the Proxy PDU is determined by the user of the Proxy protocol. For example, the
GATT bearer defines the size of the Proxy PDU based on the ATT_MTU.

#### 6.3.1. PDU format

The format of a Proxy PDU is illustrated in [Figure 6.1](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620_figure-idm4539442733936034120890374125 "Figure 6.1. Proxy PDU format") and defined in [Table 6.1](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620_Table_6.1 "Table 6.1. Proxy PDU format").

![Proxy PDU format](image/1671b81d8742fa.png)

Figure 6.1. Proxy PDU format

| Field Name | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| SAR | 2 | Message segmentation and reassembly information | M |
| MessageType | 6 | Type of message contained in the PDU | M |
| Data | variable | Full message or message segment | M |

Table 6.1. Proxy PDU format

The SAR field shown in [Table 6.2](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620_Table_6.2 "Table 6.2. SAR field values ") identifies the message segmentation and defines the contents of the Data field:

| Value | Description |
| --- | --- |
| 0b00 | Data field contains a complete message |
| 0b01 | Data field contains the first segment of a message |
| 0b10 | Data field contains a continuation segment of a message |
| 0b11 | Data field contains the last segment of a message |

Table 6.2. SAR field values

The MessageType field identifies the type of message contained in the Proxy PDU. The MessageType values are defined in [Table 6.3](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620_Table_6.3 "Table 6.3. MessageType values").

| Type | Name | Description |
| --- | --- | --- |
| 0x00 | Network PDU | The message is a Network PDU as defined in [Section 3.4.4](index-en.html#UUID-3dd0ba16-878c-54da-1b93-c877bd3ac360 "3.4.4. Network PDU"). |
| 0x01 | Mesh Beacon | The message is a mesh beacon as defined in [Section 3.10](index-en.html#UUID-f17ee0cf-93c1-0e9e-1c41-d35b0d204a9f "3.10. Mesh beacons"). |
| 0x02 | Proxy Configuration | The message is a proxy configuration message as defined in [Section 6.6](index-en.html#UUID-05a50591-1bd9-272d-d846-ebc116777db0 "6.6. Proxy configuration messages"). |
| 0x03 | Provisioning PDU | The message is a Provisioning PDU as defined in [Section 5.4.1](index-en.html#UUID-89d195da-61a7-a6c0-5a5a-85254fa13ba1 "5.4.1. Provisioning PDUs"). |
| 0x04–0x3F | RFU | Reserved for Future Use. |

Table 6.3. MessageType values

The Data field contains a message defined by the MessageType field segmented as defined by the SAR field.

#### 6.3.2. Behavior

Upon receiving a message with the Message Type field set to a value that is Reserved for Future Use or a value that is not supported by the Proxy PDU Server, the Proxy PDU Server shall ignore this message.

Upon receiving a message with the Message Type field set to a value that is Reserved for Future Use or a value that is not supported by the Proxy PDU Client, the Proxy PDU Client shall ignore this message.

##### 6.3.2.1. Segmentation

Messages sent using the Proxy protocol may be larger than an individual Proxy PDU. To enable such messages to be transmitted, segmentation and reassembly is used.

When sending a message that is less than or equal to the maximum size of a Proxy PDU, the SAR field shall be set to 0b00 and the Data field shall contain the complete message.

When sending a message that is greater than the maximum size of a Proxy PDU, the message is divided into segments that will fill each Proxy PDU except for the last Proxy PDU that may or may not be filled. These segments shall be sent in order and the SAR field of the first segment shall be set to 0b01, the SAR field of the
last segment shall be set to 0b11, and all other segments shall have the SAR field set to 0b10.

##### 6.3.2.2. Reassembly

Upon receiving a message with an unexpected value of the SAR field, the Proxy PDU Server shall disconnect.

Upon receiving a Proxy PDU matching one of the following conditions, the Proxy PDU Server shall disconnect:

* The MessageType field equal to a Network PDU and the Data field longer than the maximal size of a Network PDU (see [Section 3.4.4](index-en.html#UUID-3dd0ba16-878c-54da-1b93-c877bd3ac360 "3.4.4. Network PDU"))
* The MessageType field equal to a Mesh Beacon and the Data field longer than the maximal size of a Mesh Beacon (see [Section 3.10](index-en.html#UUID-f17ee0cf-93c1-0e9e-1c41-d35b0d204a9f "3.10. Mesh beacons"))
* The MessageType field equal to a Proxy Configuration and the Data field longer than the maximal size of a proxy configuration message (see [Section 6.6](index-en.html#UUID-05a50591-1bd9-272d-d846-ebc116777db0 "6.6. Proxy configuration messages"))
* The MessageType field equal to a Provisioning PDU and the Data field longer than the maximal size of a supported Provisioning PDU (see [Section 5.4.1](index-en.html#UUID-89d195da-61a7-a6c0-5a5a-85254fa13ba1 "5.4.1. Provisioning PDUs"))

The timeout for the SAR transfer is 20 seconds. When the timeout expires, the Proxy PDU Server shall disconnect.

Upon receiving a message with an unexpected value of the SAR field, the Proxy PDU Client shall disconnect.

Upon receiving a Proxy PDU matching one of the following conditions, the Proxy PDU Client shall disconnect:

* The MessageType field equal to a Network PDU and the Data field longer than the maximal size of a Network PDU (see [Section 3.4.4](index-en.html#UUID-3dd0ba16-878c-54da-1b93-c877bd3ac360 "3.4.4. Network PDU"))
* The MessageType field equal to a Mesh Beacon and the Data field longer than the maximal size of a Mesh Beacon (see [Section 3.10](index-en.html#UUID-f17ee0cf-93c1-0e9e-1c41-d35b0d204a9f "3.10. Mesh beacons"))
* The MessageType field equal to a Proxy Configuration and the Data field longer than the maximal size of a proxy configuration message (see [Section 6.6](index-en.html#UUID-05a50591-1bd9-272d-d846-ebc116777db0 "6.6. Proxy configuration messages"))
* The MessageType field equal to a Provisioning PDU and the Data field longer than the maximal size of a supported Provisioning PDU (see [Section 5.4.1](index-en.html#UUID-89d195da-61a7-a6c0-5a5a-85254fa13ba1 "5.4.1. Provisioning PDUs"))

The timeout for the SAR transfer is 20 seconds. When the timeout expires, the Proxy PDU Client shall disconnect.

### 6.4. Proxy filtering

In order to reduce the number of Network PDUs exchanged between a Proxy Client and a Proxy Server, a proxy filter can be used.

The output filter of the network interface (see [Section 3.4.5](index-en.html#UUID-47eec409-ad2d-8794-6b38-57b655e60ca1 "3.4.5. Network interfaces")) instantiated by the Proxy Server can be configured by the Proxy Client. This allows the Proxy Client to explicitly request
to receive only mesh messages with certain destination addresses. For example, a Proxy Client that is subscribed to a group address may want to only receive packets addressed to the unicast address of one of its elements and to that group address. Thus, the Proxy Client has full control over the packets it receives using the Proxy
protocol.

#### 6.4.1. Filter types

A proxy filter can be either an accept list filter or a reject list filter.

An accept list filter has an associated accept list, which is a list of destination addresses that are of interest to the Proxy Client. The accept list filter blocks all destination addresses except those that have been added to the accept list.

A reject list filter has an associated reject list, which is a list of destination addresses that the Proxy Client does not want to receive. The reject list filter accepts all destination addresses except those that have been added to the reject list.

The accept list filter with an empty list is the default filter type. The Proxy Client can change the filter type as well as configure the addresses in the proxy filter.

### 6.5. Proxy Privacy parameter

The Proxy Privacy parameter controls the privacy of the Proxy Server over the connection. The Proxy Privacy parameter can be set to either Enabled (0x01) or Disabled (0x00) for the connection.

When the Proxy Privacy parameter for the connection is Enabled (0x01), the Proxy Server sends Mesh Private beacons over the connection.

When the Proxy Privacy parameter for the connection is Disabled (0x00), the Proxy Server sends Secure Network beacons over the connection.

The value of the Proxy Privacy parameter is controlled by the type of proxy connection, which is dependent on the bearer used by the proxy connection.

The value of the Proxy Privacy parameter for GATT Proxy bearer is defined in the [Section 7.2.2.2.6](index-en.html#UUID-80b6fcd3-1237-879b-6d2b-ed817de4ce69 "7.2.2.2.6. Proxy Privacy parameter for GATT Proxy bearer").

### 6.6. Proxy configuration messages

In addition to Network PDUs, mesh beacons and Provisioning PDUs, the Proxy Client and Proxy Server can exchange proxy configuration messages using the Proxy protocol.

Proxy configuration messages are used to configure the proxy filters and the connection parameters of a Directed Proxy Server for a subnet.

The format of a proxy configuration message is identical to a Network PDU as defined in [Table 3.10](index-en.html#UUID-3dd0ba16-878c-54da-1b93-c877bd3ac360_Table_3.10 "Table 3.10. Network PDU field definitions").

The CTL field shall be set to 1.

The TTL field shall be set to 0.

The DST field shall be set to the unassigned address.

The TransportPDU field shall be formatted as shown in [Table 6.4](index-en.html#UUID-05a50591-1bd9-272d-d846-ebc116777db0_Table_6.4 "Table 6.4. Proxy TransportPDU field format") and shall be secured using the managed flooding security credentials as defined in
[Section 3.9.6.3.1](index-en.html#UUID-d0b55b79-5d9d-9a14-e649-f8d9d9fcd7d1 "3.9.6.3.1. NID, EncryptionKey, and PrivacyKey") with the proxy nonce as defined in [Section 3.9.5.4](index-en.html#UUID-49587ac0-0be8-d00b-3690-55209889a066 "3.9.5.4. Proxy nonce").

| Field Name | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | Message opcode | M |
| Parameters | 0–11 | Message parameters | M |

Table 6.4. Proxy TransportPDU field format

The Opcode field values are defined in [Table 6.5](index-en.html#UUID-05a50591-1bd9-272d-d846-ebc116777db0_Table_6.5 "Table 6.5. Proxy configuration message opcodes"):

| Value | Opcode | Description |
| --- | --- | --- |
| 0x00 | Set Filter Type | Sent by a Proxy Client to set the proxy filter type. |
| 0x01 | Add Addresses To Filter | Sent by a Proxy Client to add addresses to the proxy filter list. |
| 0x02 | Remove Addresses From Filter | Sent by a Proxy Client to remove addresses from the proxy filter list. |
| 0x03 | Filter Status | Acknowledgment by a Proxy Server to a Proxy Client to report the status of the proxy filter list. |
| 0x04 | DIRECTED_PROXY_CAPABILITIES_STATUS | Sent by a Directed Proxy Server to report the status of its capabilities for a subnet. |
| 0x05 | DIRECTED_PROXY_CONTROL | Sent by a Directed Proxy Client to set connection parameters of the Directed Proxy for a subnet. |
| 0x06–0xFF | RFU | Reserved for Future Use |

Table 6.5. Proxy configuration message opcodes

The Parameters field is specific to each opcode and is defined in the following subsections.

#### 6.6.1. Set Filter Type

A Set Filter Type message can be sent by a Proxy Client to change the proxy filter type and clear the proxy filter list.

The parameters of this message are defined in [Table 6.6](index-en.html#UUID-ace9ed2e-360d-4ed8-ccb3-cfc476382736_Table_6.6 "Table 6.6. Set Filter Type Message Format"):

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| FilterType | 1 | The proxy filter type. | M |

Table 6.6. Set Filter Type Message Format

The values for the FilterType field are defined in [Table 6.7](index-en.html#UUID-ace9ed2e-360d-4ed8-ccb3-cfc476382736_Table_6.7 "Table 6.7. FilterType Values"):

| Value | Description |
| --- | --- |
| 0x00 | Accept list filter |
| 0x01 | Reject list filter |
| 0x02–0xFF | Prohibited |

Table 6.7. FilterType Values

#### 6.6.2. Add Addresses to Filter

An Add Addresses to Filter message is sent by a Proxy Client to add destination addresses to the proxy filter list.

The parameters of this message are defined in [Table 6.8](index-en.html#UUID-14b6c061-73f7-9f10-21ab-64fbd8d58f19_Table_6.8 "Table 6.8. Add Addresses to Filter message format"):

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| AddressArray | 2 * N | List of addresses where N is the number of addresses in this message. | M |

Table 6.8. Add Addresses to Filter message format

The AddressArray field contains a sequence of addresses to be added to the proxy filter list. It may contain any combination of unicast addresses, virtual addresses, and group addresses. The field size is parameterized by parameter N, and the N is an integer in the range 0 to 5 inclusive.

### Note

Note: Each address in the AddressArray is a 16-bit value and therefore the 16-bit virtual address and not the Label UUID is used.

#### 6.6.3. Remove Addresses from Filter

A Remove Addresses from Filter message is sent by a Proxy Client to remove destination addresses from the proxy filter list.

The parameters of this message are defined in [Table 6.9](index-en.html#UUID-1693cebd-a420-dd76-033d-81bf3fafe36a_Table_6.9 "Table 6.9. Remove Addresses from Filter message format"):

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| AddressArray | 2 * N | List of addresses where N is the number of addresses in this message. | M |

Table 6.9. Remove Addresses from Filter message format

The AddressArray field contains a sequence of addresses to be removed from the proxy filter list. It may contain any combination of unicast addresses, virtual addresses, or group addresses. The field size is parameterized by parameter N, and the N is an integer in the range 0 to 5 inclusive.

### Note on Remove Addresses Filter

Note: Each address in the AddressArray is a 16-bit value and therefore the 16-bit virtual address and not the Label UUID is used.

#### 6.6.4. Filter Status

A Filter Status message is sent by a Proxy Server to report the status of the proxy filter.

The parameters of this message are defined in [Table 6.10](index-en.html#UUID-77e25ff1-cc80-62c6-988a-c68ea858feda_Table_6.10 "Table 6.10. Filter Status message format"):

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| FilterType | 1 | Accept list or reject list. | M |
| ListSize | 2 | Number of addresses in the proxy filter list. | M |

Table 6.10. Filter Status message format

The values for the FilterType field are defined in [Table 6.7](index-en.html#UUID-ace9ed2e-360d-4ed8-ccb3-cfc476382736_Table_6.7 "Table 6.7. FilterType Values").

The ListSize field contains the number of addresses in the proxy filter list.

#### 6.6.5. DIRECTED_PROXY_CAPABILITIES_STATUS

A DIRECTED_PROXY_CAPABILITIES_STATUS message is sent by a Directed Proxy Server to report current Directed Proxy capabilities in a subnet.

The parameters of this message are defined in [Table 6.11](index-en.html#UUID-48ed80db-93b4-6835-05d2-82f64ae83aef_Table_6.11 "Table 6.11. DIRECTED_PROXY_CAPABILITIES_STATUS message format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Directed_Proxy | 1 | Current Directed Proxy state | M |
| Use_Directed | 1 | Indicates whether directed forwarding is used for messages from the Proxy Client | M |

Table 6.11. DIRECTED_PROXY_CAPABILITIES_STATUS message format

The Directed_Proxy field indicates the current Directed Proxy state for the identified subnet, as defined in [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy").

The Use_Directed field indicates whether or not the Directed Proxy Server uses directed forwarding for retransmitting Network PDUs originated from the Proxy Client.

[Table 6.12](index-en.html#UUID-48ed80db-93b4-6835-05d2-82f64ae83aef_Table_6.12 "Table 6.12. Values of the Use_Directed field of the DIRECTED_PROXY_CAPABILITIES_STATUS message") defines the values of the Use_Directed field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Directed forwarding is not used for Proxy Client messages. |
| 0x01 | Enable | Directed forwarding is used for Proxy Client messages. |
| 0x02−0xFF | Prohibited | Prohibited |

Table 6.12. Values of the Use_Directed field of the DIRECTED_PROXY_CAPABILITIES_STATUS message

#### 6.6.6. DIRECTED_PROXY_CONTROL

A DIRECTED_PROXY_CONTROL message is sent by a Directed Proxy Client to set whether or not the Directed Proxy Server uses directed forwarding for Directed Proxy Client messages for a specified range of unicast addresses.

The parameters of this message are defined in [Table 6.13](index-en.html#UUID-ca5418c5-ceee-bf2b-bde3-33d634f10ce5_Table_6.13 "Table 6.13. DIRECTED_PROXY_CONTROL message format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Use_Directed | 1 | Indicates whether directed forwarding is used for messages from the Directed Proxy Client. | M |
| Proxy_Client_Unicast_­Addr_­Range | variable  (2 or 3) | Unicast address range of the Directed Proxy Client | C.1 |

Table 6.13. DIRECTED_PROXY_CONTROL message format

C.1:
:   If the Use_Directed field is set to Enabled, the Proxy_Client_Unicast_Addr_Range field shall be present; otherwise, the Proxy_Client_Unicast_Addr_Range field shall not be present.

The Use_Directed field determines whether or not the Directed Proxy Server uses directed forwarding for Directed Proxy Client messages.

[Table 6.14](index-en.html#UUID-ca5418c5-ceee-bf2b-bde3-33d634f10ce5_Table_6.14 "Table 6.14. Values of the Use_Directed field of the DIRECTED_PROXY_CONTROL message") defines the values of the Use_Directed field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Directed forwarding will not be used for Directed Proxy Client messages. |
| 0x01 | Enable | Directed forwarding will be used for Directed Proxy Client messages. |
| 0x02−0xFF | Prohibited | Prohibited |

Table 6.14. Values of the Use_Directed field of the DIRECTED_PROXY_CONTROL message

If present, the Proxy_Client_Unicast_Addr_Range field contains the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) for which the Directed Proxy Server will use directed
forwarding for all Directed Proxy Client messages.

### 6.7. Proxy Server behavior

When a Proxy Client connects to a Proxy Server, a new instance of the GATT bearer is connected to the network layer via a network interface (see [Section 3.4.5](index-en.html#UUID-47eec409-ad2d-8794-6b38-57b655e60ca1 "3.4.5. Network interfaces")).

Upon connection, the Proxy Server shall initialize the proxy filter as an accept list filter and the accept list shall be empty.

If the proxy filter is an accept list filter, upon receiving a Proxy PDU containing a valid Network PDU from the Proxy Client, the Proxy Server shall add the unicast address contained in the SRC field of the Network PDU to the accept list.

If the proxy filter is a reject list filter, upon receiving a Proxy PDU containing a valid Network PDU from the Proxy Client, the Proxy Server shall remove the unicast address contained in the SRC field of the Network PDU from the reject list.

Upon connection, the Proxy Server shall evaluate the Proxy Privacy parameter (for GATT Proxy bearer see [Section 7.2.2.2.6](index-en.html#UUID-80b6fcd3-1237-879b-6d2b-ed817de4ce69 "7.2.2.2.6. Proxy Privacy parameter for GATT Proxy bearer")) for the connection and the Proxy
Server shall retain the value of the Proxy Privacy parameter for the lifetime of the connection. The Proxy Server shall send a mesh beacon for each known subnet to the Proxy Client, as defined in [Table 6.15](index-en.html#UUID-fc8c7bc8-562f-8e11-914d-5fd3b02e299b_Table_6.15 "Table 6.15. Proxy Server mesh beacon transmit behavior").

Upon successfully processing a Secure Network Beacon or a Mesh Private beacon with a new value for the IV Index field or the Flags field, the Proxy Server shall send a mesh beacon to the Proxy Client, as defined in [Table 6.15](index-en.html#UUID-fc8c7bc8-562f-8e11-914d-5fd3b02e299b_Table_6.15 "Table 6.15. Proxy Server mesh beacon transmit behavior").

Upon successfully generating a Secure Network Beacon or a Mesh Private beacon with a new value for the IV Index field or the Flags field, the Proxy Server shall send a mesh beacon to the Proxy Client, as defined in [Table 6.15](index-en.html#UUID-fc8c7bc8-562f-8e11-914d-5fd3b02e299b_Table_6.15 "Table 6.15. Proxy Server mesh beacon transmit behavior").

When the Proxy Server is added to a new subnet, the server shall send a mesh beacon for that subnet to the Proxy Client, as defined in [Table 6.15](index-en.html#UUID-fc8c7bc8-562f-8e11-914d-5fd3b02e299b_Table_6.15 "Table 6.15. Proxy Server mesh beacon transmit behavior").

| Proxy Privacy parameter | Behavior |
| --- | --- |
| Not Supported | Send Secure Network beacon |
| Disabled | Send Secure Network beacon |
| Enabled | Send Mesh Private beacon |

Table 6.15. Proxy Server mesh beacon transmit behavior

Upon receiving a Secure Network Beacon from the Proxy Client, the Proxy Server shall process it as defined in [Section 3.10.3.1](index-en.html#UUID-96c8cf0a-e636-a392-2dba-e495c4a28d4a "3.10.3.1. Secure Network beacon behavior").

If Mesh Private beacons are supported, upon receiving a Mesh Private beacon from the Proxy Client, the Proxy Server shall process it as defined in [Section 3.10.4.2](index-en.html#UUID-b020a4a9-53d8-c12a-e65c-6a7885d6cc68 "3.10.4.2. Mesh Private beacon behavior").

When sending a proxy configuration message, a Proxy Server shall set the SRC field to the unicast address of its primary element and the SEQ field shall use the sequence number of its primary element.

If a Proxy Server receives a Set Filter Type message, it shall set the proxy filter type as requested in the message parameter, and it shall clear the proxy filter list. The Proxy Server shall then respond with a Filter Status message.

If the Proxy Server receives an Add Addresses to Filter message, then it shall add these addresses to the proxy filter list and shall respond with a Filter Status message. If one or more addresses contained in the message are already in the list, the Proxy Server shall not add these addresses. If the Proxy Server runs out of space
in the proxy filter list, the Proxy Server shall not add these addresses. If the AddressArray field contains the unassigned address, the Proxy Server shall ignore that address.

If the Proxy Server receives a Remove Addresses from Filter message, it shall remove these addresses from the proxy filter list and shall respond with a Filter Status message. If one or more addresses contained in the message were not in the list, the Proxy Server shall ignore these addresses. If the AddressArray field contains
the unassigned address, the Proxy Server shall ignore that address.

When the Proxy Server responds to a Set Filter Type message, or an Add Addresses to Filter message, or a Remove Addresses from Filter message with the Filter Status message, the Filter Status message shall be secured with the same network security credentials as were used for the received message.

Upon receiving a proxy configuration message with the Opcode field set to a value that is Reserved for Future Use, the Proxy Server shall ignore this message.

If the proxy filter is an accept list filter, and the Proxy Server is a Directed Proxy node in a subnet (see [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality")), then the Proxy Server operates as a supporting node
for its Proxy Client according to [Section 3.6.8.3](index-en.html#UUID-0c0fc10c-4a72-e0d8-2944-e1408b1d2734 "3.6.8.3. Node dependence in directed forwarding").

#### 6.7.1. Directed Proxy Server behavior

The behavior of Directed Proxy Server for each connection is controlled by the following parameters:

* Use_Directed—Controls usage of Directed Proxy for the current connection on each subnet known to the Directed Proxy Server. The Use_Directed parameter can be set either to Enabled (0x01) or Disabled (0x00). Upon connection, the value of the Use_Directed parameter for a subnet shall be set to 0x01 if the value of the
  Directed Proxy Use Directed Default state for the subnet (see [Section 4.2.26.4](index-en.html#UUID-04cdd8a9-ea09-11c6-bdb9-d01d12540472 "4.2.26.4. Directed Proxy Use Directed Default")) is 0x01; otherwise, the value of the Use_Directed parameter for the subnet shall
  be set to 0x00.
* Proxy_Client_Address_Range—Indicates the unicast address range in a subnet for which the Directed Proxy Server uses directed forwarding. The Proxy_Client_Address_Range can be set either to a unicast address range (as defined in [Section 3.4.2.2.4](index-en.html#UUID-fc8aeae7-ad9c-d48a-b94f-ab98ad9662f5 "3.4.2.2.4. Converting to and from the unicast address range format")) or to the Unassigned value (specified by the implementer). Upon connection, the value of the Proxy_Client_Address_Range shall be set to Unassigned for all known
  subnets.
* Proxy_Client_Type—Indicates the type of Proxy Client: Proxy Client, Directed Proxy Client, Reject List Client, or Unset. Upon connection, the value of the Proxy_Client_Type shall be set to Unset.

Upon connection, the Directed Proxy Server shall send a DIRECTED_PROXY_CAPABILITIES_STATUS message for each known subnet to the Proxy Client.

When the Directed Proxy Server is added to a new subnet, and the Proxy_Client_Type parameter for the connection is either Unset or Directed_Proxy_Client, then the Directed Proxy Server shall send a DIRECTED_PROXY_CAPABILITIES_STATUS message for that subnet to the Proxy Client.

When the Directed Proxy Server is deleted from a subnet, and the Proxy_Client_Type parameter for the connection is either Unset or Directed_Proxy_Client, then the Directed Proxy Server shall set the Use_Directed parameter of the connection for the deleted subnet to 0x00, shall set the Proxy_Client_Address_Range parameter of the
connection for the deleted subnet to the Unassigned value, and shall send a DIRECTED_PROXY_CAPABILITIES_STATUS message for the deleted subnet to the Proxy Client.

When the Directed Proxy state (see [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy")) of the Directed Proxy Server is changed from enabled to disabled on a subnet, and the Proxy_Client_Type parameter for the connection
is either Unset or Directed_Proxy_Client, then the Directed Proxy Server shall set the Use_Directed parameter of the connection for the subnet to 0x00, shall set the Proxy_Client_Address_Range parameter of the connection for the subnet to the Unassigned value, and shall send a DIRECTED_PROXY_CAPABILITIES_STATUS message for the
subnet to the Proxy Client.

When the Directed Proxy state (see [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy")) of the Directed Proxy Server is changed from disabled to enabled on a subnet, and the Proxy_Client_Type parameter for the connection
is either Unset or Directed_Proxy_Client, then the Directed Proxy Server shall send a DIRECTED_PROXY_CAPABILITIES_STATUS message for the subnet to the Proxy Client.

When sending a DIRECTED_PROXY_CAPABILITIES_STATUS message for a subnet, the Directed Proxy Server shall set the Directed_Proxy field to the value of the Directed Proxy state of the subnet (see [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy")), and shall set the Use_Directed field to the value of the Use_Directed parameter of the connection for the subnet. The DIRECTED_PROXY_CAPABILITIES_STATUS message shall be secured with the managed flooding security credentials, as defined in [Section 3.9.6.3.1](index-en.html#UUID-d0b55b79-5d9d-9a14-e649-f8d9d9fcd7d1 "3.9.6.3.1. NID, EncryptionKey, and PrivacyKey"), for the corresponding subnet.

If the Directed Proxy Server receives a DIRECTED_PROXY_CONTROL message, and the node identifies the subnet from the network security credentials which were used to successfully decrypt and authenticate the message, and the value of the Proxy_Client_Type parameter is either Unset or Directed Proxy Client, and the value of the
Directed Proxy state for the identified subnet is 0x01, then the Directed Proxy Server shall set the Use_Directed parameter to the value of the Use_Directed field of the received message for the identified subnet. If the value of the Use_Directed field of the received message is Enabled, and the Directed Proxy state for the
identified subnet is 0x01, then the Directed Proxy Server shall set the Proxy_Client_Address_Range parameter for the identified subnet to the value of the Proxy_Client_Unicast_Address_Range field of the received message. The Directed Proxy Server also shall respond with the DIRECTED_PROXY_CAPABILITIES_STATUS message for the
identified subnet.

If the Directed Proxy Server receives a DIRECTED_PROXY_CONTROL message, and the Proxy_Client_Type parameter is either Reject List Client or Proxy Client, then the Directed Proxy Server shall ignore the message.

When a new connection is established between a Proxy Client and the Directed Proxy Server, and the first message received from the Proxy Client is a successfully processed DIRECTED_PROXY_CONTROL message, then the Directed Proxy Server shall set the Proxy_Client_Type parameter to Directed Proxy Client, shall set the Use_Directed
parameter to Disable for all subnets known to the Directed Proxy Server except the subnet identified by the received message; otherwise, the Directed Proxy Server shall set the Proxy_Client_Type parameter to Proxy Client.

If the proxy filter is set to reject list filter, the Directed Proxy Server shall set the Proxy_Client_Type parameter to Reject List Client and shall set the Use_Directed parameter for all subnets known to the Directed Proxy Server to Disabled. If the Proxy_Client_Type parameter is Reject List Client when a proxy connection is
established, the value of the parameter cannot be changed during the connection.

If the Directed Proxy Server receives a valid Network PDU from the Directed Proxy Client, and the value of the Use_Directed parameter of the connection for the subnet identified by the Network PDU is Enabled, and the source address of the Network PDU is outside the unicast address range defined by the Proxy_Client_Address_Range
parameter, then the Directed Proxy Server shall tag the Network PDU with the immutable-credentials tag.

When the value of the Proxy_Client_Type parameter is Proxy Client, each unicast address in the accept list shall be considered a primary element address of a separate dependent node that has no secondary elements. For example, when the accept list contains two unicast addresses, the supporting node might execute the Directed
Forwarding Initialization procedure (see [Section 3.6.8.2.1](index-en.html#UUID-f18f9aa6-b58a-e9ba-840f-2b57c43f5745 "3.6.8.2.1. Directed Forwarding Initialization")) for each unicast address.

Additional behavior associated with the retransmission of Network PDUs at a Directed Proxy Server is described in [Section 3.4.6.3](index-en.html#UUID-97d3fa03-0fa8-5780-0b9e-77654f58b2ab "3.4.6.3. Receiving a Network PDU"). Behavior associated with the execution of
Directed Forwarding procedures at a Directed Proxy Server on behalf of connected Directed Proxy Clients or Proxy Clients is described in [Section 3.6.8.3](index-en.html#UUID-0c0fc10c-4a72-e0d8-2944-e1408b1d2734 "3.6.8.3. Node dependence in directed forwarding").

### 6.8. Proxy Client behavior

When a Proxy Client connects to a Proxy Server, a new instance of the GATT bearer is connected to the network layer via a network interface (see [Section 3.4.5](index-en.html#UUID-47eec409-ad2d-8794-6b38-57b655e60ca1 "3.4.5. Network interfaces")).

The Proxy Client may send proxy configuration messages to configure the proxy filter.

When sending a proxy configuration message, the Proxy Client shall set the SRC field to the unicast address of its primary element and the SEQ field shall use the sequence number of its primary element. The Proxy Client can determine the state of the proxy filter list when it receives a Filter Status message.

Upon receiving a proxy configuration message with the Opcode field set to a value that is Reserved for Future Use, the Proxy Client shall ignore this message.

Upon receiving a Secure Network Beacon from the Proxy Server, the Proxy Client shall process it as defined in [Section 3.10.3.1](index-en.html#UUID-96c8cf0a-e636-a392-2dba-e495c4a28d4a "3.10.3.1. Secure Network beacon behavior"). If Mesh Private beacons are supported, upon
receiving a Mesh Private beacon from the Proxy Server, the Proxy Client shall process it as defined in [Section 3.10.4.2](index-en.html#UUID-b020a4a9-53d8-c12a-e65c-6a7885d6cc68 "3.10.4.2. Mesh Private beacon behavior").

#### 6.8.1. Directed Proxy Client behavior

The Directed Proxy Client can determine the capabilities of a Directed Proxy for a subnet when it receives a DIRECTED_PROXY_CAPABILITIES_STATUS message. If the Directed Proxy Client receives a DIRECTED_PROXY_CAPABILITIES_STATUS message, the Directed Proxy Client identifies the subnet from the network security credentials which
were used to successfully decrypt and authenticate the message, and determines the value of the Directed Proxy state for the identified subnet from the Directed_Proxy field of the received message, and determines the Use_Directed parameter of the connection for the identified subnet from the value of the Use_Directed field of the
received message.

The Directed Proxy Client may send a DIRECTED_PROXY_CONTROL message to control the Use_Directed and Proxy_Client_Address_Range parameters of a Directed Proxy Server for a subnet. The DIRECTED_PROXY_CONTROL message shall be secured with the managed flooding security credentials, as defined in [Section 3.9.6.3.1](index-en.html#UUID-d0b55b79-5d9d-9a14-e649-f8d9d9fcd7d1 "3.9.6.3.1. NID, EncryptionKey, and PrivacyKey"), for the corresponding subnet.

### 6.9. Proxy solicitation

A Proxy Client may use the GAP General Discoverable mode with non-connectable non-scannable undirected advertising events to send Solicitation PDUs (see [Section 6.9.1](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf "6.9.1. Solicitation PDU")) to solicit a Proxy
Server that supports the Private Proxy functionality to start advertising with Private Network Identity type (see [Section 7.2](index-en.html#UUID-27102d68-3ce7-da1c-30c7-0363cb0671be "7.2. Mesh Proxy Service")).

#### 6.9.1. Solicitation PDU

A Solicitation PDU is a non-connectable, undirected advertising PDU with a Service UUID AD Type that includes the «Mesh Proxy Solicitation Service» and a Service Data AD Type that carries network layer information for the Mesh Proxy Solicitation Service.

The Solicitation PDU has the format described in [Table 6.16](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf_Table_6.16 "Table 6.16. Advertisement Data for the Solicitation PDU ").

| AD Type | Size (octets) | Requirement | Comments |
| --- | --- | --- | --- |
| «Incomplete List of 16-bit Service UUIDs»  or  «Complete List of 16-bit Service UUIDs» | variable (4 or more) | M | Includes «Mesh Proxy Solicitation Service» |
| «Service Data» | 22 | M | Service Data AD Type for «Mesh Proxy Solicitation Service» followed by additional service data for this service |

Table 6.16. Advertisement Data for the Solicitation PDU

The format of additional service data for the «Mesh Proxy Solicitation Service» is defined in [Table 6.17](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf_Table_6.17 "Table 6.17. Format of additional service data for the «Mesh Proxy Solicitation Service» ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | See [Table 6.18](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf_Table_6.18 "Table 6.18. Identification Type values") | M |
| Identification Parameters | variable | Format determined by Identification Type field | M |

Table 6.17. Format of additional service data for the «Mesh Proxy Solicitation Service»

The Identification Type field values are defined in [Table 6.18](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf_Table_6.18 "Table 6.18. Identification Type values").

| Type Value | Description |
| --- | --- |
| 0x00 | Proxy Solicitation with Replay Protection type |
| 0x01–0xFF | Reserved for Future Use |

Table 6.18. Identification Type values

The format of the Identification Parameters for the «Mesh Proxy Solicitation Service» when advertising with the Identification Type set to Proxy Solicitation with Replay Protection is identical to a Network PDU as defined in [Section 3.4.4](index-en.html#UUID-3dd0ba16-878c-54da-1b93-c877bd3ac360 "3.4.4. Network PDU"). The Solicitation PDU shall have the following configuration:

* The IVI field shall be set to 0.
* The CTL field shall be set to 1.
* The TTL field shall be set to 0.
* The SRC field shall be set to the solicitation source (see [Section 6.9.1.1](index-en.html#UUID-b6f486a4-d22e-ab10-1526-86f9c120b241 "6.9.1.1. Solicitation source and solicitation number")).
* The DST field can be set to the unassigned address.
* The SEQ field shall be set to the solicitation sequence number of the solicitation source used (see [Section 6.9.1.1](index-en.html#UUID-b6f486a4-d22e-ab10-1526-86f9c120b241 "6.9.1.1. Solicitation source and solicitation number")).
* The TransportPDU field shall be empty.

The Solicitation PDU shall be secured using the managed flooding security material (see [Section 3.9.7](index-en.html#UUID-1e7bf322-b355-ec46-dcd2-a78747a96d9e "3.9.7. Message security")) and the proxy solicitation nonce (see [Section 3.9.5.5](index-en.html#UUID-e937bfd9-6baf-bbf4-06f2-049b7cf706d8 "3.9.5.5. Proxy solicitation nonce")). The IV Index is not used to secure the Solicitation PDU.

Because the Solicitation PDU uses only the format of the Network PDU, the DST field is ignored upon reception.

A node shall implement solicitation replay protection for all Solicitation PDU messages that are successfully processed.

##### 6.9.1.1. Solicitation source and solicitation number

A Proxy Client may use the primary address or any of the secondary addresses as the solicitation source (SSRC) for a Solicitation PDU.

A Proxy Client manages a 24-bit solicitation sequence number (SSEQ) for each solicitation source used. The solicitation sequence number is used for replay protection for Solicitation PDUs. When a Proxy Client is provisioned, the solicitation sequence number shall be set to 0 for each solicitation source. When a Solicitation
PDU is generated, the solicitation sequence number for the solicitation source used in the message shall be increased by one. When the solicitation sequence number reaches the maximum value (0xFFFFFF), the element shall no longer generate Solicitation PDUs.

#### 6.9.2. Behavior

##### 6.9.2.1. Solicitation replay protection list

Each node supporting Solicitation PDU reception shall implement the solicitation replay protection list. The solicitation replay protection list persistently stores items consisting of a solicitation source and a solicitation number. The solicitation replay protection list is used to reject Solicitation PDUs that were already
processed by a node.

The Solicitation PDU is a valid message when the SSRC field and SSEQ field combination is valid. The SSRC field and SSEQ field combination is valid when one of the following conditions is met:

* The SSRC field value is stored in the solicitation replay protection list and the SSEQ field value is bigger than the corresponding stored solicitation sequence number.
* The SSRC field value is not stored in the solicitation replay protection list and the solicitation replay protection list can store a new pair containing a solicitation source and a solicitation sequence number.

When the valid Solicitation PDU message was processed by the node, the SSRC field and SSEQ field of the message shall be stored by the node in the solicitation replay protection list.

##### 6.9.2.2. Reception of a valid Solicitation PDU

A node that receives a valid Solicitation PDU shall enter the GAP General Discoverable mode with connectable undirected advertising events and shall advertise the Service Data associated with the Private Network Identity type (see [Section 7.2](index-en.html#UUID-27102d68-3ce7-da1c-30c7-0363cb0671be "7.2. Mesh Proxy Service")) when all of the following conditions are met:

* The Proxy feature and the Private Proxy functionality are both disabled at the node.
* The On-Demand Private GATT Proxy state has a value in the range 0x01 to 0xFF.
* The PDU authenticates against a known network key.

The node shall no longer advertise the Service Data associated with the Private Network Identity type (see [Section 7.2](index-en.html#UUID-27102d68-3ce7-da1c-30c7-0363cb0671be "7.2. Mesh Proxy Service")) upon GATT connection or when no GATT client connects to this
node after a period determined by the On-Demand Private GATT Proxy state from the reception of the Solicitation PDU and the Private Proxy functionality is disabled.

### 6.10. MSC examples

#### 6.10.1. Accept list filtering

The MSC shown in [Figure 6.2](index-en.html#UUID-a812c955-0888-f2e5-f113-3d9397ab2c5b_figure-idm4613253302568034120956031398 "Figure 6.2. Accept list filtering") illustrates the accept list filtering performed by the Proxy Server, as configured by the Proxy
Client.

![Accept list filtering](image/1671b81d87b6d1.png)

Figure 6.2. Accept list filtering

#### 6.10.2. Reject list filtering

The MSC shown in [Figure 6.3](index-en.html#UUID-3e0c4d31-9179-769d-5d77-b45edf4d87b5_Figure_6.3 "Figure 6.3. Reject list filtering") illustrates the reject list filtering performed by the Proxy Server, as configured by the Proxy Client.

|  |
| --- |
| Reject list filtering |

Figure 6.3. Reject list filtering

#### 6.10.3. Directed Proxy Server interacting with a Proxy Client

The MSC shown in [Figure 6.4](index-en.html#UUID-8c8dc6ca-7faf-eedf-d0dd-ecf6703bbf58_Figure_6.4 "Figure 6.4. Proxy Client and Directed Proxy Server interaction example") illustrates a Directed Proxy Server interacting with a Proxy Client. The Directed Proxy Server
is configured to be a supporting node for the dependent node on subnet #1 but to not become a supporting node for subnet #2.

|  |
| --- |
| Proxy Client and Directed Proxy Server interaction example |

Figure 6.4. Proxy Client and Directed Proxy Server interaction example

#### 6.10.4. Directed Proxy Client interacting with a Directed Proxy Server

The MSCs shown in [Figure 6.5](index-en.html#UUID-37c3786b-705d-462e-3c97-58c7a22d40f0_Figure_6.5 "Figure 6.5. Directed Proxy Client and Directed Proxy Server interaction example") and [Figure 6.6](index-en.html#UUID-37c3786b-705d-462e-3c97-58c7a22d40f0_Figure_6.6 "Figure 6.6. Directed Proxy Server and Directed Proxy Client interaction example, continued") illustrate a Directed Proxy Client interacting with a Directed Proxy Server. The Directed Proxy Server is configured to be a supporting
node for the dependent node on subnet #1 but to not become a supporting node for subnet #2. The Directed Proxy Client sends a DIRECTED_PROXY_CONTROL message to change the configuration of the Directed Proxy Server for the connection: the Directed Proxy Server becomes a supporting node for subnet #2 but not for subnet #1.

|  |
| --- |
| Directed Proxy Client and Directed Proxy Server interaction example |

Figure 6.5. Directed Proxy Client and Directed Proxy Server interaction example

|  |
| --- |
| Directed Proxy Server and Directed Proxy Client interaction example, continued |

Figure 6.6. Directed Proxy Server and Directed Proxy Client interaction example, continued

#### 6.10.5. Simultaneous interactions between a Proxy Server and both a Proxy Client and a Directed Proxy Client

The MSC shown in [Figure 6.7](index-en.html#UUID-788808c8-91ec-b676-dcb0-eb0825f46870_Figure_6.7 "Figure 6.7. Directed Proxy Server interactions with both a Proxy Client and a Directed Proxy Client example") illustrates a Directed Proxy Server interacting
simultaneously with both a Proxy Client and a Directed Proxy Client. The Directed Proxy Server is configured to be a supporting node for dependent nodes on subnet #1 but to not be a supporting node for subnet #2.

The Directed Proxy Client sends a DIRECTED_PROXY_CONTROL message to change the configuration of the Directed Proxy Server for the connection: the Directed Proxy Server becomes a supporting node for subnet #2 but not for subnet #1. At the same time, the Directed Proxy Server is a supporting node for subnet #1 but not for subnet
#2 for the Proxy Client.

|  |
| --- |
| Directed Proxy Server interactions with both a Proxy Client and a Directed Proxy Client example |

Figure 6.7. Directed Proxy Server interactions with both a Proxy Client and a Directed Proxy Client example

#### 6.10.6. Proxy solicitation

The MSC shown in [Figure 6.8](index-en.html#UUID-cdddfc1d-7010-3b33-57ad-59c510d88e08_Figure_6.8 "Figure 6.8. Proxy solicitation") illustrates the Proxy solicitation performed by the Proxy Client to a Proxy Server.

|  |
| --- |
| Proxy solicitation |

Figure 6.8. Proxy solicitation
