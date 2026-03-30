# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 7. Mesh GATT services

This section defines two GATT-based services: The Mesh Provisioning Service and the Mesh Proxy Service.

A device may support the Mesh Provisioning Service or the Mesh Proxy Service or both. If both are supported, only one of these services shall be exposed in the GATT database at a time.

The endianness of all multiple-octet numeric values shall be the same as the endianness defined in GATT (see [Vol 3], Part G, Section 2.4, in [[24](index-en.html#idp254804)]).

### 7.1. Mesh Provisioning Service

#### 7.1.1. Introduction

The Mesh Provisioning Service allows a PB-GATT Client to provision a PB-GATT Server to allow it to participate in the mesh network.

##### 7.1.1.1. Conformance

Each capability of this specification shall be supported in the specified manner. This specification may provide options for design flexibility, because, for example, some products do not implement every portion of the specification. For each implementation option that is supported, it shall be supported as specified.

##### 7.1.1.2. Service dependency

This service has no dependencies on other GATT-based services.

##### 7.1.1.3. Bluetooth specification release compatibility

This service is compatible with any Bluetooth Core Specification that includes GATT and the Bluetooth Low Energy Controller portions of the Core Specification.

* Bluetooth Core Specification 4.2 or later [[1](index-en.html#idp254740)].

##### 7.1.1.4. GATT sub-procedure requirements

Requirements in this section represent a minimum set of requirements for a server. Other GATT sub-procedures may be used if supported by both client and server.

[Table 7.1](index-en.html#UUID-6dc13de3-642b-5bd3-c05a-28f97ad8e360_Table_7.1 "Table 7.1. Additional GATT sub-procedure requirements") summarizes additional GATT sub-procedures required beyond those required by all GATT servers.

| **GATT Sub-procedure** | **Requirements** |
| --- | --- |
| Write Without Response | M |
| Notifications | M |
| Write Characteristic Descriptors | M |

Table 7.1. Additional GATT sub-procedure requirements

##### 7.1.1.5. Transport dependencies

The PB-GATT Provisioning Service operates over the LE Physical Transport only. The specified functionality enables devices to participate in low energy mesh networks, and therefore support for the LE Physical Transport is required.

##### 7.1.1.6. Application error codes

No application error codes are defined by this service.

#### 7.1.2. Service requirements

##### 7.1.2.1. Declaration

The Mesh Provisioning Service shall be instantiated as a «Primary Service».

There shall only be one instance of the Mesh Provisioning Service on an unprovisioned PB-GATT Server.

After the PB-GATT Server has been provisioned, the Mesh Provisioning Service on that PB-GATT Server shall cease to be present in the GATT database for that GATT Client as long as the node remains provisioned.

The Service UUID shall be set to «Mesh Provisioning Service», as defined in [[4](index-en.html#idp254746)].

##### 7.1.2.2. Behaviors

The Mesh Provisioning Service may be used by a PB-GATT Client to provision a PB-GATT Server to participate in a mesh network.

###### 7.1.2.2.1. Advertising

The PB-GATT Server is only active and advertising when the device is not provisioned. The PB-GATT Server shall be discoverable by using connectable and scannable undirected advertising events in the format described in [Table 7.2](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b_Table_7.2 "Table 7.2. Advertisement Data for the Mesh Provisioning Service").

| **AD Type** | **Total Length** | **Requirement** | **Comments** |
| --- | --- | --- | --- |
| «Flags» | 3 | M | – |
| «Incomplete List of 16-bit Service UUIDs» or  «Complete List of 16-bit Service UUIDs» | variable (4 or more) | M | Include «Mesh Provisioning Service» |
| «Service Data» | 22 | M | Service Data AD Type for «Mesh Provisioning Service» followed by Service Data for this service |

Table 7.2. Advertisement Data for the Mesh Provisioning Service

The format of the Service Data for the «Mesh Provisioning Service» is defined in [Table 7.3](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b_Table_7.3 "Table 7.3. Service Data for Mesh Provisioning Service") and illustrated in [Figure 7.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b_figure-idm4557730843273634120996858125 "Figure 7.1. PB-GATT Advertising Data").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Device UUID | 16 | See [Section 3.11.3](index-en.html#UUID-29a75fe3-e98f-0067-f6c7-34aeec2c83f8 "3.11.3. Device UUID") | M |
| OOB Information | 2 | See [Table 3.78](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869_Table_3.78 "Table 3.78. OOB Information field") | M |

Table 7.3. Service Data for Mesh Provisioning Service

The format of the Device UUID field is defined in [Section 3.11.3](index-en.html#UUID-29a75fe3-e98f-0067-f6c7-34aeec2c83f8 "3.11.3. Device UUID").

The format of the OOB Information field is uint16 and is defined in [Table 3.78](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869_Table_3.78 "Table 3.78. OOB Information field").

![PB-GATT Advertising Data](image/1671b81d8b00b0.png)

Figure 7.1. PB-GATT Advertising Data

If PB-ADV Server is supported, an unprovisioned PB-GATT Server that supports PB-GATT has to interleave the connectable advertising for PB-GATT with the Unprovisioned Device beacon (see [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon")).

It is required to include the Service UUID List to allow discovery of the Mesh Provisioning Service.

URI, Appearance, TX Power Level, and Local Name AD types may optionally be included in the scan response data. The PB-GATT Server should support these data types to allow a PB-GATT Client to enhance the user experience while provisioning.

If the device supports provisioning records (see [Section 5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer")), and the PB-GATT provisioning bearer is supported by the device, the
Provisioning Server shall set bit 8 of the OOB Information field of the PB-GATT Service Data advertisements.

If a Device Certificate (as defined in [Section 5.5.1](index-en.html#UUID-054195c8-b1c3-b7b4-4137-73c200e03e4e "5.5.1. Device Certificate")) has been issued for the device and made available for retrieval (see Sections [5.4.2.6](index-en.html#UUID-21acd150-1d29-1b68-2b8f-cc09419234f5 "5.4.2.6. Provisioning record retrieval over a provisioning bearer") and [5.6](index-en.html#UUID-94433614-8bd2-3c22-cd1d-9c760ca1c13f "5.6. Device Certificate retrieval over the Internet")), the
device shall also support provisioning records. The Provisioning Server shall set bit 7 of the OOB Information field of the Service Data to indicate device’s support for certificate-based provisioning, and shall set bit 8 to indicate support for provisioning records.

###### 7.1.2.2.2. ATT_MTU

The PB-GATT Server should support an ATT_MTU size equal to or larger than 69 octets to accommodate the longest known Provisioning message (see [Section 5.3](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4 "5.3. Generic provisioning layer")).

#### 7.1.3. Mesh Provisioning Service characteristics

The characteristics shown in [Table 7.4](index-en.html#UUID-73af1792-e118-3d47-934f-33b408fe97cc_Table_7.4 "Table 7.4. Mesh Provisioning Service characteristics") are exposed in the Mesh Provisioning Service. Only one instance of each characteristic is permitted
within this service. The characteristic formats and UUIDs are defined in [[4](index-en.html#idp254746)].

Where a characteristic can be notified, a Client Characteristic Configuration descriptor shall be included in that characteristic as required by the Core Specification [[1](index-en.html#idp254740)].

| **Characteristic Name** | **Requirement** | **Mandatory Properties** | **Optional Properties** | **Security Permissions** |
| --- | --- | --- | --- | --- |
| Mesh Provisioning Data In | M | Write Without Response | None | Writeable with or without authentication or authorization when unprovisioned |
| Mesh Provisioning Data Out | M | Notify | None | Notifiable with or without authentication or authorization when unprovisioned |

Table 7.4. Mesh Provisioning Service characteristics

##### 7.1.3.1. Mesh Provisioning Data In characteristic

The Mesh Provisioning Data In characteristic can be written to send a Proxy PDU message (see [Section 6.3.1](index-en.html#UUID-30c7f122-47dc-b7d1-6c63-b67387470620 "6.3.1. PDU format")) containing Provisioning PDU (see [Section 5.3](index-en.html#UUID-32d6dbfb-4b16-48e6-ba11-3fd86ba2cfd4 "5.3. Generic provisioning layer")) to the PB-GATT Server.

The Mesh Provisioning Data In characteristic is identified using the UUID «Mesh Provisioning Data In», as defined in [[4](index-en.html#idp254746)].

The characteristic value is 66 octets long to accommodate the longest known Proxy PDU containing Provisioning PDU.

###### 7.1.3.1.1. Characteristic behavior

The Mesh Provisioning Data In characteristic is used to transmit Proxy PDU message containing Provisioning PDU from a PB-GATT Client to a PB-GATT Server.

A PB-GATT Server is not required to support bonding.

The Mesh Provisioning Data In characteristic shall support Proxy PDU messages containing Provisioning PDUs and shall not support other Proxy PDU type messages.

##### 7.1.3.2. Mesh Provisioning Data Out characteristic

The Mesh Provisioning Data Out characteristic can be notified to send a Proxy PDU message containing Provisioning PDU from a PB-GATT Server to a PB-GATT Client.

The Mesh Provisioning Data Out characteristic is identified using the UUID «Mesh Provisioning Data Out», as defined in [[4](index-en.html#idp254746)].

The characteristic value is 66 octets long to accommodate the longest known Proxy PDU message containing Provisioning PDU.

###### 7.1.3.2.1. Characteristic behavior

The Mesh Provisioning Data Out characteristic is used to Proxy PDU message containing Provisioning PDU from a PB-GATT Server to a PB-GATT Client.

A PB-GATT Server is not required to support bonding. As a bonding relationship is not established between the PB-GATT Client and the PB-GATT Server, the PB-GATT Client shall enable notifications (write value 0x0001) to the Mesh Provisioning Data Out Client Characteristic Configuration Descriptor after a connection is
established and before sending the first message of the Proxy PDU.

The Mesh Provisioning Data Out characteristic shall support Proxy PDU messages containing Provisioning PDUs and shall not support other Proxy PDU type messages.

### 7.2. Mesh Proxy Service

#### 7.2.1. Introduction

The Mesh Proxy Service is used to enable a node to send and receive Proxy PDUs via the GATT bearer.

The Mesh Proxy Service is contained in the GATT Server on a node if any of the following features or functionalities are supported:

* Proxy feature (see [Section 3.4.6.2](index-en.html#UUID-6dc6d66e-045f-96cb-8e8e-40b0c7de986a "3.4.6.2. Proxy feature"))
* Private Proxy functionality (see [Section 3.4.6.6](index-en.html#UUID-a8199519-1f47-2247-2c6f-f518335503b8 "3.4.6.6. Private Proxy functionality"))
* Node Identity functionality (see [Section 3.4.6.7](index-en.html#UUID-17a8996b-9dd3-4d56-3894-eb988df29bd3 "3.4.6.7. Node Identity functionality"))
* Private Node Identity functionality (see [Section 3.4.6.8](index-en.html#UUID-511212c8-db7d-b004-42b4-65932b69b2c1 "3.4.6.8. Private Node Identity functionality"))

##### 7.2.1.1. Conformance

Each capability of this specification shall be supported in the specified manner. This specification may provide options for design flexibility, because, for example, some products do not implement every portion of the specification. For each implementation option that is supported, it shall be supported as specified.

##### 7.2.1.2. Service dependency

This service has no dependencies on other GATT-based services.

##### 7.2.1.3. Bluetooth specification release compatibility

This service is compatible with any Bluetooth Core Specification that includes GATT and the Bluetooth Low Energy Controller portions of the Core Specification.

* Bluetooth Core Specification 4.2 or later [[1](index-en.html#idp254740)].

##### 7.2.1.4. GATT sub-procedure requirements

Requirements in this section represent a minimum set of requirements for a server. Other GATT sub-procedures may be used if supported by both client and server.

[Table 7.5](index-en.html#UUID-59db6aec-f39e-e131-29b1-7576b35b8b8d_Table_7.5 "Table 7.5. Additional GATT sub-procedure requirements") summarizes additional GATT sub-procedures required beyond those required by all GATT servers.

| **GATT Sub-procedure** | **Requirements** |
| --- | --- |
| Write Without Response | M |
| Notifications | M |
| Write Characteristic Descriptors | M |

Table 7.5. Additional GATT sub-procedure requirements

##### 7.2.1.5. Transport dependencies

The Mesh Proxy Service operates over the LE Physical Transport only. The specified functionality enables devices to participate in low energy mesh networks, and therefore support for the LE Physical Transport is required.

##### 7.2.1.6. Application error codes

No application error codes are defined by this service.

#### 7.2.2. Service requirements

##### 7.2.2.1. Declaration

The Mesh Proxy Service shall be instantiated as a «Primary Service».

A device shall only have one instance of the Mesh Proxy Service.

The Service UUID shall be set to «Mesh Proxy Service», as defined in [[4](index-en.html#idp254746)].

##### 7.2.2.2. Behaviors

The Node Identity state or the Private Node Identity state for any subnet (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity") and [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")) indicates if the Mesh Proxy Service is exposed.

If the Node Identity state for any subnet is 0x00 or 0x01, the Mesh Proxy Service shall be present in the GATT database of a provisioned device and the rules for advertising and the GATT characteristics behavior apply as discussed in the following sections.

If the Private Node Identity state for any subnet is Disable (0x00) or Enable (0x01), the Mesh Proxy Service shall be present in the GATT database of a provisioned device, and the rules for advertising and the GATT characteristics behavior apply as discussed in the following subsections from [7.2.2.2.1](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155 "7.2.2.2.1. Advertising") to [7.2.2.2.5](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e "7.2.2.2.5. Advertising with Private Node Identity").

If the Node Identity state or the Private Node Identity state for any subnet is 0x02, the Mesh Proxy Service shall not be present in the GATT database, and the UUID for "Mesh Proxy Service" shall not be indicated in the advertisements.

###### 7.2.2.2.1. Advertising

The server shall be discoverable by using connectable and scannable undirected advertising events in the format described in [Table 7.6](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.6 "Table 7.6. Advertisement Data for the Mesh Proxy Service").

| **AD Type** | **Total Length** | **Requirement** | **Comments** |
| --- | --- | --- | --- |
| «Flags» | 3 | M |  |
| «Incomplete List of 16-bit Service UUIDs» or  «Complete List of 16-bit Service UUIDs» | variable (4 or more) | M | Include «Mesh Proxy Service» |
| «Service Data» | 13 or 21 | M | Service Data AD Type for «Mesh Proxy Service» followed by Service Data for this service |

Table 7.6. Advertisement Data for the Mesh Proxy Service

The format of Service Data for the «Mesh Proxy Service» is defined in [Table 7.7](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.7 "Table 7.7. Service Data for Mesh Proxy Service").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | See [Table 7.8](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.8 "Table 7.8. Identification Type values ") | M |
| Identification Parameters | variable | Format determined by Identification Type field | M |

Table 7.7. Service Data for Mesh Proxy Service

The Identification Type field values are defined in [Table 7.8](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.8 "Table 7.8. Identification Type values ").

| Type Value | Description |
| --- | --- |
| 0x00 | Network ID type |
| 0x01 | Node Identity type |
| 0x02 | Private Network Identity type |
| 0x03 | Private Node Identity type |
| 0x04–0xFF | Reserved for Future Use |

Table 7.8. Identification Type values

A node that supports the Proxy feature and has the GATT Proxy state enabled shall support advertising with Network ID.

A node that supports the Proxy feature and has the Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")) enabled shall support advertising with Private Network Identity.

A node that does not support the Proxy feature or has the GATT Proxy state disabled shall not advertise with Network ID.

A node that does not support the Proxy feature or has the Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")) disabled shall not advertise with Private Network Identity.

The proxy advertising behavior is summarized in the [Table 7.9](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.9 "Table 7.9. Proxy advertising behavior ").

| GATT Proxy state | Private GATT Proxy state | Advertising |
| --- | --- | --- |
| 0x00 | Does Not Exist | No Proxy Advertising |
| 0x00 | Disable (0x00) | No Proxy Advertising |
| 0x00 | Enable (0x01) | Private Network Identity |
| 0x01 | Does Not Exist or Disable (0x00) | Network ID |
| 0x02 | Does Not Exist or Not Supported (0x02) | No Proxy Advertising |

Table 7.9. Proxy advertising behavior

### Note

Note: In [Table 7.9](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.9 "Table 7.9. Proxy advertising behavior "), Does Not Exist indicates that the Private GATT Proxy state is not present on the node.

A node may advertise with Node Identity or Private Node Identity regardless of the Proxy feature being supported or enabled.

The node identity advertising behavior is summarized in the [Table 7.10](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.10 "Table 7.10. Node identity advertising behavior").

| Node Identity state | Private Node Identity state | Advertising |
| --- | --- | --- |
| 0x00 | Does Not Exist | No Identity Advertising |
| 0x00 | Disable (0x00) | No Identity Advertising |
| 0x00 | Enable (0x01) | Private Node Identity |
| 0x01 | Does Not Exist or Disable (0x00) | Node Identity |
| 0x02 | Does Not Exist or Not Supported (0x02) | No Identity Advertising |

Table 7.10. Node identity advertising behavior

### Note on Node Identity Advertising

Note: In [Table 7.10](index-en.html#UUID-807c5051-d41e-a40c-23cb-9bfbb850c155_Table_7.10 "Table 7.10. Node identity advertising behavior"), Does Not Exist indicates that the Private Node Identity state is not present on the node.

The Identification Parameters for each Identification Type is defined in the subsections below.

The «Mesh Proxy Service» shall be included in the Incomplete List of 16-bit Service UUIDs or the Complete List of 16-bit Service UUIDs.

###### 7.2.2.2.2. Advertising with Network ID

The format of the Service Data for the «Mesh Proxy Service» when Advertising with Network ID is defined in [Table 7.11](index-en.html#UUID-1ef110fd-b50f-ca42-5702-05040dc29904_Table_7.11 "Table 7.11. Service Data for Mesh Proxy Service with Network ID ")
and illustrated in [Figure 7.2](index-en.html#UUID-1ef110fd-b50f-ca42-5702-05040dc29904_figure-idm4539442759678434120994356589 "Figure 7.2. Advertising with Network ID (Identification Type 0x00)").

When a server is a member of multiple subnets, it shall interleave the advertising of each subnet. The duration of the advertising is not limited.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | 0x00 (Network ID type) | M |
| Network ID | 8 | Identifies the network | M |

Table 7.11. Service Data for Mesh Proxy Service with Network ID

![Advertising with Network ID (Identification Type 0x00)](image/1671b81d8b7447.png)

Figure 7.2. Advertising with Network ID (Identification Type 0x00)

The Network ID field shall be set as defined in [Section 3.9.6.3.2](index-en.html#UUID-9165b597-82af-931c-cdf1-a7428285de39 "3.9.6.3.2. Network ID").

###### 7.2.2.2.3. Advertising with Node Identity

Advertising with Node Identity is used to identify a node based on the unicast address of the primary element and the network key of a subnet to which the node belongs. This can be useful when large amounts of data need to be delivered to a node via GATT for cases when the node cannot be easily identified or is not
advertising. This advertisement may be used to initiate a GATT connection to the selected node.

If PB-GATT is supported and the Mesh Proxy Service is present, immediately after provisioning is completed using PB-GATT (see [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT")), the Node Identity state shall be set to enabled
in order to enable advertising the Mesh Proxy Service with Node Identity for the subnet the node has been provisioned to.

When the server starts advertising as a result of user interaction, the server shall interleave the advertising of each subnet it is a member of. When the server starts advertising as a result of the Node Identity state being set to enabled, the server shall only advertise using the subnet that it was enabled on.

When the server starts advertising for a subnet as a result of user interaction, or as a result of the Node Identity state being set to enabled, the Node Identity timer corresponding to the subnet shall be stopped, if it is running, and started with the period set to 60 seconds. When the Node Identity timer expires, the
server shall stop advertising for the corresponding subnet and set the Node Identity state to disabled.

If the server stops advertising for a subnet with Node Identity before the corresponding Node Identity timer expires, for example because the server does not have sufficient resources to advertise during a connection, or it supports only a single connection, the server should resume advertising for a subnet when it is able
to do so while the corresponding Node Identity timer is still running. The Node Identity timer shall not be stopped or started when advertising stops or resumes while the timer is running.

When the server is advertising for a subnet with Node Identity, the Node Identity state for the subnet shall indicate that the server is advertising. When the server is not advertising for a subnet with Node Identity, the Node Identity state for the subnet shall indicate that the server is not advertising.

The format of the Service Data for the «Mesh Proxy Service» when Advertising with Node Identity is defined in [Table 7.12](index-en.html#UUID-be413278-d730-695e-84aa-093f6faec350_Table_7.12 "Table 7.12. Service Data for Mesh Proxy Service with Node Identity")
and illustrated in [Figure 7.3](index-en.html#UUID-be413278-d730-695e-84aa-093f6faec350_figure-idm4550630663307234120992451959 "Figure 7.3. Advertising with Node Identity (Identification Type 0x01)").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | 0x01 (Node Identity type) | M |
| Hash | 8 | Function of the included random number and identity information. | M |
| Random | 8 | 64-bit random number | M |

Table 7.12. Service Data for Mesh Proxy Service with Node Identity

![Advertising with Node Identity (Identification Type 0x01)](image/1671b81d8be981.png)

Figure 7.3. Advertising with Node Identity (Identification Type 0x01)

The Hash field is calculated as shown below:

|  |
| --- |
| *Hash=e(IdentityKey, Padding || Random || Address) mod 264* |

Where:

|  |  |
| --- | --- |
|  | Padding – 48 bits of padding, all bits set to 0.  Random – 64-bit random value.  Address – The unicast address of the node. |

The Random field is the 64-bit random value used in the Hash field calculation.

The creation of the encrypted node identity is illustrated in [Figure 7.4](index-en.html#UUID-be413278-d730-695e-84aa-093f6faec350_Figure_7.4 "Figure 7.4. Encrypted node identity creation").

|  |
| --- |
| Encrypted node identity creation |

Figure 7.4. Encrypted node identity creation

###### 7.2.2.2.4. Advertising with Private Network Identity

The format of the Service Data for the «Mesh Proxy Service» when Advertising with Private Network Identity is defined in [Table 7.13](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19_Table_7.13 "Table 7.13. Advertising with the Private Network Identity (Identification Type 0x02) ") and illustrated in [Figure 7.5](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19_figure-idm466060992789123412102204169 "Figure 7.5. Advertising with Private Network Identity (Identification Type 0x02)"). Private Network Identity advertising is controlled by the Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

When the server starts advertising with Private Network Identity as a result of the reception of a Solicitation PDU (see [Section 6.9.1](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf "6.9.1. Solicitation PDU")), the server shall only advertise the subnet
corresponding to the network key that is used to authenticate the Solicitation PDU; otherwise, the server shall interleave the advertising of each of its subnets. The duration of the advertising is not limited.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | 0x02 (Private Network Identity type) | M |
| Hash | 8 | Function of the included random number and identity information | M |
| Random | 8 | 64-bit random number | M |

Table 7.13. Advertising with the Private Network Identity (Identification Type 0x02)

![Advertising with Private Network Identity (Identification Type 0x02)](image/1671b81d8cd7ac.png)

Figure 7.5. Advertising with Private Network Identity (Identification Type 0x02)

The Hash field is calculated as shown below:

|  |
| --- |
| *Hash=e(IdentityKey, NetworkID || Random) mod 264* |

Where:

|  |  |
| --- | --- |
|  | NetworkID – 64 bits of Network ID (See [Section 3.9.6.3.2](index-en.html#UUID-9165b597-82af-931c-cdf1-a7428285de39 "3.9.6.3.2. Network ID"))  Random – 64-bit random value |

The Random field is the 64-bit random value used in the Hash field calculation.

The Random field should be updated every 10 minutes. The Private Network Identity advertisements shall use a resolvable private address or a non-resolvable private address in the AdvA field of the advertising PDU. The address used for the AdvA field shall be regenerated whenever the Random field is regenerated. The address
used for the AdvA field shall be different for each subnet.

The creation of Private Network Identity is illustrated in [Figure 7.6](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19_figure-idm4557730782942434121024949322 "Figure 7.6. Private Network Identity creation").

![Private Network Identity creation](image/1671b81d8d5ca3.png)

Figure 7.6. Private Network Identity creation

###### 7.2.2.2.5. Advertising with Private Node Identity

Advertising with Private Node Identity is used to identify a node based on the unicast address of the primary element and the network key of a subnet to which the node belongs. This can be useful when large amounts of data need to be delivered to a node via GATT for cases when the node cannot be easily identified or is not
advertising. This advertisement may be used to initiate a GATT connection to the selected node.

The Private Node Identity advertising is controlled by the Private Node Identity state (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")). The Private Node Identity state also indicates whether a server is
advertising with Private Node Identity or not.

When the server starts advertising with Private Node Identity as a result of user interaction, the server shall interleave the advertising of each subnet it is a member of. When the server starts advertising as a result of the Private Node Identity state being set to enabled, the server shall only advertise with Private Node
Identity for the subnet that the Private Node Identity state was enabled on.

When the server starts advertising for a subnet as a result of user interaction, or as a result of the Private Node Identity state being set to enabled, the Private Node Identity timer corresponding to the subnet shall be stopped, if it is running, and started with the period set to 60 seconds. When the Private Node Identity
timer expires, the server shall stop advertising for the corresponding subnet and set the Private Node Identity state to disabled.

If the server stops advertising with Private Node Identity for a subnet before the corresponding Private Node Identity timer expires, for example because the server does not have sufficient resources to advertise during a connection, or it supports only a single connection, the server should resume advertising for a subnet
when it is able to do so while the corresponding Private Node Identity timer is still running. The Private Node Identity timer shall not be stopped or started when advertising stops or resumes while the timer is running.

When the server is advertising with Private Node Identity for a subnet, the Private Node Identity state for the subnet shall indicate that the server is advertising. When the server is not advertising with Private Node Identity for a subnet, the Private Node Identity state for the subnet shall indicate that the server is not
advertising.

The format of the Service Data for the «Mesh Proxy Service» when Advertising with Private Node Identity is defined in [Table 7.14](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e_Table_7.14 "Table 7.14. Service Data for Mesh Proxy Service with Private Node Identity ") and illustrated in [Figure 7.7](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e_figure-idm453944259407843412103390773 "Figure 7.7. Advertising with Private Node Identity (Identification Type 0x03)").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Identification Type | 1 | 0x03 (Private Node Identity type) | M |
| Hash | 8 | Function of the included random number and identity information | M |
| Random | 8 | 64-bit random number | M |

Table 7.14. Service Data for Mesh Proxy Service with Private Node Identity

![Advertising with Private Node Identity (Identification Type 0x03)](image/1671b81d8ddd88.png)

Figure 7.7. Advertising with Private Node Identity (Identification Type 0x03)

The Hash field is calculated as shown below:

|  |
| --- |
| *Hash=e(IdentityKey, Padding || 0x03 || Random) mod 264* |

Where:

|  |  |
| --- | --- |
|  | Padding – 40 bits of padding, all bits set to 0  Random – 64-bit random value  Address – The unicast address of the node |

The Random field is the 64-bit random value used in the Hash field calculation.

The Random field shall be regenerated each time the server starts advertising with Private Node Identity. The Private Node Identity advertisements shall use a resolvable private address or a non-resolvable private address in the AdvA field of the advertising PDU. The address used for the AdvA field shall be regenerated
whenever the Random field is regenerated. The address used for the AdvA field shall be different for each subnet.

The creation of the encrypted node identity is illustrated in [Figure 7.8](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e_figure-idm4550635081988834121034998657 "Figure 7.8. Encrypted Private Node Identity creation").

![Encrypted Private Node Identity creation](image/1671b81d8e5965.png)

Figure 7.8. Encrypted Private Node Identity creation

###### 7.2.2.2.6. Proxy Privacy parameter for GATT Proxy bearer

When either the GATT Proxy state or the Node Identity state is enabled, the Proxy Privacy parameter (see [Section 6.5](index-en.html#UUID-3cca694e-cc9e-3673-d8fc-0003c638973a "6.5. Proxy Privacy parameter")) for the connection shall be Disabled.

When both the GATT Proxy state and the Node Identity state are disabled, and either the Private GATT Proxy state or the Private Node Identity state is enabled, the Proxy Privacy parameter (see [Section 6.5](index-en.html#UUID-3cca694e-cc9e-3673-d8fc-0003c638973a "6.5. Proxy Privacy parameter")) for the connection shall be Enabled.

###### 7.2.2.2.7. ATT_MTU

The server should support an ATT_MTU size equal to or larger than 33 octets to be able to pass the content of a full Proxy PDU (see [Section 6.5](index-en.html#UUID-3cca694e-cc9e-3673-d8fc-0003c638973a "6.5. Proxy Privacy parameter")).

#### 7.2.3. Mesh Proxy Service characteristics

The characteristics shown in [Table 7.15](index-en.html#UUID-fcb951d1-c80e-45c0-4e42-2a1897d8c188_Table_7.15 "Table 7.15. Mesh Proxy Service characteristics") are exposed by the server. Only one instance of each characteristic is permitted within this service. The
characteristic formats and UUIDs are defined in [[4](index-en.html#idp254746)].

Where a characteristic can be notified, a Client Characteristic Configuration descriptor shall be included in that characteristic as required by the Core Specification [[1](index-en.html#idp254740)].

| **Characteristic Name** | **Requirement** | **Mandatory  Properties** | **Optional  Properties** | **Security  Permissions** |
| --- | --- | --- | --- | --- |
| Mesh Proxy Data In | M | Write Without Response | None | Writeable with or without authentication or authorization when Proxy Service enabled |
| Mesh Proxy Data Out | M | Notify | None | Notifiable with or without authentication or authorization when Proxy Service enabled |

Table 7.15. Mesh Proxy Service characteristics

##### 7.2.3.1. Mesh Proxy Data In characteristic

The Mesh Proxy Data In characteristic is used by the client to send Proxy PDUs (see [Section 6.3](index-en.html#UUID-409dac4c-68c3-ce46-5b2d-11b164c45073 "6.3. Proxy PDU")) to the server.

The Mesh Proxy Data In characteristic is identified using the UUID «Mesh Proxy Data In», as defined in [[4](index-en.html#idp254746)]. The characteristic value has the same format as the Proxy PDU.

###### 7.2.3.1.1. Characteristic behavior

When the client sends a Proxy PDU to the server by executing a GATT Write Without Response procedure on this characteristic, the Attribute Value field of the ATT Write Command packet contains the Proxy PDU.

The Mesh Proxy Data In characteristic shall support Proxy PDU messages containing Network PDUs, mesh beacons, and proxy configuration messages and shall not support other Proxy PDU type messages.

##### 7.2.3.2. Mesh Proxy Data Out characteristic

The Mesh Proxy Data Out characteristic is used by the server to send Proxy PDUs to the client.

The Mesh Proxy Data Out characteristic is identified using the UUID «Mesh Proxy Data Out», as defined in [[4](index-en.html#idp254746)]. The characteristic value has the same format as the Proxy PDU.

The Mesh Proxy Data Out characteristic shall support Proxy PDU messages containing Network PDUs, mesh beacons, and proxy configuration messages and shall not support other Proxy PDU type messages.

###### 7.2.3.2.1. Characteristic behavior

As a bonding relationship is not required between the client and the server, the client will enable notifications (write value 0x0001) to the Mesh Proxy Data Out Client Characteristic Configuration Descriptor after a connection is established.

The server can send a Proxy PDU to the client by executing a GATT Notification procedure on this characteristic. The Attribute Value field of the ATT Handle Value Notification packet contains the Proxy PDU.

The Mesh Proxy Data Out characteristic shall support Proxy PDU message containing Network PDUs, mesh beacons, and proxy configuration messages and shall not support other Proxy PDU type messages.
