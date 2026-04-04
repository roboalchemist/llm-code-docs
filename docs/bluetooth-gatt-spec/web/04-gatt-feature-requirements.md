# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 4. GATT feature requirements

### 4.1. Overview

There are 11 features defined in the GATT Profile:

1. Server Configuration
2. Primary Service Discovery
3. Relationship Discovery
4. Characteristic Discovery
5. Characteristic Descriptor Discovery
6. Reading a Characteristic Value
7. Writing a Characteristic Value
8. Notification of a Characteristic Value
9. Indication of a Characteristic Value
10. Reading a Characteristic Descriptor
11. Writing a Characteristic Descriptor

Each of the features is mapped to procedures and sub-procedures. These procedures and sub-procedures describe how the Attribute Protocol is used to accomplish the corresponding feature.

### 4.2. Feature support and procedure mapping

[Table 4.1](generic-attribute-profile--gatt-.html#UUID-d8c3186f-a603-00e3-8447-a3b9def32039_table-idm13358912569806 "Table 4.1: GATT feature mapping to procedures") maps each feature to the procedures used for that feature, and indicates whether the procedure is optional or mandatory for that feature. The procedures are described in the referenced section.

If an ATT PDU is supported on any ATT bearer, then it shall be supported on all supported ATT bearers with the following exceptions:

- The Exchange MTU sub-procedure shall only be supported on the LE Fixed Channel Unenhanced ATT bearer.
- The Signed Write Without Response sub-procedure shall only be supported on the LE Fixed Channel Unenhanced ATT bearer.

| Feature | Sub-Procedure | Ref. | Support in Client | Support in Server |
| --- | --- | --- | --- | --- |
| Server Configuration | Exchange MTU | [4.3.1](generic-attribute-profile--gatt-.html#UUID-68c91ae1-e9e9-f48a-a0ba-d712edf16172 "4.3.1 Exchange MTU") | O | O |
| Primary Service Discovery | Discover All Primary Services | [4.4.1](generic-attribute-profile--gatt-.html#UUID-8db5587d-f49d-6c82-73f3-23246f2dc4f2 "4.4.1 Discover All Primary Services") | O | M |
| Discover Primary Services By Service UUID | [4.4.2](generic-attribute-profile--gatt-.html#UUID-ab366af5-af65-6f9c-d957-0b8e7c905fa8 "4.4.2 Discover Primary Service by Service UUID") | O | M |
| Relationship Discovery | Find Included Services | [4.5.1](generic-attribute-profile--gatt-.html#UUID-257d4215-8c7b-6163-ceec-b86a74e62328 "4.5.1 Find Included Services") | O | M |
| Characteristic Discovery | Discover All Characteristic of a Service | [4.6.1](generic-attribute-profile--gatt-.html#UUID-acab67bd-4175-9a3e-c37e-8ae415495349 "4.6.1 Discover All Characteristics of a Service") | O | M |
| Discover Characteristic by UUID | [4.6.2](generic-attribute-profile--gatt-.html#UUID-b676406c-3e78-696a-29e8-e0f025f34426 "4.6.2 Discover Characteristics by UUID") | O | M |
| Characteristic Descriptor Discovery | Discover All Characteristic Descriptors | [4.7.1](generic-attribute-profile--gatt-.html#UUID-ca708893-b226-d29d-7308-bece78a8fe9c "4.7.1 Discover All Characteristic Descriptors") | O | M |
| Characteristic Value Read | Read Characteristic Value | [4.8.1](generic-attribute-profile--gatt-.html#UUID-90b3e212-b224-6a3f-8f2e-e6fb63641e31 "4.8.1 Read Characteristic Value") | O | M |
| Read Using Characteristic UUID | [4.8.2](generic-attribute-profile--gatt-.html#UUID-3569a57b-2934-e1bd-9527-3d591375eb8d "4.8.2 Read Using Characteristic UUID") | O | M |
| Read Long Characteristic Values | [4.8.3](generic-attribute-profile--gatt-.html#UUID-0a5cb6bc-58f4-5a47-2c66-889a1bc466d1 "4.8.3 Read Long Characteristic Values") | O | C.4 |
| Read Multiple Characteristic Values | [4.8.4](generic-attribute-profile--gatt-.html#UUID-2bf8cd06-0fa3-0d4b-1989-c622b8af05c2 "4.8.4 Read Multiple Characteristic Values") | O | O |
| Read Multiple Variable Length Characteristic Values | [4.8.5](generic-attribute-profile--gatt-.html#UUID-7189d557-5507-079f-b195-16a0fef3013e "4.8.5 Read Multiple Variable Length Characteristic Values") | O | C.4 |
| Characteristic Value Write | Write Without Response | [4.9.1](generic-attribute-profile--gatt-.html#UUID-9f1c2e38-8fbe-f60c-d885-076707c88a43 "4.9.1 Write Without Response") | O | C.1 |
| Signed Write Without Response | [4.9.2](generic-attribute-profile--gatt-.html#UUID-516bd731-2079-87f9-8002-c3ca92fbed4b "4.9.2 Signed Write Without Response") | O | O |
| Write Characteristic Value | [4.9.3](generic-attribute-profile--gatt-.html#UUID-ba4b856a-6994-01e4-97f6-357f9be40990 "4.9.3 Write Characteristic Value") | O | C.2 |
| Write Long Characteristic Values | [4.9.4](generic-attribute-profile--gatt-.html#UUID-6ab738ad-6d26-1da1-7417-e83da50e90c5 "4.9.4 Write Long Characteristic Values") | O | C.4 |
| Characteristic Value Reliable Writes | [4.9.5](generic-attribute-profile--gatt-.html#UUID-7fc3dafa-7199-3f9c-a137-1575597b2a8c "4.9.5 Reliable Writes") | O | O |
| Characteristic Value Notifications | Single Notifications | [4.10.1](generic-attribute-profile--gatt-.html#UUID-52ccee7c-a90c-b3d8-7173-5a34a371218d "4.10.1 Single Notifications") | C.4 | C.4 |
| Multiple Variable Length Notifications | [4.10.2](generic-attribute-profile--gatt-.html#UUID-ef60fab0-0495-034a-7f7d-574b6721bb69 "4.10.2 Multiple Variable Length Notifications") | C.4 | C.4 |
| Characteristic Value Indication | Indications | [4.11.1](generic-attribute-profile--gatt-.html#UUID-a5e37122-a510-899c-9c4d-a54fe324a7d8 "4.11.1 Indications") | M | C.3 |
| Characteristic Descriptor Value Read | Read Characteristic Descriptors | [4.12.1](generic-attribute-profile--gatt-.html#UUID-5a1a9293-614a-f4ed-7771-fd8b4143d076 "4.12.1 Read Characteristic Descriptors") | O | C.4 |
| Read Long Characteristic Descriptors | [4.12.2](generic-attribute-profile--gatt-.html#UUID-84794b9f-7220-7665-0f14-b7a462da94b7 "4.12.2 Read Long Characteristic Descriptors") | O | C.4 |
| Characteristic Descriptor Value Write | Write Characteristic Descriptors | [4.12.3](generic-attribute-profile--gatt-.html#UUID-0b0e2ea7-b310-8201-4ff4-cc43787afe88 "4.12.3 Write Characteristic Descriptors") | O | C.4 |
| Write Long Characteristic Descriptors | [4.12.4](generic-attribute-profile--gatt-.html#UUID-3e9d6b9c-cd01-2b51-a3d3-47741f30f086 "4.12.4 Write Long Characteristic Descriptors") | O | O |
| C.1:  Write Without Response is mandatory if Signed Write Without Response or Enhanced ATT Bearers are supported otherwise optional  C.2:  Write Characteristic Value is mandatory if Write Long Characteristic Values or Enhanced ATT Bearers are supported otherwise optional  C.3:  If *Service Changed Characteristic* is present, this feature is mandatory, otherwise optional.  C.4:  If Enhanced ATT Bearers are supported then this feature is mandatory, otherwise optional. | | | | |

Table 4.1: GATT feature mapping to procedures

### 4.3. Server configuration

This procedure is used by the client to configure the Attribute Protocol. This procedure has only one sub-procedure used to set the MTU sizes.

#### 4.3.1. Exchange MTU

This sub-procedure is used by the client to set the ATT\_MTU to the maximum possible value that can be supported by both devices when the client supports a value greater than the default ATT\_MTU for the Attribute Protocol. This sub-procedure shall only be initiated once during a connection.

This sub-procedure shall not be used on a BR/EDR physical link since the MTU size is negotiated using L2CAP channel configuration procedures.

The ATT\_EXCHANGE\_MTU\_REQ PDU is used by this sub-procedure. The Client Rx MTU parameter shall be set to the maximum MTU that this client can receive.

Two possible responses can be sent from the server for the ATT\_EXCHANGE\_­MTU\_­REQ PDU: ATT\_EXCHANGE\_­MTU\_­RSP and ATT\_ERROR\_­RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The server shall respond to this message with an ATT\_EXCHANGE\_MTU\_RSP PDU with the Server Rx MTU parameter set to the maximum MTU that this server can receive.

If the ATT\_ERROR\_RSP PDU is sent by the server with the Error Code parameter set to *Request Not Supported* (0x06), the *Attribute Opcode* is not supported and the default MTU shall be used.

Once the messages have been exchanged, the ATT\_MTU shall be set to the minimum of the Client Rx MTU and Server Rx MTU values.

![Exchange MTU](../image/1653f7aca10bad.png)

Figure 4.1: Exchange MTU

For example, in  [Figure 4.1](generic-attribute-profile--gatt-.html#UUID-68c91ae1-e9e9-f48a-a0ba-d712edf16172_figure-idm4508319755326433598988156958 "Figure 4.1: Exchange MTU"), based on the exchanged ATT\_MTU values, the ATT\_MTU would be 0x0032.

### 4.4. Primary Service Discovery

This procedure is used by a client to discover primary services on a server. Once the primary services are discovered, additional information about the primary services can be accessed using other procedures, including characteristic discovery and relationship discovery to find other related primary and secondary services.

There are two sub-procedures that can be used for primary service discovery: Discover All Primary Services and Discover Primary Services by Service UUID.

#### 4.4.1. Discover All Primary Services

This sub-procedure is used by a client to discover all the primary services on a server.

The ATT\_READ\_BY\_GROUP\_TYPE\_REQ PDU shall be used with the Attribute Type parameter set to the UUID for «Primary Service». The *Starting Handle* shall be set to 0x0001 and the *Ending Handle* shall be set to 0xFFFF.

Two possible responses can be sent from the server for the ATT\_READ\_­BY\_­GROUP\_­TYPE\_­REQ PDU: ATT\_READ\_­BY\_­GROUP\_­TYPE\_­RSP and ATT\_ERROR\_­RSP PDUs.

An ATT\_ERROR\_­RSP PDU is returned if an error occurred on the server.

The ATT\_READ\_­BY\_­GROUP\_­TYPE\_­RSP PDU returns a list of *Attribute Handle*, *End Group Handle*, and *Attribute Value* tuples corresponding to the services supported by the server. Each *Attribute Value* contained in the response is the Service UUID of a service supported by the server. The *Attribute Handle* is the handle for the service declaration. The *End Group Handle* is the handle of the last attribute within the service definition. The *End Group Handle* of the last service in a device can be 0xFFFF. The ATT\_READ\_BY\_GROUP\_TYPE\_REQ PDU shall be issued again with the *Starting Handle* set to one greater than the last *End Group Handle* in the ATT\_READ\_­BY\_­GROUP\_­TYPE\_­RSP PDU.

This sub-procedure is complete when the ATT\_ERROR\_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found* (0x0A) or when the *End Group Handle* in the *Read by Type Group Response* is 0xFFFF.

The sub-procedure may end early if a desired primary service is found prior to discovering all the primary services on the server.

The service declaration described in  [Section 3.1](generic-attribute-profile--gatt-.html#UUID-2148a3e6-91f7-e758-750f-8b14377cab6e "3.1 Service definition") specifies that the service declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.

![Discover All Primary Services example](../image/1653f7aca120dd.png)

Figure 4.2: Discover All Primary Services example

#### 4.4.2. Discover Primary Service by Service UUID

This sub-procedure is used by a client to discover a specific primary service on a server when only the Service UUID is known. The specific primary service may exist multiple times on a server. The primary service being discovered is identified by the service UUID.

The ATT\_FIND\_BY\_TYPE\_VALUE\_REQ PDU shall be used with the Attribute Type parameter set to the UUID for «Primary Service» and the *Attribute Value* set to the 16-bit Bluetooth UUID or 128-bit UUID for the specific primary service. The *Starting Handle* shall be set to 0x0001 and the *Ending Handle* shall be set to 0xFFFF.

Two possible responses can be sent from the server for the ATT\_FIND\_BY\_TYPE\_VALUE\_REQ PDU: ATT\_FIND\_BY\_TYPE\_VALUE\_RSP and ATT\_ERROR\_RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_FIND\_BY\_TYPE\_VALUE\_RSP PDU returns a list of *Attribute Handle* ranges. The *Attribute Handle* range is the starting handle and the ending handle of the service definition. The *End Group Handle* of the last service in a device can be 0xFFFF. If the *Attribute Handle* range for the Service UUID being searched is returned and the End Found Handle is not 0xFFFF, the ATT\_FIND\_BY\_TYPE\_VALUE\_REQ PDU may be issued again with the *Starting Handle* set to one greater than the last *Attribute Handle* range in the ATT\_FIND\_BY\_TYPE\_VALUE\_RSP PDU.

This sub-procedure is complete when the ATT\_ERROR\_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found* (0x0A) or when the *End Group Handle* in the ATT\_FIND\_BY\_TYPE\_VALUE\_RSP PDU is 0xFFFF.

The sub-procedure may end early if a desired primary service is found prior to discovering all the primary services of the specified service UUID supported on the server.

The service declaration described in  [Section 3.1](generic-attribute-profile--gatt-.html#UUID-2148a3e6-91f7-e758-750f-8b14377cab6e "3.1 Service definition") specifies that the service declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.

![Discover Primary Service by Service UUID example](../image/1653f7aca13517.png)

Figure 4.3: Discover Primary Service by Service UUID example

### 4.5. Relationship Discovery

This procedure is used by a client to discover service relationships to other services.

There is one sub-procedure that can be used for relationship discovery: Find Included Services.

#### 4.5.1. Find Included Services

This sub-procedure is used by a client to find include service declarations within a service definition on a server. The service specified is identified by the service handle range.

The ATT\_READ\_BY\_TYPE\_REQ PDU shall be used with the *Attribute Type* parameter set to the UUID for «Include» The *Starting Handle* shall be set to the starting handle of the specified service and the *Ending Handle* shall be set to the ending handle of the specified service. The sub-procedure may end early if a desired included service is found prior to discovering all the included services of the specified service supported on the server.

Two possible responses can be sent from the server for the ATT\_READ\_BY\_TYPE\_REQ PDU: ATT\_READ\_BY\_TYPE\_RSP and ATT\_ERROR\_RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_READ\_BY\_TYPE\_RSP PDU returns a set of *Attribute Handle* and *Attribute Value* pairs corresponding to the included services in the service definition. Each *Attribute Value* contained in the response is composed of the *Attribute Handle* of the included service declaration and the *End Group Handle*. If the service UUID is a 16-bit Bluetooth UUID it is also returned in the response. The ATT\_READ\_BY\_TYPE\_REQ PDU shall be issued again with the *Starting Handle* set to one greater than the last *Attribute Handle* in the ATT\_READ\_BY\_TYPE\_RSP PDU.

The sub-procedure is complete when either the ATT\_ERROR\_RSP PDU is received with the Error Code parameter set to *Attribute Not Found* (0x0A) or the ATT\_READ\_BY\_TYPE\_RSP PDU has an *Attribute Handle* of the included service declaration that is equal to the *Ending Handle* of the request.

To get the included service UUID when the included service uses a 128-bit UUID, the ATT\_READ\_REQ PDU is used. The *Attribute Handle* for the ATT\_READ\_REQ PDU is the *Attribute Handle* of the included service.

The include declaration described in  [Section 3.2](generic-attribute-profile--gatt-.html#UUID-a4a91ea7-a00f-77b6-9b37-fa0492451a21 "3.2 Include definition") specifies that the include declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.

![Find Included Services example](../image/1653f7aca14916.png)

Figure 4.4: Find Included Services example

### 4.6. Characteristic discovery

This procedure is used by a client to discover service characteristics on a server. Once the characteristics are discovered additional information about the characteristics can be discovered or accessed using other procedures.

There are two sub-procedures that can be used for characteristic discovery: Discover All Characteristics of a Service and Discover Characteristics by UUID.

#### 4.6.1. Discover All Characteristics of a Service

This sub-procedure is used by a client to find all the characteristic declarations within a service definition on a server when only the service handle range is known. The service specified is identified by the service handle range.

The ATT\_READ\_BY\_TYPE\_REQ PDU shall be used with the *Attribute Type* parameter set to the UUID for «Characteristic» The *Starting Handle* shall be set to starting handle of the specified service and the *Ending Handle* shall be set to the ending handle of the specified service.

Two possible responses can be sent from the server for the ATT\_READ\_­BY\_­TYPE\_­REQ PDU: ATT\_READ\_­BY\_­TYPE\_­RSP and ATT\_ERROR\_­RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_READ\_BY\_TYPE\_RSP PDU returns a list of *Attribute Handle* and *Attribute Value* pairs corresponding to the characteristics in the service definition. The *Attribute Handle* is the handle for the characteristic declaration. The *Attribute Value* is the Characteristic Properties, Characteristic Value Handle and Characteristic UUID. The ATT\_READ\_BY\_TYPE\_REQ PDU shall be issued again with the *Starting Handle* set to one greater than the last *Attribute Handle* in the ATT\_READ\_BY\_TYPE\_RSP PDU.

The sub-procedure is complete when the ATT\_ERROR\_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found* (0x0A) or the ATT\_READ\_BY\_TYPE\_RSP PDU has an *Attribute Handle* that is equal to the *Ending Handle* of the request.

The sub-procedure may end early if a desired characteristic is found prior to discovering all the characteristics of the specified service supported on the server.

# Note

Note: The characteristic declaration described in  [Section 3.3](generic-attribute-profile--gatt-.html#UUID-70d11f51-12cd-57a4-184a-fd8a4e0283f9 "3.3 Characteristic definition") specifies that the characteristic declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors should not occur.

![Discover All Characteristics of a Service example](../image/1653f7aca15d37.png)

Figure 4.5: Discover All Characteristics of a Service example

> **Note:** In this example «UUID1» and «UUID2» are 16 bits (2 octets).

If they were 128 bits (16 octets) then the ATT\_READ\_BY\_TYPE\_RSP PDU data would instead be:

0x15, 0x0203, 0x02, 0x0204, «UUID1», 0x0210, 0x02, 0x0212, «UUID2»

#### 4.6.2. Discover Characteristics by UUID

This sub-procedure is used by a client to discover service characteristics on a server when only the service handle ranges are known and the characteristic UUID is known. The specific service may exist multiple times on a server. The characteristic being discovered is identified by the characteristic UUID.

The ATT\_READ\_BY\_TYPE\_REQ PDU is used to perform the beginning of the sub-procedure. The *Attribute Type* is set to the UUID for «Characteristic» and the *Starting Handle* and *Ending Handle* parameters shall be set to the service handle range.

Two possible responses can be sent from the server for the ATT\_READ\_BY\_TYPE\_REQ PDU: ATT\_READ\_BY\_TYPE\_RSP and ATT\_ERROR\_RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_READ\_BY\_TYPE\_RSP PDU returns a list of *Attribute Handle* and *Attribute Value* pairs corresponding to the characteristics contained in the handle range provided. Each *Attribute Value* in the list is the *Attribute Value* for the characteristic declaration. The *Attribute Value* contains the characteristic properties, Characteristic *Value Handle* and characteristic UUID. The *Attribute Value* for each *Attribute Handle* and *Attribute Value* pairs are checked for a matching characteristic UUID. Once found, the sub-procedure continues until the end of the service handle range is exhausted. The ATT\_READ\_BY\_TYPE\_REQ PDU is issued again with the *Starting Handle* set to one greater than the last *Attribute Handle* in the ATT\_READ\_BY\_TYPE\_RSP PDU.

If the ATT\_ERROR\_RSP PDU is sent by the server with the Error Code parameter set to *Attribute Not Found* (0x0A), the characteristic does not exist on the server within the handle range provided.

The sub-procedure may end early if a desired characteristic is found prior to discovering all the characteristics for the specified service supported on the server.

The characteristic declaration described in  [Section 3.3](generic-attribute-profile--gatt-.html#UUID-70d11f51-12cd-57a4-184a-fd8a4e0283f9 "3.3 Characteristic definition") specifies that the characteristic declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.

![Discover Characteristics by UUID example](../image/1653f7aca171cc.png)

Figure 4.6: Discover Characteristics by UUID example

### 4.7. Characteristic Descriptor Discovery

This procedure is used by a client to discover characteristic descriptors of a characteristic. Once the characteristic descriptors are discovered additional information about the characteristic descriptors can be accessed using other procedures.

There is one sub-procedure that can be used for characteristic descriptor discovery: Discover All Characteristic Descriptors.

#### 4.7.1. Discover All Characteristic Descriptors

This sub-procedure is used by a client to find all the characteristic descriptor’s Attribute Handles and Attribute Types within a characteristic definition when only the characteristic handle range is known. The characteristic specified is identified by the characteristic handle range.

The ATT\_FIND\_INFORMATION\_REQ PDU shall be used with the Starting Handle set to the handle of the specified characteristic value + 1 and the *Ending Handle* set to the ending handle of the specified characteristic.

Two possible responses can be sent from the server for the ATT\_FIND\_INFORMATION\_REQ PDU: ATT\_FIND\_INFORMATION\_RSP and ATT\_ERROR\_RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_FIND\_INFORMATION\_RSP PDU returns a list of *Attribute Handle* and *Attribute Type* pairs corresponding to the characteristic descriptors in the characteristic definition. The *Attribute Handle* is the handle for the characteristic descriptor declaration. The *Attribute Type* is the characteristic descriptor UUID. The ATT\_FIND\_INFORMATION\_REQ PDU shall be issued again with the *Starting Handle* set to one greater than the last *Attribute Handle* in the ATT\_FIND\_INFORMATION\_RSP PDU.

The sub-procedure is complete when the ATT\_ERROR\_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found* (0x0A) or the ATT\_FIND\_INFORMATION\_RSP PDU has an *Attribute Handle* that is equal to the *Ending Handle* of the request.

The sub-procedure may end early if a desired Characteristic Descriptor is found prior to discovering all the characteristic descriptors of the specified characteristic.

![Discover All Characteristic Descriptors example](../image/1653f7aca1860f.png)

Figure 4.7: Discover All Characteristic Descriptors example

### 4.8. Characteristic Value Read

This procedure is used to read a *Characteristic Value* from a server. There are four sub-procedures that can be used to read a *Characteristic Value*: Read Characteristic Value, Read Using Characteristic UUID, Read Long Characteristic Values, and Read Multiple Characteristic Values.

#### 4.8.1. Read Characteristic Value

This sub-procedure is used to read a *Characteristic Value* from a server when the client knows the *Characteristic Value Handle*. The ATT\_READ\_REQ PDU is used with the *Attribute Handle* parameter set to the *Characteristic Value Handle*. The ATT\_READ\_RSP PDU returns the *Characteristic Value* in the *Attribute Value* parameter.

The ATT\_READ\_RSP PDU only contains the complete *Characteristic Value* if that is less than or equal to (ATT\_MTU – 1) octets in length. If the *Characteristic Value* is greater than (ATT\_MTU – 1) octets in length, the ATT\_READ\_RSP PDU only contains the first portion of the *Characteristic Value* and the *Read Long Characteristic Value* procedure may be used if the rest is required.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value*. The *Error Code* parameter is set as specified in the Attribute Protocol.

![Read Characteristic Value example](../image/1653f7aca19a1c.png)

Figure 4.8: Read Characteristic Value example

#### 4.8.2. Read Using Characteristic UUID

This sub-procedure is used to read a *Characteristic Value* from a server when the client only knows the characteristic UUID and does not know the handle of the characteristic.

The ATT\_READ\_BY\_TYPE\_REQ PDU is used to perform the sub-procedure. The Attribute Type is set to the known characteristic UUID and the Starting Handle and Ending Handle parameters shall be set to the range over which this read is to be performed. This is typically the handle range for the service in which the characteristic belongs.

Two possible responses can be sent from the server for the ATT\_READ\_BY\_TYPE\_REQ PDU: ATT\_READ\_BY\_TYPE\_RSP and ATT\_ERROR\_RSP PDUs.

An ATT\_ERROR\_RSP PDU is returned if an error occurred on the server.

The ATT\_READ\_BY\_TYPE\_RSP PDU returns a list of *Attribute Handle* and *Attribute Value* pairs corresponding to the first characteristics contained in the handle range that will fit into the ATT\_READ\_BY\_TYPE\_RSP PDU. This procedure does not return the complete list of all characteristics with the given characteristic UUID within the range of values. If such an operation is required, then the *Discover All Characteristics by UUID* sub procedure shall be used.

If the ATT\_ERROR\_RSP PDU is sent by the server with the Error Code parameter set to *Attribute Not Found* (0x0A), the characteristic does not exist on the server within the handle range provided.

![Read Using Characteristic UUID example](../image/1653f7aca1ae9d.png)

Figure 4.9: Read Using Characteristic UUID example

#### 4.8.3. Read Long Characteristic Values

This sub-procedure is used to read a *Characteristic Value* from a server when the client knows the *Characteristic Value Handle* and the length of the *Characteristic Value* is longer than can be sent in a single ATT\_READ\_RSP PDU.

The ATT\_READ\_REQ and ATT\_READ\_BLOB\_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle* shall be set to the *Characteristic Value Handle* of the *Characteristic Value* to be read. To read the complete *Characteristic Value* an ATT\_READ\_REQ PDU should be used for the first part of the value and ATT\_READ\_BLOB\_REQ PDUs shall used for the rest. The Value Offset parameter of each ATT\_READ\_BLOB\_REQ PDU shall be set to the offset of the next octet within the *Characteristic Value* that has yet to be read. The ATT\_READ\_BLOB\_REQ PDU is repeated until the ATT\_READ\_BLOB\_RSP PDU’s *Part Attribute Value* parameter is shorter than (ATT\_MTU – 1).

For each ATT\_READ\_BLOB\_REQ PDU a ATT\_READ\_BLOB\_RSP PDU is received with a portion of the Characteristic Value contained in the *Part Attribute Value* parameter.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_BLOB\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value*. The Error Code parameter is set as specified in the Attribute Protocol. If the *Characteristic Value* has a fixed length that is not longer than (ATT\_MTU – 1), then the server may respond to the first ATT\_READ\_BLOB\_REQ\_PDU with an ATT\_ERROR\_RSP PDU with the Error Code parameter set to *Attribute Not Long* (0x0B).

> **Note:** The ATT\_READ\_BLOB\_REQ PDU with zero offset may be used to read the first part of the value of the Attribute.

![Read Long Characteristic Values example](../image/1653f7aca1c299.png)

Figure 4.10: Read Long Characteristic Values example

#### 4.8.4. Read Multiple Characteristic Values

This sub-procedure is used to read multiple *Characteristic Values* from a server when the client knows the *Characteristic Value Handles*. The ATT\_READ\_MULTIPLE\_REQ PDU is used with the *Set Of Handles* parameter set to the *Characteristic Value Handles*. The ATT\_READ\_MULTIPLE\_RSP PDU returns the *Characteristic Values* in the *Set Of Values* parameter.

The ATT\_READ\_MULTIPLE\_RSP PDU only contains a set of *Characteristic Values* that is less than or equal to (ATT\_MTU – 1) octets in length. If the *Set Of Values* is greater than (ATT\_MTU – 1) octets in length, only the first (ATT\_MTU – 1) octets are included in the response.

> **Note:** A client should not request multiple *Characteristic Values* when the response’s *Set Of Values* parameter is equal to (ATT\_MTU – 1) octets in length since it is not possible to determine if the last *Characteristic Value* was read or additional *Characteristic Values* exist but were truncated.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_MULTIPLE\_RSP PDU if insufficient authentication, insufficient authorization, a too-short encryption key size, or insufficient encryption is used by the client, or if a read operation is not permitted on any of the *Characteristic Values*. The *Error Code* parameter is set as specified in the Attribute Protocol.

Refer to the Attribute Protocol specification for the format of the *Set Of Handles* and *Set Of Values* parameter.

![Read Multiple Characteristic Values example](../image/1653f7aca1d6e0.png)

Figure 4.11: Read Multiple Characteristic Values example

#### 4.8.5. Read Multiple Variable Length Characteristic Values

This sub-procedure is used to read multiple variable length Characteristic Values from a server when the client knows the Characteristic Value Handles. The Attribute Protocol ATT\_READ\_MULTIPLE\_VARIABLE\_REQ PDU is used with the Set Of Handles parameter set to the Characteristic Value Handles. The ATT\_READ\_MULTIPLE\_VARIABLE\_RSP PDU returns the Characteristic Values in the Length Value Tuple List parameter.

The ATT\_READ\_MULTIPLE\_VARIABLE\_RSP PDU can only contain a Length Value Tuple List that is less than or equal to (ATT\_MTU – 1) octets in length. If the Length Value Tuple List is greater than (ATT\_MTU – 1) octets in length, only the first (ATT\_MTU – 1) octets are included in the response.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_MULTIPLE\_VARIABLE\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size, or insufficient encryption is used by the client, or if a read operation is not permitted on any of the Characteristic Values. The Error Code parameter is set as specified in the Attribute Protocol.

Refer to the Attribute Protocol specification for the format of the Set Of Handles and Length Value Tuple List parameter.

![Read Multiple Variable Length Characteristic Values example](../image/1653f7aca1eb0d.png)

Figure 4.12: Read Multiple Variable Length Characteristic Values example

### 4.9. Characteristic Value Write

This procedure is used to write a *Characteristic Value* to a server.

There are five sub-procedures that can be used to write a *Characteristic Value*: Write Without Response, Signed Write Without Response, Write Characteristic Value, Write Long Characteristic Values and Reliable Writes.

#### 4.9.1. Write Without Response

This sub-procedure is used to write a *Characteristic Value* to a server when the client knows the *Characteristic Value Handle* and the client does not need an acknowledgment that the write was successfully performed. This sub-procedure only writes the first (ATT\_MTU – 3) octets of a *Characteristic Value*. This sub-procedure cannot be used to write a long characteristic; instead the *Write Long Characteristic Values* sub-procedure should be used.

The ATT\_WRITE\_CMD PDU is used for this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle*. The *Attribute Value* parameter shall be set to the new *Characteristic Value*.

If the *Characteristic Value* write request is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and no error shall be generated by the server.

![Write Without Response example](../image/1653f7aca1ff2a.png)

Figure 4.13: Write Without Response example

#### 4.9.2. Signed Write Without Response

This sub-procedure is used to write a *Characteristic Value* to a server when the client knows the *Characteristic Value Handle* and the ATT bearer is not encrypted. This sub-procedure shall only be used if the *Characteristic Properties* authenticated bit is enabled and the client and server device share a bond as defined in [[Vol 3] Part C, Generic Access Profile](generic-access-profile.html "Part C Generic Access Profile").

This sub-procedure only writes the first (ATT\_MTU – 15) octets of an *Attribute Value.* This sub-procedure cannot be used to write a long Attribute.

The ATT\_SIGNED\_WRITE\_CMD PDU is used for this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle*. The *Attribute Value* parameter shall be set to the new *Characteristic Value* authenticated by signing the value, as defined in the Security Manager [[Vol 3]
Part H,
Section 2.4.5](security-manager-specification.html#UUID-193f95ea-7252-1b51-853b-a1999393dddf "2.4.5 Signing algorithm").

If the authenticated *Characteristic Value* that is written is the wrong size, has an invalid value as defined by the profile, or the signed value does not authenticate the client, then the write shall not succeed and no error shall be generated by the server.

If a connection is already encrypted with LE security mode 1, level 2 or level 3 as defined in [[Vol 3]
Part C,
Section 10.2](generic-access-profile.html#UUID-a8b8b051-dfe4-037b-ec0b-3efdfd6d9d3c "10.2 LE security modes") then, a Write Without Response as defined in  [Section 4.9.1](generic-attribute-profile--gatt-.html#UUID-9f1c2e38-8fbe-f60c-d885-076707c88a43 "4.9.1 Write Without Response") shall be used instead of a Signed Write Without Response.

On BR/EDR, the ATT bearer is always encrypted, due to the use of Security Mode 4, therefore this sub-procedure shall not be used.

![Signed Write Without Response example](../image/1653f7aca2140b.png)

Figure 4.14: Signed Write Without Response example

#### 4.9.3. Write Characteristic Value

This sub-procedure is used to write a *Characteristic Value* to a server when the client knows the *Characteristic Value Handle*. This sub-procedure only writes the first (ATT\_MTU – 3) octets of a *Characteristic Value*. This sub-procedure cannot be used to write a long Attribute; instead the *Write Long Characteristic Values* sub-procedure should be used.

The ATT\_WRITE\_REQ PDU is used to for this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle*. The *Attribute Value* parameter shall be set to the new characteristic.

An ATT\_WRITE\_RSP PDU shall be sent by the server if the write of the *Characteristic Value* succeeded.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_WRITE\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value*. The Error Code parameter is set as specified in the Attribute Protocol. If the *Characteristic Value* that is written is the wrong size, or has an invalid value as defined by the profile, then the value shall not be written and an ATT\_ERROR\_RSP PDU shall be sent with the Error Code parameter set to *Application Error* (0x80 – 0x9F) by the server.

![Write Characteristic Value example](../image/1653f7aca228ae.png)

Figure 4.15: Write Characteristic Value example

#### 4.9.4. Write Long Characteristic Values

This sub-procedure is used to write a *Characteristic Value* to a server when the client knows the *Characteristic Value Handle* but the length of the *Characteristic Value* is longer than can be sent in a single ATT\_WRITE\_REQ PDU.

The ATT\_PREPARE\_WRITE\_REQ and ATT\_EXECUTE\_WRITE\_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle* of the *Characteristic Value* to be written. The *Part Attribute Value* parameter shall be set to the part of the *Attribute Value* that is being written. The *Value Offset* parameter shall be the offset within the *Characteristic Value* to be written. To write the complete *Characteristic Value* the offset should be set to 0x0000 for the first ATT\_PREPARE\_WRITE\_REQ PDU. The offset for subsequent ATT\_PREPARE\_WRITE\_REQ PDUs is the next octet that has yet to be written. The ATT\_PREPARE\_WRITE\_REQ PDU is repeated until the complete *Characteristic Value* has been transferred, after which an ATT\_EXECUTE\_WRITE\_REQ PDU is used to write the complete value.

> **Note:** The values in the ATT\_PREPARE\_WRITE\_RSP PDU do not need to be verified in this sub-procedure.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_PREPARE\_WRITE\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value*. The Error Code parameter is set as specified in the Attribute Protocol. If the *Attribute Value* that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and an ATT\_ERROR\_RSP PDU shall be sent with the Error Code parameter set to *Application Error* (0x80 – 0x9F) by the server.

![Write Long Characteristic Values example](../image/1653f7aca23cf9.png)

Figure 4.16: Write Long Characteristic Values example

#### 4.9.5. Reliable Writes

This sub-procedure is used to write a *Characteristic Value* to a server when the client knows the *Characteristic Value Handle*, and assurance is required that the correct *Characteristic Value* is going to be written by transferring the *Characteristic Value* to be written in both directions before the write is performed. A higher-layer protocol can also use this sub-procedure to write multiple values in order in a single operation.

The sub-procedure has two phases; the first phase prepares the *Characteristic Values* to be written. To do this, the client transfers the *Characteristic Values* to the server. The server checks the validity of the *Characteristic Values*. The client also checks each *Characteristic Value* to verify it was correctly received by the server using the server responses. Once this is complete, the second phase performs the execution of all of the prepared Characteristic Value writes on the server from this client.

In the first phase, the ATT\_PREPARE\_WRITE\_REQ PDU is used. The *Attribute Handle* shall be set to the *Characteristic Value Handle* that is to be prepared to write. The *Value Offset* and *Part Attribute Value* parameter shall be set to the new *Characteristic Value*.

Two possible responses can be sent from the server for the ATT\_PREPARE\_­­WRITE\_­­REQ PDU: ATT\_PREPARE\_­­WRITE\_­­RSP and ATT\_ERROR\_­­RSP PDUs.

If the number of prepared write requests exceeds the number of prepared writes supported, then an ATT\_ERROR\_RSP PDU with the Error Code parameter set to *Prepare Queue Full* (0x09) shall be sent by the server.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_PREPARE\_WRITE\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value*. The *Error Code* parameter is set as specified in the Attribute Protocol.

If a *Characteristic Value* is prepared two or more times during this sub-procedure, then all prepared values are written to the same *Characteristic Value* in the order that they were prepared.

If an ATT\_PREPARE\_WRITE\_RSP PDU is returned, then the *Value Offset* and *Part Attribute Value* parameter in the response shall be checked with the *Value Offset* and *Part Attribute Value* parameter that was sent in the ATT\_PREPARE\_WRITE\_REQ PDU; if they are different, then the value has been corrupted during transmission, and the sub-procedure shall be aborted by sending an ATT\_EXECUTE\_WRITE\_REQ PDU with the Flags parameter set to 0x00 to cancel all prepared writes. The complete sub-procedure may be restarted.

Multiple ATT\_PREPARE\_WRITE\_REQ PDUs can be sent by a client, each of which will be queued by the server.

In the second phase, the ATT\_EXECUTE\_WRITE\_REQ PDU is used. The Attribute Flags parameter shall be set to 0x01 to immediately write all pending prepared values in the order that they were prepared. The server shall write the prepared writes once it receives this request and shall only send the ATT\_EXECUTE\_WRITE\_RSP PDU once all the prepared values have been successfully written. If the *Characteristic Value* that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed, and an ATT\_ERROR\_RSP PDU with the Error Code parameter set to *Application Error* (0x80 – 0x9F) shall be sent by the server. The state of the Characteristic Values that were prepared is undefined.

![Reliable Writes example](../image/1653f7aca25146.png)

Figure 4.17: Reliable Writes example

### 4.10. Characteristic Value Notification

This procedure is used to notify a client of the value of a *Characteristic Value* from a server without expecting any Attribute Protocol layer acknowledgment that the notification was successfully received. There are two sub-procedures that can be used to notify a value: Single Notifications and Multiple Variable Length Notifications. Notifications can be configured using the Client Characteristic Configuration descriptor (See  [Section 3.3.3.3](generic-attribute-profile--gatt-.html#UUID-58fcda17-4f4b-3f53-3ca8-077bbfc77c5d "3.3.3.3 Client Characteristic Configuration")).

A profile defines when to use Notifications.

#### 4.10.1. Single Notifications

This sub-procedure is used when a server is configured to notify a *Characteristic Value* to a client.

The ATT\_HANDLE\_VALUE\_NTF PDU is used to perform this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle* being notified, and the *Attribute Value* parameter shall be set to the *Characteristic Value*.

![Notifications example](../image/1653f7aca265f9.png)

Figure 4.18: Notifications example

#### 4.10.2. Multiple Variable Length Notifications

This sub-procedure is used when a server is configured to notify multiple Characteristic Values to a client.

The Attribute Protocol ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDU is used to perform this sub-procedure. The Handle Length Value Tuple List parameter shall include the set of Characteristic Value Handles and associated Attribute Values.

![Multiple Variable Length Notifications example](../image/1653f7aca27a7c.png)

Figure 4.19: Multiple Variable Length Notifications example

### 4.11. Characteristic Value Indications

This procedure is used to indicate the *Characteristic Value* from a server to a client. There is one sub-procedure that can be used to indicate a value: Indications. Indications can be configured using the Client Characteristic Configuration descriptor (See  [Section 3.3.3.3](generic-attribute-profile--gatt-.html#UUID-58fcda17-4f4b-3f53-3ca8-077bbfc77c5d "3.3.3.3 Client Characteristic Configuration")).

A profile defines when to use Indications.

#### 4.11.1. Indications

This sub-procedure is used when a server is configured to indicate a *Characteristic Value* to a client and expects an Attribute Protocol layer acknowledgment that the indication was successfully received.

The ATT\_HANDLE\_VALUE\_IND PDU is used to perform this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Value Handle* being indicated, and the *Attribute Value* parameter shall be set to the *Characteristic Value*. Once the ATT\_HANDLE\_VALUE\_IND PDU is received by the client, the client shall respond with an ATT\_HANDLE\_VALUE\_CFM PDU.

![Indications example](../image/1653f7aca28fae.png)

Figure 4.20: Indications example

### 4.12. Characteristic Descriptors

This procedure is used to read and write characteristic descriptors on a server. There are two sub-procedures that can be used to read and write characteristic descriptors: Read Characteristic Descriptors and Write Characteristic Descriptors.

#### 4.12.1. Read Characteristic Descriptors

This sub-procedure is used to read a characteristic descriptor from a server when the client knows the characteristic descriptor declaration’s Attribute handle.

The ATT\_READ\_REQ PDU is used for this sub-procedure. The ATT\_READ\_REQ PDU is used with the *Attribute Handle* parameter set to the characteristic descriptor handle. The ATT\_READ\_RSP PDU returns the characteristic descriptor value in the *Attribute Value* parameter.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value*. The *Error Code* parameter is set accordingly.

![Read Characteristic Descriptors example](../image/1653f7aca2a47b.png)

Figure 4.21: Read Characteristic Descriptors example

#### 4.12.2. Read Long Characteristic Descriptors

This sub-procedure is used to read a characteristic descriptor from a server when the client knows the characteristic descriptor declaration’s Attribute handle and the length of the characteristic descriptor declaration is longer than can be sent in a single ATT\_READ\_RSP PDU.

The ATT\_READ\_BLOB\_REQ PDU is used to perform this sub-procedure. The Attribute Handle parameter shall be set to the characteristic descriptor handle. The Value Offset parameter shall be the offset within the characteristic descriptor to be read. To read the complete characteristic descriptor the offset should be set to 0x00 for the first ATT\_READ\_BLOB\_REQ PDU. The offset for subsequent ATT\_READ\_BLOB\_REQ PDUs is the next octet that has yet to be read. The ATT\_READ\_BLOB\_REQ PDU is repeated until the ATT\_READ\_BLOB\_RSP PDU’s Part Attribute Value parameter is zero or an ATT\_ERROR\_RSP PDU is sent by the server with the Error Code parameter set to *Invalid Offset* (0x07).

For each ATT\_READ\_BLOB\_REQ PDU an ATT\_READ\_BLOB\_RSP PDU is received with a portion of the characteristic descriptor value contained in the Part Attribute Value parameter.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_READ\_­BLOB\_­REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the characteristic descriptor. The Error Code parameter is set accordingly.

![Read Long Characteristic Descriptors example](../image/1653f7aca2b915.png)

Figure 4.22: Read Long Characteristic Descriptors example

> **Note:** The ATT\_READ\_BLOB\_REQ PDU may be used to read the remainder of an characteristic descriptor value where the first part was read using a simple ATT\_READ\_REQ PDU.

![Read Long Characteristic Descriptors (following simple read) example](../image/1653f7aca2cd8e.png)

Figure 4.23: Read Long Characteristic Descriptors (following simple read) example

#### 4.12.3. Write Characteristic Descriptors

This sub-procedure is used to write a characteristic descriptor value to a server when the client knows the characteristic descriptor handle.

The ATT\_WRITE\_REQ PDU is used for this sub-procedure. The *Attribute Handle* parameter shall be set to the characteristic descriptor handle. The *Attribute Value* parameter shall be set to the new characteristic descriptor value.

An ATT\_WRITE\_RSP PDU shall be sent by the server if the write of the characteristic descriptor value succeeded.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_WRITE\_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value*. The Error Code parameter shall be set as specified in the Attribute Protocol. If the characteristic descriptor value that is written is the wrong size, or has an invalid value as defined by the profile, or the operation is not permitted at this time then the value shall not be written and an ATT\_ERROR\_RSP PDU shall be sent with the Error Code parameter set to *Application Error* (0x80 – 0x9F) by the server.

![Write Characteristic Descriptors example](../image/1653f7aca2e230.png)

Figure 4.24: Write Characteristic Descriptors example

#### 4.12.4. Write Long Characteristic Descriptors

This sub-procedure is used to write a characteristic descriptor value to a server when the client knows the characteristic descriptor handle but the length of the characteristic descriptor value is longer than can be sent in a single ATT\_WRITE\_REQ PDU.

The ATT\_PREPARE\_WRITE\_REQ and ATT\_EXECUTE\_WRITE\_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle* parameter shall be set to the *Characteristic Descriptor Handle* of the *Characteristic Value* to be written. The *Part Attribute Value* parameter shall be set to the part of the *Attribute Value* that is being written. The *Value Offset* parameter shall be the offset within the *Characteristic Value* to be written. To write the complete *Characteristic Value* the offset should be set to 0x0000 for the first ATT\_PREPARE\_WRITE\_REQ PDU. The offset for subsequent ATT\_PREPARE\_WRITE\_REQ PDUs is the next octet that has yet to be written. The ATT\_PREPARE\_WRITE\_REQ PDU is repeated until the complete *Characteristic Value* has been transferred, after which an ATT\_EXECUTE\_WRITE\_REQ PDU is used to write the complete value.

> **Note:** The values in the ATT\_PREPARE\_WRITE\_RSP PDU do not need to be verified in this sub-procedure.

An ATT\_ERROR\_RSP PDU shall be sent by the server in response to the ATT\_PREPARE\_WRITE\_REQ or ATT\_EXECUTE\_WRITE\_REQ PDUs if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value*. The Error Code parameter is set as specified in the Attribute Protocol. If the *Attribute Value* that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and an ATT\_ERROR\_RSP PDU shall be sent with the Error Code parameter set to *Application Error* (0x80 – 0x9F) by the server.

![Write Long Characteristic Descriptors example](../image/1653f7aca2f679.png)

Figure 4.25: Write Long Characteristic Descriptors example

### 4.13. GATT procedure mapping to ATT protocol opcodes

[Table 4.2](generic-attribute-profile--gatt-.html#UUID-b5a253e2-98a4-63df-fc1a-e4555ec83ddc_table-idm13358912755578 "Table 4.2: GATT procedure mapping to ATT protocol opcodes") describes the mapping of the ATT protocol opcodes to the GATT procedures and sub-procedures. Only those portions of the ATT protocol requests, responses, notifications or indications necessary to implement the mandatory or supported optional sub-procedures is required.

| Feature | Sub-Procedure | ATT Protocol Opcodes |
| --- | --- | --- |
| **Server Configuration** | Exchange MTU | ATT\_EXCHANGE\_MTU\_REQ  ATT\_EXCHANGE\_MTU\_RSP  ATT\_ERROR\_RSP PDU |
| **Primary Service Discovery** | Discover All Primary Services | ATT\_READ\_BY\_GROUP\_TYPE\_REQ  ATT\_READ\_BY\_GROUP\_TYPE\_RSP  ATT\_ERROR\_RSP PDU |
| Discover Primary Services By Service UUID | ATT\_FIND\_BY\_TYPE\_VALUE\_REQ  ATT\_FIND\_BY\_TYPE\_VALUE\_RSP  ATT\_ERROR\_RSP PDU |
| **Relationship Discovery** | Find Included Services | ATT\_READ\_BY\_TYPE\_REQ  ATT\_READ\_BY\_TYPE\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Discovery** | Discover All Characteristic of a Service | ATT\_READ\_BY\_TYPE\_REQ  ATT\_READ\_BY\_TYPE\_RSP  ATT\_ERROR\_RSP PDU |
| Discover Characteristic by UUID | ATT\_READ\_BY\_TYPE\_REQ  ATT\_READ\_BY\_TYPE\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Descriptor Discovery** | Discover All Characteristic Descriptors | ATT\_FIND\_INFORMATION\_REQ  ATT\_FIND\_INFORMATION\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Value Read** | Read Characteristic Value | ATT\_READ\_REQ  ATT\_READ\_RSP  ATT\_ERROR\_RSP PDU |
| Read Using Characteristic UUID | ATT\_READ\_BY\_TYPE\_REQ  ATT\_READ\_BY\_TYPE\_RSP  ATT\_ERROR\_RSP PDU |
| Read Long Characteristic Values | ATT\_READ\_BLOB\_REQ  ATT\_READ\_BLOB\_RSP  ATT\_ERROR\_RSP PDU |
| Read Multiple Characteristic Values | ATT\_READ\_MULTIPLE\_REQ  ATT\_READ\_MULTIPLE\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Value Write** | Write Without Response | ATT\_WRITE\_CMD |
| Signed Write Without Response | ATT\_WRITE\_CMD |
| Write Characteristic Value | ATT\_WRITE\_REQ  ATT\_WRITE\_RSP  ATT\_ERROR\_RSP PDU |
| Write Long Characteristic Values | ATT\_PREPARE\_WRITE\_REQ  ATT\_PREPARE\_WRITE\_RSP  ATT\_EXECUTE\_WRITE\_REQ  ATT\_EXECUTE\_WRITE\_RSP  ATT\_ERROR\_RSP PDU |
| Characteristic Value Reliable Writes | ATT\_PREPARE\_WRITE\_REQ  ATT\_PREPARE\_WRITE\_RSP  ATT\_EXECUTE\_WRITE\_REQ  ATT\_EXECUTE\_WRITE\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Value Notification** | Single Notifications | ATT\_HANDLE\_VALUE\_NTF |
| Multiple Variable Length Notifications | ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF |
| **Characteristic Value Indication** | Indications | ATT\_HANDLE\_VALUE\_IND  ATT\_HANDLE\_VALUE\_CFM |
| **Characteristic Descriptor Value Read** | Read Characteristic Descriptors | ATT\_READ\_REQ  ATT\_READ\_RSP  ATT\_ERROR\_RSP PDU |
| Read Long Characteristic Descriptors | ATT\_READ\_BLOB\_REQ  ATT\_READ\_BLOB\_RSP  ATT\_ERROR\_RSP PDU |
| **Characteristic Descriptor Value Write** | Write Characteristic Descriptors | ATT\_WRITE\_REQ  ATT\_WRITE\_RSP  ATT\_ERROR\_RSP PDU |
| Write Long Characteristic Descriptors | ATT\_PREPARE\_WRITE\_REQ  ATT\_PREPARE\_WRITE\_RSP  ATT\_PREPARE\_WRITE\_REQ  ATT\_PREPARE\_WRITE\_RSP  ATT\_ERROR\_RSP PDU |

Table 4.2: GATT procedure mapping to ATT protocol opcodes

### 4.14. Procedure timeouts

GATT procedures are protected from failure with an Attribute Protocol transaction timeout.

If the Attribute Protocol transaction times out, the procedure shall be considered to have failed, and the local higher layer shall be notified. No further GATT procedures shall be performed on that ATT bearer. A new GATT procedure shall only be performed on another ATT bearer.
