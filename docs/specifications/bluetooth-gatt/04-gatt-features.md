# GATT feature requirements

##### 4.1 Overview

There are 11 features defined in the GATT Profile:

-
Server Configuration

-
Primary Service Discovery

-
Relationship Discovery

-
Characteristic Discovery

-
Characteristic Descriptor Discovery

-
Reading a Characteristic Value

-
Writing a Characteristic Value

-
Notification of a Characteristic Value

-
Indication of a Characteristic Value

-
Reading a Characteristic Descriptor

-
Writing a Characteristic Descriptor

Each of the features is mapped to procedures and sub-procedures. These procedures and sub-procedures describe how the Attribute Protocol is used to accomplish the corresponding feature.

##### 4.2 Feature support and procedure mapping

Table 4.1 maps each feature to the procedures used for that feature, and indicates whether the procedure is optional or mandatory for that feature. The procedures are described in the referenced section.

If an ATT PDU is supported on any ATT bearer, then it shall be supported on all supported ATT bearers with the following exceptions:

-
The Exchange MTU sub-procedure shall only be supported on the LE Fixed Channel Unenhanced ATT bearer.

-
The Signed Write Without Response sub-procedure shall only be supported on the LE Fixed Channel Unenhanced ATT bearer.

Feature

Sub-Procedure

Ref.

Support in Client

Support in Server

Server Configuration

Exchange MTU

4.3.1

Primary Service Discovery

Discover All Primary Services

4.4.1

Discover Primary Services By Service UUID

4.4.2

Relationship Discovery

Find Included Services

4.5.1

Characteristic Discovery

Discover All Characteristic of a Service

4.6.1

Discover Characteristic by UUID

4.6.2

Characteristic Descriptor Discovery

Discover All Characteristic Descriptors

4.7.1

Characteristic Value Read

Read Characteristic Value

4.8.1

Read Using Characteristic UUID

4.8.2

Read Long Characteristic Values

4.8.3

C.4

Read Multiple Characteristic Values

4.8.4

Read Multiple Variable Length Characteristic Values

4.8.5

C.4

Characteristic Value Write

Write Without Response

4.9.1

C.1

Signed Write Without Response

4.9.2

Write Characteristic Value

4.9.3

C.2

Write Long Characteristic Values

4.9.4

C.4

Characteristic Value Reliable Writes

4.9.5

Characteristic Value Notifications

Single Notifications

4.10.1

C.4

C.4

Multiple Variable Length Notifications

4.10.2

C.4

C.4

Characteristic Value Indication

Indications

4.11.1

C.3

Characteristic Descriptor Value Read

Read Characteristic Descriptors

4.12.1

C.4

Read Long Characteristic Descriptors

4.12.2

C.4

Characteristic Descriptor Value Write

Write Characteristic Descriptors

4.12.3

C.4

Write Long Characteristic Descriptors

4.12.4

C.1:
Write Without Response is mandatory if Signed Write Without Response or Enhanced ATT Bearers are supported otherwise optional
C.2:
Write Characteristic Value is mandatory if Write Long Characteristic Values or Enhanced ATT Bearers are supported otherwise optional
C.3:
If *Service Changed Characteristic *is present, this feature is mandatory, otherwise optional.
C.4:
If Enhanced ATT Bearers are supported then this feature is mandatory, otherwise optional.
Table 4.1: GATT feature mapping to procedures

##### 4.3 Server configuration

This procedure is used by the client to configure the Attribute Protocol. This procedure has only one sub-procedure used to set the MTU sizes.

###### 4.3.1 Exchange MTU

This sub-procedure is used by the client to set the ATT_MTU to the maximum possible value that can be supported by both devices when the client supports a value greater than the default ATT_MTU for the Attribute Protocol. This sub-procedure shall only be initiated once during a connection.

This sub-procedure shall not be used on a BR/EDR physical link since the MTU size is negotiated using L2CAP channel configuration procedures.

The ATT_EXCHANGE_MTU_REQ PDU is used by this sub-procedure. The Client Rx MTU parameter shall be set to the maximum MTU that this client can receive.

Two possible responses can be sent from the server for the ATT_EXCHANGE_­MTU_­REQ PDU: ATT_EXCHANGE_­MTU_­RSP and ATT_ERROR_­RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The server shall respond to this message with an ATT_EXCHANGE_MTU_RSP PDU with the Server Rx MTU parameter set to the maximum MTU that this server can receive.

If the ATT_ERROR_RSP PDU is sent by the server with the Error Code parameter set to *Request Not Supported *(0x06), the *Attribute Opcode *is not supported and the default MTU shall be used.

Once the messages have been exchanged, the ATT_MTU shall be set to the minimum of the Client Rx MTU and Server Rx MTU values.
Figure 4.1: Exchange MTU

For example, in Figure 4.1 , based on the exchanged ATT_MTU values, the ATT_MTU would be 0x0032.

##### 4.4 Primary Service Discovery

This procedure is used by a client to discover primary services on a server. Once the primary services are discovered, additional information about the primary services can be accessed using other procedures, including characteristic discovery and relationship discovery to find other related primary and secondary services.

There are two sub-procedures that can be used for primary service discovery: Discover All Primary Services and Discover Primary Services by Service UUID.

###### 4.4.1 Discover All Primary Services

This sub-procedure is used by a client to discover all the primary services on a server.

