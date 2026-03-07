# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 7. Defined Generic Attribute Profile service

All characteristics defined within this section shall be contained in a primary service with the service UUID set to «GATT Service» as defined in  [Section 3.1](generic-attribute-profile--gatt-.html#UUID-2148a3e6-91f7-e758-750f-8b14377cab6e "3.1 Service definition"). Only one instance of the GATT service shall be exposed on a GATT Server.

[Table 7.1](generic-attribute-profile--gatt-.html#UUID-25a99b97-5f9a-6d55-c6c0-381a55b667a9_table-idm13358912909944 "Table 7.1: GATT Profile service characteristic support") lists characteristics that may be present in the server and the characteristics that may be supported by the client.

| Characteristic | Ref. | Support in Client | Support in Server |
| --- | --- | --- | --- |
| Service Changed | [7.1](generic-attribute-profile--gatt-.html#UUID-6ee92321-3db4-dad2-554e-946a80ff7435 "7.1 Service Changed") | M | C.1 |
| Client Supported Features | [7.2](generic-attribute-profile--gatt-.html#UUID-8481d6cb-91d1-ee20-e40b-9e2bcc6e60f5 "7.2 Client Supported Features") | O | C.2 |
| Database Hash | [7.3](generic-attribute-profile--gatt-.html#UUID-cc9d0db2-8c48-0611-ff58-4b9323fc4d12 "7.3 Database Hash") | O | O |
| Server Supported Features | [7.4](generic-attribute-profile--gatt-.html#UUID-d42e9f3c-fbec-1849-cac4-127fc7de6c4c "7.4 Server Supported Features") | O | C.3 |

Table 7.1: GATT Profile service characteristic support

C.1:
:   Mandatory if service definitions on the server can be added, changed, or removed; otherwise optional

C.2:
:   Mandatory if the *Database Hash* and *Service Changed* characteristics are supported or if Enhanced ATT Bearer or Multiple Variable Length Notification are supported; otherwise excluded

C.3:
:   Mandatory if any of the features in [Table 7.11](generic-attribute-profile--gatt-.html#UUID-d42e9f3c-fbec-1849-cac4-127fc7de6c4c_N1680884813042 "Table 7.11: Server Supported Features bit assignments") are supported, otherwise optional

The assigned UUIDs for these characteristics are defined in [Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers) [[1](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355391050)].

### 7.1. Service Changed

The «Service Changed» characteristic is a control-point attribute (as defined in [[Vol 3]
Part F,
Section 3.2.6](attribute-protocol--att-.html#UUID-320db6f0-7699-6e2f-4acd-e1bf2718e009 "3.2.6 Control-point attributes")) that shall be used to indicate to connected devices that services have changed (i.e., added, removed or modified). The characteristic shall be used to indicate to clients that have a trusted relationship (i.e. bond) with the server when GATT based services have changed when they re-connect to the server. See  [Section 2.5.2](generic-attribute-profile--gatt-.html#UUID-542d3f08-c238-c464-d662-b3982828e5bc "2.5.2 Attribute caching").

This *Characteristic Value* shall be configured to be indicated using the Client Characteristic Configuration descriptor by a client. Indications caused by changes to the Service Changed Characteristic Value shall be considered lost if the client has erroneously not enabled indications in the Client Characteristic Configuration descriptor (see [[Vol 3]
Part F,
Section 3.3.3](attribute-protocol--att-.html#UUID-55e35307-dcf7-8b68-15b4-fbfcd86799a3 "3.3.3 Transaction")).

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2803 – UUID for «Characteristic» | Characteristic Properties = 0x20 | 0xMMMM = Handle of Characteristic Value | 0x2A05 – UUID for «Service Changed» | No Authentication,  No Authorization |

Table 7.2: Service Changed Characteristic declaration

The *Service Changed Characteristic Value* is two 16-bit *Attribute Handles* concatenated together indicating the beginning and ending *Attribute Handles* affected by an addition, removal, or modification to a GATT-based service on the server. A change to a characteristic value is not considered a modification of the service. If a change has been made to any of the GATT service definition characteristic values other than the *Service Changed* characteristic value and the *Client Supported Features* characteristic value, the range shall also include the beginning and ending *Attribute Handle* for the GATT service definition.

| Attribute Handle | Attribute Type | Attribute Value | | Attribute Permission |
| --- | --- | --- | --- | --- |
| 0xMMMM | 0x2A05 – UUID for «Service Changed» | 0xSSSS – Start of Affected Attribute Handle Range | 0xTTTT – End of Affected Attribute Handle Range | No Authentication,  No Authorization, Not Readable, Not Writable |

Table 7.3: Service Changed Characteristic Value declaration

There shall be only one instance of the *Service Changed* characteristic within the GATT service definition. A *Service Changed* characteristic value shall exist for each client with a trusted relationship.

If the list of GATT based services and the service definitions cannot change for the lifetime of the device then this characteristic shall not exist, otherwise this characteristic shall exist.

If the *Service Changed* characteristic exists on the server, the *Characteristic Value Indication* support on the server is mandatory.

The client shall support *Characteristic Value Indication* of the *Service Changed* characteristic.

The *Service Changed* characteristic *Attribute Handle* on the server shall not change if the server has a trusted relationship with any client.

### 7.2. Client Supported Features

The *Client Supported Features* characteristic is used by the client to inform the server which features are supported by the client. If the characteristic exists on the server, the client may update the *Client Supported Features* bit field. If a client feature bit is set by a client and the server supports that feature, the server shall fulfill all requirements associated with this feature when communicating with this client. If a client feature bit is not set by a client, then the server shall not use any of the features associated with that bit when communicating with this client.

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2803 – UUID for «Characteristic» | Characteristic Properties = 0x0A | 0xMMMM = Handle of Characteristic Value | 0x2B29 – UUID for «Client Supported Features» | Read only,  No Authentication,  No Authorization |

Table 7.4: Client Supported Features characteristic declaration

The format of the *Client Supported Features* characteristic is defined in  [Table 7.5](generic-attribute-profile--gatt-.html#UUID-8481d6cb-91d1-ee20-e40b-9e2bcc6e60f5_table-idm13359011484318 "Table 7.5: Client Supported Features value declaration").

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xMMMM | 0x2B29 - UUID for «Client Supported Features» | 0xXX...XX (variable length) - Client Features | | | Readable,  Writable,  No Authentication,  No Authorization |

Table 7.5: Client Supported Features value declaration

The *Client Supported Features* characteristic value is an array of octets, each of which is a bit field. The allocation of these bits is specified in  [Table 7.6](generic-attribute-profile--gatt-.html#UUID-8481d6cb-91d1-ee20-e40b-9e2bcc6e60f5_table-idm13359011479034 "Table 7.6: Client Supported Features bit assignments"). All bits not listed are reserved for future use. The array should not have any trailing zero octets.

If any octet number in  [Table 7.6](generic-attribute-profile--gatt-.html#UUID-8481d6cb-91d1-ee20-e40b-9e2bcc6e60f5_table-idm13359011479034 "Table 7.6: Client Supported Features bit assignments") does not appear in the attribute value because it is too short, the server shall behave as if that octet were present with a value of zero.

| Client Features | Octet | Bit | Ref. | Description |
| --- | --- | --- | --- | --- |
| Robust Caching | 0 | 0 | [2.5.2.1](generic-attribute-profile--gatt-.html#UUID-787b0d4d-3112-9b07-6bef-89dda173a489 "2.5.2.1 Robust Caching") | The client supports robust caching |
| Enhanced ATT bearer | 0 | 1 | [5.3](generic-attribute-profile--gatt-.html#UUID-2f352749-51c3-45d3-fb4e-63d05aab9263 "5.3 Enhanced ATT bearer L2CAP interoperability requirements") | The client supports Enhanced ATT bearer |
| Multiple Handle Value Notifications | 0 | 2 | [4.10.2](generic-attribute-profile--gatt-.html#UUID-ef60fab0-0495-034a-7f7d-574b6721bb69 "4.10.2 Multiple Variable Length Notifications") | The client supports receiving ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDUs |

Table 7.6: Client Supported Features bit assignments

The default value for the *Client Supported Features* characteristic value shall be all bits set to zero.

There shall be only one instance of the *Client Supported Features* characteristic within the GATT service definition.

A *Client Supported Features* characteristic value shall exist for each connected client. For clients with a trusted relationship, the characteristic value shall be persistent across connections. For clients without a trusted relationship the characteristic value shall be set to the default value at each connection.

The Attribute Handle of the *Client Supported Features* characteristic on the server shall not change during a connection or if the server has a trusted relationship with any client.

A client shall not clear any bits it has set. The server shall respond to any such request with the Error Code parameter set to *Value Not Allowed* (0x13).

### 7.3. Database Hash

The *Database Hash* characteristic contains the result of a hash function applied to the service definitions in the GATT database. The client may read the characteristic at any time to determine if services have been added, removed, or modified. If any of the input fields to the hash function (as listed in  [Section 7.3.1](generic-attribute-profile--gatt-.html#UUID-d010b640-e044-bf72-03ef-617e329d3992 "7.3.1 Database Hash calculation")) have changed, the server shall calculate a new Database Hash and update the characteristic value.

The *Database Hash* characteristic is a read-only attribute.

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2803 – UUID for «Characteristic» | Characteristic Properties = 0x02 | 0xMMMM = Handle of Characteristic Value | 0x2B2A – UUID for «Database Hash» | Read only,  No Authentication,  No Authorization |

Table 7.7: Database Hash characteristic declaration

The characteristic value is a 128-bit unsigned integer number. The calculation of the Database Hash is specified in  [Section 7.3.1](generic-attribute-profile--gatt-.html#UUID-d010b640-e044-bf72-03ef-617e329d3992 "7.3.1 Database Hash calculation").

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xMMMM | 0x2B2A - UUID for «Database Hash» | uint128 - Database Hash | | | Read only,  No Authentication,  No Authorization |

Table 7.8: Database Hash characteristic value declaration

There is only one instance of the *Database Hash* characteristic within the GATT service definition. The same *Database Hash* value is used for all clients, whether a trusted relationship exists or not.

In order to read the value of this characteristic the client shall always use the *GATT Read Using Characteristic UUID* sub-procedure. The *Starting Handle* should be set to 0x0001 and the *Ending Handle* should be set to 0xFFFF.

If a client reads the value of this characteristic while the server is re-calculating the hash following a change to the database, the server shall return the new hash, delaying its response until it is available.

#### 7.3.1. Database Hash calculation

The Database Hash shall be calculated according to RFC-4493 [[2](generic-attribute-profile--gatt-.html#UUID-c32d82db-0074-99ba-c52a-307a41944215_bibliomixed-idm13391355404606)]. This RFC defines the Cipher-based Message Authentication Code (CMAC) using AES-128 as the block cipher function, also known as AES-CMAC.

The inputs to AES-CMAC are:

*m* is the variable length data to be hashed
*k* is the 128-bit key, which shall be all zero
(0x00000000\_00000000\_00000000\_00000000)

The 128-bit Database Hash is generated as follows:

Database Hash = AES-CMACk(m), where *m* is calculated as follows:

|  |  |
| --- | --- |
|  | In ascending order of attribute handles, starting with the first handle, concatenate the fields *Attribute Handle*, *Attribute Type*, and *Attribute Value* if the attribute has one of the following types: «Primary Service», «Secondary Service», «Included Service», «Characteristic», or «Characteristic Extended Properties», concatenate the fields *Attribute Handle* and *Attribute Type* if the attribute has one of the following types: «Characteristic User Description», «Client Characteristic Configuration», «Server Characteristic Configuration», «Characteristic Presentation Format», or «Characteristic Aggregate Format», and ignore the attribute if it has any other type (such attributes are not part of the concatenation). |
|  | For each *Attribute Handle*, the fields shall be concatenated in the order given above. The byte order used for each field or sub-field value shall be little-endian. If a field contains sub-fields, the subfields shall be concatenated in the order they appear in  [Section 3](generic-attribute-profile--gatt-.html#UUID-84c0a288-84cc-29aa-4074-6c3a0713b2d5 "3 Service interoperability requirements") (Service Interoperability Requirements). For instance, a characteristic declaration value of {0x02, 0x0005, 0x2A00} is represented after concatenation as 02 05 00 00 2A. |

The formats of the fields *Attribute Handle*, *Attribute Type*, and *Attribute Value* for the Attribute Types listed above are defined in  [Section 3](generic-attribute-profile--gatt-.html#UUID-84c0a288-84cc-29aa-4074-6c3a0713b2d5 "3 Service interoperability requirements") (Service Interoperability Requirements).

If the length of *m* is not a multiple of the AES-CMAC block length of 128 bits, padding shall be applied as specified in RFC-4493 Section 2.4.

### 7.4. Server Supported Features

The *Server Supported Features* characteristic is a read-only characteristic that shall be used to indicate support for server features. The server shall set a bit only if the corresponding feature is supported.

| Attribute Handle | Attribute Type | Attribute Value | | | Attribute Permission |
| --- | --- | --- | --- | --- | --- |
| 0xNNNN | 0x2803 – UUID for «Characteristic» | Characteristic Properties = 0x02 | 0xMMMM = Handle of Characteristic Value | 0x2B3A – UUID for «Server Supported Features» | Read Only,  No Authentication,  No Authorization |

Table 7.9: Server Supported Features characteristic declaration

| Attribute Handle | Attribute Type | Attribute Value | Attribute Permission |
| --- | --- | --- | --- |
| 0xMMMM | 0x2B3A – UUID for «Server Supported Features» | 0xuu - Server Supported Features | Readable |

Table 7.10: Server Supported Features value declaration

The *Server Supported Features* characteristic is an array of octets, each of which is a bit field. The allocation of these bits is specified in  [Table 7.11](generic-attribute-profile--gatt-.html#UUID-d42e9f3c-fbec-1849-cac4-127fc7de6c4c_N1680884813042 "Table 7.11: Server Supported Features bit assignments"). All bits not listed are reserved for future use. The array should not have any trailing zero octets.

| Server Supported Features | Octet | Bit | Ref. | Description |
| --- | --- | --- | --- | --- |
| EATT Supported | 0 | 0 | [5.3](generic-attribute-profile--gatt-.html#UUID-2f352749-51c3-45d3-fb4e-63d05aab9263 "5.3 Enhanced ATT bearer L2CAP interoperability requirements") | Enhanced ATT bearer supported |

Table 7.11: Server Supported Features bit assignments

If any octet number in  [Table 7.11](generic-attribute-profile--gatt-.html#UUID-d42e9f3c-fbec-1849-cac4-127fc7de6c4c_N1680884813042 "Table 7.11: Server Supported Features bit assignments") does not appear in the attribute value because it is too short, the client shall behave as if that octet were present with the value of zero.

There shall be only one instance of the *Server Supported Features* characteristic within the GATT service definition.
