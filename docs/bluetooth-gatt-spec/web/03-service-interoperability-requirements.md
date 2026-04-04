# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 3. Service interoperability requirements

### 3.1. Service definition

A service definition shall contain a service declaration and may contain include definitions and characteristic definitions. The service definition ends before the next service declaration or after the maximum *Attribute Handle* is reached. Service definitions appear on the server in an order based on *Attribute Handle*.

All include definitions and characteristic definitions contained within the service definition are considered to be part of the service. All include definitions shall immediately follow the service declaration and precede any characteristic definitions. A service definition may have zero or more include definitions. All characteristic definitions shall be immediately following the last include definition or, in the event of no include definitions, immediately following the service declaration. A service definition may have zero or more characteristic definitions. There is no upper limit for include or characteristic definitions.

A service declaration is an Attribute with the *Attribute Type* set to the UUID for «Primary Service» or «Secondary Service». The *Attribute Value* shall be the 16-bit Bluetooth UUID or 128-bit UUID for the service, known as the service UUID. A client shall support the use of both 16-bit and 128-bit UUIDs. A client may ignore any service definition with an unknown service UUID. An unknown service UUID is a UUID for an unsupported service. The *Attribute Permissions* shall be read-only and shall not require authentication or authorization.

When multiple services exist, services definitions with service declarations using 16-bit Bluetooth UUID should be grouped together (i.e. listed sequentially) and services definitions with service declarations using 128-bit UUID should be grouped together.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permission |
| --- | --- | --- | --- |
| 0xNNNN | 0x2800 – UUID for «Primary Service» OR 0x2801 for «Secondary Service» | 16-bit Bluetooth UUID or 128-bit UUID for Service | Read Only,  No Authentication,  No Authorization |

Table 3.1: Service declaration

A device or higher level specification may have multiple service definitions and may have multiple service definitions with the same service UUID.

All Attributes on a server shall either contain a service declaration or exist within a service definition.

Service definitions contained in a server may appear in any order; a client shall not assume the order of service definitions on a server.

### 3.2. Include definition

An include definition shall contain only one include declaration.

The include declaration is an Attribute with the *Attribute Type* set to the UUID for «Include». The *Attribute Value* shall be set to the included service *Attribute Handle*, the End Group Handle, and the *service UUID*. The Service UUID shall only be present when the UUID is a 16-bit Bluetooth UUID.The *Attribute Permissions* shall be read only and not require authentication or authorization.

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2802 – UUID for «Include» | Included Service Attribute Handle | End Group Handle | Service UUID | Read Only,  No Authentication,  No Authorization |

Table 3.2: Include declaration

A server shall not contain a service definition with an include definition to another service that includes the original service. This applies to each of the services the included definition references. This is referred to as a circular reference.

If the client detects a circular reference or detects nested include declarations to a greater level than it expects, it should terminate or stop using the ATT bearer.

### 3.3. Characteristic definition

A characteristic definition shall contain a characteristic declaration, a Characteristic Value declaration and may contain characteristic descriptor declarations. A characteristic definition ends at the start of the next characteristic declaration or service declaration or after the maximum *Attribute Handle*. Characteristic definitions appear on the server within a service definition in an order based on *Attribute Handle*.

Each declaration above is contained in a separate Attribute. The two required declarations are the characteristic declaration and the Characteristic Value declaration. The Characteristic Value declaration shall exist immediately following the characteristic declaration. Any optional characteristic descriptor declarations are placed after the Characteristic Value declaration. The order of the optional characteristic descriptor declarations is not significant.

A characteristic definition may be defined to concatenate several Characteristic Values into a single aggregated Characteristic Value. This may be used to optimize read and writes of multiple Characteristic Values through the reading and writing of a single aggregated Characteristic Value. This type of characteristic definition is the same as a normal characteristic definition. The characteristic declaration shall use a characteristic UUID that is unique to the aggregated characteristic definition. The aggregated characteristic definition may also contain a characteristic aggregate format descriptor that describes the display format of the aggregated Characteristic Value.

#### 3.3.1. Characteristic declaration

A characteristic declaration is an Attribute with the Attribute Type set to the UUID for «Characteristic» and *Attribute Value* set to the Characteristic Properties, Characteristic Value *Attribute Handle* and Characteristic UUID. The Attribute Permissions shall be readable and not require authentication or authorization.