The ATT_READ_BY_GROUP_TYPE_REQ PDU shall be used with the Attribute Type parameter set to the UUID for «Primary Service». The *Starting Handle *shall be set to 0x0001 and the *Ending Handle *shall be set to 0xFFFF.

Two possible responses can be sent from the server for the ATT_READ_­BY_­GROUP_­TYPE_­REQ PDU: ATT_READ_­BY_­GROUP_­TYPE_­RSP and ATT_ERROR_­RSP PDUs.

An ATT_ERROR_­RSP PDU is returned if an error occurred on the server.

The ATT_READ_­BY_­GROUP_­TYPE_­RSP PDU returns a list of *Attribute Handle **End Group Handle *, and *Attribute Value *tuples corresponding to the services supported by the server. Each *Attribute Value *contained in the response is the Service UUID of a service supported by the server. The *Attribute Handle *is the handle for the service declaration. The *End Group Handle *is the handle of the last attribute within the service definition. The *End Group Handle *of the last service in a device can be 0xFFFF. The ATT_READ_BY_GROUP_TYPE_REQ PDU shall be issued again with the *Starting Handle *set to one greater than the last *End Group Handle *in the ATT_READ_­BY_­GROUP_­TYPE_­RSP PDU.

This sub-procedure is complete when the ATT_ERROR_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found *(0x0A) or when the *End Group Handle *in the *Read by Type Group Response *is 0xFFFF.

The sub-procedure may end early if a desired primary service is found prior to discovering all the primary services on the server.

The service declaration described in Section 3.1 specifies that the service declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.
Figure 4.2: Discover All Primary Services example

###### 4.4.2 Discover Primary Service by Service UUID

This sub-procedure is used by a client to discover a specific primary service on a server when only the Service UUID is known. The specific primary service may exist multiple times on a server. The primary service being discovered is identified by the service UUID.

The ATT_FIND_BY_TYPE_VALUE_REQ PDU shall be used with the Attribute Type parameter set to the UUID for «Primary Service» and the *Attribute Value *set to the 16-bit Bluetooth UUID or 128-bit UUID for the specific primary service. The *Starting Handle *shall be set to 0x0001 and the *Ending Handle *shall be set to 0xFFFF.

Two possible responses can be sent from the server for the ATT_FIND_BY_TYPE_VALUE_REQ PDU: ATT_FIND_BY_TYPE_VALUE_RSP and ATT_ERROR_RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_FIND_BY_TYPE_VALUE_RSP PDU returns a list of *Attribute Handle *ranges. The *Attribute Handle *range is the starting handle and the ending handle of the service definition. The *End Group Handle *of the last service in a device can be 0xFFFF. If the *Attribute Handle *range for the Service UUID being searched is returned and the End Found Handle is not 0xFFFF, the ATT_FIND_BY_TYPE_VALUE_REQ PDU may be issued again with the *Starting Handle *set to one greater than the last *Attribute Handle *range in the ATT_FIND_BY_TYPE_VALUE_RSP PDU.

This sub-procedure is complete when the ATT_ERROR_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found *(0x0A) or when the *End Group Handle *in the ATT_FIND_BY_TYPE_VALUE_RSP PDU is 0xFFFF.

The sub-procedure may end early if a desired primary service is found prior to discovering all the primary services of the specified service UUID supported on the server.

The service declaration described in Section 3.1 specifies that the service declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.
Figure 4.3: Discover Primary Service by Service UUID example

##### 4.5 Relationship Discovery

This procedure is used by a client to discover service relationships to other services.

There is one sub-procedure that can be used for relationship discovery: Find Included Services.

###### 4.5.1 Find Included Services

This sub-procedure is used by a client to find include service declarations within a service definition on a server. The service specified is identified by the service handle range.

The ATT_READ_BY_TYPE_REQ PDU shall be used with the *Attribute Type *parameter set to the UUID for «Include» The *Starting Handle *shall be set to the starting handle of the specified service and the *Ending Handle *shall be set to the ending handle of the specified service. The sub-procedure may end early if a desired included service is found prior to discovering all the included services of the specified service supported on the server.

Two possible responses can be sent from the server for the ATT_READ_BY_TYPE_REQ PDU: ATT_READ_BY_TYPE_RSP and ATT_ERROR_RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_READ_BY_TYPE_RSP PDU returns a set of *Attribute Handle *and *Attribute Value *pairs corresponding to the included services in the service definition. Each *Attribute Value *contained in the response is composed of the *Attribute Handle *of the included service declaration and the *End Group Handle *. If the service UUID is a 16-bit Bluetooth UUID it is also returned in the response. The ATT_READ_BY_TYPE_REQ PDU shall be issued again with the *Starting Handle *set to one greater than the last *Attribute Handle *in the ATT_READ_BY_TYPE_RSP PDU.

The sub-procedure is complete when either the ATT_ERROR_RSP PDU is received with the Error Code parameter set to *Attribute Not Found *(0x0A) or the ATT_READ_BY_TYPE_RSP PDU has an *Attribute Handle *of the included service declaration that is equal to the *Ending Handle *of the request.

To get the included service UUID when the included service uses a 128-bit UUID, the ATT_READ_REQ PDU is used. The *Attribute Handle *for the ATT_READ_REQ PDU is the *Attribute Handle *of the included service.

The include declaration described in Section 3.2 specifies that the include declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.
Figure 4.4: Find Included Services example

##### 4.6 Characteristic discovery

This procedure is used by a client to discover service characteristics on a server. Once the characteristics are discovered additional information about the characteristics can be discovered or accessed using other procedures.

