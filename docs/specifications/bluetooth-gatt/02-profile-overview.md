# Profile overview

The GATT profile is designed to be used by an application or another profile, so that a client can communicate with a server. The server contains a number of attributes, and the GATT Profile defines how to use the Attribute Protocol to discover, read, write and obtain indications of these attributes, as well as configuring broadcast of attributes.

##### 2.1 Protocol stack

Figure 2.1 shows the peer protocols used by this profile.
Figure 2.1: Protocol model

##### 2.2 Configurations and roles

The following roles are defined for devices that implement this profile:

Client—This is the device that initiates commands and requests towards the server and can receive responses, indications and notifications sent by the server.

Server—This is the device that accepts incoming commands and requests from the client and sends responses, indications and notifications to a client.

> **Note:** The roles are not fixed to the device. The roles are determined when a device initiates a defined procedure, and they are released when the procedure ends.

A device can act in both roles at the same time.

An example of configurations illustrating the roles for this profile is depicted in Figure 2.2
Figure 2.2: Examples of configuration

In Figure 2.2 , the computer is the temperature service client and the sensor is the temperature service server. The computer initiates procedures to configure the sensor or to read the sensor values. In this example the sensor provides information about the characteristics the sensor device exposes as part of the temperature service and may permit some characteristics to be written. Also, the sensor responds to read requests with the appropriate values.

##### 2.3 User requirements and scenarios

The following scenarios are covered by this profile:

- Exchanging configuration

- Discovery of services and characteristics on a device

- Reading a characteristic value

- Writing a characteristic value

- Notification of a characteristic value

- Indication of a characteristic value

##### 2.4 Profile fundamentals

This profile can be used over any physical link, using the Attribute Protocol L2CAP channel, known as the ATT Bearer. Here is a brief summary of lower layer requirements communication between the client and the server.

- An ATT bearer is established using “Channel Establishment” as defined in Section 6

- The profile roles are not tied to the Controller roles (i.e. Central or Peripheral).

- On an LE Physical link, use of security features such as authorization, authentication and encryption are optional. On a BR/EDR physical link encryption is mandatory.

- Multi-octet fields within the GATT profile shall be sent least significant octet first (little-endian) with the exception of the Characteristic Value field. The Characteristic Value and any fields within it shall be little-endian unless otherwise defined in the specification which defines the characteristic.

- Multiple ATT bearers may be established between a client and a server. The server can determine if ATT bearers are from the same client, and vice versa, by using connection information such as the Bluetooth Device Address of the peer device.

##### 2.5 Attribute Protocol

The GATT profile requires the implementation of the Attribute Protocol (See [Vol 3] Part F ) and those Attribute Protocol PDUs required by Section 4.2 and Section 4.13

###### 2.5.1 Overview

The GATT Profile uses the Attribute Protocol to transport data in the form of commands, requests, responses, indications, notifications and confirmations between devices. This data is contained in Attribute Protocol PDUs as specified in Figure 2.3
Figure 2.3: Attribute Protocol PDU

The *Opcode*contains the specific command, request, response, indication, notification or confirmation opcode and a flag for authentication. The *Attribute Parameters*contain data for the specific command or request or the data returned in a response, indication, or notification. The *Authentication Signature*is optional and is described in [Vol 3]
 Part H,
 Section 2.4.5

Attribute Protocol commands and requests act on values stored in Attributes on the server device. An Attribute is composed of four parts: *Attribute Handle **Attribute Type**Attribute Value*, and *Attribute Permissions*Figure 2.4 shows a logical representation of an Attribute. The actual representation for a given implementation is specific to that implementation.
Figure 2.4: Logical attribute representation

The *Attribute Handle*is an index corresponding to a specific Attribute. The *Attribute Type*is a UUID that describes the *Attribute Value*. The *Attribute Value*is the data described by the *Attribute Type*and indexed by the *Attribute Handle*. The Attributes are ordered by increasing *Attribute Handle*values. *Attribute Handle*values may begin at any value between 0x0001 and 0xFFFF. Although the *Attribute Handle*values are in increasing order, following *Attribute Handle*values may differ by more than one. That is to say there may be gaps between successive *Attribute Handles*. When the specification requires two attribute handles to be adjacent or for one to immediately follow one the other, such gaps are still permitted and shall be ignored.