If the server changes any characteristic declaration *Attribute Value* while the server has a trusted relationship with any client, then it shall send each client a Service Changed Indication indicating a change in the service holding the Characteristic Declaration (see  [Section 7.1](generic-attribute-profile--gatt-.html#UUID-6ee92321-3db4-dad2-554e-946a80ff7435 "7.1 Service Changed")).

| Attribute Handle | Attribute Types | Attribute Value | | | Attribute Permissions |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2803–UUID for «Characteristic» | Characteristic Properties | Characteristic Value Attribute Handle | Characteristic UUID | Read Only,  No Authentication,  No Authorization |

Table 3.3: Characteristic declaration

The *Attribute Value* of a characteristic declaration is read only.

| Attribute Value | Size | Description |
| --- | --- | --- |
| **Characteristic Properties** | 1 octets | Bit field of characteristic properties |
| **Characteristic Value Handle** | 2 octets | Handle of the Attribute containing the value of this characteristic |
| **Characteristic UUID** | 2 or 16 octets | 16-bit Bluetooth UUID or 128-bit UUID for Characteristic Value |

Table 3.4: Attribute Value field in characteristic declaration

A service may have multiple characteristic definitions with the same Characteristic UUID.

Within a service definition, some characteristics may be mandatory and those characteristics shall be located after the include declarations and before any optional characteristics within the service definition. A client shall not assume any order of those characteristics that are mandatory or any order of those characteristics that are optional within a service definition. Whenever possible and within the requirements stated earlier, characteristics definitions with characteristic declarations using 16-bit Bluetooth UUIDs should be grouped together (i.e. listed sequentially) and characteristics definitions with characteristic declarations using 128-bit UUIDs should be grouped together.

#### 3.3.1.1. Characteristic Properties

The Characteristic Properties bit field determines how the Characteristic Value can be used, or how the characteristic descriptors (see  [Section 3.3.3](generic-attribute-profile--gatt-.html#UUID-09487be3-178b-eeca-f49f-f783e8d462f6 "3.3.3 Characteristic descriptor declarations")) can be accessed. If the bits defined in  [Table 3.5](generic-attribute-profile--gatt-.html#UUID-80c13237-6499-b5da-e575-7147fd3c7413_table-idm13358911666278 "Table 3.5: Characteristic Properties bit field") are set, the action described is permitted. Multiple characteristic properties can be set.

These bits shall be set according to the procedures allowed for this characteristic, as defined by higher layer specifications, without regard to security requirements.

| Properties | Value | Description |
| --- | --- | --- |
| Broadcast | 0x01 | If set, permits broadcasts of the Characteristic Value using Server Characteristic Configuration Descriptor. If set, the Server Characteristic Configuration Descriptor shall exist. |
| Read | 0x02 | If set, permits reads of the Characteristic Value using procedures defined in  [Section 4.8](generic-attribute-profile--gatt-.html#UUID-66cf484d-50cd-199f-dd0d-d0d02ad02ce0 "4.8 Characteristic Value Read") |
| Write Without Response | 0x04 | If set, permit writes of the Characteristic Value without response using procedures defined in  [Section 4.9.1](generic-attribute-profile--gatt-.html#UUID-9f1c2e38-8fbe-f60c-d885-076707c88a43 "4.9.1 Write Without Response"). |
| Write | 0x08 | If set, permits writes of the Characteristic Value with response using procedures defined in  [Section 4.9.3](generic-attribute-profile--gatt-.html#UUID-ba4b856a-6994-01e4-97f6-357f9be40990 "4.9.3 Write Characteristic Value") or  [Section 4.9.4](generic-attribute-profile--gatt-.html#UUID-6ab738ad-6d26-1da1-7417-e83da50e90c5 "4.9.4 Write Long Characteristic Values"). |
| Notify | 0x10 | If set, permits notifications of a Characteristic Value without acknowledgment using the procedure defined in  [Section 4.10](generic-attribute-profile--gatt-.html#UUID-74673cc2-e704-a2fa-14bb-d175c27193ab "4.10 Characteristic Value Notification"). If set, the Client Characteristic Configuration Descriptor shall exist. |
| Indicate | 0x20 | If set, permits indications of a Characteristic Value with acknowledgment using the procedure defined in  [Section 4.11](generic-attribute-profile--gatt-.html#UUID-615ed0ff-f42b-827d-6427-6474fc21737c "4.11 Characteristic Value Indications"). If set, the Client Characteristic Configuration Descriptor shall exist. |
| Authenticated Signed Writes | 0x40 | If set, permits signed writes to the Characteristic Value using the procedure defined in  [Section 4.9.2](generic-attribute-profile--gatt-.html#UUID-516bd731-2079-87f9-8002-c3ca92fbed4b "4.9.2 Signed Write Without Response"). |
| Extended Properties | 0x80 | If set, additional characteristic properties are defined in the Characteristic Extended Properties Descriptor defined in  [Section 3.3.3.1](generic-attribute-profile--gatt-.html#UUID-9154505c-6e2d-a35a-3f30-1da0383a2425 "3.3.3.1 Characteristic Extended Properties"). If set, the Characteristic Extended Properties Descriptor shall exist. |

Table 3.5: Characteristic Properties bit field

#### 3.3.1.2. Characteristic Value Attribute Handle

The Characteristic Value *Attribute Handle* field is the *Attribute Handle* of the Attribute that contains the *Characteristic Value*.

#### 3.3.1.3. Characteristic UUID

The *Characteristic UUID* field is a 16-bit Bluetooth UUID or 128-bit UUID that describes the type of *Characteristic Value*. A client shall support the use of both 16-bit and 128-bit *Characteristic UUIDs*. A client may ignore any characteristic definition with an unknown *Characteristic UUID*. An unknown characteristic UUID is a UUID for an unsupported characteristic.

#### 3.3.2. Characteristic Value declaration

The *Characteristic Value* declaration contains the value of the characteristic. It is the first Attribute after the characteristic declaration. All characteristic definitions shall have a *Characteristic Value* declaration.

A Characteristic Value declaration is an Attribute with the Attribute Type set to the 16-bit Bluetooth or 128-bit UUID for the Characteristic Value used in the characteristic declaration. The *Attribute Value* is set to the *Characteristic Value*. The *Attribute Permissions* are specified by the service or may be implementation specific if not specified otherwise.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0xUUUU – 16-bit Bluetooth UUID or 128-bit UUID for Characteristic UUID | Characteristic Value | Higher layer profile or implementation specific |

Table 3.6: Characteristic Value declaration

#### 3.3.3. Characteristic descriptor declarations

Characteristic descriptors are used to contain related information about the *Characteristic Value*. The GATT profile defines a standard set of characteristic descriptors that can be used by higher layer profiles. Higher layer profiles may define additional characteristic descriptors that are profile specific. Each characteristic descriptor is identified by the characteristic descriptor UUID. A client shall support the use of both 16-bit and 128-bit characteristic descriptor UUIDs. A client may ignore any characteristic descriptor declaration with an unknown characteristic descriptor UUID. An unknown characteristic descriptor UUID is a UUID for an unsupported characteristic descriptor.

Characteristic descriptors if present within a characteristic definition shall follow the *Characteristic Value* declaration. The characteristic descriptor declaration may appear in any order within the characteristic definition. The client shall not assume the order in which a characteristic descriptor declaration appears in a characteristic definition following the *Characteristic Value* declaration.

Characteristic descriptor declaration permissions are defined by a higher layer profile or are implementation specific. A client shall not assume all characteristic descriptor declarations are readable.

#### 3.3.3.1. Characteristic Extended Properties

The *Characteristic Extended Properties* declaration is a descriptor that defines additional *Characteristic Properties*. If the *Extended Properties* bit of the *Characteristic Properties* is set then this characteristic descriptor shall exist. The characteristic descriptor may occur in any position within the characteristic definition after the Characteristic Value. Only one *Characteristic Extended Properties* declaration shall exist in a characteristic definition.

The characteristic descriptor is contained in an Attribute and the *Attribute Type* shall be set to the UUID for «Characteristic Extended Properties» and the *Attribute Value* shall be two octets in length and shall contain the *Characteristic Extended Properties Bit Field*. The *Attribute Permissions* shall be readable without authentication and authorization being required.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0x2900 – UUID for «Characteristic Extended Properties» | Characteristic Extended Properties Bit Field | Read Only,  No Authentication,  No Authorization |

Table 3.7: Characteristic Extended Properties declaration

The *Characteristic Extended Properties* bit field describes additional properties on how the Characteristic Value can be used, or how the characteristic descriptors (see  [Section 3.3.3.3](generic-attribute-profile--gatt-.html#UUID-58fcda17-4f4b-3f53-3ca8-077bbfc77c5d "3.3.3.3 Client Characteristic Configuration")) can be accessed. If the bits defined in  [Table 3.8](generic-attribute-profile--gatt-.html#UUID-9154505c-6e2d-a35a-3f30-1da0383a2425_table-idm13358912021912 "Table 3.8: Characteristic Extended Properties bit field") are set, the action described is permitted. Multiple additional properties can be set.

| Bit Number | Property | Description |
| --- | --- | --- |
| 0 | Reliable Write | If set, permits reliable writes of the Characteristic Value using the procedure defined in  [Section 4.9.5](generic-attribute-profile--gatt-.html#UUID-7fc3dafa-7199-3f9c-a137-1575597b2a8c "4.9.5 Reliable Writes") |
| 1 | Writable Auxiliaries | If set, permits writes to the characteristic descriptor defined in  [Section 3.3.3.2](generic-attribute-profile--gatt-.html#UUID-4677edc4-2ca2-41b8-8033-9695180060a3 "3.3.3.2 Characteristic User Description") |
| All other bits |  | Reserved for future use |

Table 3.8: Characteristic Extended Properties bit field

#### 3.3.3.2. Characteristic User Description

The *Characteristic User Description* declaration is an optional characteristic descriptor that defines a UTF-8 string of variable size that is a user textual description of the *Characteristic Value*. If the *Writable Auxiliaries* bit of the *Characteristic Extended Properties* is set then this characteristic descriptor can be written. The characteristic descriptor may occur in any position within the characteristic definition after the *Characteristic Value*. Only one *Characteristic User Description* declaration shall exist in a characteristic definition.

The characteristic descriptor is contained in an Attribute and the *Attribute Type* shall be set to the UUID for «Characteristic User Description» and the *Attribute Value* shall be set to the characteristic user description UTF-8 string. The *Attribute Permissions* are specified by the profile or may be implementation specific if not specified otherwise.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0x2901 – UUID for «Characteristic User Description» | Characteristic User Description UTF-8 String | Higher layer profile or implementation specific |

Table 3.9: Characteristic User Description declaration

#### 3.3.3.3. Client Characteristic Configuration

The *Client Characteristic Configuration* declaration is an optional characteristic descriptor that defines how the characteristic may be configured by a specific client. The Client Characteristic Configuration descriptor value shall be persistent across connections for bonded devices. The Client Characteristic Configuration descriptor value shall be set to the default value at each connection with non-bonded devices.The characteristic descriptor value is a bit field. When a bit is set, that action shall be enabled, otherwise it will not be used. The *Client Characteristic Configuration* descriptor may occur in any position within the characteristic definition after the Characteristic Value. Only one *Client Characteristic Configuration* declaration shall exist in a characteristic definition.

A client may write this configuration descriptor to control the configuration of this characteristic on the server for the client. Each client has its own instantiation of the *Client Characteristic Configuration*. Reads of the *Client Characteristic Configuration* only shows the configuration for that client and writes only affect the configuration of that client. Authentication and authorization may be required by the server to write the configuration descriptor. The *Client Characteristic Configuration* declaration shall be readable and writable.

The characteristic descriptor is contained in an Attribute. The *Attribute Type* shall be set to the UUID for «Client Characteristic Configuration». The *Attribute Value* shall be two octets in length and shall be set to the characteristic descriptor value. The *Attribute Permissions* are specified by the profile or may be implementation specific if not specified otherwise.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0x2902 – UUID for «Client Characteristic Configuration» | Characteristic Configuration Bits | Readable with no authentication or authorization.  Writable with authentication and authorization defined by a higher layer specification or is implementation specific. |

Table 3.10: Client Characteristic Configuration declaration

The following Client Characteristic Configuration bits are defined:

| Bit Number | Configuration | Description |
| --- | --- | --- |
| 0 | Notification | The Characteristic Value shall be notified.This value can only be set if the characteristic’s properties have the notify bit set. |
| 1 | Indication | The Characteristic Value shall be indicated. This value can only be set if the characteristic’s properties have the indicate bit set. |
| All other bits |  | Reserved for future use. |

Table 3.11: Client Characteristic Configuration bit field definition

The default value for the *Client Characteristic Configuration* descriptor value shall be 0x0000.

Between a client and a server there shall be a single Client Characteristic Configuration Descriptor irrespective of the number of ATT bearers between them.

#### 3.3.3.4. Server Characteristic Configuration

The *Server Characteristic Configuration* declaration is an optional characteristic descriptor that defines how the characteristic may be configured for the server. The characteristic descriptor value is a bit field. When a bit is set, that action shall be enabled, otherwise it will not be used. The *Server Characteristic Configuration* descriptor may occur in any position within the characteristic definition after the *Characteristic Value*. Only one *Server Characteristic Configuration* declaration shall exist in a characteristic definition. The *Server Characteristic Configuration* declaration shall be readable and writable.

A client may write this configuration descriptor to control the configuration of this characteristic on the server for all clients. There is a single instantiation of the *Server Characteristic Configuration* for all clients. Reads of the *Server Characteristic Configuration* shows the configuration all clients and writes affect the configuration for all clients. Authentication and authorization may be required by the server to write the configuration descriptor.

The characteristic descriptor is contained in an Attribute. The *Attribute Type* shall be set to the UUID for «Server Characteristic Configuration». The *Attribute Value* shall be two octets in length and shall be set to the characteristic descriptor value. The *Attribute Permissions* are specified by the profile or may be implementation specific if not specified otherwise.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0x2903 – UUID for «Server Characteristic Configuration» | Characteristic Configuration Bits | Readable with no authentication or authorization.  Writable with authentication and authorization defined by a higher layer specification or is implementation specific. |

Table 3.12: Server Characteristic Configuration declaration

The following *Server Characteristic Configuration* bits are defined:

| Bit Number | Configuration | Description |
| --- | --- | --- |
| 0 | Broadcast | The Characteristic Value shall be broadcast when the server is in the broadcast procedure if advertising data resources are available. This value can only be set if the characteristic’s properties have the broadcast bit set. |
| All other bits |  | Reserved for future use. |

Table 3.13: Server Characteristic Configuration bit field definition

#### 3.3.3.5. Characteristic Presentation Format

The *Characteristic Presentation Format* declaration is an optional characteristic descriptor that defines the format of the *Characteristic Value*. The characteristic descriptor may occur in any position within the characteristic definition after the *Characteristic Value*. If more than one *Characteristic Presentation Format* declaration exists in a characteristic definition, then a *Characteristic Aggregate Format* declaration shall exist as part of the characteristic definition.

The characteristic presentation format value is composed of five parts: format, exponent, unit, name space, and description.

The characteristic descriptor is contained in an Attribute. The *Attribute Type* shall be set to the UUID for «Characteristic Presentation Format». The *Attribute Value* shall be set to the characteristic descriptor value. The *Attribute Permissions* shall be read only and not require authentication or authorization.

| Attribute Handle | Attribute Type | Attribute Value | | | | | Attribute Permissions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2904 – UUID for «Characteristic Presentation Format» | Format | Exponent | Unit | Name Space | Description | Read only  No Authentication,  No Authorization |

Table 3.14: Characteristic Presentation Format declaration

The definition of the Characteristic Presentation Format descriptor Attribute Value field is the following.

| Field Name | Value Size | Description |
| --- | --- | --- |
| Format | 1 octet | Format of the value of this characteristic as defined in [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)]. |
| Exponent | 1 octet | Exponent field to determine how the value of this characteristic is further formatted. |
| Unit | 2 octets | The unit of this characteristic as defined in [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)] |
| Name Space | 1 octet | The name space of the description as defined in [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)] |
| Description | 2 octets | The description of this characteristic as defined in a higher layer profile. |

Table 3.15: Characteristic Presentation Format value definition

#### 3.3.3.5.1. Bit ordering

The bit ordering used for the Characteristic Presentation Format descriptor shall be little-endian.

#### 3.3.3.5.2. Format

The format field determines how a single value contained in the *Characteristic Value* is formatted. The values of this field are defined in Assigned Numbers [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)].

#### 3.3.3.5.3. Exponent

The exponent field is used with integer data types to determine how the value is further formatted. The exponent field is only used on integer format types. The exponent field has type sint8.

actual value = *Characteristic Value* \* 10Exponent

As can be seen in the above equation, the actual value is a combination of the Characteristic Value and the value 10 to the power Exponent. This is sometimes known as a fixed point number.

For example, if the Exponent is 2 and the *Characteristic Value* is 23, the actual value would be 2300.

For example, if the Exponent is -3 and the *Characteristic Value* is 3892, the actual value would be 3.892.

#### 3.3.3.5.4. Unit

The Unit is a UUID as defined in [Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers) [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)].

#### 3.3.3.5.5. Name Space

The Name Space field is used to identify the organization, as defined in [Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers) [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)], that is responsible for defining the enumerations for the description field.

#### 3.3.3.5.6. Description

The Description is an enumerated value as defined in [Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers) [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)] from the organization identified by the Name Space field.

#### 3.3.3.6. Characteristic Aggregate Format

The *Characteristic Aggregate Format* declaration is an optional characteristic descriptor that defines the format of an aggregated *Characteristic Value*.

The characteristic descriptor may occur in any position within the characteristic definition after the *Characteristic Value*. Only one *Characteristic Aggregate Format* declaration shall exist in a characteristic definition.

The Characteristic Aggregate Format value is composed of a list of Attribute Handles of *Characteristic Presentation Format* declarations, where each *Attribute Handle* points to a *Characteristic Presentation Format* declaration.

The *Attribute Permissions* shall be read only and not require authentication or authorization.

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permissions |
| --- | --- | --- | --- |
| 0xNNNN | 0x2905 – UUID for «Characteristic Aggregate Format» | List of *Attribute Handles* for the Characteristic Presentation Format Declarations | Read only  No authentication  No authorization |

Table 3.16: Characteristic Aggregate Format declaration

The *List of Attribute Handles* is the concatenation of multiple 16-bit *Attribute Handle* values into a single *Attribute Value*. The list shall contain at least two *Attribute Handle for Characteristic Presentation Format declarations*. The Characteristic Value shall be decomposed by each of the *Characteristic Presentation Format* declarations pointed to by the *Attribute Handles*. The order of the *Attribute Handles* in the list is significant.

If more than one *Characteristic Presentation Format* declarations exist in a characteristic definition, there shall also be one Characteristic Aggregate Format declaration. The *Characteristic Aggregate Format* declaration shall include each *Characteristic Presentation Format* declaration in the characteristic definition in the list of *Attribute Handles*. Characteristic Presentation Format declarations from other characteristic definitions may also be used.

A *Characteristic Aggregate Format* declaration may exist without a *Characteristic Presentation Format* declaration existing in the characteristic definition. The *Characteristic Aggregate Format* declaration may use *Characteristic Presentation Format* declarations from other characteristic definitions.

### 3.4. Summary of GATT Profile attribute types

[Table 3.17](generic-attribute-profile--gatt-.html#UUID-1006e684-4a22-9c69-642a-876c98793a2f_table-idm13358912381556 "Table 3.17: Summary of GATT Profile attribute types") summarizes the attribute types defined by the GATT Profile.

| Attribute Type | UUID | Description |
| --- | --- | --- |
| «Primary Service» | 0x2800 | Primary Service Declaration |
| «Secondary Service» | 0x2801 | Secondary Service Declaration |
| «Include» | 0x2802 | Include Declaration |
| «Characteristic» | 0x2803 | Characteristic Declaration |
| «Characteristic Extended Properties» | 0x2900 | Characteristic Extended Properties |
| «Characteristic User Description» | 0x2901 | Characteristic User Description Descriptor |
| «Client Characteristic Configuration» | 0x2902 | Client Characteristic Configuration Descriptor |
| «Server Characteristic Configuration» | 0x2903 | Server Characteristic Configuration Descriptor |
| «Characteristic Presentation Format» | 0x2904 | Characteristic Presentation Format Descriptor |
| «Characteristic Aggregate Format» | 0x2905 | Characteristic Aggregate Format Descriptor |

Table 3.17: Summary of GATT Profile attribute types