There are two sub-procedures that can be used for characteristic discovery: Discover All Characteristics of a Service and Discover Characteristics by UUID.

###### 4.6.1 Discover All Characteristics of a Service

This sub-procedure is used by a client to find all the characteristic declarations within a service definition on a server when only the service handle range is known. The service specified is identified by the service handle range.

The ATT_READ_BY_TYPE_REQ PDU shall be used with the *Attribute Type *parameter set to the UUID for «Characteristic» The *Starting Handle *shall be set to starting handle of the specified service and the *Ending Handle *shall be set to the ending handle of the specified service.

Two possible responses can be sent from the server for the ATT_READ_­BY_­TYPE_­REQ PDU: ATT_READ_­BY_­TYPE_­RSP and ATT_ERROR_­RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_READ_BY_TYPE_RSP PDU returns a list of *Attribute Handle *and *Attribute Value *pairs corresponding to the characteristics in the service definition. The *Attribute Handle *is the handle for the characteristic declaration. The *Attribute Value *is the Characteristic Properties, Characteristic Value Handle and Characteristic UUID. The ATT_READ_BY_TYPE_REQ PDU shall be issued again with the *Starting Handle *set to one greater than the last *Attribute Handle *in the ATT_READ_BY_TYPE_RSP PDU.

The sub-procedure is complete when the ATT_ERROR_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found *(0x0A) or the ATT_READ_BY_TYPE_RSP PDU has an *Attribute Handle *that is equal to the *Ending Handle *of the request.

The sub-procedure may end early if a desired characteristic is found prior to discovering all the characteristics of the specified service supported on the server.

### Note on characteristic declaration authentication

Note: The characteristic declaration described in Section 3.3 specifies that the characteristic declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors should not occur.
Figure 4.5: Discover All Characteristics of a Service example

### Note on UUID size in examples

Note: In this example «UUID1» and «UUID2» are 16 bits (2 octets).

If they were 128 bits (16 octets) then the ATT_READ_BY_TYPE_RSP PDU data would instead be:

0x15, 0x0203, 0x02, 0x0204, «UUID1», 0x0210, 0x02, 0x0212, «UUID2»

###### 4.6.2 Discover Characteristics by UUID

This sub-procedure is used by a client to discover service characteristics on a server when only the service handle ranges are known and the characteristic UUID is known. The specific service may exist multiple times on a server. The characteristic being discovered is identified by the characteristic UUID.

The ATT_READ_BY_TYPE_REQ PDU is used to perform the beginning of the sub-procedure. The *Attribute Type *is set to the UUID for «Characteristic» and the *Starting Handle *and *Ending Handle *parameters shall be set to the service handle range.

Two possible responses can be sent from the server for the ATT_READ_BY_TYPE_REQ PDU: ATT_READ_BY_TYPE_RSP and ATT_ERROR_RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_READ_BY_TYPE_RSP PDU returns a list of *Attribute Handle *and *Attribute Value *pairs corresponding to the characteristics contained in the handle range provided. Each *Attribute Value *in the list is the *Attribute Value *for the characteristic declaration. The *Attribute Value *contains the characteristic properties, Characteristic *Value Handle *and characteristic UUID. The *Attribute Value *for each *Attribute Handle *and *Attribute Value *pairs are checked for a matching characteristic UUID. Once found, the sub-procedure continues until the end of the service handle range is exhausted. The ATT_READ_BY_TYPE_REQ PDU is issued again with the *Starting Handle *set to one greater than the last *Attribute Handle *in the ATT_READ_BY_TYPE_RSP PDU.

If the ATT_ERROR_RSP PDU is sent by the server with the Error Code parameter set to *Attribute Not Found *(0x0A), the characteristic does not exist on the server within the handle range provided.

The sub-procedure may end early if a desired characteristic is found prior to discovering all the characteristics for the specified service supported on the server.

The characteristic declaration described in Section 3.3 specifies that the characteristic declaration is readable and requires no authentication or authorization, therefore insufficient authentication or read not permitted errors shall not occur.
Figure 4.6: Discover Characteristics by UUID example

##### 4.7 Characteristic Descriptor Discovery

This procedure is used by a client to discover characteristic descriptors of a characteristic. Once the characteristic descriptors are discovered additional information about the characteristic descriptors can be accessed using other procedures.

There is one sub-procedure that can be used for characteristic descriptor discovery: Discover All Characteristic Descriptors.

###### 4.7.1 Discover All Characteristic Descriptors

This sub-procedure is used by a client to find all the characteristic descriptor’s Attribute Handles and Attribute Types within a characteristic definition when only the characteristic handle range is known. The characteristic specified is identified by the characteristic handle range.

The ATT_FIND_INFORMATION_REQ PDU shall be used with the Starting Handle set to the handle of the specified characteristic value + 1 and the *Ending Handle *set to the ending handle of the specified characteristic.

Two possible responses can be sent from the server for the ATT_FIND_INFORMATION_REQ PDU: ATT_FIND_INFORMATION_RSP and ATT_ERROR_RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_FIND_INFORMATION_RSP PDU returns a list of *Attribute Handle *and *Attribute Type *pairs corresponding to the characteristic descriptors in the characteristic definition. The *Attribute Handle *is the handle for the characteristic descriptor declaration. The *Attribute Type *is the characteristic descriptor UUID. The ATT_FIND_INFORMATION_REQ PDU shall be issued again with the *Starting Handle *set to one greater than the last *Attribute Handle *in the ATT_FIND_INFORMATION_RSP PDU.