*Attribute Permissions*is part of the Attribute that cannot be read from or written to using the Attribute Protocol. It is used by the server to determine whether read or write access is permitted for a given attribute. *Attribute Permissions*are established by the GATT profile, a higher layer profile or are implementation specific if not specified.

###### 2.5.2 Attribute caching

Attribute caching is an optimization that allows the client to discover the Attribute information such as *Attribute Handles*used by the server once and use the same Attribute information across reconnections without rediscovery. If the client does not cache the Attribute information, then it must rediscover the *Attribute*information at each reconnection. With caching, time is saved and a significant number of packets need not be exchanged between the client and server. The Attribute information that shall be cached by a client is the *Attribute Handles*of all server attributes and the GATT service characteristics values.

*Attribute Handles*used by the server should not change over time. This means that once an *Attribute Handle*is discovered by a client the *Attribute Handle*for that Attribute should not be changed.

Some circumstances may cause servers to change the *Attribute Handles*used for services, perhaps due to a factory reset or a firmware upgrade procedure being performed. The following is only required on the server if the services on the server can be added, modified or removed. If GATT based services on the server cannot be changed during the usable lifetime of the device, the *Service Changed*characteristic shall not exist on the server and the client does not need to ever perform service discovery after the initial service discovery for that server.

To support caching when a server supports changes in GATT based services, an indication is sent by the server to clients when a service is added, removed, or modified on the server. A client may also detect a service change by reading the *Database Hash*characteristic if that characteristic exists on the server. A GATT based service is considered modified if the binding of the *Attribute Handles*to the associated Attributes grouped within a service definition are changed. Any change to the GATT service definition characteristic values other than the *Service Changed*characteristic value and the *Client Supported Features*characteristic value themselves shall also be considered a modification.

For clients that have a trusted relationship (i.e. bond) with the server, the attribute cache is valid across connections. For clients with a trusted relationship and not in a connection when a service change occurs, the server shall send an indication when the client reconnects to the server (see Section 7.1 ). For clients that do not have a trusted relationship with the server and that do not support reading the *Database Hash*characteristic, the attribute cache is valid only during the connection. Clients without a trusted relationship that do support reading the *Database Hash*characteristic may validate the attribute cache on connection setup. Clients without a trusted relationship shall receive an indication when the service change occurs only during the current connection.

> **Note:** Clients without a trusted relationship that support caching must either perform service discovery or detect service changes by reading the *Database Hash*characteristic on each connection if the server supports the *Service Changed*characteristic.

The server shall send an ATT_HANDLE_VALUE_IND PDU containing the range of affected *Attribute Handles*that shall be considered invalid in the client’s attribute cache. The start *Attribute Handle*shall be the start *Attribute Handle*of the service definition containing the change and the end *Attribute Handle*shall be the last *Attribute Handle*of the service definition containing the change. The value in the indication is composed of two 16-bit *Attribute Handles*concatenated to indicate the affected *Attribute Handle*range.

> **Note:** A server may set the affected *Attribute Handle*range to 0x0001 to 0xFFFF to indicate to the client to rediscover the entire set of *Attribute Handles*on the server.

If the *Database Hash*characteristic exists on the server then, each time a service change occurs, the server shall update the *Database Hash*characteristic value with the new Database Hash (see Section 7.3 ).

If the *Database Hash*characteristic value has changed since the last time it was read, the client shall consider its attribute cache invalid and shall not make use of the cached information until it has performed service discovery or obtained the changed database definitions using an out-of-band mechanism.

