# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 5. L2CAP interoperability requirements

The following default values shall be used by an implementation of this profile. The default values used may be different depending on the physical channel that the Attribute Protocol is being sent over.

### 5.1. BR/EDR L2CAP interoperability requirements

When using an Unenhanced ATT bearer, L2CAP connection-oriented channels over BR/EDR not in Enhanced Flow Control Mode can be used to transmit Attribute Protocol PDUs. These channels use the channel establishment procedure from L2CAP using the ATT fixed PSM (see [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)]) including the configuration procedure to determine the ATT\_MTU (see [[Vol 3]
Part A,
Section 5.1](logical-link-control-and-adaptation-protocol-specification.html#UUID-f83ad3d3-8a5d-73cd-153c-67ec4867fda3 "5.1 Maximum Transmission Unit (MTU)")). Therefore, the ATT bearer (or the logical link as referred to in the Attribute Protocol) is, in this case, an established L2CAP connection-oriented channel.

#### 5.1.1. ATT\_MTU

At the end of the L2CAP configuration phase, upon transition to the OPEN state, the ATT\_MTU for this ATT bearer shall be set to the minimum of the negotiated Maximum Transmission Unit configuration options.

# Note

Note: The minimum ATT\_MTU for BR/EDR is 48 octets, as defined by L2CAP in [[Vol 3]
Part A,
Section 5.1](logical-link-control-and-adaptation-protocol-specification.html#UUID-f83ad3d3-8a5d-73cd-153c-67ec4867fda3 "5.1 Maximum Transmission Unit (MTU)").

#### 5.1.2. BR/EDR channel requirements

All Attribute Protocol messages sent by GATT over an L2CAP channel are sent using a dynamic channel ID derived by connecting using a fixed PSM. The use of a fixed PSM allows rapid reconnection of the L2CAP channel for Attribute Protocol as a preliminary SDP query is not required.

All packets sent on this L2CAP channel shall be Attribute PDUs.

PDUs shall be reliably sent.

The flow specification for the Attribute Protocol shall be best effort.

If operating in Basic L2CAP mode, the information payload of the L2CAP B-frame shall be a single Attribute PDU.

The channel shall be encrypted. The Key\_Type shall be either an Unauthenticated Combination Key or an Authenticated Combination Key.

The L2CAP connection may be initiated by the client or by the server.

#### 5.1.3. [This section is no longer used]

### 5.2. LE L2CAP interoperability requirements

When using an Unenhanced ATT bearer, the channel used to carry Attribute Protocol PDUs over LE is the Attribute L2CAP fixed channel.

To terminate the ATT bearer, the physical channel has to be disconnected.

#### 5.2.1. ATT\_MTU

Both GATT Client and GATT Server implementations shall support an ATT\_MTU not less than the default value.

| Default Value | Value for LE |
| --- | --- |
| ATT\_MTU | 23 |

Table 5.1: LE L2CAP ATT\_MTU

#### 5.2.2. LE channel requirements

L2CAP fixed CID 0x0004 shall be used for the Attribute Protocol. All packets sent on this fixed channel shall be Attribute Protocol PDUs.

The flow specification for the Attribute Protocol shall be best effort.

PDUs shall be reliably sent, and not flushed.

The retransmission and flow control mode for this channel shall be Basic L2CAP mode

The default parameters for the payload of the L2CAP B-frame shall be a single Attribute PDU.

| Parameter | Value |
| --- | --- |
| MTU | 23 |
| Flush Timeout | 0xFFFF (Infinite) |
| QoS | Best Effort |
| Mode | Basic Mode |

Table 5.2: Attribute Protocol fixed channel configuration parameters

### 5.3. Enhanced ATT bearer L2CAP interoperability requirements

When using an Enhanced ATT bearer over BR/EDR, L2CAP connection-oriented channels in Enhanced Retransmission Mode are used to transmit Attribute Protocol PDUs. Such channels are established using L2CAP\_CONNECTION\_REQ packets.

When using an Enhanced ATT bearer over LE, L2CAP connection-oriented channels in Enhanced Credit Based Flow Control Mode are used to transmit Attribute Protocol PDUs. Such channels are established using L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ packets.

In both cases, the EATT fixed PSM [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)] is used and the ATT bearer is the established L2CAP connection-oriented channel.

Multiple L2CAP channels can be established between a client and a server.

#### 5.3.1. ATT\_MTU

The ATT\_MTU for the Enhanced ATT bearer shall be set to the minimum of the MTU field values of the two devices; these values come from the L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ and L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP signaling packets or the latest L2CAP\_CREDIT\_-BASED\_RECONFIGURE\_REQ packets.

> **Note:** The minimum ATT\_MTU for an Enhanced ATT bearer is 64 octets.

#### 5.3.2. Channel Requirements

All Attribute Protocol messages sent by GATT over an L2CAP Enhanced Credit Based Flow Control Mode channel are sent using one of the dynamic channel IDs derived by connecting using a fixed PSM.

All packets sent on this L2CAP channel shall be Attribute PDUs.

The flow specification for the Attribute Protocol shall be best effort.

The information payload of the L2CAP K-frame shall be a single Attribute PDU.

The channel shall be encrypted.

### 5.4. L2CAP collision mitigation

If both devices request L2CAP connections simultaneously and both devices have limited resources, a device may reject the incoming request and find its own request is also rejected. In this situation, the Central may retry immediately but the Peripheral shall wait a minimum of 100 ms before retrying; on LE connections, the Peripheral shall wait at least 2 × (*connPeripheralLatency* + 1) × *connInterval* if that is longer.

### 5.5. Bearer support

A GATT implementation supporting bearers over BR/EDR shall support at least one of Unenhanced and Enhanced ATT bearers over BR/EDR and may support both.

A GATT implementation supporting bearers over LE shall support Unenhanced ATT bearers over LE and may support Enhanced ATT bearers over LE.

> **Note:** A GATT implementation supporting bearers over both BR/EDR and LE therefore may support any combination of bearers provided that it supports Unenhanced ATT bearers over LE and at least one type of ATT bearer over BR/EDR.