The sub-procedure is complete when the ATT_ERROR_RSP PDU is received and the Error Code parameter is set to *Attribute Not Found *(0x0A) or the ATT_FIND_INFORMATION_RSP PDU has an *Attribute Handle *that is equal to the *Ending Handle *of the request.

The sub-procedure may end early if a desired Characteristic Descriptor is found prior to discovering all the characteristic descriptors of the specified characteristic.
Figure 4.7: Discover All Characteristic Descriptors example

##### 4.8 Characteristic Value Read

This procedure is used to read a *Characteristic Value *from a server. There are four sub-procedures that can be used to read a *Characteristic Value *: Read Characteristic Value, Read Using Characteristic UUID, Read Long Characteristic Values, and Read Multiple Characteristic Values.

###### 4.8.1 Read Characteristic Value

This sub-procedure is used to read a *Characteristic Value *from a server when the client knows the *Characteristic Value Handle *. The ATT_READ_REQ PDU is used with the *Attribute Handle *parameter set to the *Characteristic Value Handle *. The ATT_READ_RSP PDU returns the *Characteristic Value *in the *Attribute Value *parameter.

The ATT_READ_RSP PDU only contains the complete *Characteristic Value *if that is less than or equal to (ATT_MTU – 1) octets in length. If the *Characteristic Value *is greater than (ATT_MTU – 1) octets in length, the ATT_READ_RSP PDU only contains the first portion of the *Characteristic Value *and the *Read Long Characteristic Value *procedure may be used if the rest is required.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value *. The *Error Code *parameter is set as specified in the Attribute Protocol.
Figure 4.8: Read Characteristic Value example

###### 4.8.2 Read Using Characteristic UUID

This sub-procedure is used to read a *Characteristic Value *from a server when the client only knows the characteristic UUID and does not know the handle of the characteristic.

The ATT_READ_BY_TYPE_REQ PDU is used to perform the sub-procedure. The Attribute Type is set to the known characteristic UUID and the Starting Handle and Ending Handle parameters shall be set to the range over which this read is to be performed. This is typically the handle range for the service in which the characteristic belongs.

Two possible responses can be sent from the server for the ATT_READ_BY_TYPE_REQ PDU: ATT_READ_BY_TYPE_RSP and ATT_ERROR_RSP PDUs.

An ATT_ERROR_RSP PDU is returned if an error occurred on the server.

The ATT_READ_BY_TYPE_RSP PDU returns a list of *Attribute Handle *and *Attribute Value *pairs corresponding to the first characteristics contained in the handle range that will fit into the ATT_READ_BY_TYPE_RSP PDU. This procedure does not return the complete list of all characteristics with the given characteristic UUID within the range of values. If such an operation is required, then the *Discover All Characteristics by UUID *sub procedure shall be used.

If the ATT_ERROR_RSP PDU is sent by the server with the Error Code parameter set to *Attribute Not Found *(0x0A), the characteristic does not exist on the server within the handle range provided.
Figure 4.9: Read Using Characteristic UUID example

###### 4.8.3 Read Long Characteristic Values

This sub-procedure is used to read a *Characteristic Value *from a server when the client knows the *Characteristic Value Handle *and the length of the *Characteristic Value *is longer than can be sent in a single ATT_READ_RSP PDU.

The ATT_READ_REQ and ATT_READ_BLOB_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle *shall be set to the *Characteristic Value Handle *of the *Characteristic Value *to be read. To read the complete *Characteristic Value *an ATT_READ_REQ PDU should be used for the first part of the value and ATT_READ_BLOB_REQ PDUs shall used for the rest. The Value Offset parameter of each ATT_READ_BLOB_REQ PDU shall be set to the offset of the next octet within the *Characteristic Value *that has yet to be read. The ATT_READ_BLOB_REQ PDU is repeated until the ATT_READ_BLOB_RSP PDU’s *Part Attribute Value *parameter is shorter than (ATT_MTU – 1).

For each ATT_READ_BLOB_REQ PDU a ATT_READ_BLOB_RSP PDU is received with a portion of the Characteristic Value contained in the *Part Attribute Value *parameter.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_BLOB_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value *. The Error Code parameter is set as specified in the Attribute Protocol. If the *Characteristic Value *has a fixed length that is not longer than (ATT_MTU – 1), then the server may respond to the first ATT_READ_BLOB_REQ_PDU with an ATT_ERROR_RSP PDU with the Error Code parameter set to *Attribute Not Long *(0x0B).

### Note on reading with zero offset

Note: The ATT_READ_BLOB_REQ PDU with zero offset may be used to read the first part of the value of the Attribute.
Figure 4.10: Read Long Characteristic Values example

###### 4.8.4 Read Multiple Characteristic Values

This sub-procedure is used to read multiple *Characteristic Values *from a server when the client knows the *Characteristic Value Handles *. The ATT_READ_MULTIPLE_REQ PDU is used with the *Set Of Handles *parameter set to the *Characteristic Value Handles *. The ATT_READ_MULTIPLE_RSP PDU returns the *Characteristic Values *in the *Set Of Values *parameter.

The ATT_READ_MULTIPLE_RSP PDU only contains a set of *Characteristic Values *that is less than or equal to (ATT_MTU – 1) octets in length. If the *Set Of Values *is greater than (ATT_MTU – 1) octets in length, only the first (ATT_MTU – 1) octets are included in the response.

