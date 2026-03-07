# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 5. Provisioning

Provisioning is a process of adding an unprovisioned device to a mesh network managed by a Provisioner. A Provisioner provides the unprovisioned device with provisioning data that allows it to become a mesh node for the initial term. The provisioning data includes a network key, the current IV Index, and the unicast address for each
element.

A Provisioner is typically a smart phone or other mobile computing device. Although only a single Provisioner is required on a network to do provisioning, multiple Provisioners may be used. The method to share cached data and coordinate across multiple Provisioners is implementation specific.

To provision an unprovisioned device, the provisioning bearer is established between a Provisioner and an unprovisioned device. An unprovisioned device can be identified to a Provisioner by its Device UUID and other supplementary information that may also be provided.

After the provisioning bearer is established, the Provisioner establishes a shared secret with the unprovisioned device using an Elliptic Curve Diffie-Hellman (ECDH) protocol. It then authenticates the unprovisioned device using OOB information that is specific to that unprovisioned device. Such OOB information may include a public
key of the unprovisioned device, a long secret, the requirement to input a value into the unprovisioned device, or the requirement to output a value on that unprovisioned device. Such OOB information may be formatted as a signed certificate (see [Section 5.5](index-en.html#UUID-c4273f5f-99c7-93b9-7189-f6be4d7aa09b "5.5. Certificate-based provisioning")). Such OOB information also enables the authentication of that unprovisioned device. Once the unprovisioned device has been authenticated, the provisioning data is transmitted to the unprovisioned device
encrypted with a key derived from that shared secret. The device key is derived from the ECDHSecret and the ProvisioningSalt.

The generic provisioning layer in [Figure 5.1](index-en.html#UUID-c2ed2695-c7e2-6000-08bb-72c4b7c7e7fe_Figure_5.1 "Figure 5.1. Provisioning protocol stack for the PB-ADV, PB-GATT and PB-Remote bearers") illustrates how the provisioning PDUs are transmitted as
transactions that can be segmented and reassembled. These transactions are sent over a provisioning bearer. The provisioning bearer defines how a session is established for the delivery of transactions from the generic provisioning layer to a single device. Finally, the bearers are in the bottom layer of the provisioning
architecture.

|  |
| --- |
| Provisioning protocol stack for the PB-ADV, PB-GATT and PB-Remote bearers |

Figure 5.1. Provisioning protocol stack for the PB-ADV, PB-GATT and PB-Remote bearers

The PB-ADV bearer allows provisioning of an unprovisioned device by using an advertising bearer. The PB-GATT bearer allows provisioning of an unprovisioned device by using the Mesh Provisioning Service.

The PB-Remote bearer allows a Provisioner that is outside immediate radio range of an unprovisioned device to communicate with a node supporting the Remote Provisioning Server model that is within immediate radio range of the unprovisioned device and to use that node as a retransmitter to communicate with the unprovisioned device
using PB-ADV or PB-GATT. This allows a Provisioner to provision unprovisioned devices using nodes of the mesh network. [Figure 5.2](index-en.html#UUID-c2ed2695-c7e2-6000-08bb-72c4b7c7e7fe_Figure_5.2 "Figure 5.2. Devices participating in provisioning using PB-Remote and PB-ADV") illustrates this process when the Remote Provisioning Server uses PB-ADV to provision an unprovisioned device.

|  |
| --- |
| Devices participating in provisioning using PB-Remote and PB-ADV |

Figure 5.2. Devices participating in provisioning using PB-Remote and PB-ADV

The Provisioner may use the Remote Provisioning Server (see [Section 4.4.5](index-en.html#UUID-a5822f3c-d602-d597-e794-15189e9e3c83 "4.4.5. Remote Provisioning Server model")) to identify unprovisioned devices within immediate radio range of the server.

As a final step, the Provisioner closes the provisioning bearer. Some provisioning bearers require that a close reason be provided when closing the bearer. The close reason is provided by the provisioning protocol. When the provisioning bearer is closed by the peer device, the close reason is provided to the provisioning
protocol.

### 5.1. Endianness

Unless stated otherwise, all multiple-octet numeric values in this layer shall be big-endian, as described in [Section 3.1.1.1](index-en.html#UUID-09eb591f-3609-5d59-4423-ca116ea147c4 "3.1.1.1. Big-endian").

### 5.2. Provisioning bearer layer

A provisioning bearer layer enables the transport of Provisioning PDUs between a Provisioner and an unprovisioned device. Three provisioning bearers are defined:

* PB-ADV (see Section [5.2.1](index-en.html#UUID-be5ca760-c95f-e721-9a93-dba5f15fe793 "5.2.1. PB-ADV"))
* PB-GATT (see Section [5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT"))
* PB-Remote (see Section [5.2.3](index-en.html#UUID-72184028-4557-a048-40bd-5c59ecae015b "5.2.3. PB-Remote"))

Six provisioning roles are defined:

* PB-ADV Client
* PB-ADV Server
* PB-GATT Client
* PB-GATT Server
* PB-Remote Client
* PB-Remote Server

An unprovisioned device may support the PB-ADV Server role and may support the PB-GATT Server role. An unprovisioned device should support both the PB-ADV Server role and the PB-GATT Server role.

A Provisioner shall support either the PB-ADV Client role or PB-GATT Client role, or both roles. If the Provisioner supports only one role, the Provisioner should support the PB-ADV Client role. The Provisioner may also support the PB-Remote Client role.

A node may support the PB-Remote Server role.

#### 5.2.1. PB-ADV

PB-ADV is a provisioning bearer used to provision an unprovisioned device using Generic Provisioning PDUs (see [Section 5.3](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4 "5.3. Generic provisioning layer")) over the advertising channels. The provisioning
mechanism is session based. An unprovisioned device shall support only one session at a time. There is no such limitation for a Provisioner. A session is established using the Link Establishment procedure (see [Section 5.3.2](index-en.html#UUID-d172a299-4dda-515c-4570-505cbff85c24 "5.3.2. Link Establishment procedure")). The PB-ADV provisioning bearer requires a reason when closing the link and provides a reason when the link is closed.

When PB-ADV is used, the Provisioner shall use the PB-ADV Client role and the unprovisioned device shall use the PB-ADV Server role.

The PB-ADV bearer is used for transmitting Generic Provisioning PDUs. The PB-ADV bearer maximum transmission unit (MTU) size is 24 octets.

When using PB-ADV, a Generic Provisioning PDU shall be sent using the PB-ADV AD type identified by «PB-ADV», as defined in [[4](index-en.html#idp254746)].

A Provisioner and an unprovisioned device supporting PB-ADV should perform passive scanning with a duty cycle as close to 100 percent as possible in order to avoid missing any incoming PB-ADV PDUs.

The PB-ADV AD type contains a PB-ADV PDU field. The format of the PB-ADV AD type is defined in [Table 5.1](index-en.html#UUID-be5ca760-c95f-e721-9a93-dba5f15fe793_Table_5.1 "Table 5.1. PB-ADV AD type").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Length | 1 | Length of the AD Type and PB-ADV PDU fields | M |
| AD Type | 1 | «PB-ADV» | M |
| PB-ADV PDU | variable | PB-ADV PDU | M |

Table 5.1. PB-ADV AD type

Any advertising data that includes the PB-ADV AD type shall use ADV_NONCONN_IND PDUs. If a node receives a PB-ADV AD type in a PDU type different from ADV_NONCONN_IND, the message shall be ignored.

The format of the PB-ADV PDU field is defined in [Table 5.2](index-en.html#UUID-be5ca760-c95f-e721-9a93-dba5f15fe793_Table_5.2 "Table 5.2. PB-ADV PDU field format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Link ID | 4 | The identifier of a link | M |
| Transaction Number | 1 | The number for identifying a transaction | M |
| Generic Provisioning PDU | 1–24 | Generic Provisioning PDU being transferred | M |

Table 5.2. PB-ADV PDU field format

The Link ID is used to identify a link between two devices.

The Transaction Number field contains a one-octet value used to identify each individual Generic Provisioning PDU sent by the device. When a Provisioning PDU that does not fit in a single PB-ADV PDU is segmented, all segments are sent using the same Transaction Number field value. When a Provisioning PDU is retransmitted, the
Transaction Number field is not changed.

Transport-specific messages are defined to establish and terminate the link between two devices (see [Section 5.3.1.4](index-en.html#UUID-c0c13026-ac92-f0af-6efc-a07435c4a6a7 "5.3.1.4. Provisioning Bearer Control")). When the link is opened, the Provisioner and the
unprovisioned device shall start the link timer from the initial value set to 60 seconds. When the link timer expires, the Provisioner and the unprovisioned device shall close the link. When the unprovisioned device receives any Provisioning PDU or a Link Close message, then the unprovisioned device shall stop the link timer.

The Generic Provisioning PDU field format is defined in [Section 5.3](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4 "5.3. Generic provisioning layer").

The following rules shall be implemented when sending a PB-ADV PDU:

* When the Generic Provisioning PDU field contains a Provisioning Bearer Control PDU, the Transaction Number field shall be set to 0 and ignored upon reception.
* When the PB-ADV Client is sending a Provisioning PDU for the first time over an open provisioning link, it shall start with a Transaction Number field value of 0x00. The PB-ADV Client shall increment the field value by 1 for each new Provisioning PDU it is sending for the duration of the provisioning link. If the field
  value has reached 0x7F, it shall wrap to 0x00 on sending the next Provisioning PDU.
* When the PB-ADV Server is sending a Provisioning PDU for the first time over an open provisioning link, it shall start with a Transaction Number field value of 0x80. The PB-ADV Server shall increment the field value by 1 for each new Provisioning PDU it is sending for the duration of the provisioning link. If the field
  value has reached 0xFF, it shall wrap to 0x80 on sending the next Provisioning PDU.
* When a PB-ADV Server is receiving a Provisioning PDU, it shall set the Transaction Number field to the value of the Transaction Number field of the PB-ADV PDUs being received during the transaction.
* When a PB-ADV Server is sending a Transaction Acknowledgement PDU, the Transaction Number field shall be set to the value of the Transaction Number field of the PB-ADV PDUs transporting the Provisioning PDU being acknowledged.

#### 5.2.2. PB-GATT

PB-GATT is a provisioning bearer used to provision an unprovisioned device using Proxy PDUs (see [Section 6.3](index-en.html#UUID-409dac4c-68c3-ce46-5b2d-11b164c45073 "6.3. Proxy PDU")) to encapsulate Provisioning PDUs (see [Section 5.4](index-en.html#UUID-3b8e4e4b-4422-810a-8e0e-bcb1913572a2 "5.4. Provisioning protocol")) within the Mesh Provisioning Service (see [Section 7.1](index-en.html#UUID-ac25d497-815b-be56-7af4-fc105dfc1873 "7.1. Mesh Provisioning Service")).
PB-GATT is provided for support when a Provisioner does not support PB-ADV due to limitations of the application interfaces.

The PB-GATT Server shall use the Provisioning Server role (see [Section 6.2.2](index-en.html#UUID-86362645-c949-913e-237b-333d862ee677 "6.2.2. Provisioning PB-GATT bearer roles")) and the PB-GATT Client shall use the Provisioning Client role (see [Section 6.2.2](index-en.html#UUID-86362645-c949-913e-237b-333d862ee677 "6.2.2. Provisioning PB-GATT bearer roles")).

When PB-GATT is used, the Provisioner shall use the PB-GATT Client role and the unprovisioned device shall use the PB-GATT Server role.

To enable very low power operation for the PB-GATT Server and allow the PB-GATT Server to calculate the Diffie-Hellman shared secret without requiring the energy to maintain an idle link, the connection interval for the connection between a PB-GATT Client and a PB-GATT Server should be between 250 and 1,000 milliseconds.

The PB-GATT Server shall be able to receive a single Proxy PDU (see [Section 6.3](index-en.html#UUID-409dac4c-68c3-ce46-5b2d-11b164c45073 "6.3. Proxy PDU")) in a single Write Command ATT PDU.

The PB-GATT Server shall use a single Handle Value Notification ATT PDU to send Provisioning PDUs to a PB-GATT Client.

If the negotiated ATT_MTU is smaller than a required Proxy PDU size, the transmission of the Mesh Provisioning Data In and Mesh Provisioning Out characteristics always needs to be fragmented and reassembled. Each PDU shall be fully reassembled before processing.

The PB-GATT Server shall be able to receive a Proxy PDU in one or several ATT PDUs. The PB-GATT Server shall use one or several Handle Value Notification ATT PDUs to send a Proxy PDU to the PB-GATT Client depending on the size of the message and the negotiated ATT_MTU.

The Mesh Provisioning Data In and Mesh Provisioning Data Out characteristic formats use the Proxy PDU format defined in [Section 6.3.1](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620 "6.3.1. PDU format").

The PB-GATT provisioning bearer does not require a reason when closing the link and does not provide a reason when the link is closed.

[Figure 5.3](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7_figure-idm4671055233464034113814258206 "Figure 5.3. Provisioning protocol, PB-GATT Server, and Mesh Provisioning Service interactions") illustrates the provisioning protocol, PB-GATT Server, and
Mesh Provisioning Service (see [Section 7.1](index-en.html#UUID-ac25d497-815b-be56-7af4-fc105dfc1873 "7.1. Mesh Provisioning Service")) interactions.

![Provisioning protocol, PB-GATT Server, and Mesh Provisioning Service interactions](image/1671b81d7cd721.png)

Figure 5.3. Provisioning protocol, PB-GATT Server, and Mesh Provisioning Service interactions

The link is opened on a PB-GATT bearer when the PB-GATT Client enables notifications (by writing 0x0001) to the Mesh Provisioning Data Out Client Characteristic Configuration Descriptor after a connection is established (see [Section 7.1.3.2.1](index-en.html#UUID-66a231eb-170a-6c57-7306-a23e6eae72bb "7.1.3.2.1. Characteristic behavior")). When the link is opened, the Provisioner and the unprovisioned device shall start the link timer from the initial value set to 60 seconds. When the link timer expires, the Provisioner and the unprovisioned device shall disconnect. When the Provisioner receives
any Provisioning PDU or the connection between the PB-GATT Client and the PB-GATT Server closes, then the Provisioner shall stop the link timer. When the unprovisioned device receives any Provisioning PDU or the connection between the PB-GATT Client and the PB-GATT Server closes, then the unprovisioned device shall stop the link
timer.

#### 5.2.3. PB-Remote

The PB-Remote provisioning bearer uses the existing mesh network to provision an unprovisioned device that is not within immediate radio range of the Provisioner. PB-Remote uses the PB-ADV bearer (see [Section 5.2.1](index-en.html#UUID-be5ca760-c95f-e721-9a93-dba5f15fe793 "5.2.1. PB-ADV")) or the PB-GATT bearer (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")) for the last hop to the unprovisioned device. PB-Remote uses one of the mesh nodes as a PB-Remote Server to
manage the PB-ADV or PB-GATT bearer link on behalf of the Provisioner.

Provisioning should be done using an OOB public key when PB-Remote is used. Provisioning should not be done using Authentication with No OOB when PB-Remote is used.

When PB-Remote is supported by the Provisioner, the Provisioner shall use the PB-Remote Client role. When the node supports the Remote Provisioning Server model, the node uses the PB-Remote Server role.

PB-Remote may also be used to execute the Device Key Refresh procedure (see [Section 3.11.8.4](index-en.html#UUID-26ebc9d4-43f2-290d-0e45-f0b43554b5bd "3.11.8.4. Device Key Refresh procedure")) or the Node Address Refresh procedure (see [Section 3.11.8.5](index-en.html#UUID-762eb7f5-76a1-6b72-8d69-a3dba41425c6 "3.11.8.5. Node Address Refresh procedure")) or the Node Composition Refresh procedure (see [Section 3.11.8.6](index-en.html#UUID-e333e921-a96d-c807-5f65-8dce2e0ccc4d "3.11.8.6. Node Composition Refresh procedure")) between the Provisioner (PB-Remote Client) and the PB-Remote Server.

Multiple instances of the PB-Remote Client can be used by the Provisioner to communicate with many nodes implementing the PB-Remote Server, thus providing the capability to provision many unprovisioned devices at the same time. The PB-Remote Server can only communicate with one PB-Remote Client and can only open one supported
provisioning bearer at a time.

|  |
| --- |
| A Provisioner using multiple instances of the PB-Remote Client |

Figure 5.4. A Provisioner using multiple instances of the PB-Remote Client

The PB-Remote provisioning bearer requires a reason when closing the link. When a PB-Remote Server uses the PB-ADV bearer for the last hop to the device being provisioned and the PB-ADV link is closed, the PB-Remote bearer provides a close reason. When the PB-Remote Server uses the PB-GATT bearer, the provided reason is not used
when closing the link. The PB-Remote Client is not aware whether the PB-ADV or PB-GATT bearer is used by the PB-Remote Server, so providing a reason is mandatory.

##### 5.2.3.1. PB-Remote Client

The PB-Remote Client is a provisioning device that controls the provisioning process. The PB-Remote Client uses the Remote Provisioning Client model. The PB-Remote Client can choose which PB-Remote Server device to communicate with, can instruct the PB-Remote Server to start scanning for unprovisioned devices, and can instruct
the PB-Remote Server to establish a provisioning link with the chosen unprovisioned device. After the Provisioning Bearer link is established, the PB-Remote Client runs the provisioning protocol by executing the PB-Remote’s Send PDU procedure (see [Section 5.2.3.3.3](index-en.html#UUID-334dd14e-7dfb-ca2b-5321-d4923ebd0d7b "5.2.3.3.3. PB-Remote Send PDU procedure")) and the PB-Remote Server executes the PB-Remote’s Receive PDU procedure (see [Section 5.2.3.3.4](index-en.html#UUID-21ae79f0-829f-0041-087f-9ab1af5df413 "5.2.3.3.4. PB-Remote Receive PDU procedure")).

##### 5.2.3.2. PB-Remote Server

The PB-Remote Server is a mesh node that supports the Remote Provisioning Server model. The PB-Remote Server uses the Remote Provisioning Scan procedure to scan for unprovisioned devices. The server uses the Remote Provisioning Extended Scan procedure to obtain additional information about unprovisioned devices and uses the
Provisioning Bearer protocol to establish a Provisioning Bearer link with an unprovisioned device. After a Provisioning Bearer link is established, the PB-Remote Server transports Provisioning PDUs between the PB-Remote Client and the connected Provisioning Bearer protocol.

##### 5.2.3.3. PB-Remote procedures

The PB-Remote Server may support multiple provisioning bearers, but the server shall use only one provisioning bearer at a time. Each provisioning bearer defines different steps that are needed to open or close the bearer connection and to send or receive the Provisioning PDU over the bearer. The subsections [5.2.3.3.1](index-en.html#UUID-d778d00c-520b-7379-123b-b40f792f84bb "5.2.3.3.1. PB-Remote Open Link procedure") through [5.2.3.3.4](index-en.html#UUID-21ae79f0-829f-0041-087f-9ab1af5df413 "5.2.3.3.4. PB-Remote Receive PDU procedure") define common names for these bearer specific steps, thus defining the PB-Remote procedures.

###### 5.2.3.3.1. PB-Remote Open Link procedure

The PB-Remote Open Link procedure is used to establish a connection between the PB-Remote Server and the unprovisioned device. The PB-Remote Server initializes the connection. The procedure accepts the UUID of the device that the provisioning bearer will be open to as a Device UUID parameter and an optional Timeout
parameter. The Timeout parameter is expressed in seconds and the valid range is from 1 to 60 seconds with one second granularity. The default value of the Timeout parameter is 10 seconds. The procedure succeeds or fails depending on the outcome of the opening of a provisioning bearer. The time before the procedure fails via
timeout shall be set to the value of the Timeout parameter.

[Table 5.3](index-en.html#UUID-d778d00c-520b-7379-123b-b40f792f84bb_Table_5.3 "Table 5.3. PB-Remote Open Link procedure results") defines Success and Fail results for the PB-Remote Open Link procedure.

| **Provisioning Bearer** | **Procedure Success** | **Procedure Fail** |
| --- | --- | --- |
| PB-ADV | The Link Establishment procedure (see [Section 5.3.2](index-en.html#UUID-d172a299-4dda-515c-4570-505cbff85c24 "5.3.2. Link Establishment procedure")) establishes a session. | The Link Establishment procedure does not establish a session. |
| PB-GATT | The PB-GATT Client successfully opens a connection to the PB-GATT Server (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")). | The PB-GATT Client is unable to open a connection to the PB-GATT Server. |

Table 5.3. PB-Remote Open Link procedure results

###### 5.2.3.3.2. PB-Remote Close Link procedure

The PB-Remote Close Link procedure is used to close a connection between a PB-Remote Server and the unprovisioned device. The procedure accepts one parameter: Reason. Some provisioning bearers require the Reason parameter to close the connection. This procedure always succeeds. [Table 5.4](index-en.html#UUID-1cbec5e7-8db0-095c-e7a0-c7ca2a7dc4b6_Table_5.4 "Table 5.4. PB-Remote Close Link procedure results") defines results for the PB-Remote Close Link procedure for each provisioning bearer.

| **Provisioning bearer** | **Procedure** |
| --- | --- |
| PB-ADV | Link close step of the Link Establishment procedure (see [Section 5.3.2](index-en.html#UUID-d172a299-4dda-515c-4570-505cbff85c24 "5.3.2. Link Establishment procedure")). |
| PB-GATT | Closing a connection between a PB-GATT Client and a PB-GATT Server (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")). |

Table 5.4. PB-Remote Close Link procedure results

###### 5.2.3.3.3. PB-Remote Send PDU procedure

The PB-Remote Send PDU procedure is used to send a Provisioning PDU from the PB-Remote Server over an open provisioning bearer to the unprovisioned device. The procedure accepts one parameter: Provisioning PDU. The procedure can either succeed or fail depending on the outcome of the Provisioning PDU delivery.

[Table 5.5](index-en.html#UUID-334dd14e-7dfb-ca2b-5321-d4923ebd0d7b_Table_5.5 "Table 5.5. PB-Remote Send PDU procedure") defines the results for the PB-Remote Send PDU procedure.

| **Provisioning Bearer** | **Procedure Success** | **Procedure Fail** |
| --- | --- | --- |
| PB-ADV | The Provisioning PDU is delivered successfully from the Provisioning Server to the unprovisioned device using the PB-ADV provisioning bearer (see [Section 5.3.3](index-en.html#UUID-afce1b57-f795-b1c8-3b0a-b5af21be00c5 "5.3.3. Generic Provisioning behavior")) | The Provisioning PDU delivery from the Provisioning Server to the unprovisioned device using the PB-ADV bearer fails. |
| PB-GATT | The Provisioning PDU is delivered successfully from the PB-Remote Server acting as the PB-GATT Client to the unprovisioned device (PB-GATT Server) using the PB-GATT bearer (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")). | The Provisioning PDU delivery from the PB-Remote Server to the unprovisioned device using the PB-GATT bearer fails. |

Table 5.5. PB-Remote Send PDU procedure

###### 5.2.3.3.4. PB-Remote Receive PDU procedure

The PB-Remote Receive PDU procedure is used to receive a Provisioning PDU sent from the unprovisioned device to the PB-Remote Server over an open provisioning bearer. When the PB-ADV bearer is used, the PB-Remote Server uses the PB-ADV Client for this procedure. When the PB-GATT bearer is used, the server uses the PB-GATT
Client. The procedure either succeeds or fails depending on the outcome of the PDU reception by the PB-Remote Server. The output of the procedure is the received Provisioning PDU.

The procedure is canceled when the open provisioning bearer is closed.

[Table 5.6](index-en.html#UUID-21ae79f0-829f-0041-087f-9ab1af5df413_Table_5.6 "Table 5.6. PB-Remote Receive PDU procedure") defines the results for the PB-Remote Receive PDU procedure.

| **Provisioning Bearer** | **Procedure Success** | **Procedure Fail** |
| --- | --- | --- |
| PB-ADV | The Provisioning PDU is delivered successfully from the unprovisioned device to the PB-Remote Server using the PB-ADV bearer (see [Section 5.3.3](index-en.html#UUID-afce1b57-f795-b1c8-3b0a-b5af21be00c5 "5.3.3. Generic Provisioning behavior")). | The Provisioning PDU delivery from the unprovisioned device to the PB-Remote Server using the PB-ADV bearer fails. |
| PB-GATT | The Provisioning PDU is delivered successfully to the PB-Remote Server acting as the PB-GATT Client from the unprovisioned device (PB-GATT Server) using the PB-GATT bearer (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")). | The Provisioning PDU delivery from unprovisioned device to the PB-Remote Server using the PB-GATT bearer fails. |

Table 5.6. PB-Remote Receive PDU procedure

### 5.3. Generic provisioning layer

The generic provisioning layer is responsible for transport of Generic Provisioning PDUs over an unreliable connectionless provisioning bearer. This layer also defines Generic Provisioning PDUs.

The Generic Provisioning PDU format consists of a Generic Provisioning Control (GPC) field followed by a variable-length Generic Provisioning Payload field as illustrated in [Figure 5.5](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4_figure-idm4662452017067234113850482007 "Figure 5.5. Generic Provisioning PDU format") and defined in [Table 5.7](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4_Table_5.7 "Table 5.7. Generic Provisioning PDU format").

![Generic Provisioning PDU format](image/1671b81d7db27b.png)

Figure 5.5. Generic Provisioning PDU format

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Generic Provisioning Control | 1–17 | Generic Provisioning Control field | M |
| Generic Provisioning Payload | 0–64 | Generic Provisioning Payload (segments of the Provisioning PDU) | M |

Table 5.7. Generic Provisioning PDU format

The two least significant bits of the first octet of the Generic Provisioning Control field contain a Generic Provisioning Control Format (GPCF) field that determines the format of the Generic Provisioning Control field. The GPCF field is an enumeration with the values shown in [Table 5.8](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4_Table_5.8 "Table 5.8. Generic Provisioning Control Format field values").

| Value | Description |
| --- | --- |
| 0b00 | Transaction Start |
| 0b01 | Transaction Acknowledgment |
| 0b10 | Transaction Continuation |
| 0b11 | Provisioning Bearer Control |

Table 5.8. Generic Provisioning Control Format field values

The format of the GPC field for each format type is defined in [Section 5.3.1](index-en.html#UUID-16b215ed-391b-c9a3-a965-fd4ce9581fa6 "5.3.1. Generic Provisioning PDU types").

#### 5.3.1. Generic Provisioning PDU types

##### 5.3.1.1. Transaction Start PDU

A Transaction Start PDU is used to start the transmission of a segmented message. The Generic Provisioning Control field of a Transaction Start PDU is illustrated in [Figure 5.6](index-en.html#UUID-28c77ee8-bf1a-cc0c-61e6-77e8aba618e0_figure-idm4587940233878434114093259309 "Figure 5.6. Transaction Start PDU") and shown in [Table 5.9](index-en.html#UUID-28c77ee8-bf1a-cc0c-61e6-77e8aba618e0_Table_5.9 "Table 5.9. Generic Provisioning Control field for Transaction Start PDU").

![Transaction Start PDU](image/1671b81d7e3de3.png)

Figure 5.6. Transaction Start PDU

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| SegN | 6 | The last segment number | M |
| GPCF | 2 | Set to Transaction Start | M |
| TotalLength | 16 | The number of octets in the Provisioning PDU | M |
| FCS | 8 | Frame Check Sequence of the Provisioning PDU | M |

Table 5.9. Generic Provisioning Control field for Transaction Start PDU

The SegN field shall be set to the last segment number (zero-based) of this transaction.

The GPCF field shall be set to Transaction Start.

The TotalLength field shall be set to the number of octets in the Provisioning PDU.

When transmitted using PB-ADV, the FCS field is calculated as defined by 3GPP TS 27.010 with the Polynomial (x8 + x2 + x1 + 1) and is calculated over the Provisioning PDU only.

The Generic Provisioning Payload shall contain segment 0 of the Provisioning PDU.

##### 5.3.1.2. Transaction Acknowledgment PDU

A Transaction Acknowledgment PDU is used to acknowledge a Provisioning PDU. The Generic Provisioning Control field of a Transaction Acknowledgment PDU is illustrated in [Figure 5.7](index-en.html#UUID-ca6911e7-2ae8-024b-b1e3-6b588e862012_figure-idm4478863068904034114099978763 "Figure 5.7. Transaction Acknowledgment PDU") and shown in [Table 5.10](index-en.html#UUID-ca6911e7-2ae8-024b-b1e3-6b588e862012_Table_5.10 "Table 5.10. Generic Provisioning Control field for Transaction Acknowledgment PDU").

|  |
| --- |
| Transaction Acknowledgment PDU |

Figure 5.7. Transaction Acknowledgment PDU

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Padding | 6 | 0b000000; all other values Prohibited | M |
| GPCF | 2 | Set to Transaction Acknowledgment | M |

Table 5.10. Generic Provisioning Control field for Transaction Acknowledgment PDU

The GPCF field shall be set to Transaction Acknowledgment.

The Generic Provisioning Payload is zero length.

##### 5.3.1.3. Transaction Continuation PDU

A Transaction Continuation PDU is used to send additional segments of a Provisioning PDU. The Generic Provisioning Control field of a Transaction Continuation PDU is illustrated in [Figure 5.8](index-en.html#UUID-d6291528-6f23-7614-2bb4-ec561c051d0f_figure-idm455303406144163411410688986 "Figure 5.8. Transaction Continuation PDU") and shown in [Table 5.11](index-en.html#UUID-d6291528-6f23-7614-2bb4-ec561c051d0f_Table_5.11 "Table 5.11. Generic Provisioning Control field for Transaction Continuation PDU").

|  |
| --- |
| Transaction Continuation PDU |

Figure 5.8. Transaction Continuation PDU

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| SegmentIndex | 6 | Segment number of the transaction | M |
| GPCF | 2 | Set to Transaction Continuation | M |

Table 5.11. Generic Provisioning Control field for Transaction Continuation PDU

The SegmentIndex field shall be set to the segment number contained within this PDU.

The GPCF field shall be set to Transaction Continuation.

The Generic Provisioning Payload shall contain segment SegmentIndex of the Provisioning PDU.

##### 5.3.1.4. Provisioning Bearer Control

A Provisioning Bearer Control PDU is used to manage sessions on bearers that have no inherent session management. The Generic Provisioning Control field of a Provisioning Bearer Control PDU is illustrated in [Figure 5.9](index-en.html#UUID-c0c13026-ac92-f0af-6efc-a07435c4a6a7_figure-idm4669002422462434114121778303 "Figure 5.9. Provisioning Bearer Control PDU") and shown in [Table 5.12](index-en.html#UUID-c0c13026-ac92-f0af-6efc-a07435c4a6a7_Table_5.12 "Table 5.12. Generic Provisioning Control field for Provisioning Bearer Control PDU"). The Provisioning Bearer Control PDUs are defined in the following sections.

|  |
| --- |
| Provisioning Bearer Control PDU |

Figure 5.9. Provisioning Bearer Control PDU

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| BearerOpcode | 6 | The opcode for the provisioning bearer control PDUs | M |
| GPCF | 2 | Set to Provisioning Bearer Control | M |
| Parameters | variable | Parameters defined by each BearerOpcode | M |

Table 5.12. Generic Provisioning Control field for Provisioning Bearer Control PDU

The BearerOpcode values are defined in [Table 5.13](index-en.html#UUID-c0c13026-ac92-f0af-6efc-a07435c4a6a7_Table_5.13 "Table 5.13. BearerOpcode field values").

| Value | Message | Description |
| --- | --- | --- |
| 0x00 | Link Open | Open a session on a bearer with an unprovisioned device |
| 0x01 | Link ACK | Acknowledge a session on a bearer |
| 0x02 | Link Close | Close a session on a bearer |
| 0x03–0x3F | RFU | Reserved for Future Use |

Table 5.13. BearerOpcode field values

The GPCF field shall be set to Provisioning Bearer Control.

The Generic Provisioning Payload is zero length.

The Parameters of each message are defined in the sections that follow.

###### 5.3.1.4.1. Link Open message

A Link Open message is used to establish a link between a Provisioner and an unprovisioned device. The unprovisioned device shall acknowledge this message with the Link ACK message.

The Parameters field for the Link Open message is defined in [Table 5.14](index-en.html#UUID-7acb22a5-3ec3-70a8-80f8-a3a82b10ae52_Table_5.14 "Table 5.14. Parameters field of Link Open message") and the message is illustrated in [Figure 5.10](index-en.html#UUID-7acb22a5-3ec3-70a8-80f8-a3a82b10ae52_figure-idm4671055299038434114136828097 "Figure 5.10. Link Open message format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Device UUID | 16 | This is the Device UUID of the chosen unprovisioned device | M |

Table 5.14. Parameters field of Link Open message

|  |
| --- |
| Link Open message format |

Figure 5.10. Link Open message format

###### 5.3.1.4.2. Link ACK message

A Link ACK message is sent to acknowledge the receipt of the Link Open message.

There are no Parameters for this message.

The Link ACK message is illustrated in [Figure 5.11](index-en.html#UUID-5d9125d2-d0fb-c400-a49b-18e5ca00bb38_Figure_5.11 "Figure 5.11. Link ACK message format").

|  |
| --- |
| Link ACK message format |

Figure 5.11. Link ACK message format

###### 5.3.1.4.3. Link Close message

A Link Close message is used to close a link. Since this message is not acknowledged, the sender shall repeat this message at least three times. Both sides of the link may send this message. This message shall be accepted and processed regardless of the setting of the Reason field.

The Parameters field for the Link Close message is defined in [Table 5.15](index-en.html#UUID-dabc5c31-cbb1-faea-391f-8b9413122bc6_Table_5.15 "Table 5.15. Parameters field of Link Close message ") and the message is illustrated in [Figure 5.12](index-en.html#UUID-dabc5c31-cbb1-faea-391f-8b9413122bc6_figure-idm4669002441729634114141883982 "Figure 5.12. Link Close message format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Reason | 1 | The reason for closing the link | M |

Table 5.15. Parameters field of Link Close message

The Reason field values are defined in [Table 5.16](index-en.html#UUID-dabc5c31-cbb1-faea-391f-8b9413122bc6_Table_5.16 "Table 5.16. Reason field values").

| Value | Reason | Description |
| --- | --- | --- |
| 0x00 | Success | The provisioning was successful |
| 0x01 | Timeout | The provisioning transaction timed out |
| 0x02 | Fail | The provisioning failed |
| 0x03–0xFF | Unrecognized | Unrecognized reason that may be defined in the future. |

Table 5.16. Reason field values

|  |
| --- |
| Link Close message format |

Figure 5.12. Link Close message format

#### 5.3.2. Link Establishment procedure

The Link Establishment procedure is used to establish a session for a bearer that does not have inherent session management. A session is identified by using a Link ID that is static for the duration of the session and shall be randomly generated to prevent collisions between sessions.

A link is established between a Provisioner and an unprovisioned device for sending provisioning messages. The unprovisioned device is identified by a Device UUID (see [Section 3.11.3](index-en.html#UUID-29a75fe3-e98f-0067-f6c7-34aeec2c83f8 "3.11.3. Device UUID")).

The Provisioner shall scan for unprovisioned devices. Upon receiving an Unprovisioned Device beacon, the Provisioner may establish a link with the unprovisioned device identified by the Device UUID.

The link is open for the unprovisioned device when the unprovisioned device sends a Link ACK for the Link Open message. The link is open for the Provisioner when a Link ACK is received with the Link ID equal to the Link ID sent in the Link Open message. The unprovisioned device is being provisioned when the link is open and the
unprovisioned device has received any Provisioning PDU.

When the link is open, the unprovisioned device shall ignore Generic Provisioning PDUs with the Link ID not equal to the Link ID received in the Link Open message.

When the link is not open, and the unprovisioned device receives a Link Open message, then the unprovisioned device shall accept this message by replying with a Link ACK message with the same Link ID set in the PB-ADV PDU. When the link is open, and the unprovisioned device is not being provisioned, and the unprovisioned device
receives a Link Open message with the same Link ID, then the unprovisioned device shall reply with a Link ACK message with the same Link ID set in the PB-ADV PDU. When the link is open, the unprovisioned device shall ignore all Provisioning Bearer Control PDUs received with a different Link ID.

To open a link, the Provisioner shall start the link establishment timer from the initial value set to 60 seconds, and then shall start sending Link Open messages. The Provisioner may cancel this procedure at any time. The Link Open message contains the Device UUID of the unprovisioned device. On PB-ADV, the PB-ADV PDU format
includes a Link ID field.

When the link establishment timer expires, the link is considered not open and the procedure may be restarted. When the link is open, the Provisioner shall stop the link establishment timer.

The link may be closed at any time after link establishment by sending the Link Close message. Either side of the link may send the Link Close message.

The Link Open, Link ACK, and Link Close messages are defined in [Section 5.3.1.4](index-en.html#UUID-c0c13026-ac92-f0af-6efc-a07435c4a6a7 "5.3.1.4. Provisioning Bearer Control").

The message sequence for establishment of a link by ID between a Provisioner and an unprovisioned device is illustrated by [Figure 5.13](index-en.html#UUID-d172a299-4dda-515c-4570-505cbff85c24_figure-idm4507043021504034114149428396 "Figure 5.13. Establishment of Link by ID between a Provisioner and an unprovisioned device") below.

|  |
| --- |
| Establishment of Link by ID between a Provisioner and an unprovisioned device |

Figure 5.13. Establishment of Link by ID between a Provisioner and an unprovisioned device

#### 5.3.3. Generic Provisioning behavior

Each Generic Provisioning PDU shall be sent after a random delay between 20 and 50 milliseconds.

Each Provisioning PDU (see [Section 5.4](index-en.html#UUID-3b8e4e4b-4422-810a-8e0e-bcb1913572a2 "5.4. Provisioning protocol")) is transmitted as a separate transaction. A transaction may be composed of one or more segments.

The number of segments required to send a Provisioning PDU is determined by the size of the Provisioning PDU. Segments are indexed from 0 to 63. Segment 0 shall be sent using a Transaction Start PDU. All other segments shall be sent using a Transaction Continuation PDU. Each segment of the Provisioning PDU is placed into the
Generic Provisioning Payload field of the respective Generic Provisioning PDU.

Each bearer has its own constraints on the maximum size of a Generic Provisioning PDU that can be transmitted by that bearer. Each Generic Provisioning PDU shall be the length of the full MTU for that bearer, except for the last segment of a transaction.

The sender shall send all segments of a transaction in sequence. If the sender does not receive a Transaction Acknowledgment message, the sender shall retransmit all segments of a transaction.

If the sender receives a Transaction Acknowledgment message, then the transaction has completed.

If the sender receives a message with other PDU types, then the message shall be ignored.

When the first message in a transaction is sent, the sender shall start the acknowledgment timer with an initial value of 30 seconds. When the Transaction Acknowledgment message for the transaction is received, the sender shall stop the acknowledgment timer. When the acknowledgment timer expires, the sender shall cancel the
transaction, cancel the provisioning process, and close the link.

The receiver shall determine the number of segments for a transaction from the Transaction Start PDU.

On the PB-ADV bearer, when the receiver has received all segments of a transaction, the receiver shall calculate the FCS for the received Provisioning PDU, and if it matches the FCS field in the Transaction Start PDU, it shall send a Transaction Acknowledgment PDU after a random delay between 20 and 50 milliseconds.

When a Transaction Acknowledgment PDU has been sent for a given transaction and another segment of the same transaction has been received, another Transaction Acknowledgment PDU shall be sent and the received segment shall be ignored.

### 5.4. Provisioning protocol

This section defines requirements for Provisioning PDUs, behavior, and security.

The provisioning protocol defines two roles:

* Provisioner
* Provisionee

The Provisioner is a device that initiates the provisioning protocol. The Provisionee is a device that participates in the execution of the provisioning protocol with the Provisioner, upon request from the Provisioner.

#### 5.4.1. Provisioning PDUs

The Provisioning PDUs are used to communicate between a Provisioner and a Provisionee.

The first octet of the Provisioning PDU is the Type field and defines the format of the Parameters of the Provisioning PDU.

The Provisioning PDU format is defined in [Table 5.17](index-en.html#UUID-89d195da-61a7-a6c0-5a5a-85254fa13ba1_Table_5.17 "Table 5.17. Provisioning PDU format") and illustrated in [Figure 5.14](index-en.html#UUID-89d195da-61a7-a6c0-5a5a-85254fa13ba1_figure-idm4669002440073634114161076261 "Figure 5.14. Provisioning PDU format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Padding | 2 | 0b00. All other values are Prohibited | M |
| Type | 6 | Provisioning PDU Type value (see the Assigned Numbers document [[4](index-en.html#idp254746)]) | M |
| Parameters | variable | Message parameters | M |

Table 5.17. Provisioning PDU format

|  |
| --- |
| Provisioning PDU format |

Figure 5.14. Provisioning PDU format

The Provisioning PDU Type values are defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 5.4.1.1. Provisioning Invite

A Provisioner sends a Provisioning Invite PDU to indicate to the intended Provisionee that the provisioning process is starting. The format of the parameters for the Provisioning Invite PDU is defined in [Table 5.18](index-en.html#UUID-afe1918d-3df9-a771-d9bc-df1adfe28109_Table_5.18 "Table 5.18. Provisioning Invite PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Attention Duration | 1 | Attention Timer state (See [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")) | M |

Table 5.18. Provisioning Invite PDU parameters format

##### 5.4.1.2. Provisioning Capabilities

The Provisionee sends a Provisioning Capabilities PDU to indicate its supported provisioning capabilities to a Provisioner. The format of the parameters for the Provisioning Capabilities PDU is defined in [Table 5.19](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.19 "Table 5.19. Provisioning Capabilities PDU parameters format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Number of Elements | 1 | Number of elements supported by the Provisionee | M |
| Algorithms | 2 | Supported algorithms and other capabilities (see [Table 5.21](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.21 "Table 5.21. Algorithms field values ")) | M |
| Public Key Type | 1 | Supported public key types (see [Table 5.22](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.22 "Table 5.22. Public Key Type field values ")) | M |
| OOB Type | 1 | Supported OOB Types (see [Table 5.23](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.23 "Table 5.23. OOB Type field values ")) | M |
| Output OOB Size | 1 | Maximum size of Output OOB supported (see [Table 5.24](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.24 "Table 5.24. Output OOB Size field values ")) | M |
| Output OOB Action | 2 | Supported Output OOB Actions (see [Table 5.25](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.25 "Table 5.25. Output OOB Action field values ")) | M |
| Input OOB Size | 1 | Maximum size in octets of Input OOB supported (see [Table 5.26](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.26 "Table 5.26. Input OOB Size field values ")) | M |
| Input OOB Action | 2 | Supported Input OOB Actions (see [Table 5.27](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.27 "Table 5.27. Input OOB Action field values")) | M |

Table 5.19. Provisioning Capabilities PDU parameters format

The Number of Elements values are defined in [Table 5.20](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.20 "Table 5.20. Number of Elements field values ").

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01–0xFF | Number of elements supported by the Provisionee |

Table 5.20. Number of Elements field values

The Algorithms values are defined in [Table 5.21](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.21 "Table 5.21. Algorithms field values ").

| Bit | Name |
| --- | --- |
| 0 | BTM_ECDH_P256_CMAC_AES128_AES_CCM |
| 1 | BTM_ECDH_P256_HMAC_SHA256_AES_CCM |
| 2–15 | Reserved for Future Use |

Table 5.21. Algorithms field values

The BTM_ECDH_P256_HMAC_SHA256_AES_CCM bit of the Algorithms field shall be set to 1 by a Provisionee. Other sections of this specification may introduce further requirements for the value of this field.

The Public Key Type values are defined in [Table 5.22](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.22 "Table 5.22. Public Key Type field values ").

| Bit | Description |
| --- | --- |
| 0 | Public Key OOB information available |
| 1–7 | Reserved for Future Use |

Table 5.22. Public Key Type field values

The size of the Public Key OOB information is determined by the selected Algorithm.

The OOB Type values are defined in [Table 5.23](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.23 "Table 5.23. OOB Type field values ").

| Bit | Description |
| --- | --- |
| 0 | Static OOB information available |
| 1 | Only OOB authenticated provisioning supported |
| 2–7 | Reserved for Future Use |

Table 5.23. OOB Type field values

If bit 1 of the OOB Type field is set to 1, bit 0 of the Algorithms field shall be set to 0 and at least one of the conditions listed below shall be met:

* Bit 0 of the OOB Type field is set to 1.
* The Output OOB Size field is not equal to 0x00.
* The Input OOB Size field is not equal to 0x00.

The maximum size of the Static OOB information is 32 octets. The data type for the Static OOB information shall be Binary, Numeric, or Alphanumeric.

The Output OOB Size defines the number of digits that can be output (e.g., displayed or spoken) when the value Output Numeric is set and Output Alphanumeric is not set in the Output OOB Action field (see [Table 5.25](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.25 "Table 5.25. Output OOB Action field values ")). The Output OOB Size defines the number of digits and uppercase letters that can be output when the value Output Numeric is not set and Output Alphanumeric is set in the Output OOB Action field. The Output OOB Size defines the number of digits and
uppercase letters that can be output when the value Output Numeric is set and Output Alphanumeric is set in the Output OOB Action field. The Output OOB Size values are defined in [Table 5.24](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.24 "Table 5.24. Output OOB Size field values ").

| Value | Description |
| --- | --- |
| 0x00 | The Provisionee does not support Output OOB |
| 0x01–0x08 | Maximum size of Output OOB supported by the Provisionee |
| 0x09–0xFF | Reserved for Future Use |

Table 5.24. Output OOB Size field values

The Output OOB Action values are defined in [Table 5.25](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.25 "Table 5.25. Output OOB Action field values ").

| Bit | Description | Data Type |
| --- | --- | --- |
| 0 | Blink | Numeric |
| 1 | Beep | Numeric |
| 2 | Vibrate | Numeric |
| 3 | Output Numeric | Numeric |
| 4 | Output Alphanumeric | Alphanumeric |
| 5–15 | Reserved for Future Use | n/a |

Table 5.25. Output OOB Action field values

The Input OOB Size defines the number of digits that can be entered when the value Input Numeric is set and Input Alphanumeric is not set in the Input OOB Action field (see [Table 5.27](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.27 "Table 5.27. Input OOB Action field values")). The Input OOB Size defines the number of digits and uppercase letters that can be entered when the value Input Numeric is not set and Input Alphanumeric is set in the Input OOB Action field. The Input OOB Size defines the number of digits and uppercase
letters that can be entered when the value Input Numeric is set and Input Alphanumeric is set in the Input OOB Action field. The Input OOB Size values are defined in [Table 5.26](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.26 "Table 5.26. Input OOB Size field values ").

| Value | Description |
| --- | --- |
| 0x00 | The Provisionee does not support Input OOB |
| 0x01–0x08 | Maximum size of Input OOB supported by the Provisionee |
| 0x09–0xFF | Reserved for Future Use |

Table 5.26. Input OOB Size field values

The Input OOB Actions are defined in [Table 5.27](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335_Table_5.27 "Table 5.27. Input OOB Action field values").

| Bit | Description | Data Type |
| --- | --- | --- |
| 0 | Push | Numeric |
| 1 | Twist | Numeric |
| 2 | Input Numeric | Numeric |
| 3 | Input Alphanumeric | Alphanumeric |
| 4–15 | Reserved for Future Use | n/a |

Table 5.27. Input OOB Action field values

##### 5.4.1.3. Provisioning Start

A Provisioner sends a Provisioning Start PDU to indicate the method it has selected from the options in the Provisioning Capabilities PDU. The format of the parameters for the Provisioning Start PDU is defined in [Table 5.28](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.28 "Table 5.28. Provisioning Start PDU parameters format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Algorithm | 1 | The algorithm used for provisioning (see [Table 5.29](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.29 "Table 5.29. Algorithm field values ")) | M |
| Public Key | 1 | Public Key used (see [Table 5.30](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.30 "Table 5.30. Public Key field values ")) | M |
| Authentication Method | 1 | Authentication Method used (see [Table 5.31](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.31 "Table 5.31. Authentication Method field values ")) | M |
| Authentication Action | 1 | Selected Output OOB Action (see [Table 5.32](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.32 "Table 5.32. Output OOB Action values for the Authentication Action field ")) or Input OOB Action (see [Table 5.34](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.34 "Table 5.34. Input OOB Action values for the Authentication Action field ")) or 0x00 | M |
| Authentication Size | 1 | Size of the Output OOB used (see [Table 5.33](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.33 "Table 5.33. Output OOB Size values for the Authentication Size field ")) or size of the Input OOB used (see [Table 5.35](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.35 "Table 5.35. Input OOB Size values for the Authentication Size field")) or 0x00 | M |

Table 5.28. Provisioning Start PDU parameters format

The Algorithm values are defined in [Table 5.29](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.29 "Table 5.29. Algorithm field values ").

| Value | Description |
| --- | --- |
| 0x00 | BTM_ECDH_P256_CMAC_AES128_AES_CCM |
| 0x01 | BTM_ECDH_P256_HMAC_SHA256_AES_CCM |
| 0x02–0xFF | Reserved for Future Use |

Table 5.29. Algorithm field values

The Public Key values are defined in [Table 5.30](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.30 "Table 5.30. Public Key field values ").

| Value | Description |
| --- | --- |
| 0x00 | No OOB Public Key is used |
| 0x01 | OOB Public Key is used |
| 0x02–0xFF | Reserved for Future Use |

Table 5.30. Public Key field values

The Authentication Method field values are defined in [Table 5.31](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.31 "Table 5.31. Authentication Method field values ").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Authentication with No OOB | No OOB authentication is used |
| 0x01 | Authentication with Static OOB | Static OOB authentication is used |
| 0x02 | Authentication with Output OOB | Output OOB authentication is used |
| 0x03 | Authentication with Input OOB | Input OOB authentication is used |
| 0x04–0xFF | Prohibited | Prohibited |

Table 5.31. Authentication Method field values

When the Authentication Method field value is Authentication with No OOB, the Authentication Action field shall be set to 0x00 and the Authentication Size field shall be set to 0x00.

When the Authentication Method field value is Authentication with Static OOB, the Authentication Size shall be set to 0x00 and the Authentication Action field shall be set to 0x00. The data type shall be transferred using an OOB technology.

When the Authentication Method field value is Authentication with Output OOB, the values defined in [Table 5.32](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.32 "Table 5.32. Output OOB Action values for the Authentication Action field ") and [Table 5.33](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.33 "Table 5.33. Output OOB Size values for the Authentication Size field ") shall be used to determine the data type, the Authentication Action, and the Authentication Size.

The Output OOB Action values for the Authentication Action field are defined in [Table 5.32](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.32 "Table 5.32. Output OOB Action values for the Authentication Action field ").

| Value | Description | Data Type |
| --- | --- | --- |
| 0x00 | Blink | Numeric |
| 0x01 | Beep | Numeric |
| 0x02 | Vibrate | Numeric |
| 0x03 | Output Numeric | Numeric |
| 0x04 | Output Alphanumeric | Alphanumeric |
| 0x05–0xFF | Reserved for Future Use | – |

Table 5.32. Output OOB Action values for the Authentication Action field

The Output OOB Size for the Authentication Size field values are defined in [Table 5.33](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.33 "Table 5.33. Output OOB Size values for the Authentication Size field ").

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01–0x08 | The Output OOB Size to be used |
| 0x09–0xFF | Reserved for Future Use |

Table 5.33. Output OOB Size values for the Authentication Size field

When the Authentication Method field value is Authentication with Input OOB, the values defined in [Table 5.34](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.34 "Table 5.34. Input OOB Action values for the Authentication Action field ") and
[Table 5.35](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.35 "Table 5.35. Input OOB Size values for the Authentication Size field") shall be used to determine the data type, the Authentication Action and the Authentication Size.

The Input OOB Action values for the Authentication Action field are defined in [Table 5.34](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.34 "Table 5.34. Input OOB Action values for the Authentication Action field ").

| Value | Description | Data Type |
| --- | --- | --- |
| 0x00 | Push | Numeric |
| 0x01 | Twist | Numeric |
| 0x02 | Input Numeric | Numeric |
| 0x03 | Input Alphanumeric | Alphanumeric |
| 0x04–0xFF | Reserved for Future Use | – |

Table 5.34. Input OOB Action values for the Authentication Action field

The Input OOB Size values for the Authentication Size field are defined in [Table 5.35](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.35 "Table 5.35. Input OOB Size values for the Authentication Size field").

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01–0x08 | The Input OOB size to be used |
| 0x09–0xFF | Reserved for Future Use |

Table 5.35. Input OOB Size values for the Authentication Size field

##### 5.4.1.4. Provisioning Public Key

The Provisioner sends a Provisioning Public Key PDU to deliver the public key to be used in the ECDH calculations. The format of the parameters for the Provisioning Public Key PDU is defined in [Table 5.36](index-en.html#UUID-5c41ac1a-ca86-5350-68b6-5c086460d868_Table_5.36 "Table 5.36. Provisioning Public Key PDU Parameters Format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Public Key X | 32 | The X component of P-256 elliptic curve public key | M |
| Public Key Y | 32 | The Y component of P-256 elliptic curve public key | M |

Table 5.36. Provisioning Public Key PDU Parameters Format

##### 5.4.1.5. Provisioning Input Complete

The Provisionee sends a Provisioning Input Complete PDU when the user completes the input operation.

There are no parameters for the Provisioning Input Complete PDU.

##### 5.4.1.6. Provisioning Confirmation

The Provisioner or the Provisionee sends a Provisioning Confirmation PDU to its peer to confirm the values exchanged so far, including the OOB Authentication value and the random number that has yet to be exchanged. The format of the parameters for the Provisioning Confirmation PDU is defined in [Table 5.37](index-en.html#UUID-3f57cb1f-bec1-6cba-b61f-1b1c7e139b28_Table_5.37 "Table 5.37. Provisioning Confirmation PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Confirmation | 16 or 32 | The values exchanged so far including the OOB Authentication value | M |

Table 5.37. Provisioning Confirmation PDU parameters format

If the PDU is sent by the Provisioner, the Confirmation field shall contain the ConfirmationProvisioner value.

If the PDU is sent by the Provisionee, the Confirmation field shall contain the ConfirmationDevice value.

The size of the Confirmation field, the ConfirmationProvisioner value, and the ConfirmationDevice value are defined in [Section 5.4.2.4.1](index-en.html#UUID-bf81044c-f849-4fd6-90d6-f2ab87064967 "5.4.2.4.1. AuthValue computation").

##### 5.4.1.7. Provisioning Random

The Provisioner or the Provisionee sends a Provisioning Random PDU to enable its peer device to validate the confirmation. The format of the parameters for the Provisioning Random PDU is defined in [Table 5.38](index-en.html#UUID-75b4c60c-edbe-3f46-28c4-b2f966b63261_Table_5.38 "Table 5.38. Provisioning Random PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Random | 16 or 32 | The final input to the confirmation | M |

Table 5.38. Provisioning Random PDU parameters format

If the PDU is sent by the Provisioner, the Random field shall contain the RandomProvisioner value.

If the PDU is sent by the Provisionee, the Random field shall contain the RandomDevice value.

The size of the Random field, the RandomProvisioner value, and the RandomDevice value are defined in [Section 5.4.2.4.1](index-en.html#UUID-bf81044c-f849-4fd6-90d6-f2ab87064967 "5.4.2.4.1. AuthValue computation").

##### 5.4.1.8. Provisioning Data

The Provisioner sends a Provisioning Data PDU to deliver provisioning data to a Provisionee. The format of the parameters for the Provisioning Data PDU is defined in [Table 5.39](index-en.html#UUID-05fccf0d-e9da-069e-47c1-043b99d4d056_Table_5.39 "Table 5.39. Provisioning Data PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Encrypted Provisioning Data | 25 | An encrypted and authenticated network key, NetKey Index, Key Refresh Flag, IV Update Flag, current value of the IV Index, and unicast address of the primary element (see [Section 5.4.2.5](index-en.html#UUID-a5735c88-759a-4471-66c6-6cd945378174 "5.4.2.5. Distribution of provisioning data")) | M |
| Provisioning Data MIC | 8 | PDU Integrity Check value | M |

Table 5.39. Provisioning Data PDU parameters format

##### 5.4.1.9. Provisioning Complete

The Provisionee sends a Provisioning Complete PDU to indicate that it has successfully received and processed the provisioning data.

There are no parameters for the Provisioning Complete PDU.

##### 5.4.1.10. Provisioning Failed

The Provisionee sends a Provisioning Failed PDU if it fails to process a received provisioning protocol PDU. The format of the parameters for the Provisioning Failed PDU is defined in [Table 5.40](index-en.html#UUID-5d074ac9-4a6a-9f60-878b-c722d517214c_Table_5.40 "Table 5.40. Provisioning Failed PDU parameters format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Error Code | 1 | This represents a specific error in the provisioning protocol encountered by a Provisionee | M |

Table 5.40. Provisioning Failed PDU parameters format

The provisioning error codes are defined in [Table 5.41](index-en.html#UUID-5d074ac9-4a6a-9f60-878b-c722d517214c_Table_5.41 "Table 5.41. Provisioning error codes").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Prohibited | Prohibited |
| 0x01 | Invalid PDU | The provisioning protocol PDU is not recognized by the Provisionee |
| 0x02 | Invalid Format | The arguments of the protocol PDUs are outside expected values or the length of the PDU is different than expected |
| 0x03 | Unexpected PDU | The PDU received was not expected at this moment of the procedure |
| 0x04 | Confirmation Failed | The computed confirmation value was not successfully verified |
| 0x05 | Out of Resources | The provisioning protocol cannot be continued due to insufficient resources in the Provisionee |
| 0x06 | Decryption Failed | The Data block was not successfully decrypted |
| 0x07 | Unexpected Error | An unexpected error occurred that may not be recoverable |
| 0x08 | Cannot Assign Addresses | The Provisionee cannot assign consecutive unicast addresses to all elements |
| 0x09 | Invalid Data | The Data block contains values that cannot be accepted because of general constraints |
| 0x0A–0xFF | RFU | Reserved for Future Use |

Table 5.41. Provisioning error codes

##### 5.4.1.11. Provisioning Record Request

The Provisioner sends a Provisioning Record Request PDU to request a provisioning record fragment (a part of a provisioning record; see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")) from the Provisionee. The format of the parameters for the Provisioning Record Request PDU is defined in [Table 5.42](index-en.html#UUID-ae152830-6598-f0db-79ca-84aeaa7c11ed_Table_5.42 "Table 5.42. Provisioning Record Request PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Record ID | 2 | Identifies the provisioning record for which the request is made (see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")). | M |
| Fragment Offset | 2 | The starting offset of the requested fragment in the provisioning record data | M |
| Fragment Maximum Size | 2 | The maximum size of the provisioning record fragment that the Provisioner can receive | M |

Table 5.42. Provisioning Record Request PDU parameters format

A Provisionee may contain multiple provisioning records, and the Record ID field specifies the record that is being requested.

The Fragment Offset field value indicates the starting offset for the provisioning record data fragment in the Provisioning Record Response PDU that corresponds to the Provisioning Record Request. The Fragment Offset field values are in the range 0, indicating the first octet of the provisioning record data, to the
provisioning record data length (in bytes) minus 1, indicating the last octet of the provisioning record data.

The Fragment Maximum Size field specifies the maximum fragment size that the Provisioner can accept. The choice of the value is affected by the provisioning bearer that is being used. A value of 0x0000 is Prohibited.

##### 5.4.1.12. Provisioning Record Response

The Provisionee sends a Provisioning Record Response PDU in response to a Provisioning Record Request PDU. The format of the parameters for the Provisioning Record Response PDU is defined in [Table 5.43](index-en.html#UUID-31c8398d-0c9d-8fc6-9008-7ed602faf9b4_Table_5.43 "Table 5.43. Provisioning Record Response PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Status | 1 | Indicates whether or not the request was handled successfully (see [Table 5.44](index-en.html#UUID-31c8398d-0c9d-8fc6-9008-7ed602faf9b4_Table_5.44 "Table 5.44. Status codes for the Provisioning Record Response PDU")). | M |
| Record ID | 2 | Identifies the provisioning record whose data fragment is sent in the response (see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")). | M |
| Fragment Offset | 2 | The starting offset of the data fragment in the provisioning record data | M |
| Total Length | 2 | Total length of the provisioning record data stored on the Provisionee | M |
| Data | N | Provisioning record data fragment | O |

Table 5.43. Provisioning Record Response PDU parameters format

[Table 5.44](index-en.html#UUID-31c8398d-0c9d-8fc6-9008-7ed602faf9b4_Table_5.44 "Table 5.44. Status codes for the Provisioning Record Response PDU") defines status codes for the Provisioning Record Response PDU.

| Status Code | Status Code Name |
| --- | --- |
| 0x00 | Success |
| 0x01 | Requested Record Is Not Present |
| 0x02 | Requested Offset Is Out Of Bounds |
| 0x03–0xFF | Reserved for Future Use |

Table 5.44. Status codes for the Provisioning Record Response PDU

The value of the Record ID field of the Provisioning Record Response PDU shall be set to the value of the Record ID field of the corresponding Provisioning Record Request PDU.

The value of the Fragment Offset field of the Provisioning Record Response PDU shall be set to the value of the Fragment Offset field of the corresponding Provisioning Record Request PDU.

If the value of the Status field of the Provisioning Record Response PDU is either Success or Requested Offset Is Out Of Bounds, the Total Length field indicates the length of provisioning record data that the Provisionee has for the provisioning record specified by the Record ID field of the Provisioning Record Response
PDU.

If the value of the Status field of the Provisioning Record Response PDU is Requested Record Is Not Present, the Total Length field shall be set to 0x0000.

The Data field contains a fragment of the provisioning record specified by the Record ID field of the Provisioning Record Response PDU.

If the value of the Status field of the Provisioning Record Response PDU is not Success, the Data field shall be empty.

If the value of the Status field of the Provisioning Record Response PDU is Success, the fragment shall start at the position given by the Fragment Offset field of the Provisioning Record Response PDU.

The length of the fragment shall not exceed the value in the Fragment Maximum Size field of the corresponding Provisioning Record Request PDU. The fragment may be shorter than the value of the Fragment Maximum Size field if less data is available or if the Provisionee cannot create a message of the requested size because of
memory limitations or some other limiting factor.

##### 5.4.1.13. Provisioning Records Get

The Provisioner sends a Provisioning Records Get PDU to request the list of IDs of the provisioning records that are stored on a Provisionee.

There are no parameters for the Provisioning Records Get PDU.

##### 5.4.1.14. Provisioning Records List

The Provisionee sends a Provisioning Records List PDU in response to a Provisioning Records Get PDU. The format of the parameters for the Provisioning Records List PDU is defined in [Table 5.45](index-en.html#UUID-dc78a032-14ed-e031-382a-75a490f090b6_Table_5.45 "Table 5.45. Provisioning Records List PDU parameters format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Provisioning Extensions | 2 | Bitmask indicating the provisioning extensions supported by the Provisionee (see [Table 5.46](index-en.html#UUID-dc78a032-14ed-e031-382a-75a490f090b6_Table_5.46 "Table 5.46. Values for the Provisioning Extensions field")) | M |
| Records List | variable | Lists the Record IDs of the provisioning records stored on the Provisionee (see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")) | O |

Table 5.45. Provisioning Records List PDU parameters format

[Table 5.46](index-en.html#UUID-dc78a032-14ed-e031-382a-75a490f090b6_Table_5.46 "Table 5.46. Values for the Provisioning Extensions field") defines provisioning extension values.

| Bit | Description |
| --- | --- |
| 0–15 | Reserved for Future Use |

Table 5.46. Values for the Provisioning Extensions field

The value of the Provisioning Extensions field of the Provisioning Records List PDU indicates the provisioning extensions supported by the Provisionee.

The Records List field of the Provisioning Records List PDU shall list the 16-bit Record IDs of the provisioning records that are stored on the Provisionee. If no provisioning records are stored on the Provisionee, the field shall be empty.

#### 5.4.2. Provisioning behavior

Provisioning is performed using a five-step process: beaconing, invitation, exchanging public keys, authentication, and distribution of the provisioning data, as illustrated by [Figure 5.15](index-en.html#UUID-3f81f59a-3ed1-8ed1-624a-52be83e5c6a9_figure-idm4612012542331234118856523811 "Figure 5.15. Provisioning behavior").

|  |
| --- |
| Provisioning behavior |

Figure 5.15. Provisioning behavior

##### 5.4.2.1. Beaconing

A device that supports PB-ADV, has not been provisioned, and is not in the process of being provisioned, shall advertise the Unprovisioned Device beacon, as defined in [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon"), otherwise a device shall not advertise the Unprovisioned Device beacon. When a device has not been provisioned, it is recommended to use anonymous advertising [[2](index-en.html#idp254742)], a
non-resolvable private address, or a resolvable private address. This beacon may indicate availability of OOB data that allows a Provisioner to prompt the user to collect this OOB data before the next step.

A device that supports PB-GATT, has not been provisioned, and is not in the process of being provisioned, must advertise the Mesh Provisioning Service as required by [Section 7.1.2.2.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b "7.1.2.2.1. Advertising").

##### 5.4.2.2. Invitation

After establishing a provisioning bearer, a Provisioner shall send a Provisioning Invite PDU and the Provisionee shall respond with a Provisioning Capabilities PDU. The Provisioning Invite PDU includes an Attention Duration field for the primary element of the Provisionee and any other elements where the Attention Timer state
(described in [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")) is present. The Attention Duration field is used to determine how long elements take to identify themselves using the Attention Timer. If the provisioning
bearer is dropped, the Provisionee shall set the Attention Timer state of the primary element, and any other elements where the Attention Timer is present, to 0x00 (Off). This Provisioning Capabilities PDU shall include information on the number of supported elements that are present in Composition Data Page 0 (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")), the set of security algorithms supported, the availability of its public key using an OOB technology, the ability for this device to output a value to the user, the
ability for this device to allow a value to be input by the user, and if the device has a block of OOB data that can be used for authentication.

Optionally, after establishing a provisioning bearer, a Provisioner may retrieve provisioning record information from the device (see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")) before sending a Provisioning Invite PDU.

The message sequence for provisioning invitation is illustrated by [Figure 5.16](index-en.html#UUID-2b9b61c6-5dc8-1f39-79af-68467f72d3a1_figure-idm4550635111304034118860173412 "Figure 5.16. Provisioning invitation") below.

|  |
| --- |
| Provisioning invitation |

Figure 5.16. Provisioning invitation

##### 5.4.2.3. Exchanging public keys

This step has two possibilities depending on the availability of the Provisionee public key on the Provisioner side. Combined with the three possibilities of the authentication step (see [Section 5.4.2.4](index-en.html#UUID-d5c63e25-0cd7-6e62-16fb-5045e087ae07 "5.4.2.4. Authentication")), there are six possible exchange/authentication paths.

Once the Provisioner has determined that it can provision the Provisionee, it shall send a Provisioning Start PDU that details which of the six possible paths that the Provisioner has chosen to use.

Upon receiving the Provisioning Start PDU from the Provisioner, the Provisionee shall set the Attention Timers present on the device to 0x00.

If bit 1 of the OOB Type field of the Provisioning Capabilities PDU is set to 1 (Only OOB authenticated provisioning supported) and any of the following conditions is met:

* the Algorithm field of the Provisioning Start PDU is not set to BTM_ECDH_P256_CMAC_AES128_AES_CCM and the Provisioning Start PDU has the Authentication Method field set to the Authentication with No OOB value
* the Algorithm field is set to BTM_ECDH_P256_CMAC_AES128_AES_CCM

the provisioning protocol shall fail and the message shall be treated by the Provisionee as an error in the provisioning protocol.

The Provisioner shall support all Algorithm values as defined in [Table 5.29](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.29 "Table 5.29. Algorithm field values "). The Provisioner shall select a single algorithm from those offered to it
by the New Device in the Provisioning Capability PDU. If the Provisioner does not understand a bit set in this algorithm bit field, it shall ignore that bit and only select from the algorithms it does understand. The Provisioner should choose the strongest algorithm. The Provisioner shall not use BTM_ECDH_P256_CMAC_AES128_AES_CCM
if another algorithm is supported by the Provisionee.

If the Provisioner cannot retrieve the public key using an OOB technology or the Provisioner has not accessed the Provisionee's public key via an OOB technology, or if the Provisioner does not use an OOB public key, then the Provisioner sets the Public Key field in the Provisioning Start PDU to zero and the public keys are
exchanged between the Provisioner and the Provisionee. For each such exchange, a new key pair shall be generated by the Provisioner and the Provisionee.

The Provisionee shall send its generated public key if the Public Key field in the Provisioning Start PDU is set to zero.

The message sequence for public key exchange when the Provisionee public key is unknown is illustrated by [Figure 5.17](index-en.html#UUID-e90dfe62-80ab-87d9-9cc7-e0a5510b8bf0_figure-idm4577035221137634118864837239 "Figure 5.17. Public key exchange when Provisionee public key is unknown").

|  |
| --- |
| Public key exchange when Provisionee public key is unknown |

Figure 5.17. Public key exchange when Provisionee public key is unknown

Otherwise, if the public key is available using an OOB technology and the Provisioner has accessed the device's public key via an OOB technology, then the Provisioner sets the Public Key field in the Provisioning Start PDU to 1, and a new key pair shall be generated by the Provisioner, and the public key of the generated key
pair shall be transmitted from the Provisioner to the Provisionee, and the public key read from the device using the appropriate OOB technology shall be used.

A Provisionee’s public key that is contained in a Device Certificate as specified in [Section 5.5.1](index-en.html#UUID-054195c8-b1c3-b7b4-4137-73c200e03e4e "5.5.1. Device Certificate"), and retrievable from the device over an established provisioning bearer (see
[Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")) or retrievable from the Internet (see [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet")), is considered to be available using an OOB technology when the Provisioner supports certificate-based provisioning.

The message sequence for public key exchange when the unprovisioned device public key is OOB is illustrated by [Figure 5.18](index-en.html#UUID-e90dfe62-80ab-87d9-9cc7-e0a5510b8bf0_figure-idm4550635131195234118866675019 "Figure 5.18. Public key exchange when Provisionee public key is OOB").

|  |
| --- |
| Public key exchange when Provisionee public key is OOB |

Figure 5.18. Public key exchange when Provisionee public key is OOB

The Provisioner and the Provisionee shall check whether the public key provided by the peer device or obtained OOB is valid (see [Section 5.4.3.1](index-en.html#UUID-ee2023fd-4e61-caf2-a069-46f2767ec63b "5.4.3.1. NIST P-256 elliptic curve definition")).

When the Provisioner receives an invalid public key or a public key that is equal to the Provisioner public key, then provisioning shall fail, and the Provisioner shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors"). When the Provisionee receives an invalid public key or a public key that is equal to the Provisionee public key, then provisioning shall fail and the Provisionee shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors") and should indicate the Invalid Format Error Code in the Provisioning Failed PDU.

After the public key is known and has been validated, the ECDHSecret shall be computed using the following formula:

|  |
| --- |
| *ECDHSecret=P256(private key, peer public key)* |

After the ECDHSecret is computed, the Provisioner and the Provisionee shall delete its private-public key pair that was generated in this step.

##### 5.4.2.4. Authentication

###### 5.4.2.4.1. AuthValue computation

Once the public key exchange has been performed, a confirmation exchange followed by a random number exchange is performed. The confirmation values are a cryptographic hash of all the values exchanged so far, the random number that is yet to be revealed, and the AuthValue. Once the random numbers are exchanged, each device
authenticates its peer.

The authentication value from the Authentication Method (Authentication with Output OOB, Authentication with Input OOB, or Authentication with Static OOB) is used in the AuthValue for the purpose of computing the confirmation value. If the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM, the confirmation value of the
Provisioner is a 128-bit value, the confirmation value of the Provisionee is a 128-bit value, and they are computed using:

|  |
| --- |
| *ConfirmationProvisioner=AES-CMACConfirmationKey (RandomProvisioner || AuthValue)* |

|  |
| --- |
| *ConfirmationProvisioner=AES-CMACConfirmationKey (RandomDevice || AuthValue)* |

Where:

|  |
| --- |
| *ConfirmationKey=k1(ECDHSecret, ConfirmationSalt, "prck")* |

|  |
| --- |
| *ConfirmationSalt=s1(ConfirmationInputs)* |

|  |
| --- |
| *ConfirmationInputs=ProvisioningInvitePDUValue || ProvisioningCapabilitiesPDUValue || ProvisioningStartPDUValue || PublicKeyProvisioner || PublicKeyDevice* |

If the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM, the confirmation value of the Provisioner is a 256-bit value, the confirmation value of the Provisionee is a 256-bit value, and they are computed using:

|  |
| --- |
| *ConfirmationProvisioner=HMAC-SHA-256ConfirmationKey (RandomProvisioner)* |

|  |
| --- |
| *ConfirmationDevice=HMAC-SHA-256ConfirmationKey (RandomDevice)* |

Where:

|  |
| --- |
| *ConfirmationKey=k5(ECDHSecret || AuthValue, ConfirmationSalt, "prck256")* |

|  |
| --- |
| *ConfirmationSalt=s2(ConfirmationInputs)* |

|  |
| --- |
| *ConfirmationInputs=ProvisionionInvitePDUValue || ProvisioningCapabilitiesPDUValue || ProvisioningStartPDUValue || PublicKeyProvisioner || PublicKeyDevice* |

The ProvisioningInvitePDUValue is the value of the Provisioning Invite PDU fields (excluding the opcode) that was sent or received.

The ProvisioningCapabilitiesPDUValue is the value of the Provisioning Capabilities PDU fields (excluding the opcode) that was sent or received.

The ProvisioningStartPDUValue is the value of the Provisioning Start PDU fields (excluding the opcode) that was sent or received.

The PublicKeyProvisioner is the value of the Public Key X and Public Key Y fields from the Public Key PDU that was sent by the Provisioner.

The PublicKeyDevice is the value of the Public Key X and Public Key Y fields from the Public Key PDU that was sent by the Provisionee or from the delivered OOB public key.

The RandomProvisioner is a string of random bits generated by the Provisioner’s random number generator. The random number generator shall be compatible with the requirements in Volume 2, Part H, Section 2 of the Core Specification [[1](index-en.html#idp254740)]. If
the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM, the RandomProvisioner is a 128-bit value. If the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM, the RandomProvisioner is a 256-bit value.

The RandomDevice is a string of random bits generated by the Provisionee’s random number generator. The random number generator shall be compatible with the requirements in Volume 2, Part H, Section 2 of the Core Specification [[1](index-en.html#idp254740)]. If the
Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM, the RandomDevice is a 128-bit value. If the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM, the RandomDevice is a 256-bit value.

If the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM, the AuthValue is a 128-bit value. If the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM, the AuthValue is a 256-bit value. The computation of AuthValue depends on the data type. There are three data type values defined: Binary, Numeric, and Alphanumeric.

If the Authentication Method field value is Authentication with No OOB, the data type is Numeric, and the authentication value is 0.

If the Authentication Method field value is Authentication with Static OOB, the data type and authentication value are transferred using an OOB technology.

If the Authentication Method field value is Authentication with Output OOB, the data type is defined by the Output OOB Action (see [Table 5.32](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.32 "Table 5.32. Output OOB Action values for the Authentication Action field ")) and the authentication value is transferred using the mechanism defined by the Authentication Action.

If the Authentication Method field value is Authentication with Input OOB, the data type is defined by the Input OOB Action (see [Table 5.34](index-en.html#UUID-3614f156-6482-0709-5cbe-d8462d40e430_Table_5.34 "Table 5.34. Input OOB Action values for the Authentication Action field ")) and the authentication value is transferred using the mechanism defined by the Authentication Action.

**Data type Binary** If the data type is Binary, the authentication value is an array of octets. The authentication value array shall be copied to the AuthValue. If the authentication value is shorter than the defined AuthValue size, the remaining bits shall be set to 0. If the
authentication value is longer than the defined AuthValue size, the array shall be trimmed by removing octets with indexes higher than needed.

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the authentication value is [0x12, 0x34, 0x56], the AuthValue is an array consisting of [0x12, 0x34, 0x56, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], and if the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM
and the authentication value is [0x78, 0x9A, 0xBC, 0xDE], the AuthValue is an array consisting of [0x78, 0x9A, 0xBC, 0xDE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00].

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the authentication value is [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13], the AuthValue is an array consisting of [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F].

**Data type Numeric** If the data type is Numeric and the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM, the authentication value is a number and shall be represented as an unsigned 128-bit value. If the data type is Numeric and the Algorithm field is
BTM_ECDH_P256_HMAC_SHA256_AES_CCM, the authentication value is a number and shall be represented as an unsigned 256-bit value.

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the Authentication with Output OOB method is used with the Output OOB Action as Blink and the output is a value of 5 (authentication value), then the AuthValue shall be 0x00000000000000000000000000000005. The AuthValue is then encoded as defined in
[Section 5.1](index-en.html#UUID-9afdc14b-1cab-1c9b-795a-3b342be36e2a "5.1. Endianness") to compute the confirmation values, resulting in an array consisting of [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05].

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the Authentication with Output OOB method is used with the Output OOB Action as Output Numeric and the displayed number is 019655 (authentication value), then the AuthValue shall be 0x00000000000000000000000000004CC7. The AuthValue is then encoded
as defined in [Section 5.1](index-en.html#UUID-9afdc14b-1cab-1c9b-795a-3b342be36e2a "5.1. Endianness") to compute the confirmation values, resulting in an array consisting of [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4C,
0xC7].

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the Authentication with No OOB method is used, the authentication value shall be set to 0x00000000000000000000000000000000, which means it is not authenticated, resulting in an AuthValue array consisting of [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00].

**Data type Alphanumeric** If the data type is Alphanumeric, the authentication value is an array of octets constructed from a string of ASCII codes of the characters. The authentication value array shall be copied to the AuthValue. If the authentication value is shorter than the
defined AuthValue size, the remaining octets shall be set to 0. If the authentication value is longer than the defined AuthValue size, the array shall be trimmed by removing octets with indexes higher than needed.

For example, if the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM and the Authentication with Output OOB method is used with the Output OOB Action as Output Alphanumeric and the displayed string is ”123ABC” (authentication value), then the AuthValue shall be 0x31323341424300000000000000000000, resulting in an array
consisting of [0x31, 0x32, 0x33, 0x41, 0x42, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00].

###### 5.4.2.4.2. Confirmation and random number exchange

To complete confirmation and random number exchange, the Provisioner and the Provisionee shall follow these steps:

1. When the confirmation value of the Provisioner is computed, the Provisioner shall send the ConfirmationProvisioner value to the Provisionee using the Provisioning Confirmation PDU.
2. When the Provisionee receives the Provisioning Confirmation PDU from the Provisioner, it shall compare the ConfirmationProvisioner and the ConfirmationDevice values.

   * If the values are not equal, the Provisionee shall send the ConfirmationDevice value to the Provisioner using the Provisioning Confirmation PDU.
   * If the values are equal, the provisioning protocol shall fail, and the Provisionee shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors") and should indicate the Invalid Format Error
     Code in the Provisioning Failed PDU.
3. When the Provisioner receives the Provisioning Confirmation PDU from the Provisionee, it shall compare the ConfirmationProvisioner and the ConfirmationDevice values.

   * If the values are not equal, the Provisioner shall send the RandomProvisioner value to the Provisionee using the Provisioning Random PDU.
   * If the values are equal, the provisioning protocol shall fail, and the Provisioner shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors").
4. When the Provisionee receives the Provisioning Random PDU from the Provisioner, it shall compute the ConfirmationProvisioner value by using the received RandomProvisioner value.

   * If the ConfirmationProvisioner value received is equal to the computed ConfirmationProvisioner, the Provisioner is authenticated, and the Provisionee shall send the RandomDevice value to the Provisioner using the Provisioning Random PDU.
   * If the ConfirmationProvisioner value received is not equal to the computed ConfirmationProvisioner, the provisioning protocol shall fail, and the Provisionee shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors") and should indicate the Confirmation Failed Error Code in the Provisioning Failed PDU.
5. When the Provisioner receives the Provisioning Random PDU from the Provisionee, it shall compute the ConfirmationDevice value by using the received RandomDevice value.

   * If the ConfirmationDevice value received is equal to the computed ConfirmationDevice, the Provisionee is authenticated.
   * If the ConfirmationDevice value received is not equal to the computed ConfirmationDevice, the provisioning protocol shall fail, and the Provisioner shall act as described in [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors").

###### 5.4.2.4.3. Authentication with Output OOB

If Output OOB authentication is used, then the Provisioning Start PDU would include a request to output either a single-digit or multiple-digit value on the Provisionee device by using a prescribed action. Examples of output actions may include making a noise, blinking a light, voice, or displaying symbols on a display.

For example, if the unprovisioned device is a door lock that includes an LED, then it would be possible to use the Output OOB authentication with the action that would blink that LED.

When the Authentication Method field value is Authentication with Output OOB and when the Output OOB Action for the Authentication Action value is equal to Blink, Beep, or Vibrate, then the Provisionee shall select a random integer between 1 and 10Authentication Size - 1 inclusive. That random number shall be
output as a sequence of events (e.g., by blinking, beeping, or vibrating with a duty cycle of 500 milliseconds on and 500 milliseconds off) with a gap of at least 3 seconds between sequences to allow the user to determine the end of the sequence. When the Output OOB Action for the Authentication Action value is equal to Output
Numeric, then the value is output (e.g., displayed or spoken) using a number of digits (i.e., ASCII character codes 0x30 to 0x39) determined by the Authentication Size value. When the Output OOB Action for the Authentication Action value is equal to Output Alphanumeric, then the value is output using a number of ASCII digits
and uppercase letters (i.e., ASCII character codes 0x30 to 0x39 and 0x41 to 0x5A) determined by the Authentication Size value.

The user of the Provisioner shall input the number observed to authenticate that Provisionee.

Once input of the number has been performed, a confirmation exchange followed by a random number exchange is performed (see [Section 5.4.2.4.2](index-en.html#UUID-178fb991-5791-9450-96f9-1bb5eec3f3d2 "5.4.2.4.2. Confirmation and random number exchange")). The
confirmation values are a cryptographic hash of all the values exchanged so far, the random number that is yet to be revealed, and the number that has been input. Once the random numbers are exchanged, each device can authenticate its peer.

The message sequence for Authentication with Output OOB is illustrated by [Figure 5.19](index-en.html#UUID-8791cfa4-50bb-f8ea-2981-9e97c8439f25_figure-idm4628614235321634118985125211 "Figure 5.19. Authentication with Output OOB").

|  |
| --- |
| Authentication with Output OOB |

Figure 5.19. Authentication with Output OOB

###### 5.4.2.4.4. Authentication with Input OOB

When the Authentication Method field value is Authentication with Input OOB and when the Input OOB Action for the Authentication Action value is equal to Push, then the Provisioner shall select a random integer between 1 and 10Authentication Size -1 inclusive. That random number shall be input by the number of
push actions. When the Input OOB Action for the Authentication Action value is equal to Twist, then the Provisioner shall select a random integer between 1 and 10Authentication Size -1 inclusive. That random number shall be input by the number of twist actions until the value on the control has been entered. When the
Input OOB Action for the Authentication Action value is equal to Input Numeric, the value is input by entering a number of digits (probably using a numeric keyboard) determined by the Authentication Size value. When the Input OOB Action for the Authentication Action value is equal to Input Alphanumeric, the value is input by
entering a number of ASCII digits and uppercase letters (probably using an alphanumeric keyboard) determined by the Authentication Size value.

The Provisioner shall then prompt the user to input that value into the Provisionee device by using an appropriate action.

When the Input OOB Action for the Authentication Action value is equal to Push or Twist, the value is considered to have been input after no further input actions are detected for more than 5 seconds. When the Input OOB Action for the Authentication Action value is equal to Input Numeric or Input Alphanumeric, the value is
considered to have been input locally on that device (e.g., by pressing an Enter key).

For example, if the unprovisioned device is a light switch, then it would allow the user to input the random number by pressing a button an appropriate number of times.

Once input of the number has been performed, the Provisionee shall send the Provisioning Input Complete PDU to the Provisioner to confirm that the Provisionee has an input value. A confirmation exchange followed by a random number exchange is performed (see [Section 5.4.2.4.2](index-en.html#UUID-178fb991-5791-9450-96f9-1bb5eec3f3d2 "5.4.2.4.2. Confirmation and random number exchange")). The confirmation values are a cryptographic hash of all the values exchanged so far, the random number that is yet to be revealed, and the number that has been input. Once the
random numbers are exchanged, each device can authenticate its peer.

The message sequence for Authentication with Input OOB is illustrated by [Figure 5.20](index-en.html#UUID-3c38c9aa-4408-044e-bf3d-b4ea41edda1a_figure-idm4577035255336034118987654141 "Figure 5.20. Authentication with Input OOB").

|  |
| --- |
| Authentication with Input OOB |

Figure 5.20. Authentication with Input OOB

###### 5.4.2.4.5. Authentication with No OOB and Authentication with Static OOB

When the Authentication Method field value is Authentication with No OOB or the Authentication Method field value is Authentication with Static OOB then the Provisioner shall immediately use the confirmation and random number exchanges (see [Section 5.4.2.4.2](index-en.html#UUID-178fb991-5791-9450-96f9-1bb5eec3f3d2 "5.4.2.4.2. Confirmation and random number exchange")). If a static OOB value is available, then this value shall be included as part of the confirmation value. If no static OOB value is available, then this value shall have a value
of zero.

The message sequence for Authentication with Static OOB or Authentication with No OOB is illustrated by [Figure 5.21](index-en.html#UUID-c3fa9047-24a8-3749-863e-0d57058c13e6_figure-idm4550634897672034118989888012 "Figure 5.21. Authentication with Static OOB or Authentication with No OOB").

|  |
| --- |
| Authentication with Static OOB or Authentication with No OOB |

Figure 5.21. Authentication with Static OOB or Authentication with No OOB

##### 5.4.2.5. Distribution of provisioning data

Once the Provisionee has been authenticated, the Provisioner and Provisionee shall use the calculated Diffie-Hellman shared secret ECDHSecret and generate a session key from that shared secret. That session key shall then be used to encrypt and authenticate the provisioning data. The Provisioner then shall send the
Provisioning Data PDU containing the encrypted and authenticated provisioning data to the Provisionee.

The provisioning data format is described in [Table 5.47](index-en.html#UUID-a5735c88-759a-4471-66c6-6cd945378174_Table_5.47 "Table 5.47. Provisioning data format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Network Key | 16 | NetKey | M |
| Key Index | 2 | Index of the NetKey | M |
| Flags | 1 | Flags bitmask | M |
| IV Index | 4 | Current value of the IV Index | M |
| Unicast Address | 2 | Unicast address of the primary element | M |

Table 5.47. Provisioning data format

The Network Key shall contain the NetKey.

The Key Index field shall identify the global NetKey Index of the NetKey and shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The values of the Flags field are defined in [Table 5.48](index-en.html#UUID-a5735c88-759a-4471-66c6-6cd945378174_Table_5.48 "Table 5.48. Flags field definition").

| Bits | Definition |
| --- | --- |
| 0 | Key Refresh Flag  0: Key Refresh Phase 0  1: Key Refresh Phase 2 |
| 1 | IV Update Flag  0: Normal Operation  1: IV Update in Progress |
| 2–7 | Reserved for Future Use |

Table 5.48. Flags field definition

The IV Index field shall contain the current value of the IV Index.

The Unicast Address shall contain the Unicast Address of the primary element of the node being added to the network.

The Session key shall be derived using the formula:

|  |
| --- |
| *ProvisioningSalt=s1(ConfirmationSalt || RandomProvisioner || RandomDevice)* |

|  |
| --- |
| *SessionKey=k1(ECDHSecret, ProvisioningSalt, "prsk")* |

The nonce shall be the 13 least significant octets of:

|  |
| --- |
| *SessionNonce=k1(ECDHSecret, ProvisioningSalt, "prsn")* |

The provisioning data shall be encrypted and authenticated using:

|  |
| --- |
| *Provisioning Data=Network Key || Key Index || Flags || IV Index || Unicast Address* |

|  |
| --- |
| *Encrypted Provisioning Data, Provisioning Data MIC=AES-CCMSessionKey (SessionNonce, Provisioning Data)* |

The size of the Provisioning Data MIC is 8 octets.

The Encrypted Provisioning Data and Provisioning Data MIC shall be used as fields in the Provisioning Data PDU. The Provisioner shall send the Provisioning Data PDU to the Provisionee.

The Provisionee shall then compute the device key as defined in [Section 3.9.6.1](index-en.html#UUID-6b7d377d-3452-3cc2-3729-e6cdf9d03e83 "3.9.6.1. Device key")

The message sequence for distribution of provisioning data is illustrated by [Figure 5.22](index-en.html#UUID-a5735c88-759a-4471-66c6-6cd945378174_figure-idm4577035250065634119216356646 "Figure 5.22. Distribution of provisioning data") below.

|  |
| --- |
| Distribution of provisioning data |

Figure 5.22. Distribution of provisioning data

The Provisioner and Provisionee calculate the device key using the k1 key derivation function based on the established Diffie-Hellman shared secret ECDHSecret.

Upon receiving the Provisioning Data PDU from the Provisioner, the Provisionee shall decrypt and authenticate the provisioning data. Upon successful authentication of the provisioning data, the Provisionee shall set the network key (identified by the Key Index), set the IV Index, set the IV Update procedure state based on the
IV Update Flag, set the Key Refresh Phase based on the Key Refresh Flag, and assign unicast addresses to all device elements starting from the primary element and using a consecutive range of addresses starting from the provided unicast address value. Upon successful completion of the address assigning procedure, the Provisionee
shall respond with a Provisioning Complete PDU to confirm that it has been provisioned. If the address assigning cannot be successfully completed, the Provisionee shall assume that provisioning failed and respond with a Provisioning Failed PDU with the Error Code parameter set to Cannot Assign Addresses.

### Note

Note: After processing the Provisioning Data PDU from the Provisioner, the 96-hour time limits for changing the IV Update procedure state, as defined in the IV Update procedure, do not apply.

Upon receiving the Provisioning Complete PDU from the Provisionee, the Provisioner shall assume that the provisioning process is completed successfully and the Provisionee is using a consecutive range of address starting from the value of the unicast address. The length of the address range is reported to the Provisioner in
Provisioning Capabilities PDU (see [Section 5.4.1.2](index-en.html#UUID-cceddea6-bc2f-3e4b-e358-64610271b335 "5.4.1.2. Provisioning Capabilities")). As a final step in procedure, the Provisioner shall disconnect the provisioning bearer. The Provisionee is now a node in
the mesh network.

The Provisioner shall not reuse unicast addresses that have been allocated to a Provisionee and sent in a Provisioning Data PDU unless the node to which the unicast addresses were previously assigned has been removed from the network and the current IV Index (in use during the Node Removal procedure) has been updated, as
required in [Section 3.11.7](index-en.html#UUID-676ac19a-a0b3-ee16-fd92-6f1bce988596 "3.11.7. Node Removal procedure"), or the Node Address Refresh procedure was executed and the current IV Index (in use during the Node Address Refresh procedure) has been updated, as
required in [Section 3.11.8.5](index-en.html#UUID-762eb7f5-76a1-6b72-8d69-a3dba41425c6 "3.11.8.5. Node Address Refresh procedure").

##### 5.4.2.6. Provisioning record retrieval over a provisioning bearer

Provisioning records are read-only data items that the Provisioner may retrieve from the Provisionee after establishing a provisioning bearer. The Provisioner may use the information contained within provisioning record data to manage the provisioning process. Provisioning records are defined in [Section 5.4.2.6.3](index-en.html#UUID-f8434c6f-6436-9dd9-42e8-8c2bb0d316b2 "5.4.2.6.3. Provisioning records").

Each provisioning record is identified by a 16-bit Record ID, which is an assigned number. See [Table 5.52](index-en.html#UUID-f8434c6f-6436-9dd9-42e8-8c2bb0d316b2_Table_5.52 "Table 5.52. Provisioning records") for the defined Record IDs.

###### 5.4.2.6.1. Provisioning record list retrieval

The Provisioner may retrieve the list of the Record IDs of the provisioning records stored on the Provisionee over an established provisioning bearer by sending a Provisioning Records Get PDU (see [Section 5.4.1.13](index-en.html#UUID-f532e069-5349-59de-4134-72b5faea23e4 "5.4.1.13. Provisioning Records Get")).

To retrieve the Record ID list, the Provisioner shall send a Provisioning Records Get PDU before it sends a Provisioning Invite PDU. A Provisionee that supports provisioning records shall respond to a Provisioning Records Get PDU with a Provisioning Records List PDU. The Provisioner shall not send a new PDU until it has
received a Provisioning Records List PDU in response to the previously sent request.

When a Provisionee receives a Provisioning Records Get PDU, and the Provisioning Invite PDU has not already been received after the most recent establishment of a provisioning bearer, then the Provisionee shall respond with a Provisioning Records List PDU with the fields set as defined in [Section 5.4.1.14](index-en.html#UUID-dc78a032-14ed-e031-382a-75a490f090b6 "5.4.1.14. Provisioning Records List").

When a Provisionee receives a Provisioning Records Get PDU, and the Provisioning Invite PDU has already been received after the most recent establishment of a provisioning bearer, this indicates that provisioning failed. The Provisionee shall respond with a Provisioning Failed PDU with the Error Code field set to Unexpected
PDU.

[Table 5.49](index-en.html#UUID-13530d3a-7c7f-cc8e-3330-16c278403c40_Table_5.49 "Table 5.49. Error conditions that lead to provisioning failure for a Provisioning Records Get PDU") defines error conditions that lead to provisioning failure for processing a
Provisioning Records Get PDU.

| Error Condition | Status Code Name  (see [Table 5.41](index-en.html#UUID-5d074ac9-4a6a-9f60-878b-c722d517214c_Table_5.41 "Table 5.41. Provisioning error codes")) |
| --- | --- |
| A Provisioning Records Get PDU was received after a Provisioning Invite PDU was received in the same provisioning session | Unexpected PDU |

Table 5.49. Error conditions that lead to provisioning failure for a Provisioning Records Get PDU

###### 5.4.2.6.2. Provisioning record data retrieval

The Provisioner may retrieve provisioning record data stored on the Provisionee over an established provisioning bearer by sending Provisioning Record Request PDUs (see [Section 5.4.1.11](index-en.html#UUID-ae152830-6598-f0db-79ca-84aeaa7c11ed "5.4.1.11. Provisioning Record Request")).

To retrieve a record, the Provisioner shall send Provisioning Record Request PDUs before sending a Provisioning Invite PDU. A Provisionee that supports provisioning records shall respond to a Provisioning Record Request PDU with a Provisioning Record Response PDU. The Provisioner shall not send a new PDU until it has
received a Provisioning Record Response PDU in response to the previously sent request.

The Provisioner may issue Provisioning Record Request PDUs multiple times in order to retrieve all fragments needed to reconstruct provisioning record data fully or in order to retrieve all records stored on a Provisionee.

When a Provisionee receives a Provisioning Record Request PDU, and the Provisioning Invite PDU has not already been received after the most recent establishment of a provisioning bearer, and the Provisioning Record Request PDU message is processed successfully (i.e., the received request meets all request validation
conditions listed in [Table 5.50](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.50 "Table 5.50. Request validation conditions for a Provisioning Record Request PDU")), then the Provisionee shall respond with a Provisioning Record Response PDU with
the Status field set to Success and the other fields set as defined in [Section 5.4.1.12](index-en.html#UUID-31c8398d-0c9d-8fc6-9008-7ed602faf9b4 "5.4.1.12. Provisioning Record Response").

When a Provisionee receives a Provisioning Record Request PDU, and the Provisioning Invite PDU has not already been received after the most recent establishment of a provisioning bearer, and the Provisioning Record Request PDU message is not processed successfully (i.e., the received request does not meet all request
validation conditions listed in [Table 5.50](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.50 "Table 5.50. Request validation conditions for a Provisioning Record Request PDU")), then the Provisionee shall respond with a Provisioning Record
Response PDU with the Status field set as defined in [Table 5.50](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.50 "Table 5.50. Request validation conditions for a Provisioning Record Request PDU") and the other fields set as defined in [Section 5.4.1.12](index-en.html#UUID-31c8398d-0c9d-8fc6-9008-7ed602faf9b4 "5.4.1.12. Provisioning Record Response").

[Table 5.50](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.50 "Table 5.50. Request validation conditions for a Provisioning Record Request PDU") defines request validation conditions for processing a Provisioning Record Request PDU and the
status codes used when validation conditions are not met.

| Request Validation Condition | Status Code Name  (see [Table 5.41](index-en.html#UUID-5d074ac9-4a6a-9f60-878b-c722d517214c_Table_5.41 "Table 5.41. Provisioning error codes")) |
| --- | --- |
| The record identified by the Record ID field is present on the device | Requested Record Is Not Present |
| The Fragment Offset field value is smaller than Total Length of the identified record | Requested Offset Is Out Of Bounds |

Table 5.50. Request validation conditions for a Provisioning Record Request PDU

When the Provisionee responds with a Provisioning Record Response PDU with the Status field set as defined in [Table 5.50](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.50 "Table 5.50. Request validation conditions for a Provisioning Record Request PDU"), provisioning of the Provisionee does not fail. The Provisioner can continue sending Provisioning Record Request PDUs, or can send a Provisioning Invite PDU.

When a Provisionee receives a Provisioning Record Request PDU, and the Provisioning Invite PDU has already been received after the most recent establishment of a provisioning bearer, this indicates that provisioning failed. The Provisionee shall respond with a Provisioning Failed PDU with the Error Code field set to
Unexpected PDU.

[Table 5.51](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Table_5.51 "Table 5.51. Error conditions that lead to provisioning failure for a Provisioning Record Request PDU") defines error conditions that result in provisioning failure for processing a
Provisioning Record Request PDU.

| Error Condition | Status Code Name  (see [Table 5.41](index-en.html#UUID-5d074ac9-4a6a-9f60-878b-c722d517214c_Table_5.41 "Table 5.41. Provisioning error codes")) |
| --- | --- |
| A Provisioning Record Request PDU was received after a Provisioning Invite PDU was received in the same provisioning session | Unexpected PDU |

Table 5.51. Error conditions that lead to provisioning failure for a Provisioning Record Request PDU

The message sequence for retrieving the provisioning records list and provisioning record data is illustrated by [Figure 5.23](index-en.html#UUID-9f28f344-6e44-93ea-098b-45635c4d7524_Figure_5.23 "Figure 5.23. Provisioning records list and provisioning data retrieval").

|  |
| --- |
| Provisioning records list and provisioning data retrieval |

Figure 5.23. Provisioning records list and provisioning data retrieval

###### 5.4.2.6.3. Provisioning records

This section contains the record definitions for the provisioning records. A summary of the provisioning records is shown in [Table 5.52](index-en.html#UUID-f8434c6f-6436-9dd9-42e8-8c2bb0d316b2_Table_5.52 "Table 5.52. Provisioning records").

| Record ID | Name | Requirement |
| --- | --- | --- |
| 0x0000 | Certificate-Based Provisioning Base URI | C.1 |
| 0x0001 | Device Certificate | C.1 |
| 0x0002 | Intermediate Certificate 1 | O |
| 0x0003 | Intermediate Certificate 2 | O |
| 0x0004 | Intermediate Certificate 3 | O |
| 0x0005 | Intermediate Certificate 4 | O |
| 0x0006 | Intermediate Certificate 5 | O |
| 0x0007 | Intermediate Certificate 6 | O |
| 0x0008 | Intermediate Certificate 7 | O |
| 0x0009 | Intermediate Certificate 8 | O |
| 0x000A | Intermediate Certificate 9 | O |
| 0x000B | Intermediate Certificate 10 | O |
| 0x000C | Intermediate Certificate 11 | O |
| 0x000D | Intermediate Certificate 12 | O |
| 0x000E | Intermediate Certificate 13 | O |
| 0x000F | Intermediate Certificate 14 | O |
| 0x0010 | Intermediate Certificate 15 | O |
| 0x0011 | Complete Local Name | O |
| 0x0012 | Appearance | O |

Table 5.52. Provisioning records

C.1:
:   If certificate-based provisioning is supported, the support of at least one of Certificate-Based Provisioning Base URI or Device Certificate records is mandatory, and the presence of the other is optional; otherwise, both records are optional

###### 5.4.2.6.3.1. Certificate-Based Provisioning Base URI record

The Certificate-Based Provisioning Base URI record represents the base URI of the location from which the Provisioner may retrieve the Device Certificate of a Provisionee, as well as optional intermediate certificates. The full Certificate-Based Provisioning URI is constructed from the Certificate-Based Provisioning Base
URI and query parameters appended to it (see [Section 5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction")).

The data contained in the Certificate-Based Provisioning Base URI is formatted as defined in [[5](index-en.html#idp254749)] for the URI data type.

###### 5.4.2.6.3.2. Device Certificate record

The Device Certificate record represents the Device Certificate of a Provisionee, which is stored on the Provisionee itself.

The data contained in the Device Certificate record is an X.509 certificate formatted using Distinguished Encoding Rules (DER).

###### 5.4.2.6.3.3. Intermediate Certificate records (Intermediate Certificate 1, Intermediate Certificate 2, … Intermediate Certificate 15)

The Intermediate Certificate records represent intermediate certificates that are used to check the Device Certificate of the Provisionee, which is stored on the Provisionee itself.

There are 15 intermediate certificate records, ranging from Intermediate Certificate 1 record to Intermediate Certificate 15 record.

The data contained in an Intermediate Certificate record is an X.509 certificate formatted using DER.

###### 5.4.2.6.3.4. Complete Local Name record

The Complete Local Name record represents the complete local name of the Provisionee. The format of the record shall be as defined in [[5](index-en.html#idp254749)] for the Complete Local Name data type. The value of the record shall be the same as the local name
assigned to the Provisionee.

###### 5.4.2.6.3.5. Appearance record

The Appearance record represents the external appearance of the Provisionee. The format of the record shall be as defined in [[5](index-en.html#idp254749)] for the Appearance data type. The value of the record shall be the same as the Appearance characteristic, as
defined in [[1](index-en.html#idp254740)].

###### 5.4.2.6.4. Certificate-Based Provisioning Base URI retrieval over a provisioning bearer

If the Provisionee supports certificate-based provisioning (see [Section 5.5](index-en.html#UUID-c4273f5f-99c7-93b9-7189-f6be4d7aa09b "5.5. Certificate-based provisioning")) and the Device Certificate (see [Section 5.5.1](index-en.html#UUID-054195c8-b1c3-b7b4-4137-73c200e03e4e "5.5.1. Device Certificate")), along with any number of intermediate certificates, is available on a server on the Internet, the Provisionee shall store the Certificate-Based Provisioning Base URI for the certificate server (see [Section 5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction")) in the Certificate-Based Provisioning Base URI record.

The Provisioner may use the mechanism defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") to retrieve the Certificate-Based Provisioning Base URI record value. After
the Provisioner retrieves the Certificate-Based Provisioning Base URI, it shall follow the procedure defined in [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet") to retrieve the Device
Certificate and any intermediate certificates it needs before provisioning the Provisionee and shall then follow the procedure defined in [Section 5.5](index-en.html#UUID-c4273f5f-99c7-93b9-7189-f6be4d7aa09b "5.5. Certificate-based provisioning") to provision the
Provisionee.

###### 5.4.2.6.5. Provisioning certificate retrieval over a provisioning bearer

If the Provisionee supports certificate-based provisioning (see [Section 5.5](index-en.html#UUID-c4273f5f-99c7-93b9-7189-f6be4d7aa09b "5.5. Certificate-based provisioning")) and stores its Device Certificate (see [Section 5.5.1](index-en.html#UUID-054195c8-b1c3-b7b4-4137-73c200e03e4e "5.5.1. Device Certificate")), along with zero to 15 intermediate certificates, on the device, the Provisionee shall store the certificate data in the records associated with the certificates (see [Table 5.53](index-en.html#UUID-d472e5bb-6890-3b46-dfe4-486596281737_Table_5.53 "Table 5.53. Records associated with certificates that are stored on the device")).

The Provisioner may use the mechanism defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") to retrieve values of provisioning records associated with the certificates
stored on the Provisionee. After the Provisioner retrieves the certificates, it shall follow the procedure defined in [Section 5.5](index-en.html#UUID-c4273f5f-99c7-93b9-7189-f6be4d7aa09b "5.5. Certificate-based provisioning") to provision the Provisionee.

[Table 5.53](index-en.html#UUID-d472e5bb-6890-3b46-dfe4-486596281737_Table_5.53 "Table 5.53. Records associated with certificates that are stored on the device") defines records assigned to certificates.

| Record | Description |
| --- | --- |
| Device Certificate | The Device Certificate, which contains the device public key |
| Intermediate Certificate 1 | The first intermediate certificate, which, if present, is used to sign the Device Certificate |
| Intermediate Certificate 2 | The second intermediate certificate, which, if present, is used to sign the first intermediate certificate |
| Intermediate Certificate 3 .. Intermediate Certificate 15 | The Nth intermediate certificate, which, if present, is used to sign the preceding intermediate certificate |

Table 5.53. Records associated with certificates that are stored on the device

If the Provisionee supports certificate-based provisioning and stores its Device Certificate as a provisioning record, it may also store as many as 15 intermediate certificates as additional provisioning records. The intermediate certificates are stored in an ordered list indexed from 1 to N, where N is the number of stored
intermediate certificates. The intermediate certificate stored with index 1 shall be used to validate the Device Certificate. When more than one intermediate certificate is stored, the certificate stored with index M shall be used to validate a certificate stored with index M - 1.

The first intermediate certificate is associated with the Intermediate Certificate 1 record, the second intermediate certificate is associated with the Intermediate Certificate 2 record and so on, up to the fifteenth intermediate certificate which is associated with the Intermediate Certificate 15 record.

When retrieving intermediate certificates, the Provisioner should retrieve the value of the Intermediate Certificate 1 record first, and, when needed, retrieve other intermediate certificate record values in sequential order.

Root certificates shall not be stored on the Provisionee. If the Provisionee responds to a Provisioning Record Request with root certificate data, the Provisioner shall treat that as a provisioning error (see [Section 5.4.4](index-en.html#UUID-074e8e4b-4daf-f77f-faca-88df08912297 "5.4.4. Provisioning errors")).

The Provisioner shall acquire the root certificate, as well as any intermediate certificates not stored on the Provisionee, by a mechanism other than the ones defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") and [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet").

#### 5.4.3. Provisioning security

All devices and Provisioners shall support the P-256 elliptic curve (see [Section 5.4.3.1](index-en.html#UUID-ee2023fd-4e61-caf2-a069-46f2767ec63b "5.4.3.1. NIST P-256 elliptic curve definition")).

##### 5.4.3.1. NIST P-256 elliptic curve definition

The P-256 elliptic curve is defined in FIPS 186-4 [[10](index-en.html#idp254762)].

Elliptic curves are specified by p, a, and b in the form of:

|  |
| --- |
| *E: y2=x3+ax+b (mod p)* |

For each value of b, a unique curve can be developed. For the P-256 elliptic curve:

|  |
| --- |
| *a=mod (-3,p)* |

|  |  |
| --- | --- |
|  | b is defined and its method of generation can be verified by using SHA-1 (with a given seed s and using *b2 c=-27 (mod p)*) |

The following parameters are given:

* The prime modulus p, order r, base point x-coordinate Gx, base point y- coordinate Gy.
* The integers p and r are given in decimal numeral; bit strings and field elements are given in hex.

  p = 115792089210356248762697446949407573530086143415290314195533631308867097853951

  r = 115792089210356248762697446949407573529996955224135760342422259061068512044369

  b = 5ac635d8 aa3a93e7 b3ebbd55 769886bc 651d06b0 cc53b0f6 3bce3c3e 27d2604b

  Gx = 6b17d1f2 e12c4247 f8bce6e5 63a440f2 77037d81 2deb33a0 f4a13945 d898c296

  Gy = 4fe342e2 fe1a7f9b 8ee7eb4a 7c0f9e16 2bce3357 6b315ece cbb64068 37bf51f5

The function P256 is defined as follows. Given an integer u, *0<u<r*, and a point V on the curve E, the value P256(u, V) is computed as the x-coordinate of the uth multiple uV of the point V.

The private keys shall be between 1 and r/2, where r is the Order of the Abelian Group on the elliptic curve (i.e., between 1 and 2256/2).

A valid public key *Q=(XQ, YQ)* is one where XQ and YQ are both in the range 0 to p - 1 and satisfy the equation *(YQ)2=(XQ)3+aXQ+b (mod p)* in the
relevant curve’s finite field.

### Note on Public Key Validation

Note: For additional information about public key validation, see NIST Special Publication 800-56A, Revision 3 [[11](index-en.html#idp254765)].

##### 5.4.3.2. Provisioning key derivation

[Figure 5.24](index-en.html#UUID-4bae9334-7ace-f98a-2db2-cf85a7ee883c_figure-idm457703527075683411933812234 "Figure 5.24. ConfirmationKey derivation") and [Figure 5.25](index-en.html#UUID-4bae9334-7ace-f98a-2db2-cf85a7ee883c_figure-idm452287372127363411933924241 "Figure 5.25. SessionKey and SessionNonce Key derivation") illustrate the derivation of the provisioning keys.

|  |
| --- |
| ConfirmationKey derivation |

Figure 5.24. ConfirmationKey derivation

![SessionKey and SessionNonce Key derivation](image/1671b81d86b92b.png)

Figure 5.25. SessionKey and SessionNonce Key derivation

#### 5.4.4. Provisioning errors

When the provisioning protocol fails for any reason, the Provisionee shall permanently delete any stored details. There is no recovery procedure and the whole provisioning procedure is started from the beginning if the Provisioner chooses to do so. The provisioning protocol treats fields in messages with Prohibited values as
errors. The protocol is asymmetric when handling fields with Reserved for Future Use values.

When the Provisionee or the Provisioner receives a message with a field set to a value that is Prohibited or with a bit set to 1 within a bitfield indicated as Prohibited, the provisioning protocol shall fail and the message shall be treated as an error in the provisioning protocol.

When the Provisionee receives a message with a field set to a value that is Reserved for Future Use or with a bit set to 1 within a bitfield indicated as Reserved for Future Use, the provisioning protocol shall fail and the message shall be treated as an error in the provisioning protocol.

The provisioning protocol is asymmetric when handling protocol errors. When the Provisioner encounters an error other than a timeout in the provisioning protocol, it shall immediately disconnect the provisioning bearer, providing the Fail reason. When the provisioning bearer closes unexpectedly, provisioning has failed.

When the Provisionee encounters an error other than a timeout in the provisioning protocol, the device shall send the Provisioning Failed PDU with an appropriate Error Code and shall wait for the closing of the provisioning bearer. At this time, any provisioning protocol PDU received from the Provisioner is considered
unexpected.

When the Provisionee or Provisioner encounters an error not defined by the provisioning protocol (e.g., out-of-memory, out-of-battery, or procedure canceled through the user interface), the device may close the provisioning bearer.

The Provisioner, upon receiving the Provisioning Failed PDU, shall assume that the provisioning failed and immediately disconnect the provisioning bearer.

The Provisioner and the Provisionee use the provisioning timer during the provisioning protocol PDU exchanges. The provisioning timer initial value shall be set to a minimum of 60 seconds. When the Authentication Method field value is Authentication with Output OOB or Authentication with Input OOB, the provisioning timer initial
value shall be set to a minimum of 120 seconds to allow sufficient time for users to interact with the Provisioner or the Provisionee.

The Provisioner shall start the provisioning timer from the initial value when the Provisioner sends the first Provisioning PDU. The Provisionee shall start the provisioning timer from the initial value when the Provisionee receives the first Provisioning PDU. The provisioning timer shall start from the initial value whenever a
provisioning protocol PDU is sent or received.

When the provisioning process is completed successfully, the provisioning timer shall be stopped. When the provisioning timer expires, then provisioning fails, the provisioning bearer shall be disconnected with the Timeout reason, the Provisioner shall send a Provisioning Failed PDU, and the Provisionee shall not send a
Provisioning Failed PDU.

### 5.5. Certificate-based provisioning

When a device stores the Certificate-Based Provisioning Base URI (see [Section 5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction")) as a provisioning record, the Certificate-Based Provisioning Base URI
shall be retrievable from the device over an established provisioning bearer using the procedure defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer"). In that case, the
certificate data associated with the device shall be retrievable from the server indicated in the Certificate-Based Provisioning Base URI using the procedure defined in Section [5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet"), and the certificate data shall be retrieved before the Provisioner sends a Provisioning Invite PDU to the Provisionee.

When a device stores its Device Certificate and any intermediate certificates on the device as provisioning records, the certificate data associated with the device shall be retrievable from the device over an established provisioning bearer using the procedure defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer"), and the certificate data shall be retrieved before the Provisioner sends a Provisioning Invite PDU to the Provisionee.

The certificate data contains the Device Certificate and can contain intermediate certificates. [Section 5.5.1](index-en.html#UUID-054195c8-b1c3-b7b4-4137-73c200e03e4e "5.5.1. Device Certificate") defines requirements for a Device Certificate.

#### 5.5.1. Device Certificate

The phrase “Device Certificate” as specified in this document means a type of public key certificate with a specific format that contains the OOB Public Key of a device, as well as the UUID of the device and the identity of the vendor that manufactured the device.

A Device Certificate is an X.509 certificate, as defined in ITU-T X.509 [[19](index-en.html#idp254789)], formatted as specified in [Section 5.5.1.1](index-en.html#UUID-8a9291c7-c925-4fb2-61c2-5aac9c302520 "5.5.1.1. Certificate format").

The trust anchor (the entity for which trust is implicit and not derived from some higher authority) of the Public Key Infrastructure (PKI) used in signing the Device Certificate shall either be a certification authority (CA) root certificate or a vendor root certificate. Intermediate certificates between the root certificate
and the Device Certificate may be present.

The Provisioner shall use the Certification Path Validation procedure defined in IETF RFC 5280 [[12](index-en.html#idp254768)], and updated by IETF RFC 6818 [[30](index-en.html#idp254821)], IETF RFC 8398 [[31](index-en.html#idp254824)], and IETF RFC 8399 [[32](index-en.html#idp254827)], to validate the Device Certificate before using the contained OOB Public Key in provisioning the device.

Device Certificates can be renewed. How Device Certificate renewals are processed is out of the scope of this specification.

Device Certificates can be revoked during their validity period. How Device Certificate revocations are processed is out of the scope of this specification.

##### 5.5.1.1. Certificate format

The format of an X.509 certificate used in a PKI is defined in IETF RFC 5280 [[12](index-en.html#idp254768)] and IETF RFC 6818 [[30](index-en.html#idp254821)]. Constraints on certificate fields, when used in a
Device Certificate for provisioning a node on a Bluetooth mesh network, are defined in Sections [5.5.1.1.1](index-en.html#UUID-bdb13ea6-2d17-0127-671b-5e385f416f81 "5.5.1.1.1. tbsCertificate field") through [5.5.1.1.4.26](index-en.html#UUID-5eb8f65b-fcb2-2fab-700c-0d52a729aabf "5.5.1.1.4.26. Subject information access extension").

Provisioners may enforce additional constraints.

###### 5.5.1.1.1. tbsCertificate field

The tbsCertificate (“to be signed” certificate) field shall be composed as defined in IETF RFC 5280 [[12](index-en.html#idp254768)], with the additional constraints for its components as defined in [5.5.1.1.4.1](index-en.html#UUID-0055de5b-393b-9a84-fcd2-38351c9c6dfa "5.5.1.1.4.1. version field") through [5.5.1.1.4.25](index-en.html#UUID-be41ffeb-da63-6af3-c744-15e81f359c30 "5.5.1.1.4.25. Authority information access extension").

###### 5.5.1.1.2. signatureAlgorithm field

The signatureAlgorithm field shall be set to the value “ecdsa-with-SHA256”, as defined in IETF RFC 5758 [[13](index-en.html#idp254771)].

###### 5.5.1.1.3. signatureValue field

The signatureValue field shall contain the computed signature value as defined in IETF RFC 5280 [[12](index-en.html#idp254768)].

###### 5.5.1.1.4. tbsCertificate field components

Constraints on the fields contained in the tbsCertificate field are described in the Sections [5.5.1.1.4.1](index-en.html#UUID-0055de5b-393b-9a84-fcd2-38351c9c6dfa "5.5.1.1.4.1. version field") through [5.5.1.1.4.25](index-en.html#UUID-be41ffeb-da63-6af3-c744-15e81f359c30 "5.5.1.1.4.25. Authority information access extension").

###### 5.5.1.1.4.1. version field

The version field shall be set to decimal value 2 (“v3”).

###### 5.5.1.1.4.2. serialNumber field

The serialNumber field shall meet the requirements defined in IETF RFC 5280 [[12](index-en.html#idp254768)].

###### 5.5.1.1.4.3. signature field

The signature field shall meet the requirements as defined in IETF RFC 5280 [[12](index-en.html#idp254768)].

###### 5.5.1.1.4.4. issuer field

As defined in IETF RFC 5280 [[12](index-en.html#idp254768)], the issuer field identifies the signer of the Device Certificate.

###### 5.5.1.1.4.5. validity field

The validity field shall meet the requirements defined in IETF RFC 5280 [[12](index-en.html#idp254768)], with the following additional constraints:

* The notBefore time value should be no earlier than the manufacturing date of the device.
* The notAfter time value shall be chosen by the vendor. The vendor should take into consideration the expected lifetime of the device as well as the certificate renewal and revocation policies associated with the Device Certificate.

###### 5.5.1.1.4.6. subject field

The subject field shall contain a valid distinguished name (DN), with the following restrictions:

* The Organization Name field of the DN shall be set to the name of the vendor organization.
* The Common Name field of the DN shall contain the Device UUID formatted in the canonical fields-and-hyphens format specified in ITU-T X.667 [[14](index-en.html#idp254774)].
* The Common Name field of the DN should contain the device’s CID value (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")). If present, the CID value shall be represented with the prefix “BCID:”,
  which shall be immediately followed by the CID value encoded using four hexadecimal digits in big-endian format.
* The Common Name field of the DN should contain the device’s PID value (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")). If present, the PID value shall be represented with the prefix “BPID:”,
  which shall be immediately followed by the PID value encoded using four hexadecimal digits in big-endian format.
* The Device UUID, CID representation, and PID representation shall be separated from each other using white-space characters.

  For example, assume that the Device UUID is b09dc847-5408-40cc-9c54-0fe8c87429e7, the device CID value is 32769, and the device PID value is 4095. These would be encoded as the following Common Name:

  |  |
  | --- |
  | `b09dc847-5408-40cc-9c54-0fe8c87429e7 BCID:8001 BPID:03ff` |

* Before using the OOB Public Key in the certificate when provisioning the device, the Provisioner shall check that the Device UUID in the Common Name field of the DN matches the UUID of the device being provisioned.
* The Provisioner may additionally check the Device UUID in the Common Name field of the DN in other ways. For example, the Provisioner could check the Device UUID against an accept list of Device UUIDs, if available.
* If present in the Common Name field of the DN, the CID value shall match the CID value recorded in the device’s composition data page 0.
* If present in the Common Name field of the DN, the PID value shall match the PID value recorded in the device’s composition data page 0.
* If the CID value is present in the Common Name field of the DN, the PID value shall also be present. Likewise, if the PID value is present in the Common Name field of the DN, the CID value shall also be present.
* A Provisioner may reject a certificate that does not contain the CID value and the PID value.
* Other fields of the DN may be checked by the Provisioner.

###### 5.5.1.1.4.7. subjectPublicKeyInfo field

The subjectPublicKeyInfo field shall be set as defined in IETF RFC 5280 [[12](index-en.html#idp254768)], with the following constraints:

* The algorithm field shall contain “id-ecPublicKey” as the algorithm object identifier and the secp256r1 curve as the parameters, as defined in IETF RFC 5480 [[23](index-en.html#idp254801)] and IETF RFC 8813 [[33](index-en.html#idp254830)].
* The subjectPublicKey field shall contain the OOB Public Key of the device.

###### 5.5.1.1.4.8. issuerUniqueID field

The issuerUniqueID field should not be present.

###### 5.5.1.1.4.9. subjectUniqueID field

The subjectUniqueID field should not be present.

###### 5.5.1.1.4.10. Authority key identifier extension

An authority key identifier extension may be present. If present, the authority key identifier shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.11. Subject key identifier extension

A subject key identifier extension may be present. If present, the subject key identifier shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.12. Key usage extension

A key usage extension shall be present. The keyAgreement bit defined in IETF RFC 5280 [[12](index-en.html#idp254768)] shall be set in the extension. No other bits shall be set in the extension.

###### 5.5.1.1.4.13. Certificate policies extension

A certificate policies extension should be present. If present, the certificate policies extension shall be marked as critical and shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] and IETF RFC 6818 [[30](index-en.html#idp254821)] without additional constraints.

A Provisioner may reject a Device Certificate that does not contain the certificate policies extension.

###### 5.5.1.1.4.14. Policy mappings extension

A policy mappings extension shall not be present.

###### 5.5.1.1.4.15. Subject alternative name extension

A subject alternative name extension shall not be present.

###### 5.5.1.1.4.16. Issuer alternative name extension

An issuer alternative name extension may be present. If present, the issuer alternative name extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.17. Subject directory attribute extension

A subject directory attribute extension may be present. If present, the subject directory attribute extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.18. Basic constraints extension

The basic constraints extension shall be present. The cA field value shall be present in the extension and shall be set to FALSE. The pathLenConstraint field shall not be present in the extension.

###### 5.5.1.1.4.19. Name constraints extension

The name constraints extension shall not be present.

###### 5.5.1.1.4.20. Policy constraints extension

The policy constraints extension shall not be present.

###### 5.5.1.1.4.21. Extended key usage extension

The extended key usage extension shall not be present.

###### 5.5.1.1.4.22. CRL distribution points extension

The certificate revocation list (CRL) distribution points extension may be present. If present, the CRL distribution points extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.23. Inhibit anyPolicy extension

The inhibit anyPolicy extension shall not be present.

###### 5.5.1.1.4.24. Freshest CRL extension

The freshest CRL extension may be present. If present, the freshest CRL extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.25. Authority information access extension

The authority information access extension may be present. If present, the authority information access extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

###### 5.5.1.1.4.26. Subject information access extension

The subject information access extension may be present. If present, the subject information access extension shall be used as defined in IETF RFC 5280 [[12](index-en.html#idp254768)] without additional constraints.

#### 5.5.2. Acquiring root and intermediate certificates

A Device Certificate may be issued either by a CA or by the device vendor. The root certificate of the certificate chain used in signing the Device Certificate may be owned either by a CA or by the vendor.

To perform path validation for the Device Certificate, the Provisioner needs the root certificate as well as any intermediate certificates used in issuing the Device Certificate.

Root and intermediate certificates of CAs usually are provided by the platform on which the Provisioner runs (e.g., by the mobile operating system). If the platform does not provide the CA root certificate or intermediate certificates needed for validation, the Provisioner can use a mechanism other than the ones defined in
[Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") and [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet") to acquire those certificates before starting to provision devices.

Vendor root and intermediate certificates typically are not provided by the platform and are acquired from the vendor. Vendor intermediate certificates may be retrieved from the vendor by the retrieval mechanism used for Device Certificates (see [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet")) or over an established provisioning bearer using Provisioning Record Request PDUs (see [Section 5.4.1.11](index-en.html#UUID-ae152830-6598-f0db-79ca-84aeaa7c11ed "5.4.1.11. Provisioning Record Request")). The Provisioner can use a mechanism other than the ones defined in [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") and [Section 5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet") to acquire the vendor root and intermediate
certificates.

### 5.6. Device Certificate retrieval over the Internet

Sections [5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction") through [5.6.4](index-en.html#UUID-6f60298f-ea05-a6cd-8459-d4f10f435005 "5.6.4. Response")
define how Device Certificates shall be retrieved over the Internet. The Device Certificates shall be retrieved using HTTP over Transport Layer Security (TLS) [[22](index-en.html#idp254798)]. The Device Certificate shall be referenced by Certificate-Based Provisioning URI,
which may be constructed from the query parameters, such as the Device UUID, and the Certificate-Based Provisioning Base URI obtained from a provisioning record (see [Section 5.4.2.6.1](index-en.html#UUID-13530d3a-7c7f-cc8e-3330-16c278403c40 "5.4.2.6.1. Provisioning record list retrieval")), an NFC tag (see [Section 5.7.1](index-en.html#UUID-3a9d143d-eaa8-aee6-5b12-8a050fb80f66 "5.7.1. Certificate-Based Provisioning Base URI stored on an NFC tag")), or a two-dimensional barcode (see
[Section 5.7.2](index-en.html#UUID-c842145a-1800-6d13-ddd7-3bcf7b231c8e "5.7.2. Certificate-Based Provisioning Base URI stored on a two-dimensional barcode")).

The Provisioner can check the server authenticity before making a request for certificate data. Likewise, the server can check the Provisioner authenticity and also control the Provisioner’s access to the certificate data. The methods used for checking peer authenticity and controlling access to data are outside the scope of this
specification.

#### 5.6.1. Certificate-Based Provisioning URI construction

Because the space available in a provisioning record, NFC tag, or 2D barcode can be limited, the Provisioner shall treat the acquired Certificate-Based Provisioning Base URI as a base only. The Provisioner shall append a query string component, which shall identify the device and the content to be retrieved, to the
Certificate-Based Provisioning Base URI to construct the full Certificate-Based Provisioning URI.

The query string component shall be composed of one or more queries that consist of key-value pairs. An equal sign (ASCII character 61) shall separate a key from its value. Key-value pairs shall be separated from each other by an ampersand (ASCII character 38).

##### 5.6.1.1. UUID query

The UUID query identifies the device for which data is being requested.

The UUID query shall appear one time in the query string.

The query key for the UUID query shall be “uuid”.

The query value shall be the Device UUID in the canonical format defined in ITU-T X.667 [[14](index-en.html#idp254774)].

##### 5.6.1.2. Content queries

Multiple data items may be available for a given device. Content queries identify the data items that are requested to be retrieved by use of query values specified in Sections [5.6.1.2.1](index-en.html#UUID-cb72aad9-2e18-e5d5-6bcf-d37f6d740e11 "5.6.1.2.1. Device Certificate query") through [5.6.1.2.3](index-en.html#UUID-3d41dd04-4bbc-2d1b-19cc-48581861d9c4 "5.6.1.2.3. Vendor-specific content query").

Content queries are optional, and may appear multiple times in the query string. If no content query is specified in the request, the request shall apply to all data that the server has for the device specified by the UUID query.

The query key for the content query shall be “content”.

###### 5.6.1.2.1. Device Certificate query

The query value “device-certificate” specifies that the Device Certificate shall be retrieved.

###### 5.6.1.2.2. Intermediate certificate query

The query value “vendor-intermediate-certs” specifies that a vendor’s intermediate certificates in the certificate chain, which are needed for path validation of the Device Certificate, shall be retrieved. The response shall not contain any root certificates; receiving a root certificate as a response from a server shall be
an error that causes provisioning to be terminated.

###### 5.6.1.2.3. Vendor-specific content query

The content query may contain vendor-specific content, and its retrieval is indicated by vendor-specific query values. A vendor-specific content query value shall begin with a prefix that consists of the vendor’s Bluetooth company identifier (see Bluetooth SIG Company Identifiers [[4](index-en.html#idp254746)]) encoded as four hexadecimal digits in big-endian format (i.e., most significant octet first) and a minus sign (ASCII character 45) so that the vendor can be unambiguously identified and name clashes can be avoided. Vendor-specific content shall not affect
certificate path validation.

For example, assume that the Device UUID is “b09dc847-5408-40cc-9c54-0fe8c87429e7” and the URI that the device has stored in the Certificate-Based Provisioning Base URI is “https://mesh.example.com/oob”. The Provisioner combines these to make the following Certificate-Based Provisioning URI for retrieving the Device
Certificate and a vendor-specific “metadata” content item with the hexadecimal company ID “0xabcd”:

|  |
| --- |
| `https://mesh.example.com/oob?uuid=b09dc847-5408-40cc-9c54-0fe8c87429e7&amp;content=device-certificate&amp;content=abcd-metadata` |

#### 5.6.2. Content types

The following Multipurpose Internet Mail Extensions (MIME) content types shall be used for OOB data:

* application/pkix-cert, as specified in IETF RFC 2585 [[15](index-en.html#idp254777)], for X.509 certificates encoded in DER format
* multipart/mixed for delivery of multiple data items in one response (for example, an X.509 certificate followed by vendor-specific metadata)

A response to a query for the intermediate certificates that are needed to validate the device public key certificate shall use the multipart/mixed content type; each intermediate certificate shall be one part of the multipart response.

Defining the content types of vendor-specific data items is outside the scope of this specification.

#### 5.6.3. Request

HTTP version 1.1 (HTTP/1.1) shall be used when making a request. The format of an HTTP/1.1 request is defined in IETF RFC 7231 [[21](index-en.html#idp254795)].

The GET request method shall be used.

The Certificate-Based Provisioning Base URI schema, and by extension the Certificate-Based Provisioning URI schema, shall be “https://”. As defined in IETF RFC 7230 [[20](index-en.html#idp254792)], the schema is case-insensitive.

##### 5.6.3.1. Request headers

The format of the request headers is defined in the HTTP/1.1 specifications [[20](index-en.html#idp254792)][21], with the additional requirements and constraints that are defined in [Section 5.6.3.1.1](index-en.html#UUID-055857d2-6dc5-1c07-5aaa-d1a9e286f0e4 "5.6.3.1.1. Accept header") through [Section 5.6.3.1.3](index-en.html#UUID-eaf4e5a9-2cef-47d5-09f0-88a229ee9c46 "5.6.3.1.3. Connection header").

###### 5.6.3.1.1. Accept header

The Accept header shall either specify the content types that the Provisioner supports for the items it has requested or shall have the value “*/*”, indicating all content types are accepted.

The Provisioner shall process only data with the “application/pkix-cert” content type as a certificate. The Provisioner may indicate support for other content types, such as “text/html”, if it can process those content types. For example, a Provisioner might use the “text/html” content type when rendering a server error page
for the user.

If the Provisioner requests multiple data items, it shall be able to handle a MIME multipart response.

###### 5.6.3.1.2. Accept-Charset and Accept-Language headers

If the Provisioner is requesting information that might be localized (e.g., vendor-specific device metadata), it may indicate support for particular character sets and languages by using the Accept-Charset header and the Accept-Language header, respectively.

###### 5.6.3.1.3. Connection header

If the Provisioner requests data for multiple devices in quick succession, it should use HTTP/1.1 [[20](index-en.html#idp254792)] persistent connections. In this case, the Connection header value “close” shall not be used.

#### 5.6.4. Response

The Provisioner shall interpret the following status codes to have the following semantics:

* 200 OK: Request has succeeded, and the requested data will be delivered at least partially. If the Provisioner requests multiple data items by specifying the content query key multiple times, a 200 OK status code will be returned as long as even one requested data item can be found; it is up to the Provisioner to determine
  whether it can work with less data than it requested.
* 404 Not Found: The Device UUID is not valid, or none of the requested data items is available for the device.
* 405 Method Not Allowed: The request method was something other than GET.
* 410 Gone: The data has been invalidated at the server (e.g., because of certificate revocation) and is not available.
* 501 Not Implemented: The request contained a query key or query value not known by the server.

Other status codes may be used as needed; this specification does not define any semantic requirements for those status codes. HTTP status codes are defined in IETF RFC 7231 [[21](index-en.html#idp254795)].

##### 5.6.4.1. Response headers

Response headers shall be interpreted by the Provisioner according to the HTTP specifications [[20](index-en.html#idp254792)][[21](index-en.html#idp254795)].

##### 5.6.4.2. Response body

The response body shall be interpreted by the Provisioner according to the HTTP specifications [[20](index-en.html#idp254792)][[21](index-en.html#idp254795)].

If the response body contains unexpected or erroneous data in any of its parts, the whole response shall be considered invalid by the Provisioner, and the Provisioner shall not proceed with provisioning the device.

If an error occurred when processing a request, the server may send a message (e.g., an HTML page, along with the error code) if it can determine that the Provisioner can accept such content, as indicated by the Accept header in the request. The message may be localized based on the Accept-Charset and Accept-Language headers
sent by the Provisioner.

### 5.7. Additional Certificate-Based Provisioning Base URI sources

In addition to provisioning records, a Certificate-Based Provisioning Base URI may originate from additional sources—e.g., an NFC tag or a two-dimensional barcode associated with the device.

#### 5.7.1. Certificate-Based Provisioning Base URI stored on an NFC tag

Instead of being read from a provisioning record, the Certificate-Based Provisioning Base URI may be read from an NFC tag associated with the device (e.g., a tag on the device itself or on the packaging for the device).

NFC tag contents shall be formatted according to NFC Forum specifications [[16](index-en.html#idp254780)][[17](index-en.html#idp254783)][[18](index-en.html#idp254786)].

##### 5.7.1.1. URI and Smart Poster records

The smallest NFC tags can hold tens of bytes of data, which is enough for storing a short URI. A tag shall hold an NFC Data Exchange Format (NDEF) message containing either a URI record or a Smart Poster record as defined by the NFC Forum specifications [[17](index-en.html#idp254783)][[18](index-en.html#idp254786)], and the Provisioner shall retrieve the actual OOB data over the Internet based on the Certificate-Based Provisioning Base URI value read from an NFC tag as it would do when retrieving the Certificate-Based
Provisioning URI Base value from the device.

The URI or Smart Poster record on the tag shall contain the Certificate-Based Provisioning Base URI appended with a query component with the “uuid” key-value pair filled in with the Device UUID value, so that the Provisioner can read both the Certificate-Based Provisioning Base URI and the Device UUID from the same source.

After the Provisioner has acquired both the Certificate-Based Provisioning Base URI and the Device UUID, the Provisioner shall proceed with establishing a provisioning session for the device identified by the Device UUID and retrieving OOB data over the Internet as defined in Sections [5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction") through [5.6.4](index-en.html#UUID-6f60298f-ea05-a6cd-8459-d4f10f435005 "5.6.4. Response").

The Provisioner may use the additional data on a Smart Poster record in an application-specific manner—e.g., for displaying a message to the end user.

#### 5.7.2. Certificate-Based Provisioning Base URI stored on a two-dimensional barcode

Two-dimensional barcode technologies typically provide several encodings (e.g., ASCII text, binary data, and Unicode text) and error correction algorithms for the contained data. However, they do not necessarily provide any explicit means for recording application-level metadata such as the content type of the data. It is often
left to the application reading the barcode to understand the semantics of the data based on the appearance of the contents. For example, a URI can be recognized by the schema prefix that it contains (such as “https://”).

Any two-dimensional barcode technology that can be used to store a text string encoded in ASCII, in a subset of ASCII, or in binary format, and that allows automatic URI recognition by the URI schema prefix in the text string, may be used to store the URI.

##### 5.7.2.1. URI encoding

Instead of being read from a provisioning record, the Certificate-Based Provisioning Base URI may be read from a two-dimensional barcode associated with the device (e.g., on the device itself or in its packaging).

The Certificate-Based Provisioning Base URI shall be identified by its schema prefix, which is “https://”.

The barcode shall contain the Certificate-Based Provisioning Base URI appended with a query component with the “uuid” key-value pair filled in with the Device UUID value, so that the Provisioner can read both the Certificate-Based Provisioning Base URI and the Device UUID from the same source.

### Note on Certificate-Based Provisioning URI

Note: The benefit of reading the Certificate-Based Provisioning Base URI with a Device UUID from a barcode is that the user has a tangible physical object associated with the device that is being provisioned (the device itself, its packaging, or, for example, a paper slip in the packaging), which might be preferable to
choosing a beaconing device in the Provisioner’s user interface.

After the Provisioner has acquired both the Certificate-Based Provisioning Base URI and the Device UUID, the Provisioner shall proceed with establishing a provisioning session for the device identified by the Device UUID and retrieving OOB data over the Internet as defined in Sections [5.6.1](index-en.html#UUID-4aa02798-f71a-60a2-d744-cc8a3c159940 "5.6.1. Certificate-Based Provisioning URI construction") through [5.6.4](index-en.html#UUID-6f60298f-ea05-a6cd-8459-d4f10f435005 "5.6.4. Response").

By choosing the most efficient encoding that is able to output all of the characters required for the URI (including semicolons and slashes needed for the schema), the implementation can reduce the physical space needed for the 2D barcode.

### 5.8. Pre-fetched out-of-band data

In some environments, an Internet connection is not available. To enable provisioning in a non-connected environment, the OOB data may be retrieved in advance if the Provisioner knows the UUIDs of the devices that are to be provisioned. Because each Device Certificate contains the Device UUID in the Subject Name field, the
Provisioner can match the correct Device Certificate with the Device UUID that is read from an Unprovisioned Device beacon sent by a device waiting to be provisioned.

If certificates are retrieved in advance, there is a possibility that a certificate can be revoked after retrieval but before provisioning happens. In the absence of up-to-date certificate revocation information, the period after which pre-fetched certificates are considered stale and no longer valid for provisioning is
implementation-specific.