The client, upon receiving an ATT_HANDLE_VALUE_IND PDU containing the range of affected Attribute Handles, shall consider the attribute cache invalid over the affected Attribute Handle range. Any outstanding request transaction shall be considered invalid if the Attribute Handle is contained within the affected Attribute Handle range. The client must perform service discovery before the client uses any service that has an attribute within the affected Attribute Handle range. Alternatively, the client may read the *Database Hash*characteristic and obtain the changed database definitions using an out-of-band mechanism. If the client receives an ATT_HANDLE_VALUE_IND PDU during service discovery and the client has read the *Database Hash*characteristic prior to the service discovery, the client may read the *Database Hash*characteristic again to determine if the current service discovery can be continued or if a new service discovery is required.

Once the server has received the ATT_HANDLE_VALUE_CFM PDU, the server can consider the client to be aware of the updated Attribute Handles.

The client shall consider the affected *Attribute Handle*range to be invalid in its attribute cache and perform the discovery procedures to restore the attribute cache. The server shall store service changed information for all bonded devices.

###### 2.5.2.1 Robust Caching

Robust Caching is a feature where the server sends an ATT_ERROR_RSP PDU to the client if the server does not consider the client to be aware of a service change.

If the *Database Hash*and *Service Changed*characteristics are both present on the server, then the server shall support the Robust Caching feature.

From the perspective of a server, each connected client is either "change-aware" or "change-unaware" regarding changes in the database definitions. After connecting to a server, the initial state of a client without a trusted relationship is change-aware. The initial state of a client with a trusted relationship is unchanged from the previous connection unless the database has been updated since the last connection, in which case the initial state is change-unaware.

Whenever the server updates the database definitions, all connected clients become change-unaware. A change-unaware connected client becomes change-aware when it reads the *Database Hash*characteristic and then the server receives another ATT request from the client. A change-unaware client using multiple ATT bearers shall wait until the server has responded to all pending requests before reading the *Database Hash*characteristic (see Figure 2.5 ).
Figure 2.5: Transition to change-aware state for a client using multiple ATT bearers

In addition, a change-unaware connected client using exactly one ATT bearer becomes change-aware when either of the following happen:

- The client receives and confirms a *Handle Value Indication*for the *Service Changed*characteristic (see Figure 2.6 ).

- The server sends the client a response with the Error Code parameter set to *Database Out Of Sync*(0x12) and then the server receives another ATT request from the client (see Figure 2.7 ).

Figure 2.6: Transition to change-aware state for a client using exactly one ATT bearer, triggered by a Service Changed confirmation
Figure 2.7: Transition to change-aware state for a client using exactly one ATT bearer, triggered by the ATT response "Database Out Of Sync" or "Hash Read"

If a client that has indicated support for robust caching (by setting the *Robust Caching*bit in the *Client Supported Features*characteristic) is change-unaware then the server shall send an ATT_ERROR_RSP PDU with the Error Code parameter set to *Database Out Of Sync*(0x12) when either of the following happen:

- That client requests an operation at any *Attribute Handle*or list of *Attribute Handles*by sending an ATT request.

- That client sends an ATT_READ_BY_TYPE_REQ PDU with Attribute Type other than «Include» or «Characteristic» and an *Attribute Handle*range other than 0x0001 to 0xFFFF.

The ATT_ERROR_RSP PDU is sent only once per bearer after the client becomes change-unaware, unless the client disconnects or the database changes again before the client becomes change-aware in which case the ATT_ERROR_RSP PDU shall be sent again. If a change-unaware client sends an ATT command, the server shall ignore it. Except for a *Handle Value Indication*for the *Service Changed*characteristic, the server shall not send notifications and indications to such a client until it becomes change-aware. If a client is change-aware, then the server shall perform the operation normally.

> **Note:** To reduce the probability of blocked notifications and indications, servers should send this indication as soon as possible after a service change.

If a client receives an ATT_ERROR_RSP PDU with the Error Code parameter set to *Database Out Of Sync*(0x12), it shall consider its attribute cache invalid and shall not make use of the cached information until it has performed service discovery or obtained the changed database definitions using an out-of-band mechanism.

###### 2.5.3 Attribute grouping