### Note on truncated characteristic values

Note: A client should not request multiple *Characteristic Values *when the response’s *Set Of Values *parameter is equal to (ATT_MTU – 1) octets in length since it is not possible to determine if the last *Characteristic Value *was read or additional *Characteristic Values *exist but were truncated.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_MULTIPLE_RSP PDU if insufficient authentication, insufficient authorization, a too-short encryption key size, or insufficient encryption is used by the client, or if a read operation is not permitted on any of the *Characteristic Values *. The *Error Code *parameter is set as specified in the Attribute Protocol.

Refer to the Attribute Protocol specification for the format of the *Set Of Handles *and *Set Of Values *parameter.
Figure 4.11: Read Multiple Characteristic Values example

###### 4.8.5 Read Multiple Variable Length Characteristic Values

This sub-procedure is used to read multiple variable length Characteristic Values from a server when the client knows the Characteristic Value Handles. The Attribute Protocol ATT_READ_MULTIPLE_VARIABLE_REQ PDU is used with the Set Of Handles parameter set to the Characteristic Value Handles. The ATT_READ_MULTIPLE_VARIABLE_RSP PDU returns the Characteristic Values in the Length Value Tuple List parameter.

The ATT_READ_MULTIPLE_VARIABLE_RSP PDU can only contain a Length Value Tuple List that is less than or equal to (ATT_MTU – 1) octets in length. If the Length Value Tuple List is greater than (ATT_MTU – 1) octets in length, only the first (ATT_MTU – 1) octets are included in the response.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_MULTIPLE_VARIABLE_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size, or insufficient encryption is used by the client, or if a read operation is not permitted on any of the Characteristic Values. The Error Code parameter is set as specified in the Attribute Protocol.

Refer to the Attribute Protocol specification for the format of the Set Of Handles and Length Value Tuple List parameter.
Figure 4.12: Read Multiple Variable Length Characteristic Values example

##### 4.9 Characteristic Value Write

This procedure is used to write a *Characteristic Value *to a server.

There are five sub-procedures that can be used to write a *Characteristic Value *: Write Without Response, Signed Write Without Response, Write Characteristic Value, Write Long Characteristic Values and Reliable Writes.

###### 4.9.1 Write Without Response

This sub-procedure is used to write a *Characteristic Value *to a server when the client knows the *Characteristic Value Handle *and the client does not need an acknowledgment that the write was successfully performed. This sub-procedure only writes the first (ATT_MTU – 3) octets of a *Characteristic Value *. This sub-procedure cannot be used to write a long characteristic; instead the *Write Long Characteristic Values *sub-procedure should be used.

The ATT_WRITE_CMD PDU is used for this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *. The *Attribute Value *parameter shall be set to the new *Characteristic Value *

If the *Characteristic Value *write request is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and no error shall be generated by the server.
Figure 4.13: Write Without Response example

###### 4.9.2 Signed Write Without Response

This sub-procedure is used to write a *Characteristic Value *to a server when the client knows the *Characteristic Value Handle *and the ATT bearer is not encrypted. This sub-procedure shall only be used if the *Characteristic Properties *authenticated bit is enabled and the client and server device share a bond as defined in [Vol 3] Part C, Generic Access Profile

This sub-procedure only writes the first (ATT_MTU – 15) octets of an *Attribute Value. *This sub-procedure cannot be used to write a long Attribute.

The ATT_SIGNED_WRITE_CMD PDU is used for this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *. The *Attribute Value *parameter shall be set to the new *Characteristic Value *authenticated by signing the value, as defined in the Security Manager [Vol 3]
 Part H,
 Section 2.4.5

If the authenticated *Characteristic Value *that is written is the wrong size, has an invalid value as defined by the profile, or the signed value does not authenticate the client, then the write shall not succeed and no error shall be generated by the server.

If a connection is already encrypted with LE security mode 1, level 2 or level 3 as defined in [Vol 3]
 Part C,
 Section 10.2 then, a Write Without Response as defined in Section 4.9.1 shall be used instead of a Signed Write Without Response.

On BR/EDR, the ATT bearer is always encrypted, due to the use of Security Mode 4, therefore this sub-procedure shall not be used.
Figure 4.14: Signed Write Without Response example

###### 4.9.3 Write Characteristic Value

This sub-procedure is used to write a *Characteristic Value *to a server when the client knows the *Characteristic Value Handle *. This sub-procedure only writes the first (ATT_MTU – 3) octets of a *Characteristic Value *. This sub-procedure cannot be used to write a long Attribute; instead the *Write Long Characteristic Values *sub-procedure should be used.

The ATT_WRITE_REQ PDU is used to for this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *. The *Attribute Value *parameter shall be set to the new characteristic.

An ATT_WRITE_RSP PDU shall be sent by the server if the write of the *Characteristic Value *succeeded.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_WRITE_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value *. The Error Code parameter is set as specified in the Attribute Protocol. If the *Characteristic Value *that is written is the wrong size, or has an invalid value as defined by the profile, then the value shall not be written and an ATT_ERROR_RSP PDU shall be sent with the Error Code parameter set to *Application Error *(0x80 – 0x9F) by the server.
Figure 4.15: Write Characteristic Value example

###### 4.9.4 Write Long Characteristic Values

This sub-procedure is used to write a *Characteristic Value *to a server when the client knows the *Characteristic Value Handle *but the length of the *Characteristic Value *is longer than can be sent in a single ATT_WRITE_REQ PDU.

The ATT_PREPARE_WRITE_REQ and ATT_EXECUTE_WRITE_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *of the *Characteristic Value *to be written. The *Part Attribute Value *parameter shall be set to the part of the *Attribute Value *that is being written. The *Value Offset *parameter shall be the offset within the *Characteristic Value *to be written. To write the complete *Characteristic Value *the offset should be set to 0x0000 for the first ATT_PREPARE_WRITE_REQ PDU. The offset for subsequent ATT_PREPARE_WRITE_REQ PDUs is the next octet that has yet to be written. The ATT_PREPARE_WRITE_REQ PDU is repeated until the complete *Characteristic Value *has been transferred, after which an ATT_EXECUTE_WRITE_REQ PDU is used to write the complete value.

### Note on prepare write response verification

Note: The values in the ATT_PREPARE_WRITE_RSP PDU do not need to be verified in this sub-procedure.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_PREPARE_WRITE_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value *. The Error Code parameter is set as specified in the Attribute Protocol. If the *Attribute Value *that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and an ATT_ERROR_RSP PDU shall be sent with the Error Code parameter set to *Application Error *(0x80 – 0x9F) by the server.
Figure 4.16: Write Long Characteristic Values example

###### 4.9.5 Reliable Writes

This sub-procedure is used to write a *Characteristic Value *to a server when the client knows the *Characteristic Value Handle *, and assurance is required that the correct *Characteristic Value *is going to be written by transferring the *Characteristic Value *to be written in both directions before the write is performed. A higher-layer protocol can also use this sub-procedure to write multiple values in order in a single operation.

The sub-procedure has two phases; the first phase prepares the *Characteristic Values *to be written. To do this, the client transfers the *Characteristic Values *to the server. The server checks the validity of the *Characteristic Values *. The client also checks each *Characteristic Value *to verify it was correctly received by the server using the server responses. Once this is complete, the second phase performs the execution of all of the prepared Characteristic Value writes on the server from this client.

In the first phase, the ATT_PREPARE_WRITE_REQ PDU is used. The *Attribute Handle *shall be set to the *Characteristic Value Handle *that is to be prepared to write. The *Value Offset *and *Part Attribute Value *parameter shall be set to the new *Characteristic Value *

Two possible responses can be sent from the server for the ATT_PREPARE_­­WRITE_­­REQ PDU: ATT_PREPARE_­­WRITE_­­RSP and ATT_ERROR_­­RSP PDUs.

If the number of prepared write requests exceeds the number of prepared writes supported, then an ATT_ERROR_RSP PDU with the Error Code parameter set to *Prepare Queue Full *(0x09) shall be sent by the server.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_PREPARE_WRITE_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value *. The *Error Code *parameter is set as specified in the Attribute Protocol.

If a *Characteristic Value *is prepared two or more times during this sub-procedure, then all prepared values are written to the same *Characteristic Value *in the order that they were prepared.

If an ATT_PREPARE_WRITE_RSP PDU is returned, then the *Value Offset *and *Part Attribute Value *parameter in the response shall be checked with the *Value Offset *and *Part Attribute Value *parameter that was sent in the ATT_PREPARE_WRITE_REQ PDU; if they are different, then the value has been corrupted during transmission, and the sub-procedure shall be aborted by sending an ATT_EXECUTE_WRITE_REQ PDU with the Flags parameter set to 0x00 to cancel all prepared writes. The complete sub-procedure may be restarted.

Multiple ATT_PREPARE_WRITE_REQ PDUs can be sent by a client, each of which will be queued by the server.

In the second phase, the ATT_EXECUTE_WRITE_REQ PDU is used. The Attribute Flags parameter shall be set to 0x01 to immediately write all pending prepared values in the order that they were prepared. The server shall write the prepared writes once it receives this request and shall only send the ATT_EXECUTE_WRITE_RSP PDU once all the prepared values have been successfully written. If the *Characteristic Value *that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed, and an ATT_ERROR_RSP PDU with the Error Code parameter set to *Application Error *(0x80 – 0x9F) shall be sent by the server. The state of the Characteristic Values that were prepared is undefined.
Figure 4.17: Reliable Writes example

##### 4.10 Characteristic Value Notification

This procedure is used to notify a client of the value of a *Characteristic Value *from a server without expecting any Attribute Protocol layer acknowledgment that the notification was successfully received. There are two sub-procedures that can be used to notify a value: Single Notifications and Multiple Variable Length Notifications. Notifications can be configured using the Client Characteristic Configuration descriptor (See Section 3.3.3.3 ).

A profile defines when to use Notifications.

###### 4.10.1 Single Notifications

This sub-procedure is used when a server is configured to notify a *Characteristic Value *to a client.

The ATT_HANDLE_VALUE_NTF PDU is used to perform this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *being notified, and the *Attribute Value *parameter shall be set to the *Characteristic Value *
Figure 4.18: Notifications example

###### 4.10.2 Multiple Variable Length Notifications

This sub-procedure is used when a server is configured to notify multiple Characteristic Values to a client.

The Attribute Protocol ATT_MULTIPLE_HANDLE_VALUE_NTF PDU is used to perform this sub-procedure. The Handle Length Value Tuple List parameter shall include the set of Characteristic Value Handles and associated Attribute Values.
Figure 4.19: Multiple Variable Length Notifications example

##### 4.11 Characteristic Value Indications