The Generic Attribute Profile defines the grouping of attributes for three attribute types: «Primary Service», «Secondary Service» and «Characteristic». A group begins with a declaration, and ends as defined in Section 3.1 for services and Section 3.3 for characteristics. Not all of the grouping attributes can be used in the ATT_READ_­BY_­GROUP_­TYPE_­REQ PDU. The «Primary Service» and «Secondary Service» grouping types may be used in the ATT_READ_­BY_­GROUP_­TYPE_­REQ PDU. The «Characteristic» grouping type shall not be used in the ATT_READ_­BY_­GROUP_­TYPE_­REQ PDU.

###### 2.5.4 UUIDs

All 16-bit UUIDs shall be contained in exactly 2 octets. All 128-bit UUIDs shall be contained in exactly 16 octets.

All 32-bit UUIDs shall be converted to 128-bit UUIDs when the UUID is contained in an ATT PDU. See [Vol 3]
 Part B,
 Section 2.5.1 for the method of conversion.

##### 2.6 GATT Profile hierarchy

###### 2.6.1 Overview

The GATT Profile specifies the structure in which profile data is exchanged. This structure defines basic elements such as services and characteristics, used in a profile. All of the elements are contained by Attributes. Attributes used in the Attribute Protocol are containers that carry this profile data.

The top level of the hierarchy is a profile. A profile is composed of one or more services necessary to fulfill a use case. A service is composed of characteristics or inclusions of other services. Each characteristic contains a value and may contain optional information about the value. The service and characteristic and the components of the characteristic (i.e. value and descriptors) contain the profile data and are all stored in Attributes on the server.
Figure 2.8: GATT Profile hierarchy

###### 2.6.2 Service

A service is a collection of data and associated behaviors to accomplish a particular function or feature. In GATT, a service is defined by its service definition. A service definition may contain included services, mandatory characteristics, and optional characteristics.

To maintain backward compatibility with earlier clients, later versions of a service definition can only add new included services or optional characteristics. Later versions of a service definition are forbidden from changing behaviors from previous versions of the service definition.

There are two types of services: primary service and secondary service. A primary service is a service that exposes functionality of this device. A primary service can be included by another service. Primary services can be discovered using Primary Service Discovery procedures. A secondary service is a service that should only be included from a primary service or another secondary service or other higher layer specification. A secondary service is only relevant in the context of the entity that includes it.

The determination of whether a service is either a primary or secondary service can be mandated by a higher layer specification.

> **Note:** There is no procedure for discovering secondary services.

Services may be used in one or more higher layer specifications to fulfill a particular use case.

The service definition is described in Section 3.1

###### 2.6.3 Included services

An included service is a method to reference another service definition existing on the server into the service being defined. To include another service, an include definition is used at the beginning of the service definition. When a service definition uses an include definition to include a service, the entire included service definition becomes part of the new service definition. This includes all the included services and characteristics of the included service. The included service still exists as an independent service. A service that is included by another service shall not be changed by the act of inclusion or by the including service. There are no limits to the number of include definitions or the depth of nested includes in a service definition.

The include definition is described in Section 3.2

###### 2.6.4 Characteristic

A characteristic is a value used in a service along with properties and configuration information about how the value is accessed and information about how the value is displayed or represented. In GATT, a characteristic is defined by its characteristic definition. A characteristic definition contains a characteristic declaration, characteristic properties, and a value and may contain descriptors that describe the value or permit configuration of the server with respect to the characteristic.

The characteristic definition is described in Section 3.3

##### 2.7 Configured Broadcast

For LE physical links, Configured Broadcast is a method for a client to indicate to a server which *Characteristic Value*shall be broadcast in the advertising data when the server is executing the Broadcast mode procedure. For BR/EDR physical links, Configured Broadcast is not supported.

To configure a *Characteristic Value*to be broadcast by the server when in Broadcast mode, the client sets the broadcast configuration bit described in Section 3.3.3.4 . The frequency of the broadcast is part of the service behavior definition. The data shall be broadcast as part of the Service Data Advertising Data type as defined in Section 1.11 of [ ]. If multiple characteristics can simultaneously be enabled for broadcast, the service specification defines how the characteristics are to be formatted in the service data which follows the service UUID in the Service Data Advertising Data type payload.