This procedure is used to indicate the *Characteristic Value *from a server to a client. There is one sub-procedure that can be used to indicate a value: Indications. Indications can be configured using the Client Characteristic Configuration descriptor (See Section 3.3.3.3 ).

A profile defines when to use Indications.

###### 4.11.1 Indications

This sub-procedure is used when a server is configured to indicate a *Characteristic Value *to a client and expects an Attribute Protocol layer acknowledgment that the indication was successfully received.

The ATT_HANDLE_VALUE_IND PDU is used to perform this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Value Handle *being indicated, and the *Attribute Value *parameter shall be set to the *Characteristic Value *. Once the ATT_HANDLE_VALUE_IND PDU is received by the client, the client shall respond with an ATT_HANDLE_VALUE_CFM PDU.
Figure 4.20: Indications example

##### 4.12 Characteristic Descriptors

This procedure is used to read and write characteristic descriptors on a server. There are two sub-procedures that can be used to read and write characteristic descriptors: Read Characteristic Descriptors and Write Characteristic Descriptors.

###### 4.12.1 Read Characteristic Descriptors

This sub-procedure is used to read a characteristic descriptor from a server when the client knows the characteristic descriptor declaration’s Attribute handle.

The ATT_READ_REQ PDU is used for this sub-procedure. The ATT_READ_REQ PDU is used with the *Attribute Handle *parameter set to the characteristic descriptor handle. The ATT_READ_RSP PDU returns the characteristic descriptor value in the *Attribute Value *parameter.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the *Characteristic Value *. The *Error Code *parameter is set accordingly.
Figure 4.21: Read Characteristic Descriptors example

###### 4.12.2 Read Long Characteristic Descriptors

This sub-procedure is used to read a characteristic descriptor from a server when the client knows the characteristic descriptor declaration’s Attribute handle and the length of the characteristic descriptor declaration is longer than can be sent in a single ATT_READ_RSP PDU.

The ATT_READ_BLOB_REQ PDU is used to perform this sub-procedure. The Attribute Handle parameter shall be set to the characteristic descriptor handle. The Value Offset parameter shall be the offset within the characteristic descriptor to be read. To read the complete characteristic descriptor the offset should be set to 0x00 for the first ATT_READ_BLOB_REQ PDU. The offset for subsequent ATT_READ_BLOB_REQ PDUs is the next octet that has yet to be read. The ATT_READ_BLOB_REQ PDU is repeated until the ATT_READ_BLOB_RSP PDU’s Part Attribute Value parameter is zero or an ATT_ERROR_RSP PDU is sent by the server with the Error Code parameter set to *Invalid Offset *(0x07).

For each ATT_READ_BLOB_REQ PDU an ATT_READ_BLOB_RSP PDU is received with a portion of the characteristic descriptor value contained in the Part Attribute Value parameter.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_READ_­BLOB_­REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a read operation is not permitted on the characteristic descriptor. The Error Code parameter is set accordingly.
Figure 4.22: Read Long Characteristic Descriptors example

### Note on reading long descriptors after simple read

Note: The ATT_READ_BLOB_REQ PDU may be used to read the remainder of an characteristic descriptor value where the first part was read using a simple ATT_READ_REQ PDU.
Figure 4.23: Read Long Characteristic Descriptors (following simple read) example

###### 4.12.3 Write Characteristic Descriptors

This sub-procedure is used to write a characteristic descriptor value to a server when the client knows the characteristic descriptor handle.

The ATT_WRITE_REQ PDU is used for this sub-procedure. The *Attribute Handle *parameter shall be set to the characteristic descriptor handle. The *Attribute Value *parameter shall be set to the new characteristic descriptor value.

An ATT_WRITE_RSP PDU shall be sent by the server if the write of the characteristic descriptor value succeeded.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_WRITE_REQ PDU if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value *. The Error Code parameter shall be set as specified in the Attribute Protocol. If the characteristic descriptor value that is written is the wrong size, or has an invalid value as defined by the profile, or the operation is not permitted at this time then the value shall not be written and an ATT_ERROR_RSP PDU shall be sent with the Error Code parameter set to *Application Error *(0x80 – 0x9F) by the server.
Figure 4.24: Write Characteristic Descriptors example

###### 4.12.4 Write Long Characteristic Descriptors

This sub-procedure is used to write a characteristic descriptor value to a server when the client knows the characteristic descriptor handle but the length of the characteristic descriptor value is longer than can be sent in a single ATT_WRITE_REQ PDU.

The ATT_PREPARE_WRITE_REQ and ATT_EXECUTE_WRITE_REQ PDUs are used to perform this sub-procedure. The *Attribute Handle *parameter shall be set to the *Characteristic Descriptor Handle *of the *Characteristic Value *to be written. The *Part Attribute Value *parameter shall be set to the part of the *Attribute Value *that is being written. The *Value Offset *parameter shall be the offset within the *Characteristic Value *to be written. To write the complete *Characteristic Value *the offset should be set to 0x0000 for the first ATT_PREPARE_WRITE_REQ PDU. The offset for subsequent ATT_PREPARE_WRITE_REQ PDUs is the next octet that has yet to be written. The ATT_PREPARE_WRITE_REQ PDU is repeated until the complete *Characteristic Value *has been transferred, after which an ATT_EXECUTE_WRITE_REQ PDU is used to write the complete value.

### Note on write long descriptor verification

Note: The values in the ATT_PREPARE_WRITE_RSP PDU do not need to be verified in this sub-procedure.

An ATT_ERROR_RSP PDU shall be sent by the server in response to the ATT_PREPARE_WRITE_REQ or ATT_EXECUTE_WRITE_REQ PDUs if insufficient authentication, insufficient authorization, a too-short encryption key size is used by the client, or if a write operation is not permitted on the *Characteristic Value *. The Error Code parameter is set as specified in the Attribute Protocol. If the *Attribute Value *that is written is the wrong size, or has an invalid value as defined by the profile, then the write shall not succeed and an ATT_ERROR_RSP PDU shall be sent with the Error Code parameter set to *Application Error *(0x80 – 0x9F) by the server.
Figure 4.25: Write Long Characteristic Descriptors example

##### 4.13 GATT procedure mapping to ATT protocol opcodes

Table 4.2 describes the mapping of the ATT protocol opcodes to the GATT procedures and sub-procedures. Only those portions of the ATT protocol requests, responses, notifications or indications necessary to implement the mandatory or supported optional sub-procedures is required.

Feature

Sub-Procedure

ATT Protocol Opcodes

**Server Configuration **

Exchange MTU

ATT_EXCHANGE_MTU_REQ

ATT_EXCHANGE_MTU_RSP

ATT_ERROR_RSP PDU

**Primary Service Discovery **

Discover All Primary Services

ATT_READ_BY_GROUP_TYPE_REQ

ATT_READ_BY_GROUP_TYPE_RSP

ATT_ERROR_RSP PDU

Discover Primary Services By Service UUID

ATT_FIND_BY_TYPE_VALUE_REQ

ATT_FIND_BY_TYPE_VALUE_RSP

ATT_ERROR_RSP PDU

**Relationship Discovery **

Find Included Services

ATT_READ_BY_TYPE_REQ

ATT_READ_BY_TYPE_RSP

ATT_ERROR_RSP PDU

**Characteristic Discovery **

Discover All Characteristic of a Service

ATT_READ_BY_TYPE_REQ

ATT_READ_BY_TYPE_RSP

ATT_ERROR_RSP PDU

Discover Characteristic by UUID

ATT_READ_BY_TYPE_REQ

ATT_READ_BY_TYPE_RSP

ATT_ERROR_RSP PDU

**Characteristic Descriptor Discovery **

Discover All Characteristic Descriptors

ATT_FIND_INFORMATION_REQ

ATT_FIND_INFORMATION_RSP

ATT_ERROR_RSP PDU

**Characteristic Value Read **

Read Characteristic Value

ATT_READ_REQ

ATT_READ_RSP

ATT_ERROR_RSP PDU

Read Using Characteristic UUID

ATT_READ_BY_TYPE_REQ

ATT_READ_BY_TYPE_RSP

ATT_ERROR_RSP PDU

Read Long Characteristic Values

ATT_READ_BLOB_REQ

ATT_READ_BLOB_RSP

ATT_ERROR_RSP PDU

Read Multiple Characteristic Values

ATT_READ_MULTIPLE_REQ

ATT_READ_MULTIPLE_RSP

ATT_ERROR_RSP PDU

**Characteristic Value Write **

Write Without Response

ATT_WRITE_CMD

Signed Write Without Response

ATT_WRITE_CMD

Write Characteristic Value

ATT_WRITE_REQ

ATT_WRITE_RSP

ATT_ERROR_RSP PDU

Write Long Characteristic Values

ATT_PREPARE_WRITE_REQ

ATT_PREPARE_WRITE_RSP

ATT_EXECUTE_WRITE_REQ

ATT_EXECUTE_WRITE_RSP

ATT_ERROR_RSP PDU

Characteristic Value Reliable Writes

ATT_PREPARE_WRITE_REQ

ATT_PREPARE_WRITE_RSP

ATT_EXECUTE_WRITE_REQ

ATT_EXECUTE_WRITE_RSP

ATT_ERROR_RSP PDU

**Characteristic Value Notification **

Single Notifications

ATT_HANDLE_VALUE_NTF

Multiple Variable Length Notifications

ATT_MULTIPLE_HANDLE_VALUE_NTF

**Characteristic Value Indication **

Indications

ATT_HANDLE_VALUE_IND

ATT_HANDLE_VALUE_CFM

**Characteristic Descriptor Value Read **

Read Characteristic Descriptors

ATT_READ_REQ

ATT_READ_RSP

ATT_ERROR_RSP PDU

Read Long Characteristic Descriptors

ATT_READ_BLOB_REQ

ATT_READ_BLOB_RSP

ATT_ERROR_RSP PDU

**Characteristic Descriptor Value Write **

Write Characteristic Descriptors

ATT_WRITE_REQ

ATT_WRITE_RSP

ATT_ERROR_RSP PDU

Write Long Characteristic Descriptors

ATT_PREPARE_WRITE_REQ

ATT_PREPARE_WRITE_RSP

ATT_PREPARE_WRITE_REQ

ATT_PREPARE_WRITE_RSP

ATT_ERROR_RSP PDU
Table 4.2: GATT procedure mapping to ATT protocol opcodes

##### 4.14 Procedure timeouts

GATT procedures are protected from failure with an Attribute Protocol transaction timeout.

If the Attribute Protocol transaction times out, the procedure shall be considered to have failed, and the local higher layer shall be notified. No further GATT procedures shall be performed on that ATT bearer. A new GATT procedure shall only be performed on another ATT bearer.
