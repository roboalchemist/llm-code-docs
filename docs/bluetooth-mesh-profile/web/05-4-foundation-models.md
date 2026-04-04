# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 4. Foundation models

The foundation models define the access layer states, messages, and models required to configure and manage a mesh network.

### 4.1. Conventions

#### 4.1.1. Endianness

All multiple-octet numeric values in this layer shall be little-endian, as described in [Section 3.1.1.2](index-en.html#UUID-89646428-59af-fa05-5d7f-28ee9639d308 "3.1.1.2. Little-endian").

#### 4.1.2. Log field transformation

In order to compress two-octet values into one-octet fields, the following logarithmic transformation is used: any two-octet value is mapped onto a one-octet field value representing the largest integer n, where 2(n-1) is less than or equal to the two-octet value.

This transformation is represented in [Table 4.1](index-en.html#UUID-55e2dc8f-0d1c-e0f6-b98e-cee1963a10bc_Table_4.1 "Table 4.1. Log field values").

| Log Field Value | 2-octet Value |
| --- | --- |
| 0x01 | 0x0001 |
| 0x02 | 0x0002–0x0003 |
| 0x03 | 0x0004–0x0007 |
| 0x04 | 0x0008–0x000F |
| 0x05 | 0x0010–0x001F |
| 0x06 | 0x0020–0x003F |
| 0x07 | 0x0040–0x007F |
| 0x08 | 0x0080–0x00FF |
| 0x09 | 0x0100–0x01FF |
| 0x0A | 0x0200–0x03FF |
| 0x0B | 0x0400–0x07FF |
| 0x0C | 0x0800–0x0FFF |
| 0x0D | 0x1000–0x1FFF |
| 0x0E | 0x2000–0x3FFF |
| 0x0F | 0x4000–0x7FFF |
| 0x10 | 0x8000–0xFFFF |
| 0x11 | 0x10000 |

Table 4.1. Log field values

#### 4.1.3. Error handling

When a model processes an incoming message, the defined behavior may require the model to check one or more error conditions from a table of conditions (for example, see [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")). These error conditions shall be checked in order, from top to bottom, starting from the first row of the table. The model shall stop checking after encountering a failed condition. Or, after not encountering a failed condition, the model shall
stop checking after finishing the last row in the table.

### 4.2. State definitions

The state of a node is defined using one or more state definitions. This section defines states used throughout this specification.

State definitions that are not required as part of this specification are defined in the Mesh Model specification [[9](index-en.html#idp254760)] and follow the same format and architecture as mesh state definitions.

If a default value is defined for a state, it represents the value of the state of the node immediately after the node is provisioned.

#### 4.2.1. State instances for multiple subnets

If a node belongs to multiple subnets and supports a state that controls or provides information about a functionality of the node depending on the subnet, the node shall have an instance of the state for each subnet. Each state instance shall be referenced using the NetKey Index of the associated subnet.

#### 4.2.2. Composition Data

The Composition Data state contains information about a node, the elements it includes, and the supported models. The Composition Data is composed of a number of pages of information. All Composition Data Pages not defined in this specification are reserved for future use.

The Composition Data state can be accessed by the Configuration Server model and, if the Large Composition Data Server model is supported, by that model also.

If the node does not support the Large Composition Data Server model, the size of each page shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

##### 4.2.2.1. Composition Data Page 0

Composition Data Page 0 shall be present on a node. Composition Data Page 0 shall not change during a term of a node on the network.

The initial term of a node on the network shall start when the node is provisioned on the network.

A term shall end and a new term shall start when a Node Address Refresh procedure or a Node Composition Refresh procedure is successfully completed (see [Section 3.11.8](index-en.html#UUID-abe7a4a8-fdc0-ec16-10d6-db919df07d22 "3.11.8. Node Provisioning Protocol Interface procedures")).

The last term of a node on the network shall end when the node is removed from the network.

The format of Composition Data Page 0 is defined in [Table 4.2](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.2 "Table 4.2. Composition Data Page 0 fields").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| CID | 2 | Contains a 16-bit company identifier assigned by the Bluetooth SIG (the list is available at [[4](index-en.html#idp254746)]) that shall not change throughout the lifetime of the physical or software product | M |
| PID | 2 | Contains a 16-bit vendor-assigned product identifier that shall not change throughout the lifetime of the physical or software product | M |
| VID | 2 | Contains a 16-bit vendor-assigned product software version identifier that should be updated when the product's software is updated | M |
| CRPL | 2 | Contains a 16-bit value representing the minimum number of replay protection list entries in a device (see [Section 3.9.8](index-en.html#UUID-c39c2e5d-eba0-ea25-6edb-f88aa4bef4e5 "3.9.8. Message replay protection")) | M |
| Features | 2 | Contains a bit field indicating the device features, as defined in [Table 4.3](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.3 "Table 4.3. Features field format") | M |
| Elements | variable | Contains a sequence of element descriptions | M |

Table 4.2. Composition Data Page 0 fields

The Features field contains a bit field indicating the node capabilities as defined in [Section 3.2](index-en.html#UUID-fd0879f2-c9a9-797d-9717-abc5647ce33e "3.2. Features"). The format of the Features field is defined in [Table 4.3](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.3 "Table 4.3. Features field format").

| Bit | Feature | Description |
| --- | --- | --- |
| 0 | Relay | Relay feature support (see [Table 4.4](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.4 "Table 4.4. Features field bit values")) |
| 1 | Proxy | Proxy feature support (see [Table 4.4](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.4 "Table 4.4. Features field bit values")) |
| 2 | Friend | Friend feature support (see [Table 4.4](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.4 "Table 4.4. Features field bit values")) |
| 3 | Low Power | Low Power feature support (see [Table 4.4](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.4 "Table 4.4. Features field bit values")) |
| 4–15 | RFU | Reserved for Future Use |

Table 4.3. Features field format

Features field bits values are defined in [Table 4.4](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.4 "Table 4.4. Features field bit values").

| Bit Value | Description |
| --- | --- |
| 0 | The feature indicated by the bit is not supported |
| 1 | The feature indicated by the bit is supported |

Table 4.4. Features field bit values

The Elements field contains a sequence of one or more element descriptions. The format of each element description is defined in [Table 4.5](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.5 "Table 4.5. Element description format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Loc | 2 | Contains a location descriptor | M |
| NumS | 1 | Contains a count of SIG Model IDs in this element | M |
| NumV | 1 | Contains a count of Vendor Model IDs in this element | M |
| SIG Models | variable | Contains a sequence of NumS SIG Model IDs | M |
| Vendor Models | variable | Contains a sequence of NumV Vendor Model IDs | M |

Table 4.5. Element description format

The Loc field contains a location description as defined in the GATT Bluetooth Namespace Descriptors section of the Bluetooth SIG Assigned Numbers [[4](index-en.html#idp254746)]. Values not defined in the GATT Units table are Reserved for Future Use.

The SIG Models field contains a sequence of NumS SIG Model IDs. For each extended model included in this sequence, all models it extends shall also be included.

The Vendor Models field contains a sequence of NumV Vendor Model IDs.

![Composition Data Page 0 format](image/1671b81d77bdae.png)

Figure 4.1. Composition Data Page 0 format

The example in [Figure 4.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_figure-idm459151434552483409690981252 "Figure 4.1. Composition Data Page 0 format") shows a Composition Data Page 0 with two elements. Each element includes the location, the
number of SIG Model IDs, and the number of Vendor Model IDs. In this example, the first element has three SIG Model IDs and no Vendor Model IDs, and the second element has two SIG Model IDs and two Vendor Model IDs.

##### 4.2.2.2. Composition Data Page 1

Composition Data Page 1 shall be present on a node. Composition Data Page 1 contains information about the relationships among models. Each model either can be a root model or can extend other models (see [Section 2.3.6](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9 "2.3.6. Models")). Additionally, a model may have one or more corresponding models (see Section 6.4.3.1 in the Mesh Model Specification [[9](index-en.html#idp254760)]).

The format of Composition Data Page 1 is defined in [Table 4.6](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.6 "Table 4.6. Composition Data Page 1 format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Elements | variable | Contains a sequence of element descriptions | M |

Table 4.6. Composition Data Page 1 format

The Elements field contains a sequence of one or more element descriptions. The format of each element description is defined in [Table 4.7](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.7 "Table 4.7. Element field format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Number_S | 1 | Contains a count of SIG Models Items in this element | M |
| Number_V | 1 | Contains a count of Vendor Models in this element | M |
| SIG_Models_­Items | variable | Contains a sequence of Number_S SIG Model Items | M |
| Vendor_Models_­Items | variable | Contains a sequence of Number_V Vendor Model Items | M |

Table 4.7. Element field format

The Number_S field indicates the number of SIG Models in the element.

The Number_V field indicates the number of Vendor Models in the element.

The SIG_Models_Items field contains a sequence of Number_S of Model Items describing SIG Models in the element. The format of a Model Item is defined in [Table 4.8](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.8 "Table 4.8. Model Item field format").

The Vendor_Models_Items contains a sequence of Number_V of Model Items describing Vendor Models in the element. The format of a Model Item is defined in [Table 4.8](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.8 "Table 4.8. Model Item field format").

[Table 4.8](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.8 "Table 4.8. Model Item field format") defines the format of the Model Item.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Corresponding_Present | 1 | Corresponding_Group_ID field indicator | M |
| Format | 1 | Format of Extended_Model_Items indicator | M |
| Extended_Items_Count | 6 | Number of Extended Model Items in the Extended_Model_Items field | M |
| Corresponding_Group_ID | 8 | Corresponding group identifier | C.1 |
| Extended_Model_Items | variable | List of Extended Model Items | O |

Table 4.8. Model Item field format

C.1:
:   When the value of Corresponding_Present is 1, the Corresponding_Group_ID field shall be present; otherwise, the Corresponding_Group_ID field shall not be present.

The Corresponding_Present field indicates the presence of the Corresponding_Group_ID field.

The Format field shall indicate the format of each Extended Model Item in the Extended_Model_Items field. When the value of the Format field is 0, the format of the Extended Model Item is defined in [Table 4.9](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.9 "Table 4.9. Extended Model Item short format"). When the value of the Format field is 1, the format of the Extended Model Item is defined in [Table 4.11](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.11 "Table 4.11. Extended Model Item long format").

The Extended_Items_Count field shall indicate the number of Extended Model Items in the Extended_Model_Items field.

If present, the Corresponding_Group_ID field shall indicate the Corresponding Group ID of the model. All models from one group of corresponding Models shall share the same Corresponding Group ID. Each group of corresponding models shall have a unique Corresponding Group ID.

The Extended_Model_Items field shall contain the list of Extended Model Items. All Extended Model Items shall share the same format as defined by the Format field. Each Extended Model Item indicates a model that the Model Item is extending.

[Table 4.9](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.9 "Table 4.9. Extended Model Item short format") defines the Extended Model Item short format.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Element_Offset | 3 | Element address modifier, in the range -4 to 3 | M |
| Model_Item_Index | 5 | Model Index, in the range 0 to 31 | M |

Table 4.9. Extended Model Item short format

The Element_Offset field indicates the offset to the current element address, which identifies the element. The identified element shall be supported by the node. The value of the Element_Offset field is mapped to an integer value as defined in [Table 4.10](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.10 "Table 4.10. Mapping between values of the Element_Offset field and an integer value").

| Element_Offset | Represented Value |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | -4 |
| 5 | -3 |
| 6 | -2 |
| 7 | -1 |

Table 4.10. Mapping between values of the Element_Offset field and an integer value

The Model_Item_Index field shall indicate a model within an element indicated by the Element_Offset field. The index of a model shall be identified using the following rules:

* For a SIG Model, the index matches the index of the model in the SIG Models field of Composition Data Page 0 of the identified element,
* For a Vendor Model, the index is equal to the sum of the Number_S field value and an index of the model in the Vendor Models field of Composition Data Page 0 of the identified element.

[Table 4.11](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.11 "Table 4.11. Extended Model Item long format") defines the Extended Model Item long format.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Element_Offset | 8 | Element address modifier, in the range -128 to 127 | M |
| Model_Item_Index | 8 | Model index, in the range 0 to 255 | M |

Table 4.11. Extended Model Item long format

The Element_Offset field indicates the modifier to the current element address. The identified element shall be supported by the node. The format of the field is sint8.

The Model_Item_Index field indicates a model within an element indicated by the Element_Offset field. The Model_Item_Index field shall be computed using the same rules as for the Model_Item_Index field of the Extended Model Item short format.

###### 4.2.2.2.1. Example of Composition Data Page 1

[Table 4.12](index-en.html#UUID-4e1fc0d5-521d-ddf3-d45f-2b70018ff676_Table_4.12 "Table 4.12. Example of Composition Data Page 1 settings") summarizes the Composition Data Page 1 entries for an example node with the following element and model relationships.

* The node has two elements:

  * The first element contains SIG models A and B and vendor model V.
  * The second element contains SIG model C and vendor models X and Y.

* The models are ordered in Composition Data Page 0 as follows:

  * First element: models A, B, V
  * Second element: models C, X, Y

* Models A, C, and V are root models.
* Model B extends model A, and model X extends model V.
* Models B and C are corresponding models.
* Models X and Y are corresponding models.

Composition Page 1 for this configuration is presented in [Table 4.12](index-en.html#UUID-4e1fc0d5-521d-ddf3-d45f-2b70018ff676_Table_4.12 "Table 4.12. Example of Composition Data Page 1 settings").

| Elements | Index | Model | Model Item | Extended Model Item |
| --- | --- | --- | --- | --- |
| Number_S is 2  Number_V is 1 | 0 | A | Corresponding_Present is 0  Format is 0  Extended_Items_Count is 0 | – |
| 1 | B | Corresponding_Present is 1  Format is 0  Extended_Items_Count is 1  Corresponding_Group_ID is 0 | Item 0:  Element_Offset is 0 (Same   element)  Model_Item_Index is 0 (Model A) |
| 2 | V | Corresponding_Present is 0  Format is 0  Extended_Items_Count is 0 | – |
| Number_S is 1  Number_V is 2 | 0 | C | Corresponding_Present is 1  Format is 0  Extended_Items_Count is 0  Corresponding_Group_ID is 0 | – |
| 1 | X | Corresponding_Present is 1  Format is 0  Extended_Items_Count is 1  Corresponding_Group_ID is 1 | Item 0:  Element_Offset is -1 (First   element)  Model_Item_Index is 2 (Model V) |
| 2 | Y | Corresponding_Present is 1  Format is 0  Extended_Items_Count is 0  Corresponding_Group_ID is 1 | – |

Table 4.12. Example of Composition Data Page 1 settings

##### 4.2.2.3. Composition Data Page 2

Composition Data Page 2 shall be present on a node if the node supports one or more mesh profile specifications (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]). Composition Data Page 2 is used to indicate support for one or more mesh profile
specifications (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]).

The format of Composition Data Page 2 is defined in [Table 4.13](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa_Table_4.13 "Table 4.13. Composition Data Page 2 format").

| Field | Size  (octets) | Description |
| --- | --- | --- |
| Record_List | variable | Contains a list of records |

Table 4.13. Composition Data Page 2 format

The Record_List field contains a sequence of one or more entries, each indicating support for a specific mesh profile specification (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]). The format of each entry is defined in [Table 4.14](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa_Table_4.14 "Table 4.14. Record_List field format").

| Field | Size  (octets) | Description |
| --- | --- | --- |
| Mesh_Profile_Entry | variable | First entry |
| Mesh_Profile_Entry | variable | Second entry |
| … | … | … |
| Mesh_Profile_Entry | variable | Last entry |

Table 4.14. Record_List field format

The Mesh_Profile_Entry field format is defined in [Table 4.15](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa_Table_4.15 "Table 4.15. Mesh_Profile_Entry field format").

| Field | Size  (octets) | Description |
| --- | --- | --- |
| Mesh_Profile_Identifier | 2 | Mesh profile UUID identifying the supported mesh profile specification (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]) |
| Version | 3 | Version of the mesh profile specification (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]) |
| Num_Element_Offsets | 1 | Total number of element offsets in the Element_Offset_List field |
| Element_Offset_List | variable | List of element offsets containing models related to the supported mesh profile specification (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]) |
| Additional_Data_Len | 2 | Length of the additional data |
| Additional_Data | variable | Additional data specified in a mesh profile specification (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]) that is indicated by the Mesh_Profile_Identifier field |

Table 4.15. Mesh_Profile_Entry field format

The Version field format is defined in [Table 4.16](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa_Table_4.16 "Table 4.16. Version field format").

| Field | Size  (octets) | Description |
| --- | --- | --- |
| Version x | 1 | Specification major revision number |
| Version y | 1 | Specification minor revision number |
| Version z | 1 | Specification .Z revision number |

Table 4.16. Version field format

The Element_Offset_List field format is defined in [Table 4.17](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa_Table_4.17 "Table 4.17. Element_Offset_List field format").

| Field | Size  (octets) | Description |
| --- | --- | --- |
| Element_Offset | 1 | First element offset |
| Element_Offset | 1 | Second element offset |
| … | … | … |
| Element_Offset | 1 | Last element offset |

Table 4.17. Element_Offset_List field format

The Element_Offset field indicates a zero-based offset of the element, starting from the primary element, where models related to the supported mesh profile are present.

##### 4.2.2.4. Composition Data Page 128

Composition Data Page 128 is used to indicate the structure of elements, features, and models of a node in a new term (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")).

Composition Data Page 128 shall be present if the node supports the Remote Provisioning Server model.

The structure of Composition Data Page 128 is identical to the structure of Composition Data Page 0.

Composition Data Page 128 shall represent the contents that Composition Data Page 0 will contain in a new term.

##### 4.2.2.5. Composition Data Page 129

Composition Data Page 129 is used to indicate information about the relationships among models on a node in a new term (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")).

Composition Data Page 129 shall be present on a node if the node supports the Remote Provisioning Server model (see [Section 4.4.5](index-en.html#UUID-a5822f3c-d602-d597-e794-15189e9e3c83 "4.4.5. Remote Provisioning Server model")).

The structure of Composition Data Page 129 is identical to the structure of Composition Data Page 1.

Composition Data Page 129 shall represent the contents that Composition Data Page 2 (see [Section 4.2.2.3](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa "4.2.2.3. Composition Data Page 2")) will contain in a new term.

##### 4.2.2.6. Composition Data Page 130

Composition Data Page 130 is used to indicate support for one or more mesh profile specifications (see Section 3.12, Mesh Profiles, in [[4](index-en.html#idp254746)]) on a node in a new term (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")).

Composition Data Page 130 shall be present on a node if the node supports Composition Data Page 2 (see [Section 4.2.2.3](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa "4.2.2.3. Composition Data Page 2")) and the Remote Provisioning Server model (see [Section 4.4.5](index-en.html#UUID-a5822f3c-d602-d597-e794-15189e9e3c83 "4.4.5. Remote Provisioning Server model")).

The structure of Composition Data Page 130 is identical to the structure of Composition Data Page 2 (see [Section 4.2.2.3](index-en.html#UUID-be45f150-c6b5-1994-9aa1-360763d04faa "4.2.2.3. Composition Data Page 2")).

Composition Data Page 130 shall represent the contents that Composition Data Page 2 will contain in a new term.

#### 4.2.3. Model Publication

The Model Publication state is a composite state that controls parameters of messages that are published by a model. The Model Publication state includes the following states:

* Publish Address state
* Publish Period state
* Publish AppKey Index state
* Publish Friendship Credential Flag state
* Publish TTL state
* Publish Retransmit Count state
* Publish Retransmit Interval Steps state

Within an element, each model has a separate instance of Model Publication state. Models defined by higher layer specifications should use instances of the Model Publication state to control the publishing of messages.

##### 4.2.3.1. Publish Address

The Publish Address state determines the destination address in messages sent by a model. The publish address shall be the unassigned address, a unicast address, a Label UUID, or a group address.

When the publish address is set to the unassigned address, the publication of the model is disabled and the model does not originate any unsolicited messages.

##### 4.2.3.2. Publish Period

The Publish Period state determines the interval at which status messages are published by a model. This is a 1-octet value and consists of two fields: a 2-bit field representing the step resolution and a 6-bit field representing the number of steps. The format of this state is defined in [Table 4.18](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4_Table_4.18 "Table 4.18. Publish Period format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Number of Steps | 6 | The number of steps | M |
| Step Resolution | 2 | The resolution of the Number of Steps field | M |

Table 4.18. Publish Period format

|  |
| --- |
| Publish Period format |

Figure 4.2. Publish Period format

The Step Resolution field enumerates the resolution of the Number of Steps field and the values are defined in [Table 4.19](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4_Table_4.19 "Table 4.19. Step Resolution values").

| Value | Description |
| --- | --- |
| 0b00 | The Step Resolution is 100 milliseconds |
| 0b01 | The Step Resolution is 1 second |
| 0b10 | The Step Resolution is 10 seconds |
| 0b11 | The Step Resolution is 10 minutes |

Table 4.19. Step Resolution values

The Number of Steps field is a value representing the number of steps and the values are defined in [Table 4.20](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4_Table_4.20 "Table 4.20. Number of Steps values").

| Value | Description |
| --- | --- |
| 0x00 | Publish Period is disabled |
| 0x01–0x3F | The number of steps |

Table 4.20. Number of Steps values

The Publish Period is calculated using the formula:

|  |
| --- |
| *Publish Period=(Step Resolution)×(Number of Steps)* |

For example, if the Step Resolution is 0b10 and the Number of Steps is 0x31, then the Publish Period would be 490 seconds.

##### 4.2.3.3. Publish AppKey Index

The Publish AppKey Index state is the global AppKey Index of the application key used in messages sent by a model. The Publish AppKey Index shall be in the Model To AppKey List as defined in [Section 4.2.7](index-en.html#UUID-dc4739ad-10e2-2ffa-26b9-65891e5a673a "4.2.7. Model To AppKey List").

##### 4.2.3.4. Publish Friendship Credentials Flag

The Publish Friendship Credentials Flag state is a 1-bit state controlling the credentials used to publish messages from a model. The Publish Friendship Credentials Flag values are described in [Table 4.21](index-en.html#UUID-9f0b2d51-1d32-c1e4-fabd-62b4bfb48257_Table_4.21 "Table 4.21. Publish Friendship Credentials Flag values").

| Value | Description |
| --- | --- |
| 0 | Managed flooding security credentials or directed security credentials are used for publishing |
| 1 | Friendship security credentials are used for publishing |

Table 4.21. Publish Friendship Credentials Flag values

##### 4.2.3.5. Publish TTL

The Publish TTL state determines the TTL value for outgoing messages published by the model and the values are defined in [Table 4.22](index-en.html#UUID-bcd4eceb-9a71-bf4e-c238-27594178db23_Table_4.22 "Table 4.22. Publish TTL values"). Setting Publish TTL to 0xFF
will make the messages use the Default TTL as defined in [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL").

| Value | Description |
| --- | --- |
| 0x00–0x7F | The Publish TTL value, represented as a 1-octet integer |
| 0x80–0xFE | Prohibited |
| 0xFF | Use Default TTL |

Table 4.22. Publish TTL values

### Note

Note: If the Publish TTL state is set to 1, the outgoing messages are published to local elements only, as defined in [Section 3.4.5](index-en.html#UUID-47eec409-ad2d-8794-6b38-57b655e60ca1 "3.4.5. Network interfaces").

##### 4.2.3.6. Publish Retransmit Count

The Publish Retransmit Count state is a 3-bit value controlling the number of times that a message published by a model will be retransmitted. For example, a value of 0b000 represents no retransmissions, and a value of 0b111 represents 7 retransmissions.

##### 4.2.3.7. Publish Retransmit Interval Steps

The Publish Retransmit Interval Steps state is a 5-bit value controlling the interval between retransmissions of a message that is published by a model. The state represents the number of 50-millisecond steps that shall transpire before a message that was published by a model is retransmitted.

The retransmission interval is calculated using the following formula:

|  |
| --- |
| *retransmission interval=(Publish Retransmit Interval Steps+1)×50* |

For example, a value of 0b10000 represents an interval of 850 milliseconds.

#### 4.2.4. Subscription List

The Subscription List state is a list of group addresses and Label UUIDs.

The Subscription List is used by a model when receiving Access messages as defined in [Section 3.7.3.2](index-en.html#UUID-70753d2f-c513-176d-386a-e8912b8f9755 "3.7.3.2. Receiving an Access message"). It is highly recommended that models defined by higher layer
specifications use instances of the Subscription List state to control the receiving of messages.

Within an element, each model has a separate instance of a Subscription List, unless the model extends another model on that element. Instances of models that extend other models (i.e., all models within an extension relation tree) shall share a single instance of a Subscription List per element.

The size of the state shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

#### 4.2.5. NetKey List

The NetKey List state is an indexed list of NetKeys.

Each entry in the NetKey List holds up to two key values: the old key value and the new key value. The use of the old key and the new key values is described in the Key Refresh procedure (see Section [3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")).

The NetKey List shall contain a minimum of one NetKey.

The size of the state shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

#### 4.2.6. AppKey List

The AppKey List state is an indexed list of AppKeys.

Each entry in the AppKey List holds an AppKey Index and up to two key values: the old key value and the new key value. The use of the old key and the new key values is described in the Key Refresh procedure (see Section [3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")).

The AppKey List shall contain a minimum of one AppKey.

The size of the state shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

#### 4.2.7. Model To AppKey List

The Model To AppKey List state is a list of relationships between models and AppKeys. A model may be associated with one or more AppKeys.

The size of the state shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

#### 4.2.8. Default TTL

The Default TTL state determines the TTL value used when sending messages. The Default TTL is applied by the access layer or by the upper transport layer unless the application or functionality specifies a TTL. The Default TTL values are defined in [Table 4.23](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb_Table_4.23 "Table 4.23. Default TTL values").

| Value | Description |
| --- | --- |
| 0x00, 0x02–0x7F | The Default TTL state |
| 0x01, 0x80–0xFF | Prohibited |

Table 4.23. Default TTL values

#### 4.2.9. Relay

The Relay state indicates support for the Relay feature. If the Relay feature is supported, then this also indicates and controls whether the Relay feature is enabled or disabled. The values are defined in [Table 4.24](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b_Table_4.24 "Table 4.24. Relay values").

| Value | Description |
| --- | --- |
| 0x00 | The node support Relay feature that is disabled |
| 0x01 | The node supports Relay feature that is enabled |
| 0x02 | Relay feature is not supported |
| 0x03–0xFF | Prohibited |

Table 4.24. Relay values

If Relay feature is not supported, the Relay state value shall be 0x02 and not be changed.

If Relay feature is supported, the Relay state value 0x02 shall not be used.

#### 4.2.10. Attention Timer

The Attention Timer state determines if the Attention Timer state is on or off. This is generally intended to allow an element to attract human attention and, among others, is used during provisioning (see [Section 5.4.1.11](index-en.html#UUID-ae152830-6598-f0db-79ca-84aeaa7c11ed "5.4.1.11. Provisioning Record Request")).

An element may not support the Attention Timer. If an element does not support the Attention Timer, the Attention Timer state shall always be set to zero.

If the Attention Timer is non-zero for an element, Attention Timer state is on. If the Attention Timer is zero for an element, the Attention Timer state is off.

When the Attention Timer state is on, the value determines how long the element shall remain attracting human’s attention. The element does that by behaving in a human-recognizable way (e.g., a lamp flashes, a motor makes noise, an LED blinks). The exact behavior is implementation specific and depends on the type of device.
Normal behavior of the element is still active, although the method of identification may override the physical state of the device.

The Attention Timer is a momentary state, active for a time indicated by its value, in seconds. The value is decremented every second by 1 until it reaches zero. The values for this state are defined in [Table 4.25](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579_Table_4.25 "Table 4.25. Attention Timer values").

| Value | Description |
| --- | --- |
| 0x00 | Off |
| 0x01–0xFF | On, remaining time in seconds |

Table 4.25. Attention Timer values

#### 4.2.11. Secure Network Beacon

The Secure Network Beacon state determines if a node is periodically broadcasting Secure Network beacon messages (see [Section 3.10.3](index-en.html#UUID-684b7f2a-d17c-b4d2-80dc-8ddddb9f76ae "3.10.3. Secure Network beacon")). The values for this state are defined in
[Table 4.26](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336_Table_4.26 "Table 4.26. Secure Network Beacon values").

| Value | Description |
| --- | --- |
| 0x00 | The node is not broadcasting a Secure Network beacon |
| 0x01 | The node is broadcasting a Secure Network beacon |
| 0x02–0xFF | Prohibited |

Table 4.26. Secure Network Beacon values

#### 4.2.12. GATT Proxy

The GATT Proxy state indicates if the Proxy feature (see [Section 3.4.6.2](index-en.html#UUID-6dc6d66e-045f-96cb-8e8e-40b0c7de986a "3.4.6.2. Proxy feature")) is supported. If the feature is supported, the state indicates and controls the Proxy feature.

If the Proxy feature is disabled and the GATT server is advertising with Node Identity (see [Section 7.2.2.2.3](index-en.html#UUID-be413278-d730-695e-84aa-093f6faec350 "7.2.2.2.3. Advertising with Node Identity")), a GATT client device can connect over GATT to that node
for configuration and control. Messages from the GATT bearer are not relayed to the advertising bearer.

The values for this state are defined in [Table 4.27](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3_Table_4.27 "Table 4.27. GATT Proxy values").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disabled | The Proxy feature is supported and disabled |
| 0x01 | Enabled | The Proxy feature is supported and enabled |
| 0x02 | Not Supported | The Proxy feature is not supported |
| 0x03–0xFF | Prohibited | Prohibited |

Table 4.27. GATT Proxy values

If the Proxy feature is not supported, the GATT Proxy state value shall be Not Supported and shall not be changed.

If the Proxy feature is supported, the GATT Proxy state value Not Supported shall not be used.

#### 4.2.13. Node Identity

The Node Identity state indicates if the Node Identity functionality (see [Section 3.4.6.7](index-en.html#UUID-17a8996b-9dd3-4d56-3894-eb988df29bd3 "3.4.6.7. Node Identity functionality")) is supported. If the functionality is supported, the state indicates and controls
the Node Identity functionality.

The Node Identity state indicates and controls whether a node is advertising with Node Identity messages on a subnet (see [Section 7.2.2.2.3](index-en.html#UUID-be413278-d730-695e-84aa-093f6faec350 "7.2.2.2.3. Advertising with Node Identity")). The Node Identity state is
defined for each known subnet. If the Mesh Proxy Service is exposed, the node can be configured to advertise with Node Identity on a subnet (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). The
values for this state are defined in [Table 4.28](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97_Table_4.28 "Table 4.28. Node Identity values").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disabled | Advertising with Node Identity for a subnet is stopped |
| 0x01 | Enabled | Advertising with Node Identity for a subnet is running |
| 0x02 | Not Supported | Advertising with Node Identity is not supported |
| 0x03–0xFF | Prohibited | Prohibited |

Table 4.28. Node Identity values

If the Node Identity functionality is not supported, the value of the Node Identity state value shall be Not Supported and shall not be changed.

If the Node Identity functionality is supported, the value of the Node Identity state shall be either Disabled or Enabled.

If the Node Identity functionality is supported, then the default value of the Node Identity state shall be Disabled.

#### 4.2.14. Friend

The Friend state indicates support for the Friend feature. If Friend feature is supported, then this also indicates and controls whether Friend feature is enabled or disabled. The values for this state are defined in [Table 4.29](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec_Table_4.29 "Table 4.29. Friend values").

| Value | Description |
| --- | --- |
| 0x00 | The node supports Friend feature that is disabled |
| 0x01 | The node supports Friend feature that is enabled |
| 0x02 | The Friend feature is not supported |
| 0x03–0xFF | Prohibited |

Table 4.29. Friend values

If the Friend feature is not supported, the Friend state value shall be 0x02 and not be changed.

If the Friend feature is supported, the Friend state value 0x02 shall not be used.

If the Friend feature is supported and the Friend state changes to value 0x00 and if a node is a friend for one or more Low Power nodes, the node shall terminate all friend relationships and clear the associated Friend Queue.

#### 4.2.15. Key Refresh Phase

The Key Refresh Phase state indicates and controls the Key Refresh procedure (see [Section 3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")) for each NetKey in the NetKey List. The values for this state are defined in
[Table 4.30](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356_Table_4.30 "Table 4.30. Key Refresh Phase state values").

| Value | Description |
| --- | --- |
| 0x00 | Normal operation; Key Refresh procedure is not active |
| 0x01 | First phase of Key Refresh procedure |
| 0x02 | Second phase of Key Refresh procedure |
| 0x03–0xFF | Prohibited |

Table 4.30. Key Refresh Phase state values

[Table 4.31](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356_Table_4.31 "Table 4.31. Controllable Key Refresh transition values") defines all possible transitions of the Key Refresh Phase state that can be controlled using this state. All other transitions
are handled internally (e.g., the transition from 0x00 to 0x01 when a device receives a key update) by Key Refresh procedure.

| Old State | Transition | New State | Description |
| --- | --- | --- | --- |
| 0x00 | 0x03 | 0x00 | Transition 3 from Key Refresh Phase 0x00 does not cause any state change. |
| 0x01 | 0x02 | 0x02 | Transition 2 from Key Refresh Phase 0x01 moves to Key Refresh Phase 0x02 |
| 0x01 | 0x03 | 0x00 | Transition 3 from Key Refresh Phase 0x01 invokes Key Refresh Phase 3 and then moves to Key Refresh Phase 0x00. |
| 0x02 | 0x02 | 0x02 | Transition 2 from Key Refresh Phase 0x02 does not cause any state change. |
| 0x02 | 0x03 | 0x00 | Transition 3 from Key Refresh Phase 0x02 invokes Key Refresh Phase 3 and then moves to Key Refresh Phase 0x00. |

Table 4.31. Controllable Key Refresh transition values

#### 4.2.16. Health Fault

The Health Fault state is a composite state that represents a warning or an error condition of an element. The Health Fault state includes the following states:

* Current Fault state
* Registered Fault state

The Health Fault state is identified by Company ID and may be present in the node for more than one Company ID.

##### 4.2.16.1. Current Fault

The Current Fault state is a 1-octet value of the most recently performed self-test and an array containing a sequence of 1-octet values, each representing the current warning or error condition of an element. The format of this state is defined in [Table 4.32](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650_Table_4.32 "Table 4.32. Current Fault format").

| Field | Size | Description | Req. |
| --- | --- | --- | --- |
| Test ID | 1 | Identifier of a most recently performed self-test | M |
| FaultArray | N | Array of current faults | M |

Table 4.32. Current Fault format

Values for the Test ID are defined in [Table 4.33](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650_Table_4.33 "Table 4.33. Test ID values").

| Value | Description |
| --- | --- |
| 0x00 | Standard test |
| 0x01–0xFF | Vendor-specific test |

Table 4.33. Test ID values

The FaultArray values are Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

The FaultArray field of the Current Fault state is empty when no warning or error condition is present. The FaultArray reflects a real-time state. This means when a fault condition arises, a corresponding record is present in the FaultArray and when a fault condition is not present, the corresponding record is removed from the
FaultArray automatically.

A warning indicates the state of an element that is operating within the design limits but close to them.

An error indicates that the state of an element is outside the design limits and may not perform its functions.

##### 4.2.16.2. Registered Fault

The Registered Fault state is a 1-octet value of the most recently performed self-test and a shadow array of the FaultArray field of the Current Fault state. The format of the Registered Fault state is defined in [Table 4.34](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d_Table_4.34 "Table 4.34. Registered Fault format").

| Field | Size | Description | Req. |
| --- | --- | --- | --- |
| Test ID | 1 | Identifier of a most recently performed self-test | M |
| FaultArray | N | Array of registered faults | M |

Table 4.34. Registered Fault format

Values for the Test ID are defined in [Table 4.35](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d_Table_4.35 "Table 4.35. Test ID values").

| Value | Description |
| --- | --- |
| 0x00 | Standard test |
| 0x01–0xFF | Vendor-specific test |

Table 4.35. Test ID values

Whenever a fault condition has been present in the Current Fault state (see [Section 4.2.16.1](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650 "4.2.16.1. Current Fault")), the corresponding record is added to the FaultArray field of the Registered Fault state.
The FaultArray is cleared with a dedicated Health Fault Clear message (see [Section 4.3.3.3](index-en.html#UUID-d265de25-b6cf-4fc0-53ba-1e63f00e919f "4.3.3.3. Health Fault Clear Unacknowledged")).

#### 4.2.17. Health Fast Period Divisor

The Health Fast Period Divisor state is a 1-octet value that controls the increased cadence of publishing Health Current Status messages.

The value range for the Health Fast Period Divisor state is 0 through 15; all other values are Prohibited. The value is used to divide the Publish Period state of the Health Server model by 2n where n is the value of the Health Fast Period Divisor state.

#### 4.2.18. Heartbeat Publication

The Heartbeat Publication state is a composite state that controls sending of Heartbeat Transport Control messages. The Heartbeat Publication state includes the following states:

* Heartbeat Publication Destination state
* Heartbeat Publication Count state
* Heartbeat Publication Period Log state
* Heartbeat Publication TTL state
* Heartbeat Publication Features state
* Heartbeat Publication NetKey Index state

##### 4.2.18.1. Heartbeat Publication Destination

The Heartbeat Publication Destination state determines the destination address for Heartbeat messages. The Heartbeat Publication Destination shall be the unassigned address, a unicast address, or a group address, all other values are Prohibited.

### Note on Heartbeat Publication Destination

Note: If the Heartbeat Publication Destination is set to the unassigned address, the Heartbeat messages are not being sent.

##### 4.2.18.2. Heartbeat Publication Count

The Heartbeat Publication Count state is a 16-bit value that controls the number of periodical Heartbeat Transport Control messages to be sent. When set to 0xFFFF, it is not decremented after publication of a periodic Heartbeat message. When set to 0x0000, periodic Heartbeat messages are not published. When set to a value
greater than or equal to 0x0001 or less than or equal to 0xFFFE, it is decremented after publishing a periodic Heartbeat message. Publication of a triggered Heartbeat message does not affect the Heartbeat Publication Count state.

The Heartbeat Publication Count Log is a representation of the Heartbeat Publication Count state value. The Heartbeat Publication Count Log and Heartbeat Publication Count with the value 0x00 and 0x0000 are equivalent. The Heartbeat Publication Count Log value of 0xFF is equivalent to the Heartbeat Publication count value of
0xFFFF. The Heartbeat Publication Count Log value between 0x01 and 0x11 shall represent that smallest integer n where 2(n-1) is greater than or equal to the Heartbeat Publication Count value. For example, if the Heartbeat Publication Count value is 0x0579, then the Heartbeat Publication Count Log value would be
0x0C.

The values of the Heartbeat Publication Count Log are defined in [Table 4.36](index-en.html#UUID-5d8bca5b-84ee-a591-6c62-e409da0a03c1_Table_4.36 "Table 4.36. Heartbeat Publication Count Log values").

| Value | Description |
| --- | --- |
| 0x00 | Periodic Heartbeat messages are not published |
| 0x01–0x11 | Number of Heartbeat messages, 2(n-1), that remain to be sent |
| 0x12–0xFE | Prohibited |
| 0xFF | Periodic Heartbeat messages are published indefinitely |

Table 4.36. Heartbeat Publication Count Log values

##### 4.2.18.3. Heartbeat Publication Period Log

The Heartbeat Publication Period Log state is an 8-bit value that controls the period between the publication of two consecutive periodic Heartbeat Transport Control messages. The value is represented as 2(n-1) seconds. For example, the value 0x04 would have a publication period of 8 seconds, and the value 0x07
would have a publication period of 64 seconds. The values for this state are defined in [Table 4.37](index-en.html#UUID-c06973e0-b8ab-6b50-1cd1-a11015e5eaf1_Table_4.37 "Table 4.37. Heartbeat Publication Period Log values").

| Value | Description |
| --- | --- |
| 0x00 | Periodic Heartbeat messages are not published |
| 0x01–0x11 | Publication period represented as 2(n-1) seconds |
| 0x12–0xFF | Prohibited |

Table 4.37. Heartbeat Publication Period Log values

##### 4.2.18.4. Heartbeat Publication TTL

The Heartbeat Publication TTL state determines the TTL value used when sending Heartbeat messages. The values for this state are defined in [Table 4.38](index-en.html#UUID-55ab89ce-7da2-5b17-634d-ad3a930eb7b0_Table_4.38 "Table 4.38. Heartbeat Publication TTL values").

| Value | Description |
| --- | --- |
| 0x00–0x7F | The Heartbeat Publication TTL state |
| 0x80–0xFF | Prohibited |

Table 4.38. Heartbeat Publication TTL values

##### 4.2.18.5. Heartbeat Publication Features

The Heartbeat Publication Features state determines the features that trigger sending Heartbeat messages when changed. The values for this state are defined in [Table 4.39](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.39 "Table 4.39. Heartbeat Publication Feature values").

| Bit | Feature | Description |
| --- | --- | --- |
| 0 | Relay | Relay feature change trigger (see [Table 4.40](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.40 "Table 4.40. Heartbeat Publication Features state bit values")) |
| 1 | Proxy | Proxy feature change trigger (see [Table 4.40](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.40 "Table 4.40. Heartbeat Publication Features state bit values")) |
| 2 | Friend | Friend feature change trigger (see [Table 4.40](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.40 "Table 4.40. Heartbeat Publication Features state bit values")) |
| 3 | Low Power | Low Power feature change trigger (see [Table 4.40](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.40 "Table 4.40. Heartbeat Publication Features state bit values")) |
| 4–15 | RFU | Reserved for Future Use |

Table 4.39. Heartbeat Publication Feature values

Heartbeat Publication Features state bits values are defined in [Table 4.40](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf_Table_4.40 "Table 4.40. Heartbeat Publication Features state bit values").

| Bit Value | Description |
| --- | --- |
| 0 | The feature change indicated by the bit does not trigger a Heartbeat message |
| 1 | The feature change indicated by the bit triggers a Heartbeat message |

Table 4.40. Heartbeat Publication Features state bit values

##### 4.2.18.6. Heartbeat Publication NetKey Index

The Heartbeat Publication NetKey Index state determines the global NetKey Index of the NetKey used to send Heartbeat messages.

#### 4.2.19. Heartbeat Subscription

The Heartbeat Subscription state is a composite state that controls receiving of Heartbeat Transport Control messages. The Heartbeat Subscription state includes the following states:

* Heartbeat Subscription Source state
* Heartbeat Subscription Destination state
* Heartbeat Subscription Count state
* Heartbeat Subscription Period Log state
* Heartbeat Subscription Min Hops state
* Heartbeat Subscription Max Hops state

##### 4.2.19.1. Heartbeat Subscription Source

The Heartbeat Subscription Source state determines the source address for Heartbeat messages a node shall process. The Heartbeat Subscription Source shall be the unassigned address or a unicast address, all other values are Prohibited.

If the Heartbeat Subscription Source is set to the unassigned address, the Heartbeat messages are not being processed.

##### 4.2.19.2. Heartbeat Subscription Destination

The Heartbeat Subscription Destination state determines the destination address for Heartbeat messages. This can be used by nodes to configure a proxy filter to allow them to receive Heartbeat messages, for example, nodes connected using a GATT bearer or in a friendship. The Heartbeat Subscription Destination shall be the
unassigned address, the primary unicast address of the node, or a group address, all other values are Prohibited.

If the Heartbeat Subscription Destination is set to the unassigned address, the Heartbeat messages are not being processed.

##### 4.2.19.3. Heartbeat Subscription Count

The Heartbeat Subscription Count state is a 16-bit counter that controls the number of Heartbeat Transport Control messages received since receiving the most recent Config Heartbeat Subscription Set message. The counter stops counting at 0xFFFF. The values for this state are defined in [Table 4.41](index-en.html#UUID-d91f14d6-7e24-f2e8-9edb-01023b0580ea_Table_4.41 "Table 4.41. Heartbeat Subscription Count values").

The Heartbeat Subscription Count Log is a representation of the Heartbeat Subscription Count state value. The Heartbeat Subscription Count Log and Heartbeat Subscription Count with the value 0x00 and 0x0000 are equivalent. The Heartbeat Subscription Count Log value of 0xFF is equivalent to the Heartbeat Subscription count
value of 0xFFFF. The Heartbeat Subscription Count Log value between 0x01 and 0x10 shall represent the Heartbeat Subscription Count value, using the transformation defined in [Table 4.1](index-en.html#UUID-55e2dc8f-0d1c-e0f6-b98e-cee1963a10bc_Table_4.1 "Table 4.1. Log field values").

| Value | Description |
| --- | --- |
| 0x0000–0xFFFE | Number of Heartbeat messages received |
| 0xFFFF | More than 0xFFFE messages have been received |

Table 4.41. Heartbeat Subscription Count values

##### 4.2.19.4. Heartbeat Subscription Period

The Heartbeat Subscription Period state controls the duration for processing Heartbeat Transport Control messages. When set to 0x0000, Heartbeat messages are not processed. When set to a value greater than or equal to 0x0001, Heartbeat messages are processed.

The Heartbeat Subscription Period Log is a representation of the Heartbeat Subscription Period state value. The Heartbeat Subscription Period Log and Heartbeat Subscription Period with the value 0x00 and 0x0000 are equivalent. The Heartbeat Subscription Period Log value between 0x01 and 0x11 shall represent the Heartbeat
Subscription Period value, using the transformation defined in [Table 4.1](index-en.html#UUID-55e2dc8f-0d1c-e0f6-b98e-cee1963a10bc_Table_4.1 "Table 4.1. Log field values").

The values of Heartbeat Subscription Period Log are defined in [Table 4.42](index-en.html#UUID-ac2a794a-cec0-a399-4c1b-d844f78935c4_Table_4.42 "Table 4.42. Heartbeat Subscription Period Log values").

| Value | Description |
| --- | --- |
| 0x00 | Heartbeat messages are not processed |
| 0x01–0x11 | Remaining period in seconds for processing Heartbeat messages as defined in [Table 4.1](index-en.html#UUID-55e2dc8f-0d1c-e0f6-b98e-cee1963a10bc_Table_4.1 "Table 4.1. Log field values") |
| 0x12–0xFF | Prohibited |

Table 4.42. Heartbeat Subscription Period Log values

##### 4.2.19.5. Heartbeat Subscription Min Hops

The Heartbeat Subscription Min Hops state determines the minimum hops value registered when receiving Heartbeat messages since receiving the most recent Config Heartbeat Subscription Set message. The values for this state are defined in [Table 4.43](index-en.html#UUID-8e89c52c-df13-a8a8-9794-7f1b4a227cdf_Table_4.43 "Table 4.43. Heartbeat Subscription Min TTL values").

| Value | Description |
| --- | --- |
| 0x00–0x7F | The value of Heartbeat Subscription Min Hops state (see [Section 3.6.7.3](index-en.html#UUID-0d39f67c-dad6-d515-9695-d256ffab0b22 "3.6.7.3. Receiving Heartbeat messages")) |
| 0x80–0xFF | Prohibited |

Table 4.43. Heartbeat Subscription Min TTL values

##### 4.2.19.6. Heartbeat Subscription Max Hops

The Heartbeat Subscription Max Hops state determines the maximum hops value registered when receiving Heartbeat messages since receiving the most recent Config Heartbeat Subscription Set message. The values for this state are defined in [Table 4.44](index-en.html#UUID-c7735893-2088-d78a-f3d5-c1827aaef6c1_Table_4.44 "Table 4.44. Heartbeat Subscription Max TTL values").

| Value | Description |
| --- | --- |
| 0x00–0x7F | The value of Heartbeat Subscription Max Hops state (see [Section 3.6.7.3](index-en.html#UUID-0d39f67c-dad6-d515-9695-d256ffab0b22 "3.6.7.3. Receiving Heartbeat messages")) |
| 0x80–0xFF | Prohibited |

Table 4.44. Heartbeat Subscription Max TTL values

#### 4.2.20. Network Transmit

The Network Transmit state is a composite state that controls the number and timing of the transmissions of Network PDUs originating from a node. The Network Transmit state includes the following states:

* Network Transmit Count state
* Network Transmit Interval Steps state

A node contains a single instance of the Network Transmit state.

##### 4.2.20.1. Network Transmit Count

The Network Transmit Count state is a 3-bit value that controls the number of transmissions of Network PDUs that originate from the node. The number of transmissions of a Network PDU is Network Transmit Count + 1.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

##### 4.2.20.2. Network Transmit Interval Steps

The Network Transmit Interval Steps state is a 5-bit value representing the number of 10‑millisecond steps, which controls the interval between transmissions of Network PDUs originating from the node.

The transmission interval is calculated using the formula:

|  |
| --- |
| *transmission interval=(Network Transmit Interval Steps+1)×10* |

Each transmission should be perturbed by a random value from 0 milliseconds to 10 milliseconds between transmissions.

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

#### 4.2.21. Relay Retransmit

The Relay Retransmit state is a composite state that controls the number and timing of the retransmissions of the Network PDUs relayed by the node. The Relay Retransmit state includes the following states:

* Relay Retransmit Count
* Relay Retransmit Interval Steps

A node contains a single instance of the Relay Retransmit state.

##### 4.2.21.1. Relay Retransmit Count

The Relay Retransmit Count state is a 3-bit value that controls the number of retransmissions of Network PDUs relayed by the node. The Relay Retransmit Count + 1 is the number of times that a Network PDU is transmitted for each Network PDU that is relayed.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

##### 4.2.21.2. Relay Retransmit Interval Steps

The Relay Retransmit Interval Steps state is a 5-bit value representing the number of 10‑millisecond steps, which controls the interval between retransmissions of Network PDUs relayed by the node.

The transmission interval is calculated using the following formula:

|  |
| --- |
| *transmission interval=(Relay Retransmit Interval Steps+1)×10* |

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

#### 4.2.22. PollTimeout List

The PollTimeout List state is a list of current values of PollTimeout timer of the Low Power nodes within a Friend node.

For each Low Power node, the entry in the PollTimeout List holds the current value of the PollTimeout timer. If there are multiple friendship relationships set up on multiple subnets, the value held on the list is the minimum value of all PollTimeout timers for all friendship relationships the Friend Node has established with
the Low Power node.

The list is indexed by Low Power node primary element address.

| Value | Description |
| --- | --- |
| 0x000000 | The node is no longer a Friend node of the Low Power node identified by the LPNAddress |
| 0x000001–0x000009 | Prohibited |
| 0x00000A–0x34BBFF | The PollTimeout timer value in units of 100 milliseconds |
| 0x34BC00–0xFFFFFF | Prohibited |

Table 4.45. PollTimeout timer values

If the Friend feature is not supported or the Friend feature is supported and disabled, the current value of the PollTimeout List state for any Low Power node shall be set to 0x000000.

If the Friend feature is supported and enabled and the Friend node has not established friendship with the Low Power node identified by a primary element address, the current value of the PollTimeout List state for that Low Power node shall be set to 0x000000.

The size of the state shall not exceed the maximum useful Access message size ([Table 3.61](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9_Table_3.61 "Table 3.61. Maximum useful Access message sizes for various sizes of TransMIC")).

#### 4.2.23. Remote Provisioning Scan Capabilities

The Remote Provisioning Scan Capabilities state is a composite state that indicates various capabilities of scanning in the Remote Provisioning Server model. The state includes a Remote Provisioning Max Scanned Items state and a Remote Provisioning Active Scan state.

##### 4.2.23.1. Remote Provisioning Max Scanned Items

The Remote Provisioning Max Scanned Items state indicates the maximum number of UUIDs that the Remote Provisioning Server can report during scanning. [Table 4.46](index-en.html#UUID-bbd2744d-fa3f-2378-9bfd-018e95e72a07_Table_4.46 "Table 4.46. Remote Provisioning Max Scanned Items state values") defines the possible values. This state is read-only, and the state’s value is implementation-specific. The minimum value of the state is 4. The maximum value of the state is 255.

| Value | Description |
| --- | --- |
| 0x00–0x03 | Prohibited |
| 0x04–0xFF | Maximum number of unprovisioned devices that the Remote Provisioning Server can report |

Table 4.46. Remote Provisioning Max Scanned Items state values

##### 4.2.23.2. Remote Provisioning Active Scan

The Remote Provisioning Active Scan state indicates whether the Remote Provisioning Server supports active scanning (see [[2](index-en.html#idp254742)] Vol 6, Part B, Section 4.4.3.2). [Table 4.47](index-en.html#UUID-a71ea8da-1d69-a0c3-8d24-7ebd0d1f3a3e_Table_4.47 "Table 4.47. Remote Provisioning Active Scan state values") defines possible values of the state. This state is read-only, and the state’s value is implementation-specific.

| Value | Description |
| --- | --- |
| 0x00 | The Remote Provisioning Server does not support active scanning |
| 0x01 | The Remote Provisioning Server supports active scanning |
| 0x02–0xFF | Prohibited |

Table 4.47. Remote Provisioning Active Scan state values

#### 4.2.24. Remote Provisioning Scan Parameters

The Remote Provisioning Scan Parameters state is a composite state that indicates various parameters of scanning in the Remote Provisioning Server model. The state includes a Remote Provisioning Scan state, a Remote Provisioning Scan Items Limit state, and a Remote Provisioning Timeout state.

##### 4.2.24.1. Remote Provisioning Scan

The Remote Provisioning Scan state enumerates the values defined in [Table 4.48](index-en.html#UUID-ca4b8784-dd2f-4a97-be4a-f071bb1c0a1d_Table_4.48 "Table 4.48. Remote Provisioning Scan state values"), which describe the state of the Remote Provisioning Scan
procedure in the Remote Provisioning Server model (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")).

| Value | Description |
| --- | --- |
| 0x00 | Idle |
| 0x01 | Remote Provisioning Multiple Devices Scan (not limited to one device) |
| 0x02 | Remote Provisioning Single Device Scan (limited to one device) |
| 0x03–0xFF | Reserved for Future Use |

Table 4.48. Remote Provisioning Scan state values

##### 4.2.24.2. Remote Provisioning Scan Items Limit

The Remote Provisioning Scan Items Limit state identifies the maximum number of items the Remote Provisioning Server may report while performing the Remote Provisioning Scan procedure. [Table 4.49](index-en.html#UUID-4d9761e3-d2ae-5689-d269-31375e0a8491_Table_4.49 "Table 4.49. Remote Provisioning Scan Items Limit state values") defines the values of the Remote Provisioning Scan Items Limit state.

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01–0xFF | Maximum number of items to be reported |

Table 4.49. Remote Provisioning Scan Items Limit state values

##### 4.2.24.3. Remote Provisioning Timeout

The Remote Provisioning Timeout state indicates the maximum available time for the Remote Provisioning Scan procedure (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")). [Table 4.50](index-en.html#UUID-c687cf35-65e6-6a9e-4a9a-8a193cdf205e_Table_4.50 "Table 4.50. Remote Provisioning Timeout state values") defines the values for the Remote Provisioning Timeout state.

| Value | Description |
| --- | --- |
| 0x00 | The Remote Provisioning Scan procedure is not in progress. |
| 0x01–0xFF | The Remote Provisioning Scan procedure is in progress. The value indicates the maximum number of seconds remaining before the scan will stop. |

Table 4.50. Remote Provisioning Timeout state values

#### 4.2.25. Remote Provisioning Link Parameters

The Remote Provisioning Link Parameters state is a composite state that indicates various parameters of a provisioning link. This state includes a Remote Provisioning Link state, a Remote Provisioning Device UUID state, a Remote Provisioning Outbound PDU Count state, a Remote Provisioning Inbound PDU Count state, a Link Close
Reason state, and a Link Close Status state.

##### 4.2.25.1. Remote Provisioning Link

The Remote Provisioning Link state enumerates the values defined in [Table 4.51](index-en.html#UUID-1ae77eff-b468-ffc6-ac8f-4dac1d79b155_Table_4.51 "Table 4.51. Remote Provisioning Link state values"), which describe the state of the Remote Provisioning Server
model. During the execution of any of the Node Provisioning Protocol Interface procedures, the Link Opening, Outbound Packet Transfer, and Link Closing values are not used.

| Value | Description |
| --- | --- |
| 0x00 | Idle |
| 0x01 | Link Opening |
| 0x02 | Link Active |
| 0x03 | Outbound Packet Transfer |
| 0x04 | Link Closing |
| 0x05–0xFF | Prohibited |

Table 4.51. Remote Provisioning Link state values

##### 4.2.25.2. Remote Provisioning Device UUID

The Remote Provisioning Device UUID state indicates either the Device UUID that the provisioning bearer is open to, or, if any of the Node Provisioning Protocol Interface procedures is in progress, the Device UUID of the Remote Provisioning Server.

##### 4.2.25.3. Remote Provisioning Outbound PDU Count

The Remote Provisioning Outbound PDU Count state indicates the number of unique Provisioning PDUs delivered to the device being provisioned from the Remote Provisioning Server during the provisioning process, or during any Node Provisioning Protocol Interface procedure that is in progress.

##### 4.2.25.4. Remote Provisioning Inbound PDU Count

The Remote Provisioning Inbound PDU Count state indicates the number of unique Provisioning PDUs sent to the Remote Provisioning Client during the provisioning process, or during any of the Node Provisioning Protocol Interface procedures that is in progress.

##### 4.2.25.5. Link Close Reason

The Link Close Reason state contains the PB-ADV bearer link close Reason as defined in [Table 5.16](index-en.html#UUID-dabc5c31-cbb1-faea-391f-8b9413122bc6_Table_5.16 "Table 5.16. Reason field values"). For the bearers that do not define the link close reason, the
value of the state is not defined and the state is not used.

##### 4.2.25.6. Link Close Status

The Link Close Status state contains a status code that indicates the reason why the Remote Provisioning Server started the PB-Remote Close Link procedure (see [Section 5.2.3.3.2](index-en.html#UUID-1cbec5e7-8db0-095c-e7a0-c7ca2a7dc4b6 "5.2.3.3.2. PB-Remote Close Link procedure")).

#### 4.2.26. Directed Control

The Directed Control state is a composite state that controls the directed forwarding functionality for each subnet a node is member of (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). The
Directed Control state includes the Directed Forwarding, Directed Relay, Directed Proxy, Directed Proxy Use Directed Default, and Directed Friend states.

##### 4.2.26.1. Directed Forwarding

The Directed Forwarding state controls whether directed forwarding functionality is enabled or disabled for a subnet.

The values are defined in [Table 4.52](index-en.html#UUID-76e0b3d3-4024-6fea-16f8-4698690725d7_Table_4.52 "Table 4.52. Directed Forwarding state values").

| Value | Description |
| --- | --- |
| 0x00 | Directed forwarding functionality is disabled for a subnet |
| 0x01 | Directed forwarding functionality is enabled for a subnet |
| 0x02–0xFF | Prohibited |

Table 4.52. Directed Forwarding state values

The default value of the Directed Forwarding state is 0x00.

##### 4.2.26.2. Directed Relay

The Directed Relay state controls whether directed relay functionality is enabled or disabled for a subnet.

The state values are defined in [Table 4.53](index-en.html#UUID-539af574-8676-a61c-5e6f-b26f58c259d1_Table_4.53 "Table 4.53. Directed Relay state values").

| Value | Description |
| --- | --- |
| 0x00 | Directed relay functionality is disabled for a subnet |
| 0x01 | Directed relay functionality is enabled for a subnet |
| 0x02–0xFF | Prohibited |

Table 4.53. Directed Relay state values

The default value of the Directed Relay state is 0x00.

###### 4.2.26.2.1. Binding with Directed Forwarding state

When the Directed Forwarding state is set to 0x00 for a subnet, then Directed Relay state shall be set to 0x00 for the subnet.

##### 4.2.26.3. Directed Proxy

The Directed Proxy indicates the support for directed proxy functionality for a subnet. If directed proxy functionality is supported, then this state also indicates and controls whether directed proxy functionality is enabled or disabled for a subnet.

The state values are defined in [Table 4.54](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a_Table_4.54 "Table 4.54. Directed Proxy state values").

| Value | Description |
| --- | --- |
| 0x00 | Directed proxy functionality is disabled for a subnet |
| 0x01 | Directed proxy functionality is enabled for a subnet |
| 0x02 | Directed proxy functionality is not supported by the node |
| 0x03–0xFF | Prohibited |

Table 4.54. Directed Proxy state values

If directed proxy functionality is not supported by the node, the default value of the Directed Proxy state shall be 0x02 and shall not be changed.

If directed proxy functionality is supported by the node, the value of the Directed Proxy state for any subnet shall not be 0x02, and the default value of the Directed Proxy state shall be 0x00.

###### 4.2.26.3.1. Binding with Directed Forwarding state

When the Directed Forwarding state is set to 0x00 for a subnet, and directed proxy functionality is supported, then the Directed Proxy state for that subnet shall be set to 0x00 and shall not be changed.

###### 4.2.26.3.2. Binding with GATT Proxy state

When the GATT Proxy state is set to 0x00, and directed proxy functionality is supported, then the Directed Proxy state for all subnets shall be set to 0x00 and shall not be changed.

##### 4.2.26.4. Directed Proxy Use Directed Default

The Directed Proxy Use Directed Default state indicates and controls the default value of the Use_Directed parameter of the Directed Proxy Server (see [Section 6.7.1](index-en.html#UUID-10475ad4-589c-ed2b-b15f-a727a8093ebb "6.7.1. Directed Proxy Server behavior")) for
a subnet.

| Value | Description |
| --- | --- |
| 0x00 | Use_Directed is set to Disabled for a subnet when connection is created |
| 0x01 | Use_Directed is set to Enabled for a subnet when connection is created |
| 0x02 | Directed proxy functionality is not supported or is disabled for a subnet |
| 0x03–0xFF | Prohibited |

Table 4.55. Directed Proxy Use Directed Default state values

If directed proxy functionality is not supported by the node, the default value of the Directed Proxy Use Directed Default state shall be 0x02 and shall not be changed.

###### 4.2.26.4.1. Binding with Directed Proxy state

When the Directed Proxy state for a subnet is set to 0x00, the Directed Proxy Use Directed Default state for that subnet shall be set to 0x02 and shall not be changed.

##### 4.2.26.5. Directed Friend

The Directed Friend state indicates the support for directed friend functionality. If directed friend functionality is supported, then this state also indicates and controls whether directed friend functionality is enabled or disabled for a subnet.

The state values are defined in [Table 4.56](index-en.html#UUID-1a85383c-b86c-df9b-b4cc-889b0865e1fe_Table_4.56 "Table 4.56. Directed Friend state values").

| Value | Description |
| --- | --- |
| 0x00 | Directed friend functionality is disabled for a subnet |
| 0x01 | Directed friend functionality is enabled for a subnet |
| 0x02 | Directed friend functionality is not supported by the node |
| 0x03–0xFF | Prohibited |

Table 4.56. Directed Friend state values

If directed friend functionality is not supported by the node, the default value of the Directed Friend state shall be 0x02 and shall not be changed.

If directed friend functionality is supported by the node, the value of the Directed Friend state for any subnet shall not be 0x02, and the default value of the Directed Friend state shall be 0x00.

###### 4.2.26.5.1. Binding with Directed Forwarding state

When the Directed Forwarding state is set to 0x00 for a subnet, and directed friend functionality is supported, then the Directed Friend state shall be set to 0x00 for that subnet.

###### 4.2.26.5.2. Binding with Friend state

When the Friend state is set to 0x00, and directed friend functionality is supported, then the Directed Friend state for all subnets shall be set to 0x00 and shall not be changed.

#### 4.2.27. Path Metric

The Path Metric state is a composite state that controls the type of path metric to be used to evaluate the quality of a non-fixed path in a subnet and the lifetime of non-fixed paths established in the subnet (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). It includes the Path Metric Type state and the Path Lifetime state.

##### 4.2.27.1. Path Metric Type

The Path Metric Type state is a 3-bit value that represents the type of path metric to be used to evaluate the quality of a non-fixed path in a subnet and to rank the path accordingly when the node selects a path toward a given destination.

The values of the Path Metric Type state are defined in [Table 4.57](index-en.html#UUID-1219fa02-97bf-c8c9-848a-9fc17f223db1_Table_4.57 "Table 4.57. Path Metric Type state values").

| Value | Name | Description |
| --- | --- | --- |
| 0b000 | Node Count | The node uses the Node Count metric |
| 0b001–0b111 | RFU | Reserved for Future Use |

Table 4.57. Path Metric Type state values

The default value of the Path Metric Type state is Node Count.

The Node Count metric counts the number of hops between a Path Origin and a Path Target. If a node is traversed by multiple lanes of the path, the Node Count is incremented by the Lane_Counter value of the Forwarding Table entry.

During the Directed Forwarding Discovery procedure (see [Section 3.6.8.2.2](index-en.html#UUID-4efd3de6-9259-d010-8b47-87e534b7b4c0 "3.6.8.2.2. Directed Forwarding Discovery")), a Path_Origin_Path_Metric value is calculated based on the current Path_Origin_Path_Metric
value stored in the Discovery Table.

If a Forwarding Table entry corresponding to the received PATH_REQUEST message exists (see [Section 3.6.8.5.2](index-en.html#UUID-320ffb1c-0e22-f0e7-3c56-e1d202447215 "3.6.8.5.2. PATH_REQUEST message received")) with the same forwarding number, the
Path_Origin_Path_Metric value shall be calculated as follows:

|  |
| --- |
| *new Path_Origin_Path_Metric=current Path_Origin_Path_Metric + 1 + Lane_Counter* |

Otherwise, the Path_Origin_Path_Metric value shall be calculated as follows:

|  |
| --- |
| *new Path_Origin_Path_Metric=current Path_Origin_Path_Metric + 1* |

The new Path_Origin_Path_Metric value is transmitted in the PATH_REQUEST message sent by a Directed Relay node.

##### 4.2.27.2. Path Lifetime

The Path Lifetime state is a 2-bit value that determines how long a non-fixed path originated by the node is valid. While a non-fixed path is valid, the path information is stored in a non-fixed path entry in the Forwarding Table state of the subnet. When this time elapses, the path entry is deleted from the Forwarding Table
state.

The values of the Path Lifetime state are defined in [Table 4.58](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a_Table_4.58 "Table 4.58. Path Lifetime state values").

| Value | Description |
| --- | --- |
| 0b00 | Path lifetime is 12 minutes. |
| 0b01 | Path lifetime is 2 hours. |
| 0b10 | Path lifetime is 24 hours. |
| 0b11 | Path lifetime is 10 days. |

Table 4.58. Path Lifetime state values

The default value of the Path Lifetime state is 0b10.

#### 4.2.28. Discovery Table Capabilities

The Discovery Table Capabilities state is a composite state that indicates the maximum number of Discovery Table entries and controls the maximum number of Directed Forwarding Initialization procedures on a node in a given subnet (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). It includes the Max Discovery Table Entries Count state and the Max Concurrent Init state.

##### 4.2.28.1. Max Discovery Table Entries Count

The Max Discovery Table Entries Count state is a 1-octet value that indicates the maximum number of Discovery Table entries supported by the node in a given subnet. The node shall support at least two Discovery Table entries in a given subnet.

##### 4.2.28.2. Max Concurrent Init

The Max Concurrent Init state is a 1-octet value that determines the maximum number of concurrent Directed Forwarding Initialization procedures in a node in a given subnet. 0x00 is a prohibited value for this state.

The value of the Max Concurrent Init state shall be at most the value of the Max Discovery Table Entries Count state.

The default value of the Max Concurrent Init state is 0x02, which allows at most two concurrent Directed Forwarding Initialization procedures.

#### 4.2.29. Forwarding Table

The Forwarding Table state is a composite state that controls the transmission of Network PDUs by a Directed Forwarding node. Each node contains a Forwarding Table state for each subnet to which the node belongs (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). The Forwarding Table state includes the Forwarding Table Update Identifier state and the Forwarding Table Entries state.

##### 4.2.29.1. Forwarding Table Update Identifier

The Forwarding Table Update Identifier state is a 16-bit value that changes after each change to the Forwarding Table Entries state (see [Section 4.2.29.2](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee "4.2.29.2. Forwarding Table Entries")). The Forwarding
Table Update Identifier state is initialized to 0.

##### 4.2.29.2. Forwarding Table Entries

The Forwarding Table Entries state is a list of entries for all paths that contain the node in a given subnet.

Each Forwarding Table entry shall have the format defined in [Table 4.59](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee_Table_4.59 "Table 4.59. Forwarding Table entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Fixed_Path | 1 | Flag indicating whether or not the path is a fixed path | M |
| Backward_Path_Validated | 1 | Flag indicating whether or not the backward path has been validated | M |
| Path_Not_Ready | 1 | Flag indicating whether or not the path is ready for use. | M |
| RFU | 5 | Reserved for Future Use | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Path_Origin_Secondary_  Elements_Count | 8 | Number of secondary element addresses of the Path Origin | M |
| Dependent_Origin_List | variable  (16 * N1) | List of primary element addresses of dependent nodes of the Path Origin. Each list entry has a corresponding Dependent_Origin_Secondary_Elements_Count_List entry. | M |
| Dependent_Origin_  Secondary_Elements_  Count_List | variable  (8 * N1) | List of numbers of secondary elements of dependent nodes of the Path Origin. Each list entry has a corresponding Dependent_Origin_List entry. | M |
| Destination | 16 | Primary element address of the Path Target, or the group address or the virtual address to which the Path Target is subscribed | M |
| Path_Target_Secondary_  Elements_Count | 8 | Number of secondary elements of the Path Target | M |
| Dependent_Target_List | variable  (16 * N2) | List of primary element addresses of dependent nodes of the Path Target. Each list entry has a corresponding Dependent_Target_Secondary_Elements_Count_List entry. | M |
| Dependent_Target_  Secondary_Elements_  Count_List | variable  (8 * N2) | List of numbers of secondary elements of dependent nodes of the Path Target. Each list entry has a corresponding Dependent_Target_List entry. | M |
| Forwarding_Number | 8 | Forwarding number of the Path Origin; if the entry is associated with a fixed path, the value is 0. | M |
| Lane_Counter | 8 | Number of lanes discovered; if the entry is associated with a fixed path, the value is 1. | M |
| Bearer_Toward_Path_Origin | 16 | If the node is not the Path Origin, the bearer index to be used for forwarding messages directed to the Path Origin; otherwise, the unassigned bearer index. | M |
| Bearer_Toward_Path_Target | 16 | If the node is not the Path Target, the bearer index to be used for forwarding messages directed to the Path Target; otherwise, the unassigned bearer index. | M |

Table 4.59. Forwarding Table entry format

In the Size entries in [Table 4.59](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee_Table_4.59 "Table 4.59. Forwarding Table entry format"), N1 is the number of list entries in the Dependent_Origin_List, and N2 is the number of entries in the
Dependent_Target_List.

The values of the Fixed_Path field are defined in [Table 4.60](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee_Table_4.60 "Table 4.60. Forwarding Table Fixed_Path field values").

| Value | Description |
| --- | --- |
| 0b0 | The path is a non-fixed path. |
| 0b1 | The path is a fixed path. |

Table 4.60. Forwarding Table Fixed_Path field values

The values of the Backward_Path_Validated field are defined in [Table 4.61](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee_Table_4.61 "Table 4.61. Forwarding Table Backward_Path_Validated field values").

| Value | Description |
| --- | --- |
| 0b0 | The backward path has not been validated, i.e., the node has not received a PATH_CONFIRMATION message for the path. |
| 0b1 | The backward path has been validated, i.e., the node has received a PATH_CONFIRMATION message for the path. |

Table 4.61. Forwarding Table Backward_Path_Validated field values

The values of the Path_Not_Ready field are defined in [Table 4.62](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee_Table_4.62 "Table 4.62. Forwarding Table Path_Not_Ready field values").

| Value | Description |
| --- | --- |
| 0b0 | The path is ready for use |
| 0b1 | The path is not ready for use |

Table 4.62. Forwarding Table Path_Not_Ready field values

The Forwarding Table Entries state is empty by default.

#### 4.2.30. Wanted Lanes

The Wanted Lanes state is a 1-octet value that determines the number of lanes to be discovered for each path in a subnet (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")). 0x00 is a prohibited
value for this state.

The default value for the Wanted Lanes state is 0x01.

#### 4.2.31. Two Way Path

The Two Way Path state is a 1-bit value that determines whether a node that is the Path Target in a subnet considers the paths as one-way or two-way paths (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

If the state value is 0b0, each path is considered one-way and shall be used to forward messages only from the Path Origin to the Path Target.

If the state value is 0b1, each path is considered two-way and shall be used to forward messages from the Path Origin to the Path Target and from the Path Target to the Path Origin.

The default value of the Two Way Path state is 0b1.

#### 4.2.32. Path Echo Interval

The Path Echo Interval state is a composite state consisting of the Unicast Echo Interval state and the Multicast Echo Interval state.

##### 4.2.32.1. Unicast Echo Interval

The Unicast Echo Interval state is a 1-octet value that determines the minimum interval that a Path Origin waits after it discovers a path towards a unicast address before executing a Directed Forwarding Echo procedure to validate the same path; the state also determines the minimum interval between two Directed Forwarding
Echo procedures executed for the same path.

The values of the Unicast Echo Interval state are defined in [Table 4.63](index-en.html#UUID-3e7efc9b-b39c-03a4-b396-10d29e418623_Table_4.63 "Table 4.63. Unicast Echo Interval state values").

| Value | Description |
| --- | --- |
| 0x00 | The Directed Forwarding Echo procedure is not executed for a destination that is a unicast address. |
| 0x01−0x63 | Interval expressed as percentage of the time corresponding to the Path Lifetime state (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")). |
| 0x64−0xFF | Prohibited |

Table 4.63. Unicast Echo Interval state values

When the Directed Forwarding Echo procedure is executed towards a unicast address, the validation interval is calculated using the following formula:

|  |
| --- |
| *validation interval=(path lifetime)×(Unicast Echo Interval)÷100* |

The default value of the Unicast Echo Interval state is 0x00.

##### 4.2.32.2. Multicast Echo Interval

The Multicast Echo Interval state is a 1-octet value that determines the minimum interval that a Path Origin waits after it discovers a path towards a group address or a virtual address before executing a Directed Forwarding Echo procedure to validate the same path; the state also determines the minimum interval between two
Directed Forwarding Echo procedures executed for the same path.

The values of the Multicast Echo Interval state are defined in [Table 4.64](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c_Table_4.64 "Table 4.64. Multicast Echo Interval state values").

| Value | Description |
| --- | --- |
| 0x00 | The Directed Forwarding Echo procedure is not executed for a destination that is a group address or a virtual address. |
| 0x01–0x63 | Interval expressed as percentage of the time corresponding to the Path Lifetime state (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")). |
| 0x64–0xFF | Prohibited |

Table 4.64. Multicast Echo Interval state values

When the Directed Forwarding Echo procedure is executed towards a group address or a virtual address, the validation interval is calculated using the following formula:

|  |
| --- |
| *validation interval=(path lifetime)×(Multicast Echo Interval)÷100* |

The default value of the Multicast Echo Interval state is 0x00.

#### 4.2.33. Directed Network Transmit

The Directed Network Transmit state is a composite state that controls the number and timing of the transmissions of Network PDUs with CTL equal to 0 that originates from either a Path Origin or a Path Target and that are secured using directed security material.

The Directed Network Transmit state includes the Directed Network Transmit Count state and the Directed Network Transmit Interval Steps state.

##### 4.2.33.1. Directed Network Transmit Count

The Directed Network Transmit Count state is a 3-bit value that controls the number of transmissions of Network PDUs with CTL equal to 0 that originate from either a Path Origin or a Path Target and that are secured using directed security material. The number of transmissions of a Network PDU is Directed Network Transmit
Count + 1.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

The default value of the Directed Network Transmit Count state is 0b001 (2 transmissions).

##### 4.2.33.2. Directed Network Transmit Interval Steps

The Directed Network Transmit Interval Steps state is a 5-bit value representing the number of 10-millisecond steps, which controls the interval between transmissions of Network PDUs with CTL equal to 0 that originates from either a Path Origin or a Path Target and that are secured using directed security material.

The transmission interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *transmission interval=(Directed Network Transmit Interval Steps+1)×10* |

Each transmission should be perturbed by a random value from 0 milliseconds to 10 milliseconds between transmissions.

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

The default value of the Directed Network Transmit Interval Steps state is 0b01001 (i.e., 100 milliseconds).

#### 4.2.34. Directed Relay Retransmit

The Directed Relay Retransmit state is a composite state that controls the number and timing of the retransmissions of Network PDUs with CTL equal to 0 relayed by a Directed Relay node and secured with directed security material.

The Directed Relay Retransmit state includes the Directed Relay Retransmit Count state and the Directed Relay Retransmit Interval Steps state.

##### 4.2.34.1. Directed Relay Retransmit Count

The Directed Relay Retransmit Count state is a 3-bit value that controls the number of retransmissions of Network PDUs with CTL equal to 0 relayed by a Directed Relay node and secured with directed security material. The Directed Relay Retransmit Count + 1 is the number of times that a Network PDU is transmitted for each
Network PDU that is relayed.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

The default value of the Directed Relay Retransmit Count state is 0b010 (3 transmissions).

##### 4.2.34.2. Directed Relay Retransmit Interval Steps

The Directed Relay Retransmit Interval Steps state is a 5-bit value representing the number of 10-millisecond steps, which controls the interval between retransmissions of Network PDUs with CTL equal to 0 relayed by a Directed Relay node and secured with directed security material.

The transmission interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *transmission interval=(Directed Relay Retransmit Interval Steps+1)×10* |

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

The default value of the Directed Relay Retransmit Interval Steps state is 0b01001 (i.e., 100 milliseconds)

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

#### 4.2.35. RSSI Threshold

The RSSI Threshold state is a composite state that determines the default RSSI threshold and controls the margin above the RSSI threshold that the Directed Forwarding Discovery procedure uses to filter out weak radio links.

The RSSI Threshold state includes the Default RSSI Threshold state and the RSSI Margin state.

##### 4.2.35.1. Default RSSI Threshold

The Default RSSI Threshold state is a 1-octet signed integer in the range -128 to 127 representing the default RSSI threshold in dBm. The value is implementation specific and should be 10 dB above the receiver sensitivity.

##### 4.2.35.2. RSSI Margin

The RSSI Margin state is a 1-octet value representing the margin (in dB) above the default RSSI threshold for which the link quality with a neighbor node is considered acceptable.

The values of the RSSI Margin state are defined in [Table 4.65](index-en.html#UUID-c30bb5db-a914-901c-6609-c60e528972bd_Table_4.65 "Table 4.65. RSSI Margin state values").

| Value | Description |
| --- | --- |
| 0x00−0x32 | Margin above the default RSSI threshold, in dB |
| 0x33−0xFF | Prohibited |

Table 4.65. RSSI Margin state values

The default value for the RSSI Margin state is 0x14.

#### 4.2.36. Directed Paths

The Directed Paths state is a composite state that indicates the minimum number of paths of each path type that the node supports.

The state includes the Directed Node Paths, Directed Relay Paths, Directed Proxy Paths, and Directed Friend Paths states.

##### 4.2.36.1. Directed Node Paths

The Directed Node Paths state is a 2-octet integer that indicates the minimum number of paths that the node supports when acting as a Path Origin or as a Path Target. The value of the Directed Node Paths state shall be equal to or greater than 20.

##### 4.2.36.2. Directed Relay Paths

The Directed Relay Paths state is a 2-octet integer that indicates the minimum number of paths that the node supports when acting as an intermediate Directed Relay node. The value of the Directed Relay Paths state shall be equal to or greater than 20.

##### 4.2.36.3. Directed Proxy Paths

If the node supports directed proxy functionality (see [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality")), the Directed Proxy Paths state is a 2-octet integer that indicates the minimum number of paths that
the node supports when acting as a Directed Proxy node. If directed proxy functionality is supported, the value of the Directed Proxy Paths state shall be equal to or greater than 20; otherwise, the Directed Proxy Paths state shall be 0.

##### 4.2.36.4. Directed Friend Paths

If the node supports directed friend functionality (see [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality")), the Directed Friend Paths state is a 2-octet integer that indicates the minimum number of paths that
the node supports when acting as a Directed Friend node. If directed friend functionality is supported, the value of the Directed Friend Paths state shall be equal to or greater than 20; otherwise, the Directed Friend Paths state shall be 0.

#### 4.2.37. Directed Publish Policy

The Directed Publish Policy state is a 1-octet value that determines whether a model uses managed flooding or directed forwarding when publishing.

The values of the Directed Publish Policy state are defined in [Table 4.66](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea_Table_4.66 "Table 4.66. Directed Publish Policy state values").

| Value | Policy Name | Description |
| --- | --- | --- |
| 0x00 | Managed Flooding | The policy is to use managed flooding when publishing. |
| 0x01 | Directed Forwarding | The policy is to use directed forwarding when publishing. |
| 0x02−0xFF | RFU | Reserved for Future Use |

Table 4.66. Directed Publish Policy state values

The default value of the Directed Publish Policy state is 0x00.

#### 4.2.38. Path Discovery Timing Control

The Path Discovery Timing Control state is a composite state that controls the timing of the Directed Forwarding Initialization procedure.

The Path Discovery Timing Control state includes a Path Monitoring Interval state, a Path Discovery Retry Interval state, a Path Discovery Interval state, and a Lane Discovery Guard Interval state.

##### 4.2.38.1. Path Monitoring Interval

The Path Monitoring Interval state is a 2-octet unsigned value that controls the time interval (in seconds) during which the node collects information to determine whether or not to execute a Directed Forwarding Initialization procedure for a destination before a path to that destination expires. This state is used by the Path
Origin State Machine for the destination (see [Section 4.4.7.2](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc "4.4.7.2. Path Origin State Machine")).

The default value of the Path Monitoring Interval state is 120 seconds.

##### 4.2.38.2. Path Discovery Retry Interval

The Path Discovery Retry Interval state is a 2-octet unsigned value that controls the time interval (in seconds) after a Directed Forwarding Initialization procedure fails before starting a new Directed Forwarding Initialization procedure for the same destination. This state is used by the Path Origin State Machine for the
destination (see [Section 4.4.7.2](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc "4.4.7.2. Path Origin State Machine")).

The default value of the Path Discovery Retry Interval state is 300 seconds.

The Configuration Manager should set the value of the Path Discovery Retry Interval to be at least the value of the Lane Discovery Guard Interval. If the Path Discovery Retry Interval is less than the Lane Discovery Guard Interval, some nodes might not participate in the subsequent Directed Forwarding Discovery procedure
because of Discovery Table entries that have not expired.

##### 4.2.38.3. Path Discovery Interval

The Path Discovery Interval state is a 1-bit value that represents the initial value of the Path Discovery timer.

The values of the Path Discovery Interval state are defined in [Table 4.67](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf_Table_4.67 "Table 4.67. Path Discovery Interval state values").

| Value | Description |
| --- | --- |
| 0b0 | Path discovery interval is 5 seconds |
| 0b1 | Path discovery interval is 30 seconds |

Table 4.67. Path Discovery Interval state values

The default value of the Path Discovery Interval state is 0b1.

##### 4.2.38.4. Lane Discovery Guard Interval

The Lane Discovery Guard Interval state is a 1-bit value that represents the interval between the Path Discovery timer expiry and sending a PATH_REQUEST for a new lane discovery for the same path.

The values of the Lane Discovery Guard Interval state are defined in [Table 4.68](index-en.html#UUID-11e4dd23-ac53-7cb3-8ee3-d8ae38fda848_Table_4.68 "Table 4.68. Lane Discovery Guard Interval state values").

| Value | Description |
| --- | --- |
| 0b0 | Lane discovery guard interval is 2 seconds |
| 0b1 | Lane discovery guard interval is 10 seconds |

Table 4.68. Lane Discovery Guard Interval state values

The default value of the Lane Discovery Guard Interval state is 0b1.

#### 4.2.39. Directed Control Network Transmit

The Directed Control Network Transmit state is a composite state that controls the number and timing of the transmissions of Network PDUs with CTL field equal to 1 that originate from either a Path Origin or a Path Target and that are secured using directed security material.

The Directed Control Network Transmit state includes the Directed Control Network Transmit Count state and the Directed Control Network Transmit Interval Steps state.

##### 4.2.39.1. Directed Control Network Transmit Count

The Directed Control Network Transmit Count state is a 3-bit value that controls the number of transmissions of Network PDUs with CTL field equal to 1 that originate from either a Path Origin or a Path Target and that are secured with directed security material. The number of transmissions of a Network PDU is Directed Control
Network Transmit Count + 1.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

The default value of the Directed Control Network Transmit Count state is 0b001 (2 transmissions).

##### 4.2.39.2. Directed Control Network Transmit Interval Steps

The Directed Control Network Transmit Interval Steps state is a 5-bit value representing the number of 10-millisecond steps, which controls the interval between transmissions of Network PDUs with CTL field equal to 1 that originate from either a Path Origin or a Path Target and that are secured with directed security
material.

The transmission interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *transmission interval=(Directed Control Network Transmit Interval Steps+1)×10* |

Each transmission should be perturbed by a random value from 0 milliseconds to 10 milliseconds between transmissions.

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

The default value of the Directed Control Network Transmit Interval Steps state is 0b01001 (i.e., 100 milliseconds).

#### 4.2.40. Directed Control Relay Retransmit

The Directed Control Relay Retransmit state is a composite state that controls the number and timing of the retransmissions of Network PDUs with CTL field equal to 1 relayed by a Directed Relay node and secured with directed security material.

The Directed Control Relay Retransmit state includes the Directed Control Relay Retransmit Count state and the Directed Control Relay Retransmit Interval Steps state.

##### 4.2.40.1. Directed Control Relay Retransmit Count

The Directed Control Relay Retransmit Count state is a 3-bit value that controls the number of retransmissions of Network PDUs with CTL field equal to 1 relayed by a Directed Relay node and secured with directed security material. The Directed Control Relay Retransmit Count + 1 is the number of times that a Network PDU is
transmitted for each Network PDU that is relayed.

For example, 0b000 represents a single transmission and 0b111 represents 8 transmissions.

The default value of the Directed Control Relay Retransmit Count state is 0b010 (3 transmissions).

##### 4.2.40.2. Directed Control Relay Retransmit Interval Steps

The Directed Control Relay Retransmit Interval Steps state is a 5-bit value representing the number of 10-millisecond steps, which controls the interval between retransmissions of Network PDUs with CTL field equal to 1 relayed by a Directed Relay node and secured with directed security material.

The transmission interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *transmission interval=(Directed Control Relay Retransmit Interval Steps+1)×10* |

For example, 0b10000 represents an interval from 170 milliseconds to 180 milliseconds between transmissions.

The default value of the Directed Control Relay Retransmit Interval Steps state is 0b01001 (i.e., 100 milliseconds)

A bearer (for example, the advertising bearer) can impose restrictions on the set of intervals that it considers valid. Therefore, the interval used can be larger than the value of the state.

#### 4.2.41. Subnet Bridge

The Subnet Bridge state controls whether subnet bridge functionality is enabled or disabled. The values of the Subnet Bridge state are defined in [Table 4.69](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf_Table_4.69 "Table 4.69. Subnet Bridge state values").

| Value | Description |
| --- | --- |
| 0x00 | Subnet bridge functionality is disabled. |
| 0x01 | Subnet bridge functionality is enabled. |
| 0x02–0xFF | Prohibited |

Table 4.69. Subnet Bridge state values

The default value of the Subnet Bridge state shall be 0x00.

#### 4.2.42. Bridging Table

The Bridging Table state is a list of entries. Each entry includes the NetKey Indexes of a pair of subnets, a pair of addresses in those subnets, and traffic directions for which subnet bridging is allowed. There is a single instance of a Bridging Table state for a Subnet Bridge node.

Each Bridging Table state entry shall have the format defined in [Table 4.70](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.70 "Table 4.70. Bridging Table state entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Directions | 8 | Allowed directions for the bridged traffic | M |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |
| Address1 | 16 | Address of the node in the first subnet | M |
| Address2 | 16 | Address of the node in the second subnet | M |

Table 4.70. Bridging Table state entry format

The values for the Directions field are defined in [Table 4.71](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.71 "Table 4.71. Directions field values").

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01 | Bridging is allowed only for messages with Address1 as the source address and Address2 as the destination address. |
| 0x02 | Bridging is allowed for messages with Address1 as the source address and Address2 as the destination address, and messages with Address2 as the source address and Address1 as the destination address. |
| 0x03–0xFF | Prohibited |

Table 4.71. Directions field values

The Bridging Table state shall be empty by default.

##### 4.2.42.1. Binding with NetKey List state

When a NetKey is deleted from the NetKey List state, and subnet bridge functionality is supported, then all the Bridging Table state entries with one of the values of the NetKeyIndex1 and NetKeyIndex2 fields that matches the NetKey Index of the deleted NetKey are removed according to the requirements in [Section 4.4.1.2.9](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce "4.4.1.2.9. NetKey List state").

#### 4.2.43. Bridging Table Size

The Bridging Table Size state is a 2-octet value indicating the maximum number of Bridging Table state entries that the Subnet Bridge node can support. Multiple Bridging Table state entries can be stored for a single pair of subnets.

The Bridging Table Size state value shall be at least 16.

#### 4.2.44. Mesh Private Beacon

The Mesh Private Beacon state is a composite state that controls the transmission of Mesh Private beacons and the cadence of the Random field updates in the Mesh Private beacon.

##### 4.2.44.1. Private Beacon

The Private Beacon state determines whether a node broadcasts Mesh Private beacons periodically (see [Section 3.10.4.2](index-en.html#UUID-b020a4a9-53d8-c12a-e65c-6a7885d6cc68 "3.10.4.2. Mesh Private beacon behavior")).

The values of the state are defined in [Table 4.72](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853_Table_4.72 "Table 4.72. Private Beacon state"). The default value shall be Disable (0x00).

| Value | Name | Definition |
| --- | --- | --- |
| 0x00 | Disable | The node does not broadcast Mesh Private beacons. |
| 0x01 | Enable | The node broadcasts Mesh Private beacons. |
| 0x02–0xFF | Prohibited | Prohibited |

Table 4.72. Private Beacon state

##### 4.2.44.2. Random Update Interval Steps

The Random Update Interval Steps state determines the cadence of updates to the Random field in the Mesh Private beacon. The Random Update Interval Steps are defined in units of 10 seconds, with an approximate maximum value of 42 minutes.

The values of the Random Update Interval Steps state are defined in [Table 4.73](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb_Table_4.73 "Table 4.73. Random Update Interval Steps state values"). The default value of this state shall be 60 (0x3C) (i.e.,
10 minutes).

| Value | Definition |
| --- | --- |
| 0x00 | Random field is updated for every Mesh Private beacon. |
| 0x01–0xFF | Random field is updated at an interval (in seconds) of (10 * Random Update Interval Steps). |

Table 4.73. Random Update Interval Steps state values

#### 4.2.45. Private GATT Proxy

The Private GATT Proxy state indicates whether the Private Proxy functionality (see [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality")) is supported. If the Private Proxy functionality is supported, the Private
GATT Proxy state indicates support of and controls the Private Proxy functionality.

If the Private Proxy functionality is disabled and the GATT server is advertising with Private Node Identity (see [Section 7.2.2.2.5](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e "7.2.2.2.5. Advertising with Private Node Identity")), a GATT client device can
connect over GATT to that node for configuration and control. Messages from the GATT bearer are not relayed to the advertising bearer.

The values for the Private GATT Proxy state are defined in [Table 4.74](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4_Table_4.74 "Table 4.74. Private GATT Proxy state values").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disabled | The Private Proxy functionality is supported and disabled. |
| 0x01 | Enabled | The Private Proxy functionality is supported and enabled. |
| 0x02 | Not Supported | The Private Proxy functionality is not supported. |
| 0x03–0xFF | Prohibited | Prohibited |

Table 4.74. Private GATT Proxy state values

If the Private Proxy functionality is not supported, the value of the Private GATT Proxy state shall be Not Supported and shall not be changed.

If Private Proxy functionality is supported, the value of the Private GATT Proxy state shall be either Disabled or Enabled.

If Private Proxy functionality is supported, then the default value of the Private GATT Proxy state shall be Disabled; otherwise, the default value of the Private GATT Proxy state shall be Not Supported.

##### 4.2.45.1. Binding with GATT Proxy

If the value of the GATT Proxy state of the node is Not Supported (see [Table 4.27](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3_Table_4.27 "Table 4.27. GATT Proxy values")), then the value of the Private GATT Proxy state shall be Not Supported and
shall not be changed.

If the value of the GATT Proxy state of the node is Enabled (see [Table 4.27](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3_Table_4.27 "Table 4.27. GATT Proxy values")), then the value of the Private GATT Proxy state shall be Disabled. Therefore, to
change the Private GATT Proxy state to Enabled, the GATT Proxy state must be set to Disabled.

#### 4.2.46. Private Node Identity

The Private Node Identity state indicates and controls whether a node is advertising with Private Node Identity messages on a subnet (see [Section 7.2.2.2.5](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e "7.2.2.2.5. Advertising with Private Node Identity")).
The Private Node Identity state is defined for each known subnet. If the Mesh Proxy Service is exposed, the node can be configured to advertise with Private Node Identity on a subnet (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

The values for the Private Node Identity state are defined in [Table 4.75](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee_Table_4.75 "Table 4.75. Private Node Identity values").

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disabled | Advertising with Private Node Identity for a subnet is stopped. |
| 0x01 | Enabled | Advertising with Private Node Identity for a subnet is running. |
| 0x02 | Not Supported | Advertising with Private Node Identity is not supported. |
| 0x03–0xFF | Prohibited | Prohibited |

Table 4.75. Private Node Identity values

If the Private Node Identity functionality is not supported, the value of the Private Node Identity state shall be Not Supported and shall not be changed.

If the Private Node Identity functionality is supported, the value of the Private Node Identity state shall be either Disabled or Enabled.

If the Private Node Identity functionality is supported, then the default value of the Private Node Identity state shall be Disabled.

##### 4.2.46.1. Binding with Node Identity

If the value of the Node Identity state of the node is Not Supported (see [Table 4.28](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97_Table_4.28 "Table 4.28. Node Identity values")), then the value of the Private Node Identity state shall be Not Supported
and shall not be changed.

If the value of the Node Identity state of the node for any subnet is Enabled (see [Table 4.28](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97_Table_4.28 "Table 4.28. Node Identity values")), then the value of the Private Node Identity state shall be
Disabled for each known subnet. Therefore, to change the Private Node Identity state to Enabled, the Node Identity state must be set to Disabled for all subnets.

#### 4.2.47. On-Demand Private GATT Proxy

The On-Demand Private GATT Proxy state indicates whether advertising with Private Network Identity type (see [Section 7.2](index-en.html#UUID-27102d68-3ce7-da1c-30c7-0363cb0671be "7.2. Mesh Proxy Service")) can be enabled on demand and can be triggered upon reception of
a Solicitation PDU.

The value of this state determines the interval (in seconds) during which advertising with Private Network Identity type is enabled after receiving a Solicitation PDU or after a client disconnects.

The values for this state are defined in [Table 4.76](index-en.html#UUID-b688770d-69cc-ff39-feb3-8b82ebe09fb5_Table_4.76 "Table 4.76. On-Demand Private GATT Proxy values").

| Value | Description |
| --- | --- |
| 0x00 | Advertising with Private Network Identity type cannot be enabled on demand |
| 0x01–0xFF | Duration in seconds of the interval during which advertising with Private Network Identity type is enabled after receiving a Solicitation PDU or after a client disconnect |

Table 4.76. On-Demand Private GATT Proxy values

##### 4.2.47.1. Binding with the Private GATT Proxy state

The On-Demand Private GATT Proxy state is conditionally bound to the Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

If the Private GATT Proxy state value is 0x02, the On-Demand Private GATT Proxy state value shall be set to 0x00 and shall not be changed.

#### 4.2.48. SAR Transmitter

The SAR Transmitter state is a composite state that controls the number and timing of transmissions of segmented messages. A node shall implement the SAR Transmitter state independently of the presence of the SAR Configuration Server model.

The SAR Transmitter state includes the SAR Segment Interval Step state, the SAR Unicast Retransmissions Count state, the SAR Unicast Retransmissions Without Progress Count state, the SAR Unicast Retransmissions Interval Step state, the SAR Unicast Retransmissions Interval Increment state, the SAR Multicast Retransmissions Count
state, and the SAR Multicast Retransmissions Interval Step state (see [Section 4.2.48.7](index-en.html#UUID-2dd60df5-b721-e70e-e473-b8c4ad9faec0 "4.2.48.7. SAR Multicast Retransmissions Interval Step")).

##### 4.2.48.1. SAR Segment Interval Step

The SAR Segment Interval Step state is a 4-bit value that controls the interval between transmissions of segments of a segmented message.

The segment transmission interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *segment transmission interval=(SAR Segment Interval Step+1)×10* |

The default value of the SAR Segment Interval Step state should be 0b0101 (60 milliseconds).

##### 4.2.48.2. SAR Unicast Retransmissions Count

The SAR Unicast Retransmissions Count state is a 4-bit value that controls the maximum number of transmissions of segments of segmented messages to a unicast destination. The maximum number of transmissions of a segment is (SAR Unicast Retransmissions Count + 1).

For example, 0b0000 represents a single transmission, and 0b0111 represents 8 transmissions.

The default value of the SAR Unicast Retransmissions Count state should be 0b0010 (3 transmissions).

##### 4.2.48.3. SAR Unicast Retransmissions Without Progress Count

The SAR Unicast Retransmissions Without Progress Count state is a 4-bit value that controls the maximum number of transmissions of segments of segmented messages to a unicast destination without progress (i.e., without newly marking any segment as acknowledged). The maximum number of transmissions of a segment without progress
is (SAR Unicast Retransmissions Without Progress Count + 1).

For example, 0b0000 represents a single transmission, and 0b0111 represents 8 transmissions.

The default value of the SAR Unicast Retransmissions Without Progress Count state should be 0b0010 (3 transmissions).

The value of this state should be set to a value greater than the value of the SAR Acknowledgement Retransmissions Count on a peer node. This helps prevent the SAR transmitter from abandoning the SAR prematurely.

##### 4.2.48.4. SAR Unicast Retransmissions Interval Step

The SAR Unicast Retransmissions Interval Step state is a 4-bit value that controls the interval between retransmissions of segments of a segmented message for a destination that is a unicast address.

The unicast retransmissions interval step is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *unicast retransmissions interval=(SAR Unicast Retransmissions Interval Step+1)×25* |

The default value of the SAR Unicast Retransmissions Interval Step should be 0b0111 (200 milliseconds) or higher.

##### 4.2.48.5. SAR Unicast Retransmissions Interval Increment

The SAR Unicast Retransmissions Interval Increment state is a 4-bit value that controls the incremental component of the interval between retransmissions of segments of a segmented message for a destination that is a unicast address.

The unicast retransmissions interval increment is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *unicast retransmissions interval increment=(SAR Unicast Retransmissions Interval Increment+1)×25* |

The default value of the SAR Unicast Retransmissions Interval Increment state should be 0b0001 (50 milliseconds).

##### 4.2.48.6. SAR Multicast Retransmissions Count

The SAR Multicast Retransmissions Count state is a 4-bit value that controls the maximum number of transmissions of segments of segmented messages to a group address or a virtual address. The maximum number of transmissions of a segment is (SAR Multicast Retransmissions Count + 1).

For example, 0b0000 represents a single transmission, and 0b0111 represents 8 transmissions.

The default value of the SAR Multicast Retransmissions Count state should be 0b0010 (3 transmissions).

##### 4.2.48.7. SAR Multicast Retransmissions Interval Step

The SAR Multicast Retransmissions Interval Step state is a 4-bit value that controls the interval between retransmissions of segments of a segmented message for a destination that is a group address or a virtual address.

The multicast retransmissions interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *multicast retransmissions interval=(SAR Multicast Retransmissions Interval Step+1)×25* |

The default value of the SAR Multicast Retransmissions Interval Step state should be 0b1001 (250 milliseconds).

#### 4.2.49. SAR Receiver

The SAR Receiver state is a composite state that controls the number and timing of Segment Acknowledgment transmissions and the discarding of reassembly of a segmented message. The node shall implement the SAR Receiver independently of the presence of the SAR Configuration Server model.

The SAR Receiver state includes the SAR Segments Threshold state, the SAR Discard Delay state, the SAR Acknowledgment Delay Increment state, the SAR Acknowledgment Retransmissions Count state, and the SAR Receiver Segment Interval Step state.

##### 4.2.49.1. SAR Segments Threshold

The SAR Segments Threshold state is a 5-bit value that represents the size of a segmented message in number of segments above which the Segment Acknowledgment messages are enabled.

The default value for the SAR Segments Threshold state should be 0b00011 (3 segments).

##### 4.2.49.2. SAR Acknowledgment Delay Increment

The SAR Acknowledgment Delay Increment state is a 3-bit value that controls the interval between the reception of a new segment of a segmented message for a destination that is a unicast address and the transmission of the Segment Acknowledgment for that message.

The acknowledgment delay increment is calculated using the following formula:

|  |
| --- |
| *acknowledgment delay increment=SAR Acknowledgment Delay Increment+1.5* |

The default value of the SAR Acknowledgment Delay Increment state should be 0b001 (2.5 segment transmission interval steps) or higher.

##### 4.2.49.3. SAR Acknowledgment Retransmissions Count

The SAR Acknowledgment Retransmissions Count state is a 2-bit value that controls the number of retransmissions of Segment Acknowledgment messages sent by the lower transport layer. The maximum number of transmissions of a Segment Acknowledgment message is (SAR Acknowledgment Retransmissions Count + 1).

For example, 0b00 represents a limit of 1 transmission, and 0b11 represents a limit of 4 transmissions.

The default value of the SAR Acknowledgment Retransmissions Count state should be 0b00 (1 transmission).

##### 4.2.49.4. SAR Discard Timeout

The SAR Discard Timeout state is a 4-bit value that controls the time that the lower transport layer waits after receiving unique segments of a segmented message before discarding that segmented message.

The discard timeout is the number of seconds calculated using the following formula:

|  |
| --- |
| *discard timeout=(SAR Discard Timeout+1)×5* |

The default value of the SAR Discard Timeout state should be 0b0001 (10 seconds) or higher.

##### 4.2.49.5. SAR Receiver Segment Interval Step

The SAR Receiver Segment Interval Step state is a 4-bit value that indicates the interval between received segments of a segmented message. This is used to control rate of transmission of Segment Acknowledgment messages.

The segment reception interval is the number of milliseconds calculated using the following formula:

|  |
| --- |
| *segment reception interval=(SAR Receiver Segment Interval Step+1)×10* |

The default value of the SAR Receiver Segment Interval Step state should be 0b0101 (60 milliseconds).

#### 4.2.50. Models Metadata

The Models Metadata state contains metadata of a node’s models. The Models Metadata state is composed of a number of pages of information. If the Large Composition Data Server model is supported, Models Metadata Page 0 is mandatory. If both the Large Composition Data Server model and the Remote Provisioning Server model are
supported, then Models Metadata Page 128 is mandatory; otherwise, it is optional. All other pages are optional. All Models Metadata Pages not defined in this specification are reserved for future use.

The Models Metadata Page corresponds to the Composition Data Page with the same page number.

##### 4.2.50.1. Models Metadata Page 0

Models Metadata Page 0 shall be present if the node supports the Large Composition Data Server model.

Composition Metadata Page 0 shall not change during a term of a node on the network (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")).

The format of the Models Metadata Page 0 is defined in [Table 4.77](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.77 "Table 4.77. Models Metadata Page 0 fields").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Metadata_Elements | variable | List of metadata for models for each element | M |

Table 4.77. Models Metadata Page 0 fields

The Metadata_Elements field indicates a list of metadata for models of the elements. The order of the list shall be the same as in the corresponding Composition Data Page.

The format of each entry in the Metadata_Elements field is defined in [Table 4.78](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.78 "Table 4.78. Metadata_Elements field entry format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Items_Number_SIG_Models | 1 | Number of metadata items for SIG models in the element | M |
| Items_Number_Vendor_Models | 1 | Number of metadata items for vendor models in the element | M |
| SIG_Metadata_Items | variable | List of metadata items for SIG models in the element | O |
| Vendor_Metadata_Items | variable | List of metadata items for vendor models in the element | O |

Table 4.78. Metadata_Elements field entry format

The Items_Number_SIG_Models field indicates the number of metadata items for the SIG models. The Items_Number_SIG_Models field value shall be less than or equal to the NumS field of the corresponding element in the Composition Data Page 0.

The Items_Number_Vendor_Models field indicates the number of metadata items for the vendor models. The Items_Number_Vendor_Models field value shall be less than or equal to the NumV field of the corresponding element in the Composition Data Page 0.

If present, the SIG_Metadata_Items field includes a list of metadata for SIG models in the element.

The format of each entry in the SIG_Metadata_Items field is defined in [Table 4.79](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.79 "Table 4.79. SIG_Metadata_Items field entry format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Model_ID | 2 | SIG model identifier | M |
| Metadata_Entries_Number | 1 | Number of metadata entries | M |
| Metadata_Entries | variable | List of model’s metadata | M |

Table 4.79. SIG_Metadata_Items field entry format

The Model_ID field includes the SIG Model identifier of the model to which the metadata applies.

The Metadata_Entries_Number field includes the number of metadata items in the Metadata_Items field.

The Metadata_Items field includes a list of metadata for the model.

The format of each entry in the Metadata_Entries field is defined in [Table 4.80](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.80 "Table 4.80. Metadata_Entries field entry format").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Metadata_Length | 2 | Size of the Metadata field | M |
| Metadata_ID | 2 | Bluetooth assigned number for the Metadata Identifier | M |
| Metadata | variable | Model’s metadata | M |

Table 4.80. Metadata_Entries field entry format

The Metadata_Length field indicates the size in octets of the Metadata field.

The Metadata_ID field indicates the Bluetooth assigned number for the Metadata Identifier [[4](index-en.html#idp254746)].

The Metadata field indicates the metadata of the corresponding model and Metadata Identifier.

If present, the Vendor_Metadata_Items field includes a list of metadata for vendor models in the element.

The format of each entry in the Vendor_Metadata_Items field is defined in [Table 4.81](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.81 "Table 4.81. Vendor_Metadata_Items field entry format ").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Model_ID | 4 | Vendor model identifier | M |
| Metadata_Entries_Number | 1 | Number of metadata entries | M |
| Metadata_Entries | variable | List of model’s metadata | M |

Table 4.81. Vendor_Metadata_Items field entry format

The Model_ID field includes the Vendor Model identifier of the model to which the metadata applies.

The Metadata_Entries_Number field includes the number of metadata items in the Metadata_Items field.

The Metadata_Items field includes a list of metadata for the model.

The format of each entry in the Metadata_Entries field is defined in [Table 4.80](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.80 "Table 4.80. Metadata_Entries field entry format").

[Table 4.82](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Table_4.82 "Table 4.82. Correspondence conditions for models in Composition Data Pages and Models Metadata Pages ") defines correspondence conditions between the Model ID of the Composition
Data Pages (0 and 128) and the model’s Metadata_Item of the Models Metadata Pages (0 and 128).

| Condition |
| --- |
| Composition Data Page is equal to Models Metadata Page |
| Elements field entry has the same index as the Metadata_Elements field entry |

Table 4.82. Correspondence conditions for models in Composition Data Pages and Models Metadata Pages

The example in [Figure 4.3](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad_Figure_4.3 "Figure 4.3. Models Metadata Page 0 example") shows Models Metadata Page 0 with two elements. Metadata_Element #0 includes two metadata items for a SIG model and one for
a vendor model for the primary element.

|  |
| --- |
| Models Metadata Page 0 example |

Figure 4.3. Models Metadata Page 0 example

##### 4.2.50.2. Models Metadata Page 128

Models Metadata Page 128 contains metadata for the node’s models in a new term (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")).

Models Metadata Page 128 shall be present if the node supports the Remote Provisioning Server model and the node supports the Large Composition Data Server model.

The structure of Models Metadata Page 128 is identical to the structure of Models Metadata Page 0.

Models Metadata Page 128 shall represent the contents that Models Metadata Page 0 will contain in a new term.

### 4.3. Message definitions

This section defines messages used throughout this specification. Each message has an opcode and zero or more parameters, as defined in [Section 3.7.2](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9 "3.7.2. Access message"). Messages are also defined as either
unacknowledged or acknowledged. Acknowledged messages have defined responses that shall be used to confirm execution.

Message definitions that are not required as part of this specification are defined in the Mesh Model specification [[9](index-en.html#idp254760)] and follow the same format and architecture as mesh message definitions.

#### 4.3.1. Supplemental parameter requirements

This section contains supplemental requirements for the handling of some parameters. Parameter values that do not conform to these requirements shall be considered Reserved for Future Use.

##### 4.3.1.1. Key indexes

Both NetKeys and AppKeys are 16-octets long and thus do not fit in a single-segment message. The generic segmentation and reassembly mechanism is used to transport new keys to nodes.

A Configuration Client maintains two indexed global lists of NetKeys and AppKeys – the NetKey List and AppKey List. Each key shall have a unique global index in the appropriate list and this index is used to identify that key in the module.

Global key indexes are 12 bits long. Some messages include one, two or multiple key indexes. To enable efficient packing, two key indexes are packed into three octets. Where an odd number of key indexes need to be packed, all but the last key index are packed into sequences of three octets (see [Figure 4.4](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d_figure-idm4511324930430434099957641383 "Figure 4.4. Packing of two 12-bit key Indexes into three octets")), and the last key index is packed into two octets (see [Figure 4.5](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d_figure-idm4595263938324834099959128916 "Figure 4.5. Encoding of one 12-bit key index into two octets")). Where an even number of key indexes need to be packed, they are all packed into sequences of three octets.

To pack two key indexes into three octets, 8 LSbs of first key index value are packed into the first octet, placing the remaining 4 MSbs into 4 LSbs of the second octet. The first 4 LSbs of the second 12-bit key index are packed into the 4 MSbs of the second octet with the remaining 8 MSbs into the third octet.

|  |
| --- |
| Packing of two 12-bit key Indexes into three octets |

Figure 4.4. Packing of two 12-bit key Indexes into three octets

To pack one key index into two octets, 8 LSbs of first key index value are packed into the first octet, placing the remaining 4 MSbs into 4 LSbs of the second octet, and the 4 MSbs of the second octet shall be set to 0.

|  |
| --- |
| Encoding of one 12-bit key index into two octets |

Figure 4.5. Encoding of one 12-bit key index into two octets

##### 4.3.1.2. Element addresses

Messages may contain fields carrying network addresses, such as an element address, a group address, or a virtual address. Such fields may be used by the access layer and other upper layers, but shall not be used by the network layer, the lower transport layer, nor the upper transport layer.

##### 4.3.1.3. Model identifiers

Messages may contain fields carrying Model IDs. Such fields may have a 2-octet size or a 4-octet size to accommodate either a SIG Model ID (16-bit) or a Vendor Model ID (32-bit).

##### 4.3.1.4. Bearer index

The bearer index is a 16-bit field that identifies a bearer or a combination of bearers. Bit 0 indicates the advertising bearer, and bit 1 indicates the GATT bearer. Bits 2 to 15 of the bearer index are RFU.

An unassigned bearer index is a bearer index that does not represent any bearer. The unassigned bearer index has all bits set to 0.

#### 4.3.2. Configuration messages

Configuration messages are used to control states that determine network-related behaviors of the node, manipulate network and application keys, as well as perform other operations that require an elevated level of security.

##### 4.3.2.1. Config Beacon Get

A Config Beacon Get is an acknowledged message used to get the current Secure Network Beacon state of a node (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")).

The response to a Config Beacon Get message is a Config Beacon Status message.

The structure of the Config Beacon Get message is defined in [Table 4.83](index-en.html#UUID-ccfeadac-f7fa-4f00-d9db-f5349488ff24_Table_4.83 "Table 4.83. Config Beacon Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.83. Config Beacon Get message structure

The Opcode field shall contain the opcode value for the Config Beacon Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.2. Config Beacon Set

A Config Beacon Set is an acknowledged message used to set the Secure Network Beacon state of a node (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")).

The response to a Config Beacon Set message is a Config Beacon Status message.

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Beacon | 1 | New Secure Network Beacon state | M |

Table 4.84. Config Beacon Set message structure

The Opcode field shall contain the opcode value for the Config Beacon Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Beacon field shall provide the new Secure Network Beacon state of the node (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")).

##### 4.3.2.3. Config Beacon Status

A Config Beacon Status is an unacknowledged message used to report the current Secure Network Beacon state of a node (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Beacon | 1 | Secure Network Beacon state | M |

Table 4.85. Config Beacon Status message structure

The Opcode field shall contain the opcode value for the Config Beacon Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Beacon field shall provide the current Secure Network Beacon state of the node (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")).

##### 4.3.2.4. Config Composition Data Get

A Config Composition Data Get is an acknowledged message used to read one page of the Composition Data (see Section [4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

The response to a Config Composition Data Get message is a Config Composition Data Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Page | 1 | Page number of the Composition Data | M |

Table 4.86. Config Composition Data Get message structure

The Opcode field shall contain the opcode value for the Config Composition Data Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Page field shall identify the Composition Data Page number that is being read.

##### 4.3.2.5. Config Composition Data Status

A Config Composition Data Status is an unacknowledged message used to report a single page of the Composition Data (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

This message uses a single-octet opcode to maximize the size of a payload.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| Page | 1 | Page number of the Composition Data | M |
| Data | variable | Composition Data for the identified page | M |

Table 4.87. Config Composition Data Status message structure

The Opcode field shall contain the opcode value for the Config Composition Data Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Page field shall identify the Composition Data Page number.

The Data field shall contain the identified single page of the Composition Data.

##### 4.3.2.6. Config Default TTL Get

A Config Default TTL Get is an acknowledged message used to get the current Default TTL state of a node.

The response to a Config Default TTL Get message is a Config Default TTL Status message.

The structure of the Config Default TTL Get message is defined in [Table 4.88](index-en.html#UUID-9be61801-8a01-86fd-36f2-c61e4743fdb3_Table_4.88 "Table 4.88. Config Default TTL Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.88. Config Default TTL Get message structure

The Opcode field shall contain the opcode value for the Config Default TTL Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.7. Config Default TTL Set

A Config Default TTL Set is an acknowledged message used to set the Default TTL state of a node (see [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL")).

The response to a Config Default TTL Set message is a Config Default TTL Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| TTL | 1 | New Default TTL value | M |

Table 4.89. Config Default TTL Set message structure

The Opcode field shall contain the opcode value for the Config Default TTL Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The TTL field shall identify a new Default TTL for the node (see [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL")).

##### 4.3.2.8. Config Default TTL Status

A Config Default TTL Status is an unacknowledged message used to report the current Default TTL state of a node (see [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| TTL | 1 | Default TTL | M |

Table 4.90. Config Default TTL Status message structure

The Opcode field shall contain the opcode value for the Config Default TTL Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The TTL field shall identify the Default TTL for the node, as defined in Default TTL (see [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL")).

##### 4.3.2.9. Config GATT Proxy Get

A Config GATT Proxy Get is an acknowledged message used to get the current GATT Proxy state of a node (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")).

The response to a Config GATT Proxy Get message is a Config GATT Proxy Status message.

The structure of the Config GATT Proxy Get message is defined in [Table 4.91](index-en.html#UUID-f398bf54-b66e-6a61-7d8d-f53dc15be81f_Table_4.91 "Table 4.91. Config GATT Proxy Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.91. Config GATT Proxy Get message structure

The Opcode field shall contain the opcode value for the Config GATT Proxy Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.10. Config GATT Proxy Set

A Config GATT Proxy Set is an acknowledged message used to set the GATT Proxy state of a node (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")).

The response to a Config GATT Proxy Set message is a Config GATT Proxy Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| GATTProxy | 1 | New GATT Proxy state | M |

Table 4.92. Config GATT Proxy Set message structure

The Opcode field shall contain the opcode value for the Config GATT Proxy Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The GATTProxy field shall provide the new GATT Proxy state of the node (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")).

##### 4.3.2.11. Config GATT Proxy Status

A Config GATT Proxy Status is an unacknowledged message used to report the current GATT Proxy state of a node (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| GATTProxy | 1 | GATT Proxy state | M |

Table 4.93. Config GATT Proxy Status message structure

The Opcode field shall contain the opcode value for the Config GATT Proxy Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The GATTProxy field shall provide the current GATT Proxy state of the node (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")).

##### 4.3.2.12. Config Relay Get

A Config Relay Get is an acknowledged message used to get the current Relay (see [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay")) and Relay Retransmit (see [Section 4.2.21](index-en.html#UUID-0b36a2de-a550-d0f8-677a-5cc500a65aa3 "4.2.21. Relay Retransmit")) states of a node.

The response to a Config Relay Get message is a Config Relay Status message.

The structure of the Config Relay Get message is defined in [Table 4.94](index-en.html#UUID-852f8ee6-b724-35c9-42ba-9c6a244c00d9_Table_4.94 "Table 4.94. Config Relay Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.94. Config Relay Get message structure

The Opcode field shall contain the opcode value for the Config Relay Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.13. Config Relay Set

A Config Relay Set is an acknowledged message used to set the Relay (see [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay")) and Relay Retransmit (see [Section 4.2.21](index-en.html#UUID-0b36a2de-a550-d0f8-677a-5cc500a65aa3 "4.2.21. Relay Retransmit")) states of a node.

The response to a Config Relay Set message is a Config Relay Status message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Relay | 8 | Relay | M |
| RelayRetransmitCount | 3 | Number of retransmissions on advertising bearer for each Network PDU relayed by the node | M |
| RelayRetransmitIntervalSteps | 5 | Number of 10-millisecond steps between retransmissions | M |

Table 4.95. Config Relay Set message structure

The Opcode field shall contain the opcode value for the Config Relay Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Relay field shall identify the new Relay state for the node, as defined in [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay").

The RelayRetransmitCount field shall contain a new value for the Relay Retransmit Count state of a node (see [Section 4.2.21.1](index-en.html#UUID-77fc564e-e5ed-e0fe-66c2-896aab67bbf7 "4.2.21.1. Relay Retransmit Count")).

The RelayRetransmitIntervalSteps field shall contain a new value for the Relay Retransmit Interval Steps state of a node (see [Section 4.2.21.2](index-en.html#UUID-27e0d4d9-6a1a-f425-01e5-830f205a6768 "4.2.21.2. Relay Retransmit Interval Steps")).

##### 4.3.2.14. Config Relay Status

A Config Relay Status is an unacknowledged message used to report the current Relay (see [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay")) and Relay Retransmit (see [Section 4.2.21](index-en.html#UUID-0b36a2de-a550-d0f8-677a-5cc500a65aa3 "4.2.21. Relay Retransmit")) states of a node.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Relay | 8 | Relay | M |
| RelayRetransmitCount | 3 | Number of retransmissions on advertising bearer for each Network PDU relayed by the node | M |
| RelayRetransmitIntervalSteps | 5 | Number of 10-millisecond steps between retransmissions | M |

Table 4.96. Config Relay Status message structure

The Opcode field shall contain the opcode value for the Config Relay Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Relay field shall identify the current Relay state for the node, as defined in [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay").

The RelayRetransmitCount field shall contain a new value for the Relay Retransmit Count state of a node (see [Section 4.2.21.1](index-en.html#UUID-77fc564e-e5ed-e0fe-66c2-896aab67bbf7 "4.2.21.1. Relay Retransmit Count")).

The RelayRetransmitIntervalSteps field shall contain a new value for the Relay Retransmit Interval Steps state of a node (see [Section 4.2.21.2](index-en.html#UUID-27e0d4d9-6a1a-f425-01e5-830f205a6768 "4.2.21.2. Relay Retransmit Interval Steps")).

##### 4.3.2.15. Config Model Publication Get

A Config Model Publication Get is an acknowledged message used to get the publish address and parameters of an outgoing message that originates from a model.

The response to a Config Model Publication Get message is a Config Model Publication Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.97. Config Model Publication Get message structure

The Opcode field shall contain the opcode value for the Config Model Publication Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.16. Config Model Publication Set

A Config Model Publication Set is an acknowledged message used to set the Model Publication state (see [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129")) of an outgoing message that originates from a
model.

The response to a Config Model Publication Set message is a Config Model Publication Status message.

The Config Model Publication Set message uses a single-octet opcode to maximize the size of a payload.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 8 | The message opcode | M |
| ElementAddress | 16 | Address of the element | M |
| PublishAddress | 16 | Value of the publish address | M |
| AppKeyIndex | 12 | Index of the application key | M |
| CredentialFlag | 1 | Value of the Friendship Credential Flag | M |
| RFU | 3 | Reserved for Future Use | M |
| PublishTTL | 8 | Default TTL value for the outgoing messages | M |
| PublishPeriod | 8 | Period for periodic status publishing | M |
| PublishRetransmitCount | 3 | Number of retransmissions for each published message | M |
| PublishRetransmitIntervalSteps | 5 | Number of 50-millisecond steps between retransmissions | M |
| ModelIdentifier | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.98. Config Model Publication Set message structure

![Config Model Publication Set format](image/1671b81d79a01f.png)

Figure 4.6. Config Model Publication Set format

The Opcode field shall contain the opcode value for the Config Model Publication Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The PublishAddress field shall contain the new Publish Address state (see [Section 4.2.3.1](index-en.html#UUID-cf2e0dbd-668d-dc4d-d1c9-ce7bb3023073 "4.2.3.1. Publish Address")) for the model. A virtual address value of the PublishAddress field is Prohibited.

The AppKeyIndex field shall contain the new Publish AppKey Index state (see [Section 4.2.3.3](index-en.html#UUID-21c07c92-e42b-73c5-33ef-f744a24011be "4.2.3.3. Publish AppKey Index")).

The CredentialFlag field shall contain the new Publish Friendship Credentials Flag state (see [Section 4.2.3.4](index-en.html#UUID-9f0b2d51-1d32-c1e4-fabd-62b4bfb48257 "4.2.3.4. Publish Friendship Credentials Flag")).

The PublishTTL field shall contain the new Publish TTL state (see [Section 4.2.3.5](index-en.html#UUID-bcd4eceb-9a71-bf4e-c238-27594178db23 "4.2.3.5. Publish TTL")).

The PublishPeriod field shall contain a new value for the Publish Period state (see [Section 4.2.3.2](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4 "4.2.3.2. Publish Period")).

The PublishRetransmitCount field shall contain a new value for the Publish Retransmit Count state of an element (see [Section 4.2.3.6](index-en.html#UUID-7ff4b704-2bb8-1887-7b33-8dd510069452 "4.2.3.6. Publish Retransmit Count")).

The PublishRetransmitIntervalSteps field shall contain a new value for the Publish Retransmit Interval Steps state of an element (see [Section 4.2.3.7](index-en.html#UUID-7135206d-7865-bc4a-d2ca-36f94d561b89 "4.2.3.7. Publish Retransmit Interval Steps")).

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.17. Config Model Publication Virtual Address Set

A Config Model Publication Virtual Address Set is an acknowledged message used to set the model Publication state (see [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129")) of an outgoing message that
originates from a model.

The response to a Config Model Publication Virtual Address Set message is a Config Model Publication Status message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| ElementAddress | 16 | Address of the element | M |
| PublishAddress | 128 | Value of the Label UUID publish address | M |
| AppKeyIndex | 12 | Index of the application key | M |
| CredentialFlag | 1 | Value of the Friendship Credential Flag | M |
| RFU | 3 | Reserved for Future Use | M |
| PublishTTL | 8 | Default TTL value for the outgoing messages | M |
| PublishPeriod | 8 | Period for periodic status publishing | M |
| PublishRetransmitCount | 3 | Number of retransmissions for each published message | M |
| PublishRetransmitIntervalSteps | 5 | Number of 50-millisecond steps between retransmissions | M |
| ModelIdentifier | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.99. Config Model Publication Virtual Address Set message structure

The Opcode field shall contain the opcode value for the Config Model Publication Virtual Address Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The PublishAddress field shall contain the Label UUID used as the new Publish Address state (see [Section 4.2.3.1](index-en.html#UUID-cf2e0dbd-668d-dc4d-d1c9-ce7bb3023073 "4.2.3.1. Publish Address")) for the model.

The AppKeyIndex field shall contain the new Publish AppKey Index state (see [Section 4.2.3.3](index-en.html#UUID-21c07c92-e42b-73c5-33ef-f744a24011be "4.2.3.3. Publish AppKey Index")).

The CredentialFlag field shall contain the new Publish Friendship Credentials Flag state (see [Section 4.2.3.4](index-en.html#UUID-9f0b2d51-1d32-c1e4-fabd-62b4bfb48257 "4.2.3.4. Publish Friendship Credentials Flag")).

The PublishTTL field shall contain the new Publish TTL state (see [Section 4.2.3.5](index-en.html#UUID-bcd4eceb-9a71-bf4e-c238-27594178db23 "4.2.3.5. Publish TTL")).

The PublishPeriod field shall contain a new value for the Publish Period state (see [Section 4.2.3.2](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4 "4.2.3.2. Publish Period")).

The PublishRetransmitCount field shall contain a new value for the Publish Retransmit Count state of an element (see [Section 4.2.3.6](index-en.html#UUID-7ff4b704-2bb8-1887-7b33-8dd510069452 "4.2.3.6. Publish Retransmit Count")).

The PublishRetransmitIntervalSteps field shall contain a new value for the Publish Retransmit Interval Steps state of an element (see [Section 4.2.3.7](index-en.html#UUID-7135206d-7865-bc4a-d2ca-36f94d561b89 "4.2.3.7. Publish Retransmit Interval Steps")).

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.18. Config Model Publication Status

A Config Model Publication Status is an unacknowledged message used to report the model Publication state (see [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129")) of an outgoing message that is published by
the model.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status Code for the requesting message | M |
| ElementAddress | 16 | Address of the element | M |
| PublishAddress | 16 | Value of the publish address | M |
| AppKeyIndex | 12 | Index of the application key | M |
| CredentialFlag | 1 | Value of the Friendship Credential Flag | M |
| RFU | 3 | Reserved for Future Use | M |
| PublishTTL | 8 | Default TTL value for the outgoing messages | M |
| PublishPeriod | 8 | Period for periodic status publishing | M |
| PublishRetransmitCount | 3 | Number of retransmissions for each published message | M |
| PublishRetransmitIntervalSteps | 5 | Number of 50-millisecond steps between retransmissions | M |
| ModelIdentifier | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.100. Config Model Publication Status message structure

The Opcode field shall contain the opcode value for the Config Model Publication Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the last operation on Config Model Publication parameters. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field shall contain the unicast address of the element, all other address types are Prohibited.

The PublishAddress field shall contain the current Publish Address for the model. When using a Label UUID, the status message shall provide this value as the virtual address as defined in [Section 3.4.2.3](index-en.html#UUID-eab92f24-d710-17f2-304d-e62695a2e696 "3.4.2.3. Virtual address").

The AppKeyIndex is a global AppKey Index of the AppKey.

The CredentialFlag field shall contain the current value Publish Friendship Credentials Flag state (see [Section 4.2.3.4](index-en.html#UUID-9f0b2d51-1d32-c1e4-fabd-62b4bfb48257 "4.2.3.4. Publish Friendship Credentials Flag")).

The PublishTTL field shall contain the current value of the Publish TTL state (see [Section 4.2.3.5](index-en.html#UUID-bcd4eceb-9a71-bf4e-c238-27594178db23 "4.2.3.5. Publish TTL")) for outgoing messages published by the model within the element.

The PublishPeriod field shall contain the current value for the Publish Period state (see [Section 4.2.3.2](index-en.html#UUID-dddcf83b-90e5-0055-ad45-c91013cb89e4 "4.2.3.2. Publish Period")) for outgoing messages published by the model within the element.

The PublishRetransmitCount field shall contain a new value for the Publish Retransmit Count state of an element (see [Section 4.2.3.6](index-en.html#UUID-7ff4b704-2bb8-1887-7b33-8dd510069452 "4.2.3.6. Publish Retransmit Count")).

The PublishRetransmitIntervalSteps field shall contain a new value for the Publish Retransmit Interval Steps state of an element (see [Section 4.2.3.7](index-en.html#UUID-7135206d-7865-bc4a-d2ca-36f94d561b89 "4.2.3.7. Publish Retransmit Interval Steps")).

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.19. Config Model Subscription Add

A Config Model Subscription Add is an acknowledged message used to add an address to a Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Add message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Address | 2 | Value of the address | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.101. Config Model Subscription Add message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Add message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Address field shall contain the new address to be added to the Subscription List. The unassigned address, a unicast address, the all-nodes address, and a virtual address value of the Address field are Prohibited.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.20. Config Model Subscription Virtual Address Add

A Config Model Subscription Virtual Address Add is an acknowledged message used to add a Label UUID to a Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Virtual Address Add message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Label | 16 | Value of the Label UUID | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.102. Config Model Subscription Virtual Address Add message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Virtual Address Add message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Label field shall contain the Label UUID to be added to the Subscription List.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.21. Config Model Subscription Delete

A Config Model Subscription Delete is an acknowledged message used to delete a subscription address from the Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Delete message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Address | 2 | Value of the Address | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.103. Config Model Subscription Delete message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Delete message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Address field shall identify the address to be removed from the Subscription List. The unassigned address, a unicast address, the all-nodes address, and a virtual address value of the Address field are Prohibited.

The ModelIdentifier field either is a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.22. Config Model Subscription Virtual Address Delete

A Config Model Subscription Virtual Address Delete is an acknowledged message used to delete a Label UUID from the Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Virtual Address Delete message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Label | 16 | Value of the Label UUID | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.104. Config Model Subscription Virtual Address Delete message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Virtual Address Delete message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Label field shall contain the Label UUID to be removed from the Subscription List.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.23. Config Model Subscription Overwrite

A Config Model Subscription Overwrite is an acknowledged message used to discard the Subscription List and add an address to the cleared Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Overwrite message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Address | 2 | Value of the Address | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.105. Config Model Subscription Overwrite message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Overwrite message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Address field shall contain the address to be the only entry in the overwritten Subscription List. The unassigned address, a unicast address, the all-nodes address, and a virtual address value of the Address field are Prohibited.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.24. Config Model Subscription Virtual Address Overwrite

A Config Model Subscription Virtual Address Overwrite is an acknowledged message used to discard the Subscription List and add a Label UUID to the cleared Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Virtual Address Overwrite message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| Label | 16 | Value of the Label UUID | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.106. Config Model Subscription Virtual Address Overwrite message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Virtual Address Overwrite message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The Label field shall contain the Label UUID used as the only entry in the overwritten Subscription List.

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.25. Config Model Subscription Delete All

A Config Model Subscription Delete All is an acknowledged message used to discard the Subscription List of a model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

The response to a Config Model Subscription Delete All message is a Config Model Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.107. Config Model Subscription Delete All message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Delete All message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.26. Config Model Subscription Status

A Config Model Subscription Status is an unacknowledged message used to report a status of the operation on the Subscription List (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message. | M |
| ElementAddress | 2 | Address of the element | M |
| Address | 2 | Value of the address | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.108. Config Model Subscription Status message structure

The Opcode field shall contain the opcode value for the Config Model Subscription Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the last operation on the Subscription List. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The value of the Address field shall contain the address that was used to modify the Subscription List or the unassigned address. When referencing the Label UUID, the virtual address shall be used. The unicast address and the all-nodes address values of the Address field are Prohibited.

The ModelIdentifier field is a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.27. Config SIG Model Subscription Get

A Config SIG Model Subscription Get is an acknowledged message used to get the list of subscription addresses of a model within the element. This message is only for SIG Models.

The response to a Config SIG Model Subscription Get message is a Config SIG Model Subscription List message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 | SIG Model ID | M |

Table 4.109. Config SIG Model Subscription Get message structure

The Opcode field shall contain the opcode value for the Config SIG Model Subscription Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a SIG Model ID that shall identify the model within the element.

##### 4.3.2.28. Config SIG Model Subscription List

A Config SIG Model Subscription List is an unacknowledged message used to report all addresses from the Subscription List of the model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")). This message is only for
SIG Models.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 | SIG Model ID | M |
| Addresses | variable | A block of all addresses from the Subscription List | M |

Table 4.110. Config SIG Model Subscription List message structure

The Opcode field shall contain the opcode value for the Config SIG Model Subscription List message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the last operation on the Subscription List. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a SIG Model ID that shall identify the model within the element.

The Addresses field shall identify all addresses from the Subscription List of an element. When using a Label UUID, the status message shall provide the value of the virtual address as defined in [Section 3.4.2.3](index-en.html#UUID-eab92f24-d710-17f2-304d-e62695a2e696 "3.4.2.3. Virtual address"). The empty Subscription List results in Address field of zero length.

##### 4.3.2.29. Config Vendor Model Subscription Get

A Config Vendor Model Subscription Get is an acknowledged message used to get the list of subscription addresses of a model within the element. This message is only for Vendor Models.

The response to a Config Vendor Model Subscription Get message is a Config Vendor Model Subscription List message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 4 | Vendor Model ID | M |

Table 4.111. Config Vendor Model Subscription Get message structure

The Opcode field shall contain the opcode value for the Config Vendor Model Subscription Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.30. Config Vendor Model Subscription List

A Config Vendor Model Subscription List is an unacknowledged message used to report all addresses from the Subscription List of the model (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")). This message is only for
Vendor Models.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 4 | Vendor Model ID | M |
| Addresses | variable | A block of all addresses from the Subscription List | M |

Table 4.112. Config Vendor Model Subscription List message structure

The Opcode field shall contain the opcode value for the Config Vendor Model Subscription List message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the last operation on the Subscription List. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a Vendor Model ID that shall identify the model within the element.

The Addresses field shall identify all addresses from the Subscription List of an element. When using a Label UUID, the status message shall provide the value of the virtual address as defined in [Section 3.4.2.3](index-en.html#UUID-eab92f24-d710-17f2-304d-e62695a2e696 "3.4.2.3. Virtual address"). The empty Subscription List results in Address field of zero length.

##### 4.3.2.31. Config NetKey Add

A Config NetKey Add is an acknowledged message used to add a NetKey to a NetKey List (see [Section 4.2.5](index-en.html#UUID-a4e051bc-0765-7678-6187-aee13f713495 "4.2.5. NetKey List")) on a node. The added NetKey is then used by the node to authenticate and decrypt
messages it receives, as well as authenticate and encrypt messages it sends.

The response to a Config NetKey Add message is a Config NetKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | NetKey Index | M |
| NetKey | 16 | NetKey | M |

Table 4.113. Config NetKey Add message structure

The Opcode field shall contain the opcode value for the Config NetKey Add message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The NetKey field shall contain the NetKey.

##### 4.3.2.32. Config NetKey Update

A Config NetKey Update is an acknowledged message used to update a NetKey on a node. The updated NetKey is then used by the node to authenticate and decrypt messages it receives, as well as authenticate and encrypt messages it sends, as defined by the Key Refresh procedure (see [Section 3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")).

The response to a Config NetKey Update message is a Config NetKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |
| NetKey | 16 | NetKey | M |

Table 4.114. Config NetKey Update message structure

The Opcode field shall contain the opcode value for the Config NetKey Update message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The NetKey field shall contain the NetKey.

##### 4.3.2.33. Config NetKey Delete

A Config NetKey Delete is an acknowledged message used to delete a NetKey on a NetKey List from a node.

The response to a Config NetKey Delete message is a Config NetKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |

Table 4.115. Config NetKey Delete message structure

The Opcode field shall contain the opcode value for the Config NetKey Delete message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.34. Config NetKey Status

A Config NetKey Status is an unacknowledged message used to report the status of the operation on the NetKey List.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndex | 2 | Index of the NetKey | M |

Table 4.116. Config NetKey Status message structure

The Opcode field shall contain the opcode value for the Config NetKey Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the last operation on the NetKey List. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes"). The Status Code shall be Success if the received request was redundant (add of an identical existing key, update of an identical updated key, or delete of a non-existent key), with no further action taken.

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.35. Config NetKey Get

A Config NetKey Get is an acknowledged message used to report all NetKeys known to the node.

The response to a Config NetKey Get message is a Config NetKey List message.

The structure of the Config NetKey Get message is defined in [Table 4.117](index-en.html#UUID-d20bd7cd-ef2c-2c0b-d536-2fd541e8b587_Table_4.117 "Table 4.117. Config NetKey Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.117. Config NetKey Get message structure

The Opcode field shall contain the opcode value for the Config NetKey Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.36. Config NetKey List

A Config NetKey List is an unacknowledged message reporting all NetKeys known to the node.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndexes | variable | A list of NetKey Indexes known to the node | M |

Table 4.118. Config NetKey List message structure

The Opcode field shall contain the opcode value for the Config NetKey List message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndexes field shall contain all NetKey Indexes that are known to the node. The NetKey Indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.37. Config AppKey Add

A Config AppKey Add is an acknowledged message used to add an AppKey to the AppKey List on a node and bind it to the NetKey identified by NetKeyIndex. The added AppKey can be used by the node only as a pair with the specified NetKey. The AppKey is used to authenticate and decrypt messages it receives, as well as authenticate
and encrypt messages it sends.

The response to a Config AppKey Add message is a Config AppKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| NetKeyIndexAndAppKeyIndex | 3 | Index of the NetKey and index of the AppKey | M |
| AppKey | 16 | AppKey value | M |

Table 4.119. Config AppKey Add message structure

The Opcode field shall contain the opcode value for the Config AppKey Add message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndexAndAppKeyIndex field contains two indexes that shall identify the global NetKey Index of the NetKey and the global AppKey Index of the AppKey. These two indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes") using NetKey Index as first key index and AppKey Index as second key index.

The AppKey field shall contain the AppKey value identified by the AppKeyIndex.

##### 4.3.2.38. Config AppKey Update

A Config AppKey Update is an acknowledged message used to update an AppKey value on the AppKey List on a node. The updated AppKey is used by the node to authenticate and decrypt messages it receives, as well as authenticate and encrypt messages it sends, as defined by the Key Refresh procedure (see [Section 3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")).

The response to an Config AppKey Update message is an Config AppKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| NetKeyIndexAndAppKeyIndex | 3 | Index of the NetKey and index of the AppKey | M |
| AppKey | 16 | New AppKey value | M |

Table 4.120. Config AppKey Update message structure

The Opcode field shall contain the opcode value for the Config AppKey Update message defined in the Assigned Numbers document [4].

The NetKeyIndexAndAppKeyIndex field contains two indexes that shall identify the global NetKey Index of the NetKey and the global AppKey Index of the AppKey. These two indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes") using NetKey Index as first key index and AppKey Index as second key index. The AppKeyIndex shall be bound to the NetKeyIndex.

The AppKey field shall contain the new value of the AppKey, identified by the AppKeyIndex.

##### 4.3.2.39. Config AppKey Delete

A Config AppKey Delete is an acknowledged message used to delete an AppKey from the AppKey List on a node.

The response to a Config AppKey Delete message is a Config AppKey Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndexAndAppKeyIndex | 3 | Index of the NetKey and index of the AppKey | M |

Table 4.121. Config AppKey Delete message structure

The Opcode field shall contain the opcode value for the Config AppKey Delete message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndexAndAppKeyIndex field contains two indexes that shall identify the global NetKey Index of the NetKey and the global AppKey Index of the AppKey. These two indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes") using NetKey Index as first key index and AppKey Index as second key index.

##### 4.3.2.40. Config AppKey Status

A Config AppKey Status is an unacknowledged message used to report a status for the requesting message, based on the NetKey Index identifying the NetKey on the NetKey List and on the AppKey Index identifying the AppKey on the AppKey List.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndexAndAppKeyIndex | 3 | Index of the NetKey and index of the AppKey | M |

Table 4.122. Config AppKey Status message structure

The Opcode field shall contain the opcode value for the Config AppKey Status message defined in the Assigned Numbers document [4].

The Status field shall identify the Status Code for the last operation on the AppKey List. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes"). The Status Code shall be Success if the received request was redundant (add of an identical existing key, update of an identical updated key, or delete of a non-existent key), with no further action taken.

The NetKeyIndexAndAppKeyIndex field contains two indexes that shall identify the global NetKey Index of the NetKey and the global AppKey Index of the AppKey. These two indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes") using NetKey Index as first key index and AppKey Index as second key index.

##### 4.3.2.41. Config AppKey Get

An AppKey Get is an acknowledged message used to report all AppKeys bound to the NetKey.

The response to a Config AppKey Get message is a Config AppKey List message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |

Table 4.123. Config AppKey Get message structure

The Opcode field shall contain the opcode value for the Config AppKey Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.42. Config AppKey List

A Config AppKey List is an unacknowledged message reporting all AppKeys that are bound to the NetKey.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndex | 2 | NetKey Index of the NetKey that the AppKeys are bound to | M |
| AppKeyIndexes | variable | A list of AppKey indexes that are bound to the NetKey identified by NetKeyIndex | M |

Table 4.124. Config AppKey List message structure

The Opcode field shall contain the opcode value for the Config AppKey List message defined in the Assigned Numbers document [4].

The Status field shall identify the Status Code for the last operation on the AppKey of the NetKey. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey to which the AppKeys are bound. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The AppKeyIndexes field shall contain all AppKey indexes that are bound to the NetKey. The AppKey indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.43. Config Node Identity Get

A Config Node Identity Get is an acknowledged message used to get the current Node Identity state for a subnet (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")).

The response to a Config Node Identity Get message is a Config Node Identity Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |

Table 4.125. Config Node Identity Get message structure

The Opcode field shall contain the opcode value for the Config Node Identity Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.44. Config Node Identity Set

A Config Node Identity Set is an acknowledged message used to set the current Node Identity state for a subnet (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")).

The response to a Config Node Identity Set message is a Config Node Identity Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |
| Identity | 1 | New Node Identity state | M |

Table 4.126. Config Node Identity Set message structure

The Opcode field shall contain the opcode value for the Config Node Identity Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey of the Node Identity state. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Identity field shall provide the new Node Identity state of the NetKey (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")).

##### 4.3.2.45. Config Node Identity Status

A Config Node Identity Status is an unacknowledged message used to report the current Node Identity state for a subnet (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndex | 2 | Index of the NetKey | M |
| Identity | 1 | Node Identity state | M |

Table 4.127. Config Node Identity Status message structure

The Opcode field shall contain the opcode value for the Config Node Identity Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey of the Node Identity state. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Identity field shall provide the current Node Identity state for a subnet (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")).

##### 4.3.2.46. Config Model App Bind

A Config Model App Bind is an acknowledged message used to bind an AppKey to a model.

The response to a Config Model App Bind message is a Config Model App Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| AppKeyIndex | 2 | Index of the AppKey | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.128. Config Model App Bind message structure

The Opcode field shall contain the opcode value for the Config Model App Bind message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The AppKeyIndex field is an index that shall identify the global AppKey Index of the AppKey. The AppKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The ModelIdentifier field is either a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.47. Config Model App Unbind

A Config Model App Unbind is an acknowledged message used to remove the binding between an AppKey and a model.

The response to a Config Model App Unbind message is a Config Model App Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| AppKeyIndex | 2 | Index of the AppKey | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.129. Config Model App Unbind message structure

The Opcode field shall contain the opcode value for the Config Model App Unbind message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The AppKeyIndex field is an index that shall identify the global AppKey Index of the AppKey. The AppKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The ModelIdentifier field is a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.48. Config Model App Status

A Config Model App Status is an unacknowledged message used to report a status for the requesting message, based on the element address, the AppKeyIndex identifying the AppKey on the AppKey List, and the ModelIdentifier.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| ElementAddress | 2 | Address of the element | M |
| AppKeyIndex | 2 | Index of the AppKey | M |
| ModelIdentifier | 2 or 4 | SIG Model ID or Vendor Model ID | M |

Table 4.130. Config Model App Status message structure

The Opcode field shall contain the opcode value for the Config Model App Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes"). The Status
Code shall be Success if the received request was redundant (bind request of existing binding, or unbind of a non-existing binding), with no further action taken.

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The AppKeyIndex field is an index that shall identify the global AppKey Index of the AppKey. The AppKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The ModelIdentifier field is a SIG Model ID or a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.49. Config SIG Model App Get

A Config SIG Model App Get is an acknowledged message used to request report of all AppKeys bound to the SIG Model.

The response to a Config SIG Model App Get message is a Config SIG Model App List message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 | SIG Model ID | M |

Table 4.131. Config SIG Model App Get message structure

The Opcode field shall contain the opcode value for the Config SIG Model App Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a SIG Model ID that shall identify the model within the element.

##### 4.3.2.50. Config SIG Model App List

A Config SIG Model App List is an unacknowledged message used to report all AppKeys bound to the SIG Model.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 2 | SIG Model ID | M |
| AppKeyIndexes | variable | All AppKey indexes bound to the Model | M |

Table 4.132. Config SIG Model App List message structure

The Opcode field shall contain the opcode value for the Config SIG Model App List message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a SIG Model ID that shall identify the SIG model within the element.

The AppKeyIndexes field shall contain all AppKey indexes that are bound to an instance of a model. The AppKey indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.51. Config Vendor Model App Get

A Config Vendor Model App Get is an acknowledged message used to request report of all AppKeys bound to the model. This message is only for Vendor Models.

The response to a Config Vendor Model App Get message is a Config Vendor Model App List message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 4 | Vendor Model ID | M |

Table 4.133. Config Vendor Model App Get message structure

The Opcode field shall contain the opcode value for the Config Vendor Model App Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a Vendor Model ID that shall identify the model within the element.

##### 4.3.2.52. Config Vendor Model App List

A Config Vendor Model App List is an unacknowledged message used to report indexes of all AppKeys bound to the model. This message is only for Vendor Models.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| ElementAddress | 2 | Address of the element | M |
| ModelIdentifier | 4 | Vendor Model ID | M |
| AppKeyIndexes | variable | Indexes of all AppKeys bound to the model | M |

Table 4.134. Config Vendor Model App List message structure

The Opcode field shall contain the opcode value for the Config Vendor Model App List message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The ElementAddress field is the unicast address of the element, all other address types are Prohibited.

The ModelIdentifier field is a Vendor Model ID that shall identify the model within the element.

The AppKeyIndexes field shall contain indexes of all AppKeys that are bound to an instance of a model. The AppKey indexes shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.53. Config Node Reset

A Config Node Reset is an acknowledged message used to reset a node (other than a Provisioner) and remove it from the network.

The response to a Config Node Reset message is a Config Node Reset Status message.

The structure of the Config Node Reset message is defined in [Table 4.135](index-en.html#UUID-eb5b2ee3-4f0a-9f75-f4dc-4e61cc4f56a9_Table_4.135 "Table 4.135. Config Node Reset message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.135. Config Node Reset message structure

The Opcode field shall contain the opcode value for the Config Node Reset message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.54. Config Node Reset Status

A Config Node Reset Status is an unacknowledged message used to acknowledge that an element has received a Config Node Reset message.

The structure of the Config Node Reset Status message is defined in [Table 4.136](index-en.html#UUID-1b8cb385-a642-2f66-7cbc-8eefb8da8fa4_Table_4.136 "Table 4.136. Config Node Reset Status message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.136. Config Node Reset Status message structure

The Opcode field shall contain the opcode value for the Config Node Reset Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.55. Config Friend Get

A Config Friend Get is an acknowledged message used to get the current Friend state of a node (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")).

The response to a Config Friend Get message is a Config Friend Status message.

The structure of the Config Friend Get message is defined in [Table 4.137](index-en.html#UUID-20541b40-c66f-e51b-fb0c-426814a34842_Table_4.137 "Table 4.137. Config Friend Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.137. Config Friend Get message structure

The Opcode field shall contain the opcode value for the Config Friend Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.56. Config Friend Set

A Config Friend Set is an acknowledged message used to set the Friend state of a node (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")).

The response to a Config Friend Set message is a Config Friend Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Friend | 1 | New Friend state | M |

Table 4.138. Config Friend Set message structure

The Opcode field shall contain the opcode value for the Config Friend Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Friend field shall provide the new Friend state of the node (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")).

##### 4.3.2.57. Config Friend Status

A Config Friend Status is an unacknowledged message used to report the current Friend state of a node (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Friend | 1 | Friend state | M |

Table 4.139. Config Friend Status message structure

The Opcode field shall contain the opcode value for the Config Friend Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Friend field shall provide the current Friend state of the node (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")).

##### 4.3.2.58. Config Key Refresh Phase Get

A Config Key Refresh Phase Get is an acknowledged message used to get the current Key Refresh Phase state of the identified network key.

The response to a Config Key Refresh Phase Get message is a Config Key Refresh Phase Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | NetKey Index | M |

Table 4.140. Config Key Refresh Phase Get message structure

The Opcode field shall contain the opcode value for the Config Key Refresh Phase Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.59. Config Key Refresh Phase Set

A Config Key Refresh Phase Set is an acknowledged message used to set the Key Refresh Phase state of the identified network key (see [Section 4.2.15](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356 "4.2.15. Key Refresh Phase")).

The response to a Config Key Refresh Phase Set message is a Config Key Refresh Phase Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | NetKey Index | M |
| Transition | 1 | New Key Refresh Phase Transition | M |

Table 4.141. Config Key Refresh Phase Set message structure

The Opcode field shall contain the opcode value for the Config Key Refresh Phase Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Transition field shall identify the Key Refresh Phase Transitions (see [Section 4.2.15](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356 "4.2.15. Key Refresh Phase"), [Table 4.31](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356_Table_4.31 "Table 4.31. Controllable Key Refresh transition values")) allowed for each given starting state. All other transition values are Prohibited.

##### 4.3.2.60. Config Key Refresh Phase Status

A Config Key Refresh Phase Status is an unacknowledged message used to report the current Key Refresh Phase state of the identified network key (see [Section 4.2.15](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356 "4.2.15. Key Refresh Phase")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndex | 2 | NetKey Index | M |
| Phase | 1 | Key Refresh Phase State | M |

Table 4.142. Config Key Refresh Phase Status message structure

The Opcode field shall contain the opcode value for the Config Key Refresh Phase Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes"). The Status
Code shall be Success if the received request was redundant (the requested phase transition has already occurred), with no further action taken.

The NetKeyIndex field shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Phase field shall identify the Key Refresh Phase state for the node, as defined in Key Refresh Phase (see [Section 4.2.15](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356 "4.2.15. Key Refresh Phase")).

##### 4.3.2.61. Config Heartbeat Publication Get

A Config Heartbeat Publication Get is an acknowledged message used to get the current Heartbeat Publication state of an element (see [Section 4.2.18](index-en.html#UUID-77d5df26-1351-cc93-d733-38817a094198 "4.2.18. Heartbeat Publication")).

The response to a Config Heartbeat Publication Get message is a Config Heartbeat Publication Status message.

The structure of the Config Heartbeat Publication Get message is defined in [Table 4.143](index-en.html#UUID-13ae9e1c-3e5a-5e7e-d07a-bf01dd8a5c23_Table_4.143 "Table 4.143. Config Heartbeat Publication Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.143. Config Heartbeat Publication Get message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Publication Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.62. Config Heartbeat Publication Set

A Config Heartbeat Publication Set is an acknowledged message used to set the current Heartbeat Publication state of an element (see [Section 4.2.18](index-en.html#UUID-77d5df26-1351-cc93-d733-38817a094198 "4.2.18. Heartbeat Publication")).

The response to a Config Heartbeat Publication Set message is a Config Heartbeat Publication Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Destination | 2 | Destination address for Heartbeat messages | M |
| CountLog | 1 | Number of Heartbeat messages to be sent | M |
| PeriodLog | 1 | Period for sending Heartbeat messages | M |
| TTL | 1 | TTL to be used when sending Heartbeat messages | M |
| Features | 2 | Bit field indicating features that trigger Heartbeat messages when changed | M |
| NetKeyIndex | 2 | NetKey Index | M |

Table 4.144. Config Heartbeat Publication Set message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Publication Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Destination field shall identify the Heartbeat Publication Destination state (see [Section 4.2.18.1](index-en.html#UUID-20690ce1-f558-01d4-53ec-97f33eabc3bb "4.2.18.1. Heartbeat Publication Destination")).

The CountLog field shall identify the Heartbeat Publication Count Log representation of the Heartbeat Publication Count state (see [Section 4.2.18.2](index-en.html#UUID-5d8bca5b-84ee-a591-6c62-e409da0a03c1 "4.2.18.2. Heartbeat Publication Count")).

The PeriodLog field shall identify the Heartbeat Publication Period Log state (see [Section 4.2.18.3](index-en.html#UUID-c06973e0-b8ab-6b50-1cd1-a11015e5eaf1 "4.2.18.3. Heartbeat Publication Period Log")).

The TTL field shall identify the Heartbeat Publication TTL state (see [Section 4.2.18.4](index-en.html#UUID-55ab89ce-7da2-5b17-634d-ad3a930eb7b0 "4.2.18.4. Heartbeat Publication TTL")).

The Features field shall identify the Heartbeat Publication Features state (see [Section 4.2.18.5](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf "4.2.18.5. Heartbeat Publication Features")).

The NetKeyIndex field shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.63. Config Heartbeat Publication Status

A Config Heartbeat Publication Status is an unacknowledged message used to report the Heartbeat Publication state of a node (see [Section 4.2.18](index-en.html#UUID-77d5df26-1351-cc93-d733-38817a094198 "4.2.18. Heartbeat Publication")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| Destination | 2 | Destination address for Heartbeat messages | M |
| CountLog | 1 | Number of Heartbeat messages remaining to be sent | M |
| PeriodLog | 1 | Period for sending Heartbeat messages | M |
| TTL | 1 | TTL to be used when sending Heartbeat messages | M |
| Features | 2 | Bit field indicating features that trigger Heartbeat messages when changed | M |
| NetKeyIndex | 2 | NetKey Index | M |

Table 4.145. Config Heartbeat Publication Status message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Publication Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The Destination field shall identify the Heartbeat Publication Destination state (see [Section 4.2.18.1](index-en.html#UUID-20690ce1-f558-01d4-53ec-97f33eabc3bb "4.2.18.1. Heartbeat Publication Destination")).

The CountLog field shall identify the Heartbeat Publication Count Log representation of the Heartbeat Publication Count state (see [Section 4.2.18.2](index-en.html#UUID-5d8bca5b-84ee-a591-6c62-e409da0a03c1 "4.2.18.2. Heartbeat Publication Count")).

The PeriodLog field shall identify the Heartbeat Publication Period Log state (see [Section 4.2.18.3](index-en.html#UUID-c06973e0-b8ab-6b50-1cd1-a11015e5eaf1 "4.2.18.3. Heartbeat Publication Period Log")).

The TTL field shall identify the Heartbeat Publication TTL state (see [Section 4.2.18.4](index-en.html#UUID-55ab89ce-7da2-5b17-634d-ad3a930eb7b0 "4.2.18.4. Heartbeat Publication TTL")).

The Features field shall identify the Heartbeat Publication Features state (see Section [4.2.18.5](index-en.html#UUID-47e6d33f-106d-5680-590d-d59a5ed2f7bf "4.2.18.5. Heartbeat Publication Features")).

The NetKeyIndex field shall identify the global NetKey Index of the NetKey used to publish heartbeats. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.2.64. Config Heartbeat Subscription Get

A Config Heartbeat Subscription Get is an acknowledged message used to get the current Heartbeat Subscription state of an element (see [Section 4.2.19](index-en.html#UUID-23a5a1db-9d53-1bc0-0385-8da5bc458f9d "4.2.19. Heartbeat Subscription")).

The response to a Config Heartbeat Subscription Get message is a Config Heartbeat Subscription Status message.

The structure of the Config Heartbeat Subscription Get message is defined in [Table 4.146](index-en.html#UUID-2af24fce-7bc1-b6f6-a0c0-ad1c70a0c591_Table_4.146 "Table 4.146. Config Heartbeat Subscription Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.146. Config Heartbeat Subscription Get message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Subscription Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.65. Config Heartbeat Subscription Set

A Config Heartbeat Subscription Set is an acknowledged message used to set the current Heartbeat Subscription state of an element (see [Section 4.2.19](index-en.html#UUID-23a5a1db-9d53-1bc0-0385-8da5bc458f9d "4.2.19. Heartbeat Subscription")).

The response to a Config Heartbeat Subscription Set message is a Config Heartbeat Subscription Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Source | 2 | Source address for Heartbeat messages | M |
| Destination | 2 | Destination address for Heartbeat messages | M |
| PeriodLog | 1 | Period for receiving Heartbeat messages | M |

Table 4.147. Config Heartbeat Subscription Set message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Subscription Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Source field shall identify the Heartbeat Subscription Source state (see [Section 4.2.19.1](index-en.html#UUID-78bba213-943c-bd97-29c5-f10c37de1ceb "4.2.19.1. Heartbeat Subscription Source")).

The Destination field shall identify the Heartbeat Subscription Destination state (see [Section 4.2.19.2](index-en.html#UUID-61cb08b9-daac-faf6-8d0f-db63cd4e545f "4.2.19.2. Heartbeat Subscription Destination")).

The PeriodLog field shall identify the Heartbeat Subscription Period state (see [Section 4.2.19.4](index-en.html#UUID-ac2a794a-cec0-a399-4c1b-d844f78935c4 "4.2.19.4. Heartbeat Subscription Period")).

##### 4.3.2.66. Config Heartbeat Subscription Status

A Config Heartbeat Subscription Status is an unacknowledged message used to report the Heartbeat Subscription state of a node (see [Section 4.2.19](index-en.html#UUID-23a5a1db-9d53-1bc0-0385-8da5bc458f9d "4.2.19. Heartbeat Subscription")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| Source | 2 | Source address for Heartbeat messages | M |
| Destination | 2 | Destination address for Heartbeat messages | M |
| PeriodLog | 1 | Remaining Period for processing Heartbeat messages | M |
| CountLog | 1 | Number of Heartbeat messages received | M |
| MinHops | 1 | Minimum hops when receiving Heartbeat messages | M |
| MaxHops | 1 | Maximum hops when receiving Heartbeat messages | M |

Table 4.148. Config Heartbeat Subscription Status message structure

The Opcode field shall contain the opcode value for the Config Heartbeat Subscription Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The Source field shall identify the Heartbeat Subscription Source state (see [Section 4.2.19.1](index-en.html#UUID-78bba213-943c-bd97-29c5-f10c37de1ceb "4.2.19.1. Heartbeat Subscription Source")).

The Destination field shall identify the Heartbeat Subscription Destination state (see [Section 4.2.19.2](index-en.html#UUID-61cb08b9-daac-faf6-8d0f-db63cd4e545f "4.2.19.2. Heartbeat Subscription Destination")).

The PeriodLog field shall identify the Heartbeat Subscription Period Log state (see [Section 4.2.19.4](index-en.html#UUID-ac2a794a-cec0-a399-4c1b-d844f78935c4 "4.2.19.4. Heartbeat Subscription Period")).

The CountLog field shall identify the Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state (see [Section 4.2.19.3](index-en.html#UUID-d91f14d6-7e24-f2e8-9edb-01023b0580ea "4.2.19.3. Heartbeat Subscription Count")).

The MinHops field shall identify the Heartbeat Subscription Min Hops state (see [Section 4.2.19.5](index-en.html#UUID-8e89c52c-df13-a8a8-9794-7f1b4a227cdf "4.2.19.5. Heartbeat Subscription Min Hops")).

The MaxHops field shall identify the Heartbeat Subscription Max Hops state (see [Section 4.2.19.6](index-en.html#UUID-c7735893-2088-d78a-f3d5-c1827aaef6c1 "4.2.19.6. Heartbeat Subscription Max Hops")).

##### 4.3.2.67. Config Low Power Node PollTimeout Get

A Config Low Power Node PollTimeout Get is an acknowledged message used to get the current value of PollTimeout timer of the Low Power node within a Friend node (see [Section 3.6.6.1](index-en.html#UUID-8e110900-697a-24e0-f873-8e97c8a1e861 "3.6.6.1. Functional overview")). The message is sent to a Friend node that has claimed to be handling messages by sending acknowledgments (ACKs) on behalf of the indicated Low Power node. This message should only be sent to a node that has the Friend feature supported and enabled.

The response to a Config Low Power Node PollTimeout Get message is a Config Low Power Node PollTimeout Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| LPNAddress | 2 | The unicast address of the Low Power node | M |

Table 4.149. Config Low Power Node PollTimeout Get message structure

The Opcode field shall contain the opcode value for the Config Low Power Node PollTimeout Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The LPNAddress field shall contain the primary unicast address of the Low Power node within a Friend node.

##### 4.3.2.68. Config Low Power Node PollTimeout Status

A Config Low Power Node PollTimeout Status is an unacknowledged message used to report the current value of the PollTimeout timer of the Low Power node within a Friend node.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| LPNAddress | 2 | The unicast address of the Low Power node | M |
| PollTimeout | 3 | The current value of the PollTimeout timer of the Low Power node | M |

Table 4.150. Config Low Power Node PollTimeout Status message structure

The Opcode field shall contain the opcode value for the Config Low Power Node PollTimeout Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The LPNAddress field shall contain the primary unicast address of the Low Power node.

The PollTimeout field shall contain the current value of the PollTimeout timer of the Low Power node within a Friend node, or 0x000000 if the node is not a Friend node for the Low Power node identified by LPNAddress.

##### 4.3.2.69. Config Network Transmit Get

A Config Network Transmit Get is an acknowledged message used to get the current Network Transmit state of a node (see [Section 4.2.20](index-en.html#UUID-dccb10ac-b38d-031d-bf38-c007347342db "4.2.20. Network Transmit")).

The response to a Config Network Transmit Get message is a Config Network Transmit Status message.

The structure of the Config Network Transmit Get message is defined in [Table 4.151](index-en.html#UUID-cc9e93d0-8260-9d50-ef07-9c82988c1b90_Table_4.151 "Table 4.151. Config Network Transmit Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.151. Config Network Transmit Get message structure

The Opcode field shall contain the opcode value for the Config Network Transmit Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.2.70. Config Network Transmit Set

A Config Network Transmit Set is an acknowledged message used to set the Network Transmit state of a node (see [Section 4.2.20](index-en.html#UUID-dccb10ac-b38d-031d-bf38-c007347342db "4.2.20. Network Transmit")).

The response to a Config Network Transmit Set message is a Config Network Transmit Status message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetworkTransmitCount | 3 | Number of transmissions for each Network PDU originating from the node | M |
| NetworkTransmitIntervalSteps | 5 | Number of 10-millisecond steps between transmissions | M |

Table 4.152. Config Network Transmit Set message structure

The Opcode field shall contain the opcode value for the Config Network Transmit Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetworkTransmitCount field shall contain a new value for the Network Transmit Count state of a node (see [Section 4.2.20.1](index-en.html#UUID-5d762ef1-22e1-0358-fc5d-56c4f6604c66 "4.2.20.1. Network Transmit Count")).

The NetworkTransmitIntervalSteps field shall contain a new value for the Network Transmit Interval Steps state of a node (see [Section 4.2.20.2](index-en.html#UUID-12c9df52-76f3-a189-ccb8-1d2501c5e658 "4.2.20.2. Network Transmit Interval Steps")).

##### 4.3.2.71. Config Network Transmit Status

A Config Network Transmit Status is an unacknowledged message used to report the current Network Transmit state of a node (see [Section 4.2.20](index-en.html#UUID-dccb10ac-b38d-031d-bf38-c007347342db "4.2.20. Network Transmit")).

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetworkTransmitCount | 3 | Number of transmissions for each Network PDU originating from the node | M |
| NetworkTransmitIntervalSteps | 5 | Number of 10-millisecond steps between transmissions | M |

Table 4.153. Config Network Transmit Status message structure

The Opcode field shall contain the opcode value for the Config Network Transmit Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetworkTransmitCount field shall contain a new value for the Network Transmit Count state of a node (see [Section 4.2.20.1](index-en.html#UUID-5d762ef1-22e1-0358-fc5d-56c4f6604c66 "4.2.20.1. Network Transmit Count")).

The NetworkTransmitIntervalSteps field shall contain a new value for the Network Transmit Interval Steps state of a node (see [Section 4.2.20.2](index-en.html#UUID-12c9df52-76f3-a189-ccb8-1d2501c5e658 "4.2.20.2. Network Transmit Interval Steps")).

#### 4.3.3. Health messages

Health messages are used to monitor states that determine the physical condition of a node.

##### 4.3.3.1. Health Current Status

A Health Current Status is an unacknowledged message used to report the Current Health state of an element (see [Section 4.2.16.1](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650 "4.2.16.1. Current Fault")). The message may contain several Fault fields,
depending on the number of concurrently present fault conditions. If no Fault fields are present, it means no fault condition exists on an element.

The message uses a single-octet opcode to maximize the size of the FaultArray.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| Test ID | 1 | Identifier of a most recently performed test | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |
| FaultArray | N | The FaultArray field contains a sequence of 1-octet fault values | M |

Table 4.154. Health Current Status message structure

The Opcode field shall contain the opcode value for the Health Current Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Test ID field identifies a most recently performed test by the element.

The Company ID field is a Bluetooth assigned Company Identifier [[4](index-en.html#idp254746)]. It shall be used to resolve vendor-specific fault codes in the Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

The FaultArray field contains a sequence of fault values, as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.2. Health Fault Get

A Health Fault Get is an acknowledged message used to get the current Registered Fault state identified by Company ID of an element (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")).

The response to a Health Fault Get message is a Health Fault Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |

Table 4.155. Health Fault Get message structure

The Opcode field shall contain the opcode value for the Health Fault Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Company ID field is a Bluetooth assigned Company identifier [[4](index-en.html#idp254746)]. It shall be used to resolve specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.3. Health Fault Clear Unacknowledged

A Health Fault Clear Unacknowledged is an unacknowledged message used to clear the current Registered Fault state identified by Company ID of an element (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |

Table 4.156. Health Fault Clear Unacknowledged message structure

The Opcode field shall contain the opcode value for the Health Fault Clear Unacknowledged message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Company ID field is a Bluetooth assigned Company identifier [[4](index-en.html#idp254746)]. It shall be used to resolve specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.4. Health Fault Clear

A Health Fault Clear is an acknowledged message used to clear the current Registered Fault state identified by Company ID of an element (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")).

The response to a Health Fault Clear message is a Health Fault Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |

Table 4.157. Health Fault Clear message structure

The Opcode field shall contain the opcode value for the Health Fault Clear message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Company ID field is a Bluetooth assigned Company identifier [[4](index-en.html#idp254746)]. It shall be used to resolve specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.5. Health Fault Test

A Health Fault Test is an acknowledged message used to invoke a self-test procedure of an element. The procedure is implementation specific and may result in changing the Health Fault state of an element (see [Section 4.2.16](index-en.html#UUID-17941ebc-d1a6-fe23-086c-c35ca7df2f26 "4.2.16. Health Fault")).

The response to a Health Fault Test message is a Health Fault Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Test ID | 1 | Identifier of a specific test to be performed | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |

Table 4.158. Health Fault Test message structure

The Opcode field shall contain the opcode value for the Health Fault Test message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Test ID field identifies a test the element should perform.

The Company ID field is a Bluetooth assigned Company Identifier [[4](index-en.html#idp254746)]. It shall be used to resolve vendor-specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.6. Health Fault Test Unacknowledged

A Health Fault Test Unacknowledged is an unacknowledged message used to invoke a self-test procedure of an element. The procedure is implementation specific and may result in changing the Health Fault state of an element (see [Section 4.2.16](index-en.html#UUID-17941ebc-d1a6-fe23-086c-c35ca7df2f26 "4.2.16. Health Fault")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Test ID | 1 | Identifier of a specific test to be performed | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |

Table 4.159. Health Fault Test Unacknowledged message structure

The Opcode field shall contain the opcode value for the Health Fault Test Unacknowledged message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Test ID field identifies a test the element should perform.

The Company ID field is a Bluetooth assigned Company Identifier [[4](index-en.html#idp254746)]. It shall be used to resolve vendor-specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.7. Health Fault Status

A Health Fault Status is an unacknowledged message used to report the current Registered Fault state of an element (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")). The message may contain several Fault
fields, depending on the number of concurrently present fault conditions. If no Fault fields are present, it means no registered fault condition exists on an element.

The message uses a single-octet opcode to maximize the size of the FaultArray.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 1 | The message opcode | M |
| Test ID | 1 | Identifier of a most recently performed test | M |
| Company ID | 2 | 16-bit Bluetooth assigned Company Identifier | M |
| FaultArray | N | The FaultArray field contains a sequence of 1-octet fault values | M |

Table 4.160. Health Fault Status message structure

The Opcode field shall contain the opcode value for the Health Fault Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Test ID field identifies a most recently performed test by the element.

The Company ID field is a Bluetooth assigned Company Identifier [[4](index-en.html#idp254746)]. It shall be used to resolve vendor-specific fault codes as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

The FaultArray field contains a sequence of fault values, as specified in Bluetooth assigned Health Fault values [[4](index-en.html#idp254746)].

##### 4.3.3.8. Health Period Get

A Health Period Get is an acknowledged message used to get the current Health Fast Period Divisor state of an element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

The response to a Health Period Get message is a Health Period Status message.

The structure of the Health Period Get message is defined in [Table 4.161](index-en.html#UUID-db745d4a-1dc1-6589-0b21-5ea1039fbb54_Table_4.161 "Table 4.161. Health Period Get message structure").

| Field | Size  (octets) | Description | **Req.** |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.161. Health Period Get message structure

The Opcode field shall contain the opcode value for the Health Period Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.3.9. Health Period Set Unacknowledged

A Health Period Set Unacknowledged is an unacknowledged message used to set the current Health Fast Period Divisor state of an element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| FastPeriodDivisor | 1 | Divider for the Publish Period. Modified Publish Period is used for sending Current Health Status messages when there are active faults to communicate | M |

Table 4.162. Health Period Set Unacknowledged message structure

The Opcode field shall contain the opcode value for the Health Period Set Unacknowledged message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The FastPeriodDivisor field shall identify the Health Fast Period Divisor state for the element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

##### 4.3.3.10. Health Period Set

A Health Period Set is an acknowledged message used to set the current Health Fast Period Divisor state of an element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

The response to a Health Period Set message is a Health Period Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| FastPeriodDivisor | 1 | Divider for the Publish Period. Modified Publish Period is used for sending Current Health Status messages when there are active faults to communicate | M |

Table 4.163. Health Period Set message structure

The Opcode field shall contain the opcode value for the Health Period Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The FastPeriodDivisor field shall identify the Health Fast Period Divisor state for the element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

##### 4.3.3.11. Health Period Status

A Health Period Status is an unacknowledged message used to report the Health Fast Period Divisor state of an element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| FastPeriodDivisor | 1 | Divider for the Publish Period. Modified Publish Period is used for sending Current Health Status messages when there are active faults to communicate | M |

Table 4.164. Health Period Status message structure

The Opcode field shall contain the opcode value for the Health Period Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The FastPeriodDivisor field shall identify the Health Fast Period Divisor state for the element (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")).

##### 4.3.3.12. Health Attention Get

A Health Attention Get is an acknowledged message used to get the current Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

The response to a Health Attention Get message is an Attention Status message.

The structure of the Health Attention Get message is defined in [Table 4.165](index-en.html#UUID-fcfa6fca-6f36-ff67-fa0a-202ba5cd1622_Table_4.165 "Table 4.165. Health Attention Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.165. Health Attention Get message structure

The Opcode field shall contain the opcode value for the Health Attention Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.3.13. Health Attention Set

A Health Attention Set is an acknowledged message used to set the Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

The response to a Health Attention Set message is a Health Attention Status message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Attention | 1 | Value of the Attention Timer state | M |

Table 4.166. Health Attention Set message structure

The Opcode field shall contain the opcode value for the Health Attention Set message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Attention field shall identify the new Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

##### 4.3.3.14. Health Attention Set Unacknowledged

A Health Attention Set Unacknowledged is an unacknowledged message used to set the Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Attention | 1 | Value of the Attention Timer state | M |

Table 4.167. Health Attention Set Unacknowledged message structure

The Opcode field shall contain the opcode value for the Health Attention Set Unacknowledged message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Attention field shall identify the new Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

##### 4.3.3.15. Health Attention Status

A Health Attention Status is an unacknowledged message used to report the current Attention Timer state of an element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Attention | 1 | Value of the Attention Timer state | M |

Table 4.168. Health Attention Status message structure

The Opcode field shall contain the opcode value for the Health Attention Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Attention field shall identify the current Attention Timer state of the element (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")).

#### 4.3.4. Remote Provisioning messages

Remote Provisioning messages are used by a Remote Provisioning Client to communicate with a Remote Provisioning Server over a mesh network to find the UUID of unprovisioned devices within immediate radio range of the Remote Provisioning Server and to provision a remote unprovisioned device. Remote Provisioning messages also can
be used to obtain extended information about an unprovisioned device or to execute a Device Key Refresh procedure or a Node Address Refresh procedure or a Node Composition Refresh procedure.

##### 4.3.4.1. Remote Provisioning Scan Capabilities Get

A Remote Provisioning Scan Capabilities Get message is an acknowledged message used by the Remote Provisioning Client to get the value of the Remote Provisioning Scan Capabilities state (see [Section 4.2.23](index-en.html#UUID-eab9589a-c072-7bbc-b38b-62454988e3f9 "4.2.23. Remote Provisioning Scan Capabilities")).

The response to a Remote Provisioning Scan Capabilities Get message is a Remote Provisioning Scan Capabilities Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

The structure of the Remote Provisioning Scan Capabilities Get message is defined in [Table 4.169](index-en.html#UUID-baad19b6-7b74-cf1c-9533-bb0c05368093_Table_4.169 "Table 4.169. Remote Provisioning Scan Capabilities Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.169. Remote Provisioning Scan Capabilities Get message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Capabilities Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.4.2. Remote Provisioning Scan Capabilities Status

A Remote Provisioning Scan Capabilities Status message is an unacknowledged message used by the Remote Provisioning Server to report the current value of the Remote Provisioning Scan Capabilities state of a Remote Provisioning Server.

The structure of the Remote Provisioning Scan Capabilities Status message is defined in [Table 4.170](index-en.html#UUID-8c18f25d-9b9a-db5d-fa73-786f500f0694_Table_4.170 "Table 4.170. Remote Provisioning Scan Capabilities Status message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| MaxScannedItems | 1 | The maximum number of UUIDs that can be reported during scanning | M |
| ActiveScan | 1 | Indication if active scan is supported | M |

Table 4.170. Remote Provisioning Scan Capabilities Status message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Capabilities Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The MaxScannedItems field identifies the value of the Remote Provisioning Max Scanned Items state (see [Section 4.2.23.1](index-en.html#UUID-bbd2744d-fa3f-2378-9bfd-018e95e72a07 "4.2.23.1. Remote Provisioning Max Scanned Items")).

The ActiveScan field identifies the value of the Remote Provisioning Active Scan state (see [Section 4.2.23.2](index-en.html#UUID-a71ea8da-1d69-a0c3-8d24-7ebd0d1f3a3e "4.2.23.2. Remote Provisioning Active Scan")).

##### 4.3.4.3. Remote Provisioning Scan Get

A Remote Provisioning Scan Get message is an acknowledged message that is used by the Remote Provisioning Client to get the various scanning states of a Remote Provisioning Server model.

The response to a Remote Provisioning Scan Get message is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

The structure of the Remote Provisioning Scan Get message is defined in [Table 4.171](index-en.html#UUID-4485f14a-fa6b-db38-ee05-0e8570ed5d11_Table_4.171 "Table 4.171. Remote Provisioning Scan Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.171. Remote Provisioning Scan Get message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.4.4. Remote Provisioning Scan Start

A Remote Provisioning Scan Start message is an acknowledged message that is used by the Remote Provisioning Client to start the Remote Provisioning Scan procedure, which finds unprovisioned devices within immediate radio range of the Remote Provisioning Server (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")).

The response to a Remote Provisioning Scan Start message is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

The structure of the Remote Provisioning Scan Start message is defined in [Table 4.172](index-en.html#UUID-d6fd8126-4daf-994f-e1b6-0f9c04a8e051_Table_4.172 "Table 4.172. Remote Provisioning Scan Start message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ScannedItemsLimit | 1 | Maximum number of scanned items to be reported | M |
| Timeout | 1 | Time limit for a scan (in seconds) | M |
| UUID | 16 | Device UUID | O |

Table 4.172. Remote Provisioning Scan Start message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Start message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ScannedItemsLimit field identifies the maximum number of unprovisioned devices the Remote Provisioning Server can report while executing the Remote Provisioning Scan procedure. Value 0 indicates that the Remote Provisioning Client does not set a limit on the number of unprovisioned devices that the Remote Provisioning
Server can report.

The Timeout field identifies the new value of the Remote Provisioning Timeout state (see [Section 4.2.24.3](index-en.html#UUID-c687cf35-65e6-6a9e-4a9a-8a193cdf205e "4.2.24.3. Remote Provisioning Timeout")). The value of the Timeout field shall not be 0.

If the UUID field is present, the Remote Provisioning Client is requesting a Single Device Scanning procedure (i.e., a scan for a specific unprovisioned device identified by the value of the UUID field). If the UUID field is absent, the Remote Provisioning Client is requesting a scan for all unprovisioned devices within
immediate radio range (a Multiple Devices Scanning).

##### 4.3.4.5. Remote Provisioning Scan Stop

A Remote Provisioning Scan Stop message is an acknowledged message that is used by the Remote Provisioning Client to terminate the Remote Provisioning Scan procedure (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")).

The response to a Remote Provisioning Scan Stop message is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

The structure of the Remote Provisioning Scan Stop message is defined in [Table 4.173](index-en.html#UUID-e64f9c00-3884-46fb-4760-7e138d817deb_Table_4.173 "Table 4.173. Remote Provisioning Scan Stop message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.173. Remote Provisioning Scan Stop message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Stop message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.4.6. Remote Provisioning Scan Status

A Remote Provisioning Scan Status message is an unacknowledged message used by the Remote Provisioning Server to report the current value of the Remote Provisioning Scan Parameters state and the Remote Provisioning Scan state of a Remote Provisioning Server model.

The structure of the Remote Provisioning Scan Status message is defined in [Table 4.174](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1_Table_4.174 "Table 4.174. Remote Provisioning Scan Status message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status for the requesting message | M |
| RPScanningState | 1 | The Remote Provisioning Scan state value | M |
| ScannedItemsLimit | 1 | Maximum number of scanned items to be reported | M |
| Timeout | 1 | Time limit for a scan (in seconds) | M |

Table 4.174. Remote Provisioning Scan Status message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field identifies the status of the most recent operation on Remote Provisioning Scan state, as defined in [Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes").

The RPScanningState field identifies the value of the Remote Provisioning Scan state (see [Section 4.2.24.1](index-en.html#UUID-ca4b8784-dd2f-4a97-be4a-f071bb1c0a1d "4.2.24.1. Remote Provisioning Scan")).

The ScannedItemsLimit field identifies the maximum number of unprovisioned devices as requested by the Remote Provisioning Client in the Remote Provisioning Scan Start message.

The Timeout field identifies the current value of the Remote Provisioning Timeout state (see [Section 4.2.24.2](index-en.html#UUID-4d9761e3-d2ae-5689-d269-31375e0a8491 "4.2.24.2. Remote Provisioning Scan Items Limit")).

##### 4.3.4.7. Remote Provisioning Scan Report

A Remote Provisioning Scan Report message is an unacknowledged message used by the Remote Provisioning Server to report the scanned Device UUID of an unprovisioned device. Based on the Remote Provisioning Scan Reports received from multiple Remote Provisioning Servers, the Remote Provisioning Client can select the most
suitable Remote Provisioning Server to execute the Extended Scan procedure and/or to provision the unprovisioned device.

The structure of the Remote Provisioning Scan Report message is defined in [Table 4.175](index-en.html#UUID-89265fa6-9143-b73c-96b0-8b798d8e1f8b_Table_4.175 "Table 4.175. Remote Provisioning Scan Report message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| RSSI | 1 | Signed integer that is interpreted as an indication of received signal strength measured in dBm. | M |
| UUID | 16 | Device UUID | M |
| OOB | 2 | OOB information | M |
| URI Hash | 4 | URI Hash | O |

Table 4.175. Remote Provisioning Scan Report message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Scan Report message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The RSSI field contains a signed 8-bit value and is interpreted as an indication of received signal strength measured in dBm. The Remote Provisioning Server measures the RSSI value on packets sent by the unprovisioned device. If the RSSI cannot be read, the RSSI field shall be set to 127.

The UUID field identifies the Device UUID of the unprovisioned device.

The OOB field identifies the OOB Information of the unprovisioned device (see [Table 3.78](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869_Table_3.78 "Table 3.78. OOB Information field")).

If present, the URI Hash field identifies the URI Hash (see [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon")) of the unprovisioned device.

##### 4.3.4.8. Remote Provisioning Extended Scan Start

A Remote Provisioning Extended Scan Start message is an unacknowledged message that is used by the Remote Provisioning Client to request additional information about a specific unprovisioned device or about the Remote Provisioning Server itself.

As a result of processing a Remote Provisioning Extended Scan Start message, the Remote Provisioning Server sends a Remote Provisioning Extended Scan Report message (see [Section 4.3.4.9](index-en.html#UUID-77aac123-f6bc-8246-4821-d8fbd89ef828 "4.3.4.9. Remote Provisioning Extended Scan Report")).

The structure of the Remote Provisioning Extended Scan Start message is defined in [Table 4.176](index-en.html#UUID-8bf36c3a-b2de-f4ac-8d12-f58bcc7f3951_Table_4.176 "Table 4.176. Remote Provisioning Extended Scan Start message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| ADTypeFilterCount | 1 | Number of AD Types in the ADTypeFilter field | M |
| ADTypeFilter | variable | List of AD Types to be reported | M |
| UUID | 16 | Device UUID | O |
| Timeout | 1 | Time limit for a scan (in seconds) | C.1 |

Table 4.176. Remote Provisioning Extended Scan Start message structure

C.1: If UUID field is present, the Timeout field shall also be present; otherwise, Timeout field shall not be present.

The Opcode field shall contain the opcode value for the Remote Provisioning Extended Scan Start message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The ADTypeFilterCount field identifies the number of AD types listed in the ADTypeFilter field. The ADTypeFilterCount field value equal to 0x00 or greater than 0x10 is prohibited.

The ADTypeFilter is a list of AD types that the client is requesting. The ADTypeFilter shall not contain the Shortened Local Name AD Type, the Incomplete List of 16-bit Service UUIDs AD Type, the Incomplete List of 32-bit Service UUIDs AD Type, or the Incomplete List of 128-bit Service UUIDs AD Type. The ADTypeFilter shall not
contain more than one of the same AD type values.

If the ADTypeFilter field contains the Complete Local Name AD Type, the client is requesting either the Complete Local Name or the Shortened Local Name (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")).

If present, the UUID field identifies the Device UUID of the unprovisioned device for which additional information is requested (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")). If
the UUID field is absent, the request retrieves information about the Remote Provisioning Server (see [Section 4.4.5](index-en.html#UUID-a5822f3c-d602-d597-e794-15189e9e3c83 "4.4.5. Remote Provisioning Server model")). In the latter case, the Remote Provisioning Server
ignores the Timeout field value.

The Timeout field indicates how long the Remote Provisioning Client requests the Remote Provisioning Server to collect information about the unprovisioned device identified by the UUID. [Table 4.177](index-en.html#UUID-8bf36c3a-b2de-f4ac-8d12-f58bcc7f3951_Table_4.177 "Table 4.177. Remote Provisioning Extended Scan Start Timeout field values") defines the values for the Timeout field.

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01−0x15 | Length of time (in seconds) to collect information about the unprovisioned device |
| 0x16–0xFF | Prohibited |

Table 4.177. Remote Provisioning Extended Scan Start Timeout field values

##### 4.3.4.9. Remote Provisioning Extended Scan Report

A Remote Provisioning Extended Scan Report message is an unacknowledged message used by the Remote Provisioning Server to report the advertising data requested by the client in a Remote Provisioning Extended Scan Start message (see [Section 4.3.4.8](index-en.html#UUID-8bf36c3a-b2de-f4ac-8d12-f58bcc7f3951 "4.3.4.8. Remote Provisioning Extended Scan Start")).

The structure of the Remote Provisioning Extended Scan Report message is defined in [Table 4.178](index-en.html#UUID-77aac123-f6bc-8246-4821-d8fbd89ef828_Table_4.178 "Table 4.178. Remote Provisioning Extended Scan Report message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status for the requesting message | M |
| UUID | 16 | Device UUID | M |
| OOBInformation | 2 | OOB Information | O |
| AdvStructures | variable | Concatenated list of AD Structures that match the AD Types requested by the client in the ADTypeFilter field of the Remote Provisioning Extended Scan Start message | C.1 |

Table 4.178. Remote Provisioning Extended Scan Report message structure

C.1:
:   If OOBInformation field is present, the AdvStructures field is optional; otherwise, AdvStructures field shall not be present.

The Opcode field shall contain the opcode value for the Remote Provisioning Extended Scan Report message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field identifies the status of the Remote Provisioning Extended Scan Start processing, as defined in [Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes").

The UUID field identifies the Device UUID of either the unprovisioned device (see [Section 3.11.3](index-en.html#UUID-29a75fe3-e98f-0067-f6c7-34aeec2c83f8 "3.11.3. Device UUID")) or the Remote Provisioning Server.

The OOBInformation field contains the OOB Information of either the unprovisioned device (see [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon")) or the Remote Provisioning Server.

If present, the AdvStructures field contains a concatenated list of AD Structures with information requested by the Remote Provisioning Client. The value has the same format as advertising data or scan response data, as defined in [[1](index-en.html#idp254740)] Vol 3,
Part C, Section 11.

##### 4.3.4.10. Remote Provisioning Link Get

A Remote Provisioning Link Get message is an acknowledged message used by the Remote Provisioning Client to get the Remote Provisioning Link state of a Remote Provisioning Server model.

The response to a Remote Provisioning Link Get message is a Remote Provisioning Link Status message (see Section [4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

The structure of the Remote Provisioning Link Get message is defined in [Table 4.179](index-en.html#UUID-4e10a1d6-a60b-0607-6785-c755673a5467_Table_4.179 "Table 4.179. Remote Provisioning Link Get message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.179. Remote Provisioning Link Get message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Link Get message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.4.11. Remote Provisioning Link Open

A Remote Provisioning Link Open message is an acknowledged message used by the Remote Provisioning Client to establish the provisioning bearer between a node supporting the Remote Provisioning Server model and an unprovisioned device, or to open the Node Provisioning Protocol Interface.

The response to a Remote Provisioning Link Open message is a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

The structure of the Remote Provisioning Link Open message is defined in [Table 4.180](index-en.html#UUID-921ddce6-3e9d-931e-3867-6758cf74730b_Table_4.180 "Table 4.180. Remote Provisioning Link Open message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| UUID | 16 | Device UUID | O |
| Link Open Timeout | 1 | Link open timeout in seconds | C.1 |
| NPPI Procedure | 1 | Node Provisioning Protocol Interface procedure | C.2 |

Table 4.180. Remote Provisioning Link Open message structure

C.1:
:   If UUID field is present, the Link Open Timeout field is optional; otherwise it is excluded.

C.2:
:   If UUID field is present, the NPPI Procedure field is prohibited; otherwise, the NPPI Procedure field is mandatory.

The Opcode field shall contain the opcode value for the Remote Provisioning Link Open message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

If present, the UUID field identifies the Device UUID parameter of the PB-Remote Open Link procedure (see [Section 5.2.3.3.1](index-en.html#UUID-d778d00c-520b-7379-123b-b40f792f84bb "5.2.3.3.1. PB-Remote Open Link procedure")). If the UUID field is absent, the Remote
Provisioning Server will open the Node Provisioning Protocol Interface.

If present, the Link Open Timeout field identifies Timeout parameter of the PB-Remote Open Link procedure. The Link Open Timeout field values are defined in [Table 4.181](index-en.html#UUID-921ddce6-3e9d-931e-3867-6758cf74730b_Table_4.181 "Table 4.181. Link Open Timeout field values for the Remote Provisioning Link Open message").

| Value | Description |
| --- | --- |
| 0x00 | Prohibited |
| 0x01–0x3C | Timeout in seconds of the PB-Remote Open Link procedure. |
| 0x3D–0xFF | Prohibited |

Table 4.181. Link Open Timeout field values for the Remote Provisioning Link Open message

If present, the NPPI Procedure field identifies one of the Node Provisioning Protocol Interface procedures the Remote Provisioning Server will execute. The NPPI Procedure field values for the Remote Provisioning Link Open message are defined in [Table 4.182](index-en.html#UUID-921ddce6-3e9d-931e-3867-6758cf74730b_Table_4.182 "Table 4.182. NPPI Procedure field values for the Remote Provisioning Link Open message").

| Value | Procedure | Description |
| --- | --- | --- |
| 0x00 | Device Key Refresh | Device Key Refresh procedure |
| 0x01 | Node Address Refresh | Node Address Refresh procedure |
| 0x02 | Node Composition Refresh | Node Composition Refresh procedure |
| 0x03–0xFF | RFU | Reserved for Future Use |

Table 4.182. NPPI Procedure field values for the Remote Provisioning Link Open message

##### 4.3.4.12. Remote Provisioning Link Close

A Remote Provisioning Link Close message is an acknowledged message used by the Remote Provisioning Client to close a provisioning bearer or the Node Provisioning Protocol Interface.

The response to a Remote Provisioning Link Close message is a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

The structure of the Remote Provisioning Link Close message is defined in [Table 4.183](index-en.html#UUID-d3990040-9b66-9a7b-31d3-c235eba6a3b8_Table_4.183 "Table 4.183. Remote Provisioning Link Close message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Reason | 1 | Provisioning bearer link close reason code | M |

Table 4.183. Remote Provisioning Link Close message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Link Close message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Reason field identifies the reason for the provisioning bearer link close. The Reason field values for the Remote Provisioning Link Close message are defined in [Table 4.184](index-en.html#UUID-d3990040-9b66-9a7b-31d3-c235eba6a3b8_Table_4.184 "Table 4.184. Reason field values for a Remote Provisioning Link Close message").

| Reason Code | Reason Code Name | Description |
| --- | --- | --- |
| 0x00 | Success | The provisioning or Node Provisioning Protocol Interface procedure completed successfully. |
| 0x01 | Prohibited | Prohibited |
| 0x02 | Fail | The provisioning or Node Provisioning Protocol Interface procedure failed. |
| 0x03–0xFF | RFU | Reserved for Future Use |

Table 4.184. Reason field values for a Remote Provisioning Link Close message

##### 4.3.4.13. Remote Provisioning Link Status

A Remote Provisioning Link Status message is an unacknowledged message used by the Remote Provisioning Server to acknowledge a Remote Provisioning Link Get message, a Remote Provisioning Link Open message, or a Remote Provisioning Link Close message.

The structure of the Remote Provisioning Link Status message is defined in [Table 4.185](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b_Table_4.185 "Table 4.185. Remote Provisioning Link Status message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status for the requesting message | M |
| RPState | 1 | Remote Provisioning Link state | M |

Table 4.185. Remote Provisioning Link Status message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Link Status message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field identifies the status of the processing of the message from the client, as defined in [Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes").

The RPState field identifies the Remote Provisioning Link state (see [Table 4.51](index-en.html#UUID-1ae77eff-b468-ffc6-ac8f-4dac1d79b155_Table_4.51 "Table 4.51. Remote Provisioning Link state values")).

##### 4.3.4.14. Remote Provisioning Link Report

A Remote Provisioning Link Report message is an unacknowledged message used by the Remote Provisioning Server to report the state change of a provisioning bearer link or the Node Provisioning Protocol Interface.

The structure of the Remote Provisioning Link Report message is defined in [Table 4.186](index-en.html#UUID-dadd085e-be70-c3f1-3ce5-d96bba9437c2_Table_4.186 "Table 4.186. Remote Provisioning Link Report message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status of the provisioning bearer or the Node Provisioning Protocol Interface | M |
| RPState | 1 | Remote Provisioning Link state | M |
| Reason | 1 | Link close Reason code | O |

Table 4.186. Remote Provisioning Link Report message structure

The Opcode field shall contain the opcode value for the Remote Provisioning Link Report message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field identifies the provisioning bearer status as defined in [Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes").

The RPState field identifies the Remote Provisioning Link state.

If present, the Reason field identifies the reason for the provisioning bearer link close as defined in [Table 5.16](index-en.html#UUID-dabc5c31-cbb1-faea-391f-8b9413122bc6_Table_5.16 "Table 5.16. Reason field values"). The field shall be present when Status is
either Link Closed by Device or Link Closed by Server and the provisioning bearer provides a Reason code. Otherwise, it shall be omitted.

##### 4.3.4.15. Remote Provisioning PDU Send

A Remote Provisioning PDU Send message is an unacknowledged message used by the Remote Provisioning Client to deliver the Provisioning PDU to an unprovisioned device or to the Node Provisioning Protocol Interface.

A Remote Provisioning PDU Send message should be tagged with the send-segmented tag. Alternatively, the Remote Provisioning Client needs to keep track of Remote Provisioning PDU Outbound Report messages and may need to retry sending Remote Provisioning PDU Send messages.

When the Remote Provisioning server receives a Remote Provisioning PDU Send message, the server attempts to deliver a Provisioning PDU. If the Provisioning PDU is delivered, the Remote Provisioning Server sends a Remote Provisioning PDU Outbound Report message (see [Section 4.3.4.16](index-en.html#UUID-06bee883-bb71-03ff-de70-86972f8c05c5 "4.3.4.16. Remote Provisioning PDU Outbound Report")). If the Remote Provisioning Server fails to deliver the Provisioning PDU, the Remote Provisioning Link Report message is sent (see [Section 4.3.4.14](index-en.html#UUID-dadd085e-be70-c3f1-3ce5-d96bba9437c2 "4.3.4.14. Remote Provisioning Link Report")).

The structure of the Remote Provisioning PDU Send message is defined in [Table 4.187](index-en.html#UUID-c6a224eb-2550-037e-1648-c5538dbc4bcd_Table_4.187 "Table 4.187. Remote Provisioning PDU Send message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| OutboundPDUNumber | 1 | The value of the Remote Provisioning Outbound PDU Count state of the Remote Provisioning Server | M |
| ProvisioningPDU | variable | Provisioning PDU | M |

Table 4.187. Remote Provisioning PDU Send message structure

The Opcode field shall contain the opcode value for the Remote Provisioning PDU Send message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The OutboundPDUNumber field identifies the value of the Remote Provisioning Outbound PDU Count state of the Remote Provisioning Server after successful delivery of the PDU in the ProvisioningPDU field of the message to the device being provisioned.

The ProvisioningPDU field identifies the Provisioning PDU that either will be sent to an unprovisioned device or will be processed locally if the Device Key Refresh procedure, the Node Address Refresh procedure, or the Node Composition Refresh procedure is in progress.

##### 4.3.4.16. Remote Provisioning PDU Outbound Report

A Remote Provisioning PDU Outbound Report message is an unacknowledged message used by the Remote Provisioning Server to report completion of the delivery of the Provisioning PDUs that the Remote Provisioning Server either sends to a device that is being provisioned or processes locally during the Device Key Refresh procedure,
the Node Address Refresh procedure, or the Node Composition Refresh procedure.

The structure of the Remote Provisioning PDU Outbound Report message is defined in [Table 4.188](index-en.html#UUID-06bee883-bb71-03ff-de70-86972f8c05c5_Table_4.188 "Table 4.188. Remote Provisioning PDU Outbound Report message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| OutboundPDUNumber | 1 | Remote Provisioning Outbound PDU Count state | M |

Table 4.188. Remote Provisioning PDU Outbound Report message structure

The Opcode field shall contain the opcode value for the Remote Provisioning PDU Outbound Report message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The OutboundPDUNumber field contains the value of the Remote Provisioning Outbound PDU Count state.

##### 4.3.4.17. Remote Provisioning PDU Report

A Remote Provisioning PDU Report message is an unacknowledged message used by the Remote Provisioning Server to report the Provisioning PDU that either was received from the device being provisioned or was generated locally during the Device Key Refresh procedure, the Node Address Refresh procedure, or the Node Composition
Refresh procedure.

The structure of the Remote Provisioning PDU Report message is defined in [Table 4.189](index-en.html#UUID-b5d0fa3b-6a11-6c97-880a-fba085eca39b_Table_4.189 "Table 4.189. Remote Provisioning PDU Report message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| InboundPDUNumber | 1 | Number of received Provisioning PDUs | M |
| ProvisioningPDU | variable | Provisioning PDU | M |

Table 4.189. Remote Provisioning PDU Report message structure

The Opcode field shall contain the opcode value for the Remote Provisioning PDU Report message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The InboundPDUNumber field identifies the value of the Remote Provisioning Inbound PDU Count state (see [Section 4.2.25.4](index-en.html#UUID-149af927-3a33-19ae-5acb-3acbe0559344 "4.2.25.4. Remote Provisioning Inbound PDU Count")).

The ProvisioningPDU field identifies the Provisioning PDU that was sent by an unprovisioned device or generated locally during the Device Key Refresh procedure, the Node Address Refresh procedure, or the Node Composition Refresh procedure.

#### 4.3.5. Directed Forwarding Configuration messages

Directed Forwarding Configuration messages are exchanged between the Directed Forwarding Configuration Server and the Directed Forwarding Configuration Client models to control and monitor states that determine the behavior of Directed Forwarding nodes within one or all the subnets to which they belong.

##### 4.3.5.1. Forwarding Table path entries format

This section describes the format used to serialize the Forwarding Table entry in the messages. The serialization format of the table entry depends on whether the entry represents a fixed path or a non-fixed path. Depending on the type of path, represented by the table entry, the serialization format is optimized by omitting
the static values in the entry.

###### 4.3.5.1.1. Forwarding Table Entry Header

The Forwarding Table Entry Header is a 16-bit data structure that encapsulates the flags and the indicators of presence and size of fields of fixed and non-fixed Forwarding Table entries. [Table 4.190](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.190 "Table 4.190. Forwarding Table Entry Header parameters ") defines the structure of the Forwarding Table Entry Header.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Fixed_Path_Flag | 1 | Indicates whether the table entry is a fixed path entry or a non-fixed path entry | M |
| Unicast_Destination_Flag | 1 | Indicates whether or not the destination of the path is a unicast address | M |
| Backward_Path_Validated_Flag | 1 | Indicates whether or not the backward path has been validated | M |
| Bearer_Toward_Path_Origin_Indicator | 1 | Indicates the presence or absence of the Bearer_Toward_Path_Origin field | M |
| Bearer_Toward_Path_Target_Indicator | 1 | Indicates the presence or absence of the Bearer_Toward_Path_Target field | M |
| Dependent_Origin_List_Size_Indicator | 2 | Indicates the size of the Dependent_Origin_List field | M |
| Dependent_Target_List_Size_Indicator | 2 | Indicates the size of the Dependent_Target_List field | M |
| Prohibited | 7 | Prohibited | M |

Table 4.190. Forwarding Table Entry Header parameters

The Fixed_Path_Flag field indicates whether the table entry is a fixed path entry or a non-fixed path entry. The values of the Fixed_Path_Flag field are defined in [Table 4.191](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.191 "Table 4.191. Fixed_Path_Flag field values").

| Value | Description |
| --- | --- |
| 0 | The table entry is a non-fixed path entry |
| 1 | The table entry is a fixed path entry |

Table 4.191. Fixed_Path_Flag field values

The Unicast_Destination_Flag field indicates whether the Destination field value in the Forwarding Table entry is a unicast address or a multicast address (i.e., a group address or a virtual address). If the Unicast_Destination_Flag field value is 0, then the value of the Dependent_Target_List_Size_Indicator field shall be
0b00.

The Backward_Path_Validated_Flag field indicates whether the backward path has been validated. Backward_Path_Validated_Flag field values are defined in [Table 4.192](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.192 "Table 4.192. Backward_Path_Validated_Flag field values ").

| Value | Description |
| --- | --- |
| 0 | The backward path has not been validated |
| 1 | The backward path has been validated |

Table 4.192. Backward_Path_Validated_Flag field values

The Bearer_Toward_Path_Origin_Indicator field indicates whether the node is the Path Origin for the Forwarding Table entry. Bearer_Toward_Path_Origin_Indicator field values are defined in [Table 4.193](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.193 "Table 4.193. Bearer_Toward_Path_Origin_Indicator field values ").

| Value | Description |
| --- | --- |
| 0 | The node is not the Path Origin for the Forwarding Table entry (the bearer index is the unassigned bearer index) |
| 1 | The node is the Path Origin for the Forwarding Table entry (bearer index is not the unassigned bearer index) |

Table 4.193. Bearer_Toward_Path_Origin_Indicator field values

The Bearer_Toward_Path_Target_Indicator field indicates whether the node is the Path Target for the Forwarding Table entry. Bearer_Toward_Path_Target_Indicator field values are defined in [Table 4.194](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.194 "Table 4.194. Bearer_Toward_Path_Target_Indicator field values").

| Value | Description |
| --- | --- |
| 0 | The node is not the Path Target for the Forwarding Table entry (the bearer index is the unassigned bearer index) |
| 1 | The node is the Path Target for the Forwarding Table entry (bearer index is not the unassigned bearer index) |

Table 4.194. Bearer_Toward_Path_Target_Indicator field values

The Dependent_Origin_List_Size_Indicator field and the Dependent_Target_List_Size_Indicator field indicate the number of octets used to represent the length of the Dependent_Origin_List field and the Dependent_Target_List field in the Forwarding Table entry, respectively.

[Table 4.195](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0_Table_4.195 "Table 4.195. Values of the Dependent_Origin_List_Size_Indicator and Dependent_Target_List_Size_Indicator fields") defines the values of the Dependent_Origin_List_Size_Indicator
and Dependent_Target_List_Size_Indicator fields.

| Value | Description |
| --- | --- |
| 0b00 | List size is zero. |
| 0b01 | 1-octet list size field. |
| 0b10 | 2-octet list size field. |
| 0b11 | Prohibited |

Table 4.195. Values of the Dependent_Origin_List_Size_Indicator and Dependent_Target_List_Size_Indicator fields

###### 4.3.5.1.2. Fixed path entry format

Fixed path entries in the Forwarding Table are formatted as described in [Table 4.196](index-en.html#UUID-ce3de742-3dbf-d825-cb98-0b34c0ddfcb3_Table_4.196 "Table 4.196. Fixed path entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Forwarding_Table_Entry_Header | 16 | Forwarding Table Entry Header | M |
| Path_Origin_Unicast_Addr_Range | variable  (16 or 24) | Path Origin unicast address range | M |
| Dependent_Origin_List_Size | variable  (8 or 16) | Current number of entries in the list of dependent nodes of the Path Origin | C.1 |
| Bearer_Toward_Path_Origin | 16 | Index of the bearer toward the Path Origin | C.2 |
| Path_Target_Unicast_Addr_Range | variable  (16 or 24) | Path Target unicast address range | C.3 |
| Multicast_Destination | 16 | Multicast destination address | C.4 |
| Dependent_Target_List_Size | variable  (8 or 16) | Current number of entries in the list of dependent nodes of the Path Target | C.5 |
| Bearer_Toward_Path_Target | 16 | Index of the bearer toward the Path Target | C.6 |

Table 4.196. Fixed path entry format

C.1:
:   If the value of the Dependent_Origin_List_Size_Indicator field in the Forwarding_Table_Entry_Header field is 0b01 or 0b10, then the Dependent_Origin_List_Size field shall be present; otherwise, the Dependent_Origin_List_Size field shall not be present.

C.2:
:   If the value of the Bearer_Toward_Path_Origin_Indicator field in the Forwarding_Table_Entry_Header is 1, then the Bearer_Toward_Path_Origin field shall be present; otherwise, the Bearer_Toward_Path_Origin field shall not be present.

C.3:
:   If the value of the Unicast_Destination_Flag field in the Forwarding_Table_Entry_Header is 1, then the Path_Target_Unicast_Addr_Range field shall be present; otherwise, the Path_Target_Unicast_Addr_Range field shall not be present.

C.4:
:   If the value of the Unicast_Destination_Flag field in the Forwarding_Table_Entry_Header is 0, then the Multicast_Destination field shall be present; otherwise, the Multicast_Destination field shall not be present.

C.5:
:   If the value of the Dependent_Target_List_Size_Indicator field in the Forwarding_Table_Entry_Header is 0b01 or 0b10, then the Dependent_Target_List_Size field shall be present; otherwise, the Dependent_Target_List_Size field shall not be present.

C.6:
:   If the value of the Bearer_Toward_Path_Target_Indicator field in the Forwarding_Table_Entry_Header is 1, then the Bearer_Toward_Path_Target field shall be present; otherwise, the Bearer_Toward_Path_Target field shall not be present.

The Forwarding_Table_Entry_Header field represents the Forwarding Table Entry Header as described in the [Section 4.3.5.1.1](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0 "4.3.5.1.1. Forwarding Table Entry Header").

The Path_Origin_Unicast_Addr_Range field represents the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Path Origin in the Forwarding Table entry.

If present, the Dependent_Origin_List_Size field represents the current number of entries in the Dependent_Origin_List field in the Forwarding Table entry.

If present, the Bearer_Toward_Path_Origin field represents the index of the bearer toward the Path Origin in the Forwarding Table entry.

If present, the Path_Target_Unicast_Addr_Range field represents the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Destination field in the Forwarding Table
entry.

If present, the Multicast_Destination field represents the group address or the virtual address of the Destination field in the Forwarding Table entry.

If present, the Dependent_Target_List_Size field represents the current number of entries in the Dependent_Target_List field in the Forwarding Table entry.

If present, the Bearer_Toward_Path_Target field represents the index of the bearer toward the Path Target in the Forwarding Table entry.

###### 4.3.5.1.3. Non-fixed path entry format

Non-fixed path entries in the Forwarding Table are formatted as described in [Table 4.197](index-en.html#UUID-a53a4af1-4ba2-b130-eb6b-0657123ef829_Table_4.197 "Table 4.197. Non-fixed path entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Forwarding_Table_Entry_­Header | 16 | Forwarding Table Entry Header | M |
| Lane_Counter | 8 | Number of lanes in the path | M |
| Path_Remaining_Time | 16 | Path lifetime remaining | M |
| Path_Origin_Forwarding_­Number | 8 | Forwarding number of the Path Origin | M |
| Path_Origin_Unicast_Addr_­Range | variable  (16 or 24) | Path Origin unicast address range | M |
| Dependent_Origin_List_Size | variable  (8 or 16) | Current number of entries in the list of dependent nodes of the Path Origin | C.1 |
| Bearer_Toward_Path_Origin | 16 | Index of the bearer toward the Path Origin | C.2 |
| Path_Target_Unicast_­Addr_­Range | variable  (16 or 24) | Path Target unicast address range | C.3 |
| Multicast_Destination | 16 | Multicast destination address | C.4 |
| Dependent_Target_List_­Size | variable  (8 or 16) | Current number of entries in the list of dependent nodes of the Path Target | C.5 |
| Bearer_Toward_Path_­Target | 16 | Index of the bearer toward the Path Target | C.6 |

Table 4.197. Non-fixed path entry format

C.1:
:   If the value of the Dependent_Origin_List_Size_Indicator field in the Forwarding_Table_Entry_Header field is 0b01 or 0b10, then the Dependent_Origin_List_Size field shall be present; otherwise, the Dependent_Origin_List_Size field shall not be present.

C.2:
:   If the value of the Bearer_Toward_Path_Origin_Indicator field in the Forwarding_Table_Entry_Header field is 1, then the Bearer_Toward_Path_Origin field shall be present; otherwise the Bearer_Toward_Path_Origin field shall not be present.

C.3:
:   If the value of the Unicast_Destination_Flag field in the Forwarding_Table_Entry_Header field is 1, then the Path_Target_Unicast_Addr_Range field shall be present; otherwise, the Path_Target_Unicast_Addr_Range field shall not be present.

C.4:
:   If the value of the Unicast_Destination_Flag field in the Forwarding_Table_Entry_Header field is 0, then the Multicast_Destination field shall be present; otherwise, the Multicast_Destination field shall not be present.

C.5:
:   If the value of the Dependent_Target_List_Size_Indicator field in the Forwarding_Table_Entry_Header field is 0b01 or 0b10, then the Dependent_Target_List_Size field shall be present; otherwise, the Dependent_Target_List_Size field shall not be present.

C.6:
:   If the value of the Bearer_Toward_Path_Target_Indicator field in the Forwarding_Table_Entry_Header field is 1, then the Bearer_Toward_Path_Target field shall be present; otherwise, the Bearer_Toward_Path_Target field shall not be present.

The Forwarding_Table_Entry_Header field represents the Forwarding Table Entry Header as described in the [Section 4.3.5.1.1](index-en.html#UUID-c630af0e-b6c0-5568-8fe5-91b2f56c53e0 "4.3.5.1.1. Forwarding Table Entry Header").

The Lane_Counter field contains a count of the number of lanes in the path.

The Path_Remaining_Time field represents the remaining path lifetime (in minutes).

The Path_Origin_Forwarding_Number field contains the forwarding number of the Path Origin.

The Path_Origin_Unicast_Addr_Range field represents the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Path Origin.

If present, the Dependent_Origin_List_Size field represents the current number of entries in the list of dependent nodes of the Path Origin (i.e., in the Dependent_Origin_List field).

If present, the Bearer_Toward_Path_Origin field represents the index of the bearer toward the Path Origin.

If present, the Path_Target_Unicast_Addr_Range field represents the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Path Target.

If present, the Multicast_Destination field represents the group address or virtual address of the destination.

If present, the Dependent_Target_List_Size field represents the current number of entries in the list of dependent nodes of the Path Target (i.e., in the Dependent_Target_List field).

If present, the Bearer_Toward_Path_Target field represents the index of the bearer toward the Path Target.

##### 4.3.5.2. Finding a path entry in a Forwarding Table

Any path entry in the Forwarding Table state is uniquely identified by its Fixed_Path, Path_Origin, and Destination fields.

To identify a path entry in the Forwarding Table that corresponds to a Directed Forwarding Configuration message, the following conditions shall be met:

* If the message contains a Fixed_Path_Flag field, the value of the Fixed_Path field of the table entry shall be equal to the value of the Fixed_Path_Flag field in the message; otherwise, the value of the Fixed_Path field of the table entry shall be implicitly determined through the behavior of the message (e.g., the
  FORWARDING_TABLE_DEPENDENTS_ADD message acts on fixed path entries only).
* If the message contains a Path_Origin field, the value of the Path_Origin field of the table entry shall be equal to the value of the Path_Origin field in the message; or if the message contains a Path_Origin_Unicast_Addr_Range field, the value of the Path_Origin field of the table entry shall be equal to any address
  derived from the Path_Origin_Unicast_Addr_Range field in the message.
* If the message contains a Destination field, the value of the Destination field of the table entry shall be equal to the value of the Destination field in the message; or if the message contains a Path_Target_Unicast_Addr_Range field, the value of the Destination field of the table entry shall be equal to any address
  derived from the Path_Target_Unicast_Address_Range field in the message; or if the message contains a Multicast_Destination field, the value of the Destination field of the table entry shall be equal to the value of the Multicast_Destination field in the message.

When the value of the Fixed_Path field in the table entry cannot be determined by the message, at most two path entries (i.e., one fixed path entry and one non-fixed path entry) shall be found in the Forwarding Table state.

##### 4.3.5.3. DIRECTED_CONTROL_GET

A DIRECTED_CONTROL_GET message is an acknowledged message used to get the current Directed Control state of a node (see [Section 4.2.26](index-en.html#UUID-26bfef24-6d38-7b00-55a7-909e5862e7ad "4.2.26. Directed Control")).

The response to a DIRECTED_CONTROL_GET message is a DIRECTED_CONTROL_STATUS message.

[Table 4.198](index-en.html#UUID-88fd4de7-bd7a-c770-2359-04212b32a0ab_Table_4.198 "Table 4.198. DIRECTED_CONTROL_GET message structure") defines the structure of the DIRECTED_CONTROL_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.198. DIRECTED_CONTROL_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Directed Control state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.4. DIRECTED_CONTROL_SET

A DIRECTED_CONTROL_SET message is an acknowledged message used to set the Directed Control state of a subnet (see [Section 4.2.26](index-en.html#UUID-26bfef24-6d38-7b00-55a7-909e5862e7ad "4.2.26. Directed Control")).

The response to a DIRECTED_CONTROL_SET message is a DIRECTED_CONTROL_STATUS message.

[Table 4.199](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.199 "Table 4.199. DIRECTED_CONTROL_SET message structure") defines the structure of the DIRECTED_CONTROL_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Directed_Forwarding | 8 | New Directed Forwarding state | M |
| Directed_Relay | 8 | New Directed Relay state | M |
| Directed_Proxy | 8 | New Directed Proxy state or Do Not Process value | M |
| Directed_Proxy_Use_Directed_Default | 8 | New Directed Proxy Use Directed Default state or Do Not Process value | M |
| Directed_Friend | 8 | New Directed Friend state or Do Not Process value | M |

Table 4.199. DIRECTED_CONTROL_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Directed Control state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Directed_Forwarding field determines the new Directed Forwarding state for the identified subnet, as defined in [Section 4.2.26.1](index-en.html#UUID-76e0b3d3-4024-6fea-16f8-4698690725d7 "4.2.26.1. Directed Forwarding").

[Table 4.200](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.200 "Table 4.200. Values of the Directed_Forwarding field of the DIRECTED_CONTROL_SET message") defines the values of the Directed_Forwarding field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Disables directed forwarding functionality for the identified subnet. |
| 0x01 | Enable | Enables directed forwarding functionality for the identified subnet. |
| 0x02−0xFF | Prohibited | Prohibited |

Table 4.200. Values of the Directed_Forwarding field of the DIRECTED_CONTROL_SET message

The Directed_Relay field determines the new Directed Relay state for the identified subnet, as defined in [Section 4.2.26.2](index-en.html#UUID-539af574-8676-a61c-5e6f-b26f58c259d1 "4.2.26.2. Directed Relay").

[Table 4.201](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.201 "Table 4.201. Values of the Directed_Relay field of the DIRECTED_CONTROL_SET message") defines the values of the Directed_Relay field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Disables directed relay functionality for the identified subnet. |
| 0x01 | Enable | Enables directed relay functionality for the identified subnet. |
| 0x02−0xFF | Prohibited | Prohibited |

Table 4.201. Values of the Directed_Relay field of the DIRECTED_CONTROL_SET message

If the value of the Directed_Proxy field is Disable or Enable, then the Directed_Proxy field determines the new Directed Proxy state for the identified subnet, as defined in [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy").

[Table 4.202](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.202 "Table 4.202. Values of the Directed_Proxy field of the DIRECTED_CONTROL_SET message ") defines the values of the Directed_Proxy field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Indicates to disable directed proxy functionality for the identified subnet. |
| 0x01 | Enable | Indicates to enable directed proxy functionality for the identified subnet. |
| 0x02−0xFE | Prohibited | Prohibited |
| 0xFF | Do Not Process | The field is not processed |

Table 4.202. Values of the Directed_Proxy field of the DIRECTED_CONTROL_SET message

If the value of the Directed_Proxy_Use_Directed_Default field is Disable or Enable, then the Directed_Proxy_Use_Directed_Default field determines the new Directed Proxy Use Directed Default state for the identified subnet, as defined in [Section 4.2.26.4](index-en.html#UUID-04cdd8a9-ea09-11c6-bdb9-d01d12540472 "4.2.26.4. Directed Proxy Use Directed Default").

[Table 4.203](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.203 "Table 4.203. Values of the Directed_Proxy_Use_Directed_Default field of the DIRECTED_CONTROL_SET message ") defines the values of the Directed_Proxy_Use_Directed_Default
field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Indicates the new default value of the Use_Directed parameter of the Directed Proxy Server for the identified subnet |
| 0x01 | Enable | Indicates the new default value of the Use_Directed parameter of the Directed Proxy Server for the identified subnet |
| 0x02−0xFE | Prohibited | Prohibited |
| 0xFF | Do Not Process | The field is not processed |

Table 4.203. Values of the Directed_Proxy_Use_Directed_Default field of the DIRECTED_CONTROL_SET message

If the value of the Directed_Proxy field is either Do Not Process or Disabled, then the value of the Directed_Proxy_Use_Directed_Default field shall be set to Do Not Process. If the value of the Directed_Proxy field is Enable, then the value of the Directed_Proxy_Use_Directed_Default field shall be set to either Disable or
Enable.

If the value of the Directed_Friend field is Disable or Enable, then the Directed_Friend field determines the new Directed Friend state for the identified subnet, as defined in [Section 4.2.26.5](index-en.html#UUID-1a85383c-b86c-df9b-b4cc-889b0865e1fe "4.2.26.5. Directed Friend").

[Table 4.204](index-en.html#UUID-79026424-ac9c-1c3a-4378-be332d33ff6a_Table_4.204 "Table 4.204. Values of the Directed_Friend field of the DIRECTED_CONTROL_SET message") defines the values of the Directed_Friend field.

| Value | Name | Description |
| --- | --- | --- |
| 0x00 | Disable | Indicates to disable directed friend functionality for the identified subnet. |
| 0x01 | Enable | Indicates to enable directed friend functionality for the identified subnet. |
| 0x02−0xFE | Prohibited | Prohibited |
| 0xFF | Do Not Process | The field is not processed |

Table 4.204. Values of the Directed_Friend field of the DIRECTED_CONTROL_SET message

If the Directed_Forwarding field is set to Disable, then the Enable value is Prohibited for any of the Directed_Relay, Directed_Proxy, and Directed_Friend fields.

##### 4.3.5.5. DIRECTED_CONTROL_STATUS

A DIRECTED_CONTROL_STATUS message is an unacknowledged message used to report the current Directed Control state of a subnet (see [Section 4.2.26](index-en.html#UUID-26bfef24-6d38-7b00-55a7-909e5862e7ad "4.2.26. Directed Control")).

[Table 4.205](index-en.html#UUID-8ff62789-4d08-406a-53f9-25ac937e267e_Table_4.205 "Table 4.205. DIRECTED_CONTROL_STATUS message structure") defines the structure of the DIRECTED_CONTROL_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Directed_Forwarding | 8 | Current Directed Forwarding state | M |
| Directed_Relay | 8 | Current Directed Relay state | M |
| Directed_Proxy | 8 | Current Directed Proxy state or 0xFF | M |
| Directed_Proxy_Use_Directed_Default | 8 | Current Directed Proxy Use Directed Default state or 0xFF | M |
| Directed_Friend | 8 | Current Directed Friend state or 0xFF | M |

Table 4.205. DIRECTED_CONTROL_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Directed Control state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Directed Control state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Directed_Forwarding field indicates the current Directed Forwarding state for the identified subnet, as defined in [Section 4.2.26.1](index-en.html#UUID-76e0b3d3-4024-6fea-16f8-4698690725d7 "4.2.26.1. Directed Forwarding").

The Directed_Relay field indicates the current Directed Relay state for the identified subnet, as defined in [Section 4.2.26.2](index-en.html#UUID-539af574-8676-a61c-5e6f-b26f58c259d1 "4.2.26.2. Directed Relay").

The Directed_Proxy field indicates the current Directed Proxy state for the identified subnet, as defined in [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy"), or reports 0xFF.

The Directed_Proxy_Use_Directed_Default field indicates the current Directed Proxy Use Directed Default state for the identified subnet, as defined in [Section 4.2.26.4](index-en.html#UUID-04cdd8a9-ea09-11c6-bdb9-d01d12540472 "4.2.26.4. Directed Proxy Use Directed Default"), or reports 0xFF.

The Directed_Friend field indicates the current Directed Friend state for the identified subnet, as defined in [Section 4.2.26.5](index-en.html#UUID-1a85383c-b86c-df9b-b4cc-889b0865e1fe "4.2.26.5. Directed Friend"), or reports 0xFF.

##### 4.3.5.6. PATH_METRIC_GET

A PATH_METRIC_GET message is an acknowledged message used to get the current Path Metric state of a node (see [Section 4.2.27](index-en.html#UUID-37c55d17-2b41-9a57-03f6-db8046a3c215 "4.2.27. Path Metric")).

The response to a PATH_METRIC_GET message is a PATH_METRIC_STATUS message.

[Table 4.206](index-en.html#UUID-b57aa37c-54ce-2017-9ede-dd9a3a6f0565_Table_4.206 "Table 4.206. PATH_METRIC_GET message structure") defines the structure of the PATH_METRIC_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.206. PATH_METRIC_GET message structure

The Opcode field shall contain the opcode value for the PATH_METRIC_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Metric state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.7. PATH_METRIC_SET

A PATH_METRIC_SET message is an acknowledged message used to set the Path Metric state of a node (see [Section 4.2.27](index-en.html#UUID-37c55d17-2b41-9a57-03f6-db8046a3c215 "4.2.27. Path Metric")).

The response to a PATH_METRIC_SET message is a PATH_METRIC_STATUS message.

[Table 4.207](index-en.html#UUID-58815237-4306-fd56-3cbd-68ec8618261e_Table_4.207 "Table 4.207. PATH_METRIC_SET message structure") defines the structure of the PATH_METRIC_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Metric_Type | 3 | New Path Metric Type state | M |
| Path_Lifetime | 2 | New Path Lifetime state | M |
| Prohibited | 3 | Prohibited | M |

Table 4.207. PATH_METRIC_SET message structure

The Opcode field shall contain the opcode value for the PATH_METRIC_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Metric state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Metric_Type field determines the new Path Metric Type state for the node, as defined in [Section 4.2.27.1](index-en.html#UUID-1219fa02-97bf-c8c9-848a-9fc17f223db1 "4.2.27.1. Path Metric Type").

The Path_Lifetime field determines the new Path Lifetime state for the node, as defined in [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime").

##### 4.3.5.8. PATH_METRIC_STATUS

A PATH_METRIC_STATUS message is an unacknowledged message used to report the current Path Metric state of a node (see [Section 4.2.27](index-en.html#UUID-37c55d17-2b41-9a57-03f6-db8046a3c215 "4.2.27. Path Metric")).

[Table 4.208](index-en.html#UUID-574eead8-2c3c-530b-c5f2-e08f1698eb05_Table_4.208 "Table 4.208. PATH_METRIC_STATUS message structure") defines the structure of the PATH_METRIC_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Metric_Type | 3 | Current Path Metric Type state | M |
| Path_Lifetime | 2 | Current Path Lifetime state | M |
| Prohibited | 3 | Prohibited | M |

Table 4.208. PATH_METRIC_STATUS message structure

The Opcode field shall contain the opcode value for the PATH_METRIC_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Path Metric state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Metric state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Metric_Type field indicates the current Path Metric Type state for the node, as defined in [Section 4.2.27.1](index-en.html#UUID-1219fa02-97bf-c8c9-848a-9fc17f223db1 "4.2.27.1. Path Metric Type").

The Path_Lifetime field indicates the current Path Lifetime state for the node, as defined in [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime").

##### 4.3.5.9. DISCOVERY_TABLE_CAPABILITIES_GET

A DISCOVERY_TABLE_CAPABILITIES_GET message is an acknowledged message used to get the current Discovery Table Capabilities state of a node (see [Section 4.2.28](index-en.html#UUID-cd835a58-3802-7e57-32e1-75431f2da4c8 "4.2.28. Discovery Table Capabilities")).

The response to a DISCOVERY_TABLE_CAPABILITIES_GET message is a DISCOVERY_TABLE_CAPABILITIES_STATUS message.

[Table 4.209](index-en.html#UUID-f2e1277a-1c8f-53b3-4aa3-e39a63347c13_Table_4.209 "Table 4.209. DISCOVERY_TABLE_CAPABILITIES_GET message structure") defines the structure of the DISCOVERY_TABLE_CAPABILITIES_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.209. DISCOVERY_TABLE_CAPABILITIES_GET message structure

The Opcode field shall contain the opcode value for the DISCOVERY_TABLE_CAPABILITIES_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Discovery Table Capabilities state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.10. DISCOVERY_TABLE_CAPABILITIES_SET

A DISCOVERY_TABLE_CAPABILITIES_SET message is an acknowledged message used to set the Max Concurrent Init state of a node (see [Section 4.2.28.2](index-en.html#UUID-e37303da-42b9-e0ba-5e52-efc1fc194309 "4.2.28.2. Max Concurrent Init")).

The response to a DISCOVERY_TABLE_CAPABILITIES_SET message is a DISCOVERY_TABLE_CAPABILITIES_STATUS message.

[Table 4.210](index-en.html#UUID-9b7d3672-c5ee-88e4-0a9f-4cbb36acf674_Table_4.210 "Table 4.210. DISCOVERY_TABLE_CAPABILITIES_SET message structure") defines the structure of the DISCOVERY_TABLE_CAPABILITIES_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Max_Concurrent_Init | 8 | New Max Concurrent Init state | M |

Table 4.210. DISCOVERY_TABLE_CAPABILITIES_SET message structure

The Opcode field shall contain the opcode value for the DISCOVERY_TABLE_CAPABILITIES_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Max Concurrent Init state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Max_Concurrent_Init field determines the new Max Concurrent Init state for the node, as defined in [Section 4.2.28.2](index-en.html#UUID-e37303da-42b9-e0ba-5e52-efc1fc194309 "4.2.28.2. Max Concurrent Init").

##### 4.3.5.11. DISCOVERY_TABLE_CAPABILITIES_STATUS

A DISCOVERY_TABLE_CAPABILITIES_STATUS message is an unacknowledged message used to report the current Discovery Table Capabilities state of a node (see [Section 4.2.28](index-en.html#UUID-cd835a58-3802-7e57-32e1-75431f2da4c8 "4.2.28. Discovery Table Capabilities")).

[Table 4.211](index-en.html#UUID-8c0475bc-38fe-49d9-d99c-3e8d9c6ded68_Table_4.211 "Table 4.211. DISCOVERY_TABLE_CAPABILITIES_STATUS message structure") defines the structure of the DISCOVERY_TABLE_CAPABILITIES_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Max_Concurrent_Init | 8 | Current Max Concurrent Init state | M |
| Max_Discovery_Table_Entries_Count | 8 | Max Discovery Table Entries Count state | M |

Table 4.211. DISCOVERY_TABLE_CAPABILITIES_STATUS message structure

The Opcode field shall contain the opcode value for the DISCOVERY_TABLE_CAPABILITIES_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Discovery Table Capabilities state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Discovery Table Capabilities state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Max_Concurrent_Init field indicates the current Max Concurrent Init state of the node, as defined in [Section 4.2.28.2](index-en.html#UUID-e37303da-42b9-e0ba-5e52-efc1fc194309 "4.2.28.2. Max Concurrent Init").

The Max_Discovery_Table_Entries_Count field indicates the Max Discovery Table Entries Count state of the node, as defined in [Section 4.2.28.1](index-en.html#UUID-b4fb8e0e-c8b5-f1a2-370c-c1acd2133ba3 "4.2.28.1. Max Discovery Table Entries Count").

##### 4.3.5.12. FORWARDING_TABLE_ADD

A FORWARDING_TABLE_ADD message is an acknowledged message used to add a fixed path entry to the Forwarding Table state of a node or to update an existing fixed path entry (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")).

The response to a FORWARDING_TABLE_ADD message is a FORWARDING_TABLE_STATUS message.

[Table 4.212](index-en.html#UUID-55678ec8-52b4-5e1b-80a9-e1890ef5e135_Table_4.212 "Table 4.212. FORWARDING_TABLE_ADD message structure") defines the structure of the FORWARDING_TABLE_ADD message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 8 | The message opcode | M |
| NetKeyIndex | 12 | NetKey Index of the NetKey used in the subnet | M |
| Prohibited | 2 | Prohibited | M |
| Unicast_Destination_Flag | 1 | Indicates whether or not the destination of the path is a unicast address | M |
| Backward_Path_Validated_Flag | 1 | Indicates whether or not the backward path has been validated | M |
| Path_Origin_Unicast_Addr_Range | variable  (16 or 24) | Unicast address range of the Path Origin | M |
| Path_Target_Unicast_Addr_Range | variable  (16 or 24) | Unicast address range of the Path Target | C.1 |
| Multicast_Destination | 16 | Multicast destination address | C.2 |
| Bearer_Toward_Path_Origin | 16 | Index of the bearer toward the Path Origin | M |
| Bearer_Toward_Path_Target | 16 | Index of the bearer toward the Path Target | M |

Table 4.212. FORWARDING_TABLE_ADD message structure

C.1:
:   If the value of the Unicast_Destination_Flag field is 1, then the Path_Target_Unicast_Addr_Range field shall be present; otherwise, the Path_Target_Unicast_Addr_Range field shall not be present.

C.2:
:   If the value of the Unicast_Destination_Flag field is 0, then the Multicast_Destination field shall be present; otherwise, the Multicast_Destination field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_ADD message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state.

The Unicast_Destination_Flag field determines whether the Destination field in the Forwarding Table entry is a unicast address (Unicast_Destination_Flag = 1) or not (Unicast_Destination_Flag = 0).

The Backward_Path_Validated_Flag field determines whether the backward path is validated (Backward_Path_Validated_Flag = 1) or not (Backward_Path_Validated_Flag = 0). If the Unicast_Destination_Flag field is 0, then the Backward_Path_Validated_Flag field shall be 0.

The Path_Origin_Unicast_Addr_Range field contains the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Path Origin in the Forwarding Table entry.

If present, the Path_Target_Unicast_Addr_Range field contains the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the Path Target in the Forwarding Table entry. Any
address derived from the Path_Origin_Unicast_Addr_Range field shall be different from any address derived from the Path_Target_Unicast_Addr_Range field.

If present, the Multicast_Destination field identifies the group address or the virtual address of the Destination field in the Forwarding Table entry. The all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Multicast_Destination field.

The Bearer_Toward_Path_Origin field determines the index of the bearer to be used for directed forwarding toward the Path Origin in the Forwarding Table entry.

The Bearer_Toward_Path_Target field determines the index of the bearer to be used for directed forwarding toward the Path Target in the Forwarding Table entry.

##### 4.3.5.13. FORWARDING_TABLE_DELETE

A FORWARDING_TABLE_DELETE message is an acknowledged message used to delete all the path entries from a specific Path Origin to a specific destination from the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")).

The response to a FORWARDING_TABLE_DELETE message is a FORWARDING_TABLE_STATUS message.

[Table 4.213](index-en.html#UUID-5b1dcf5c-6a3f-2a97-b532-93b69123a632_Table_4.213 "Table 4.213. FORWARDING_TABLE_DELETE message structure") defines the structure of the FORWARDING_TABLE_DELETE message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |

Table 4.213. FORWARDING_TABLE_DELETE message structure

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DELETE message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Origin and Destination fields identify respectively the Path Origin and the destination of the path entries to be deleted from the Forwarding Table state. The unassigned address, group addresses, and virtual addresses are Prohibited for the Path_Origin field. The unassigned address and the
all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Destination field. The Path_Origin and Destination fields shall not have the same value.

##### 4.3.5.14. FORWARDING_TABLE_STATUS

A FORWARDING_TABLE_STATUS message is an unacknowledged message used to report the status of the most recent operation performed on the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")).

[Table 4.214](index-en.html#UUID-3725bb57-444d-817e-b6ac-089f710ad8cb_Table_4.214 "Table 4.214. FORWARDING_TABLE_STATUS message structure") defines the structure of the FORWARDING_TABLE_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |

Table 4.214. FORWARDING_TABLE_STATUS message structure

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Forwarding Table state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The other fields in [Table 4.214](index-en.html#UUID-3725bb57-444d-817e-b6ac-089f710ad8cb_Table_4.214 "Table 4.214. FORWARDING_TABLE_STATUS message structure") contain the values used in the most recent operation to add or delete an entry in the Forwarding Table
state.

The Path_Origin and Destination fields identify respectively the Path Origin and the destination of the path entries that have been added to or deleted from the Forwarding Table state in the most recent operation. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.
The unassigned address is a prohibited value for the Destination field.

##### 4.3.5.15. FORWARDING_TABLE_DEPENDENTS_ADD

A FORWARDING_TABLE_DEPENDENTS_ADD message is an acknowledged message used to add entries to the Dependent_Origin_List field or to the Dependent_Target_List field of a fixed path entry in the Forwarding Table state of a node.

The response to a FORWARDING_TABLE_DEPENDENTS_ADD message is a FORWARDING_TABLE_DEPENDENTS_STATUS message.

[Table 4.215](index-en.html#UUID-78f62b88-e639-5f4f-fc05-d867c28592b0_Table_4.215 "Table 4.215. FORWARDING_TABLE_DEPENDENTS_ADD message structure") defines the structure of the FORWARDING_TABLE_DEPENDENTS_ADD message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 8 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |
| Dependent_Origin_­Unicast_­Addr_­Range_­List_­Size | 8 | Number of entries in the Dependent_Origin_­Unicast_­Addr_­Range_­List field of the message | M |
| Dependent_Target_­Unicast_­Addr_­Range_­List_­Size | 8 | Number of entries in the Dependent_Target_­Unicast_­Addr_­Range_­List field of the message | M |
| Dependent_Origin_­Unicast_­Addr_­Range_­List | variable | List of the unicast address ranges of the dependent nodes of the Path Origin | C.1 |
| Dependent_Target_Unicast_­Addr_­Range_­List | variable | List of the unicast address ranges of the dependent nodes of the Path Target | C.2 |

Table 4.215. FORWARDING_TABLE_DEPENDENTS_ADD message structure

C.1:
:   If the value of the Dependent_Origin_Unicast_Addr_Range_List_Size field is greater than 0, then the Dependent_Origin_Unicast_Addr_Range_List field shall be present; otherwise, the Dependent_Origin_Unicast_Addr_Range_List field shall not be present.

C.2:
:   If the value of the Dependent_Target_Unicast_Addr_Range_List_Size field is greater than 0, then the Dependent_Target_Unicast_Addr_Range_List field shall be present; otherwise, the Dependent_Target_Unicast_Addr_Range_List field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DEPENDENTS_ADD message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Origin field identifies the Path Origin of the path entry. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

The Destination field identifies the Path Target of the path entry. The unassigned address and the all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Destination field. The Path_Origin and Destination fields shall not have the same value.

The Dependent_Origin_Unicast_Addr_Range_List_Size field represents the number of entries in the Dependent_Origin_Unicast_Addr_Range_List field of the message.

If the Destination field contains a unicast address, the Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field represents the number of entries in the Dependent_­Target_­Unicast_­Addr_­Range_­List field of the message. Otherwise, values greater than 0 are prohibited for the
Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field.

The value of either the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size field or the Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field shall not be 0. Both the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size field and the Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field may have a non-zero value.

If present, the Dependent_­Origin_­Unicast_­Addr_­Range_­List field contains the list of unicast address ranges of the dependent nodes of the Path Origin of the path entry. Any address derived from unicast address ranges in the Dependent_­Origin_­Unicast_­Addr_­Range_­List field shall be different from the Path_Origin field
value and shall be different from the Destination field value.

If present, the Dependent_­Target_­Unicast_­Addr_­Range_­List field contains the list of unicast address ranges of the dependent nodes of the Path Target of the path entry. Any address derived from unicast address ranges in the Dependent_­Target_­Unicast_­Addr_­Range_­List field shall be different from the Path_Origin field
value and shall be different from the Destination field value.

If the Dependent_­Origin_­Unicast_­Addr_­Range_­List and Dependent_­Target_­Unicast_­Addr_­Range_­List fields are both present, each address derived from unicast address ranges in the Dependent_­Origin_­Unicast_­Addr_­Range_­List field shall be different from any address derived from unicast address ranges in the
Dependent_­Target_­Unicast_­Addr_­Range_­List field.

##### 4.3.5.16. FORWARDING_TABLE_DEPENDENTS_DELETE

A FORWARDING_TABLE_DEPENDENTS_DELETE message is an acknowledged message used to delete dependent node entries from the Dependent_Origin_List field or the Dependent_Target_List field of a fixed path entry in the Forwarding Table state of a node.

The response to a FORWARDING_TABLE_DEPENDENTS_DELETE message is a FORWARDING_TABLE_DEPENDENTS_STATUS message.

[Table 4.216](index-en.html#UUID-3a5a9174-3221-b34f-8b46-1abea997c24d_Table_4.216 "Table 4.216. FORWARDING_TABLE_DEPENDENTS_DELETE message structure") defines the structure of the FORWARDING_TABLE_DEPENDENTS_DELETE message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |
| Dependent_Origin_List_Size | 8 | Number of entries in the Dependent_Origin_List field of the message (N1) | M |
| Dependent_Target_List_Size | 8 | Number of entries in the Dependent_Target_List field of the message (N2) | M |
| Dependent_Origin_List | variable  (16*N1) | List of the primary element addresses of the dependent nodes of the Path Origin | C.1 |
| Dependent_Target_List | variable  (16*N2) | List of the primary element addresses of the dependent nodes of the Path Target | C.2 |

Table 4.216. FORWARDING_TABLE_DEPENDENTS_DELETE message structure

C.1:
:   If the value of the Dependent_Origin_List_Size field is greater than 0, then the Dependent_Origin_List field shall be present; otherwise, the Dependent_Origin_List field shall not be present.

C.2:
:   If the value of the Dependent_Target_List_Size field is greater than 0, then the Dependent_Target_List field shall be present; otherwise, the Dependent_Target_List field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DEPENDENTS_DELETE message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Origin field identifies the Path Origin of the path entry. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

The Destination field identifies the Path Target of the path entry. The unassigned address and the all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Destination field. The Path_Origin and Destination fields shall not have the same value.

The Dependent_Origin_List_Size field represents the number of entries in the Dependent_Origin_List field of the message.

If the Destination field contains a unicast address, the Dependent_Target_List_Size field represents the number of entries in the Dependent_Target_List field of the message. Otherwise, values greater than 0 are prohibited for the Dependent_Target_List_Size field.

The value of either the Dependent_Origin_List_Size field or the Dependent_Target_List_Size field shall not be 0. Both the Dependent_Origin_List_Size field and the Dependent_Target_List_Size field may have a non-zero value.

If present, the Dependent_Origin_List field contains the list of the primary element addresses of the dependent nodes of the Path Origin of the path entry. The Dependent_Origin_List field shall not contain the address indicated by the Path_Origin field and shall not contain the address indicated by the Destination field.

If present, the Dependent_Target_List field contains the list of the primary element addresses of the dependent nodes of the Path Target of the path entry. The Dependent_Target_List field shall not contain the address indicated by the Path_Origin field and shall not contain the address indicated by the Destination field.

If the Dependent_Origin_List and Dependent_Target_List fields are both present, each address in the Dependent_Origin_List field shall be different from any address in the Dependent_Target_List field.

##### 4.3.5.17. FORWARDING_TABLE_DEPENDENTS_STATUS

A FORWARDING_TABLE_DEPENDENTS_STATUS message is an unacknowledged message used to report the status of the most recent operation performed on the Dependent_Origin_List field or the Dependent_Target_List field of a fixed path entry in the Forwarding Table state of a node.

This message is a response to a FORWARDING_TABLE_DEPENDENTS_ADD message or to a FORWARDING_TABLE_DEPENDENTS_DELETE message.

[Table 4.217](index-en.html#UUID-87e8b134-d1fb-987a-40e9-34bca20a9bae_Table_4.217 "Table 4.217. FORWARDING_TABLE_DEPENDENTS_STATUS message structure") defines the structure of the FORWARDING_TABLE_DEPENDENTS_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code of the most recent operation | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |

Table 4.217. FORWARDING_TABLE_DEPENDENTS_STATUS message structure

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DEPENDENTS_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Dependent_Origin_List or Dependent_Target_List fields of the fixed path entry in the Forwarding Table state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Path_Origin field identifies the Path Origin of the path entry. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

The Destination field identifies the Path Target of the path entry. The unassigned address is a prohibited value for the Destination field.

##### 4.3.5.18. FORWARDING_TABLE_ENTRIES_COUNT_GET

A FORWARDING_TABLE_ENTRIES_COUNT_GET message is an acknowledged message used to get the information about the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")).

The response to a FORWARDING_TABLE_ENTRIES_COUNT_GET message is a FORWARDING_TABLE_ENTRIES_COUNT_STATUS message.

[Table 4.218](index-en.html#UUID-8737d2c2-9c74-e627-4f44-3f223460d704_Table_4.218 "Table 4.218. FORWARDING_TABLE_ENTRIES_COUNT_GET message structure") defines the structure of the FORWARDING_TABLE_ENTRIES_COUNT_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | Index of the NetKey | M |

Table 4.218. FORWARDING_TABLE_ENTRIES_COUNT_GET message structure

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_ENTRIES_COUNT_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.19. FORWARDING_TABLE_ENTRIES_COUNT_STATUS

A FORWARDING_TABLE_ENTRIES_COUNT_STATUS message is an unacknowledged message used to report the information about the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")).

This message is a response to a FORWARDING_TABLE_ENTRIES_COUNT_GET message.

[Table 4.219](index-en.html#UUID-a637408f-638d-635e-0356-af3e152a5b28_Table_4.219 "Table 4.219. FORWARDING_TABLE_ENTRIES_COUNT_STATUS message structure") defines the structure of the FORWARDING_TABLE_ENTRIES_COUNT_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code of the requesting message | M |
| NetKeyIndex | 16 | Index of the NetKey | M |
| Forwarding_Table_Update_Identifier | 16 | Current Forwarding Table Update Identifier state | C.1 |
| Fixed_Path_Entries_Count | 16 | Number of fixed path entries in the Forwarding Table | C.1 |
| Non_Fixed_Path_Entries_Count | 16 | Number of non-fixed path entries in the Forwarding Table | C.1 |

Table 4.219. FORWARDING_TABLE_ENTRIES_COUNT_STATUS message structure

C.1:
:   If the value of the Status field is Success, then the Forwarding_Table_Update_Identifier, Fixed_Path_Entries_Count, and Non_Fixed_Path_Entries_Count fields shall be present; otherwise, the Forwarding_Table_Update_Identifier, Fixed_Path_Entries_Count, and Non_Fixed_Path_Entries_Count fields shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_ENTRIES_COUNT_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent FORWARDING_TABLE_ENTRIES_COUNT_GET operation on the Forwarding Table state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

If present, the Forwarding_Table_Update_Identifier field indicates the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

If present, the Fixed_Path_Entries_Count field indicates the number of fixed path entries in the Forwarding Table state.

If present, the Non_Fixed_Path_Entries_Count field indicates the number of non-fixed path entries in the Forwarding Table state.

##### 4.3.5.20. FORWARDING_TABLE_ENTRIES_GET

A FORWARDING_TABLE_ENTRIES_GET message is an acknowledged message used to get a filtered set of path entries in the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")). The path
entries can be filtered to fixed path entries or non-fixed path entries or to path entries for a given Path Origin or destination.

The response to a FORWARDING_TABLE_ENTRIES_GET message is a FORWARDING_TABLE_ENTRIES_STATUS message.

[Table 4.220](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.220 "Table 4.220. FORWARDING_TABLE_ENTRIES_GET message structure") defines the structure of the FORWARDING_TABLE_ENTRIES_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 12 | Index of the NetKey | M |
| Filter_Mask | 4 | Filter to be applied to the Forwarding Table entries | M |
| Start_Index | 16 | Start offset to read in units of Forwarding Table entries | M |
| Path_Origin | 16 | Primary element address of the Path Origin | C.1 |
| Destination | 16 | Destination address | C.2 |
| Forwarding_Table_Update_Identifier | 16 | Last saved Forwarding Table Update Identifier state | O |

Table 4.220. FORWARDING_TABLE_ENTRIES_GET message structure

C.1:
:   If the Path_Origin_Match bit field in the Filter_Mask field is set to 1, then the Path_Origin field shall be present; otherwise, the Path_Origin field shall not be present.

C.2:
:   If the Destination_Match bit field in the Filter_Mask field is set to 1, then the Destination field shall be present; otherwise, the Destination field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_ENTRIES_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state.

The Filter_Mask field indicates the filtering applied to the entries of the Forwarding Table state when reporting the status.

[Table 4.221](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.221 "Table 4.221. Description of the Filter_Mask bits") defines the structure of the Filter_Mask field. Bits 0 and 1 of the Filter_Mask field shall not both be set to 0.

| Bit | Name | Description |
| --- | --- | --- |
| 0 | Fixed_Paths | Return fixed path entries (see [Table 4.222](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.222 "Table 4.222. Filter_Mask field bit values")) |
| 1 | Non_Fixed_Paths | Return non-fixed path entries (see [Table 4.222](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.222 "Table 4.222. Filter_Mask field bit values")) |
| 2 | Path_Origin_Match | Return path entries with a matching Path_Origin (see [Table 4.222](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.222 "Table 4.222. Filter_Mask field bit values")) |
| 3 | Destination_Match | Return path entries with a matching Destination (see [Table 4.222](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.222 "Table 4.222. Filter_Mask field bit values")) |

Table 4.221. Description of the Filter_Mask bits

Filter_Mask field bits values are defined in [Table 4.222](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.222 "Table 4.222. Filter_Mask field bit values").

| Bit Value | Description |
| --- | --- |
| 0 | Indicated by the Filter_Mask bit path entries not being returned |
| 1 | Indicated by the Filter_Mask bit path entries being returned |

Table 4.222. Filter_Mask field bit values

The Start_Index field determines the offset in units of Forwarding Table entries to start from when reporting the filtered set of path entries of the Forwarding Table state.

If present, the Path_Origin field reports the primary element address of the Path Origin to be matched when filtering the path entries in the Forwarding Table state. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

If present, the Destination field reports the destination to be matched when filtering the path entries in the Forwarding Table state. The unassigned address and the all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Destination field.

If the Path_Origin and Destination fields are both present, the fields shall not have the same value.

If present, the Forwarding_Table_Update_Identifier field reports the last saved value of the Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

##### 4.3.5.21. FORWARDING_TABLE_ENTRIES_STATUS

A FORWARDING_TABLE_ENTRIES_STATUS message is an unacknowledged message used to report status information for a filtered set of path entries in the Forwarding Table state of a node (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")), optionally including a list of path entries.

This message is a response to the FORWARDING_TABLE_ENTRIES_GET message.

[Table 4.223](index-en.html#UUID-8189be4b-6543-b24b-fa54-fa5109b154bc_Table_4.223 "Table 4.223. FORWARDING_TABLE_ENTRIES_STATUS message structure") defines the structure of the FORWARDING_TABLE_ENTRIES_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code of the requesting message | M |
| NetKeyIndex | 12 | Index of the NetKey | M |
| Filter_Mask | 4 | Filter applied to the Forwarding Table entries | M |
| Start_Index | 16 | Start offset in units of Forwarding Table entries | M |
| Path_Origin | 16 | Primary element address of the Path Origin | C.1 |
| Destination | 16 | Destination address | C.2 |
| Forwarding_Table_Update_Identifier | 16 | Current Forwarding Table Update Identifier state | C.3 |
| Forwarding_Table_Entry_List | variable | List of Forwarding Table entries | O |

Table 4.223. FORWARDING_TABLE_ENTRIES_STATUS message structure

C.1:
:   If the Path_Origin_Match bit field in the Filter_Mask field is set to 1, then the Path_Origin field shall be present; otherwise, the Path_Origin field shall not be present.

C.2:
:   If the Destination_Match bit field in the Filter_Mask field is set to 1, then the Destination field shall be present; otherwise, the Destination field shall not be present.

C.3:
:   If the value of the Status field is either Success or Obsolete Information, then the Forwarding_Table_Update_Identifier field shall be present; otherwise, the Forwarding_Table_Update_Identifier field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_ENTRIES_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent FORWARDING_TABLE_ENTRIES_GET message. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state.

The Filter_Mask field indicates the filtering applied to the entries of the Forwarding Table state, when reporting the status. The Filter_Mask field is described in [Table 4.221](index-en.html#UUID-64adf066-7b53-4c61-60da-27ae14988c4a_Table_4.221 "Table 4.221. Description of the Filter_Mask bits"). Bits 0 and 1 of the Filter_Mask field shall not both be set to 0.

The Start_Index field indicates the offset in units of Forwarding Table entries used when reporting the filtered set of path entries of the Forwarding Table state.

If present, the Path_Origin field reports the primary element address of the Path Origin that was matched when filtering the entries in the Forwarding Table state. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

If present, the Destination field reports the destination that was matched when filtering the entries in the Forwarding Table state. The unassigned address is a prohibited value for the Destination field.

If present, the Forwarding_Table_Update_Identifier field indicates the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

If present, the Forwarding_Table_Entry_List field contains the filtered set of path entries of the Forwarding Table state. The format of the fixed path entries and non-fixed path entries in the Forwarding_Table_Entry_List field is defined in [Section 4.3.5.1](index-en.html#UUID-4c3dd561-07e1-77ef-1fcb-c5d6a1315dd8 "4.3.5.1. Forwarding Table path entries format").

##### 4.3.5.22. FORWARDING_TABLE_DEPENDENTS_GET

A FORWARDING_TABLE_DEPENDENTS_GET message is an acknowledged message used to get the list of unicast address ranges of dependent nodes of the Path Origin or the Path Target of a Forwarding Table entry.

The response to a FORWARDING_TABLE_DEPENDENTS_GET message is a FORWARDING_TABLE_DEPENDENTS_GET_STATUS message.

[Table 4.224](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.224 "Table 4.224. FORWARDING_TABLE_DEPENDENTS_GET message structure ") defines the structure of the FORWARDING_TABLE_DEPENDENTS_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 12 | Index of the NetKey | M |
| Dependents_List_Mask | 2 | Filter applied to the lists of unicast address ranges for dependent nodes | M |
| Fixed_Path_Flag | 1 | Flag indicating whether or not to return the unicast address ranges of dependent nodes in a fixed path entry | M |
| Prohibited | 1 | Prohibited | M |
| Start_Index | 16 | Start offset in units of unicast address ranges | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |
| Forwarding_Table_Update_Identifier | 16 | Last saved Forwarding Table Update Identifier state | O |

Table 4.224. FORWARDING_TABLE_DEPENDENTS_GET message structure

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DEPENDENTS_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state.

The Dependents_List_Mask field determines the filter to be applied to the lists of unicast address ranges for dependent nodes. Bits 0 and 1 of the Dependents_List_Mask field shall not both be set to 0.

[Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description") defines the structure of the Dependents_List_Mask field.

| Bit | Description |
| --- | --- |
| 0 | Return list of unicast address ranges of dependent nodes of the Path Origin (see [Table 4.226](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.226 "Table 4.226. Dependents_List_Mask field bit values")) |
| 1 | Return list of unicast address ranges of dependent nodes of the Path Target (see [Table 4.226](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.226 "Table 4.226. Dependents_List_Mask field bit values")) |

Table 4.225. Dependents_List_Mask field description

Dependents_List_Mask field bits values are defined in [Table 4.226](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.226 "Table 4.226. Dependents_List_Mask field bit values").

| Bit Value | Description |
| --- | --- |
| 0 | Indicated by the Dependents_List_Mask bit list of unicast address ranges not being returned |
| 1 | Indicated by the Dependents_List_Mask bit list of unicast address ranges being returned |

Table 4.226. Dependents_List_Mask field bit values

The Fixed_Path_Flag field indicates whether to return the unicast address ranges of dependent nodes in a fixed path entry or in a non-fixed path entry. Fixed_Path_Flag field values are defined in [Table 4.227](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.227 "Table 4.227. Fixed_Path_Flag field values").

| Value | Description |
| --- | --- |
| 0 | Return the unicast address ranges of dependent nodes in a non-fixed path entry |
| 1 | Return the unicast address ranges of dependent nodes in a fixed path entry |

Table 4.227. Fixed_Path_Flag field values

The Start_Index field determines the offset in units of unicast address ranges to start from when reporting the filtered lists of unicast address ranges of dependent nodes.

The Path_Origin field reports the primary element address of the Path Origin to be matched in the Forwarding Table entry. The unassigned address, group addresses, and virtual addresses are prohibited values for the Path_Origin field.

The Destination field reports the destination to be matched in the Forwarding Table entry. The unassigned address and the all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses are Prohibited for the Destination field. If the Destination field is a group address or a virtual address, then bit 1 in the
Dependents_List_Mask (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")) field shall be 0. The Path_Origin and Destination fields shall not have the same value.

If present, the Forwarding_Table_Update_Identifier field reports the last saved value of the Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

##### 4.3.5.23. FORWARDING_TABLE_DEPENDENTS_GET_STATUS

A FORWARDING_TABLE_DEPENDENTS_GET_STATUS message is an unacknowledged message used to report status information for a filtered list of unicast address ranges of dependent nodes of the Path Origin or the Path Target of a Forwarding Table entry.

The message is a response to the FORWARDING_TABLE_DEPENDENTS_GET message.

[Table 4.228](index-en.html#UUID-8c0fc007-0b18-0324-786a-c72c1bc43416_Table_4.228 "Table 4.228. FORWARDING_TABLE_DEPENDENTS_GET_STATUS message structure ") defines the structure of the FORWARDING_TABLE_DEPENDENTS_GET_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 12 | Index of the NetKey | M |
| Dependents_List_Mask | 2 | Filter applied to the lists of unicast address ranges for dependent nodes | M |
| Fixed_Path_Flag | 1 | Flag indicating whether or not to return the unicast address ranges of dependent nodes in a fixed path entry | M |
| Prohibited | 1 | Prohibited | M |
| Start_Index | 16 | Start offset in units of unicast address ranges | M |
| Path_Origin | 16 | Primary element address of the Path Origin | M |
| Destination | 16 | Destination address | M |
| Forwarding_Table_­Update_­Identifier | 16 | Current Forwarding Table Update Identifier state | C.1 |
| Dependent_Origin_­Unicast_­Addr_­Range_­List_­Size | 8 | Number of unicast address ranges in the Dependent_Origin_Unicast_Addr_Range_List field in the message | C.2 |
| Dependent_Target_­Unicast_­Addr_­Range_­List_­Size | 8 | Number of unicast address ranges in the Dependent_Target_Unicast_Addr_Range_List field in the message | C.2 |
| Dependent_Origin_­Unicast_­Addr_­Range_­List | variable | List of unicast address ranges of dependent nodes of the Path Origin | C.3 |
| Dependent_Target_­Unicast_­Addr_­Range_­List | variable | List of unicast address ranges of dependent nodes of the Path Target | C.4 |

Table 4.228. FORWARDING_TABLE_DEPENDENTS_GET_STATUS message structure

C.1:
:   If the value of the Status field is either Success or Obsolete Information, then the Forwarding_­Table_­Update_­Identifier field shall be present; otherwise, the Forwarding_­Table_­Update_­Identifier field shall not be present.

C.2:
:   If the value of the Status field is Success, then the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size and Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size fields shall be present; otherwise, the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size and Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size fields shall
    not be present.

C.3:
:   If the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size field is present and its value is greater than 0, then the Dependent_­Origin_­Unicast_­Addr_­Range_­List field shall be present; otherwise, the Dependent_­Origin_­Unicast_­Addr_­Range_­List field shall not be present.

C.4:
:   If the Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field is present and its value is greater than 0, then the Dependent_­Target_­Unicast_­Addr_­Range_­List field shall be present; otherwise, the Dependent_­Target_­Unicast_­Addr_­Range_­List field shall not be present.

The Opcode field shall contain the opcode value for the FORWARDING_TABLE_DEPENDENTS_GET_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent FORWARDING_TABLE_DEPENDENTS_GET message. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Forwarding Table state.

The Dependents_List_Mask field indicates the filter applied to the lists of unicast address ranges for dependent nodes (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")).

The Fixed_Path_Flag field indicates whether to return the unicast address ranges of dependent nodes in a fixed path entry or in a non-fixed path entry. Fixed_Path_Flag field values are defined in [Table 4.229](index-en.html#UUID-8c0fc007-0b18-0324-786a-c72c1bc43416_Table_4.229 "Table 4.229. Fixed_Path_Flag field values").

| Value | Description |
| --- | --- |
| 0 | Return the unicast address ranges of dependent nodes in a non-fixed path entry |
| 1 | Return the unicast address ranges of dependent nodes in a fixed path entry |

Table 4.229. Fixed_Path_Flag field values

The Start_Index field indicates the offset in units of unicast address ranges used when reporting the filtered lists of unicast address ranges of dependent nodes.

The Path_Origin field reports the primary element address of the Path Origin that was matched in the Forwarding Table entry.

The Destination field reports the destination that was matched in the Forwarding Table entry. If the Destination field is a group address or a virtual address, then bit 1 in the Dependents_List_Mask field (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")) shall be 0.

If present, the Forwarding_Table_Update_Identifier field indicates the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

If present, the Dependent_­Origin_­Unicast_­Addr_­Range_­List_­Size field represents the number of unicast address ranges in the Dependent_­Origin_­Unicast_­Addr_­Range_­List field in the message. If bit 0 of the Dependents_List_Mask field (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")) is 0, then the value of the Dependent_­Origin_­Unicast_­Addr_­Range_­List_Size field shall be 0, and the Dependent_­Origin_­Unicast_­Addr_­Range_­List field shall not be
present.

If present, the Dependent_­Target_­Unicast_­Addr_­Range_­List_­Size field represents the number of unicast address ranges in the Dependent_­Target_­Unicast_­Addr_­Range_­List field in the message. If bit 1 of the Dependents_List_Mask field (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")) is 0, then the value of the Dependent_Target_Unicast_Addr_Range_List_Size field shall be 0, and the Dependent_­Target_­Unicast_­Addr_­Range_­List field shall not be
present.

If present, the Dependent_­Origin_­Unicast_­Addr_­Range_­List field contains the list of unicast address ranges of dependent nodes of the Path Origin.

If present, the Dependent_Target_Unicast_Addr_Range_List field contains the list of unicast address ranges of dependent nodes of the Path Target.

##### 4.3.5.24. WANTED_LANES_GET

A WANTED_LANES_GET message is an acknowledged message used to get the Wanted Lanes state of a node (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")).

The response to a WANTED_LANES_GET message is a WANTED_LANES_STATUS message.

[Table 4.230](index-en.html#UUID-5af7e89a-e8d6-038d-0691-d60049a91281_Table_4.230 "Table 4.230. WANTED_LANES_GET message structure") defines the structure of the WANTED_LANES_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.230. WANTED_LANES_GET message structure

The Opcode field shall contain the opcode value for the WANTED_LANES_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Wanted Lanes state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.25. WANTED_LANES_SET

A WANTED_LANES_SET message is an acknowledged message used to set the Wanted Lanes state of a node (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")).

The response to a WANTED_LANES_SET message is a WANTED_LANES_STATUS message.

[Table 4.231](index-en.html#UUID-db41d16d-0b51-6fdf-2842-b94c16e65bc9_Table_4.231 "Table 4.231. WANTED_LANES_SET message structure") defines the structure of the WANTED_LANES_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Wanted_Lanes | 8 | New Wanted Lanes state | M |

Table 4.231. WANTED_LANES_SET message structure

The Opcode field shall contain the opcode value for the WANTED_LANES_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Wanted Lanes state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Wanted_Lanes field determines the new Wanted Lanes state for the node, as defined in [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes").

##### 4.3.5.26. WANTED_LANES_STATUS

A WANTED_LANES_STATUS message is an unacknowledged message used to report the current Wanted Lanes state of a node (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")).

[Table 4.232](index-en.html#UUID-e2b00656-ed04-0079-db66-45f0b3a7e19f_Table_4.232 "Table 4.232. WANTED_LANES_STATUS message structure") defines the structure of the WANTED_LANES_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Wanted_Lanes | 8 | Current Wanted Lanes state | M |

Table 4.232. WANTED_LANES_STATUS message structure

The Opcode field shall contain the opcode value for the WANTED_LANES_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Wanted Lanes state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Wanted Lanes state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Wanted_Lanes field indicates the current Wanted Lanes state for the node, as defined in [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes").

##### 4.3.5.27. TWO_WAY_PATH_GET

A TWO_WAY_PATH_GET message is an acknowledged message used to get the current Two Way Path state of a node (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")).

The response to a TWO_WAY_PATH_GET message is a TWO_WAY_PATH_STATUS message.

[Table 4.233](index-en.html#UUID-9b37e802-302d-c69f-03c0-ab67b2a4ad0a_Table_4.233 "Table 4.233. TWO_WAY_PATH_GET message structure") defines the structure of the TWO_WAY_PATH_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.233. TWO_WAY_PATH_GET message structure

The Opcode field shall contain the opcode value for the TWO_WAY_PATH_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Two Way Path state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.28. TWO_WAY_PATH_SET

A TWO_WAY_PATH_SET message is an acknowledged message used to set the Two Way Path state of a node (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")).

The response to a TWO_WAY_PATH_SET message is a TWO_WAY_PATH_STATUS message.

[Table 4.234](index-en.html#UUID-9fab0149-0d01-410d-ba7d-a46165654544_Table_4.234 "Table 4.234. TWO_WAY_PATH_SET message structure") defines the structure of the TWO_WAY_PATH_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Two_Way_Path | 1 | New Two Way Path state | M |
| Prohibited | 7 | Prohibited | M |

Table 4.234. TWO_WAY_PATH_SET message structure

The Opcode field shall contain the opcode value for the TWO_WAY_PATH_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Two Way Path state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Two_Way_Path field determines the new Two Way Path state for the node, as defined in [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path").

##### 4.3.5.29. TWO_WAY_PATH_STATUS

A TWO_WAY_PATH_STATUS message is an unacknowledged message used to report the current Two Way Path state of a node (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")).

[Table 4.235](index-en.html#UUID-d4dc801b-2950-303e-27fb-b82267fe9b75_Table_4.235 "Table 4.235. TWO_WAY_PATH_STATUS message structure") defines the structure of the TWO_WAY_PATH_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Two_Way_Path | 1 | Current Two Way Path state | M |
| Prohibited | 7 | Prohibited | M |

Table 4.235. TWO_WAY_PATH_STATUS message structure

The Opcode field shall contain the opcode value for the TWO_WAY_PATH_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Two Way Path state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Two Way Path state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Two_Way_Path field indicates the current Two Way Path state for the node, as defined in [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path").

##### 4.3.5.30. PATH_ECHO_INTERVAL_GET

A PATH_ECHO_INTERVAL_GET message is an acknowledged message used to get the current Path Echo Interval state of a node (see [Section 4.2.32](index-en.html#UUID-f4522b18-a1a0-f41c-96e7-9a56288eb5c0 "4.2.32. Path Echo Interval")).

The response to a PATH_ECHO_INTERVAL_GET message is a PATH_ECHO_INTERVAL_STATUS message.

[Table 4.236](index-en.html#UUID-3af87d8d-4149-377e-17a0-94602e279d9a_Table_4.236 "Table 4.236. PATH_ECHO_INTERVAL_GET message structure") defines the structure of the PATH_ECHO_INTERVAL_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |

Table 4.236. PATH_ECHO_INTERVAL_GET message structure

The Opcode field shall contain the opcode value for the PATH_ECHO_INTERVAL_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Echo Interval state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.5.31. PATH_ECHO_INTERVAL_SET

A PATH_ECHO_INTERVAL_SET message is an acknowledged message used to set the Path Echo Interval state of a node (see [Section 4.2.32](index-en.html#UUID-f4522b18-a1a0-f41c-96e7-9a56288eb5c0 "4.2.32. Path Echo Interval")).

The response to a PATH_ECHO_INTERVAL_SET message is a PATH_ECHO_INTERVAL_STATUS message.

[Table 4.237](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.237 "Table 4.237. PATH_ECHO_INTERVAL_SET message structure") defines the structure of the PATH_ECHO_INTERVAL_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Unicast_Echo_Interval | 8 | New Unicast Echo Interval state or indication of no state change defined in [Table 4.238](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.238 "Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values") | M |
| Multicast_Echo_Interval | 8 | New Multicast Echo Interval state or indication of no state change defined in [Table 4.238](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.238 "Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values") | M |

Table 4.237. PATH_ECHO_INTERVAL_SET message structure

The Opcode field shall contain the opcode value for the PATH_ECHO_INTERVAL_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Echo Interval state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Unicast_Echo_Interval field determines the new Unicast Echo Interval state for the node or indicates no change in the Unicast Echo Interval state, as defined in [Table 4.238](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.238 "Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values").

The Multicast_Echo_Interval field determines the new Multicast Echo Interval state for the node or indicates no change in the Multicast Echo Interval state, as defined in [Table 4.238](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.238 "Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values").

The Unicast_Echo_Interval field and the Multicast_Echo_Interval field values are defined in [Table 4.238](index-en.html#UUID-ab38c0dd-873e-7d06-df40-b9d0954481a3_Table_4.238 "Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values").

| Value | Description |
| --- | --- |
| 0x00 | The Directed Forwarding Echo procedure is not executed for this address type. |
| 0x01−0x63 | Interval expressed as percentage of the time corresponding to the Path Lifetime state (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")). |
| 0x64−0xFE | Prohibited |
| 0xFF | No change in the state |

Table 4.238. Unicast_Echo_Interval field and Multicast_Echo_Interval field values

The Unicast_Echo_Interval field and the Multicast_Echo_Interval field both shall not be 0xFF.

##### 4.3.5.32. PATH_ECHO_INTERVAL_STATUS

A PATH_ECHO_INTERVAL_STATUS message is an unacknowledged message used to report the current Path Echo Interval state of a node (see [Section 4.2.32](index-en.html#UUID-f4522b18-a1a0-f41c-96e7-9a56288eb5c0 "4.2.32. Path Echo Interval")).

[Table 4.239](index-en.html#UUID-f5ffb0ab-48e8-e51c-0336-080ea8f3a2f4_Table_4.239 "Table 4.239. PATH_ECHO_INTERVAL_STATUS message structure") defines the structure of the PATH_ECHO_INTERVAL_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| NetKeyIndex | 16 | NetKey Index of the NetKey used in the subnet | M |
| Unicast_Echo_Interval | 8 | Current Unicast Echo Interval state | M |
| Multicast_Echo_Interval | 8 | Current Multicast Echo Interval state | M |

Table 4.239. PATH_ECHO_INTERVAL_STATUS message structure

The Opcode field shall contain the opcode value for the PATH_ECHO_INTERVAL_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Path Echo Interval state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is the global NetKey Index of the NetKey of the subnet that is associated with the Path Echo Interval state and is encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Unicast_Echo_Interval field indicates the current Unicast Echo Interval state for the node, as defined in [Section 4.2.32.1](index-en.html#UUID-3e7efc9b-b39c-03a4-b396-10d29e418623 "4.2.32.1. Unicast Echo Interval"), or reports 0xFF.

The Multicast_Echo_Interval field indicates the current Multicast Echo Interval state for the node, as defined in [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval"), or reports 0xFF.

##### 4.3.5.33. DIRECTED_NETWORK_TRANSMIT_GET

A DIRECTED_NETWORK_TRANSMIT_GET message is an acknowledged message used to get the current Directed Network Transmit state of a node (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")).

The response to a DIRECTED_NETWORK_TRANSMIT_GET message is a DIRECTED_NETWORK_TRANSMIT_STATUS message.

The structure of the DIRECTED_NETWORK_TRANSMIT_GET message is defined in [Table 4.240](index-en.html#UUID-962818cc-f26b-bdfe-d26e-023bf31e4cd9_Table_4.240 "Table 4.240. DIRECTED_NETWORK_TRANSMIT_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.240. DIRECTED_NETWORK_TRANSMIT_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_NETWORK_TRANSMIT_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.34. DIRECTED_NETWORK_TRANSMIT_SET

A DIRECTED_NETWORK_TRANSMIT_SET message is an acknowledged message used to set the Directed Network Transmit state of a node (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")).

The response to a DIRECTED_NETWORK_TRANSMIT_SET message is a DIRECTED_NETWORK_TRANSMIT_STATUS message.

[Table 4.241](index-en.html#UUID-342ced2a-1190-c1e4-7e83-c10492260293_Table_4.241 "Table 4.241. DIRECTED_NETWORK_TRANSMIT_SET message structure") defines the structure of the DIRECTED_NETWORK_TRANSMIT_SET message.

| **Field** | **Size  (bits)** | **Description** | **Req.** |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Network_Transmit_Count | 3 | New Directed Network Transmit Count state | M |
| Directed_Network_Transmit_Interval_Steps | 5 | New Directed Network Transmit Interval Steps state | M |

Table 4.241. DIRECTED_NETWORK_TRANSMIT_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_NETWORK_TRANSMIT_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Network_Transmit_Count field determines the new Directed Network Transmit Count state for the node, as defined in [Section 4.2.33.1](index-en.html#UUID-156477a1-fee3-c009-ba33-6e0eb7b68be1 "4.2.33.1. Directed Network Transmit Count").

The Directed_Network_Transmit_Interval_Steps field determines the new Directed Network Transmit Interval Steps state for the node, as defined in [Section 4.2.33.2](index-en.html#UUID-80851bac-c2eb-58a9-bae3-2732e8859f95 "4.2.33.2. Directed Network Transmit Interval Steps").

##### 4.3.5.35. DIRECTED_NETWORK_TRANSMIT_STATUS

A DIRECTED_NETWORK_TRANSMIT_STATUS message is an unacknowledged message used to report the current Directed Network Transmit state of a node (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")).

[Table 4.242](index-en.html#UUID-04272639-bd3b-49a5-b86e-d752b94636ad_Table_4.242 "Table 4.242. DIRECTED_NETWORK_TRANSMIT_STATUS message structure") defines the structure of the DIRECTED_NETWORK_TRANSMIT_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Network_Transmit_Count | 3 | Current Directed Network Transmit Count state | M |
| Directed_Network_Transmit_Interval_Steps | 5 | Current Directed Network Transmit Interval Steps state | M |

Table 4.242. DIRECTED_NETWORK_TRANSMIT_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_NETWORK_TRANSMIT_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Network_Transmit_Count field indicates the current Directed Network Transmit Count state for the node, as defined in [Section 4.2.33.1](index-en.html#UUID-156477a1-fee3-c009-ba33-6e0eb7b68be1 "4.2.33.1. Directed Network Transmit Count").

The Directed_Network_Transmit_Interval_Steps field indicates the current Directed Network Transmit Interval Steps state for the node, as defined in [Section 4.2.33.2](index-en.html#UUID-80851bac-c2eb-58a9-bae3-2732e8859f95 "4.2.33.2. Directed Network Transmit Interval Steps").

##### 4.3.5.36. DIRECTED_RELAY_RETRANSMIT_GET

A DIRECTED_RELAY_RETRANSMIT_GET message is an acknowledged message used to get the current Directed Relay Retransmit state of a node (see [Section 4.2.34](index-en.html#UUID-41edd232-dff9-4fe3-1373-2f5a50aa874a "4.2.34. Directed Relay Retransmit")).

The response to a DIRECTED_RELAY_RETRANSMIT_GET message is a DIRECTED_RELAY_RETRANSMIT_STATUS message.

The structure of the DIRECTED_RELAY_RETRANSMIT_GET message is defined in [Table 4.243](index-en.html#UUID-fa8d5728-6e69-273d-3422-faf33d2d7c40_Table_4.243 "Table 4.243. DIRECTED_RELAY_RETRANSMIT_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.243. DIRECTED_RELAY_RETRANSMIT_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_RELAY_RETRANSMIT_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.37. DIRECTED_RELAY_RETRANSMIT_SET

A DIRECTED_RELAY_RETRANSMIT_SET message is an acknowledged message used to set the Directed Relay Retransmit state of a node (see [Section 4.2.34](index-en.html#UUID-41edd232-dff9-4fe3-1373-2f5a50aa874a "4.2.34. Directed Relay Retransmit")).

The response to a DIRECTED_RELAY_RETRANSMIT_SET message is a DIRECTED_RELAY_RETRANSMIT_STATUS message.

[Table 4.244](index-en.html#UUID-2aa11a97-b276-8c48-5637-fe98153d2381_Table_4.244 "Table 4.244. DIRECTED_RELAY_RETRANSMIT_SET message structure") defines the structure of the DIRECTED_RELAY_RETRANSMIT_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Relay_Retransmit_Count | 3 | New Directed Relay Retransmit Count state | M |
| Directed_Relay_Retransmit_Interval_Steps | 5 | New Directed Relay Retransmit Interval Steps state | M |

Table 4.244. DIRECTED_RELAY_RETRANSMIT_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_RELAY_RETRANSMIT_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Relay_Retransmit_Count field determines the new Directed Relay Retransmit Count state for the node, as defined in [Section 4.2.34.1](index-en.html#UUID-c2007925-882b-4a14-3e90-b6a1c4a71c9a "4.2.34.1. Directed Relay Retransmit Count").

The Directed_Relay_Retransmit_Interval_Steps field determines the new Directed Relay Retransmit Interval Steps state for the node, as defined in [Section 4.2.34.2](index-en.html#UUID-a175dda0-1ac3-18e3-0635-9804394db061 "4.2.34.2. Directed Relay Retransmit Interval Steps").

##### 4.3.5.38. DIRECTED_RELAY_RETRANSMIT_STATUS

A DIRECTED_RELAY_RETRANSMIT_STATUS message is an unacknowledged message used to report the current Directed Relay Retransmit state of a node (see [Section 4.2.34](index-en.html#UUID-41edd232-dff9-4fe3-1373-2f5a50aa874a "4.2.34. Directed Relay Retransmit")).

[Table 4.245](index-en.html#UUID-fc1f5b42-6b72-56b7-8ee4-f42bd3b3d0b6_Table_4.245 "Table 4.245. DIRECTED_RELAY_RETRANSMIT_STATUS message structure") defines the structure of the DIRECTED_RELAY_RETRANSMIT_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Relay_Retransmit_Count | 3 | Current Directed Relay Retransmit Count state | M |
| Directed_Relay_Retransmit_Interval_Steps | 5 | Current Directed Relay Retransmit Interval Steps state | M |

Table 4.245. DIRECTED_RELAY_RETRANSMIT_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_RELAY_RETRANSMIT_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Relay_Retransmit_Count field indicates the current Directed Relay Retransmit Count state for the node, as defined in [Section 4.2.34.1](index-en.html#UUID-c2007925-882b-4a14-3e90-b6a1c4a71c9a "4.2.34.1. Directed Relay Retransmit Count").

The Directed_Relay_Retransmit_Interval_Steps field indicates the current Directed Relay Retransmit Interval Steps state for the node, as defined in [Section 4.2.34.2](index-en.html#UUID-a175dda0-1ac3-18e3-0635-9804394db061 "4.2.34.2. Directed Relay Retransmit Interval Steps").

##### 4.3.5.39. RSSI_THRESHOLD_GET

A RSSI_THRESHOLD_GET message is an acknowledged message used to get the current RSSI Threshold state of a node (see [Section 4.2.35](index-en.html#UUID-f5f8e95b-b448-36cc-7818-a08a46e24834 "4.2.35. RSSI Threshold")).

The response to an RSSI_THRESHOLD_GET message is an RSSI_THRESHOLD_STATUS message.

The structure of the RSSI_THRESHOLD_GET message is defined in [Table 4.246](index-en.html#UUID-5449c201-6615-3658-7ed5-df67e37a2413_Table_4.246 "Table 4.246. RSSI_THRESHOLD_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.246. RSSI_THRESHOLD_GET message structure

The Opcode field shall contain the opcode value for the RSSI_THRESHOLD_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.40. RSSI_THRESHOLD_SET

A RSSI_THRESHOLD_SET message is an acknowledged message used to set the RSSI Margin state of a node (see [Section 4.2.35](index-en.html#UUID-f5f8e95b-b448-36cc-7818-a08a46e24834 "4.2.35. RSSI Threshold")).

The response to an RSSI_THRESHOLD_SET message is an RSSI_THRESHOLD_STATUS message.

[Table 4.247](index-en.html#UUID-a129582a-5bd0-8a96-637d-af06e7299ca6_Table_4.247 "Table 4.247. RSSI_THRESHOLD_SET message structure") defines the structure of the RSSI_THRESHOLD_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| RSSI_Margin | 8 | New RSSI Margin state | M |

Table 4.247. RSSI_THRESHOLD_SET message structure

The Opcode field shall contain the opcode value for the RSSI_THRESHOLD_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The RSSI_Margin field determines the new RSSI Margin state for the node, as defined in [Section 4.2.35.2](index-en.html#UUID-c30bb5db-a914-901c-6609-c60e528972bd "4.2.35.2. RSSI Margin").

##### 4.3.5.41. RSSI_THRESHOLD_STATUS

A RSSI_THRESHOLD_STATUS message is an unacknowledged message used to report the current RSSI Threshold state of a node (see [Section 4.2.35](index-en.html#UUID-f5f8e95b-b448-36cc-7818-a08a46e24834 "4.2.35. RSSI Threshold")).

[Table 4.248](index-en.html#UUID-2165bd22-d75a-0905-e5c1-e0da1186894f_Table_4.248 "Table 4.248. RSSI_THRESHOLD_STATUS message structure") defines the structure of the RSSI_THRESHOLD_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Default_RSSI_Threshold | 8 | Default RSSI Threshold state | M |
| RSSI_Margin | 8 | Current RSSI Margin state | M |

Table 4.248. RSSI_THRESHOLD_STATUS message structure

The Opcode field shall contain the opcode value for the RSSI_THRESHOLD_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Default_RSSI_Threshold field indicates the Default RSSI Threshold state for the node, as defined in [Section 4.2.35.1](index-en.html#UUID-d474c478-bc5e-bbe6-48f5-943397437f43 "4.2.35.1. Default RSSI Threshold").

The RSSI_Margin field indicates the current RSSI Margin state for the node, as defined in [Section 4.2.35.2](index-en.html#UUID-c30bb5db-a914-901c-6609-c60e528972bd "4.2.35.2. RSSI Margin").

##### 4.3.5.42. DIRECTED_PATHS_GET

A DIRECTED_PATHS_GET message is an acknowledged message used to get the Directed Paths state of a node (see [Section 4.2.36](index-en.html#UUID-f915c359-525a-2c8e-41db-7da6eab4482c "4.2.36. Directed Paths")).

The response to a DIRECTED_PATHS_GET message is a DIRECTED_PATHS_STATUS message.

The structure of the DIRECTED_PATHS_GET message is defined in [Table 4.249](index-en.html#UUID-886c12e7-5221-360c-714c-1283dad1e186_Table_4.249 "Table 4.249. DIRECTED_PATHS_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.249. DIRECTED_PATHS_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_PATHS_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.43. DIRECTED_PATHS_STATUS

A DIRECTED_PATHS_STATUS message is an unacknowledged message used to report the Directed Paths state of a node (see [Section 4.2.36](index-en.html#UUID-f915c359-525a-2c8e-41db-7da6eab4482c "4.2.36. Directed Paths")).

[Table 4.250](index-en.html#UUID-b7b7ba79-a32a-34f6-909d-9916a6f08704_Table_4.250 "Table 4.250. DIRECTED_PATHS_STATUS message structure") defines the structure of the DIRECTED_PATHS_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Node_Paths | 16 | Directed Node Paths state | M |
| Directed_Relay_Paths | 16 | Directed Relay Paths state | M |
| Directed_Proxy_Paths | 16 | Directed Proxy Paths state | M |
| Directed_Friend_Paths | 16 | Directed Friend Paths state | M |

Table 4.250. DIRECTED_PATHS_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_PATHS_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Node_Paths field indicates the Directed Node Paths state for the node, as defined in [Section 4.2.36.1](index-en.html#UUID-1dd98673-e5f9-a65d-bcd6-822880da0c63 "4.2.36.1. Directed Node Paths").

The Directed_Relay_Paths field indicates the Directed Relay Paths state for the node, as defined in [Section 4.2.36.2](index-en.html#UUID-1f8b8740-e3ca-08a0-930d-4a5ea4b02261 "4.2.36.2. Directed Relay Paths").

The Directed_Proxy_Paths field indicates the Directed Proxy Paths state for the node, as defined in [Section 4.2.36.3](index-en.html#UUID-ff81b630-84f4-f85f-8be1-399f08a6905c "4.2.36.3. Directed Proxy Paths").

The Directed_Friend_Paths field indicates the Directed Friend Paths state for the node, as defined in [Section 4.2.36.4](index-en.html#UUID-624bd74f-fbcc-44a7-a0c9-a12e6f451ba1 "4.2.36.4. Directed Friend Paths").

##### 4.3.5.44. DIRECTED_PUBLISH_POLICY_GET

A DIRECTED_PUBLISH_POLICY_GET message is an acknowledged message used to get the Directed Publish Policy state of a model of an element of a node (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")).

The response to a DIRECTED_PUBLISH_POLICY_GET message is a DIRECTED_PUBLISH_POLICY_STATUS message.

[Table 4.251](index-en.html#UUID-55bd4c29-4c57-e687-a6dc-b0a7762ec7d4_Table_4.251 "Table 4.251. DIRECTED_PUBLISH_POLICY_GET message structure") defines the structure of the DIRECTED_PUBLISH_POLICY_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Element_Addr | 16 | Address of the element | M |
| Model_ID | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.251. DIRECTED_PUBLISH_POLICY_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_PUBLISH_POLICY_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Element_Addr field reports the unicast address of the element that supports the publishing model. All other address types are Prohibited for this field.

The Model_ID field reports either a SIG Model ID or a Vendor Model ID that identifies the model within the element.

##### 4.3.5.45. DIRECTED_PUBLISH_POLICY_SET

A DIRECTED_PUBLISH_POLICY_SET message is an acknowledged message used to set the Directed Publish Policy state of a model of an element of a node (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")).

The response to a DIRECTED_PUBLISH_POLICY_SET message is a DIRECTED_PUBLISH_POLICY_STATUS message.

[Table 4.252](index-en.html#UUID-7aa68fac-f471-e39f-df75-9e36da7935bf_Table_4.252 "Table 4.252. DIRECTED_PUBLISH_POLICY_SET message structure") defines the structure of the DIRECTED_PUBLISH_POLICY_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Publish_Policy | 8 | New Directed Publish Policy state | M |
| Element_Addr | 16 | Address of the element | M |
| Model_ID | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.252. DIRECTED_PUBLISH_POLICY_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_PUBLISH_POLICY_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Publish_Policy field determines the new Directed Publish Policy state for the model as defined in [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy").

The Element_Addr field reports the unicast address of the element that supports the publishing model. All other address types are Prohibited for this field.

The Model_ID field reports either a SIG Model ID or a Vendor Model ID that identifies the model within the element.

##### 4.3.5.46. DIRECTED_PUBLISH_POLICY_STATUS

A DIRECTED_PUBLISH_POLICY_STATUS message is an unacknowledged message used to report the current Directed Publish Policy state of a model of an element of a node (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")).

[Table 4.253](index-en.html#UUID-008728fa-d2e1-00ad-b82f-36f01e00ca9c_Table_4.253 "Table 4.253. DIRECTED_PUBLISH_POLICY_STATUS message structure") defines the structure of the DIRECTED_PUBLISH_POLICY_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status code for the requesting message | M |
| Directed_Publish_Policy | 8 | Current Directed Publish Policy state | M |
| Element_Addr | 16 | Address of the element | M |
| Model_ID | 16 or 32 | SIG Model ID or Vendor Model ID | M |

Table 4.253. DIRECTED_PUBLISH_POLICY_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_PUBLISH_POLICY_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status code for the most recent operation on the Directed Publish Policy state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The Directed_Publish_Policy field indicates the current Directed Publish Policy state for the model as defined in [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy").

The Element_Addr field reports the unicast address of the element that supports the publishing model. All other address types are Prohibited for this field.

The Model_ID field reports either a SIG Model ID or a Vendor Model ID that identifies the model within the element.

##### 4.3.5.47. PATH_DISCOVERY_TIMING_CONTROL_GET

A PATH_DISCOVERY_TIMING_CONTROL_GET message is an acknowledged message used to get the Path Discovery Timing Control state of a node (see [Section 4.2.38](index-en.html#UUID-b2b1d81f-e9b3-2803-e46f-5271d0f079c6 "4.2.38. Path Discovery Timing Control")).

The response to a PATH_DISCOVERY_TIMING_CONTROL_GET message is a PATH_DISCOVERY_TIMING_CONTROL_STATUS message.

The structure of the PATH_DISCOVERY_TIMING_CONTROL_GET message is defined in [Table 4.254](index-en.html#UUID-87fa4376-0e5d-464e-9210-0f2c409a5d7f_Table_4.254 "Table 4.254. PATH_DISCOVERY_TIMING_CONTROL_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.254. PATH_DISCOVERY_TIMING_CONTROL_GET message structure

The Opcode field shall contain the opcode value for the PATH_DISCOVERY_TIMING_CONTROL_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.48. PATH_DISCOVERY_TIMING_CONTROL_SET

A PATH_DISCOVERY_TIMING_CONTROL_SET message is an acknowledged message used to set the Path Discovery Timing Control state of a node (see [Section 4.2.38](index-en.html#UUID-b2b1d81f-e9b3-2803-e46f-5271d0f079c6 "4.2.38. Path Discovery Timing Control")).

The response to a PATH_DISCOVERY_TIMING_CONTROL_SET message is a PATH_DISCOVERY_TIMING_CONTROL_STATUS message.

[Table 4.255](index-en.html#UUID-9bf1fa36-8014-91ea-9e50-c07e72c3fdb4_Table_4.255 "Table 4.255. PATH_DISCOVERY_TIMING_CONTROL_SET message structure") defines the structure of the PATH_DISCOVERY_TIMING_CONTROL_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Path_Monitoring_Interval | 16 | New Path Monitoring Interval state | M |
| Path_Discovery_Retry_Interval | 16 | New Path Discovery Retry Interval state | M |
| Path_Discovery_Interval | 1 | New Path Discovery Interval state | M |
| Lane_Discovery_Guard_Interval | 1 | New Lane Discovery Guard Interval state | M |
| Prohibited | 6 | Prohibited | M |

Table 4.255. PATH_DISCOVERY_TIMING_CONTROL_SET message structure

The Opcode field shall contain the opcode value for the PATH_DISCOVERY_TIMING_CONTROL_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Path_Monitoring_Interval field determines the new Path Monitoring Interval state for the node as defined in [Section 4.2.38.1](index-en.html#UUID-f207102b-3e10-0547-65c2-0cdc3afd2c3f "4.2.38.1. Path Monitoring Interval").

The Path_Discovery_Retry_Interval field determines the new Path Discovery Retry Interval state for the node as defined in [Section 4.2.38.2](index-en.html#UUID-00b281da-cf97-1f1b-e2cb-9b18ef10da6e "4.2.38.2. Path Discovery Retry Interval").

The Path_Discovery_Interval field determines the new Path Discovery Interval state for the node as defined in [Section 4.2.38.3](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf "4.2.38.3. Path Discovery Interval").

The Lane_Discovery_Guard_Interval field determines the new Lane Discovery Guard Interval state for the node as defined in [Section 4.2.38.4](index-en.html#UUID-11e4dd23-ac53-7cb3-8ee3-d8ae38fda848 "4.2.38.4. Lane Discovery Guard Interval").

##### 4.3.5.49. PATH_DISCOVERY_TIMING_CONTROL_STATUS

A PATH_DISCOVERY_TIMING_CONTROL_STATUS message is an unacknowledged message used to report the current Path Discovery Timing Control state of a node (see [Section 4.2.38](index-en.html#UUID-b2b1d81f-e9b3-2803-e46f-5271d0f079c6 "4.2.38. Path Discovery Timing Control")).

[Table 4.256](index-en.html#UUID-74568f1d-28a6-308f-55dc-e0c294c3034d_Table_4.256 "Table 4.256. PATH_DISCOVERY_TIMING_CONTROL_STATUS message structure") defines the structure of the PATH_DISCOVERY_TIMING_CONTROL_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Path_Monitoring_Interval | 16 | Current Path Monitoring Interval state | M |
| Path_Discovery_Retry_Interval | 16 | Current Path Discovery Retry Interval state | M |
| Path_Discovery_Interval | 1 | Current Path Discovery Interval state | M |
| Lane_Discovery_Guard_Interval | 1 | Current Lane Discovery Guard Interval state | M |
| Prohibited | 6 | Prohibited | M |

Table 4.256. PATH_DISCOVERY_TIMING_CONTROL_STATUS message structure

The Opcode field shall contain the opcode value for the PATH_DISCOVERY_TIMING_CONTROL_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Path_Monitoring_Interval field indicates the current Path Monitoring Interval state of the node as defined in [Section 4.2.38.1](index-en.html#UUID-f207102b-3e10-0547-65c2-0cdc3afd2c3f "4.2.38.1. Path Monitoring Interval").

The Path_Discovery_Retry_Interval field indicates the current Path Discovery Retry Interval state of the node as defined in [Section 4.2.38.2](index-en.html#UUID-00b281da-cf97-1f1b-e2cb-9b18ef10da6e "4.2.38.2. Path Discovery Retry Interval").

The Path_Discovery_Interval field determines the current Path Discovery Interval state of the node as defined in [Section 4.2.38.3](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf "4.2.38.3. Path Discovery Interval").

The Lane_Discovery_Guard_Interval field determines the current Lane Discovery Guard Interval state of the node as defined in [Section 4.2.38.4](index-en.html#UUID-11e4dd23-ac53-7cb3-8ee3-d8ae38fda848 "4.2.38.4. Lane Discovery Guard Interval").

##### 4.3.5.50. DIRECTED_CONTROL_NETWORK_TRANSMIT_GET

A DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message is an acknowledged message used to get the current Directed Control Network Transmit state of a node (see [Section 4.2.39](index-en.html#UUID-bda1ae5c-f4fc-6585-77ea-c54f24acbef8 "4.2.39. Directed Control Network Transmit")).

The response to a DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message is a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message.

The structure of the DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message is defined in [Table 4.257](index-en.html#UUID-dd2c3af1-4b75-58d2-7eac-d0c5d55dd799_Table_4.257 "Table 4.257. DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.257. DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.51. DIRECTED_CONTROL_NETWORK_TRANSMIT_SET

A DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message is an acknowledged message used to set the Directed Control Network Transmit state of a node (see [Section 4.2.39](index-en.html#UUID-bda1ae5c-f4fc-6585-77ea-c54f24acbef8 "4.2.39. Directed Control Network Transmit")).

The response to a DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message is a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message.

[Table 4.258](index-en.html#UUID-fff6b7b9-1aed-be68-b544-25d3b09b8bdc_Table_4.258 "Table 4.258. DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message structure") defines the structure of the DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Control_Network_Transmit_Count | 3 | New Directed Control Network Transmit Count state | M |
| Directed_Control_Network_Transmit_Interval_Steps | 5 | New Directed Control Network Transmit Interval Steps state | M |

Table 4.258. DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Control_Network_Transmit_Count field determines the new Directed Control Network Transmit Count state for the node, as defined in [Section 4.2.39.1](index-en.html#UUID-44d73067-2274-ad60-fc6f-7274eea08c63 "4.2.39.1. Directed Control Network Transmit Count").

The Directed_Control_Network_Transmit_Interval_Steps field determines the new Directed Control Network Transmit Interval Steps state for the node, as defined in [Section 4.2.39.2](index-en.html#UUID-aaef1564-b0da-1501-24af-257fa188d014 "4.2.39.2. Directed Control Network Transmit Interval Steps").

##### 4.3.5.52. DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS

A DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message is an unacknowledged message used to report the current Directed Control Network Transmit state of a node (see [Section 4.2.39](index-en.html#UUID-bda1ae5c-f4fc-6585-77ea-c54f24acbef8 "4.2.39. Directed Control Network Transmit")).

[Table 4.259](index-en.html#UUID-6c1ca410-a3cc-d55a-69e0-7be21801ccc5_Table_4.259 "Table 4.259. DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message structure") defines the structure of the DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Control_Network_Transmit_Count | 3 | Current Directed Control Network Transmit Count state | M |
| Directed_Control_Network_Transmit_Interval_Steps | 5 | Current Directed Control Network Transmit Interval Steps state | M |

Table 4.259. DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Control_Network_Transmit_Count field indicates the current Directed Control Network Transmit Count state for the node, as defined in [Section 4.2.39.1](index-en.html#UUID-44d73067-2274-ad60-fc6f-7274eea08c63 "4.2.39.1. Directed Control Network Transmit Count").

The Directed_Control_Network_Transmit_Interval_Steps field indicates the current Directed Control Network Transmit Interval Steps state for the node, as defined in [Section 4.2.39.2](index-en.html#UUID-aaef1564-b0da-1501-24af-257fa188d014 "4.2.39.2. Directed Control Network Transmit Interval Steps").

##### 4.3.5.53. DIRECTED_CONTROL_RELAY_RETRANSMIT_GET

A DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message is an acknowledged message used to get the current Directed Control Relay Retransmit state of a node (see [Section 4.2.40](index-en.html#UUID-efce1e35-df07-15c0-0784-95c584a64d65 "4.2.40. Directed Control Relay Retransmit")).

The response to a DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message is a DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message.

The structure of the DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message is defined in [Table 4.260](index-en.html#UUID-c6f9c0a6-5187-b6fa-e468-23e88da6accf_Table_4.260 "Table 4.260. DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.260. DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.5.54. DIRECTED_CONTROL_RELAY_RETRANSMIT_SET

A DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message is an acknowledged message used to set the Directed Control Relay Retransmit state of a node (see [Section 4.2.40](index-en.html#UUID-efce1e35-df07-15c0-0784-95c584a64d65 "4.2.40. Directed Control Relay Retransmit")).

The response to a DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message is a DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message.

[Table 4.261](index-en.html#UUID-21037c97-4199-c34f-4592-b4f5bab7e2cf_Table_4.261 "Table 4.261. DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message structure") defines the structure of the DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Control_Relay_Retransmit_Count | 3 | New Directed Control Relay Retransmit Count state | M |
| Directed_Control_Relay_Retransmit_Interval_Steps | 5 | New Directed Control Relay Retransmit Interval Steps state | M |

Table 4.261. DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Control_Relay_Retransmit_Count field determines the new Directed Control Relay Retransmit Count state for the node, as defined in [Section 4.2.40.1](index-en.html#UUID-43b4d545-19dd-ad94-5ce4-f2b105f4162f "4.2.40.1. Directed Control Relay Retransmit Count").

The Directed_Control_Relay_Retransmit_Interval_Steps field determines the new Directed Control Relay Retransmit Interval Steps state for the node, as defined in [Section 4.2.40.2](index-en.html#UUID-df3188af-6ad4-491d-7c9d-7dc7f322c242 "4.2.40.2. Directed Control Relay Retransmit Interval Steps").

##### 4.3.5.55. DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS

A DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message is an unacknowledged message used to report the current Directed Control Relay Retransmit state of a node (see [Section 4.2.40](index-en.html#UUID-efce1e35-df07-15c0-0784-95c584a64d65 "4.2.40. Directed Control Relay Retransmit")).

[Table 4.262](index-en.html#UUID-46c5d7e9-366f-8a54-8ae0-a90237295ccb_Table_4.262 "Table 4.262. DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message structure") defines the structure of the DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directed_Control_Relay_Retransmit_Count | 3 | Current Directed Control Relay Retransmit Count state | M |
| Directed_Control_Relay_Retransmit_Interval_Steps | 5 | Current Directed Control Relay Retransmit Interval Steps state | M |

Table 4.262. DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message structure

The Opcode field shall contain the opcode value for the DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directed_Control_Relay_Retransmit_Count field indicates the current Directed Control Relay Retransmit Count state for the node, as defined in [Section 4.2.40.1](index-en.html#UUID-43b4d545-19dd-ad94-5ce4-f2b105f4162f "4.2.40.1. Directed Control Relay Retransmit Count").

The Directed_Control_Relay_Retransmit_Interval_Steps field indicates the current Directed Control Relay Retransmit Interval Steps state for the node, as defined in [Section 4.2.40.2](index-en.html#UUID-df3188af-6ad4-491d-7c9d-7dc7f322c242 "4.2.40.2. Directed Control Relay Retransmit Interval Steps").

#### 4.3.6. On-Demand Private GATT Proxy messages

On-Demand Private GATT Proxy messages are used to control the On-Demand GATT Proxy state (see [Section 4.2.47](index-en.html#UUID-b688770d-69cc-ff39-feb3-8b82ebe09fb5 "4.2.47. On-Demand Private GATT Proxy")).

##### 4.3.6.1. ON_DEMAND_PRIVATE_PROXY_GET

An ON_DEMAND_PRIVATE_PROXY_GET message is an acknowledged message used to get the current On-Demand Private GATT Proxy state of a node.

The response to an ON_DEMAND_PRIVATE_PROXY_GET message is an ON_DEMAND_PRIVATE_PROXY_GET_STATUS message.

The structure of the ON_DEMAND_PRIVATE_PROXY_GET message is defined in [Table 4.263](index-en.html#UUID-d44e6bf8-e917-2728-d1a1-e6d8b395a543_Table_4.263 "Table 4.263. ON_DEMAND_PRIVATE_PROXY_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.263. ON_DEMAND_PRIVATE_PROXY_GET message structure

The Opcode field shall contain the opcode value for the ON_DEMAND_PRIVATE_PROXY_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.6.2. ON_DEMAND_PRIVATE_PROXY_SET

An ON_DEMAND_PRIVATE_PROXY_SET message is an acknowledged message used to set the On-Demand Private GATT Proxy state of a node.

The response to an ON_DEMAND_PRIVATE_PROXY_SET message is an ON_DEMAND_PRIVATE_PROXY_STATUS message.

The parameters of this message are defined in [Table 4.264](index-en.html#UUID-3114aa4d-b36d-ab71-ba2d-763a4fe67e23_Table_4.264 "Table 4.264. ON_DEMAND_PRIVATE_PROXY_SET message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| On-Demand_Private_GATT_Proxy | 1 | New On-Demand Private GATT Proxy state | M |

Table 4.264. ON_DEMAND_PRIVATE_PROXY_SET message structure

The Opcode field shall contain the opcode value for the ON_DEMAND_PRIVATE_PROXY_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The On-Demand_Private_GATT_Proxy field contains the new On-Demand Private GATT Proxy state of the node.

##### 4.3.6.3. ON_DEMAND_PRIVATE_PROXY_STATUS

An ON_DEMAND_PRIVATE_PROXY_STATUS message is an unacknowledged message used to report the current On-Demand Private GATT Proxy state of a node.

The parameters of this message are defined in [Table 4.265](index-en.html#UUID-2415d9fc-614f-d0ad-bbdb-6052b243637e_Table_4.265 "Table 4.265. ON_DEMAND_PRIVATE_PROXY_STATUS message structure").

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| On-Demand_Private_GATT_Proxy | 1 | GATT Proxy state | M |

Table 4.265. ON_DEMAND_PRIVATE_PROXY_STATUS message structure

The Opcode field shall contain the opcode value for the ON_DEMAND_PRIVATE_PROXY_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The On-Demand_Private_GATT_Proxy field indicates the current On-Demand Private GATT Proxy state of the node.

#### 4.3.7. Solicitation PDU RPL Configuration messages

Solicitation PDU RPL Configuration messages are used to control the solicitation replay protection list of a node (see [Section 6.9.2.1](index-en.html#UUID-4f699c10-9c25-e312-207d-d5ec847045dc "6.9.2.1. Solicitation replay protection list")).

##### 4.3.7.1. SOLICITATION_PDU_RPL_ITEMS_CLEAR

A SOLICITATION_PDU_RPL_ITEMS_CLEAR message is an acknowledged message used to remove one or more items from the solicitation replay protection list of a node.

The response to a SOLICITATION_PDU_RPL_ITEMS_CLEAR message is a SOLICITATION_PDU_RPL_ITEMS_CLEAR_STATUS message.

[Table 4.266](index-en.html#UUID-98b87649-03e3-fb3a-e0c6-0be821e18f1e_Table_4.266 "Table 4.266. SOLICITATION_PDU_RPL_ITEMS_CLEAR message structure") defines the structure of the SOLICITATION_PDU_RPL_ITEMS_CLEAR message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Address_Range | 2 or 3 | Unicast address range | M |

Table 4.266. SOLICITATION_PDU_RPL_ITEMS_CLEAR message structure

The Opcode field shall contain the opcode value for the SOLICITATION_PDU_RPL_ITEMS_CLEAR message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Address_Range field indicates the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the solicitation PDU sequences to be removed from the solicitation replay
protection list of a node.

##### 4.3.7.2. SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED

A SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED message is an unacknowledged message used to remove one or more items from the solicitation replay protection list of a node.

[Table 4.267](index-en.html#UUID-7f546dd4-ce9e-e92c-f24d-67633cde8d7c_Table_4.267 "Table 4.267. SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED message structure") defines the structure of the SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Address_Range | 2 or 3 | Unicast address range | M |

Table 4.267. SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED message structure

The Opcode field shall contain the opcode value for the SOLICITATION_PDU_RPL_ITEMS_CLEAR_UNACKNOWLEDGED message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Address_Range field indicates the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the solicitation PDU sequences to be removed from the solicitation replay
protection list of a node.

##### 4.3.7.3. SOLICITATION_PDU_RPL_ITEMS_STATUS

A SOLICITATION_PDU_RPL_ITEMS_STATUS message is an unacknowledged message used to confirm the removal of one or more items from the solicitation replay protection list of a node.

[Table 4.268](index-en.html#UUID-1f959e73-0bbf-6e66-08d1-c237f0945fd9_Table_4.268 "Table 4.268. SOLICITATION_PDU_RPL_ITEMS_STATUS message structure") defines the structure of the SOLICITATION_PDU_RPL_ITEMS_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Address_Range | 2 or 3 | Unicast address range | M |

Table 4.268. SOLICITATION_PDU_RPL_ITEMS_STATUS message structure

The Opcode field shall contain the opcode value for the SOLICITATION_PDU_RPL_ITEMS_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Address_Range field indicates the unicast address range (see [Section 3.4.2.2.1](index-en.html#UUID-af80374f-9849-5a8e-b508-1ce34a0bec84 "3.4.2.2.1. Unicast address range format")) of the solicitation PDU sequences removed from the solicitation replay protection
list of a node.

#### 4.3.8. SAR Configuration messages

##### 4.3.8.1. SAR_TRANSMITTER_GET

A SAR_TRANSMITTER_GET message is an acknowledged message used to get the current SAR Transmitter state of a node.

The response to a SAR_TRANSMITTER_GET message is a SAR_TRANSMITTER_STATUS message.

The structure of the SAR_TRANSMITTER_GET message is defined in [Table 4.269](index-en.html#UUID-40757b39-cff2-c865-543a-cc2f546993cd_Table_4.269 "Table 4.269. SAR_TRANSMITTER_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.269. SAR_TRANSMITTER_GET message structure

The Opcode field shall contain the opcode value for the SAR_TRANSMITTER_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.8.2. SAR_TRANSMITTER_SET

A SAR_TRANSMITTER_SET message is an acknowledged message used to set the SAR Transmitter state of a node.

The response to a SAR_TRANSMITTER_SET message is a SAR_TRANSMITTER_STATUS message.

[Table 4.270](index-en.html#UUID-64dd5c4e-7d1d-8eb1-806b-66bc233a95a1_Table_4.270 "Table 4.270. SAR_TRANSMITTER_SET message structure") defines the structure of the SAR_TRANSMITTER_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| SAR_Segment_Interval_Step | 4 | New SAR Segment Interval Step state | M |
| SAR_Unicast_Retransmissions_Count | 4 | New SAR Unicast Retransmissions Count state | M |
| SAR_Unicast_Retransmissions_Without_Progress_Count | 4 | New SAR Unicast Retransmissions Without Progress Count state | M |
| SAR_Unicast_Retransmissions_Interval_Step | 4 | New SAR Unicast Retransmissions Interval Step state | M |
| SAR_Unicast_Retransmissions_Interval_Increment | 4 | New SAR Unicast Retransmissions Interval Increment state | M |
| SAR_Multicast_Retransmissions_Count | 4 | New SAR Multicast Retransmissions Count state | M |
| SAR_Multicast_Retransmissions_Interval_Step | 4 | New SAR Multicast Retransmissions Interval Step state | M |
| RFU | 4 | Reserved for Future Use | M |

Table 4.270. SAR_TRANSMITTER_SET message structure

The Opcode field shall contain the opcode value for the SAR_TRANSMITTER_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The SAR_Segment_Interval_Step field determines the new SAR Segment Interval Step state for the node, as defined in [Section 4.2.48.1](index-en.html#UUID-8e9f8c8e-5f5b-cfc3-c6c5-8104d04ea236 "4.2.48.1. SAR Segment Interval Step").

The SAR_Unicast_Retransmissions_Count field determines the new SAR Unicast Retransmissions Count state for the node, as defined in [Section 4.2.48.2](index-en.html#UUID-2dd0fc6f-d7a1-15d5-b9a7-1d63c5752ce4 "4.2.48.2. SAR Unicast Retransmissions Count").

The SAR_Unicast_Retransmissions_Without_Progress_Count field determines the new SAR Unicast Retransmissions Without Progress Count state for the node, as defined in [Section 4.2.48.3](index-en.html#UUID-eff91da3-c5c0-f4c0-6037-c9e713dc7d9a "4.2.48.3. SAR Unicast Retransmissions Without Progress Count").

The SAR_Unicast_Retransmissions_Interval_Step field determines the new SAR Unicast Retransmissions Interval Step state for the node, as defined in [Section 4.2.48.4](index-en.html#UUID-26e4432b-aeba-a9ff-71b1-7880bcad6605 "4.2.48.4. SAR Unicast Retransmissions Interval Step").

The SAR_Unicast_Retransmissions_Interval_Increment field determines the new SAR Unicast Retransmissions Interval Increment state for the node, as defined in [Section 4.2.48.5](index-en.html#UUID-fd2d1be5-ca83-2c6e-724f-99e63a6824a7 "4.2.48.5. SAR Unicast Retransmissions Interval Increment").

The SAR_Multicast_Retransmissions_Count field determines the new SAR Multicast Retransmissions Count state for the node, as defined in [Section 4.2.48.6](index-en.html#UUID-5f949ca2-e0af-4e91-83b4-fa41f68fd284 "4.2.48.6. SAR Multicast Retransmissions Count").

The SAR_Multicast_Retransmissions_Interval_Step field determines the new SAR Multicast Retransmissions Interval Step state for the node, as defined in [Section 4.2.48.7](index-en.html#UUID-2dd60df5-b721-e70e-e473-b8c4ad9faec0 "4.2.48.7. SAR Multicast Retransmissions Interval Step").

##### 4.3.8.3. SAR_TRANSMITTER_STATUS

A SAR_TRANSMITTER_STATUS message is an unacknowledged message used to report the current SAR Transmitter state of a node.

[Table 4.271](index-en.html#UUID-15154eba-8f81-a4d2-a8dd-a16c4b4ca21a_Table_4.271 "Table 4.271. SAR_TRANSMITTER_STATUS message structure") defines the structure of the SAR_TRANSMITTER_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| SAR_Segment_Interval_Step | 4 | Current SAR Segment Interval Step state | M |
| SAR_Unicast_Retransmissions_Count | 4 | Current SAR Unicast Retransmissions Count state | M |
| SAR_Unicast_Retransmissions_Without_Progress_Count | 4 | Current SAR Unicast Retransmissions Without Progress Count state | M |
| SAR_Unicast_Retransmissions_Interval_Step | 4 | Current SAR Unicast Retransmissions Interval Step state | M |
| SAR_Unicast_Retransmissions_Interval_Increment | 4 | Current SAR Unicast Retransmissions Interval Increment state | M |
| SAR_Multicast_Retransmissions_Count | 4 | Current SAR Multicast Retransmissions Count state | M |
| SAR_Multicast_Retransmissions_Interval_Step | 4 | Current SAR Multicast Retransmissions Interval Step state | M |
| RFU | 4 | Reserved for Future Use | M |

Table 4.271. SAR_TRANSMITTER_STATUS message structure

The Opcode field shall contain the opcode value for the SAR_TRANSMITTER_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The SAR_Segment_Interval_Step field indicates the current SAR Segment Interval Step state for the node, as defined in [Section 4.2.48.1](index-en.html#UUID-8e9f8c8e-5f5b-cfc3-c6c5-8104d04ea236 "4.2.48.1. SAR Segment Interval Step").

The SAR_Unicast_Retransmissions_Count field indicates the current SAR Unicast Retransmissions Count state for the node, as defined in [Section 4.2.48.2](index-en.html#UUID-2dd0fc6f-d7a1-15d5-b9a7-1d63c5752ce4 "4.2.48.2. SAR Unicast Retransmissions Count").

The SAR_Unicast_Retransmissions_Without_Progress_Count field indicates the current SAR Unicast Retransmissions Without Progress Count state for the node, as defined in [Section 4.2.48.3](index-en.html#UUID-eff91da3-c5c0-f4c0-6037-c9e713dc7d9a "4.2.48.3. SAR Unicast Retransmissions Without Progress Count").

The SAR_Unicast_Retransmissions_Interval_Step field indicates the current SAR Unicast Retransmissions Interval Step state for the node, as defined in [Section 4.2.48.4](index-en.html#UUID-26e4432b-aeba-a9ff-71b1-7880bcad6605 "4.2.48.4. SAR Unicast Retransmissions Interval Step").

The SAR_Unicast_Retransmissions_Interval_Increment field indicates the current SAR Unicast Retransmissions Interval Increment state for the node, as defined in [Section 4.2.48.5](index-en.html#UUID-fd2d1be5-ca83-2c6e-724f-99e63a6824a7 "4.2.48.5. SAR Unicast Retransmissions Interval Increment").

The SAR_Multicast_Retransmissions_Count field indicates the current SAR Multicast Retransmissions Count state for the node, as defined in [Section 4.2.48.6](index-en.html#UUID-5f949ca2-e0af-4e91-83b4-fa41f68fd284 "4.2.48.6. SAR Multicast Retransmissions Count").

The SAR_Multicast_Retransmissions_Interval_Step field indicates the current SAR Multicast Retransmissions Interval Step state for the node, as defined in [Section 4.2.48.7](index-en.html#UUID-2dd60df5-b721-e70e-e473-b8c4ad9faec0 "4.2.48.7. SAR Multicast Retransmissions Interval Step").

##### 4.3.8.4. SAR_RECEIVER_GET

A SAR_RECEIVER_GET message is an acknowledged message used to get the current SAR Receiver state of a node.

The response to a SAR_RECEIVER_GET message is a SAR_RECEIVER_STATUS message.

The structure of the SAR_RECEIVER_GET message is defined in [Table 4.272](index-en.html#UUID-ddbe39ca-c775-5a8f-f36c-95216a239f1b_Table_4.272 "Table 4.272. SAR_RECEIVER_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.272. SAR_RECEIVER_GET message structure

The Opcode field shall contain the opcode value for the SAR_RECEIVER_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.8.5. SAR_RECEIVER_SET

A SAR_RECEIVER_SET message is an acknowledged message used to set the SAR Receiver state of a node.

The response to a SAR_RECEIVER_SET message is a SAR_RECEIVER_STATUS message.

[Table 4.273](index-en.html#UUID-a35fc8b6-0441-eedc-d08f-04acd95456c0_Table_4.273 "Table 4.273. SAR_RECEIVER_SET message structure") defines the structure of the SAR_RECEIVER_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| SAR_Segments_Threshold | 5 | New SAR Segments Threshold state | M |
| SAR_Acknowledgment_Delay_Increment | 3 | New SAR Acknowledgment Delay Increment state | M |
| SAR_Discard_Timeout | 4 | New SAR Discard Timeout state | M |
| SAR_Receiver_Segment_Interval_Step | 4 | New SAR Receiver Segment Interval Step state | M |
| SAR_Acknowledgment_Retransmissions_Count | 2 | New SAR Acknowledgment Retransmissions Count state | M |
| RFU | 6 | Reserved for Future Use | M |

Table 4.273. SAR_RECEIVER_SET message structure

The Opcode field shall contain the opcode value for the SAR_RECEIVER_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The SAR_Segments_Threshold field determines the new SAR Segments Threshold state for the node, as defined in [Section 4.2.49.1](index-en.html#UUID-1485ed5f-fe9d-3af8-923b-e4a1464adee6 "4.2.49.1. SAR Segments Threshold").

The SAR_Acknowledgment_Delay_Increment field determines the new SAR Acknowledgment Delay Increment state for the node, as defined in [Section 4.2.49.2](index-en.html#UUID-41e1a57f-f1ae-d323-67e4-54a8b8aeb70f "4.2.49.2. SAR Acknowledgment Delay Increment").

The SAR_Discard_Timeout field determines the new SAR Discard Timeout state for the node, as defined in [Section 4.2.49.4](index-en.html#UUID-b566885f-47f4-a84d-9ca9-fbabaf87406a "4.2.49.4. SAR Discard Timeout").

The SAR_Receiver_Segment_Interval_Step field determines the new SAR Receiver Segment Interval Step state for the node, as defined in [Section 4.2.49.5](index-en.html#UUID-cb59ec2b-0564-e693-a2b2-498e11382769 "4.2.49.5. SAR Receiver Segment Interval Step").

The SAR_Acknowledgment_Retransmissions_Count field determines the new SAR Acknowledgment Retransmissions Count state for the node, as defined in [Section 4.2.49.3](index-en.html#UUID-604f7ad9-8618-da8f-cf30-edd183f08c66 "4.2.49.3. SAR Acknowledgment Retransmissions Count").

##### 4.3.8.6. SAR_RECEIVER_STATUS

A SAR_RECEIVER_STATUS message is an unacknowledged message used to report the current SAR Receiver state of a node.

[Table 4.274](index-en.html#UUID-e6ae2fcb-df03-1cce-c0a6-c5ba638890ee_Table_4.274 "Table 4.274. SAR_RECEIVER_STATUS message structure") defines the structure of the SAR_RECEIVER_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| SAR_Segments_Threshold | 5 | Current SAR Segments Threshold state | M |
| SAR_Acknowledgment_Delay_Increment | 3 | Current SAR Acknowledgment Delay Increment state | M |
| SAR_Discard_Timeout | 4 | Current SAR Discard Timeout state | M |
| SAR_Receiver_Segment_Interval_Step | 4 | New SAR Receiver Segment Interval Step state | M |
| SAR_Acknowledgment_Retransmissions_Count | 2 | Current SAR Acknowledgment Retransmissions Count state | M |
| RFU | 6 | Reserved for Future Use | M |

Table 4.274. SAR_RECEIVER_STATUS message structure

The Opcode field shall contain the opcode value for the SAR_RECEIVER_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The SAR_Segments_Threshold field indicates the current SAR Segments Threshold state for the node, as defined in [Section 4.2.49.1](index-en.html#UUID-1485ed5f-fe9d-3af8-923b-e4a1464adee6 "4.2.49.1. SAR Segments Threshold").

The SAR_Acknowledgment_Delay_Increment field indicates the current SAR Acknowledgment Delay Increment state for the node, as defined in [Section 4.2.49.2](index-en.html#UUID-41e1a57f-f1ae-d323-67e4-54a8b8aeb70f "4.2.49.2. SAR Acknowledgment Delay Increment").

The SAR_Discard_Timeout field indicates the current SAR Discard Timeout state for the node, as defined in [Section 4.2.49.4](index-en.html#UUID-b566885f-47f4-a84d-9ca9-fbabaf87406a "4.2.49.4. SAR Discard Timeout").

The SAR_Receiver_Segment_Interval_Step field determines the new SAR Receiver Segment Interval Step state for the node, as defined in [Section 4.2.49.5](index-en.html#UUID-cb59ec2b-0564-e693-a2b2-498e11382769 "4.2.49.5. SAR Receiver Segment Interval Step").

The SAR_Acknowledgment_Retransmissions_Count field indicates the current SAR Acknowledgment Retransmissions Count state for the node, as defined in [Section 4.2.49.3](index-en.html#UUID-604f7ad9-8618-da8f-cf30-edd183f08c66 "4.2.49.3. SAR Acknowledgment Retransmissions Count").

#### 4.3.9. Opcodes Aggregator messages

##### 4.3.9.1. Aggregator Item format

An Aggregator Item encapsulates an Access message for a given model. Multiple Aggregator Items can be concatenated in an OPCODES_AGGREGATOR_SEQUENCE message (see [Section 4.3.9.2](index-en.html#UUID-06e68ef8-773f-d4c4-4120-89130be6736b "4.3.9.2. OPCODES_AGGREGATOR_SEQUENCE")) or an OPCODES_AGGREGATOR_STATUS message (see [Section 4.3.9.3](index-en.html#UUID-d2fc676d-d3de-804c-321b-c4bb5cc6bee0 "4.3.9.3. OPCODES_AGGREGATOR_STATUS")).

The structure of an Aggregator Item field is defined in [Table 4.275](index-en.html#UUID-bc7c73b5-0f92-6198-b0da-5f50e4edcea4_Table_4.275 "Table 4.275. Format of the Aggregator Item").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Length_Format | 1 | 0: Length_Short field is present  1: Length_Long field is present | M |
| Length_Short | 7 | Size of Opcode_And_Parameters field | C.1 |
| Length_Long | 15 | Size of Opcode_And_Parameters field | C.2 |
| Opcode_And_Parameters | variable | Opcode and parameters | M |

Table 4.275. Format of the Aggregator Item

C.1:
:   Included if Length_Format is 0, otherwise excluded.

C.2:
:   Included if Length_Format is 1, otherwise excluded.

The Length_Format field indicates whether either the Length_Short field or Length_Long field is present in the message. The values of the Length_Format field are defined in [Table 4.276](index-en.html#UUID-bc7c73b5-0f92-6198-b0da-5f50e4edcea4_Table_4.276 "Table 4.276. Values of the Length_Format field").

| Value | Description |
| --- | --- |
| 0 | The Length_Short field is present in the message |
| 1 | The Length_Long field is present in the message |

Table 4.276. Values of the Length_Format field

If present, the Length_Short field shall indicate the length of the Opcode_And_Parameters field.

If present, the Length_Long field shall indicate the length of the Opcode_And_Parameters field.

An empty item shall be represented by setting the value of the Length_Format field to 0 and the value of the Length_Short field to 0.

The Opcode_And_Parameters field shall contain a valid opcode and parameters (contained in an unencrypted access layer message) for the given model.

##### 4.3.9.2. OPCODES_AGGREGATOR_SEQUENCE

An OPCODES_AGGREGATOR_SEQUENCE message is an acknowledged message that the Opcodes Aggregator Client uses to encapsulate a sequence of Access messages to be processed by the Opcodes Aggregator Server.

The response to an OPCODES_AGGREGATOR_SEQUENCE message is an OPCODES_AGGREGATOR_STATUS message.

[Table 4.277](index-en.html#UUID-06e68ef8-773f-d4c4-4120-89130be6736b_Table_4.277 "Table 4.277. OPCODES_AGGREGATOR_SEQUENCE message structure") defines the structure of the OPCODES_AGGREGATOR_SEQUENCE message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Element_Address | 2 | The element address | M |
| Items | variable | List of items with each item represented as an Aggregator Item | M |

Table 4.277. OPCODES_AGGREGATOR_SEQUENCE message structure

The Opcode field shall contain the opcode value for the OPCODES_AGGREGATOR_SEQUENCE message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Element_Address field is the unicast address of the element that will process the opcodes. All other address types are prohibited.

The minimum number of Items field entries included in the message is 2. Each entry in the Items field contains an Aggregator Item encapsulating an Access message for a model located in the element identified by the Element_Address field. The format of each entry of the Items field is defined in [Section 4.3.9.1](index-en.html#UUID-bc7c73b5-0f92-6198-b0da-5f50e4edcea4 "4.3.9.1. Aggregator Item format").

##### 4.3.9.3. OPCODES_AGGREGATOR_STATUS

An OPCODES_AGGREGATOR_STATUS message is an unacknowledged message used to report status for the most recent operation and response messages as a result of processing the Items field in an OPCODES_AGGREGATOR_SEQUENCE message.

[Table 4.278](index-en.html#UUID-d2fc676d-d3de-804c-321b-c4bb5cc6bee0_Table_4.278 "Table 4.278. OPCODES_AGGREGATOR_STATUS message structure") defines the structure of the OPCODES_AGGREGATOR_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | – | M |
| Element_Address | 2 | Element Address | M |
| Status_Items | variable | List of status items with each status item containing an unacknowledged access layer message or empty item | O |

Table 4.278. OPCODES_AGGREGATOR_STATUS message structure

The Opcode field shall contain the opcode value for the OPCODES_AGGREGATOR_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field indicates the status of the most recent operation.

The Element_Address field is the unicast address of the element that processed the opcodes. All other address types are Prohibited.

If present, the Status_Items field contains a list of unacknowledged response messages corresponding to the acknowledged messages in the Items field of the OPCODES_AGGREGATOR_SEQUENCE message, or an empty message when the corresponding Item field contained an unacknowledged message. The format of a Status_Items field entry is
the same as the format of the Items field defined in [Section 4.3.9.1](index-en.html#UUID-bc7c73b5-0f92-6198-b0da-5f50e4edcea4 "4.3.9.1. Aggregator Item format").

#### 4.3.10. Large Composition Data messages

##### 4.3.10.1. LARGE_COMPOSITION_DATA_GET

A LARGE_COMPOSITION_DATA_GET message is an acknowledged message used to read a portion of a page of the Composition Data (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

The response to a LARGE_COMPOSITION_DATA_GET message is a LARGE_COMPOSITION_DATA_STATUS message.

[Table 4.279](index-en.html#UUID-31938f56-0917-6b65-757e-e84c4aaad229_Table_4.279 "Table 4.279. LARGE_COMPOSITION_DATA_GET message structure") defines the structure of the LARGE_COMPOSITION_DATA_GET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Page | 1 | Page number of the Composition Data | M |
| Offset | 2 | Offset within the page | M |

Table 4.279. LARGE_COMPOSITION_DATA_GET message structure

The Opcode field shall contain the opcode value for the LARGE_COMPOSITION_DATA_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Page field shall identify the Composition Data Page number that is being read.

The Offset field shall identify the offset within the Composition Data Page in octets.

##### 4.3.10.2. LARGE_COMPOSITION_DATA_STATUS

A LARGE_COMPOSITION_DATA_STATUS message is an unacknowledged message used to report a portion of a page of the Composition Data (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

[Table 4.280](index-en.html#UUID-52b3ec3e-bbe5-c503-bd27-b22c3d1ec910_Table_4.280 "Table 4.280. LARGE_COMPOSITION_DATA_STATUS message structure") defines the structure of the LARGE_COMPOSITION_DATA_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Page | 1 | Page number of the Composition Data | M |
| Offset | 2 | Offset within the page | M |
| Total_Size | 2 | Total size of the page | M |
| Data | variable | Composition Data for the identified portion of the page | M |

Table 4.280. LARGE_COMPOSITION_DATA_STATUS message structure

The Opcode field shall contain the opcode value for the LARGE_COMPOSITION_DATA_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Page field shall identify the Composition Data Page number.

The Offset field shall identify the offset within the Composition Data Page in octets.

The Total_Size field shall identify the total size of the Composition Data Page in octets.

The Data field shall contain the identified portion of page of the Composition Data.

##### 4.3.10.3. MODELS_METADATA_GET

A MODELS_METADATA_GET message is an acknowledged message used to read a portion of a page of the Models Metadata state (see [Section 4.2.50](index-en.html#UUID-b97e5bcb-e7f2-fa87-24bf-4d017cdde2d9 "4.2.50. Models Metadata")).

The response to a MODELS_METADATA_GET message is a MODELS_METADATA_STATUS message.

[Table 4.281](index-en.html#UUID-539daca9-ae8d-e7fa-79c4-179b09bc902d_Table_4.281 "Table 4.281. MODELS_METADATA_GET message structure") defines the structure of the MODELS_METADATA_GET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Metadata_Page | 1 | Page number of the Models Metadata | M |
| Offset | 2 | Offset within the page | M |

Table 4.281. MODELS_METADATA_GET message structure

The Opcode field shall contain the opcode value for the MODELS_METADATA_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Metadata_Page field identifies the Models Metadata Page number.

The Offset field identifies the offset within the Models Metadata Page in octets.

##### 4.3.10.4. MODELS_METADATA_STATUS

A MODELS_METADATA_STATUS message is an unacknowledged message used to report a portion of a page of the Models Metadata state (see [Section 4.2.50](index-en.html#UUID-b97e5bcb-e7f2-fa87-24bf-4d017cdde2d9 "4.2.50. Models Metadata")).

[Table 4.282](index-en.html#UUID-56f48dd4-4b56-02ea-245b-20ded5aa8396_Table_4.282 "Table 4.282. MODELS_METADATA_STATUS message structure") defines the structure of the MODELS_METADATA_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Metadata_Page | 1 | Page number of the Models Metadata Page | M |
| Offset | 2 | Offset within the page | M |
| Total_Size | 2 | Total size of the page | M |
| Data | variable | Models Metadata for the identified portion of the page | M |

Table 4.282. MODELS_METADATA_STATUS message structure

The Opcode field shall contain the opcode value for the MODELS_METADATA_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Metadata_Page field identifies the Models Metadata Page number.

The Offset field identifies the offset within the Models Metadata Page in octets.

The Total_Size field identifies the total size of the Models Metadata Page in octets.

The Data field contains the identified portion of the Models Metadata Page.

#### 4.3.11. Bridge messages

The Bridge messages are used to configure the behavior of a Subnet Bridge node.

The Bridge messages shall be encrypted and authenticated using the DevKey of the Subnet Bridge node.

##### 4.3.11.1. SUBNET_BRIDGE_GET

A SUBNET_BRIDGE_GET message is an acknowledged message used to get the current Subnet Bridge state of a node (see [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge")).

The response to a SUBNET_BRIDGE_GET message is a SUBNET_BRIDGE_STATUS message.

The structure of the SUBNET_BRIDGE_GET message is defined in [Table 4.283](index-en.html#UUID-5b5343e9-d7ec-394f-077b-de9f7e22eb1c_Table_4.283 "Table 4.283. SUBNET_BRIDGE_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.283. SUBNET_BRIDGE_GET message structure

The Opcode field shall contain the opcode value for the SUBNET_BRIDGE_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.11.2. SUBNET_BRIDGE_SET

A SUBNET_BRIDGE_SET message is an acknowledged message used to set the Subnet Bridge state of a node (see [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge")).

The response to a SUBNET_BRIDGE_SET message is a SUBNET_BRIDGE_STATUS message.

[Table 4.284](index-en.html#UUID-d3b8d5fa-aa7f-b002-ba02-13bd5edd21e9_Table_4.284 "Table 4.284. SUBNET_BRIDGE_SET message structure") defines the structure of the SUBNET_BRIDGE_SET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Subnet_Bridge | 8 | New Subnet Bridge state | M |

Table 4.284. SUBNET_BRIDGE_SET message structure

The Opcode field shall contain the opcode value for the SUBNET_BRIDGE_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Subnet_Bridge field determines the new Subnet Bridge state for the node as defined in [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge").

##### 4.3.11.3. SUBNET_BRIDGE_STATUS

A SUBNET_BRIDGE_STATUS message is an unacknowledged message used to report the current Subnet Bridge state of a node (see [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge")).

[Table 4.285](index-en.html#UUID-7444da24-33a0-c052-7aa1-52bf7b10a6ef_Table_4.285 "Table 4.285. SUBNET_BRIDGE_STATUS message structure") defines the structure of the SUBNET_BRIDGE_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Subnet_Bridge | 8 | Current Subnet Bridge state | M |

Table 4.285. SUBNET_BRIDGE_STATUS message structure

The Opcode field shall contain the opcode value for the SUBNET_BRIDGE_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Subnet_Bridge field indicates the current Subnet Bridge state of the node as defined in [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge").

##### 4.3.11.4. BRIDGING_TABLE_ADD

A BRIDGING_TABLE_ADD message is an acknowledged message used to add entries to the Bridging Table state (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) of a Subnet Bridge node.

The response to a BRIDGING_TABLE_ADD message is a BRIDGING_TABLE_STATUS message.

[Table 4.286](index-en.html#UUID-cc95fff6-a91e-1b79-abd1-2c0debf5feea_Table_4.286 "Table 4.286. BRIDGING_TABLE_ADD message structure") defines the structure of the BRIDGING_TABLE_ADD message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Directions | 8 | Allowed directions for the bridged traffic | M |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |
| Address1 | 16 | Address of the node in the first subnet | M |
| Address2 | 16 | Address of the node in the second subnet | M |

Table 4.286. BRIDGING_TABLE_ADD message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_ADD message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Directions field indicates the allowed directions for the bridged traffic. The values for this field are defined in [Table 4.71](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.71 "Table 4.71. Directions field values").

Each of the NetKeyIndex1 and NetKeyIndex2 fields is the global NetKey Index of the NetKey associated with the first subnet and the second subnet, respectively. The NetKeyIndex1 and NetKeyIndex2 fields shall have different values.

The Address1 and Address2 fields identify the addresses of the nodes in the first subnet and in the second subnet, respectively. The Address1 and Address2 fields shall have different values.

The Address1 field value shall be a unicast address.

If the Directions field value is 0x01 (see [Table 4.71](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.71 "Table 4.71. Directions field values")), the unassigned address and the all-nodes fixed group address are prohibited values for the Address2
field.

If the Directions field value is 0x02 (see [Table 4.71](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.71 "Table 4.71. Directions field values")), then the Address2 field value shall be a unicast address.

##### 4.3.11.5. BRIDGING_TABLE_REMOVE

A BRIDGING_TABLE_REMOVE message is an acknowledged message used to remove entries from the Bridging Table state (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) of a Subnet Bridge node.

The response to a BRIDGING_TABLE_REMOVE message is a BRIDGING_TABLE_STATUS message.

[Table 4.287](index-en.html#UUID-e423d1ae-47f6-ec68-83e3-986dc5f20da8_Table_4.287 "Table 4.287. BRIDGING_TABLE_REMOVE message structure") defines the structure of the BRIDGING_TABLE_REMOVE message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |
| Address1 | 16 | Address of the node in the first subnet | M |
| Address2 | 16 | Address of the node in the second subnet | M |

Table 4.287. BRIDGING_TABLE_REMOVE message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_REMOVE message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

Each of the NetKeyIndex1 and NetKeyIndex2 fields is the global NetKey Index of the NetKey associated with the first subnet and the second subnet, respectively.

The Address1 and Address2 fields identify the addresses of the nodes in the first subnet and in the second subnet, respectively.

The Address1 field value shall be the unassigned address or a unicast address.

The Address2 field value shall not be the all-nodes fixed group address.

##### 4.3.11.6. BRIDGING_TABLE_STATUS

A BRIDGING_TABLE_STATUS message is an unacknowledged message used to report the status of the most recent operation on the Bridging Table state (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) of a Subnet Bridge
node.

[Table 4.288](index-en.html#UUID-fab530f3-84a3-1c86-14af-c4e8723e1100_Table_4.288 "Table 4.288. BRIDGING_TABLE_STATUS message structure") defines the structure of the BRIDGING_TABLE_STATUS message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status Code for the requesting message | M |
| Current_Directions | 8 | Allowed directions for bridged traffic or bridged traffic not allowed | M |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |
| Address1 | 16 | Address of the node in the first subnet | M |
| Address2 | 16 | Address of the node in the second subnet | M |

Table 4.288. BRIDGING_TABLE_STATUS message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status Code for the most recent operation on the Bridging Table state. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The Current_Directions field indicates whether the bridged traffic is allowed and, if so, the allowed directions for the bridged traffic. The values for this field are defined in [Table 4.289](index-en.html#UUID-fab530f3-84a3-1c86-14af-c4e8723e1100_Table_4.289 "Table 4.289. Current_Directions values").

| Value | Description |
| --- | --- |
| 0x00 | Bridging is not allowed for messages between Address1 and Address2. |
| 0x01 | Bridging is allowed only for messages with Address1 as the source address and Address2 as the destination address. |
| 0x02 | Bridging is allowed for messages with Address1 as the source address and Address2 as the destination address, and for messages with Address2 as the source address and Address1 as the destination address. |
| 0x03–0xFF | Prohibited |

Table 4.289. Current_Directions values

Each of the NetKeyIndex1 and NetKeyIndex2 fields is the global NetKey Index of the NetKey associated with the first subnet and the second subnet, respectively.

The Address1 and Address2 fields identify the addresses of the nodes in the first subnet and in the second subnet, respectively.

The Address1 field value shall be the unassigned address or a unicast address.

The Address2 field value shall not be the all-nodes fixed group address.

##### 4.3.11.7. BRIDGED_SUBNETS_GET

A BRIDGED_SUBNETS_GET message is an acknowledged message used to get a filtered set of pairs of NetKey Indexes (see [Table 4.293](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.293 "Table 4.293. Bridged_Subnets_List entry format")) extracted from
the Bridging Table state entries of a Subnet Bridge node.

The response to a BRIDGED_SUBNETS_GET message is a BRIDGED_SUBNETS_LIST message.

[Table 4.290](index-en.html#UUID-898d24ab-99b1-ce66-728f-68f15dde8472_Table_4.290 "Table 4.290. BRIDGED_SUBNETS_GET message structure") defines the structure of the BRIDGED_SUBNETS_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Filter | 2 | Filter to be applied when reporting the set of pairs of NetKey Indexes | M |
| Prohibited | 2 | Prohibited | M |
| NetKeyIndex | 12 | NetKey Index of any of the subnets | M |
| Start_Index | 8 | Start offset in units of pairs of NetKey Indexes to read | M |

Table 4.290. BRIDGED_SUBNETS_GET message structure

The Opcode field shall contain the opcode value for the BRIDGED_SUBNETS_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Filter field determines the filtering to be applied when reporting the set of pairs of NetKey Indexes extracted from the Bridging Table state entries in the response message.

[Table 4.291](index-en.html#UUID-898d24ab-99b1-ce66-728f-68f15dde8472_Table_4.291 "Table 4.291. Filter field values") defines the Filter field values.

| Value | Description |
| --- | --- |
| 0b00 | Report all pairs of NetKey Indexes extracted from the Bridging Table state entries. |
| 0b01 | Report pairs of NetKey Indexes extracted from the Bridging Table state entries in which the NetKey Index of the first subnet (NetKeyIndex1) matches the NetKeyIndex field value. |
| 0b10 | Report pairs of NetKey Indexes extracted from the Bridging Table state entries in which the NetKey Index of the second subnet (NetKeyIndex2) matches the NetKeyIndex field value. |
| 0b11 | Report pairs of NetKey Indexes extracted from the Bridging Table state entries in which one of the NetKey Indexes (NetKeyIndex1 or NetKeyIndex2) matches the NetKeyIndex field. |

Table 4.291. Filter field values

The NetKeyIndex field is the global NetKey Index of the NetKey to be used for filtering if the Filter field value is different from 0b00.

The Start_Index field determines the offset in units of pairs of NetKey Indexes (see [Table 4.293](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.293 "Table 4.293. Bridged_Subnets_List entry format")) to start from when reporting the filtered set
of pairs of NetKey Indexes extracted from the Bridging Table state entries of a Subnet Bridge.

##### 4.3.11.8. BRIDGED_SUBNETS_LIST

A BRIDGED_SUBNETS_LIST message is an unacknowledged message used to report a filtered set of pairs of NetKey Indexes extracted from the Bridging Table state entries of a Subnet Bridge node.

This message is a response to the BRIDGED_SUBNETS_GET message.

[Table 4.292](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.292 "Table 4.292. BRIDGED_SUBNETS_LIST message structure") defines the structure of the BRIDGED_SUBNETS_LIST message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Filter | 2 | Filter applied to the set of pairs of NetKey Indexes | M |
| Prohibited | 2 | Prohibited | M |
| NetKeyIndex | 12 | NetKey Index used for filtering or ignored | M |
| Start_Index | 8 | Start offset in units of bridges | M |
| Bridged_Subnets_List | variable (24 * N) | Filtered set of N pairs of NetKey Indexes | O |

Table 4.292. BRIDGED_SUBNETS_LIST message structure

The Opcode field shall contain the opcode value for the BRIDGED_SUBNETS_LIST message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Filter field indicates the filtering applied when reporting the set of pairs of NetKey Indexes extracted from the Bridging Table state entries of the Subnet Bridge. [Table 4.291](index-en.html#UUID-898d24ab-99b1-ce66-728f-68f15dde8472_Table_4.291 "Table 4.291. Filter field values") defines the Filter field values.

If used for filtering, the NetKeyIndex field is the global NetKey Index of the NetKey associated with one of the subnets.

The Start_Index field indicates the offset in units of pairs of NetKey Indexes (see [Table 4.293](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.293 "Table 4.293. Bridged_Subnets_List entry format")) to start from when reporting the filtered set
of pairs of NetKey Indexes extracted from the Bridging Table state entries of the Subnet Bridge.

If present, the Bridged_Subnets_List field contains the filtered set of pairs of NetKey Indexes extracted from the Bridging Table state entries of the Subnet Bridge. Each Bridged_Subnets_List field entry shall be formatted as defined in [Table 4.293](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.293 "Table 4.293. Bridged_Subnets_List entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |

Table 4.293. Bridged_Subnets_List entry format

##### 4.3.11.9. BRIDGING_TABLE_GET

A BRIDGING_TABLE_GET message is an acknowledged message used to get the list of addresses and allowed traffic directions of the Bridging Table state entries (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) of a
Subnet Bridge node.

The response to a BRIDGING_TABLE_GET message is a BRIDGING_TABLE_LIST message.

[Table 4.294](index-en.html#UUID-90c0b066-0a8e-c6cb-2e97-280461179578_Table_4.294 "Table 4.294. BRIDGING_TABLE_GET message structure") defines the structure of the BRIDGING_TABLE_GET message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| NetKeyIndex1 | 12 | NetKey Index of first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of second subnet | M |
| Start_Index | 16 | Start offset to read in units of Bridging Table state entries | M |

Table 4.294. BRIDGING_TABLE_GET message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex1 field is the global NetKey Index of the NetKey associated with the first subnet (NetKeyIndex1) in the Bridging Table state.

The NetKeyIndex2 field is the global NetKey Index of the NetKey associated with the second subnet (NetKeyIndex2) in the Bridging Table state.

The Start_Index field determines the offset in units of Bridging Table state entries (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) to start from when reporting the list of addresses and allowed traffic
directions of the Bridging Table state.

##### 4.3.11.10. BRIDGING_TABLE_LIST

A BRIDGING_TABLE_LIST message is an unacknowledged message used to report the list of addresses and allowed traffic directions of the Bridging Table state entries (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table"))
of a Subnet Bridge node.

[Table 4.295](index-en.html#UUID-fecb508a-86df-1ea4-6cb1-a6ac09e1e444_Table_4.295 "Table 4.295. BRIDGING_TABLE_LIST message structure") defines the structure of the BRIDGING_TABLE_LIST message.

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 16 | The message opcode | M |
| Status | 8 | Status Code for the requesting message | M |
| NetKeyIndex1 | 12 | NetKey Index of the first subnet | M |
| NetKeyIndex2 | 12 | NetKey Index of the second subnet | M |
| Start_Index | 16 | Start offset in units of Bridging Table state entries | M |
| Bridged_Addresses_List | variable | List of bridged addresses and allowed traffic directions | C.1 |

Table 4.295. BRIDGING_TABLE_LIST message structure

C.1:
:   If the value of the Status field is Success, the Bridged_Addresses_List field shall be optional; otherwise, the Bridged_Addresses_List field shall not be present.

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_LIST message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field reports the Status Code for the most recent BRIDGING_TABLE_GET message. The Status codes are defined in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

Each of the NetKeyIndex1 and NetKeyIndex2 fields is the global NetKey Index of the NetKey associated with the first subnet and the second subnet, respectively.

The Start_Index field indicates the offset in units of Bridging Table state entries (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) used when reporting the list of addresses and allowed traffic directions of the
Bridging Table state.

If present, the Bridged_Addresses_List field contains a portion of the addresses and allowed traffic directions of the Bridging Table state entries. The format of the Bridged_Addresses_List entry is defined in [Table 4.296](index-en.html#UUID-fecb508a-86df-1ea4-6cb1-a6ac09e1e444_Table_4.296 "Table 4.296. Bridged_Addresses_List entry format").

| Field | Size  (bits) | Description | Req. |
| --- | --- | --- | --- |
| Address1 | 16 | Address of the node in the first subnet | M |
| Address2 | 16 | Address of the node in the second subnet | M |
| Directions | 8 | Allowed directions for bridged traffic | M |

Table 4.296. Bridged_Addresses_List entry format

The Directions field values are defined in [Table 4.71](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2_Table_4.71 "Table 4.71. Directions field values").

##### 4.3.11.11. BRIDGING_TABLE_SIZE_GET

A BRIDGING_TABLE_SIZE_GET message is an acknowledged message used to get the Bridging Table Size state (see [Section 4.2.43](index-en.html#UUID-40ebf047-039b-ff9d-e508-290dfe8681ca "4.2.43. Bridging Table Size")) of a Subnet Bridge node.

The response to a BRIDGING_TABLE_SIZE_GET message is a BRIDGING_TABLE_SIZE_STATUS message.

The structure of the BRIDGING_TABLE_SIZE_GET message is defined in [Table 4.297](index-en.html#UUID-96291620-da4f-c1bb-b06d-24ad51980988_Table_4.297 "Table 4.297. BRIDGING_TABLE_SIZE_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.297. BRIDGING_TABLE_SIZE_GET message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_SIZE_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.11.12. BRIDGING_TABLE_SIZE_STATUS

A BRIDGING_TABLE_SIZE_STATUS message is an unacknowledged message used to report the Bridging Table Size state (see [Section 4.2.43](index-en.html#UUID-40ebf047-039b-ff9d-e508-290dfe8681ca "4.2.43. Bridging Table Size")) of a Subnet Bridge node.

[Table 4.298](index-en.html#UUID-73ec6a2e-5a6b-4a4f-d0f0-2e00f04ab168_Table_4.298 "Table 4.298. BRIDGING_TABLE_SIZE_STATUS message structure") defines the structure of the BRIDGING_TABLE_SIZE_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Bridging_Table_Size | 2 | Bridging Table Size state | M |

Table 4.298. BRIDGING_TABLE_SIZE_STATUS message structure

The Opcode field shall contain the opcode value for the BRIDGING_TABLE_SIZE_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Bridging_Table_Size field indicates the Bridging Table Size state of the node, as defined in [Section 4.2.43](index-en.html#UUID-40ebf047-039b-ff9d-e508-290dfe8681ca "4.2.43. Bridging Table Size").

#### 4.3.12. Mesh Private Beacon messages

Mesh Private Beacon messages are used to control the transmission of Mesh Private beacons.

Mesh Private Beacon messages shall be encrypted and authenticated using the DevKey.

##### 4.3.12.1. PRIVATE_BEACON_GET

A PRIVATE_BEACON_GET message is an acknowledged message used to get the current Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) and Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of a node.

The response to a PRIVATE_BEACON_GET message is a PRIVATE_BEACON_STATUS message.

The structure of the PRIVATE_BEACON_GET message is defined in [Table 4.299](index-en.html#UUID-a7bf6c14-22d3-f879-f204-4b35e00ee9b4_Table_4.299 "Table 4.299. PRIVATE_BEACON_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.299. PRIVATE_BEACON_GET message structure

The Opcode field shall contain the opcode value for the PRIVATE_BEACON_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.12.2. PRIVATE_BEACON_SET

A PRIVATE_BEACON_SET message is an acknowledged message used to set the Private Beacon state and the Random Update Interval Steps state of a node.

The response to a PRIVATE_BEACON_SET message is a PRIVATE_BEACON_STATUS message.

[Table 4.300](index-en.html#UUID-12408cf3-da06-4112-efc3-ebd7549c4b78_Table_4.300 "Table 4.300. PRIVATE_BEACON_SET message structure") defines the structure of the PRIVATE_BEACON_SET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Private_Beacon | 1 | New Private Beacon state | M |
| Random_Update_Interval_Steps | 1 | New Random Update Interval Steps state | O |

Table 4.300. PRIVATE_BEACON_SET message structure

The Opcode field shall contain the opcode value for the PRIVATE_BEACON_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Private_Beacon field shall identify the value of the new Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) of a node.

If present, the Random_Update_Interval_Steps field shall identify the value of the new Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of a node.

##### 4.3.12.3. PRIVATE_BEACON_STATUS

A PRIVATE_BEACON_STATUS message is an unacknowledged message used to report the current Private Beacon state and Random Update Interval Steps state of a node.

This message is a response to PRIVATE_BEACON_GET message or a PRIVATE_BEACON_SET message.

[Table 4.301](index-en.html#UUID-ea833dc0-93e1-8241-9f71-135325219534_Table_4.301 "Table 4.301. PRIVATE_BEACON_STATUS message structure") defines the structure of the PRIVATE_BEACON_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Private_Beacon | 1 | Current value of the Private Beacon state | M |
| Random_Update_Interval_Steps | 1 | Current value of the Random Update Interval Steps state | M |

Table 4.301. PRIVATE_BEACON_STATUS message structure

The Opcode field shall contain the opcode value for the PRIVATE_BEACON_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Private_Beacon field shall identify the value of the current Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) of a node.

The Random_Update_Interval_Steps field shall identify the value of the current Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of a node.

##### 4.3.12.4. PRIVATE_GATT_PROXY_GET

A PRIVATE_GATT_PROXY_GET message is an acknowledged message used to get the current Private GATT Proxy state of a node (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

The response to a PRIVATE_GATT_PROXY_GET message is a PRIVATE_GATT_PROXY_STATUS message.

The structure of the PRIVATE_GATT_PROXY_GET message is defined in [Table 4.302](index-en.html#UUID-75ce45b0-9ed6-946d-dffe-f45884fd42ba_Table_4.302 "Table 4.302. PRIVATE_GATT_PROXY_GET message structure").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |

Table 4.302. PRIVATE_GATT_PROXY_GET message structure

The Opcode field shall contain the opcode value for the PRIVATE_GATT_PROXY_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

##### 4.3.12.5. PRIVATE_GATT_PROXY_SET

A PRIVATE_GATT_PROXY_SET message is an acknowledged message used to set the Private GATT Proxy state of a node (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

The response to a PRIVATE_GATT_PROXY_SET message is a PRIVATE_GATT_PROXY_STATUS message.

[Table 4.303](index-en.html#UUID-ef567def-d9c8-3f92-8e1a-7c942801c59b_Table_4.303 "Table 4.303. PRIVATE_GATT_PROXY_SET message structure") defines the structure of the PRIVATE_GATT_PROXY_SET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Private_GATT_Proxy | 1 | New Private GATT Proxy state | M |

Table 4.303. PRIVATE_GATT_PROXY_SET message structure

The Opcode field shall contain the opcode value for the PRIVATE_GATT_PROXY_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Private_GATT_Proxy field shall provide the new Private GATT Proxy state of the node (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")). The value of the Private_GATT_Proxy field shall be either Disabled or
Enabled, and all other values are Prohibited.

##### 4.3.12.6. PRIVATE_GATT_PROXY_STATUS

A PRIVATE_GATT_PROXY_STATUS message is an unacknowledged message used to report the current Private GATT Proxy state of a node (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

[Table 4.304](index-en.html#UUID-32f017e9-1dfa-994e-3480-6f06e712bfc9_Table_4.304 "Table 4.304. PRIVATE_GATT_PROXY_STATUS message structure") defines the structure of the PRIVATE_GATT_PROXY STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Private_GATT_Proxy | 1 | Private GATT Proxy state | M |

Table 4.304. PRIVATE_GATT_PROXY_STATUS message structure

The Opcode field shall contain the opcode value for the PRIVATE_GATT_PROXY_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Private_GATT_Proxy field shall provide the current Private GATT Proxy state of the node (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

##### 4.3.12.7. PRIVATE_NODE_IDENTITY_GET

A PRIVATE_NODE_IDENTITY_GET message is an acknowledged message used to get the current Private Node Identity state for a subnet (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")).

The response to a PRIVATE_NODE_IDENTITY_GET message is a PRIVATE_NODE_IDENTITY_STATUS message.

[Table 4.305](index-en.html#UUID-ff681346-0e3e-ce9d-532c-6b0bfd64a7f3_Table_4.305 "Table 4.305. PRIVATE_NODE_IDENTITY_GET message structure") defines the structure of the PRIVATE_NODE_IDENTITY_GET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |

Table 4.305. PRIVATE_NODE_IDENTITY_GET message structure

The Opcode field shall contain the opcode value for the PRIVATE_NODE_IDENTITY_GET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

##### 4.3.12.8. PRIVATE_NODE_IDENTITY_SET

A PRIVATE_NODE_IDENTITY_SET message is an acknowledged message used to set the current Private Node Identity state for a subnet (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")).

The response to a PRIVATE_NODE_IDENTITY_SET message is a PRIVATE_NODE_IDENTITY_STATUS message.

[Table 4.306](index-en.html#UUID-5fe6e2f7-2a87-cd5d-ef56-7153fdb8cf31_Table_4.306 "Table 4.306. PRIVATE_NODE_IDENTITY_SET message structure") defines the structure of the PRIVATE_NODE_IDENTITY_SET message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| NetKeyIndex | 2 | Index of the NetKey | M |
| Private_Identity | 1 | New Private Node Identity state | M |

Table 4.306. PRIVATE_NODE_IDENTITY_SET message structure

The Opcode field shall contain the opcode value for the PRIVATE_NODE_IDENTITY_SET message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey of the Node Identity state. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Private_Identity field shall provide the new Private Node Identity state of the NetKey (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")). The value of the Private_Identity field shall be either Disabled
or Enabled, and all other values are Prohibited.

##### 4.3.12.9. PRIVATE_NODE_IDENTITY_STATUS

A PRIVATE_NODE_IDENTITY_STATUS message is an unacknowledged message used to report the current Private Node Identity state for a subnet (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")).

[Table 4.307](index-en.html#UUID-ee8767aa-6309-3567-6c7d-1226f110dfba_Table_4.307 "Table 4.307. PRIVATE_NODE_IDENTITY_STATUS message structure") defines the structure of the PRIVATE_NODE_IDENTITY_STATUS message.

| Field | Size  (octets) | Description | Req. |
| --- | --- | --- | --- |
| Opcode | 2 | The message opcode | M |
| Status | 1 | Status Code for the requesting message | M |
| NetKeyIndex | 2 | Index of the NetKey | M |
| Private_Identity | 1 | Private Node Identity state | M |

Table 4.307. PRIVATE_NODE_IDENTITY_STATUS message structure

The Opcode field shall contain the opcode value for the PRIVATE_NODE_IDENTITY_STATUS message defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

The Status field shall identify the Status Code for the requesting message. The allowed values for Status codes and their meanings are documented in [Section 4.3.14](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6 "4.3.14. Summary of status codes").

The NetKeyIndex field is an index that shall identify the global NetKey Index of the NetKey of the Node Identity state. The NetKeyIndex field shall be encoded as defined in [Section 4.3.1.1](index-en.html#UUID-f7bdbeee-b1e1-dfba-6023-9976d51b312d "4.3.1.1. Key indexes").

The Private_Identity field shall provide the current Private Node Identity state for a subnet (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")).

#### 4.3.13. Messages summary

The list of messages, and their opcodes, that are available for each of the mesh models is defined in the Assigned Numbers document [[4](index-en.html#idp254746)].

#### 4.3.14. Summary of status codes

[Table 4.308](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.308 "Table 4.308. Summary of configuration and health messages status codes ") defines status codes for configuration messages (see [Section 4.3.2](index-en.html#UUID-e202c58e-be9b-d732-ae6b-ebd7fab382cc "4.3.2. Configuration messages")) and health messages (see [Section 4.3.3](index-en.html#UUID-5ba6a0bf-8408-2b80-be9c-2d101338131a "4.3.3. Health messages")) that contain a Status
parameter. Status messages are sent only in response to properly formatted messages (see [Section 3.7.3.4](index-en.html#UUID-3fad2ba1-effb-ca5c-3d33-e342dbb8da6d "3.7.3.4. Message error procedure")).

| Status Code | Status Code Name |
| --- | --- |
| 0x00 | Success |
| 0x01 | Invalid Address |
| 0x02 | Invalid Model |
| 0x03 | Invalid AppKey Index |
| 0x04 | Invalid NetKey Index |
| 0x05 | Insufficient Resources |
| 0x06 | Key Index Already Stored |
| 0x07 | Invalid Publish Parameters |
| 0x08 | Not a Subscribe Model |
| 0x09 | Storage Failure |
| 0x0A | Feature Not Supported |
| 0x0B | Cannot Update |
| 0x0C | Cannot Remove |
| 0x0D | Cannot Bind |
| 0x0E | Temporarily Unable to Change State |
| 0x0F | Cannot Set |
| 0x10 | Unspecified Error |
| 0x11 | Invalid Binding |
| 0x12 | Invalid Path Entry |
| 0x13 | Cannot Get |
| 0x14 | Obsolete Information |
| 0x15 | Invalid Bearer |
| 0x16–0xFF | RFU |

Table 4.308. Summary of configuration and health messages status codes

[Table 4.309](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.309 "Table 4.309. Summary of status codes for Opcodes Aggregator messages ") defines the status codes for Opcodes Aggregator messages.

| Status Code | Status Code Name |
| --- | --- |
| 0x00 | Success |
| 0x01 | Invalid Address |
| 0x02 | WrongAccessKey |
| 0x03 | WrongOpCode |
| 0x04 | MessageNotUnderstood |
| 0x05 | ResponseOverflow |
| 0x06–0xFF | Reserved for Future Use |

Table 4.309. Summary of status codes for Opcodes Aggregator messages

[Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes") defines status codes for Remote Provisioning Server messages that contain a status code.

| Status Code | Status Code Name |
| --- | --- |
| 0x00 | Success |
| 0x01 | Scanning Cannot Start |
| 0x02 | Invalid State |
| 0x03 | Limited Resources |
| 0x04 | Link Cannot Open |
| 0x05 | Link Open Failed |
| 0x06 | Link Closed by Device |
| 0x07 | Link Closed by Server |
| 0x08 | Link Closed by Client |
| 0x09 | Link Closed as Cannot Receive PDU |
| 0x0A | Link Closed as Cannot Send PDU |
| 0x0B | Link Closed as Cannot Deliver PDU Report |
| 0x0C–0xFF | Reserved for Future Use |

Table 4.310. Summary of Remote Provisioning Server model status codes

### 4.4. Model definitions

This section defines the foundation models used throughout this specification.

Model definitions that are not required as part of this specification are defined in the Mesh Model specification [[9](index-en.html#idp254760)] and follow the same format and architecture as mesh model definitions.

#### 4.4.1. Configuration Server model

##### 4.4.1.1. Description

The Configuration Server model is used to support the mesh configuration functionality of a node.

The Configuration Server model is a root model and a main model that does not extend any other models.

The Configuration Server model defines the state instances listed in [Table 4.311](index-en.html#UUID-73d8eb7c-f37a-9767-cd63-4999d115906a_Table_4.311 "Table 4.311. Configuration Server states and bindings") and the messages listed in [Table 4.312](index-en.html#UUID-73d8eb7c-f37a-9767-cd63-4999d115906a_Table_4.312 "Table 4.312. Configuration Server model messages").

The Configuration Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Configuration Server model shall use the device key.

[Table 4.311](index-en.html#UUID-73d8eb7c-f37a-9767-cd63-4999d115906a_Table_4.311 "Table 4.311. Configuration Server states and bindings") illustrates the state bindings between the Configuration Server model states.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Secure Network Beacon | – | – |
| Composition Data | – | – |
| Default TTL | – | – |
| GATT Proxy | Configuration Server | Node Identity |
| Friend | – | – |
| Relay | – | – |
| Model Publication | – | – |
| Subscription List | – | – |
| NetKey List | – | – |
| AppKey List | – | – |
| Model To AppKey List | – | – |
| Node Identity | – | – |
| Key Refresh Phase | – | – |
| Heartbeat Publish | – | – |
| Heartbeat Subscription | – | – |
| Network Transmit | – | – |
| Relay Retransmit | – | – |

Table 4.311. Configuration Server states and bindings

[Table 4.312](index-en.html#UUID-73d8eb7c-f37a-9767-cd63-4999d115906a_Table_4.312 "Table 4.312. Configuration Server model messages") lists the Configuration Server model messages. The model shall support receiving the messages marked as mandatory in the Rx column
and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Primary | Configuration Server | Secure Network Beacon  (see [Section 4.2.11](index-en.html#UUID-3764465c-cf65-2df6-cedc-c9fc106e8336 "4.2.11. Secure Network Beacon")) | Config Beacon Get | M | – |
| Config Beacon Set | M | – |
| Config Beacon Status | – | M |
| Composition Data  (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")) | Config Composition Data Get | M | – |
| Config Composition Data Status | – | M |
| Default TTL  (see [Section 4.2.8](index-en.html#UUID-a8dfaeb9-3d97-ed05-dc57-06975d19fcdb "4.2.8. Default TTL")) | Config Default TTL Get | M | – |
| Config Default TTL Set | M | – |
| Config Default TTL Status | – | M |
| GATT Proxy  (see [Section 4.2.12](index-en.html#UUID-43c162ac-873e-994c-4994-cceb056e6cf3 "4.2.12. GATT Proxy")) | Config GATT Proxy Get | M | – |
| Config GATT Proxy Set | M | – |
| Config GATT Proxy Status | – | M |
| Friend  (see [Section 4.2.14](index-en.html#UUID-1825212b-bf29-c33f-2a8e-c159b53f1eec "4.2.14. Friend")) | Config Friend Get | M | – |
| Config Friend Set | M | – |
| Config Friend Status | – | M |
| Relay  (see [Section 4.2.9](index-en.html#UUID-51ed1508-829e-308c-5062-ee04978bb22b "4.2.9. Relay")) and   Relay Retransmit   (see [Section 4.2.21](index-en.html#UUID-0b36a2de-a550-d0f8-677a-5cc500a65aa3 "4.2.21. Relay Retransmit")) | Config Relay Get | M | – |
| Config Relay Set | M | – |
| Config Relay Status | – | M |
| Model Publication  (see [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129")) | Config Model Publication Get | M | – |
| Config Model Publication Set | M | – |
| Config Model Publication Virtual Address Set | M | – |
| Config Model Publication Status | – | M |
| Subscription List  (see [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List")) | Config Model Subscription Add | M | – |
| Config Model Subscription Virtual Address Add | M | – |
| Config Model Subscription Delete | M | – |
| Config Model Subscription Virtual Address Delete | M | – |
| Config Model Subscription Virtual Address Overwrite | M | – |
| Config Model Subscription Overwrite | M | – |
| Config Model Subscription Delete All | M | – |
| Config Model Subscription Status | – | M |
| Config SIG Model Subscription Get | M | – |
| Config SIG Model Subscription List | – | M |
| Config Vendor Model Subscription Get | M | – |
| Config Vendor Model Subscription List | – | M |
| NetKey List  (see [Section 4.2.5](index-en.html#UUID-a4e051bc-0765-7678-6187-aee13f713495 "4.2.5. NetKey List")) | Config NetKey Add | M | – |
| Config NetKey Update | M | – |
| Config NetKey Delete | M | – |
| Config NetKey Status | – | M |
| Config NetKey Get | M | – |
| Config NetKey List | – | M |
| AppKey List  (see [Section 4.2.6](index-en.html#UUID-408e5b57-a0fd-9a95-a6d3-65d85d9dd69d "4.2.6. AppKey List")) | Config AppKey Add | M | – |
| Config AppKey Update | M | – |
| Config AppKey Delete | M | – |
| Config AppKey Status | – | M |
| Config AppKey Get | M | – |
| Config AppKey List | – | M |
| Model To AppKey List  (see [Section 4.2.7](index-en.html#UUID-dc4739ad-10e2-2ffa-26b9-65891e5a673a "4.2.7. Model To AppKey List")) | Config Model App Bind | M | – |
| Config Model App Unbind | M | – |
| Config Model App Status | – | M |
| Config SIG Model App Get | M | – |
| Config SIG Model App List | – | M |
| Config Vendor Model App Get | M | – |
| Config Vendor Model App List | – | M |
| Node Identity  (see [Section 4.2.13](index-en.html#UUID-14ebcb7c-e739-3862-af95-05eb8b4b2c97 "4.2.13. Node Identity")) | Config Node Identity Get | M | – |
| Config Node Identity Set | M | – |
| Config Node Identity Status | – | M |
| N/A | Config Node Reset | M | – |
| Config Node Reset Status | – | M |
| Key Refresh Phase (see [Section 4.2.15](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356 "4.2.15. Key Refresh Phase")) | Config Key Refresh Phase Get | M | – |
| Config Key Refresh Phase Set | M | – |
| Config Key Refresh Phase Status | – | M |
| Heartbeat Publication (see [Section 4.2.18](index-en.html#UUID-77d5df26-1351-cc93-d733-38817a094198 "4.2.18. Heartbeat Publication")) | Config Heartbeat Publication Get | M | – |
| Config Heartbeat Publication Set | M | – |
| Config Heartbeat Publication Status | – | M |
| Heartbeat Subscription (see [Section 4.2.19](index-en.html#UUID-23a5a1db-9d53-1bc0-0385-8da5bc458f9d "4.2.19. Heartbeat Subscription")) | Config Heartbeat Subscription Get | M | – |
| Config Heartbeat Subscription Set | M | – |
| Config Heartbeat Subscription Status | – | M |
| Network Transmit (see [Section 4.2.20](index-en.html#UUID-dccb10ac-b38d-031d-bf38-c007347342db "4.2.20. Network Transmit")) | Config Network Transmit Get | M | – |
| Config Network Transmit Set | M | – |
| Config Network Transmit Status | – | M |

Table 4.312. Configuration Server model messages

##### 4.4.1.2. Behavior

This section describes behaviors for states and messages for this server model.

###### 4.4.1.2.1. Secure Network Beacon state

When an element receives a Config Beacon Get message, it shall respond with a Config Beacon Status message with the Beacon field set to the current Secure Network Beacon state.

When an element receives a Config Beacon Set message, it shall set the Secure Network Beacon state to the value of the Beacon field of the message and respond with a Config Beacon Status message with the Beacon field set to the current Secure Network Beacon state.

###### 4.4.1.2.2. Composition Data state

When an element receives a Config Composition Data Get message with the Page field of the message containing a value of a Composition Data Page that the node contains, it shall respond with a Config Composition Data Status message with the Page field set to the page number of the Composition Data and the Data field set to
the value of the largest portion of the Composition Data Page that fits in the Data field. If an element is reported in the Config Composition Data Status message, the complete list of models supported by the element shall be included in the elements description (see [Table 4.5](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.5 "Table 4.5. Element description format") and [Table 4.7](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.7 "Table 4.7. Element field format")). If
the complete list of models does not fit in the Data field, the element shall not be reported.

When an element receives a Config Composition Data Get message with the Page field of the message containing a reserved page number or a page number the node does not support, it shall respond with a Config Composition Data Status message with the Page field set to the largest page number of the Composition Data that the
node supports and that is less than the Page field value of the received Config Composition Data Get message and with the Data field set to the value of the largest portion of the Composition Data Page for that page number that fits in the Data field. If an element is reported in a Config Composition Data Status message, the
complete list of models supported by the element shall be included in the elements description (see [Table 4.5](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a_Table_4.5 "Table 4.5. Element description format") and [Table 4.7](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31_Table_4.7 "Table 4.7. Element field format")). If the complete list of models does not fit in the Data field, the element shall not be reported.

### Note on Composition Data Pages

Note: It is possible to read all supported Composition Data Pages by reading 0xFF first, and then reading one less than the returned page number until the page number is 0x00.

###### 4.4.1.2.3. Default TTL state

When an element receives a Config Default TTL Get message, it shall respond with a Config Default TTL Status message with the TTL field set to the current Default TTL state.

When an element receives a Config Default TTL Set message, it shall set the Default TTL state to the value of the TTL field of the message and respond with a Config Default TTL Status message with the TTL field set to the current Default TTL state.

###### 4.4.1.2.4. GATT Proxy state

When an element receives a Config GATT Proxy Get message, it shall respond with a Config GATT Proxy Status message with the GATTProxy field set to the current GATT Proxy state.

When an element receives a Config GATT Proxy Set message and the node supports the Mesh GATT Proxy Service, it shall set the GATT Proxy state to the value of the GATTProxy field of the message and respond with a Config GATT Proxy Status message with the GATTProxy field set to the current GATT Proxy state.

When an element receives a Config GATT Proxy Set message and the node does not support the Mesh GATT Proxy Service, it shall respond with a Config GATT Proxy Status message with the GATTProxy field set to the current GATT Proxy state.

###### 4.4.1.2.5. Friend state

When an element receives a Config Friend Get message, it shall respond with a Config Friend Status message with the Friend field set to the current Friend state.

When an element receives a Config Friend Set message and the node supports the Friend feature, it shall set the Friend state to the value of the Friend field of the message and respond with a Config Friend Status message with the Friend field set to the current Friend state.

When an element receives a Config Friend Set message and the node does not support the Friend feature, it shall respond with a Config Friend Status message with the Friend field set to the current Friend state.

###### 4.4.1.2.6. Relay state

When an element receives a Config Relay Get message, it shall respond with a Config Relay Status message with the Relay field set to the current Relay state, and with the RelayRetransmitCount field set to the current Relay Retransmit Count state, and with the RelayRetransmitIntervalSteps field set to the current Relay
Retransmit Interval Steps state.

When an element receives a Config Relay Set message and the node supports the Relay feature, it shall set the Relay state to the value of the Relay field of the message, and set the Relay Retransmit Count state to the value of the RelayRetransmitCount field of the message, and set the Relay Retransmit Interval Steps state to
the value of the RelayRetransmitIntervalSteps field of the message and respond with a Config Relay Status message with the Relay field set to the current Relay state, and with the RelayRetransmitCount field set to the current Relay Retransmit Count state, and with the RelayRetransmitIntervalSteps field set to the current Relay
Retransmit Interval Steps state.

When an element receives a Config Relay Set message and the node does not support the Relay feature, it shall respond with a Config Relay Status message with the Relay field set to the current Relay state, and setting the RelayRetransmitCount and RelayRetransmitIntervalSteps fields to 0x00.

###### 4.4.1.2.7. Model Publication state

When an element receives a Config Model Publication Get message that is processed successfully (i.e., it does not result in any error conditions listed in [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")), it shall respond with a Config Model Publication Status message with the current values of the identified Model Publication state, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message and setting the
Status field to Success. When the PublishAddress is set to the unassigned address, the values of the AppKeyIndex, CredentialFlag, PublishTTL, PublishPeriod, PublishRetransmitCount, and PublishRetransmitIntervalSteps fields shall be set to 0x00.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The model defined by ElementAddress and ModelIdentifier does not support the publish mechanism | Invalid Publish Parameters |
| The unicast address provided in ElementAddress is not known to the node | Invalid Address |
| The model identified by SIG Model ID or Vendor Model ID is not found in a given element | Invalid Model |
| The AppKey identified by AppKeyIndex is not known to the node or is not bound to the model identified by the ModelIdentifier | Invalid AppKey Index |
| The CredentialFlag cannot be set to 1 since the node does not support Low Power feature | Feature Not Supported |

Table 4.313. Error conditions for Model Publication state

When an element receives a Config Model Publication Get message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")), it shall respond with the Config Model Publication Status message, setting its fields to the values of the corresponding fields (i.e., the identically named fields) of the incoming message, setting the Status field to a status code
(defined in [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")), and setting all other fields to 0x00.

When an element receives a Config Model Publication Set message or a Config Model Publication Virtual Address Set message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")), it shall update the identified Model Publication state to the corresponding field values (defined in [Table 4.314](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.314 "Table 4.314. Model Publication state to message field mappings")) and respond with a Config Model Publication Status message with the new values of the identified Model Publication state, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message and setting the
Status field to Success. When the Publish Address field of a Config Model Publication Set message is set to the unassigned address, the publication of the model shall be disabled and the AppKeyIndex, CredentialFlag, PublishTTL, PublishPeriod, PublishRetransmitCount, and PublishRetransmitIntervalSteps shall be ignored.

| State | Message Field |
| --- | --- |
| Publish AppKey Index | AppKeyIndex |
| Publish Friendship Credentials Flag | CredentialFlag |
| Publish TTL | PublishTTL |
| Publish Period | PublishPeriod |
| Publish Retransmission Count | PublishRetransmitCount |
| Publish Retransmit Interval Steps | PublishRetransmitIntervalSteps |
| Publish Address | PublishAddress |

Table 4.314. Model Publication state to message field mappings

When an element receives a Config Model Publication Set message or a Config Model Publication Virtual Address Set message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")), it shall respond with a Config Model Publication Status message setting the ElementAddress and ModelIdentifier fields to the corresponding fields of the incoming message, setting the Status field to a status code (defined in ), and
setting all other fields to 0x00.

###### 4.4.1.2.8. Subscription List state

When an element receives a Config Model Subscription Add message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to add an address identified by the value of the Address field that is not existing in the identified Subscription List, it shall add the value of the Address field to the identified Subscription List and respond with a
Config Model Subscription Status message, setting the Address, ElementAddress, and ModelIdentifier fields as defined by the incoming message and setting the Status field to Success. If it is an element of a Directed Forwarding node, the element shall trigger a Directed Forwarding Solicitation (see [Section 3.6.8.2.7](index-en.html#UUID-23c95a35-5300-5925-d06c-db472cc2f47e "3.6.8.2.7. Directed Forwarding Solicitation")).

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The model defined by ElementAddress and ModelIdentifier does not support subscription mechanism | Not a Subscribe Model |
| The device cannot store new address due to insufficient resources on device | Insufficient Resources |
| The unicast address provided in ElementAddress is not known to the node | Invalid Address |
| The model identified by SIG Model ID or Vendor Model ID is not found in a given element | Invalid Model |

Table 4.315. Error conditions for Subscription List state

When an element receives a Config Model Subscription Add message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to add an address identified by the value of the Address field that is existing in the identified Subscription List, it shall respond with a Config Model Subscription Status message, setting the Address, ElementAddress,
and ModelIdentifier fields as defined by the incoming message and setting the Status field to Success.

When an element receives a Config Model Subscription Add message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting its fields to the values of the corresponding fields (i.e., the identically named fields) of the incoming message, setting the Status field to a status code
(defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting all other fields to 0.

When an element receives a Config Model Subscription Virtual Address Add message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to add a Label UUID identified by the value of the Label field that is not existing in the identified Subscription List, it shall add the value of the Label field to the identified Subscription List and respond with a
Config Model Subscription Status message, setting the Address field to the value of the virtual address of the identified Label UUID, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Model Subscription Virtual Address Add message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to add a Label UUID identified by the value of the Label field that is existing in the identified Subscription List, it shall respond with a Config Model Subscription Status message, setting the Address field to the
value of the virtual address of the identified Label UUID, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Model Subscription Virtual Address Add message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting its fields to the values of the corresponding fields (i.e., the identically named fields) of the incoming message, setting the Address field to the value of the
virtual address of the identified Label UUID, setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting all
other fields to 0.

When an element receives a Config Model Subscription Delete message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to delete an address identified by the value of the Address field that is existing in the identified Subscription List, it shall delete the value of the Address field from the identified Subscription List and respond
with a Config Model Subscription Status message, setting the Address, ElementAddress, and ModelIdentifier fields as defined by the incoming message and setting the Status field to Success.

When an element receives a Config Model Subscription Delete message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to delete an address identified by the value of the Address field that is not existing in the identified Subscription List, it shall respond with a Config Model Subscription Status message, setting the Address,
ElementAddress, and ModelIdentifier fields as defined by the incoming message and setting the Status field to Success.

When an element receives a Config Model Subscription Delete message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting its fields to the values of the corresponding fields of the incoming message, setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting all other fields to 0.

When an element receives a Config Model Subscription Virtual Address Delete message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to delete a Label UUID identified by the value of the Label field that is existing in the identified Subscription List, it shall delete the value of the Label field from the identified Subscription List and respond with
a Config Model Subscription Status message, setting the Address field to the value of the virtual address of the identified Label UUID, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Model Subscription Virtual Address Delete message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")) and is requesting to delete a Label UUID identified by the value of the Label field that is not existing in the identified Subscription List, it shall respond with a Config Model Subscription Status message, setting the Address field to
the value of the virtual address of the identified Label UUID, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Model Subscription Virtual Address Delete message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting the Address field to the value of the virtual address of the identified Label UUID, setting its fields to the values of the corresponding fields of the incoming
message, setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting all other fields to 0.

When an element receives a Config Model Subscription Overwrite message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall clear the identified Subscription List, add an address identified by the value of the Address field to the identified Subscription List, and respond with a Config Model Subscription Status message, setting the Address,
ElementAddress, and ModelIdentifier fields as defined by the incoming message and setting the Status field to Success. If it is an element of a Directed Forwarding node, the element shall trigger a Directed Forwarding Solicitation (see [Section 3.6.8.2.7](index-en.html#UUID-23c95a35-5300-5925-d06c-db472cc2f47e "3.6.8.2.7. Directed Forwarding Solicitation")).

When an element receives a Config Model Subscription Overwrite message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting the message fields to the values of the corresponding fields of the incoming message and setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")).

When an element receives a Config Model Subscription Virtual Address Overwrite message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall clear the identified Subscription List, add the value of the Label field to the identified Subscription List, and respond with a Config Model Subscription Status message, setting the Address field to the value of the virtual
address of the identified Label UUID message, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Model Subscription Virtual Address Overwrite message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting its fields to the values of the corresponding fields of the incoming message, setting the Address field to the value of the virtual address of the identified
Label UUID, and setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")).

When an element receives a Config Model Subscription Delete All message that is successfully processed (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall clear the identified Subscription List and respond with a Config Model Subscription Status message, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, setting the Address field to
unassigned address value, and setting the Status field to Success.

When an element receives a Config Model Subscription Delete All message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Model Subscription Status message, setting its fields to the values of the corresponding fields of the incoming message, setting the Address field to unassigned address value, and setting the Status
field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting all other fields to 0.

When an element receives a Config SIG Model Subscription Get message that is processed successfully (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with a Config SIG Model Subscription List message with the current values of the identified Subscription List state, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message and setting
the Status field to Success.

When an element receives a Config Vendor Model Subscription Get message that is processed successfully (i.e., the processing of the message does not result in any error conditions listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with a Config Vendor Model Subscription List message with the current values of the identified Subscription List state, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message and
setting the Status field to Success.

When an element receives a Config SIG Model Subscription Get message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config SIG Model Subscription List message, setting its fields to the values of the corresponding fields of the incoming message, setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting the Addresses field to a zero-length (empty) list.

When an element receives a Config Vendor Model Subscription Get message that is not successfully processed (i.e., the processing of the message results in an error condition listed in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), it shall respond with the Config Vendor Model Subscription List message, setting its fields to the values of the corresponding fields of the incoming message, setting the Status field to a status code (defined in [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")), and setting the Addresses field to a zero-length (empty) list.

###### 4.4.1.2.9. NetKey List state

When an element receives a Config NetKey Add message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall add a new NetKey identified by the NetKeyIndex field to the NetKey List and respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to Success.

### Note on NetKey Add Idempotency

Note: When an element receives a Config NetKey Add message that identifies a NetKey that has already been added to the NetKey List, it responds with Success, because the result of adding the key again, with the same NetKey value, using the same NetKeyIndex will be the same as the result of adding the key the first
time.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The NetKey identified by NetKeyIndex is already stored in the node and the new NetKey value is different | Key Index Already Stored |
| The key identified by NetKeyIndex is not valid for this device for Config NetKey Update message | Invalid NetKey Index |
| The node cannot store the new key due to insufficient resources | Insufficient Resources |
| The requested delete operation cannot be performed due to general constraints | Cannot Remove |
| The requested update operation cannot be performed due to general constraints | Cannot Update |

Table 4.316. Error conditions for NetKey List state

When an element receives a Config NetKey Add message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")).

When an element receives a Config NetKey Update message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall update the value of the NetKey identified by NetKeyIndex field and respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config NetKey Update message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")).

When an element receives a Config NetKey Delete message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall delete NetKey identified by NetKeyIndex field from the NetKey List, delete all AppKeys bound to the deleted NetKey, and respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message,
and setting the Status field to Success.

The foundation model states bound to the deleted NetKey and AppKeys shall be updated as follows:

* When an AppKey used in model Publication is deleted as a result of the processing of the Config NetKey Delete message, the publication for the appropriate models shall be disabled.
* When NetKey used in Heartbeat Publication is deleted as a result of the processing of the Config NetKey Delete message, the Publication for the appropriate NetKey shall be disabled.
* When the Mesh Proxy Service is exposed, and the NetKey of the subnet utilized in advertising with Node Identity or Private Node Identity is deleted, the Node Identity state and the Private Node Identity state of the subnet of the deleted NetKey shall be set to 0x00.
* When a node supports directed forwarding functionality, and the functionality is enabled in a subnet corresponding to a NetKey that is deleted, the states associated with the functionality and with the subnet of the deleted NetKey shall be set to their default values (see [Sections 4.2.26](index-en.html#UUID-26bfef24-6d38-7b00-55a7-909e5862e7ad "4.2.26. Directed Control") to [4.2.40](index-en.html#UUID-efce1e35-df07-15c0-0784-95c584a64d65 "4.2.40. Directed Control Relay Retransmit")) and all the entries in the Forwarding
  Table state (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")) and in the Discovery Table (see [Section 3.6.8.6](index-en.html#UUID-ee4eeec1-2289-73dd-3feb-f577bc76533b "3.6.8.6. Discovery Table processing")) shall be removed.
* When a node supports subnet bridge functionality, and the NetKey that is deleted corresponds to any of the NetKey Indexes that are stored in the Bridging Table state of the node, all the Bridging Table state entries (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) with one of the values of the NetKeyIndex1 or NetKeyIndex2 fields that matches the NetKey Index of the deleted NetKey shall be removed.

When an element receives a Config NetKey Delete message that identifies a NetKey that is not in the NetKey List, it responds with Success, because the result of deleting a key that does not exist in the NetKey List is the same as if the key was deleted from the NetKey List.

When an element receives a Config NetKey Delete message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")), it shall respond with a Config NetKey Status message, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")).

When an element receives a Config NetKey Get message, it shall respond with a Config NetKey List message, setting the NetKeyIndexes field to a list of all indexes of NetKeys known to the node.

A NetKey shall not be deleted from the NetKey List using a message secured with this NetKey.

###### 4.4.1.2.10. AppKey List state

When an element receives a Config AppKey Add message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall add a new AppKey identified by AppKeyIndex field to the AppKey List, bind the new AppKey to the NetKey referenced by the NetKeyIndex, and respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as
defined by the incoming message, and setting the Status field to Success.

### Note on AppKey Add Idempotency

Note: When an element receives a Config AppKey Add message that identifies an AppKey that has already been added to the AppKey List, it responds with Success, because the result of adding the key again, with the same AppKey value, using the same AppKeyIndex will be the same as the result of adding the key the first
time.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The AppKey identified by AppKeyIndex is already stored in the node and the new AppKey is different | Key Index Already Stored |
| The node cannot store the new key due to insufficient resources | Insufficient Resources |
| The key identified by AppKeyIndex is not valid for this device | Invalid AppKey Index |
| The key identified by NetKeyIndex is not valid for this device | Invalid NetKey Index |
| The requested update operation cannot be performed due to general constraints | Cannot Update |
| The NetKeyIndexAndAppKeyIndex combination is not valid for a Config AppKey Update message | Invalid Binding |
| The key identified by the AppKeyIndex is already bound to a different NetKeyIndex for a Config AppKey Add message | Invalid NetKey Index |

Table 4.317. Error Conditions for AppKey List state

When an element receives a Config AppKey Add message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")).

When an element receives a Config AppKey Update message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall update the value of the AppKey identified by the AppKeyIndex field to the AppKey List and respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as defined by the incoming message, and setting the
Status field to Success.

When an element receives a Config AppKey Update message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")).

When an element receives a Config AppKey Delete message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall delete the AppKey identified by the AppKeyIndex field from the AppKey List and respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as defined by the incoming message, and setting the Status field
to Success. When an AppKey used in Model Publication is deleted as a result of the processing of the Config AppKey Delete message, the publication for the appropriate models shall be disabled.

### Note on AppKey Delete Idempotency

Note: When an element receives a Config AppKey Delete message that identifies an AppKey that is not in the AppKey List, it responds with Success, because the result of deleting the key that does not exist in the AppKey List will be the same as if the key was deleted from the AppKey List.

When an element receives a Config AppKey Delete message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall respond with a Config AppKey Status message, setting the NetKeyIndexAndAppKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")).

When an element receives a Config AppKey Get message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall respond with a Config AppKey List message, setting the AppKeyIndexes field to a list of all indexes of AppKeys bound to the NetKey identified by the NetKeyIndex field, setting the NetKeyIndex field as defined by the incoming message,
and setting the Status field to Success.

When an element receives a Config AppKey Get message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), it shall respond with a Config AppKey List message, setting the NetKeyIndex field as defined by the incoming message, setting the Status field to a status code (defined in [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")), and setting the AppKeyIndexes field to a zero-length (empty) list.

###### 4.4.1.2.11. Model To AppKey List state

When an element receives a Config Model App Bind message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall bind the AppKey referenced by the AppKeyIndex to the identified Model and respond with a Config Model App Status message, setting the ElementAddress, AppKeyIndex, and ModelIdentifier fields as defined by the incoming
message, and setting the Status field to Success.

When an element receives a Config Model App Bind message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with the Config Model App Status message, setting its fields to the values of the corresponding fields (i.e., the identically named fields) of the incoming message, and setting the Status field to a status code
(defined in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")).

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The model identified by SIG Model ID or Vendor Model ID is not found for a given element | Invalid Model |
| The unicast address provided in ElementAddress is not used by the node | Invalid Address |
| The key identified by AppKeyIndex is not stored in the node | Invalid AppKey Index |
| The node cannot store new binding due to insufficient resources | Insufficient Resources |
| The requested bind operation cannot be performed due to general constraints | Cannot Bind |

Table 4.318. Error Conditions for Model To AppKey List state

When an element receives a Config Model App Unbind message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall unbind the AppKey referenced by the AppKeyIndex from the identified model and respond with a Config Model App Status message, setting the ElementAddress, AppKeyIndex, and ModelIdentifier fields as defined by the incoming
message, and setting the Status field to Success. When the specified AppKeyIndex is used by the identified model as a Publish AppKeyIndex the Model Publication, the publication for the model shall be disabled.

When an element receives a Config Model App Unbind message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with the Config Model App Status message, setting its fields to the values of the corresponding fields of the incoming message, and setting the Status field to a status code (defined in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")).

When an element receives a Config SIG Model App Get message that is processed successfully (i.e., it does not result in any error conditions listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with a Config SIG Model App List message with the current values of the identified Model To AppKey List, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the
Status field to Success.

When an element receives a Config SIG Model App Get message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with the Config SIG Model App List message, setting its fields to the values of the ElementAddress and ModelIdentifier of the incoming message, setting the Status field to a status code (defined in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), and setting the AppKeyIndexes field to a zero-length (empty) list.

When an element receives a Config Vendor Model App Get message that is processed successfully (i.e., it does not result in any error conditions listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with a Config Vendor Model App List message with the current values of the identified Model To AppKey List, setting the ElementAddress and ModelIdentifier fields as defined by the incoming message, and setting the
Status field to Success.

When an element receives a Config Vendor Model App Get message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), it shall respond with the Config Vendor Model App List message, setting its fields to the values of the ElementAddress and ModelIdentifier of the incoming message, setting the Status field to a status code (defined in [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")), and setting the AppKeyIndexes field to a zero-length (empty) list.

###### 4.4.1.2.12. Node Identity state

When an element receives a Config Node Identity Get message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")), it shall respond with a Config Node Identity Status message with the Identity field set to the current Node Identity state identified by the NetKeyIndex field, setting the NetKeyIndex field as defined by the incoming message, and setting
the Status field to Success.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |
| The node cannot start advertising with Node Identity since the maximum number of parallel advertising is reached | Temporarily Unable to Change State |

Table 4.319. Error Conditions for Node Identity state

When an element receives a Config Node Identity Get message that is not successfully processed (i.e., it results in any error conditions listed in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")), it shall respond with a Config Node Identity Status message, setting the NetKeyIndex field as defined by the incoming message, setting the Identity field to 0x00, and setting the Status field to a status code (defined in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")).

When an element receives a Config Node Identity Set message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")), it shall set the Node Identity state identified by the NetKeyIndex field to the value of the Identity field of the message and respond with a Config Node Identity Status message with the Identity field set to the current Node Identity state
of the NetKey, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Node Identity Set message that is not successfully processed (i.e., it results in any error conditions listed in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")), it shall respond with a Config Node Identity Status message, setting the NetKeyIndex and Identity fields as defined by the incoming message, and setting the Status field to a status code defined in [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state").

###### 4.4.1.2.13. Reset

When an element receives a Config Node Reset message, it shall perform the Node Removal procedure (see [Section 3.11.7](index-en.html#UUID-676ac19a-a0b3-ee16-fd92-6f1bce988596 "3.11.7. Node Removal procedure")) and respond with a Config Node Reset Status message.

###### 4.4.1.2.14. Key Refresh Phase state

When an element receives a Config Key Refresh Phase Get message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")), it shall respond with a Config Key Refresh Phase Status message with the Phase field set to the current Key Refresh Phase state, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to
Success.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |

Table 4.320. Error Conditions for Key Refresh Phase state

When an element receives a Config Key Refresh Phase Get message that is not successfully processed (i.e., it results in any of the error conditions listed in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")), it shall respond with a Config Key Refresh Phase Status message with the Phase field set to 0x00, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")).

When an element receives a Config Key Refresh Phase Set message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")), it shall set the Key Refresh Phase state according to [Table 4.31](index-en.html#UUID-a8fd1d39-99ef-3b09-6396-ac9c0e98a356_Table_4.31 "Table 4.31. Controllable Key Refresh transition values") and respond with a Config Key Refresh Phase Status message with the Phase field set to the current Key Refresh Phase state, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to Success.

When an element receives a Config Key Refresh Phase Set message that is not successfully processed (i.e., it results in any of the error conditions listed in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")), it shall respond with a Config Key Refresh Phase Status message with the Phase field set to 0x00, setting the NetKeyIndex field as defined by the incoming message, and setting the Status field to a status code (defined in [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")).

###### 4.4.1.2.15. Heartbeat Publication state

When an element receives a Config Heartbeat Publication Get message, it shall respond with a Config Heartbeat Publication Status message with the current values of the Heartbeat Publication state, setting the Status field to Success, setting the Destination field to the value of the Heartbeat Publication Destination state,
the CountLog field to the Heartbeat Publication Count Log representation of the Heartbeat Publication Count state, the PeriodLog field to the value of the Heartbeat Publication Period Log state, the TTL field to the value of the Heartbeat Publication TTL state, the Features field to the value of the Heartbeat Publication
Features state, and the NetKey Index to the value of the Heartbeat Publication NetKey Index state. When the Destination field is set to the unassigned address, the values of the CountLog, PeriodLog, TTL, and Features fields shall be set to 0x00 and NetKeyIndex field shall be set to 0x0000.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |

Table 4.321. Error Conditions for Heartbeat Publication state

When an element receives a Config Heartbeat Publication Set message that is not successfully processed (i.e., it results in any of the error conditions listed in [Table 4.321](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.321 "Table 4.321. Error Conditions for Heartbeat Publication state")), it shall respond with a Config Heartbeat Publication Status message, setting the Destination, CountLog, PeriodLog, and TTL fields to the values of corresponding fields of the incoming message and setting the Status field to a status
code (defined in [Table 4.321](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.321 "Table 4.321. Error Conditions for Heartbeat Publication state")).

When an element receives a Config Heartbeat Publication Set message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.321](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.321 "Table 4.321. Error Conditions for Heartbeat Publication state")), it shall update the Heartbeat Publication state to the corresponding field values (defined in [Table 4.322](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.322 "Table 4.322. Heartbeat Publication state to message field mappings")) and the Heartbeat Publication Count state to the corresponding value (defined in the [Table 4.323](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.323 "Table 4.323. CountLog Field Value to Heartbeat Publication Count State mappings")) and respond with a Config Heartbeat Publication Status message, setting the Status field to Success, setting the PeriodLog field to the value of the PeriodLog field of the Config Heartbeat Publication Set message
and setting the Destination, CountLog, TTL, Features, and NetKeyIndex fields with the new values of the corresponding fields of the Heartbeat Publication state.

| State | Message Field |
| --- | --- |
| Heartbeat Publication Destination | Destination |
| Heartbeat Publication Period Log | PeriodLog |
| Heartbeat Publication TTL | TTL |
| Heartbeat Publication Features | Features |
| Heartbeat Publication NetKey Index | NetKeyIndex |

Table 4.322. Heartbeat Publication state to message field mappings

| CountLog Field Value | Heartbeat Publication Count State |
| --- | --- |
| 0x00 | 0x0000 |
| 0x01–0x10 | 2(CountLog-1) |
| 0x11 | 0xFFFE |
| 0x12–0xFE | Prohibited |
| 0xFF | 0xFFFF |

Table 4.323. CountLog Field Value to Heartbeat Publication Count State mappings

###### 4.4.1.2.16. Heartbeat Subscription state

When an element receives a Config Heartbeat Subscription Get message, it shall respond with a Config Heartbeat Subscription Status message, setting the Status field to Success, setting the CountLog field to the Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state, setting the PeriodLog
field to the Heartbeat Subscription Period Log representation of the Heartbeat Subscription Period state, and setting the Source, Destination, MinHops and MaxHops fields to the current values of the corresponding fields (defined in [Table 4.324](index-en.html#UUID-eeff2121-5539-e9f5-0968-af33ff649589_Table_4.324 "Table 4.324. Heartbeat Subscription state to message field mappings")) of the Heartbeat Subscription state. When the Heartbeat Subscription Source state or the Heartbeat Subscription Destination state is set to the
unassigned address, the value of the Source and Destination fields of the Config Heartbeat Subscription Status message shall be set to the unassigned address and the values of the CountLog, PeriodLog, MinHops, and MaxHops fields shall be set to 0x00.

When an element receives a Config Heartbeat Subscription Set message, and at least one of the following conditions is met:

* The Source field is set to the unassigned address.
* The Destination field is set to the unassigned address.
* The PeriodLog field is set to 0x00.

then the element shall perform the following actions:

* Disable the processing of received Heartbeat messages.
* Set the Heartbeat Subscription Source state to the unassigned address.
* Set the Heartbeat Subscription Destination state to the unassigned address.
* Set the Heartbeat Subscription Period state to 0x00.
* Respond with a Config Heartbeat Subscription Status message with the following field values:

  * The Status field set to Success
  * The Source, Destination, MinHops, and MaxHops fields set to the new values of the corresponding fields of the Heartbeat Subscription state
  * The CountLog field set to the Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state
  * The PeriodLog field set to the Heartbeat Subscription Period Log representation of the Heartbeat Subscription Period state

When an element receives a Config Heartbeat Subscription Set message, and all of the following conditions are met:

* The Source field is set to a unicast address.
* The Destination field is set to a unicast address or a group address.
* The PeriodLog field is set to a non-zero value.

then the element shall perform the following actions:

* Update the Heartbeat Subscription state to the corresponding field values (defined in [Table 4.324](index-en.html#UUID-eeff2121-5539-e9f5-0968-af33ff649589_Table_4.324 "Table 4.324. Heartbeat Subscription state to message field mappings")).
* Set the Heartbeat Subscription Period state to the corresponding value (defined in the [Table 4.325](index-en.html#UUID-eeff2121-5539-e9f5-0968-af33ff649589_Table_4.325 "Table 4.325. PeriodLog Field Value to Heartbeat Subscription Period state mappings")).
* Set the Heartbeat Subscription MinHops state to 0x7F.
* Set the Heartbeat Subscription MaxHops state to 0x00.
* Set the Heartbeat Subscription Count state to 0x0000.
* Enable the processing of received Heartbeat messages.
* Respond with a Config Heartbeat Subscription Status message with the following field values:

  * The Status field set to Success
  * The Source, Destination, MinHops, and MaxHops fields set to the new values of the corresponding fields of the Heartbeat Subscription state
  * The CountLog field set to the Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state
  * The PeriodLog field set to the Heartbeat Subscription Period Log representation of the Heartbeat Subscription Period state

| State | Message Field |
| --- | --- |
| Heartbeat Subscription Source | Source |
| Heartbeat Subscription Destination | Destination |
| Heartbeat Subscription Min Hops | MinHops |
| Heartbeat Subscription Max Hops | MaxHops |

Table 4.324. Heartbeat Subscription state to message field mappings

| PeriodLog Field Value | Heartbeat Subscription Period State |
| --- | --- |
| 0x00 | 0x0000 |
| 0x01–0x11 | 2(PeriodLog-1) |
| 0x12–0xFF | Prohibited |

Table 4.325. PeriodLog Field Value to Heartbeat Subscription Period state mappings

### Note on Heartbeat Subscription and LPN Nodes

Note: Using heartbeat with LPN nodes as destinations is not recommended as it may cause the Friend Queue to overflow. However, if the subscribing element is within a Low Power Node, it should update the Friend Subscription List (see [Section 3.6.6.4.3](index-en.html#UUID-e120fc07-9072-b778-f0af-cd6589b44141 "3.6.6.4.3. Low Power management")).

###### 4.4.1.2.17. PollTimeout List state

When an element receives a Config Low Power Node PollTimeout Get message, it shall respond with a Config Low Power Node PollTimeout Status message with the PollTimeout field set to the current PollTimeout List state element identified by the value of the LPNAddress field.

###### 4.4.1.2.18. Network Transmit state

When an element receives a Config Network Transmit Get message, it shall respond with a Config Network Transmit Status message that has the NetworkTransmitCount field set to the current Network Transmit Count state and the NetworkTransmitIntervalSteps field set to the current Network Transmit Interval Steps state.

When an element receives a Config Network Transmit Set message, it shall set the Network Transmit Count state to the value of the NetworkTransmitCount field and shall set the Network Transmit Interval Steps state to the value of the NetworkTransmitIntervalSteps fields of the message and shall respond with a Config Network
Transmit Status message that has the NetworkTransmitCount field set to the current Network Transmit Count state and the NetworkTransmitIntervalSteps field set to the current Network Transmit Interval Steps state.

##### 4.4.1.3. Error handling behavior

When a node receives a message that requires it to store some information in the node’s persistent memory and the storage is not successful, the node shall use the Storage Failure as a value of the Status Code. This might be either a permanent or a temporary situation.

When an error occurs that does not correspond to an error-handling condition (see [Section 4.1.3](index-en.html#UUID-ac153cdb-f490-1de9-72f9-bc4dd84078c6 "4.1.3. Error handling")) for message behaviors for a given state, the node shall use the Unspecified Error as a
value of the Status Code (see [Table 4.308](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.308 "Table 4.308. Summary of configuration and health messages status codes ")).

#### 4.4.2. Configuration Client model

##### 4.4.2.1. Description

The Configuration Client model is used to support the functionality of a node that can configure another mesh node.

The Configuration Client model is a root model and a main model that does not extend any other models. The Configuration Client model may operate on states defined by the Configuration Server model (see [Section 4.4.1](index-en.html#UUID-983db022-d6e3-ac72-0296-26a0d31afc91 "4.4.1. Configuration Server model")) using Configuration messages (see [Section 4.3.2](index-en.html#UUID-e202c58e-be9b-d732-ae6b-ebd7fab382cc "4.3.2. Configuration messages")).

If supported, the Configuration Client model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Configuration Client model shall use the device key of the node supporting the Configuration Server model.

[Table 4.326](index-en.html#UUID-0db73a3f-4b9a-b65c-b77f-d0a382a84459_Table_4.326 "Table 4.326. Configuration Client model messages") lists the Configuration Client model messages. The model shall support receiving the messages marked as mandatory in the Rx column
and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Primary | Configur­ation Client | Secure Network Beacon | Config Beacon Get | – | M |
| Config Beacon Set | – | M |
| Config Beacon Status | M | – |
| Composition Data | Config Composition Data Get | – | M |
| Config Composition Data Status | M | – |
| Default TTL | Config Default TTL Get | – | M |
| Config Default TTL Set | – | M |
| Config Default TTL Status | M | – |
| GATT Proxy | Config GATT Proxy Get | – | M |
| Config GATT Proxy Set | – | M |
| Config GATT Proxy Status | M | – |
| Friend | Config Friend Get | – | M |
| Config Friend Set | – | M |
| Config Friend Status | M | – |
| Relay | Config Relay Get | – | M |
| Config Relay Set | – | M |
| Config Relay Status | M | – |
| Model Publication | Config Model Publication Get | – | M |
| Config Model Publication Set | – | M |
| Config Model Publication Virtual Address Set | – | M |
| Config Model Publication Status | M | – |
| Subscription List | Config Model Subscription Add | – | M |
| Config Model Subscription Virtual Address Add | – | M |
| Config Model Subscription Delete | – | M |
| Config Model Subscription Virtual Address Delete | – | M |
| Config Model Subscription Overwrite | – | M |
| Config Model Subscription Virtual Address Overwrite | – | M |
| Config Model Subscription Delete All | – | M |
| Config Model Subscription Status | M | – |
| Config SIG Model Subscription Get | – | M |
| Config SIG Model Subscription List | M | – |
| Config Vendor Model Subscription Get | – | M |
| Config Vendor Model Subscription List | M | – |
| NetKey List | Config NetKey Add | – | M |
| Config NetKey Update | – | M |
| Config NetKey Delete | – | M |
| Config NetKey Status | M | – |
| Config NetKey Get | – | M |
| Config NetKey List | M | – |
| AppKey List | Config AppKey Add | – | M |
| Config AppKey Update | – | M |
| Config AppKey Delete | – | M |
| Config AppKey Status | M | – |
| Config AppKey Get | – | M |
| Config AppKey List | M | – |
| Model To AppKey List | Config Model App Bind | – | M |
| Config Model App Unbind | – | M |
| Config Model App Status | M | – |
| Config SIG Model App Get | – | M |
| Config SIG Model App List | M | – |
| Config Vendor Model App Get | – | M |
| Config Vendor Model App List | M | – |
| Node Identity | Config Node Identity Get | – | M |
| Config Node Identity Set | – | M |
| Config Node Identity Status | M | – |
| Reset | Config Node Reset | – | M |
| Config Node Reset Status | M | – |
| Key Refresh Phase | Config Key Refresh Phase Get | – | M |
| Config Key Refresh Phase Set | – | M |
| Config Key Refresh Phase Status | M | – |
| Heartbeat Publication | Config Heartbeat Publication Get | – | M |
| Config Heartbeat Publication Set | – | M |
| Config Heartbeat Publication Status | M | – |
| Heartbeat Subscription | Config Heartbeat Subscription Get | – | M |
| Config Heartbeat Subscription Set | – | M |
| Config Heartbeat Subscription Status | M | – |
| Network Transmit | Config Network Transmit Get | – | M |
| Config Network Transmit Set | – | M |
| Config Network Transmit Status | M | – |

Table 4.326. Configuration Client model messages

##### 4.4.2.2. Behavior

This section describes behaviors for procedures and messages for this client model.

An element can send any Configuration Client message at any time to query or change a configuration state of a peer element.

###### 4.4.2.2.1. Secure Network Beacon procedure

To determine the Secure Network Beacon state of a Configuration Server, a Configuration Client shall send a Config Beacon Get message. The response is a Config Beacon Status message that contains the Secure Network Beacon state.

To set the Secure Network Beacon state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Beacon Set message. The response is a Config Beacon Status message that contains the Secure Network Beacon state.

Upon receiving a Config Beacon Status message, a Configuration Client can determine the Secure Network Beacon state of a Configuration Server.

###### 4.4.2.2.2. Composition Data procedure

The Composition Data state of a server is composed or one or more pages. To determine the Composition Data state of a Configuration Server, a Configuration Client shall send a Config Composition Data Get message with the Page field value set to 0xFF. The response is a Config Composition Data Status message that contains the
last page (or a portion of that page) of the Composition Data state. If the Page field of the Config Composition Data Status message contains a non-zero value, then the Configuration Client shall send another Composition Data Get message with the Page field value set to one less than the Page field value of the Config
Composition Data Status message.

###### 4.4.2.2.3. Default TTL procedure

To determine the Default TTL state of a Configuration Server, a Configuration Client shall send a Config Default TTL Get message. The response is a Config Default TTL Status message that contains the Default TTL state.

To set the Default TTL state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Default TTL Set message. The response is a Config Default TTL Status message that contains the Default TTL state.

Upon receiving a Config Default TTL Status message, a Configuration Client can determine the current Default TTL state of a Configuration Server.

###### 4.4.2.2.4. GATT Proxy procedure

To determine the GATT Proxy state of a Configuration Server, a Configuration Client shall send a Config GATT Proxy Get message. The response is a Config GATT Proxy Status message that contains the GATT Proxy state.

To set the GATT Proxy state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config GATT Proxy Set message. The response is a Config GATT Proxy Status message that contains the GATT Proxy state.

Upon receiving a Config GATT Proxy Status message, a Configuration Client can determine the current GATT Proxy state of a Configuration Server.

###### 4.4.2.2.5. Friend procedure

To determine the Friend state of a Configuration Server, a Configuration Client shall send a Config Friend Get message. The response is a Config Friend Status message that contains the Friend state.

To set the Friend state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Friend Set message. The response is a Config Friend Status message that contains the Friend state.

Upon receiving a Config Friend Status message, a Configuration Client can determine the Friend state of a Configuration Server.

###### 4.4.2.2.6. Relay procedure

To determine the Relay and Relay Retransmit states of a Configuration Server, a Configuration Client shall send a Config Relay Get message. The response is a Config Relay Status message that contains the Relay and Relay Retransmit states.

To set the Relay and Relay Retransmit states of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Relay Set message. The response is a Config Relay Status message that contains the Relay and Relay Retransmit states.

Upon receiving a Config Relay Status message, a Configuration Client can determine the current Relay and Relay Retransmit states of a Configuration Server.

###### 4.4.2.2.7. Model Publication procedure

To determine the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish TTL states of a particular model within the element, a Configuration Client shall send a Config Model Publication Get message. The response is a
Config Model Publication Status message that contains a status and may contain the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish TTL states.

To set the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish TTL states of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Publication Set message. The
response is a Config Model Publication Status message that contains a status and may contain the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish TTL states.

To unset the Publish Address state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Publication Set message with the PublishAddress field set to Unassigned and with the AppKeyIndex, CredentialFlag, PublishTTL, PublishRetransmitCount,
PublishRetransmitIntervalSteps, and PublishPeriod fields set to 0.

To set the Label UUID as the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, and Publish TTL states of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Publication Virtual Address Set message. The response is a Config Model
Publication Status message that contains a status and may contain the Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish TTL states.

Upon receiving a Config Model Publication Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.313](index-en.html#UUID-7fc7b58a-2251-c1d9-9ec7-0e4ecb66875c_Table_4.313 "Table 4.313. Error conditions for Model Publication state")). If it’s Success, the Configuration Client can also determine the current Publish Address, Publish AppKey Index, Publish Friendship Credential Flag, Publish Period, Publish Retransmit Count, Publish Retransmit Interval Steps, and Publish
TTL states of a particular model within the element. If it’s an error, the Status field shall contain the error condition; and the values of the PublishAddress, AppKeyIndex, CredentialFlag, PublishPeriod, PublishRetransmitCount, PublishRetransmitIntervalSteps, and PublishTTL fields shall be discarded.

###### 4.4.2.2.8. Subscription List procedure

To add the address to the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Add message. The response is a Config Model Subscription Status message that contains a status and may contain the added address value.

To add the Label UUID to the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Virtual Address Add message. The response is a Config Model Subscription Status message that contains a status and may contain the added
corresponding virtual address value.

To delete the address from the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Delete message. The response is a Config Model Subscription Status message that contains a status and may contain the deleted address value.

To delete the Label UUID from the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Virtual Address Delete message. The response is a Config Model Subscription Status message that contains a status and may contain the deleted
corresponding virtual address value.

To clear the Subscription List and add the address to the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Overwrite message. The response is a Config Model Subscription Status message that contains a status and may contain the
added address value.

To clear the Subscription List and add the Label UUID to the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Virtual Address Overwrite message. The response is a Config Model Subscription Status message that contains a status
and may contain the added corresponding virtual address value.

To clear the Subscription List of the Subscription List state of a particular model within the element with acknowledgment, a Configuration Client shall send a Config Model Subscription Delete All message. The response is a Config Model Subscription Status message that contains a status.

### Note on Subscription List Replay Protection

Note: After adding a previously not known group address to one of the node's subscription lists, the node is not protected against a replay attack utilizing messages to that new group address. It is therefore strongly recommended that the Configuration Client run, for a brief period of time, a Heartbeat Subscription
procedure on the node and a Heartbeat Publication procedure on all nodes that publish to the new group address to initialize the replay protection list of the node with the current value of the sequence numbers for all affected publishers.

Upon receiving a Config Model Subscription Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")). If it’s Success, the Configuration Client may determine the address that was used to change the Subscription List state of a particular model within the element. If it’s an error, the Status field will contain the error condition.

To determine the Subscription List state of a particular SIG Model within the element, a Configuration Client shall send a Config SIG Model Subscription Get message. The response is a Config SIG Model Subscription List message that contains a status and may contain the Subscription List state.

To determine the Subscription List state of a particular Vendor Model within the element, a Configuration Client shall send a Config Vendor Model Subscription Get message. The response is a Config Vendor Model Subscription List message that contains a status and may contain the Subscription List state.

Upon receiving a Config SIG Model Subscription List message or a Config Vendor Model Subscription List message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.315](index-en.html#UUID-904c46b4-6103-bf61-fe83-7890c92a47fe_Table_4.315 "Table 4.315. Error conditions for Subscription List state")). If it’s Success, the Configuration Client can also determine the current Subscription List state of a particular model within the element. If it’s an error, the Status field will contain the error condition, and the Addresses field will
be set to a zero-length (empty) list.

###### 4.4.2.2.9. NetKey List procedure

To add the NetKey identified by NetKeyIndex to the NetKey List state with acknowledgment, a Configuration Client shall send a Config NetKey Add message. The response is a Config NetKey Status message that contains a status and the NetKeyIndex value.

To update the NetKey identified by NetKeyIndex to the NetKey List state with acknowledgment, a Configuration Client shall send a Config NetKey Update message. The response is a Config NetKey Status message that contains a status and the NetKeyIndex value.

To delete the NetKey identified by NetKeyIndex to the NetKey List state with acknowledgment, a Configuration Client shall send a Config NetKey Delete message. The response is a Config NetKey Status message that contains a status and the NetKeyIndex value.

Upon receiving a Config NetKey Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.316](index-en.html#UUID-269d648a-b509-ed82-43ad-aaa3a3c9f0ce_Table_4.316 "Table 4.316. Error conditions for NetKey List state")) and the NetKeyIndex value. If it’s Success, the Status field will be set to Success. If it’s an error, the Status field will contain the error condition.

To determine the NetKey List of the Configuration Server, a Configuration Client shall send a Config NetKey Get message. The response is a Config NetKey List message that contains a NetKey List.

Upon receiving a Config NetKey List message, a Configuration Client can determine the current NetKey List of a Configuration Server.

###### 4.4.2.2.10. AppKey List procedure

To add the AppKey to the AppKey List and bind it to the NetKey identified by the NetKeyIndex of a Configuration Server with acknowledgment, a Configuration Client shall send a Config AppKey Add message. The response is a Config AppKey Status message that contains a status, the added AppKey index, and the NetKeyIndex
value.

To update the value of the AppKey from the AppKey List of the NetKey identified by the NetKeyIndex of a Configuration Server with acknowledgment, a Configuration Client shall send a Config AppKey Update message. The response is a Config AppKey Status message that contains a status, the added AppKey index, and the NetKeyIndex
value.

To delete the AppKey from the AppKey List of the NetKey identified by the NetKeyIndex of a Configuration Server with acknowledgment, a Configuration Client shall send a Config AppKey Delete message. The response is a Config AppKey Status message that contains a status, the deleted AppKey index, and the NetKeyIndex value.

Upon receiving a Config AppKey Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")). If it’s Success, the Configuration Client can determine the AppKey index that was used to change the AppKey List of the NetKey identified by the NetKeyIndex of a Configuration Server. If it’s an error, the Status field will contain the error
condition.

To determine the AppKey List of the NetKey identified by the NetKeyIndex of a Configuration Server, a Configuration Client shall send a Config AppKey Get message. The response is a Config AppKey List message that contains a status and may contain the AppKey List.

Upon receiving a Config AppKey List message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.317](index-en.html#UUID-5f03e5f5-0ec1-c734-0570-ecfe5bba72b8_Table_4.317 "Table 4.317. Error Conditions for AppKey List state")). If it’s Success, the Configuration Client can also determine the current AppKey List of the NetKey identified by the NetKeyIndex of a Configuration Server. If it’s an error, the Status field will contain the error condition, and the
AppKeyIndexes field will be set to a zero-length (empty) list.

###### 4.4.2.2.11. Model To AppKey List procedure

To bind the AppKey to a model of a particular element of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Model App Bind message. The response is a Config Model App Status message that contains a status and other fields set to the values of the corresponding fields (i.e., the identically
named fields) of the incoming message.

To unbind the AppKey from a model of a particular element of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Model App Unbind message. The response is a Config Model App Status message that contains a status and other fields set to the values of the corresponding fields of the incoming
message.

Upon receiving a Config Model App Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")). If it’s Success, the Configuration Client can also determine the values of the ElementAddress, AppKeyIndex, and ModelIdentifier that were used to change the Model To AppKey List state. If it’s an error, the Status field will contain
the error condition.

To determine the Model To AppKey List of a particular SIG Model within the element, a Configuration Client shall send a Config SIG Model App Get message. The response is a Config SIG Model App List message that contains a status and may contain the Model To AppKey List.

Upon receiving a Config SIG Model App List message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")). If it’s Success, the Configuration Client can also determine the current Model To AppKey List of a particular SIG Model within the element. If it’s an error, the Status field will contain the error condition, and the AppKeyIndexes
field will be set to a zero-length (empty) list.

To determine the Model To AppKey List of a particular Vendor Model within the element, a Configuration Client shall send a Config Vendor Model App Get message. The response is a Config Vendor Model App List message that contains a status and may contain the Model To AppKey List.

Upon receiving a Config Vendor Model App List message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.318](index-en.html#UUID-22a5be61-a733-0d57-0c87-90224ca4cb8f_Table_4.318 "Table 4.318. Error Conditions for Model To AppKey List state")). If it’s Success, the Configuration Client can also determine the current Model To AppKey List of a particular Vendor model within the element. If it’s an error, the Status field will contain the error condition, and the AppKeyIndexes
field will be set to a zero-length (empty) list.

###### 4.4.2.2.12. Node Identity procedure

To determine the Node Identity state of the NetKey identified by the NetKeyIndex of a Configuration Server, a Configuration Client shall send a Config Node Identity Get message. The response is a Config Node Identity Status message that contains a status, NetKeyIndex value, and the Node Identity state of the NetKey.

To set the Node Identity state of the NetKey identified by the NetKeyIndex of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Node Identity Set message. The response is a Config Node Identity Status message that contains a status, NetKeyIndex value, and the Node Identity state.

Upon receiving a Config Node Identity Status message, a Configuration Client can determine the status that can be either Success or an error (see [Table 4.319](index-en.html#UUID-970bd756-95dc-3f66-62e0-9ad0f7282ba9_Table_4.319 "Table 4.319. Error Conditions for Node Identity state")). If it’s Success, the Configuration Client can also determine the current Node Identity state of the NetKey identified by the NetKeyIndex of a Configuration Server. If it’s an error, the Status field will contain the error condition, and the
Identity field will be set to zero.

###### 4.4.2.2.13. Reset procedure

To initiate the Node Removal procedure of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Node Reset message. The response is a Config Node Reset Status message.

Upon receiving a Config Node Reset Status message, a Configuration Client can determine that the Node Removal procedure was initiated on a Configuration Server.

###### 4.4.2.2.14. Key Refresh Phase procedure

To determine the Key Refresh Phase state of a Configuration Server, a Configuration Client shall send a Config Key Refresh Phase Get message. The response is a Config Key Refresh Phase Status message that contains a status, the NetKeyIndex value, and the Key Refresh Phase state.

To set the Key Refresh Phase state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Key Refresh Phase Set message. The response is a Config Key Refresh Phase Status message that contains a status, the NetKeyIndex value, and the Key Refresh Phase state.

Upon receiving a Config Key Refresh Phase Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.320](index-en.html#UUID-046b829a-ef7f-0e65-e99f-9d9fa5053160_Table_4.320 "Table 4.320. Error Conditions for Key Refresh Phase state")). If it’s Success, the Configuration Client can also determine the current Key Refresh Phase state of the NetKey identified by the NetKeyIndex of a Configuration Server. If it’s an error, the Status field will contain the error
condition.

###### 4.4.2.2.15. Heartbeat Publication procedure

A configuration client may use the Heartbeat Publication and Heartbeat Subscription procedures to map a topology of the subnet. Using the Heartbeat Publication procedure sets one node to publish a series of Heartbeat messages (see [Section 3.6.5.10](index-en.html#UUID-f66f9eb6-eda7-e421-f5d1-b00037083e4f "3.6.5.10. Heartbeat")), and using the Heartbeat Subscription procedure sets another node to process received Heartbeat messages and report them to the configuration client.

To determine the Heartbeat Publication Destination, Heartbeat Publication Count Log representation of the Heartbeat Publication Count state, Heartbeat Publication Period Log, Heartbeat Publication TTL, Heartbeat Publication Features, and Heartbeat NetKey Index states of a node, a Configuration Client shall send a Config
Heartbeat Publication Get message. The response is a Config Heartbeat Publication Status message that contains the Heartbeat Publication Destination, Heartbeat Publication Count Log representation of the Heartbeat Publication Count state, Heartbeat Publication Period Log, Heartbeat Publication TTL, Heartbeat Publication
Features and Heartbeat Publication NetKey Index states.

To set the Heartbeat Publication Destination, Heartbeat Publication Count, Heartbeat Publication Period, Heartbeat Publication TTL, Publication Features, and Publication NetKey Index of a node with acknowledgment, a Configuration Client shall send a Config Heartbeat Publication Set message. The response is a Config Heartbeat
Publication Status message that contains a Status of the operation and the Heartbeat Publication Destination, Heartbeat Publication Count Log representation of the Heartbeat Publication Count state, Heartbeat Publication Period Log, Heartbeat Publication TTL, Heartbeat Publication Features, and Heartbeat Publication NetKey
Index states.

Upon receiving a Config Heartbeat Publication Status message, a Configuration Client can determine the status that can be either a Success or an error (see [Table 4.321](index-en.html#UUID-baad70be-ece0-a58e-ec19-bacba6579832_Table_4.321 "Table 4.321. Error Conditions for Heartbeat Publication state")). If it’s Success, the Configuration Client can also determine the current Heartbeat Publication Destination, Heartbeat Publication Count Log representation of the Heartbeat Publication Count state, Heartbeat Publication Period Log,
Heartbeat Publication TTL, Heartbeat Publication Features, and Heartbeat Publication NetKey Index states of a node. If it’s an error, the Status field will contain the error condition.

###### 4.4.2.2.16. Heartbeat Subscription procedure

To determine the Heartbeat Subscription Source, Heartbeat Subscription Destination, Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state, Heartbeat Subscription Period Log, Heartbeat Subscription Min Hops, and Heartbeat Subscription Max Hops states of a node, a Configuration Client shall
send a Config Heartbeat Subscription Get message. The response is a Config Heartbeat Subscription Status message that contains the Heartbeat Subscription Source, Heartbeat Subscription Destination, Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state, Heartbeat Subscription Period Log,
Heartbeat Subscription Min Hops, and Heartbeat Subscription Max Hops states.

To set the Heartbeat Subscription Source, Heartbeat Subscription Destination, Heartbeat Subscription Count, and Heartbeat Subscription Period states of a node with acknowledgment, a Configuration Client shall send a Config Heartbeat Subscription Set message. The response is a Config Heartbeat Subscription Status message that
contains a Status of the operation and the Heartbeat Subscription Source, Heartbeat Subscription Destination, Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state, Heartbeat Subscription Period Log, Heartbeat Subscription Min Hops, and Heartbeat Subscription Max Hops states.

Upon receiving a Config Heartbeat Subscription Status message, a Configuration Client can determine the current Heartbeat Subscription Source, Heartbeat Subscription Destination, Heartbeat Subscription Count Log representation of the Heartbeat Subscription Count state, Heartbeat Subscription Period Log, Heartbeat
Subscription Min Hops, and Heartbeat Subscription Max Hops states of a node.

###### 4.4.2.2.17. PollTimeout List procedure

To determine the current PollTimeout List state value of a Configuration Server, a Configuration Client shall send a Config Low Power Node PollTimeout Get message with the LPNAddress field set to the primary unicast address of the Low Power node. The response is a Config Low Power Node PollTimeout Status message that
contains the current value of the PollTimeout List state for that LPNAddress.

###### 4.4.2.2.18. Network Transmit procedure

To determine the Network Transmit state of a Configuration Server, a Configuration Client shall send a Config Network Transmit Get message. The response is a Config Network Transmit Status message that contains the Network Transmit state.

To set the Network Transmit state of a Configuration Server with acknowledgment, a Configuration Client shall send a Config Network Transmit Set message. The response is a Config Network Transmit Status message that contains the Network Transmit state.

Upon receiving a Config Network Transmit Status message, a Configuration Client can determine the Network Transmit state of a Configuration Server.

#### 4.4.3. Health Server model

##### 4.4.3.1. Description

The Health Server model is used to support the fault reporting and identification functionality of a node.

The Health Server model is a root model and a main model that does not extend any other models.

This model shall support model publication defined in [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129") and model subscription defined in [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List"). When configured for publication, the Health Server shall publish Health Current Status messages (see [Section 4.4.3.2.1](index-en.html#UUID-463cb148-16a9-f63c-5938-b059ddc5a641 "4.4.3.2.1. Current Fault state")). The Health Server model requires one element: the Health Main element. The Health Main element contains the Health Server main model.

The Health Server model defines the state instances listed in [Table 4.327](index-en.html#UUID-0f6d5518-eb7c-3fa2-4446-05f2fe530b47_Table_4.327 "Table 4.327. Health Server states and bindings") and the messages listed in [Table 4.328](index-en.html#UUID-0f6d5518-eb7c-3fa2-4446-05f2fe530b47_Table_4.328 "Table 4.328. Health Server model messages").

The Health Server model shall be supported by a primary element and may be supported by any secondary elements. The access layer security on the Health Server model shall use application keys.

[Table 4.327](index-en.html#UUID-0f6d5518-eb7c-3fa2-4446-05f2fe530b47_Table_4.327 "Table 4.327. Health Server states and bindings") illustrates the state bindings between the Health Server model states and the states of the models that the Health Server
extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Current Fault | – | – |
| Registered Fault | – | – |
| Health Period | – | – |
| Attention Timer | – | – |

Table 4.327. Health Server states and bindings

[Table 4.328](index-en.html#UUID-0f6d5518-eb7c-3fa2-4446-05f2fe530b47_Table_4.328 "Table 4.328. Health Server model messages") lists the Health Server model messages. The model shall support receiving the messages marked as mandatory in the Rx column and shall
support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Health Main | Health Server | Current Fault  (see [Section 4.2.16.1](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650 "4.2.16.1. Current Fault")) | Health Current Status | – | M |
| Registered Fault  (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")) | Health Fault Get | M | – |
| Health Fault Clear | M | – |
| Health Fault Clear Unacknowledged | M | – |
| Health Fault Status | – | M |
| Health Fault Test | M | – |
| Health Fault Test Unacknowledged | M | – |
| Health Period  (see [Section 4.2.17](index-en.html#UUID-eb28a070-d988-5b1a-a99c-5f99d1e3e085 "4.2.17. Health Fast Period Divisor")) | Health Period Get | M | – |
| Health Period Set | M | – |
| Health Period Set Unacknowledged | M | – |
| Health Period Status | – | M |
| Attention Timer  (see [Section 4.2.10](index-en.html#UUID-bce44a1d-9909-9847-e3f0-4d7b33ed3579 "4.2.10. Attention Timer")) | Health Attention Get | M | – |
| Health Attention Set | M | – |
| Health Attention Set Unacknowledged | M | – |
| Health Attention Status | – | M |

Table 4.328. Health Server model messages

##### 4.4.3.2. Behavior

This section describes behaviors for states and messages for this server model.

###### 4.4.3.2.1. Current Fault state

When the value of a Publish Period state is non-zero, and the FaultArray field of the Current Fault state (see [Section 4.2.16.1](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650 "4.2.16.1. Current Fault")) for any Company ID contains no records, an
unsolicited Health Current Status message with the Company ID field set to one of the Company IDs supported by the Health Fault state and an empty FaultArray field shall be published as defined by the value of the Publish Period state. It is recommended that in this case the Company ID is set to the value of the CID field of
the Composition Data state (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")).

When the value of a Publish Period state is non-zero, and the FaultArray field of the Current Fault state (see [Section 4.2.16.1](index-en.html#UUID-6b40b412-2985-bd45-4f24-7e3d222f1650 "4.2.16.1. Current Fault")) for at least one Company ID contains records, an
unsolicited Health Current Status message set to the value of that Company ID and the FaultArray field containing a sequence of faults representing a sequence of faults in the FaultArray field of the Current Fault state shall be published as defined by the value of the Publish Period divided by the value represented by the
Health Fast Period Divisor state, or every 100 milliseconds (the minimum Publish Period value), whichever is greater.

When there is a state change in the FaultArray field of the Current Fault state, either by removing or adding a record for any Company ID, an unsolicited Health Current Status message shall be published to indicate the change in the Current Fault state.

###### 4.4.3.2.2. Registered Fault state

When an element receives a Health Fault Get message with the Company ID field that successfully identified the Health Fault state, it shall respond with a Health Fault Status message with the Company ID field set to the value as set in the incoming message, the Test ID field set to the identifier (ID) of the most recently
performed test for the identified state, and the FaultArray field containing a sequence of faults representing a sequence of faults in the FaultArray field of the Registered Fault state (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")).

When an element receives a Health Fault Test message with the Company ID field that successfully identified the Health Fault state, it shall perform a test indicated by the Test ID and Company ID fields and respond with a Health Fault Status message with the Company ID field set to the value as set in the incoming message,
the Test ID field set to the ID of the performed test, and the FaultArray field containing a sequence of faults representing a sequence of faults in the FaultArray field of the Registered Fault state (see [Section 4.2.16.2](index-en.html#UUID-b6dae8dc-5d98-5ecc-fe50-7a62d172319d "4.2.16.2. Registered Fault")).

When an element receives a Health Fault Test Unacknowledged message with the Company ID field that successfully identified the Health Fault state, it shall perform a test indicated by the Test ID and Company ID fields.

When an element receives a Health Fault Clear message with the Company ID field that successfully identified the Health Fault state, it shall clear the identified Registered Fault state and respond with a Health Fault Status message with the Company ID field set to the value as set in the incoming message, and an empty
FaultArray field.

When an element receives a Health Fault Clear Unacknowledged message with the Company ID field that successfully identified the Health Fault state, it shall clear the identified Registered Fault state.

When an element receives a Health Fault Get, Health Fault Test, Health Fault Test Unacknowledged, Health Fault Clear, or Health Fault Clear Unacknowledged message that is not successfully processed (i.e., the Company ID field does not identify any Health Fault state present in the node), it shall ignore the message.

###### 4.4.3.2.3. Health Period states

When an element receives a Health Period Get message, it shall respond with a Health Period Status message with the FastPeriodDivisor field set to the current Health Fast Period Divisor state.

When an element receives a Health Period Set message, it shall set the Health Fast Period Divisor state to the value of the FastPeriodDivisor field, and respond with a Health Period Status message with the FastPeriodDivisor field set to the current Health Fast Period Divisor state.

When an element receives a Health Period Set Unacknowledged message, it shall set the Health Fast Period Divisor state to the value of the FastPeriodDivisor field.

###### 4.4.3.2.4. Attention Timer state

When an element receives a Health Attention Get message, it shall respond with a Health Attention Status message with the Attention field set to the current Attention Timer state.

When an element receives a Health Attention Set message, it shall set the Attention Timer state to the value of the Attention field of the message and respond with a Health Attention Status message with the Attention field set to the current Attention Timer state.

When an element receives a Health Attention Set Unacknowledged message, it shall set the Attention Timer state to the value of the Attention field of the message.

An unsolicited Health Attention Status message with the Attention field set to the current Attention Timer state may be sent at any time.

##### 4.4.3.3. Metadata

The Health Server model supports the Health Tests Information metadata [[4](index-en.html#idp254746)].

The format of the Health Tests Information metadata is defined in [Table 4.329](index-en.html#UUID-7f7e6d21-e05c-0499-dd62-f18313660a58_Table_4.329 "Table 4.329. Health Tests Information metadata format").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| Test_Information_Items | variable | List with entries | M |

Table 4.329. Health Tests Information metadata format

The Test_Information_Items field contains a list of entries.

The format of the Test_Information_Items field is defined in [Table 4.330](index-en.html#UUID-7f7e6d21-e05c-0499-dd62-f18313660a58_Table_4.330 "Table 4.330. Test_Information_Items field format").

| Field | Size (octets) | Description |
| --- | --- | --- |
| Test_Information_Item | variable | First entry |
| Test_Information_Item | variable | Second entry |
| … | … | … |
| Test_Information_Item | variable | Last entry |

Table 4.330. Test_Information_Items field format

The format of the Test_Information_Item field is defined in [Table 4.331](index-en.html#UUID-7f7e6d21-e05c-0499-dd62-f18313660a58_Table_4.331 "Table 4.331. Test_Information_Item field format").

| Field | Size (octets) | Description | Req. |
| --- | --- | --- | --- |
| CompanyID | 2 | Company ID | M |
| Number_Of_Tests | 1 | Number of supported Test IDs associated to the Company ID | M |
| TestIDs | variable | List of supported Test IDs associated to the Company ID | M |

Table 4.331. Test_Information_Item field format

The CompanyID field contains the Company ID of the entry in the Health Tests Information metadata.

The Number_Of_Tests field represents the number of supported Test IDs associated with the Company ID.

The TestIDs field contains all supported Test IDs associated with the Company ID.

#### 4.4.4. Health Client model

##### 4.4.4.1. Description

The Health Client model is used to support the fault monitoring and node identification request functionality of a node.

The Health Client model is a root model and a main model that does not extend any other models. The Health Client model may operate on states defined by the Health Server model (see [Section 4.4.3](index-en.html#UUID-90de2c6e-3db3-6f36-1e11-a21ed55c59a1 "4.4.3. Health Server model")) using Health messages (see [Section 4.3.3](index-en.html#UUID-5ba6a0bf-8408-2b80-be9c-2d101338131a "4.3.3. Health messages")).

The Health Client model shall support model publication defined in [Section 4.2.2.5](index-en.html#UUID-9b162037-b7d7-bfca-1468-ca523082be79 "4.2.2.5. Composition Data Page 129") and model subscription defined in [Section 4.2.4](index-en.html#UUID-214e1352-c71e-d76f-b48e-6423c5efa36a "4.2.4. Subscription List"), and requires one element: the Health Main element. The Health Main element contains the Health Client main model.

If supported, the Health Client model shall be supported by a primary element and may be supported by any secondary elements. The access layer security on the Health Client model shall use application keys.

[Table 4.332](index-en.html#UUID-d172e689-5013-2e6c-1db1-b30c76d8e723_Table_4.332 "Table 4.332. Health Client model messages") lists the Health Client model messages. The model shall support receiving the messages marked as mandatory in the Rx column and shall
support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Health Main | Health Client | Current Fault | Current Health Status | M | – |
| Registered Fault | Health Fault Get | – | M |
| Health Fault Clear | – | M |
| Health Fault Clear Unacknowledged | – | M |
| Health Fault Status | M | – |
| Health Fault Test | – | M |
| Health Fault Test Unacknowledged | – | M |
| Health Period | Health Period Get | – | M |
| Health Period Set | – | M |
| Health Period Set Unacknowledged | – | M |
| Health Period Status | M | – |
| Attention Timer | Health Attention Get | – | M |
| Health Attention Set | – | M |
| Health Attention Set Unacknowledged | – | M |
| Health Attention Status | M | – |

Table 4.332. Health Client model messages

##### 4.4.4.2. Behavior

This section describes behaviors for procedures and messages for this client model.

An element can send any Health Client message at any time to query or change a state of a peer element.

###### 4.4.4.2.1. Current Fault procedure

Upon receiving a Health Current Status message, a Health Client can determine the Current Fault state of a Health Server.

###### 4.4.4.2.2. Registered Fault procedure

To determine the Registered Fault state identified by Company ID of a Health Server, a Health Client shall send a Health Fault Get message. The response is a Health Fault Status message that contains the Registered Fault state.

To execute a self-test identified by a Test ID and Company ID for a given element and determine the Registered Fault state identified by Company ID of a Health Server with acknowledgment, a Health Client shall send a Health Fault Test message. The response is a Health Fault Status message that contains the Registered Fault
state identified by Company ID.

To execute a self-test identified by a Test ID and Company ID for a given element without acknowledgment, a Health Client shall send a Health Fault Test Unacknowledged message.

To clear the Registered Fault state identified by Company ID of a Health Server without acknowledgment, a Health Client shall send a Health Fault Clear Unacknowledged message.

To clear the Registered Fault state identified by Company ID of a Health Server with acknowledgment, a Health Client shall send a Health Fault Clear message. The response is a Health Fault Status message that contains the identified Registered Fault state.

Upon receiving a Health Fault Status message, a Health Client can determine the Registered Fault state of a Health Server.

###### 4.4.4.2.3. Health Period procedure

To determine the Health Fast Period Divisor state of a Health Server, a Health Client shall send a Health Period Get message. The response is a Health Period Status message that contains the Health Fast Period Divisor state.

To set the Health Fast Period Divisor state of a Health Server without acknowledgment, a Health Client shall send a Health Period Set Unacknowledged message.

To reliably set the Health Fast Period Divisor state of a Health Server, a Health Client shall send a Health Period Set message. The response is a Health Period Status message that contains the Health Fast Period Divisor state.

Upon receiving a Health Period Status message, a Health Client can determine the Health Fast Period Divisor state of a Health Server.

###### 4.4.4.2.4. Attention Timer procedure

To determine the Attention Timer state of a Health Server, a Health Client shall send a Health Attention Get message. The response is a Health Attention Status message that contains the Attention Timer state.

To set the Attention Timer state of a Health Server with acknowledgment, a Health Client shall send a Health Attention Set message. The response is a Health Attention Status message that contains the Attention Timer state.

To set the Attention Timer state of a Health Server without acknowledgment, a Health Client shall send a Health Attention Set Unacknowledged message.

Upon receiving a Health Attention Status message, a Health Client can determine the current Attention Timer state of a Health Server.

#### 4.4.5. Remote Provisioning Server model

##### 4.4.5.1. Description

The Remote Provisioning Server model is used to support the functionality of provisioning a remote device over the mesh network and to perform the Node Provisioning Protocol Interface procedures.

The Remote Provisioning Server model is a root model and a main model that does not extend any other models.

The Remote Provisioning Server model defines the state instances listed in [Table 4.333](index-en.html#UUID-f2bc3a3e-6fa0-4679-a11f-31936853de38_Table_4.333 "Table 4.333. Remote Provisioning Server states and bindings") and the messages listed in [Table 4.334](index-en.html#UUID-f2bc3a3e-6fa0-4679-a11f-31936853de38_Table_4.334 "Table 4.334. Remote Provisioning Server model messages"), and requires one element: the Remote Provisioning Main element. The Remote Provisioning Main element contains the Remote Provisioning
Server main model.

If supported, the Remote Provisioning Server shall be supported by a primary element and may be supported by any secondary elements. The access layer security on the Remote Provisioning Server model shall use the device key.

[Table 4.333](index-en.html#UUID-f2bc3a3e-6fa0-4679-a11f-31936853de38_Table_4.333 "Table 4.333. Remote Provisioning Server states and bindings") illustrates the state bindings between the Remote Provisioning Server states and the states of the models that the
Remote Provisioning Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Remote Provisioning Scan Capabilities | – | – |
| Remote Provisioning Scan Parameters | – | – |
| Remote Provisioning Link Parameters | – | – |

Table 4.333. Remote Provisioning Server states and bindings

[Table 4.334](index-en.html#UUID-f2bc3a3e-6fa0-4679-a11f-31936853de38_Table_4.334 "Table 4.334. Remote Provisioning Server model messages") lists the Remote Provisioning Server model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Remote Provisioning Main | Remote Provisioning Server | Remote Provisioning Scan Capabilities | Remote Provisioning Scan Capabilities Get | M | – |
| Remote Provisioning Scan Capabilities Status | – | M |
| Remote Provisioning Scan Parameters | Remote Provisioning Scan Get | M | – |
| Remote Provisioning Scan Start | M | – |
| Remote Provisioning Scan Stop | M | – |
| Remote Provisioning Scan Status | – | M |
| Remote Provisioning Scan Report | – | M |
| Remote Provisioning Extended Scan Start | M | – |
| Remote Provisioning Extended Scan Report | – | M |
| Remote Provisioning Link Parameters | Remote Provisioning Link Get | M | – |
| Remote Provisioning Link Open | M | – |
| Remote Provisioning Link Close | M | – |
| Remote Provisioning Link Status | – | M |
| Remote Provisioning Link Report | – | M |
| Remote Provisioning PDU Send | M | – |
| Remote Provisioning PDU Outbound Report | – | M |
| Remote Provisioning PDU Report | – | M |

Table 4.334. Remote Provisioning Server model messages

The Remote Provisioning Server supports two scan procedures: the Remote Provisioning Scan procedure (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")) and the Remote Provisioning Extended Scan
procedure (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")).

The Remote Provisioning Scan procedure and the Remote Provisioning Extended Scan procedure are independent. For example, the Remote Provisioning Client can start the Remote Provisioning Scan procedure, and, while that procedure is being executed, can perform one or more Remote Provisioning Extended Scan procedures. Termination
of the Remote Provisioning Scan procedure does not affect any Remote Provisioning Extended Scan procedures that are in progress.

##### 4.4.5.2. Remote Provisioning Scan procedure

The Remote Provisioning Client may put the Remote Provisioning Server into the Remote Provisioning Multiple Devices Scan state to search for unprovisioned devices within immediate radio range of the Remote Provisioning Server. The Remote Provisioning Client may put the Remote Provisioning Server into the Remote Provisioning
Single Device Scan state to detect if a specific unprovisioned device is present within immediate radio range of the Remote Provisioning Server.

While executing the Remote Provisioning Scan procedure, the Remote Provisioning Server collects the Device UUIDs of unprovisioned devices and passes them to the Remote Provisioning Client via Remote Provisioning Scan Report messages (see [Section 4.4.5.5.1.7](index-en.html#UUID-4c18ccc6-e9d2-06f9-371e-9323910ba2aa "4.4.5.5.1.7. Sending a Remote Provisioning Scan Report message")).

* The Remote Provisioning Server shall only report the devices that it is capable of provisioning. That is, the Remote Provisioning Server shall only send a Remote Provisioning Scan Report message for a device under either of the following circumstances: The server receives an Unprovisioned Device beacon (see [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon")), and it supports provisioning over the PB-ADV provisioning bearer.
* The server receives a connectable advertising packet with the Service Data for the «Mesh Provisioning Service» (see [Section 7.1.2.2.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b "7.1.2.2.1. Advertising")), and it supports provisioning over the
  PB-GATT bearer.

To reduce the probability of a collision when several Remote Provisioning Servers are sending Remote Provisioning Scan Reports to the same Remote Provisioning Client at the same time, the Remote Provisioning Server should introduce a random delay between 20 and 500 milliseconds after receiving an Unprovisioned Device beacon or
a connectable advertising packet with the Service Data for the «Mesh Provisioning Service», and before sending the Remote Provisioning Scan Report.

While the Remote Provisioning Server is in the Remote Provisioning Multiple Devices Scan state or the Remote Provisioning Single Device Scan state, the server shall maintain a list of unprovisioned devices that it reported to the Remote Provisioning Client, which is used to filter out duplicates (discussed later in this
section, under “**Single Device vs. Multiple Devices scanning**”). The list shall be cleared when the Remote Provisioning Scan Start message is received, and it may be cleared when the Remote Provisioning Server stops the scan.

**Starting a scan**. When the Remote Provisioning Server receives a Remote Provisioning Scan Start message with parameters that can be accepted (see [Section 4.4.5.5.1.4](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889 "4.4.5.5.1.4. Receiving a Remote Provisioning Scan Start message")), and the Remote Provisioning Scan state is Idle, the Server shall set Remote Provisioning Scan state either to the Remote Provisioning Multiple Devices Scan value or to the Remote Provisioning Single Device Scan value.

When setting the Remote Provisioning Scan state, the Remote Provisioning Server shall perform the following behaviors:

1. Shall save the source address and the security material (NetKey Index) of the Remote Provisioning Scan Start message, and shall use them when sending Remote Provisioning Scan Report messages. If the saved security material becomes unavailable (for example, if a NetKey is deleted), the Remote Provisioning Server shall set
   the Remote Provisioning Scan state to Idle and stop the scan.
2. Shall set the Remote Provisioning Timeout state to the value of the Timeout field of the Remote Provisioning Scan Start message, and shall start the scanning timer from the initial value indicated by the Remote Provisioning Timeout state.
3. Shall set the Remote Provisioning Scan state to Remote Provisioning Multiple Devices Scan value if the Remote Provisioning Scan Start message does not contain the UUID field, or shall set it to Remote Provisioning Single Device Scan value if the UUID field is present.
4. Shall set the Remote Provisioning Scan Items Limit state to the value of the ScannedItemsLimit field of the Remote Provisioning Scan Start message if the value is not zero, or shall set the Remote Provisioning Scan Item Limit state to the value of the Remote Provisioning Max Scanned Items state if the ScannedItemsLimit
   field value is zero.

**Restarting a scan.** When the Remote Provisioning Server receives a Remote Provisioning Scan Start message with parameters that can be accepted (see [Section 4.4.5.5.1.4](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889 "4.4.5.5.1.4. Receiving a Remote Provisioning Scan Start message")), and the Remote Provisioning Scan state is not Idle, and the source address and the security material match the saved values, then a list of unprovisioned devices that the Remote Provisioning Server reported to the Remote
Provisioning Client shall be cleared, the values of the Remote Provisioning Timeout state, the Remote Provisioning Items Limit state, and the Remote Provisioning Scan state shall be updated according to the values specified in the received Remote Provisioning Scan Start message, and the scanning timer shall be started from the
initial value indicated by the Remote Provisioning Timeout state.

**Single Device vs. Multiple Devices scanning.** If the Remote Provisioning Scan Start message specifies a Remote Provisioning Single Device Scan (the UUID field is present), then the Remote Provisioning Server shall only send information from advertising reports received from the
device associated with the Device UUID that is specified in the message.

If the Remote Provisioning Scan Start message specifies a Remote Provisioning Multiple Devices Scan, then the Remote Provisioning Server shall send information about the first N unprovisioned devices, where N is the value of the Remote Provisioning Scan Items Limit state.

**Successful scan completion.** A Single Device Scan is considered complete when the Remote Provisioning Server sends a Remote Provisioning Scan Report for the device with the UUID specified in the Remote Provisioning Scan Start message.

A Multiple Devices Scan is considered complete when the Remote Provisioning Server sends Remote Provisioning Scan Reports for the value of the Remote Provisioning Scan Items Limit state devices.

**Stopping a scan.** The Remote Provisioning Server shall stop the execution of the Remote Provisioning Scan procedure (i.e., shall stop sending Remote Provisioning Scan Report messages) when it receives a Remote Provisioning Scan Stop message, or when the scanning timer expires, or
when scanning is completed as specified above. If the scanning timer is running when the Remote Provisioning Server stops the Remote Provisioning Scan procedure, the scanning timer shall be stopped, and the Remote Provisioning Timeout state shall be set to zero. When the Remote Provisioning Server stops the Remote Provisioning
Scan procedure, the Remote Provisioning Scan state shall be set to Idle, and the Remote Provisioning Scan Items Limit state shall be set to zero.

##### 4.4.5.3. Remote Provisioning Extended Scan procedure

The Remote Provisioning Client may request additional information about an unprovisioned device that is not available in the Unprovisioned Device beacon or in the advertising packets with the Service Data for the «Mesh Provisioning Service» but may be available in the scan response data or additional advertising reports from
the same device. For example, the client may request a Device Name or a URI for a device.

The Remote Provisioning Server shall support the Remote Provisioning Extended Scan procedure’s collecting information about a single device and may support executing multiple Remote Provisioning Extended Scan procedures in parallel collecting information about multiple devices at the same time.

**Starting a scan.** The Remote Provisioning server starts executing the Remote Provisioning Extended Scan procedure when it receives a Remote Provisioning Extended Scan Start message with the UUID field present, as specified in [Section 4.4.5.5.2.1](index-en.html#UUID-dbcba60c-a6eb-0613-9128-e277ad5943c3 "4.4.5.5.2.1. Receiving a Remote Provisioning Extended Scan Start message").

**Collecting information.** While the Remote Provisioning Server executes the Remote Provisioning Extended Scan procedure, it collects information received in a scan response or in advertising reports from the device associated with the specified UUID. To receive scan responses from the
unprovisioned devices, the Remote Provisioning Server should perform an active scan (see [[2](index-en.html#idp254742)] Vol 6, Part B, Section 4.4.3.2).

The Remote Provisioning Server shall include AD Structures received in the scan response data that match the AD Type in the ADTypeFilter field of the Remote Provisioning Extended Scan Start message.

If the ADTypeFilter field received in the Remote Provisioning Extended Scan Start message contains the URI AD Type, and URI Hash information is available in the Unprovisioned Device beacon (see [Section 3.10.2](index-en.html#UUID-8c1ea7e9-b4b1-51fe-53c3-82fb4a206869 "3.10.2. Unprovisioned Device beacon")), then the Remote Provisioning Server shall include ADStructures with URI data that matches the URI Hash information.

If the ADTypeFilter received in the Remote Provisioning Extended Scan Start message contains the Complete Local Name AD Type, the Remote Provisioning Server shall include AD Structure with either the Complete Local Name or the Shortened Local Name if one is available in the scan response data of the unprovisioned device.

**Scan completion.** The Remote Provisioning Extended Scan procedure is considered complete when one of the following conditions is satisfied:

* The Remote Provisioning Server collects AD structures corresponding to all AD Types specified in the ADTypeFilter field of the Remote Provisioning Extended Scan Start message.
* The timeout specified in the Timeout field of the Remote Provisioning Extended Scan Start message expires.
* The ADTypeFilter field of the Remote Provisioning Extended Scan Start message does not contain the URI AD Type, and the Remote Provisioning Server receives and processes the scan response data from the device with Device UUID requested in the Remote Provisioning Extended Scan Start message.
* The ADTypeFilter field of the Remote Provisioning Extended Scan Start message contains only the URI AD Type, and the Remote Provisioning Server has received an advertising report or scan response with the URI corresponding to the URI Hash of the device with the Device UUID that was requested in the Remote Provisioning
  Extended Scan Start message.
* The ADTypeFilter field of the Remote Provisioning Extended Scan Start message contains only the URI AD Type, and the URI Hash is not available for the device with the Device UUID that was requested in the Remote Provisioning Extended Scan Start message.
* The ADTypeFilter field of the Remote Provisioning Extended Scan Start message contains the URI AD Type and at least one different AD Type in the ADTypeFilter field, and the Remote Provisioning Server has received an advertising report or scan response with the URI corresponding to the URI Hash of the device with the
  Device UUID that was requested in the Remote Provisioning Extended Scan Start message, and the Remote Provisioning Server received the scan response from the same device.
* The ADTypeFilter field of the Remote Provisioning Extended Scan Start message contains the URI AD Type and at least one different AD Type in the ADTypeFilter field, and the URI Hash is not available for the device with the Device UUID that was requested in the Remote Provisioning Extended Scan Start message, and the
  Remote Provisioning Server received the scan response from the same device.

The Remote Provisioning Server shall save the source address and the security material of the Remote Provisioning Extended Scan Start message, and shall use them when sending the Remote Provisioning Extended Scan Report message. When the saved security material is no longer available, the Remote Provisioning Server shall
complete the Remote Provisioning Extended Scanning procedure.

When the Extended Remote Provisioning Scan procedure completes, the Remote Provisioning Server shall send the Remote Provisioning Extended Scan Report message (see [Section 4.4.5.5.2.1](index-en.html#UUID-dbcba60c-a6eb-0613-9128-e277ad5943c3 "4.4.5.5.2.1. Receiving a Remote Provisioning Extended Scan Start message")), which contains obtained data. When the Remote Provisioning Extended Scan procedure completes without receiving an advertisement from the unprovisioned device, the OOBInformation and AdvStructures fields shall be skipped.
When the obtained data is empty, the AdvStructures field shall be skipped. The Status field shall be set to Success.

##### 4.4.5.4. Provisioning procedure

The Provisioning procedure is used for the following purposes:

* To provision a device within immediate radio range of the Remote Provisioning Server.
* To change the Device Key Candidate of the Remote Provisioning Server by using the Device Key Refresh procedure.
* To change the Device Key Candidate and the Composition Data state of the Remote Provisioning Server by using the Node Composition Refresh procedure.
* To change the device key and the primary element address of the Remote Provisioning Server by using the Node Address Refresh procedure.

When entering the Link Opening state, the Remote Provisioning Server shall save the source address and the security material (NetKey Index) of the Remote Provisioning Link Open message, and shall use them when sending the Remote Provisioning Link Report, the Remote Provisioning PDU Outbound Report message, and the Remote
Provisioning PDU Report message.

When the saved security material is no longer available, the Remote Provisioning Server shall do one of the following:

* If a Device Key Refresh procedure, a Node Address Refresh procedure, or a Node Composition Refresh procedure is active, the Remote Provisioning Server shall close the Node Provisioning Protocol Interface and then set the Remote Provisioning Link state to Idle.
* If an unprovisioned device is being provisioned, the Remote Provisioning Server shall start the PB-Remote Close Link procedure and then set the Remote Provisioning Link state to Idle.

When the Remote Provisioning Client sends the first Remote Provisioning PDU Send message after the link is opened, it shall set the OutboundPDUNumber field to 1. When the Remote Provisioning Client sends consecutive Remote Provisioning PDU Send messages with a new Provisioning PDU, it shall set the OutboundPDUNumber field to
the previous value incremented by 1.

To recover from a transmission error, the Remote Provisioning Client may send the Provisioning PDU Send message again with the OutboundPDUNumber and ProvisioningPDU fields set to the same values as in the previously sent Provisioning PDU Send message.

[Figure 4.7](index-en.html#UUID-b23722ef-3b3e-d587-bc02-28fdce7b22e1_Figure_4.7 "Figure 4.7. Remote Provisioning Link state values, message processing, and procedure execution results processing for the Provisioning procedure of the Remote Provisioning Server model") illustrates the provisioning behavior of the Remote Provisioning Server model, showing all relevant states of the
model, messages processed, procedures, and state transitions that occur based on the procedure outcomes.

|  |
| --- |
| Remote Provisioning Link state values, message processing, and procedure execution results processing for the Provisioning procedure of the Remote Provisioning Server model |

Figure 4.7. Remote Provisioning Link state values, message processing, and procedure execution results processing for the Provisioning procedure of the Remote Provisioning Server model

###### 4.4.5.4.1. Example: Provisioning PDU exchange between a Remote Provisioning Client and a Remote Provisioning Server

The message sequence chart in [Figure 4.8](index-en.html#UUID-92221f95-8c17-bb47-f03a-e7dbe49c4a8e_Figure_4.8 "Figure 4.8. Example message sequence for the exchange of Provisioning PDUs") illustrates the beginning of the Provisioning PDU exchange between a
Remote Provisioning Client and a Remote Provisioning Server, which uses PB-ADV to deliver Provisioning PDUs to an unprovisioned device. The figure also illustrates how peers recover communication after a transmission error.

|  |
| --- |
| Example message sequence for the exchange of Provisioning PDUs |

Figure 4.8. Example message sequence for the exchange of Provisioning PDUs

##### 4.4.5.5. Behavior

This section describes behaviors for states and messages for the Remote Provisioning Server model.

When the Node Provisioning Protocol Interface closes as a result of a timeout on the layer executing the provisioning protocol and when the Remote Provisioning Link state is Link Active or Outbound Packet, the behavior specified in [Section 4.4.5.5.3.5](index-en.html#UUID-0b0309a0-e559-b1dc-ce79-a244266c2496 "4.4.5.5.3.5. Sending a Remote Provisioning Link Report message") shall be executed.

###### 4.4.5.5.1. Remote Provisioning Scan behavior

This section describes behaviors of the Remote Provisioning Server model associated with the Remote Provisioning Scan procedure (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")).

###### 4.4.5.5.1.1. Receiving a Remote Provisioning Scan Capabilities Get message

When a Remote Provisioning Server receives a Remote Provisioning Scan Capabilities Get message, the Remote Provisioning Server shall respond with a Remote Provisioning Scan Capabilities Status message (see [Section 4.3.4.2](index-en.html#UUID-8c18f25d-9b9a-db5d-fa73-786f500f0694 "4.3.4.2. Remote Provisioning Scan Capabilities Status")).

###### 4.4.5.5.1.2. Sending a Remote Provisioning Scan Capabilities Status message

A Remote Provisioning Server shall send a Remote Provisioning Scan Capabilities Status message as a response to a Remote Provisioning Scan Capabilities Get message (see [Section 4.3.4.1](index-en.html#UUID-baad19b6-7b74-cf1c-9533-bb0c05368093 "4.3.4.1. Remote Provisioning Scan Capabilities Get")).

When sending a Remote Provisioning Scan Capabilities Status message, the Remote Provisioning Server shall set the message field values as defined in [Table 4.335](index-en.html#UUID-ab26ce8a-a183-c7dd-32f0-4a84b930baa5_Table_4.335 "Table 4.335. Remote Provisioning Scan Capabilities state mapping to fields of the Remote Provisioning Scan Capabilities Status message").

| Message Field | State |
| --- | --- |
| MaxScannedItems | Remote Provisioning Max Scanned Items |
| ActiveScan | Remote Provisioning Active Scan |

Table 4.335. Remote Provisioning Scan Capabilities state mapping to fields of the Remote Provisioning Scan Capabilities Status message

###### 4.4.5.5.1.3. Receiving a Remote Provisioning Scan Get message

When a Remote Provisioning Server receives a Remote Provisioning Scan Get message, the Remote Provisioning Server shall respond with a Remote Provisioning Scan Status message (see [Section 4.4.5.5.1.6](index-en.html#UUID-5090bd71-cdcd-4fda-0415-6b000f990b58 "4.4.5.5.1.6. Sending a Remote Provisioning Scan Status message")) with the Status field set to Success.

###### 4.4.5.5.1.4. Receiving a Remote Provisioning Scan Start message

The Remote Provisioning Client sends a Remote Provisioning Scan Start message to start or restart the Remote Provisioning Scan procedure.

For a Remote Provisioning Scan Start message to be accepted, the values of the message shall meet all conditions defined in [Table 4.336](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889_Table_4.336 "Table 4.336. Remote Provisioning Scan Start message acceptance condition").

| Name | Condition |
| --- | --- |
| Items Limit | The value of the ScannedItemsLimit field shall be less than or equal to the value of the Remote Provisioning Max Scanned Items state. |

Table 4.336. Remote Provisioning Scan Start message acceptance condition

When a Remote Provisioning Server receives a Remote Provisioning Scan Start message with values that cannot be accepted, the server shall respond with a Remote Provisioning Scan Status message with the Status field set to Scanning Cannot Start.

When the Remote Provisioning Server receives a Remote Provisioning Scan Start message with values that can be accepted (see [Table 4.336](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889_Table_4.336 "Table 4.336. Remote Provisioning Scan Start message acceptance condition")), and the Remote Provisioning Scan state is not Idle, then the Remote Provisioning Server shall start the Remote Provisioning Scan Procedure as defined in [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure"), and shall respond with a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")) with the Status field set to Success.

When a Remote Provisioning Server receives a Remote Provisioning Scan Start message that can be accepted (see [Table 4.336](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889_Table_4.336 "Table 4.336. Remote Provisioning Scan Start message acceptance condition")), and the Remote Provisioning Scan state is equal to Remote Provisioning Single Device Scan, and the source address or the security material of the message does not match values saved when the server entered the Remote
Provisioning Single Device Scan state, then the Remote Provisioning Server shall respond with a Remote Provisioning Scan Status message with the Status field set to Invalid State.

When a Remote Provisioning Server receives a Remote Provisioning Scan Start message that can be accepted, and the Remote Provisioning Scan state is equal to Remote Provisioning Multiple Devices Scan, and the source address or the security material of the message does not match values saved when the server entered the
Remote Provisioning Multiple Devices Scan state, then the Remote Provisioning Server shall respond with a Remote Provisioning Scan Status message with the Status field set to Invalid State.

When a Remote Provisioning Server receives a Remote Provisioning Scan Start message that can be accepted (see [Table 4.336](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889_Table_4.336 "Table 4.336. Remote Provisioning Scan Start message acceptance condition")), and the Remote Provisioning Scan state is not Idle, and the source address and the security material of the message match values saved when the server entered either the Remote Provisioning Single Device Scan state or
the Remote Provisioning Multiple Devices Scan state, then the Remote Provisioning Server shall restart the Remote Provisioning Scan procedure as defined in [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure"), and shall respond with a Remote Provisioning Scan Status message with the Status field set to Success.

###### 4.4.5.5.1.5. Receiving a Remote Provisioning Scan Stop message

When a Remote Provisioning Server receives a Remote Provisioning Scan Stop message, it shall respond with a Remote Provisioning Scan Status message (see [Section 4.4.5.5.1.6](index-en.html#UUID-5090bd71-cdcd-4fda-0415-6b000f990b58 "4.4.5.5.1.6. Sending a Remote Provisioning Scan Status message")) with the Status field set to Success. When a Remote Provisioning Server receives a Remote Provisioning Scan Stop message, and the Remote Provisioning Scan state is not Idle, then the Remote Provisioning Server shall stop the
Remote Provisioning Scan procedure as defined in [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure").

###### 4.4.5.5.1.6. Sending a Remote Provisioning Scan Status message

A Remote Provisioning Server shall send the Remote Provisioning Scan Status message in response to a Remote Provisioning Scan Get message, a Remote Provisioning Scan Start message, or a Remote Provisioning Scan Stop message.

The Remote Provisioning Scan Parameters state shall be mapped to the fields of the Remote Provisioning Scan Status message as defined in [Table 4.337](index-en.html#UUID-5090bd71-cdcd-4fda-0415-6b000f990b58_Table_4.337 "Table 4.337. Mapping of Remote Provisioning Scan Parameters state to the fields of a Remote Provisioning Scan Status message").

| Field | State |
| --- | --- |
| RPScanningState | Remote Provisioning Scan |
| ScannedItemsLimit | Remote Provisioning Scan Items Limit |
| Timeout | Remote Provisioning Timeout |

Table 4.337. Mapping of Remote Provisioning Scan Parameters state to the fields of a Remote Provisioning Scan Status message

When a Remote Provisioning Server sends a Remote Provisioning Scan Status message in response to a Remote Provisioning Scan Get message, then the Status field shall be set as defined in [Section 4.4.5.5.1.3](index-en.html#UUID-9f95c9e9-611f-a2d2-61d7-7b518534a043 "4.4.5.5.1.3. Receiving a Remote Provisioning Scan Get message").

When a Remote Provisioning Server sends a Remote Provisioning Scan Status message in response to a Remote Provisioning Scan Start message, then the Remote Provisioning Server shall set the message field values as defined in [Section 4.4.5.5.1.4](index-en.html#UUID-90bea879-84a1-e68d-fab1-63edff224889 "4.4.5.5.1.4. Receiving a Remote Provisioning Scan Start message").

When a Remote Provisioning Server sends a Remote Provisioning Scan Status message in response to a Remote Provisioning Scan Stop message, then the Remote Provisioning Server shall set the message field values as defined in [Section 4.4.5.5.1.5](index-en.html#UUID-1f6fb038-28f3-d52b-3fe1-1d49d8207954 "4.4.5.5.1.5. Receiving a Remote Provisioning Scan Stop message").

###### 4.4.5.5.1.7. Sending a Remote Provisioning Scan Report message

The Remote Provisioning Scan Report message is sent as a result of the execution of the Remote Provisioning Scan procedure as defined in [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure").

The Remote Provisioning Scan Report message shall be tagged with the send-segmented tag. When sending the Remote Provisioning Scan Report message, the Remote Provisioning Server shall set message fields to the following values:

* The UUID field shall be set to the Device UUID value obtained from the unprovisioned device beacon or from the connectable advertising packet with the Service Data for the «Mesh Provisioning Service» (see [Section 7.1.2.2.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b "7.1.2.2.1. Advertising")).
* The OOB field shall be set to the OOB information value.
* The RSSI field shall be set to the measured value (see [Section 4.3.4.7](index-en.html#UUID-89265fa6-9143-b73c-96b0-8b798d8e1f8b "4.3.4.7. Remote Provisioning Scan Report")).
* URI Hash field shall be set to the URI Hash when the URI Hash value is available; otherwise the field shall be excluded.

The URI Hash value is present only in the Unprovisioned Device beacon; the URI Hash is not present in a connectable advertising packet with the Service Data for the «Mesh Provisioning Service» (see [Section 7.1.2.2.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b "7.1.2.2.1. Advertising")).

###### 4.4.5.5.2. Remote Provisioning Extended Scan behavior

This section describes behaviors of the Remote Provisioning Server model associated with the Remote Provisioning Extended Scan procedure (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")).

###### 4.4.5.5.2.1. Receiving a Remote Provisioning Extended Scan Start message

The Remote Provisioning Client sends the Remote Provisioning Extended Scan Start message to start the Remote Provisioning Extended Scan procedure for a device with a specific UUID, or to obtain information about the Remote Provisioning Server itself.

When a Remote Provisioning Server receives a Remote Provisioning Extended Scan Start message that does not contain the UUID field (i.e., the request is to obtain the information about the Remote Provisioning Server), it shall respond with a Remote Provisioning Extended Scan Report message with the Status field set to
Success (see [Section 4.4.5.5.2.2](index-en.html#UUID-0d687f06-4c4b-e615-0380-4f8d1e612634 "4.4.5.5.2.2. Sending a Remote Provisioning Extended Scan Report message")).

When a Remote Provisioning Server receives a Remote Provisioning Extended Scan Start message with the UUID field present (i.e., the request is to execute the Remote Provisioning Extended Scan procedure as described in [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")), and it has sufficient resources to start a new procedure, the server shall start a new Remote Provisioning Extended Scan procedure, and it shall send the Remote Provisioning Extended Scan Report when the procedure completes. A new Remote
Provisioning Extended Scan procedure is started even if another Remote Provisioning Extended Scan procedure with the same parameters is already running.

When a Remote Provisioning Server receives a Remote Provisioning Extended Scan Start message with the UUID field present (i.e., the request is to execute the Remote Provisioning Extended Scan procedure as described in [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")), and it does not have sufficient resources to start a new procedure, the server shall respond with a Remote Provisioning Extended Scan Report message with the Status field set to Limited Resources and the OOBInformation and AdvStructures
fields omitted.

###### 4.4.5.5.2.2. Sending a Remote Provisioning Extended Scan Report message

The Remote Provisioning Extended Scan Report message is sent as a result of execution of the Remote Provisioning Extended Scan procedure (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")), or in response to a Remote Provisioning Extended Scan Start message if the Remote Provisioning Server cannot start the Remote Provisioning Extended Scan procedure, or if the Remote Provisioning Extended Scan Start message requests the
information about the Remote Provisioning Server itself.

The Remote Provisioning Extended Scan Report message shall be tagged with the send-segmented tag.

When the Remote Provisioning Server sends a Remote Provisioning Extended Scan Report message in response to a Remote Provisioning Extended Scan Start message, then the Status field shall be set as defined in [Section 4.4.5.5.2.1](index-en.html#UUID-dbcba60c-a6eb-0613-9128-e277ad5943c3 "4.4.5.5.2.1. Receiving a Remote Provisioning Extended Scan Start message").

When the Remote Provisioning Server sends a Remote Provisioning Extended Scan Report message after executing the Remote Provisioning Extended Scan procedure, then the Status field shall be set as defined in [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure").

When the Remote Provisioning Extended Scan Report message is sent in response to a Remote Provisioning Extended Scan Start message requesting information about the Remote Provisioning Server itself, the Remote Provisioning Server shall construct the ADStructures field based on available local information. The UUID field
shall be set to the Device UUID of the Remote Provisioning Server, and the OOBInformation field shall be set to the OOB Information of the Remote Provisioning Server.

When the Remote Provisioning Server sends a Remote Provisioning Extended Scan Report message as a result of executing the Remote Provisioning Extended Scan procedure, then the UUID field shall match the UUID in the corresponding Remote Provisioning Extended Scan Start message; the OOBInformation field shall be set to the
OOB Information of the unprovisioned device, if available; and the ADStructures field shall contain AD structures obtained during the Remote Provisioning Extended Scan procedure as defined in [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure"), if available.

###### 4.4.5.5.3. Provisioning link management behavior

This section describes link management behaviors for the Remote Provisioning Server model.

###### 4.4.5.5.3.1. Receiving a Remote Provisioning Link Get message

When a Remote Provisioning Server receives a Remote Provisioning Link Get message, the server shall respond with a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")) with the Status field set to Success.

###### 4.4.5.5.3.2. Receiving a Remote Provisioning Link Open message

The response to a Remote Provisioning Link Open message is determined by the Remote Provisioning Link state when the message is received.

**When the Remote Provisioning Link state is Idle:** When a Remote Provisioning Server receives a Remote Provisioning Link Open message, and the Remote Provisioning Link state is Idle, then the Remote Provisioning Server shall set the Remote Provisioning Inbound PDU state to zero
and shall set the Remote Provisioning Outbound PDU Count state to zero.

In addition, the server shall execute one of the following behavior sequences based on the presence or absence of the UUID field in the message:

* If the UUID field is present in the Remote Provisioning Link Open message, the Remote Provisioning Server shall set the Remote Provisioning Link state to Link Opening, shall set the Remote Provisioning Device UUID state to the value of the UUID field, shall respond with a Remote Provisioning Link Status message (see
  [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Success, shall select the PB-GATT or PB-ADV provisioning bearer, and shall start the
  corresponding PB-Remote Open Link procedure using the value of the UUID field as the Device UUID parameter and the value of the Timeout field as Timeout parameter, if present.
* If the NPPI Procedure field is present in the Remote Provisioning Link Open message, the Remote Provisioning Server shall open the Node Provisioning Protocol Interface.

  * If the Node Provisioning Protocol Interface is not opened successfully, the Remote Provisioning Server shall respond with a Remote Provisioning Link Status message with the Status field set to Link Cannot Open.
  * If the Node Provisioning Protocol Interface is opened successfully, the Remote Provisioning Server shall identify the Node Provisioning Protocol Interface procedure as defined in [Table 4.338](index-en.html#UUID-712be6e3-8199-fa48-ea62-7b738ad2c8f7_Table_4.338 "Table 4.338. Mappings between NPPI Procedure field values and Node Provisioning Protocol Interface procedures"), and shall check whether the condition defined in the Additional Condition column is met.
  * If the condition is met, the Remote Provisioning Server shall start the identified Node Provisioning Protocol Interface procedure, shall set the Remote Provisioning Device UUID state to its own Device UUID, shall set the Remote Provisioning Link state to Link Active, shall respond with a Remote Provisioning
    Link Status message (see [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Success, and shall send a Remote Provisioning Link Report
    message (see [Section 4.4.5.5.3.5](index-en.html#UUID-0b0309a0-e559-b1dc-ce79-a244266c2496 "4.4.5.5.3.5. Sending a Remote Provisioning Link Report message")) with the Status field set to Success and without the Reason field.
  * If the condition is not met, the Remote Provisioning Server shall close the Node Provisioning Protocol Interface, and shall respond with a Remote Provisioning Link Status message with the Status field set to Link Cannot Open.

| NPPI Procedure field value | Node Provisioning Protocol Interface procedure | Additional condition |
| --- | --- | --- |
| Device Key Refresh | Device Key Refresh procedure | – |
| Node Address Refresh | Node Address Refresh procedure | – |
| Node Composition Refresh | Node Composition Refresh | Composition Data Page 128 is not equal to Composition Data Page 0. |

Table 4.338. Mappings between NPPI Procedure field values and Node Provisioning Protocol Interface procedures

**When the Remote Provisioning Link state is Link Opening or Link Active:** When a Remote Provisioning Server receives a Remote Provisioning Link Open message, and the Remote Provisioning Link state is either Link Opening or Link Active, the server shall execute one of the following
behavior sequences depending on the conditions defined in [Table 4.339](index-en.html#UUID-712be6e3-8199-fa48-ea62-7b738ad2c8f7_Table_4.339 "Table 4.339. Additional Remote Provisioning Link Open message validation conditions"):

* If all conditions defined in [Table 4.339](index-en.html#UUID-712be6e3-8199-fa48-ea62-7b738ad2c8f7_Table_4.339 "Table 4.339. Additional Remote Provisioning Link Open message validation conditions") are met, the Remote Provisioning Server shall respond
  with a Remote Provisioning Link Status message with the Status field set to Success.
* If one or more conditions defined in [Table 4.339](index-en.html#UUID-712be6e3-8199-fa48-ea62-7b738ad2c8f7_Table_4.339 "Table 4.339. Additional Remote Provisioning Link Open message validation conditions") are not met, the Remote Provisioning Server
  shall respond with a Remote Provisioning Link Status message with the Status field set to Link Cannot Open.

| Condition Name | Condition |
| --- | --- |
| Same Client | Source address of the message is equal to the saved source address of the Remote Provisioning Link Open message. |
| Same NetKey | Network security material of the message is equal to the saved security material from the Remote Provisioning Link Open message. |
| Same UUID | UUID field is present and is equal to the Remote Provisioning Device UUID state; or the UUID field is absent, and the Device UUID of the Remote Provisioning Server is equal to the Remote Provisioning Device UUID state. |
| Same NPPI Procedure | NPPI Procedure field is present and identifies the running Node Provisioning Protocol Interface procedure. Or NPPI Procedure field is absent, and no Node Provisioning Protocol Interface procedure is currently active. |

Table 4.339. Additional Remote Provisioning Link Open message validation conditions

**When the Remote Provisioning Link state is Link Closing or Outbound Packet Transfer:** When a Remote Provisioning Server receives a Remote Provisioning Link Open message, and the Remote Provisioning Link state is either Link Closing or Outbound Packet Transfer, then the Remote
Provisioning Server shall respond with a Remote Provisioning Link Status message with the Status field set to Invalid State.

###### 4.4.5.5.3.3. Receiving a Remote Provisioning Link Close message

The response to a Remote Provisioning Link Close message is determined by the active process (either a procedure or provisioning), if applicable, and the Remote Provisioning Link state when the message is received.

**When the Remote Provisioning Link state is Idle:** When a Remote Provisioning Server receives a Remote Provisioning Link Close message, and the Remote Provisioning Link state is Idle, then the Remote Provisioning Server shall respond with a Remote Provisioning Link Status message
with the Status field set to Success.

**When a Node Provisioning Protocol Interface procedure is active:** When a Remote Provisioning Server receives a Remote Provisioning Link Close message, and a Node Provisioning Protocol Interface procedure is active, and the Remote Provisioning Link state is Link Active, and all
conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions") are met, then the Remote Provisioning Server shall do the following in
sequence:

1. Shall close the Node Provisioning Protocol Interface, passing the Reason Code to the layer executing the provisioning protocol
2. Shall set the Remote Provisioning Link state to Link Closing
3. Shall respond with a Remote Provisioning Link Status message (see [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Success
4. Shall store DevKey/Unicast/Page0 changes
5. Shall set the Remote Provisioning Link state to Idle
6. Shall send a Remote Provisioning Link Report message (see [Section 4.4.5.5.3.5](index-en.html#UUID-0b0309a0-e559-b1dc-ce79-a244266c2496 "4.4.5.5.3.5. Sending a Remote Provisioning Link Report message")) with the Status field set to Link Closed by Client

When a Remote Provisioning Server receives a Remote Provisioning Link Close message, and a Node Provisioning Protocol Interface procedure is active, and the Remote Provisioning Link state is Link Active, and one or more conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions") are not met, then the Remote Provisioning Server shall respond with a Remote Provisioning Link Status message (see [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Invalid State.

| Condition Name | Condition |
| --- | --- |
| Same Client | Source address of the message is equal to the saved source address of the Remote Provisioning Link Close message. |
| Same NetKey | Network security material of the message is equal to the saved security material from the Remote Provisioning Link Close message. |

Table 4.340. Additional Remote Provisioning Link Close message validation conditions

**When an unprovisioned device is being provisioned:** When the Remote Provisioner Server receives a Remote Provisioning Link Close message, and an unprovisioned device is being provisioned, the server’s response shall be determined by the Remote Provisioning Link state:

* If the Remote Provisioning Link state is Link Active, Link Opening, or Outbound Packet Transfer, and one or more conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions") are not met, then the Remote Provisioning Server shall respond with a Remote Provisioning Link Status message (see [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Invalid State.
* If the Remote Provisioning Link state is Link Active and all conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions")
  are met, then the Remote Provisioning Server shall start the PB-Remote Close Link procedure using the value of the Reason field as the Reason, shall set the Link Close Reason state to the Reason field if a reason is required for the PB-Remote Close Link procedure, shall set the Link Close Status state to Link Closed by
  Client, shall set the Remote Provisioning Link state to Link Closing, and shall respond with a Remote Provisioning Link Status message (see [Section 4.4.5.5.3.4](index-en.html#UUID-6b26b86d-28cf-9edf-576c-31207ac296a7 "4.4.5.5.3.4. Sending a Remote Provisioning Link Status message")) with the Status field set to Success.
* If the Remote Provisioning Link state is Link Opening and all conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions")
  are met, then the Remote Provisioning Server shall stop the PB-Remote Open Link procedure, shall start the PB-Remote Close Link procedure using the value of the Reason field as the Reason, shall set the Link Close Reason state to the Reason field if a reason is required for the PB-Remote Close Link procedure, shall set
  the Link Close Status state to Link Closed by Client, shall set the Remote Provisioning Link state to Link Closing, and shall respond with a Remote Provisioning Link Status message with the Status field set to Success.
* If the Remote Provisioning Link state is Outbound Packet Transfer and all conditions defined in [Table 4.340](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62_Table_4.340 "Table 4.340. Additional Remote Provisioning Link Close message validation conditions") are met, then the Remote Provisioning Server shall abort all Provisioning Bearer PDU transfers, shall start the PB-Remote Close Link procedure using the value of the Reason field as the Reason, shall set
  the Link Close Reason state to the Reason field if a reason is required for the PB-Remote Close Link procedure, shall set the Link Close Status state to Link Closed by Client, shall set the Remote Provisioning Link state to Link Closing, and shall respond with a Remote Provisioning Link Status message with the Status
  field set to Success.

**Remote Provisioning Link state is Link Closing:** When a Remote Provisioning Server receives a Remote Provisioning Link Close message, and the Remote Provisioning Link state is Link Closing, then the Remote Provisioning Server shall respond with a Remote Provisioning Link Status
message with the Status field set to Success.

Starting the PB-Remote Close Link procedure initiates additional behavior described in [Section 4.4.5.5.3.5](index-en.html#UUID-0b0309a0-e559-b1dc-ce79-a244266c2496 "4.4.5.5.3.5. Sending a Remote Provisioning Link Report message").

###### 4.4.5.5.3.4. Sending a Remote Provisioning Link Status message

A Remote Provisioning Server shall send a Remote Provisioning Link Status message as a response to a Remote Provisioning Link Open message or a Remote Provisioning Link Close message.

When sending a Remote Provisioning Link Status message in response to a Remote Provisioning Link Open message, the Remote Provisioning Server shall set the RPState field to the current value of the Remote Provisioning Link state and shall set the Status field as defined in [Section 4.4.5.5.3.2](index-en.html#UUID-712be6e3-8199-fa48-ea62-7b738ad2c8f7 "4.4.5.5.3.2. Receiving a Remote Provisioning Link Open message").

When sending a Remote Provisioning Link Status message in response to a Remote Provisioning Link Close message, the Remote Provisioning Server shall set the RPState field to the current value of the Remote Provisioning Link state and shall set the Status field as defined in [Section 4.4.5.5.3.3](index-en.html#UUID-1bf5803a-d00a-21d1-3237-49ac428b7e62 "4.4.5.5.3.3. Receiving a Remote Provisioning Link Close message").

###### 4.4.5.5.3.5. Sending a Remote Provisioning Link Report message

When sending a Remote Provisioning Link Report message, the Remote Provisioning Server shall set the RPState field to the current value of the Remote Provisioning Link state. The Remote Provisioning Link Report message shall be tagged with the send-segmented tag.

**When the Remote Provisioning Link state is Link Opening:** When the Remote Provisioning Link state is Link Opening, and the PB-Remote Open Link procedure succeeds, then the Remote Provisioning Server shall start the PB-Remote Receive PDU procedure, shall set the Remote
Provisioning Link state to Link Active, and shall send a Remote Provisioning Link Report message with the Status field set to Success and without the Reason field. If the PB-Remote Open Link procedure fails, then the Remote Provisioning Server shall set the Remote Provisioning Link state to Idle and shall send a Remote
Provisioning Link Report message with the Status field set to Link Open Failed and without the Reason field.

**When the Remote Provisioning Link state is Link Active or Outbound Packet:** When the Remote Provisioning Link state is either Link Active or Outbound Packet Transfer, and the unprovisioned device closes the Provisioning Bearer link or the local layer executing the provisioning
protocol closes the Node Provisioning Protocol Interface, then the Remote Provisioning Server shall set the Remote Provisioning Link state to Idle, shall abort all Provisioning Bearer PDU transfers, and shall send a Remote Provisioning Link Report message with the Status field set to Link Closed by Device and the Reason field
set to the Reason provided by the Provisioning Bearer if applicable.

When the Remote Provisioning Link state is either Link Active or Outbound Packet Transfer, and the Remote Provisioning Server encounters a condition resulting in the start of the PB-Remote Close Link procedure, then the Remote Provisioning Server shall set the Remote Provisioning Link state to Link Closing, shall start the
PB-Remote Close Link procedure with an appropriate Reason if applicable, shall set the Link Close Reason state to Reason if a reason is required for the PB-Remote Close Link procedure, shall set the Link Close Status to Link Closed by Server, and shall abort all Provisioning Bearer PDU transfers.

**When the Remote Provisioning Link state is Link Closing:** When the Remote Provisioning Link state is Link Closing, and the PB-Remote Close Link procedure completes, then the Remote Provisioning Server shall set the Remote Provisioning Link state to Idle and shall send a Remote
Provisioning Link Report message with the Status field set to the Link Close Status state and the Reason field set to the Link Close Reason state if available.

###### 4.4.5.5.4. Provisioning PDU transfer behavior

This section describes behaviors related to the transfer of Provisioning PDUs for the Remote Provisioning Server model.

###### 4.4.5.5.4.1. Receiving a Remote Provisioning PDU Send message

When a Remote Provisioning Server receives a Remote Provisioning PDU Send message, the server’s response shall be determined by the Remote Provisioning Link state:

* If the Remote Provisioning Link state is Link Active:

  * If the Remote Provisioning Link state is Link Active, and the value of the OutboundPDUNumber field is equal to the Remote Provisioning Outbound PDU Count state incremented by 1, then the Remote Provisioning Server shall set the Remote Provisioning Link state to Outbound Packet Transfer, and shall start the
    PB-Remote Send PDU procedure (see [Section 5.2.3.3.3](index-en.html#UUID-334dd14e-7dfb-ca2b-5321-d4923ebd0d7b "5.2.3.3.3. PB-Remote Send PDU procedure")) using the value of the ProvisioningPDU field as the input parameter. Additionally, if either the
    Device Key Refresh procedure, the Node Address Refresh procedure, or the Node Composition Refresh procedure is active, then the Remote Provisioning Server shall send a Remote Provisioning Outbound PDU Report (see [Section 4.3.4.16](index-en.html#UUID-06bee883-bb71-03ff-de70-86972f8c05c5 "4.3.4.16. Remote Provisioning PDU Outbound Report")) as defined in [Section 4.4.5.5.4.2](index-en.html#UUID-893ff205-e2d4-7e94-3fa6-aa08c07700a2 "4.4.5.5.4.2. Sending a Remote Provisioning PDU Outbound Report message").
  * If the Remote Provisioning Link state is Link Active, and the value of the OutboundPDUNumber field is not equal to the Remote Provisioning Outbound PDU Count state incremented by 1, then the Remote Provisioning Server shall send a Remote Provisioning Outbound PDU Report with the OutboundPDUNumber field set to
    the value of the Remote Provisioning Outbound PDU Count state.
* If the Remote Provisioning Link state is not Link Active, then the Remote Provisioning Server shall ignore the received Remote Provisioning PDU Send message.

###### 4.4.5.5.4.2. Sending a Remote Provisioning PDU Outbound Report message

The Remote Provisioning PDU Outbound Report message is sent to report successful transmission of a Provisioning PDU from the Remote Provisioning Server.

The Remote Provisioning PDU Outbound Report message shall be tagged with the send-segmented tag.

When the Remote Provisioning Link state is Outbound Packet Transfer, and the PB-Remote Send PDU procedure succeeds (see [Section 5.2.3.3.3](index-en.html#UUID-334dd14e-7dfb-ca2b-5321-d4923ebd0d7b "5.2.3.3.3. PB-Remote Send PDU procedure")), then the Remote
Provisioning Server shall increment the value of the Remote Provisioning Outbound PDU Count state by 1, and shall send a Remote Provisioning PDU Outbound Report with the OutboundPDUNumber field set to the value of the Remote Provisioning Outbound PDU Count state and shall set the Remote Provisioning Link state to Link
Active.

When the Remote Provisioning Link state is Outbound Packet Transfer, and the PB-Remote Send PDU procedure fails, then the Remote Provisioning Server shall start the PB-Remote Close Link procedure with an appropriate Reason if applicable, shall set the Link Close Reason state to the Reason if a reason is required for the
PB-Remote Close Link procedure, and shall set the Link Close Status state to Link Closed as Cannot Send PDU.

###### 4.4.5.5.4.3. Sending a Remote Provisioning PDU Report message

The Remote Provisioning PDU Report message shall be tagged with the send-segmented tag.

**When a Node Provisioning Protocol Interface procedure is active:** When the Remote Provisioning Link state is Link Active, and the provisioning protocol generates a Provisioning PDU, then the Remote Provisioning Server shall increment the Remote Provisioning Inbound PDU Count
state value by 1, and shall send a Remote Provisioning PDU Report message with the ProvisioningPDU field set to new Provisioning PDU and the InboundPDUNumber field set to the value of the Remote Provisioning Inbound PDU Count state.

When the delivery of the Remote Provisioning PDU Report message does not complete successfully, then the Remote Provisioning Server shall close the Node Provisioning Protocol Interface; shall set the Remote Provisioning Link state to Idle; and shall send a Remote Provisioning Link Report message (see [Section 4.4.5.5.3.5](index-en.html#UUID-0b0309a0-e559-b1dc-ce79-a244266c2496 "4.4.5.5.3.5. Sending a Remote Provisioning Link Report message")) with the Status field set to Link Closed by Server.

**When an unprovisioned device is being provisioned:** When the Remote Provisioning Link state is either Link Active or Outbound Packet Transfer, and a new inbound Provisioning PDU has been successfully transferred using the PB-Remote Receive PDU procedure (see [Section 5.2.3.3.4](index-en.html#UUID-21ae79f0-829f-0041-087f-9ab1af5df413 "5.2.3.3.4. PB-Remote Receive PDU procedure")), then the Remote Provisioning Server shall increment the Remote Provisioning Inbound PDU Count state value by 1, and shall restart the PB-Remote Receive
PDU procedure, and shall send a Remote Provisioning PDU Report message with the ProvisioningPDU field set to new Provisioning PDU and the InboundPDUNumber field set to the value of the Remote Provisioning Inbound PDU Count state.

To enable expedited recovery after an unexpected link loss between the Provisioner and the Remote Provisioning Server while the remote provisioning is in progress, the Remote Provisioning Server should monitor the status of the Remote Provisioning PDU Report delivery to the Provisioner.

When the delivery of the Remote Provisioning PDU Report does not complete successfully, then the Remote Provisioning Server should perform all of the following actions:

* Start the PB-Remote Close Link procedure with an appropriate Reason code if applicable.
* If a reason is required for the PB-Remote Close Link procedure, set the Link Close Reason state to the Reason.
* Set the Link Close Status state to Link Closed as Cannot Deliver PDU Report.

Because the provisioning protocol allows two consecutive Provisioning PDUs originating from the new device, but the SAR mechanism does not allow more than one transfer of the Upper Transport PDUs between two nodes (see [Section 3.5.3.1](index-en.html#UUID-fcb0ba8f-12ee-ffba-6ea3-0e20948570d9 "3.5.3.1. Segmentation")), the inbound Provisioning PDU should be cached. Because the behavior of the Remote Provisioning Server model cannot guarantee that only one message at a time will be scheduled to be sent to the client, queuing of the messages should be implemented.

#### 4.4.6. Remote Provisioning Client model

##### 4.4.6.1. Description

The Remote Provisioning Client model is used to support the functionality of provisioning devices into a mesh network by interacting with a mesh node that supports the Remote Provisioning Server model.

The Remote Provisioning Client is a root model and a main model that does not extend any other models. The Remote Provisioning Client may operate on states defined by the Remote Provisioning Server model (see [Section 4.4.5](index-en.html#UUID-a5822f3c-d602-d597-e794-15189e9e3c83 "4.4.5. Remote Provisioning Server model")) using Remote Provisioning messages (see [Section 4.3.4](index-en.html#UUID-5cd8b4f9-8a63-d89a-6ba0-f0a251a83d95 "4.3.4. Remote Provisioning messages")), and requires one element: the Remote
Provisioning Main element. The Remote Provisioning Main element contains the Remote Provisioning Client main model.

If supported, the Remote Provisioning Client shall be supported by a primary element and may be supported by any secondary elements. The access layer security on the Remote Provisioning Client model shall use the device key of the node supporting the Remote Provisioning Server model.

[Table 4.341](index-en.html#UUID-af22d589-8f8a-c02b-44bd-30d155f137f7_Table_4.341 "Table 4.341. Remote Provisioning Client model messages") lists the Remote Provisioning Client model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | **Rx** | **Tx** |
| --- | --- | --- | --- | --- | --- |
| Remote Provisioning Main | Remote Provisioning Client | Remote Provisioning Scan Capabilities | Remote Provisioning Scan Capabilities Get | – | M |
| Remote Provisioning Scan Capabilities Status | M | – |
| Remote Provisioning Scan Parameters | Remote Provisioning Scan Get | – | M |
| Remote Provisioning Scan Start | – | M |
| Remote Provisioning Scan Stop | – | M |
| Remote Provisioning Scan Status | M | – |
| Remote Provisioning Scan Report | M | – |
| Remote Provisioning Extended Scan Start | – | M |
| Remote Provisioning Scan Extended Report | M | – |
| Remote Provisioning Link Parameters | Remote Provisioning Link Get | – | M |
| Remote Provisioning Link Open | – | M |
| Remote Provisioning Link Close | – | M |
| Remote Provisioning Link Status | M | – |
| Remote Provisioning Link Report | M | – |
| Remote Provisioning PDU Send | – | M |
| Remote Provisioning PDU Outbound Report | M | – |
| Remote Provisioning PDU Report | M | – |

Table 4.341. Remote Provisioning Client model messages

##### 4.4.6.2. Behavior

This section describes behaviors for procedures and messages for the Remote Provisioning Client model.

An element can send any Remote Provisioning Client message at any time to query or change a state of a peer element. The element may receive some unsolicited Remote Provisioning Server messages, and it shall process them and deliver them to the upper layer.

###### 4.4.6.2.1. Remote Provisioning Scan procedure

This section describes behaviors of the Remote Provisioning Client model associated with the Remote Provisioning Scan procedure (see [Section 4.4.5.2](index-en.html#UUID-9beb4b25-3d46-2f65-e1c2-4a18bbaaf67d "4.4.5.2. Remote Provisioning Scan procedure")).

###### 4.4.6.2.1.1. Sending a Remote Provisioning Scan Capabilities Get message

To determine the Remote Provisioning Scan Capabilities state (see [Section 4.2.23](index-en.html#UUID-eab9589a-c072-7bbc-b38b-62454988e3f9 "4.2.23. Remote Provisioning Scan Capabilities")) of a Remote Provisioning Server, a Remote Provisioning Client shall send a
Remote Provisioning Scan Capabilities Get message. The response is a Remote Provisioning Scan Capabilities Status message (see [Section 4.3.4.2](index-en.html#UUID-8c18f25d-9b9a-db5d-fa73-786f500f0694 "4.3.4.2. Remote Provisioning Scan Capabilities Status")).

###### 4.4.6.2.1.2. Receiving a Remote Provisioning Scan Capabilities Status message

Upon receiving a Remote Provisioning Scan Capabilities Status message, a Remote Provisioning Client can determine the Remote Provisioning Scan Capabilities state (see [Section 4.2.23](index-en.html#UUID-eab9589a-c072-7bbc-b38b-62454988e3f9 "4.2.23. Remote Provisioning Scan Capabilities")) of a Remote Provisioning Server.

###### 4.4.6.2.1.3. Sending a Remote Provisioning Scan Get message

To determine the Remote Provisioning Scan Parameters state (see [Section 4.2.24](index-en.html#UUID-b4bb0ed7-b1fa-9e12-d4ab-1dbdaf34447f "4.2.24. Remote Provisioning Scan Parameters")) of a Remote Provisioning Server, a Remote Provisioning Client shall send a
Remote Provisioning Scan Get message. The response is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

###### 4.4.6.2.1.4. Sending a Remote Provisioning Scan Start message

To start the Remote Provisioning Scan procedure, a Remote Provisioning Client shall send a Remote Provisioning Scan Start message. The response is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

###### 4.4.6.2.1.5. Sending a Remote Provisioning Scan Stop message

To stop the Remote Provisioning Scan procedure, a Remote Provisioning Client shall send a Remote Provisioning Scan Stop message. The response is a Remote Provisioning Scan Status message (see [Section 4.3.4.6](index-en.html#UUID-c7fe6bcc-d4fe-d5f2-948d-bda85e5cafb1 "4.3.4.6. Remote Provisioning Scan Status")).

###### 4.4.6.2.1.6. Receiving a Remote Provisioning Scan Status message

Upon receiving a Remote Provisioning Scan Status message, a Remote Provisioning Client can determine the Remote Provisioning Scan Parameters state (see [Section
4.2.24](index-en.html#UUID-b4bb0ed7-b1fa-9e12-d4ab-1dbdaf34447f "4.2.24. Remote Provisioning Scan Parameters")) of a Remote Provisioning Server.

###### 4.4.6.2.1.7. Receiving a Remote Provisioning Scan Report message

Upon receiving a Remote Provisioning Scan Report message, a Remote Provisioning Client can determine information about an unprovisioned device within immediate radio range of a Remote Provisioning Server.

###### 4.4.6.2.2. Remote Provisioning Extended Scan procedure

This section describes behaviors of the Remote Provisioning Client model associated with the Remote Provisioning Extended Scan procedure (see [Section 4.4.5.3](index-en.html#UUID-3ae43484-6f37-a5f6-6ca8-b86aefe541ed "4.4.5.3. Remote Provisioning Extended Scan procedure")).

###### 4.4.6.2.2.1. Sending a Remote Provisioning Extended Scan Start message

To execute the scan for specific Advertisement Data (see [Section 7.1.2.2.1](index-en.html#UUID-380d983e-28fa-b1cc-567d-98e3a585e89b "7.1.2.2.1. Advertising")) for a specific device, or to receive Advertisement Data from the Remote Provisioning Server itself, a
Remote Provisioning Client shall send a Remote Provisioning Extended Scan Start message. The response is a Remote Provisioning Extended Scan Report message (see [Section 4.3.4.9](index-en.html#UUID-77aac123-f6bc-8246-4821-d8fbd89ef828 "4.3.4.9. Remote Provisioning Extended Scan Report")).

###### 4.4.6.2.2.2. Receiving a Remote Provisioning Extended Scan Report message

Upon receiving a Remote Provisioning Extended Scan Report message, a Remote Provisioning Client can determine OOB Information and AD Structure values received by a Remote Provisioning Server, originating from the identified device, and matching the AD Types specified in the ADTypeFilter field of the Remote Provisioning
Extended Scan Start message.

###### 4.4.6.2.3. Provisioning link management procedures

This section describes behaviors of the Remote Provisioning Client model for managing Remote Provisioning links.

###### 4.4.6.2.3.1. Sending a Remote Provisioning Link Get message

To determine the Remote Provisioning Link state of a Remote Provisioning Server, a Remote Provisioning Client shall send a Remote Provisioning Link Get message. The response is a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

###### 4.4.6.2.3.2. Sending a Remote Provisioning Link Open message

To start the Device Key Refresh procedure, the Node Address Refresh procedure, or the Node Composition Refresh procedure, the Remote Provisioning Client shall send a Remote Provisioning Link Open message with a NPPI Procedure field.

To initiate the opening of a Provisioning Bearer link, the Remote Provisioning Client shall send a Remote Provisioning Link Open message with a UUID field.

The response is a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

###### 4.4.6.2.3.3. Sending a Remote Provisioning Link Close message

To close a Provisioning Bearer link, a Remote Provisioning Client shall send a Remote Provisioning Link Close message. The response is a Remote Provisioning Link Status message (see [Section 4.3.4.13](index-en.html#UUID-f8ff1fe9-05ca-d4ff-2039-7f0e2a7a470b "4.3.4.13. Remote Provisioning Link Status")).

###### 4.4.6.2.3.4. Receiving a Remote Provisioning Link Status message

Upon receiving a Remote Provisioning Link Status message, a Remote Provisioning Client can determine the Remote Provisioning Link state of a Remote Provisioning Server and can determine the result of the associated requesting message, which is indicated in the Status field of the message (see [Table 4.310](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.310 "Table 4.310. Summary of Remote Provisioning Server model status codes")).

###### 4.4.6.2.3.5. Receiving a Remote Provisioning Link Report message

Upon receiving a Remote Provisioning Link Report message, a Remote Provisioning Client can determine the Remote Provisioning Link state of a Remote Provisioning Server and can determine the Link Close Status. When the Reason field is present, the Remote Provisioning Client can determine the reason why the provisioning link
was closed.

###### 4.4.6.2.4. Provisioning PDU transfer procedures

This section describes behaviors of the Remote Provisioning Client model for the transfer of Provisioning PDUs.

###### 4.4.6.2.4.1. Sending a Remote Provisioning PDU Send message

To send a Provisioning PDU, a Remote Provisioning Client shall send a Remote Provisioning PDU Send message (see [Section 4.3.4.15](index-en.html#UUID-c6a224eb-2550-037e-1648-c5538dbc4bcd "4.3.4.15. Remote Provisioning PDU Send")).

###### 4.4.6.2.4.2. Receiving a Remote Provisioning PDU Outbound Report message

Upon receiving a Remote Provisioning PDU Outbound Report message, a Remote Provisioning Client can determine the result of the PB-Remote Send PDU procedure (see [Section 5.2.3.3.3](index-en.html#UUID-334dd14e-7dfb-ca2b-5321-d4923ebd0d7b "5.2.3.3.3. PB-Remote Send PDU procedure")).

###### 4.4.6.2.4.3. Receiving a Remote Provisioning PDU Report message

Upon receiving a Remote Provisioning PDU Report message, a Remote Provisioning Client can receive an output of the PB-Remote Receive PDU procedure (see [Section 5.2.3.3.4](index-en.html#UUID-21ae79f0-829f-0041-087f-9ab1af5df413 "5.2.3.3.4. PB-Remote Receive PDU procedure")).

#### 4.4.7. Directed Forwarding Configuration Server model

##### 4.4.7.1. Description

The Directed Forwarding Configuration Server model is used to support the configuration of the directed forwarding functionality of a node (see [Section 3.6.8](index-en.html#UUID-f079fa7b-73dc-c9a7-aa41-f8ea2afe64cf "3.6.8. Directed forwarding")).

The Directed Forwarding Configuration Server model is a main model that extends the Configuration Server model.

The Directed Forwarding Configuration Server model defines the state instances listed in [Table 4.342](index-en.html#UUID-67b573f6-eeb5-470c-9dc2-c5bb6f0fbba8_Table_4.342 "Table 4.342. Directed Forwarding Configuration Server states and bindings") and the messages
listed in [Table 4.343](index-en.html#UUID-67b573f6-eeb5-470c-9dc2-c5bb6f0fbba8_Table_4.343 "Table 4.343. Directed Forwarding Configuration Server model messages").

If supported, the Directed Forwarding Configuration Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Directed Forwarding Configuration Server model shall use the device key.

[Table 4.342](index-en.html#UUID-67b573f6-eeb5-470c-9dc2-c5bb6f0fbba8_Table_4.342 "Table 4.342. Directed Forwarding Configuration Server states and bindings") illustrates the state bindings between the Directed Forwarding Configuration Server model states and the
states of the models that the Directed Forwarding Configuration Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Directed Control | Configuration Server | GATT Proxy |
| Configuration Server | Friend |
| Path Metric | – | – |
| Discovery Table Capabilities | – | – |
| Forwarding Table | – | – |
| Wanted Lanes | – | – |
| Two Way Path | – | – |
| Path Echo Interval | – | – |
| Directed Network Transmit | – | – |
| Directed Relay Retransmit | – | – |
| RSSI Threshold | – | – |
| Directed Paths | – | – |
| Directed Publish Policy | – | – |
| Path Discovery Timing Control | – | – |
| Directed Control Network Transmit | – | – |
| Directed Control Relay Retransmit | – | – |

Table 4.342. Directed Forwarding Configuration Server states and bindings

[Table 4.343](index-en.html#UUID-67b573f6-eeb5-470c-9dc2-c5bb6f0fbba8_Table_4.343 "Table 4.343. Directed Forwarding Configuration Server model messages") lists the Directed Forwarding Configuration Server model messages. The model shall support receiving the
messages marked as mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Directed Forwarding Main (Primary) | Directed Forwarding Configuration Server | Directed Control  (see [Section 4.2.26](index-en.html#UUID-26bfef24-6d38-7b00-55a7-909e5862e7ad "4.2.26. Directed Control")) | DIRECTED_CONTROL_GET | M | – |
| DIRECTED_CONTROL_SET | M | – |
| DIRECTED_CONTROL_STATUS | – | M |
| Path Metric  (see [Section 4.2.27](index-en.html#UUID-37c55d17-2b41-9a57-03f6-db8046a3c215 "4.2.27. Path Metric")) | PATH_METRIC_GET | M | – |
| PATH_METRIC_SET | M | – |
| PATH_METRIC_STATUS | – | M |
| Discovery Table Capabilities  (see [Section 4.2.28](index-en.html#UUID-cd835a58-3802-7e57-32e1-75431f2da4c8 "4.2.28. Discovery Table Capabilities")) | DISCOVERY_TABLE_CAPABILITIES_GET | M | – |
| DISCOVERY_TABLE_CAPABILITIES_SET | M | – |
| DISCOVERY_TABLE_CAPABILITIES_STATUS | – | M |
| Forwarding Table  (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")) | FORWARDING_TABLE_ADD | M | – |
| FORWARDING_TABLE_DELETE | M | – |
| FORWARDING_TABLE_STATUS | – | M |
| FORWARDING_TABLE_DEPENDENTS_ADD | M | – |
| FORWARDING_TABLE_DEPENDENTS_DELETE | M | – |
| FORWARDING_TABLE_DEPENDENTS_STATUS | – | M |
| FORWARDING_TABLE_ENTRIES_COUNT_GET | M | – |
| FORWARDING_TABLE_ENTRIES_COUNT_STATUS | – | M |
| FORWARDING_TABLE_ENTRIES_GET | M | – |
| FORWARDING_TABLE_ENTRIES_STATUS | – | M |
| FORWARDING_TABLE_DEPENDENTS_GET | M | – |
| FORWARDING_TABLE_DEPENDENTS_GET_STATUS | – | M |
| Wanted Lanes  (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")) | WANTED_LANES_GET | M | – |
| WANTED_LANES_SET | M | – |
| WANTED_LANES_STATUS | – | M |
| Two Way Path  (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")) | TWO_WAY_PATH_GET | M | – |
| TWO_WAY_PATH_SET | M | – |
| TWO_WAY_PATH_STATUS | – | M |
| Path Echo Interval  (see [Section 4.2.32](index-en.html#UUID-f4522b18-a1a0-f41c-96e7-9a56288eb5c0 "4.2.32. Path Echo Interval")) | PATH_ECHO_INTERVAL_GET | M | – |
| PATH_ECHO_INTERVAL_SET | M | – |
| PATH_ECHO_INTERVAL_STATUS | – | M |
| Directed Network Transmit  (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")) | DIRECTED_NETWORK_TRANSMIT_GET | M | – |
| DIRECTED_NETWORK_TRANSMIT_SET | M | – |
| DIRECTED_NETWORK_TRANSMIT_STATUS | – | M |
| Directed Relay Retransmit  (see [Section 4.2.34](index-en.html#UUID-41edd232-dff9-4fe3-1373-2f5a50aa874a "4.2.34. Directed Relay Retransmit")) | DIRECTED_RELAY_RETRANSMIT_GET | M | – |
| DIRECTED_RELAY_RETRANSMIT_SET | M | – |
| DIRECTED_RELAY_RETRANSMIT_STATUS | – | M |
| RSSI Threshold  (see [Section 4.2.35](index-en.html#UUID-f5f8e95b-b448-36cc-7818-a08a46e24834 "4.2.35. RSSI Threshold")) | RSSI_THRESHOLD_GET | M | – |
| RSSI_THRESHOLD_SET | M | – |
| RSSI_THRESHOLD_STATUS | – | M |
| Directed Paths  (see [Section 4.2.36](index-en.html#UUID-f915c359-525a-2c8e-41db-7da6eab4482c "4.2.36. Directed Paths")) | DIRECTED_PATHS_GET | M | – |
| DIRECTED_PATHS_STATUS | – | M |
| Directed Publish Policy (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")) | DIRECTED_PUBLISH_POLICY_GET | M | – |
| DIRECTED_PUBLISH_POLICY_SET | M | – |
| DIRECTED_PUBLISH_POLICY_STATUS | – | M |
| Path Discovery Timing Control (see [Section 4.2.38](index-en.html#UUID-b2b1d81f-e9b3-2803-e46f-5271d0f079c6 "4.2.38. Path Discovery Timing Control")) | PATH_DISCOVERY_TIMING_CONTROL_GET | M | – |
| PATH_DISCOVERY_TIMING_CONTROL_SET | M | – |
| PATH_DISCOVERY_TIMING_CONTROL_STATUS | – | M |
| Directed Control Network Transmit  (see [Section 4.2.39](index-en.html#UUID-bda1ae5c-f4fc-6585-77ea-c54f24acbef8 "4.2.39. Directed Control Network Transmit")) | DIRECTED_CONTROL_NETWORK_TRANSMIT_GET | M | – |
| DIRECTED_CONTROL_NETWORK_TRANSMIT_SET | M | – |
| DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS | – | M |
| Directed Control Relay Retransmit  (see [Section 4.2.40](index-en.html#UUID-efce1e35-df07-15c0-0784-95c584a64d65 "4.2.40. Directed Control Relay Retransmit")) | DIRECTED_CONTROL_RELAY_RETRANSMIT_GET | M | – |
| DIRECTED_CONTROL_RELAY_RETRANSMIT_SET | M | – |
| DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS | – | M |

Table 4.343. Directed Forwarding Configuration Server model messages

##### 4.4.7.2. Path Origin State Machine

When a Directed Forwarding node transmits a message that is tagged with the use-directed tag for a new destination (see [Section 3.7.3.1](index-en.html#UUID-32c1a8f7-5ee7-402c-04e0-35fe2bce7455 "3.7.3.1. Transmitting an Access message")), the Directed Forwarding node
creates an instance of the Path Origin State Machine for that destination. The Path Origin State Machine controls the execution of a Directed Forwarding Initialization procedure for the associated destination following the occurrence of some events that are described in this section.

[Figure 4.9](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc_Figure_4.9 "Figure 4.9. Path Origin State Machine states, events, and transitions") is a diagram of the Path Origin State Machine with its states, events, and transitions.

|  |
| --- |
| Path Origin State Machine states, events, and transitions |

Figure 4.9. Path Origin State Machine states, events, and transitions

[Table 4.344](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc_Table_4.344 "Table 4.344. Path Origin State Machine timers ") defines the timers used by the Path Origin State Machine and the corresponding values that the node shall set the timers to. If
the timer is started from the initial value set to 0, the implementation shall execute the behavior associated with the expiration of the timer. For example, when the Path Monitoring Interval State is 0, setting the Path Monitoring timer results in the creation of the Path Not Needed event.

| Timer Name | Timer Initial Value | Description |
| --- | --- | --- |
| Path Monitoring | Path Monitoring Interval state. | The timer defines the interval during which the use of an established path is monitored. |
| Power Up Monitoring | Value defined in [Section 4.4.7.2.1](index-en.html#UUID-27e362de-afa1-2670-6ebf-12a314b4f439 "4.4.7.2.1. Path Monitoring test mode"). | The timer defines the interval after a node is powered up during which the need for a path is verified. |
| Path Discovery Retry | Path Discovery Retry Interval state | The timer defines the interval after a Directed Forwarding Initialization procedure fails during which the need for a path is verified. |
| Path Use | max(path discovery interval, path lifetime - path discovery interval - Path Monitoring Interval) | The timer defines the interval during which the use of an established path is not monitored.  The value of the timer is the greater of two values: either the path discovery interval (see [Section 4.2.38.3](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf "4.2.38.3. Path Discovery Interval")) or the result of subtracting the path discovery interval and the Path Monitoring Interval (see [Section 4.2.38.1](index-en.html#UUID-f207102b-3e10-0547-65c2-0cdc3afd2c3f "4.2.38.1. Path Monitoring Interval")) from the path lifetime (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")). |

Table 4.344. Path Origin State Machine timers

[Table 4.345](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc_Table_4.345 "Table 4.345. Path Origin State Machine states ") defines the states of the Path Origin State Machine.

| State | Description |
| --- | --- |
| Initial | The initial state of the Path Origin State Machine. |
| Power Up | The state of the Path Origin State Machine at power-up. |
| Path Discovery | The Directed Forwarding Initialization procedure is in progress. |
| Path In Use | The Path Use timer is running. |
| Path Validation | The Directed Forwarding Echo procedure is in progress. |
| Path Monitoring | Either the Path Monitoring timer or the Power Up Monitoring timer is running. |
| Path Discovery Retry Wait | The Path Discovery Retry timer is running. |
| Final | The final state of the Path Origin State Machine. |

Table 4.345. Path Origin State Machine states

[Table 4.346](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc_Table_4.346 "Table 4.346. Path Origin State Machine states") defines the events that determine the transitions of the Path Origin State Machine and the conditions that generate the events.

| Event | Condition |
| --- | --- |
| Path Needed | One of the following conditions is met:  * The Path Origin State Machine is instantiated in the Initial state. * The Path Monitoring timer expired, and the node had transmitted at least one message to the destination while the timer was running. * The Power Up Monitoring timer expired, and the node had transmitted at least one message to the destination while the timer was running. * The Path Discovery Retry timer expired, and the node had transmitted at least one message to the destination while the timer was running. |
| Path Not Needed | One of the following conditions is met:  * The Path Monitoring timer expired, and the node had not transmitted any message to the destination while the timer was running. * The Power Up Monitoring timer expired, and the node had not transmitted any message to the destination while the timer was running. * The Path Discovery Retry timer expired, and the node had not transmitted any message to the destination while the timer was running. |
| Power Up Executed | The Path Origin State Machine is instantiated in the Power Up state. |
| Path Discovery Succeeded | The Directed Forwarding Initialization procedure for the destination completed successfully. |
| Path Discovery Failed | The Directed Forwarding Initialization procedure for the destination failed. |
| Path Validation Started | The Directed Forwarding Echo procedure for the destination started (see [Section 3.6.8.2.6](index-en.html#UUID-0ce483bb-d4af-37a9-694d-12a30e0ddc95 "3.6.8.2.6. Directed Forwarding Echo")). |
| Path Validation Succeeded | The Directed Forwarding Echo procedure for the destination completed successfully. |
| Path Validation Failed | The Directed Forwarding Echo procedure for the destination failed. |
| Path Removed | The non-fixed path entry for the destination is removed from the Forwarding Table while the Path Use timer is running and a new Directed Forwarding Initialization procedure for the destination is not solicited. |
| Path Solicited | The non-fixed path entry for the destination is removed from the Forwarding Table while the Path Use timer is running and a new Directed Forwarding Initialization procedure for the destination is solicited. |
| Path Monitoring Started | The Path Use timer expired. |

Table 4.346. Path Origin State Machine states

[Table 4.347](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc_Table_4.347 "Table 4.347. Path Origin State Machine transitions and actions") defines the transitions of the Path Origin State Machine and the resulting actions that the node shall execute.

| State | Event | New State | Actions |
| --- | --- | --- | --- |
| Initial | Path Needed | Path Discovery | Start the Directed Forwarding Initialization procedure |
| Power Up | Power Up Executed | Path Monitoring | Start the Power Up Monitoring timer |
| Path Discovery | Path Discovery Succeeded | Path In Use | Start the Path Use timer |
| Path Discovery | Path Discovery Failed | Path Discovery Retry Wait | Start the Path Discovery Retry timer |
| Path Discovery Retry Wait | Path Needed | Path Discovery | Start the Directed Forwarding Initialization procedure |
| Path Discovery Retry Wait | Path Not Needed | Final | Stop all timers  **AND**  Destroy the Path Origin State Machine |
| Path In Use | Path Monitoring Started | Path Monitoring | Start the Path Monitoring timer |
| Path In Use | Path Validation Started | Path Validation | – |
| Path In Use | Path Removed | Final | Stop all timers  **AND**  Destroy the Path Origin State Machine |
| Path In Use | Path Solicited | Path Discovery | Stop the Path Use timer  **AND**  Start the Directed Forwarding Initialization procedure |
| Path Monitoring | Path Needed | Path Discovery | Start the Directed Forwarding Initialization procedure |
| Path Monitoring | Path Not Needed | Final | Stop all timers  **AND**  Destroy the Path Origin State Machine |
| Path Validation | Path Validation Succeeded | Path In Use | – |
| Path Validation | Path Validation Failed | Path Discovery | Stop the Path Use timer  **AND**  Start the Directed Forwarding Initialization procedure |

Table 4.347. Path Origin State Machine transitions and actions

###### 4.4.7.2.1. Path Monitoring test mode

To enable efficient testing of the Path Monitoring procedure, a node shall support the Path Monitoring test mode. The activation of the test mode shall be carried out locally (via a hardware or software interface). The Path Monitoring test mode only removes the Path Use timer; all other behavior of the device shall be
unchanged.

One signal is defined in the Path Monitoring test mode:

* Transit to Path Monitoring state signal

When the Transit to Path Monitoring state signal is received, the node shall transition to the Path Monitoring state, ignoring the Path Use timer.

##### 4.4.7.3. Power-down and power-up behavior

When a node is powered down, the Directed Forwarding Configuration Server shall remove the non-fixed path entries in the Forwarding Table state for the subnets that the node belongs to, shall destroy all instances of the Path Origin State Machine, and shall cancel all Directed Forwarding procedures.

When a node is powered up, all states of the Directed Forwarding Configuration Server model shall be restored to the values they had when the node was powered down. In addition, the node shall instantiate a Path Origin State Machine in the Power Up state for each publish address different from the
all-directed-forwarding-nodes, all-nodes, and all-relays fixed group addresses of models with the Directed Publish Policy state equal to Directed Forwarding.

For the Nth instance *(N>0)* of the Path Origin State Machine, the Power Up Monitoring timer for the Path Monitoring state shall be started from the initial value set to a random value in the range *(N-1)×2000* to *(N×2000-1)* in milliseconds. This helps reduce the number of concurrent directed forwarding procedures.

###### 4.4.7.3.1. Example of power-up behavior

The following example illustrates how the Directed Publish Policy state affects power-up behavior in an example configuration.

In the example configuration, a node has four publishing models configured as follows:

* Publishing model A is configured to publish to address X and has the Directed Publish Policy state set to Directed Forwarding.
* Publishing model B is configured to publish to address X and has the Directed Publish Policy state set to Directed Forwarding.
* Publishing model C is configured to publish to address Y and has the Directed Publish Policy state set to Directed Forwarding.
* Publishing model D is configured to publish to address Z and has the Directed Publish Policy state set to Managed Flooding.

On power-up, the node instantiates two Path Origin State Machines, one for publish address X and one for publish address Y:

* The state machine for publish address X has the Power Up Monitoring timer started from an initial value lower than 2 seconds.
* The state machine for publish address Y has the Power Up Monitoring timer started from an initial value greater than or equal to 2 seconds and lower than 4 seconds.

##### 4.4.7.4. Behavior

This section describes behaviors for states and messages for the Directed Forwarding Configuration Server model.

[Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model"), referred to in the following sections, defines the error
conditions for the DIRECTED_CONTROL_GET, DIRECTED_CONTROL_SET, PATH_METRIC_GET, PATH_METRIC_SET, DISCOVERY_TABLE_CAPABILITIES_GET, FORWARDING_TABLE_DELETE, FORWARDING_TABLE_ENTRIES_COUNT_GET, WANTED_LANES_GET, WANTED_LANES_SET, TWO_WAY_PATH_GET, TWO_WAY_PATH_SET, PATH_ECHO_INTERVAL_GET, and PATH_ECHO_INTERVAL_SET messages
processed by the Directed Forwarding Configuration Server model.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |

Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model

###### 4.4.7.4.1. Directed Control state

When an element receives a DIRECTED_CONTROL_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a DIRECTED_CONTROL_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to NetKeyIndex field value in the received message.
* The Directed_Forwarding field shall be set to the current Directed Forwarding state (see [Section 4.2.26.1](index-en.html#UUID-76e0b3d3-4024-6fea-16f8-4698690725d7 "4.2.26.1. Directed Forwarding")) of the subnet identified by the NetKeyIndex field.
* The Directed_Relay field shall be set to the current Directed Relay state (see [Section 4.2.26.2](index-en.html#UUID-539af574-8676-a61c-5e6f-b26f58c259d1 "4.2.26.2. Directed Relay")) of the subnet identified by the NetKeyIndex field.
* The Directed_Proxy field shall be set to the current Directed Proxy state (see [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy")) of the subnet identified by the NetKeyIndex field.
* The Directed_Proxy_Use_Directed_Default field shall be set to the current Directed Proxy Use Directed Default state (see [Section 4.2.26.4](index-en.html#UUID-04cdd8a9-ea09-11c6-bdb9-d01d12540472 "4.2.26.4. Directed Proxy Use Directed Default")) of the subnet
  identified by the NetKeyIndex field.
* The Directed_Friend field shall be set to the current Directed Friend state (see [Section 4.2.26.5](index-en.html#UUID-1a85383c-b86c-df9b-b4cc-889b0865e1fe "4.2.26.5. Directed Friend")) of the subnet identified by the NetKeyIndex field.

When an element receives a DIRECTED_CONTROL_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a DIRECTED_CONTROL_STATUS message with the following configuration:

* The Status field shall be set to a status code defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Directed_Forwarding field shall be set to 0x00.
* The Directed_Relay field shall be set to 0x00.
* The Directed_Proxy field shall be set to 0x00.
* The Directed_Proxy_Use_Directed_Default field shall be set to 0x00.
* The Directed_Friend field shall be set to 0x00.

When an element receives a DIRECTED_CONTROL_SET message that is successfully processed (i.e., it does not result in any error condition listed in Table 4.348), the states of the subnet identified by the NetKeyIndex field in the received message shall be set according to the corresponding fields in the DIRECTED_CONTROL_SET
message, as follows:

* The Directed Forwarding state shall be set to the value of the Directed Forwarding field.
* The Directed Relay state shall be set to the value of the Directed Relay field.
* If the node supports directed proxy functionality, and the value of the Directed_Proxy field is Disable or Enable, then the Directed Proxy state shall be set to the value of the Directed_Proxy field, and the Directed Proxy Use Directed Default state shall be set to the value of the Directed_Proxy_Use_Directed_Default
  field.
* If the node supports directed friend functionality, and the value of the Directed_Friend field is Disable or Enable, then the Directed Friend state shall be set to the value of the Directed_Friend field.

If the new value of the Directed Forwarding state is 0, then the Directed Forwarding Configuration Server shall remove the non-fixed path entries from the Forwarding Table state for the identified subnet (see [Section 4.2.29](index-en.html#UUID-287f030c-daf7-ecff-61f2-10c125f3a3fe "4.2.29. Forwarding Table")), shall destroy all instances of the Path Origin State Machine (see [Section 4.4.7.2](index-en.html#UUID-76be61da-8701-951c-d217-c7544473e1fc "4.4.7.2. Path Origin State Machine")) for the identified subnet, and
shall cancel all Directed Forwarding procedures for the identified subnet.

The element shall also respond to a DIRECTED_CONTROL_SET message that is successfully processed with a DIRECTED_CONTROL_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Directed_Forwarding field shall be set to the current Directed Forwarding state (see [Section 4.2.26.1](index-en.html#UUID-76e0b3d3-4024-6fea-16f8-4698690725d7 "4.2.26.1. Directed Forwarding")) of the subnet identified by the NetKeyIndex field.
* The Directed_Relay field shall be set to the current Directed Relay state (see [Section 4.2.26.2](index-en.html#UUID-539af574-8676-a61c-5e6f-b26f58c259d1 "4.2.26.2. Directed Relay")) of the subnet identified by the NetKeyIndex field.
* The Directed_Proxy field shall be set to the current Directed Proxy state (see [Section 4.2.26.3](index-en.html#UUID-c2d5aef8-5e89-ee26-7d66-64fdb1f82f8a "4.2.26.3. Directed Proxy")) of the subnet identified by the NetKeyIndex field.
* The Directed_Proxy_Use_Directed_Default field shall be set to the current Directed Proxy Use Directed Default state (see [Section 4.2.26.4](index-en.html#UUID-04cdd8a9-ea09-11c6-bdb9-d01d12540472 "4.2.26.4. Directed Proxy Use Directed Default")) of the subnet
  identified by the NetKeyIndex field.
* The Directed_Friend field shall be set to the current Directed Friend state (see [Section 4.2.26.5](index-en.html#UUID-1a85383c-b86c-df9b-b4cc-889b0865e1fe "4.2.26.5. Directed Friend")) of the subnet identified by the NetKeyIndex field.

When an element receives a DIRECTED_CONTROL_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a DIRECTED_CONTROL_STATUS message with the following configuration:

* The Status field shall be set to a status code defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex, Directed_Forwarding, Directed_Relay, Directed_Proxy, Directed_Proxy_Use_Directed_Default, and Directed_Friend fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.2. Path Metric state

When an element receives a PATH_METRIC_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_METRIC_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Path_Metric_Type field shall be set to the current Path Metric Type state (see [Section 4.2.27.1](index-en.html#UUID-1219fa02-97bf-c8c9-848a-9fc17f223db1 "4.2.27.1. Path Metric Type")) of the subnet identified by the NetKeyIndex field.
* The Path_Lifetime field shall be set to the current Path Lifetime state (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")) of the subnet identified by the NetKeyIndex field.

When an element receives a PATH_METRIC_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_METRIC_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Path_Metric_Type field shall be set to 0b000.
* The Path_Lifetime field shall be set to 0b00.

When an element receives a PATH_METRIC_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall set the Path Metric Type state and the Path Lifetime state of the subnet identified by the NetKeyIndex field to the corresponding values of the Path_Metric_Type and
Path_Lifetime fields in the received message. The element shall also respond with a PATH_METRIC_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Path_Metric_Type field shall be set to the current Path Metric Type state (see [Section 4.2.27.1](index-en.html#UUID-1219fa02-97bf-c8c9-848a-9fc17f223db1 "4.2.27.1. Path Metric Type")) of the subnet identified by the NetKeyIndex field.
* The Path_Lifetime field shall be set to the current Path Lifetime state (see [Section 4.2.27.2](index-en.html#UUID-48f2ede3-a56b-0fca-3dc3-92bc009d1e8a "4.2.27.2. Path Lifetime")) of the subnet identified by the NetKeyIndex field.

When an element receives a PATH_METRIC_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_METRIC_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex, Path_Metric_Type, and Path_Lifetime fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.3. Discovery Table Capabilities state

When an element receives a DISCOVERY_TABLE_CAPABILITIES_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a DISCOVERY_TABLE_CAPABILITIES_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Max_Concurrent_Init field shall be set to the current Max Concurrent Init state (see [Section 4.2.28.2](index-en.html#UUID-e37303da-42b9-e0ba-5e52-efc1fc194309 "4.2.28.2. Max Concurrent Init")) of the subnet identified by the NetKeyIndex field.
* The Max_Discovery_Table_Entries_Count field shall be set to the Max Discovery Table Entries Count state (see [Section 4.2.28.1](index-en.html#UUID-b4fb8e0e-c8b5-f1a2-370c-c1acd2133ba3 "4.2.28.1. Max Discovery Table Entries Count")) of the subnet identified by
  the NetKeyIndex field.

When an element receives a DISCOVERY_TABLE_CAPABILITIES_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a DISCOVERY_TABLE_CAPABILITIES_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Max_Concurrent_Init field shall be set to 0x00.
* The Max_Discovery_Table_Entries_Count field shall be set to 0x00.

When an element receives a DISCOVERY_TABLE_CAPABILITIES_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.349](index-en.html#UUID-f89ab638-6a0a-e96d-03c1-7f05acd56afe_Table_4.349 "Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message")), it shall set the Max Concurrent Init state of the subnet identified by the NetKeyIndex field to the value of the Max_Concurrent_Init field in the received message. The element shall also respond with a
DISCOVERY_TABLE_CAPABILITIES_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Max_Concurrent_Init field shall be set to the current Max Concurrent Init state (see [Section 4.2.28.2](index-en.html#UUID-e37303da-42b9-e0ba-5e52-efc1fc194309 "4.2.28.2. Max Concurrent Init")) of the subnet identified by the NetKeyIndex field.
* The Max_Discovery_Table_Entries_Count field shall be set to the Max Discovery Table Entries Count state (see [Section 4.2.28.1](index-en.html#UUID-b4fb8e0e-c8b5-f1a2-370c-c1acd2133ba3 "4.2.28.1. Max Discovery Table Entries Count")) of the subnet identified by
  the NetKeyIndex field.

[Table 4.349](index-en.html#UUID-f89ab638-6a0a-e96d-03c1-7f05acd56afe_Table_4.349 "Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message") defines the error conditions for the DISCOVERY_TABLE_CAPABILITIES_SET message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |
| The value of the Max_Concurrent_Init field is greater than the Max Discovery Table Entries Count state of the subnet. | Cannot Set |

Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message

When an element receives a DISCOVERY_TABLE_CAPABILITIES_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.349](index-en.html#UUID-f89ab638-6a0a-e96d-03c1-7f05acd56afe_Table_4.349 "Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message")), it shall respond with a DISCOVERY_TABLE_CAPABILITIES_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.349](index-en.html#UUID-f89ab638-6a0a-e96d-03c1-7f05acd56afe_Table_4.349 "Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message").
* The NetKeyIndex and Max_Concurrent_Init fields shall be set to the values of the corresponding fields in the received message.
* If the Status field is set to Invalid NetKey Index, then the Max_Discovery_Table_Entries_Count field shall be set to 0x00; otherwise, the Max_Discovery_Table_Entries_Count field shall be set to the Max Discovery Table Entries Count state (see [Section 4.2.28.1](index-en.html#UUID-b4fb8e0e-c8b5-f1a2-370c-c1acd2133ba3 "4.2.28.1. Max Discovery Table Entries Count")) of the subnet identified by the NetKeyIndex field.

###### 4.4.7.4.4. Forwarding Table state

When an element receives a FORWARDING_TABLE_ADD message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.350](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.350 "Table 4.350. Error conditions for FORWARDING_TABLE_ADD message ")), it checks whether a fixed path entry that corresponds to the received message exists in the Forwarding Table state identified by the NetKeyIndex field, according to [Section 4.3.5.2](index-en.html#UUID-28bb2afe-b190-78c5-e92c-fe52dd197e65 "4.3.5.2. Finding a path entry in a Forwarding Table").

If the fixed path entry does not exist in the table, the element shall change the value of the Forwarding Table Update Identifier (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) and
shall add a new fixed path entry to the Forwarding Table with the following settings:

* The Path_Origin and Path_Origin_Secondary_Elements_Count fields in the table entry shall be set, respectively, to the primary element address and to the number of secondary element addresses derived from the Path_Origin_Unicast_Addr_Range field in the message (see [Section 3.4.2.2.4](index-en.html#UUID-fc8aeae7-ad9c-d48a-b94f-ab98ad9662f5 "3.4.2.2.4. Converting to and from the unicast address range format")).
* If the Unicast_Destination_Flag field in the message is 1, the Destination and Path_Target_Secondary_Elements_Count fields in the table entry shall be set, respectively, to the primary element address and to the number of secondary element addresses derived from the Path_Target_Unicast_Addr_Range field in the message.
  If the Unicast_Destination_Flag field in the message is 0, the Destination field in the table entry shall be set to the value of the Multicast_Destination field in the message, and the Path_Target_Secondary_Elements_Count field in the table entry shall be set to 0.
* The Backward_Path_Validated field in the table entry shall be set to the value of the Backward_Path_Validated_Flag field in the message.
* The Bearer_Toward_Path_Origin and Bearer_Toward_Path_Target fields in the table entry shall be set to the corresponding values in the message.
* The Fixed_Path and Lane_Counter fields in the table entry shall be set to 1.
* The Path_Not_Ready field in the table entry shall be set to 0.
* All the other fields in the table entry shall be ignored.

If the fixed path entry exists in the table, the element shall change the value of the Forwarding Table Update Identifier (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) and shall update
the table entry with the following settings:

* The Backward_Path_Validated field in the table entry shall be set to the value of the Backward_Path_Validated_Flag field in the message.
* The Bearer_Toward_Path_Origin and Bearer_Toward_Path_Target fields in the table entry shall be set to the corresponding values in the message.

The element shall also respond with a FORWARDING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Path_Origin field shall be set to the Path_Origin value in the table entry that has been updated.
* The Destination field shall be set to the Destination value in the table entry that has been updated.

[Table 4.350](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.350 "Table 4.350. Error conditions for FORWARDING_TABLE_ADD message ") defines the error conditions for the FORWARDING_TABLE_ADD message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device. | Invalid NetKey Index |
| There is not sufficient memory to add the path entry. | Insufficient Resources |
| The Bearer_Toward_Path_Origin field contains the index of a bearer that is not supported or disabled by the node. | Invalid Bearer |
| The Bearer_Toward_Path_Target field contains the index of a bearer that is not supported or disabled by the node. | Invalid Bearer |
| The value of the Unicast_Destination_Flag field is 0, and the Multicast_Destination field value is one of the group addresses or virtual addresses that the node or any of its dependents are subscribed to, and the Bearer_Toward_Path_Origin field value is the unassigned bearer index. | Invalid Bearer |
| The value of the Unicast_Destination_Flag field is 0, and the addresses derived from the Path_Origin_Unicast_Addr_Range field are not supported by the node, and the Multicast_Destination field value is not one of the group addresses or virtual addresses that the node or any of its dependents are subscribed to, and the value of either the Bearer_Toward_Path_Target field or the Bearer_Toward_Path_Origin field is the unassigned bearer index. | Invalid Bearer |
| At least one of the addresses derived from the Path_Origin_Unicast_Addr_Range field is supported by the node, and either the Bearer_Toward_Path_Target field value is the unassigned bearer index or the Bearer_Toward_Path_Origin field value is not the unassigned bearer index. | Invalid Bearer |
| The value of the Unicast_Destination_Flag field is 1, and at least one of the addresses derived from the Path_Target_Unicast_Addr_Range field is supported by the node, and either the Bearer_Toward_Path_Origin field value is the unassigned bearer index or the Bearer_Toward_Path_Target field value is not the unassigned bearer index. | Invalid Bearer |
| The value of the Unicast_Destination_Flag field is 1, and the addresses derived from the Path_Origin_Unicast_Addr_Range and Path_Target_Unicast_Addr_Range fields are not supported by the node, and the value of either the Bearer_Toward_Path_Target field or the Bearer_Toward_Path_Origin field is the unassigned bearer index. | Invalid Bearer |

Table 4.350. Error conditions for FORWARDING_TABLE_ADD message

When an element receives a FORWARDING_TABLE_ADD message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.350](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.350 "Table 4.350. Error conditions for FORWARDING_TABLE_ADD message ")), it shall respond with a FORWARDING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.350](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.350 "Table 4.350. Error conditions for FORWARDING_TABLE_ADD message ").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Path_Origin field shall be set to the primary element address derived from the Path_Origin_Unicast_Addr_Range field in the received message.
* If the value of the Unicast_Destination field in the received message is 1, the Destination field shall be set to the primary element address derived from the Path_Target_Unicast_Addr_Range field in the received message.
* If the value of the Unicast_Destination field in the received message is 0, the Destination field shall be set to the Multicast_Destination field in the received message.

When an element receives a FORWARDING_TABLE_DELETE message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it checks whether a path entry that corresponds to the received message exists in the Forwarding Table state identified by the NetKeyIndex field, according to [Section 4.3.5.2](index-en.html#UUID-28bb2afe-b190-78c5-e92c-fe52dd197e65 "4.3.5.2. Finding a path entry in a Forwarding Table").

If one or more path entries exist, the element shall delete the entries from the Forwarding Table state and shall change the value of the Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

The element shall also respond with a FORWARDING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.

When an element receives a FORWARDING_TABLE_DELETE message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a FORWARDING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.

When an element receives a FORWARDING_TABLE_DEPENDENTS_ADD message that is successfully processed (i.e., it doesn’t result in any error condition listed in [Table 4.351](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.351 "Table 4.351. Error conditions for FORWARDING_TABLE_DEPENDENTS_ADD message ")), it checks whether a fixed path entry that corresponds to the received message exists in the Forwarding Table state identified by the NetKeyIndex field, according to [Section 4.3.5.2](index-en.html#UUID-28bb2afe-b190-78c5-e92c-fe52dd197e65 "4.3.5.2. Finding a path entry in a Forwarding Table").

If a fixed path entry exists in the table, the entry shall be updated with the following settings:

* For each unicast address range in the Dependent_Origin_Unicast_Addr_Range_List field in the received message, if the primary element address derived from the unicast address range is not included in the Dependent_Origin_List field of the table entry, then the primary element address and the number of secondary element
  addresses derived from the unicast address range shall be added, respectively, to the Dependent_Origin_List and Dependent_Origin_Secondary_Elements_Count fields of the table entry.
* For each unicast address range in the Dependent_Target_Unicast_Addr_Range_List field in the received message, if the primary element address derived from the unicast address range is not included in the Dependent_Target_List field of the table entry, then the primary element address and the number of secondary element
  addresses derived from the unicast address range shall be added, respectively, to the Dependent_Target_List and Dependent_Target_Secondary_Elements_Count fields of the table entry.

If any address is added to the table entry, the element shall change the value of the Forwarding Table Update Identifier (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

The element shall also respond with a FORWARDING_TABLE_DEPENDENTS_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to values of the corresponding fields in the received message.

[Table 4.351](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.351 "Table 4.351. Error conditions for FORWARDING_TABLE_DEPENDENTS_ADD message ") defines the error conditions for the FORWARDING_TABLE_DEPENDENTS_ADD message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device. | Invalid NetKey Index |
| The Path_Origin field contains one of the element addresses of the node, and the Dependent_Origin_Unicast_Addr_Range_List field is present, and the node doesn’t support any of the features or functionality to be a supporting node. | Feature Not Supported |
| The Destination field contains one of the element addresses of the node, and the Dependent_Target_Unicast_Addr_Range_List field is present, and the node doesn’t support any of the features or functionality to be a supporting node. | Feature Not Supported |
| A fixed path entry that corresponds to the message does not exist. | Invalid Path Entry |
| There is not sufficient memory to add new dependents' addresses. | Insufficient Resources |

Table 4.351. Error conditions for FORWARDING_TABLE_DEPENDENTS_ADD message

When an element receives a FORWARDING_TABLE_DEPENDENTS_ADD message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.351](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.351 "Table 4.351. Error conditions for FORWARDING_TABLE_DEPENDENTS_ADD message ")), it shall respond with a FORWARDING_TABLE_DEPENDENTS_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.351](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.351 "Table 4.351. Error conditions for FORWARDING_TABLE_DEPENDENTS_ADD message ").
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.

When an element receives a FORWARDING_TABLE_DEPENDENTS_DELETE message that is successfully processed (i.e., it doesn’t result in any error condition listed in [Table 4.352](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.352 "Table 4.352. Error conditions for FORWARDING_TABLE_DEPENDENTS_DELETE message ")), it checks whether a fixed path entry that corresponds to the received message exists in the Forwarding Table state identified by the NetKeyIndex field, according to [Section 4.3.5.2](index-en.html#UUID-28bb2afe-b190-78c5-e92c-fe52dd197e65 "4.3.5.2. Finding a path entry in a Forwarding Table").

If a fixed path entry exists in the table, the entry shall be updated with the following settings:

* For each unicast address range in the Dependent_Origin_Unicast_Addr_Range_List field in the received message, if the primary element address derived from the unicast address range is included in the Dependent_Origin_List field of the table entry, then the primary element address and the number of secondary element
  addresses derived from the unicast address range shall be removed, respectively, from the Dependent_Origin_List and Dependent_Origin_Secondary_Elements_Count fields of the table entry.
* For each unicast address range in the Dependent_Target_Unicast_Addr_Range_List field in the received message, if the primary element address derived from the unicast address range is included in the Dependent_Target_List field of the table entry, then the primary element address and the number of secondary element
  addresses derived from the unicast address range shall be removed, respectively, from the Dependent_Target_List and Dependent_Target_Secondary_Elements_Count fields of the table entry.

If any address is removed from the table entry, the element shall change the value of the Forwarding Table Update Identifier (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")).

The element shall also respond with a FORWARDING_TABLE_DEPENDENTS_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.

[Table 4.352](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.352 "Table 4.352. Error conditions for FORWARDING_TABLE_DEPENDENTS_DELETE message ") defines the error conditions for the FORWARDING_TABLE_DEPENDENTS_DELETE message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device. | Invalid NetKey Index |
| A fixed path entry that corresponds to the message does not exist. | Invalid Path Entry |

Table 4.352. Error conditions for FORWARDING_TABLE_DEPENDENTS_DELETE message

When an element receives a FORWARDING_TABLE_DEPENDENTS_DELETE message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.352](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.352 "Table 4.352. Error conditions for FORWARDING_TABLE_DEPENDENTS_DELETE message ")), it shall respond with a FORWARDING_TABLE_DEPENDENTS_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.352](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.352 "Table 4.352. Error conditions for FORWARDING_TABLE_DEPENDENTS_DELETE message ").
* The NetKeyIndex, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.

When an element receives a FORWARDING_TABLE_ENTRIES_COUNT_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a FORWARDING_TABLE_ENTRIES_COUNT_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Forwarding_Table_Update_Identifier field shall be set to the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) of the subnet
  identified by the NetKeyIndex field.
* The Fixed_Path_Entries_Count and Non_Fixed_Path_Entries_Count fields shall be set, respectively, to the current number of fixed path entries and non-fixed path entries in the Forwarding Table Entries state (see [Section 4.2.29.2](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee "4.2.29.2. Forwarding Table Entries")) of the subnet identified by the NetKeyIndex field.

When an element receives a FORWARDING_TABLE_ENTRIES_COUNT_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a FORWARDING_TABLE_ENTRIES_COUNT_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.

When an element receives a FORWARDING_TABLE_ENTRIES_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.353](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.353 "Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message ")), it shall respond with a FORWARDING_TABLE_ENTRIES_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex, Filter_Mask, and Start_Index fields shall be set to the values of the corresponding fields in the received message.
* If the Path_Origin_Match bit in the Filter_Mask field is 1, the Path_Origin field shall be set to the Path_Origin field value in the received message.
* If the Destination_Match bit in the Filter_Mask field is 1, the Destination field shall be set to the Destination field value in the received message.
* The Forwarding_Table_Update_Identifier field shall be set to the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) of the subnet
  identified by the NetKeyIndex field.
* The Forwarding_Table_Entry_List field shall contain a filtered list of path entries extracted from the Forwarding Table Entries state (see [Section 4.2.29.2](index-en.html#UUID-ec60273f-4be4-b726-f028-552eece681ee "4.2.29.2. Forwarding Table Entries")) of the
  subnet identified by the NetKeyIndex field. The filtered list includes path entries that meet the filtering conditions in the Filter_Mask field and starts with the filtered path entry indicated by the Start_Index field, considering zero-based indexing (i.e., the first filtered path entry is assigned the index 0). The
  fixed path entries in the Forwarding_Table_Entry_List field shall be formatted as defined in [section 4.3.5.1.2](index-en.html#UUID-ce3de742-3dbf-d825-cb98-0b34c0ddfcb3 "4.3.5.1.2. Fixed path entry format"). The non-fixed path entries in the Forwarding_Table_Entry_List
  field shall be formatted as defined in [section 4.3.5.1.3](index-en.html#UUID-a53a4af1-4ba2-b130-eb6b-0657123ef829 "4.3.5.1.3. Non-fixed path entry format").

[Table 4.353](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.353 "Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message ") defines the error conditions for the FORWARDING_TABLE_ ENTRIES_GET message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device. | Invalid NetKey Index |
| The Forwarding_Table_Update_Identifier field value in the message is not equal to the current Forwarding Table Update Identifier state identified by the NetKeyIndex field. | Obsolete Information |

Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message

When an element receives a FORWARDING_TABLE_ENTRIES_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.353](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.353 "Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message ")), it shall respond with a FORWARDING_TABLE_ENTRIES_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.353](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.353 "Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message ").
* The NetKeyIndex, Filter_Mask, and Start_Index fields shall be set to the values of the corresponding fields in the received message.
* If the Path_Origin_Match bit in the Filter_Mask field is 1, the Path_Origin field shall be set to the Path_Origin field value in the received message.
* If the Destination_Match bit in the Filter_Mask field is 1, the Destination field shall be set to the Destination field value in the received message.
* If the status is Obsolete Information, then the Forwarding_Table_Update_Identifier field shall be set to the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) of the subnet identified by the NetKeyIndex field.

When an element receives a FORWARDING_TABLE_DEPENDENTS_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.354](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.354 "Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message")), it shall respond with a FORWARDING_TABLE_DEPENDENTS_GET_STATUS message.

The FORWARDING_TABLE_DEPENDENTS_GET_STATUS message that is sent in response to a FORWARDING_TABLE_DEPENDENTS_GET message shall have the following configuration. The values shall be set according to the path entry in the Forwarding Table state that is identified by the NetKeyIndex field corresponding to the received message
(according to [Section 4.3.5.2](index-en.html#UUID-28bb2afe-b190-78c5-e92c-fe52dd197e65 "4.3.5.2. Finding a path entry in a Forwarding Table")).

* The Status field shall be set to Success.
* The NetKeyIndex, Dependents_List_Mask, Fixed_Path_Flag, Start_Index, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.
* The Forwarding_Table_Update_Identifier field shall be set to the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) of the subnet
  identified by the NetKeyIndex field.
* If the Dependent_Origin_Unicast_Addr_Range_List field is present, the Dependent_Origin_Unicast_Addr_Range_List_Size field shall be set to the number of unicast address ranges in the Dependent_Origin_Unicast_Addr_Range_List field in the FORWARDING_TABLE_DEPENDENTS_GET_STATUS message; otherwise, the
  Dependent_Origin_Unicast_Addr_Range_List_Size field shall be set to 0.
* If the Dependent_Target_Unicast_Addr_Range_List field is present, the Dependent_Target_Unicast_Addr_Range_List_Size field shall be set to the number of unicast address ranges in the Dependent_Target_Unicast_Addr_Range_List field in the FORWARDING_TABLE_DEPENDENTS_GET_STATUS message; otherwise, the
  Dependent_Target_Unicast_Addr_Range_List_Size field shall be set to 0.
* The Dependent_Origin_Unicast_Addr_Range_List and Dependent_Target_Unicast_Addr_Range_List fields shall be set as follows, based on the Dependents_List_Mask field (see [Table 4.225](index-en.html#UUID-4707950b-f659-f7f7-cf83-1b15e27f9827_Table_4.225 "Table 4.225. Dependents_List_Mask field description")) and the Start_Index field in the received message:

  * If not empty, the Dependent_Origin_Unicast_Addr_Range_List field shall include a list of unicast address ranges derived from the Dependent_Origin_List field and the Dependent_Origin_Secondary_Elements_Count field of the table entry and formatted as defined in [Section 3.4.2.2.2](index-en.html#UUID-c33829d1-321d-7dcb-3cba-3b40f8454d29 "3.4.2.2.2. Unicast address range list").
  * If not empty, the Dependent_Target_Unicast_Addr_Range_List field shall include a list of unicast address ranges derived from the Dependent_Target_List field and the Dependent_Target_Secondary_Elements_Count field of the table entry and formatted as defined in [Section 3.4.2.2.2](index-en.html#UUID-c33829d1-321d-7dcb-3cba-3b40f8454d29 "3.4.2.2.2. Unicast address range list").
  * If bit 0 and bit 1 of the Dependents_List_Mask field are set to 1 and 0 respectively, the following configuration shall be applied:

    * The Dependent_Target_Unicast_Addr_Range_List field shall be empty.
    * If the value of the Start_Index field is less than the number of addresses in the Dependent_Origin_List field, the Dependent_Origin_Unicast_Addr_Range_List field shall start with the unicast address range indicated by the Start_Index field, considering zero-based indexing (i.e., the first unicast address
      range is assigned the index 0).
    * If the value of the Start_Index field is greater than or equal to the number of addresses in the Dependent_Origin_List field, the Dependent_Origin_Unicast_Addr_Range_List field shall be empty.
  * If bit 0 and bit 1 of the Dependents_List_Mask field are set to 0 and 1 respectively, the following configuration shall be applied:

    * The Dependent_Origin_Unicast_Addr_Range_List field shall be empty.
    * If the value of the Start_Index field is less than the number of addresses in the Dependent_Target_List field, the Dependent_Target_Unicast_Addr_Range_List field shall start with the unicast address range indicated by the Start_Index field, considering zero-based indexing (i.e., the first unicast address
      range is assigned the index 0).
    * If the value of the Start_Index field is greater than or equal to the number of addresses in the Dependent_Target_List field, the Dependent_Target_Unicast_Addr_Range_List field shall be empty.
  * If both bit 1 and bit 0 of the Dependents_List_Mask field are set to 1, the value of the Start_Index field indicates the offset in the aggregation of the Dependent_Origin_List field followed by the Dependent_Target_List field (i.e., total number of addresses in the Dependent_Origin_List and Dependent_Target_List
    fields).

    If the value of the Start_Index field is less than the number of addresses in the Dependent_Origin_List field, the Dependent_Origin_Unicast_Addr_Range_List field shall start with the unicast address range indicated by the Start_Index field, considering zero-based indexing (i.e., the first unicast address range is
    assigned the index 0), and the Dependent_Target_Unicast_Addr_Range_List field shall start with the first unicast address range.

    If the value of the Start_Index field is greater than or equal to the number of addresses in the Dependent_Origin_List field, and the value of the Start_Index field is less than the total number of addresses in the Dependent_Origin_List and Dependent_Target_List fields, then the
    Dependent_Origin_Unicast_Addr_Range_List field shall be empty and the Dependent_Target_Unicast_Addr_Range_List field shall start with the unicast address range indicated by the difference between the value of the Start_Index field and the number of addresses in the Dependent_Origin_List field, considering zero-based
    indexing (i.e., the first unicast address range is assigned the index 0).

    If the value of the Start_Index field is greater than or equal to the total number of addresses in the Dependent_Origin_List and Dependent_Target_List fields, both the Dependent_Origin_Unicast_Addr_Range_List and Dependent_Target_Unicast_Addr_Range_List fields shall be empty.

[Table 4.354](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.354 "Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message") defines the error conditions for the FORWARDING_TABLE_ DEPENDENTS_GET message.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device. | Invalid NetKey Index |
| The Forwarding_Table_Update_Identifier field value in the message is not equal to the current Forwarding Table Update Identifier state identified by the NetKeyIndex field. | Obsolete Information |
| A path entry that corresponds to the message does not exist. | Invalid Path Entry |

Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message

When an element receives a FORWARDING_TABLE_DEPENDENTS_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.354](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.354 "Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message")), it shall respond with a FORWARDING_TABLE_DEPENDENTS_GET_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.354](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.354 "Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message").
* The NetKeyIndex, Dependents_List_Mask, Fixed_Path_Flag, Start_Index, Path_Origin, and Destination fields shall be set to the values of the corresponding fields in the received message.
* If the status is Obsolete Information, then the Forwarding_Table_Update_Identifier field shall be set to the current Forwarding Table Update Identifier state (see [Section 4.2.29.1](index-en.html#UUID-3b919ad9-bd1c-d299-efa7-3464cd605908 "4.2.29.1. Forwarding Table Update Identifier")) of the subnet identified by the NetKeyIndex field.

###### 4.4.7.4.5. Wanted Lanes state

When an element receives a WANTED_LANES_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a WANTED_LANES_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Wanted_Lanes field shall be set to the current Wanted Lanes state (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")) of the subnet identified by the NetKeyIndex field.

When an element receives a WANTED_LANES_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a WANTED_LANES_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Wanted_Lanes field shall be set to 0x00.

When an element receives a WANTED_LANES_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall set the Wanted Lanes state of the subnet identified by the NetKeyIndex field to the value of the Wanted_Lanes field in the received message. The element shall also respond
with a WANTED_LANES_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Wanted_Lanes field shall be set to the current Wanted Lanes state (see [Section 4.2.30](index-en.html#UUID-551d5666-1ca8-035c-7485-5defc0c3c715 "4.2.30. Wanted Lanes")) of the subnet identified by the NetKeyIndex field.

When an element receives a WANTED_LANES_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a WANTED_LANES_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex and Wanted_Lanes fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.6. Two Way Path state

When an element receives a TWO_WAY_PATH_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a TWO_WAY_PATH_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Two_Way_Path field shall be set to the current Two Way Path state (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")) of the subnet identified by the NetKeyIndex field.

When an element receives a TWO_WAY_PATH_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a TWO_WAY_PATH_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Two_Way_Path field shall be set to 0b0.

When an element receives a TWO_WAY_PATH_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall set the Two Way Path state of the subnet identified by the NetKeyIndex field to the value of the Two_Way_Path field in the received message. The element shall respond with
a TWO_WAY_PATH_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Two_Way_Path field shall be set to the current Two Way Path state (see [Section 4.2.31](index-en.html#UUID-f33185be-d68a-4d64-8b11-333b6d9a1b88 "4.2.31. Two Way Path")) of the subnet identified by the NetKeyIndex field.

When an element receives a TWO_WAY_PATH_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a TWO_WAY_PATH_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex and Two_Way_Path fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.7. Path Echo Interval state

When an element receives a PATH_ECHO_INTERVAL_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_ECHO_INTERVAL_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Unicast_Echo_Interval field shall be set to the current Unicast Echo Interval state (see [Section 4.2.32.1](index-en.html#UUID-3e7efc9b-b39c-03a4-b396-10d29e418623 "4.2.32.1. Unicast Echo Interval")) of the subnet identified by the NetKeyIndex field.
* The Multicast_Echo_Interval field shall be set to the current Multicast Echo Interval state (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")) of the subnet identified by the NetKeyIndex
  field.

When an element receives a PATH_ECHO_INTERVAL_GET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_ECHO_INTERVAL_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Unicast_Echo_Interval field shall be set to 0x00.
* The Multicast_Echo_Interval field shall be set to 0x00.

When an element receives a PATH_ECHO_INTERVAL_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall modify the Path Echo Interval (see [Section 4.2.32](index-en.html#UUID-f4522b18-a1a0-f41c-96e7-9a56288eb5c0 "4.2.32. Path Echo Interval")) state with the following settings:

* If the Unicast_Echo_Interval field in the received message is not 0xFF (No change in the state), then the element shall set the Unicast Echo Interval state of the subnet identified by the NetKeyIndex field to the value of the Unicast_Echo_Interval field in the received message.
* If the Multicast_Echo_Interval field in the received message is not 0xFF (No change in the state), then the element shall set the Multicast Echo Interval state of the subnet identified by the NetKeyIndex field to the value of the Multicast_Echo_Interval field in the received message.

The element shall also respond with a PATH_ECHO_INTERVAL_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex field shall be set to the NetKeyIndex field value in the received message.
* The Unicast_Echo_Interval field shall be set to the current Unicast Echo Interval state (see [Section 4.2.32.1](index-en.html#UUID-3e7efc9b-b39c-03a4-b396-10d29e418623 "4.2.32.1. Unicast Echo Interval")) of the subnet identified by the NetKeyIndex field.
* The Multicast_Echo_Interval field shall be set to the current Multicast Echo Interval state (see [Section 4.2.32.2](index-en.html#UUID-db86d2b0-e8c0-39b4-50a9-94d31f969d8c "4.2.32.2. Multicast Echo Interval")) of the subnet identified by the NetKeyIndex
  field.

When an element receives a PATH_ECHO_INTERVAL_SET message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")), it shall respond with a PATH_ECHO_INTERVAL_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model").
* The NetKeyIndex, Unicast_Echo_Interval and Multicast_Echo_Interval fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.8. Directed Network Transmit state

When an element receives a DIRECTED_NETWORK_TRANSMIT_GET message, it shall respond with a DIRECTED_NETWORK_TRANSMIT_STATUS message with the following configuration:

* The Directed_Network_Transmit_Count field shall be set to the current Directed Network Transmit Count state (see [Section 4.2.33.1](index-en.html#UUID-156477a1-fee3-c009-ba33-6e0eb7b68be1 "4.2.33.1. Directed Network Transmit Count")).
* The Directed_Network_Transmit_Interval_Steps field shall be set to the current Directed Network Transmit Interval Steps state (see [Section 4.2.33.2](index-en.html#UUID-80851bac-c2eb-58a9-bae3-2732e8859f95 "4.2.33.2. Directed Network Transmit Interval Steps")).

When an element receives a DIRECTED_NETWORK_TRANSMIT_SET message, it shall set the Directed Network Transmit Count state to the value of the Directed_Network_Transmit_Count field in the received message, and shall set the Directed Network Transmit Interval Steps state to the value of the
Directed_Network_Transmit_Interval_Steps field in the received message.

In response to a DIRECTED_NETWORK_TRANSMIT_SET message, the element shall also transmit a DIRECTED_NETWORK_TRANSMIT_STATUS message with the following configuration:

* The Directed_Network_Transmit_Count field shall be set to the current Directed Network Transmit Count state (see [Section 4.2.33.1](index-en.html#UUID-156477a1-fee3-c009-ba33-6e0eb7b68be1 "4.2.33.1. Directed Network Transmit Count")).
* The Directed_Network_Transmit_Interval_Steps field shall be set to the current Directed Network Transmit Interval Steps state (see [Section 4.2.33.2](index-en.html#UUID-80851bac-c2eb-58a9-bae3-2732e8859f95 "4.2.33.2. Directed Network Transmit Interval Steps")).

###### 4.4.7.4.9. Directed Relay Retransmit state

When an element receives a DIRECTED_RELAY_RETRANSMIT_GET message, it shall respond with a DIRECTED_RELAY_RETRANSMIT_STATUS message with the following configuration:

* The Directed_Relay_Retransmit_Count field shall be set to the current Directed Relay Retransmit Count state (see [Section 4.2.34.1](index-en.html#UUID-c2007925-882b-4a14-3e90-b6a1c4a71c9a "4.2.34.1. Directed Relay Retransmit Count")).
* The Directed_Relay_Retransmit_Interval_Steps field shall be set to the current Directed Relay Retransmit Interval Steps state (see [Section 4.2.34.2](index-en.html#UUID-a175dda0-1ac3-18e3-0635-9804394db061 "4.2.34.2. Directed Relay Retransmit Interval Steps")).

When an element receives a DIRECTED_RELAY_RETRANSMIT_SET message, it shall set the Directed Relay Retransmit Count state to the value of the Directed_Relay_Retransmit_Count field in the received message, and shall set the Directed Relay Retransmit Interval Steps state to the value of the
Directed_Relay_Retransmit_Interval_Steps field in the received message.

In response to a DIRECTED_RELAY_RETRANSMIT_SET message, the element shall also transmit a DIRECTED_RELAY_RETRANSMIT_STATUS message with the following configuration:

* The Directed_Relay_Retransmit_Count field shall be set to the current Directed Relay Retransmit Count state (see [Section 4.2.34.1](index-en.html#UUID-c2007925-882b-4a14-3e90-b6a1c4a71c9a "4.2.34.1. Directed Relay Retransmit Count")).
* The Directed_Relay_Retransmit_Interval_Steps field shall be set to the current Directed Relay Retransmit Interval Steps state (see [Section 4.2.34.2](index-en.html#UUID-a175dda0-1ac3-18e3-0635-9804394db061 "4.2.34.2. Directed Relay Retransmit Interval Steps")).

###### 4.4.7.4.10. RSSI Threshold state

When an element receives an RSSI_THRESHOLD_GET message, it shall respond with an RSSI_THRESHOLD_STATUS message with the following configuration:

* The Default_RSSI_Threshold field shall be set to the Default RSSI Threshold state (see [Section 4.2.35.1](index-en.html#UUID-d474c478-bc5e-bbe6-48f5-943397437f43 "4.2.35.1. Default RSSI Threshold")).
* The RSSI_Margin field shall be set to the current RSSI Margin state (see [Section 4.2.35.2](index-en.html#UUID-c30bb5db-a914-901c-6609-c60e528972bd "4.2.35.2. RSSI Margin")).

When an element receives a RSSI_THRESHOLD_SET message, it shall set the RSSI Margin state to the value of the RSSI_Margin field in the received message. The element shall also respond with a RSSI_THRESHOLD_STATUS message with the following configuration:

* The Default_RSSI_Threshold field shall be set to the Default RSSI Threshold state (see [Section 4.2.35.1](index-en.html#UUID-d474c478-bc5e-bbe6-48f5-943397437f43 "4.2.35.1. Default RSSI Threshold")).
* The RSSI_Margin field shall be set to the current RSSI Margin state (see [Section 4.2.35.1](index-en.html#UUID-d474c478-bc5e-bbe6-48f5-943397437f43 "4.2.35.1. Default RSSI Threshold")).

###### 4.4.7.4.11. Directed Paths state

When an element receives a DIRECTED_PATHS_GET message, it shall respond with a DIRECTED_PATHS_STATUS message with the following configuration:

* The Directed_Node_Paths field shall be set to the Directed Node Paths state (see [Section 4.2.36.1](index-en.html#UUID-1dd98673-e5f9-a65d-bcd6-822880da0c63 "4.2.36.1. Directed Node Paths")).
* The Directed_Relay_Paths field shall be set to the Directed Relay Paths state (see [Section 4.2.36.2](index-en.html#UUID-1f8b8740-e3ca-08a0-930d-4a5ea4b02261 "4.2.36.2. Directed Relay Paths")).
* The Directed_Proxy_Paths field shall be set to the Directed Proxy Paths state (see [Section 4.2.36.3](index-en.html#UUID-ff81b630-84f4-f85f-8be1-399f08a6905c "4.2.36.3. Directed Proxy Paths")).
* The Directed_Friend_Paths field shall be set to the Directed Friend Paths state (see [Section 4.2.36.4](index-en.html#UUID-624bd74f-fbcc-44a7-a0c9-a12e6f451ba1 "4.2.36.4. Directed Friend Paths")).

###### 4.4.7.4.12. Directed Publish Policy state

When an element receives a DIRECTED_PUBLISH_POLICY_GET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages")), it shall respond with a DIRECTED_PUBLISH_POLICY_STATUS messages with the following configuration:

* The Status field shall be set to Success.
* The Directed_Publish_Policy field shall be set to the current value of the Directed Publish Policy state of the identified model (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")).
* The Element_Addr and Model_ID fields shall be set to the values of the corresponding fields in the received message.

[Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages") defines the error conditions for the DIRECTED_PUBLISH_POLICY_GET and
DIRECTED_PUBLISH_POLICY_SET messages.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The model defined by the Element_Addr and Model_ID fields does not support the publish mechanism. | Invalid Publish Parameters |
| The unicast address provided in the Element_Addr field is not known to the node. | Invalid Address |
| The model identified by the Model_ID field is not found in the identified element. | Invalid Model |

Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages

When an element receives a DIRECTED_PUBLISH_POLICY_GET message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages")), it shall respond with a DIRECTED_PUBLISH_POLICY_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages").
* The Directed_Publish_Policy field shall be set to 0x00.
* The Element_Addr and Model_ID fields shall be set to the values of the corresponding fields in the received message.

When an element receives a DIRECTED_PUBLISH_POLICY_SET message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages")), it shall set the Directed Publish Policy state of the identified model to the value of the Directed_Publish_Policy field in the received message. The element shall also respond with a
DIRECTED_PUBLISH_POLICY_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The Directed_Publish_Policy field shall be set to the current Directed Publish Policy state of the identified model (see [Section 4.2.37](index-en.html#UUID-72fae7d0-2242-740e-c8c2-4b95f55036ea "4.2.37. Directed Publish Policy")).
* The Element_Addr and Model_ID fields shall be set to the values of the corresponding fields in the received message.

When an element receives a DIRECTED_PUBLISH_POLICY_SET message that is not successfully processed (i.e., it results in an error condition listed in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages")), it shall respond with a DIRECTED_PUBLISH_POLICY_STATUS message with the following configuration:

* The Status field shall be set to the status code corresponding to the error condition as defined in [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages").
* The Directed_Publish_Policy, Element_Addr, and Model_ID fields shall be set to the values of the corresponding fields in the received message.

###### 4.4.7.4.13. Path Discovery Timing Control state

When an element receives a PATH_DISCOVERY_TIMING_CONTROL_GET message, it shall respond with a PATH_DISCOVERY_TIMING_CONTROL_STATUS message with the following configuration:

* The Path_Monitoring_Interval field shall be set to the current Path Monitoring Interval state (see [Section 4.2.38.1](index-en.html#UUID-f207102b-3e10-0547-65c2-0cdc3afd2c3f "4.2.38.1. Path Monitoring Interval")).
* The Path_Discovery_Retry_Interval field shall be set to the current Path Discovery Retry Interval state (see [Section 4.2.38.2](index-en.html#UUID-00b281da-cf97-1f1b-e2cb-9b18ef10da6e "4.2.38.2. Path Discovery Retry Interval")).
* The Path_Discovery_Interval field shall be set to the current Path Discovery Interval state (see [Section 4.2.38.3](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf "4.2.38.3. Path Discovery Interval")).
* The Lane_Discovery_Guard_Interval field shall be set to the current Lane Discovery Guard Interval state (see [Section 4.2.38.4](index-en.html#UUID-11e4dd23-ac53-7cb3-8ee3-d8ae38fda848 "4.2.38.4. Lane Discovery Guard Interval")).

When an element receives a PATH_DISCOVERY_TIMING_CONTROL_SET message, it shall set the Path Monitoring Interval, Path Discovery Retry Interval, Path Discovery Interval, and Lane Discovery Guard Interval states to the corresponding values of the Path_Monitoring_Interval field and Lane_Discovery_Guard_Interval fields in the
received message. The element shall also respond with a PATH_DISCOVERY_TIMING_CONTROL_STATUS message with the following configuration:

* The Path_Monitoring_Interval field shall be set to the current Path Monitoring Interval state (see [Section 4.2.38.1](index-en.html#UUID-f207102b-3e10-0547-65c2-0cdc3afd2c3f "4.2.38.1. Path Monitoring Interval")).
* The Path_Discovery_Retry_Interval field shall be set to the current Path Discovery Retry Interval state (see [Section 4.2.38.2](index-en.html#UUID-00b281da-cf97-1f1b-e2cb-9b18ef10da6e "4.2.38.2. Path Discovery Retry Interval")).
* The Path_Discovery_Interval field shall be set to the current Path Discovery Interval state (see [Section 4.2.38.3](index-en.html#UUID-b4debf63-5bc7-7422-2c45-e1effb56caaf "4.2.38.3. Path Discovery Interval")).
* The Lane_Discovery_Guard_Interval field shall be set to the current Lane Discovery Guard Interval state (see [Section 4.2.38.4](index-en.html#UUID-11e4dd23-ac53-7cb3-8ee3-d8ae38fda848 "4.2.38.4. Lane Discovery Guard Interval")).

###### 4.4.7.4.14. Directed Control Network Transmit state

When an element receives a DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message, it shall respond with a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message with the following configuration:

* The Directed_Control_Network_Transmit_Count field shall be set to the current Directed Control Network Transmit Count state (see [Section 4.2.39.1](index-en.html#UUID-44d73067-2274-ad60-fc6f-7274eea08c63 "4.2.39.1. Directed Control Network Transmit Count")).
* The Directed_Control_Network_Transmit_Interval_Steps field shall be set to the current Directed Control Network Transmit Interval Steps state (see [Section 4.2.39.2](index-en.html#UUID-aaef1564-b0da-1501-24af-257fa188d014 "4.2.39.2. Directed Control Network Transmit Interval Steps")).

When an element receives a DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message, it shall set the Directed Control Network Transmit Count state to the value of the Directed_Control_Network_Transmit_Count field in the received message, and shall set the Directed Control Network Transmit Interval Steps state to the value of the
Directed_Control_Network_Transmit_Interval_Steps field in the received message.

In response to a DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message, the element shall also transmit a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message with the following configuration:

* The Directed_Control_Network_Transmit_Count field shall be set to the current Directed Control Network Transmit Count state (see [Section 4.2.39.1](index-en.html#UUID-44d73067-2274-ad60-fc6f-7274eea08c63 "4.2.39.1. Directed Control Network Transmit Count")).
* The Directed_Control_Network_Transmit_Interval_Steps field shall be set to the current Directed Control Network Transmit Interval Steps state (see [Section 4.2.39.2](index-en.html#UUID-aaef1564-b0da-1501-24af-257fa188d014 "4.2.39.2. Directed Control Network Transmit Interval Steps")).

###### 4.4.7.4.15. Directed Control Relay Retransmit state

When an element receives a DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message, it shall respond with a DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message with the following configuration:

* The Directed_Control_Relay_Retransmit_Count field shall be set to the current Directed Control Relay Retransmit Count state (see [Section 4.2.40.1](index-en.html#UUID-43b4d545-19dd-ad94-5ce4-f2b105f4162f "4.2.40.1. Directed Control Relay Retransmit Count")).
* The Directed_Control_Relay_Retransmit_Interval_Steps field shall be set to the current Directed Control Relay Retransmit Interval Steps state (see [Section 4.2.40.2](index-en.html#UUID-df3188af-6ad4-491d-7c9d-7dc7f322c242 "4.2.40.2. Directed Control Relay Retransmit Interval Steps")).

When an element receives a DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message, it shall set the Directed Control Relay Retransmit Count state to the value of the Directed_Control_Relay_Retransmit_Count field in the received message, and shall set the Directed Control Relay Retransmit Interval Steps state to the value of the
Directed_Control_Relay_Retransmit_Interval_Steps field in the received message.

In response to a DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message, the element shall also transmit a DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message with the following configuration:

* The Directed_Control_Relay_Retransmit_Count field shall be set to the current Directed Control Relay Retransmit Count state (see [Section 4.2.40.1](index-en.html#UUID-43b4d545-19dd-ad94-5ce4-f2b105f4162f "4.2.40.1. Directed Control Relay Retransmit Count")).
* The Directed_Control_Relay_Retransmit_Interval_Steps field shall be set to the current value of the Directed Control Relay Retransmit Interval Steps state (see [Section 4.2.40.2](index-en.html#UUID-df3188af-6ad4-491d-7c9d-7dc7f322c242 "4.2.40.2. Directed Control Relay Retransmit Interval Steps")).

#### 4.4.8. Directed Forwarding Configuration Client model

##### 4.4.8.1. Description

The Directed Forwarding Configuration Client model is used to support the functionality of a node that can configure the directed forwarding functionality of another node.

The Directed Forwarding Configuration Client model is a root model and a main model that does not extend any other models. The Directed Forwarding Configuration Client model may operate on states defined by the Directed Forwarding Configuration Server model (see [Section 4.4.7](index-en.html#UUID-b6798fda-618c-2a98-5558-f53a2a8db930 "4.4.7. Directed Forwarding Configuration Server model")) using Directed Forwarding Configuration messages (see [Section 4.3.5](index-en.html#UUID-b24bbe2e-0bf0-585b-2058-bfbc9e18b0f8 "4.3.5. Directed Forwarding Configuration messages"))

If supported, the Directed Forwarding Configuration Client model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Directed Forwarding Configuration Client model shall use the device key of the node supporting the Directed Forwarding Configuration
Server model.

[Table 4.356](index-en.html#UUID-9436c6eb-3949-191b-332e-a0176707e059_Table_4.356 "Table 4.356. Directed Forwarding Configuration Client model messages") lists the Directed Forwarding Configuration Client model messages. The model shall support receiving the
messages marked as mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Directed   Forwarding   Main (Primary) | Directed   Forwarding   Configuration   Client | Directed Control | DIRECTED_CONTROL_GET | – | M |
| DIRECTED_CONTROL_SET | – | M |
| DIRECTED_CONTROL_STATUS | M | – |
| Path Metric | PATH_METRIC_GET | – | M |
| PATH_METRIC_SET | – | M |
| PATH_METRIC_STATUS | M | – |
| Discovery Table Capabilities | DISCOVERY_TABLE_  CAPABILITIES_GET | – | M |
| DISCOVERY_TABLE_  CAPABILITIES_SET | – | M |
| DISCOVERY_TABLE_  CAPABILITIES_STATUS | M | – |
| Forwarding Table | FORWARDING_TABLE_ADD | – | M |
| FORWARDING_TABLE_DELETE | – | M |
| FORWARDING_TABLE_STATUS | M | – |
| FORWARDING_TABLE_  DEPENDENTS_ADD | – | M |
| FORWARDING_TABLE_  DEPENDENTS_DELETE | – | M |
| FORWARDING_TABLE_  DEPENDENTS_STATUS | M | – |
| FORWARDING_TABLE_  ENTRIES_COUNT_GET | – | M |
| FORWARDING_TABLE_  ENTRIES_COUNT_STATUS | M | – |
| FORWARDING_TABLE_  ENTRIES_GET | – | M |
| FORWARDING_TABLE_  ENTRIES_STATUS | M | – |
| FORWARDING_TABLE_  DEPENDENTS_GET | – | M |
| FORWARDING_TABLE_  DEPENDENTS_GET_STATUS | M | – |
| Wanted Lanes | WANTED_LANES_GET | – | M |
| WANTED_LANES_SET | – | M |
| WANTED_LANES_STATUS | M | – |
| Two Way Path | TWO_WAY_PATH_GET | – | M |
| TWO_WAY_PATH_SET | – | M |
| TWO_WAY_PATH_STATUS | M | – |
| Path Echo   Interval | PATH_ECHO_INTERVAL_GET | – | M |
| PATH_ECHO_INTERVAL_SET | – | M |
| PATH_ECHO_INTERVAL_  STATUS | M | – |
| Directed Network Transmit | DIRECTED_NETWORK_  TRANSMIT_GET | – | M |
| DIRECTED_NETWORK_  TRANSMIT_SET | – | M |
| DIRECTED_NETWORK_  TRANSMIT_STATUS | M | – |
| Directed Relay Retransmit | DIRECTED_RELAY_  RETRANSMIT_GET | – | M |
| DIRECTED_RELAY_  RETRANSMIT_SET | – | M |
| DIRECTED_RELAY_  RETRANSMIT_STATUS | M | – |
| RSSI Threshold | RSSI_THRESHOLD_GET | – | M |
| RSSI_THRESHOLD_SET | – | M |
| RSSI_THRESHOLD_STATUS | M | – |
| Directed Paths | DIRECTED_PATHS_GET | – | M |
| DIRECTED_PATHS_STATUS | M | – |
| Directed Publish Policy | DIRECTED_PUBLISH_  POLICY_GET | – | M |
| DIRECTED_PUBLISH_  POLICY_SET | – | M |
| DIRECTED_PUBLISH_  POLICY_STATUS | M | – |
| Path Discovery Timing Control | PATH_DISCOVERY_TIMING  _CONTROL_GET | – | M |
| PATH_DISCOVERY_TIMING  _CONTROL_SET | – | M |
| PATH_DISCOVERY_TIMING  _CONTROL_STATUS | M | – |
| Directed Control Network Transmit | DIRECTED_CONTROL_  NETWORK_TRANSMIT_GET | – | M |
| DIRECTED_CONTROL_  NETWORK_TRANSMIT_SET | – | M |
| DIRECTED_CONTROL_  NETWORK_TRANSMIT_STATUS | M | – |
| Directed Control Relay Retransmit | DIRECTED_CONTROL_RELAY  _RETRANSMIT_GET | – | M |
| DIRECTED_CONTROL_RELAY  _RETRANSMIT_SET | – | M |
| DIRECTED_CONTROL_RELAY  _RETRANSMIT_STATUS | M | – |

Table 4.356. Directed Forwarding Configuration Client model messages

##### 4.4.8.2. Behavior

This section describes behaviors for procedures and messages for the Directed Forwarding Configuration Client model.

An element can send any Directed Forwarding Configuration Client message at any time to query or change the states supported by the Directed Forwarding Configuration Server model of a peer node.

###### 4.4.8.2.1. Directed Control procedure

To determine the Directed Control state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a DIRECTED_CONTROL_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
DIRECTED_CONTROL_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Directed Control state of the subnet identified by the NetKey Index value.

To set the Directed Control state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a DIRECTED_CONTROL_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
DIRECTED_CONTROL_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Directed Control state of the subnet identified by the NetKey Index value.

Upon receiving a DIRECTED_CONTROL_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Directed Control state of a Directed Forwarding Configuration Server in the
subnet identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.2. Path Metric procedure

To determine the Path Metric state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a PATH_METRIC_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a PATH_METRIC_STATUS message
that contains a status, a NetKey Index value, and may contain the value of the Path Metric state of the subnet identified by the NetKey Index value.

To set the Path Metric state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a PATH_METRIC_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
PATH_METRIC_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Path Metric state of the subnet identified by the NetKey Index value.

Upon receiving a PATH_METRIC_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Path Metric Type and Path Lifetime states of a Directed Forwarding
Configuration Server in the subnet identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.3. Discovery Table Capabilities procedure

To determine the Discovery Table Capabilities state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a DISCOVERY_TABLE_CAPABILITIES_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message
is a DISCOVERY_TABLE_CAPABILITIES_STATUS message that contains a status, a NetKey Index value, and may contain the values of the Max Concurrent Init state and the Max Discovery Table Entries Count state of the subnet identified by the NetKey Index value.

To set the Max Concurrent Init state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a DISCOVERY_TABLE_CAPABILITIES_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the
message is a DISCOVERY_TABLE_CAPABILITIES_STATUS message that contains a status, a NetKey Index value, and may contain the values of the Max Concurrent Init state and the Max Discovery Table Entries Count state of the subnet identified by the NetKey Index value.

Upon receiving a DISCOVERY_TABLE_CAPABILITIES_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.349](index-en.html#UUID-f89ab638-6a0a-e96d-03c1-7f05acd56afe_Table_4.349 "Table 4.349. Error conditions for DISCOVERY_TABLE_CAPABILITIES_SET message")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Max Concurrent Init state and the Max Discovery Table Entries Count state of a Directed Forwarding Configuration
Server in the subnet identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.4. Forwarding Table procedure

The Forwarding Table procedure is used to read or change the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet.

To determine the Forwarding Table Update Identifier state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send one of the following messages: FORWARDING_TABLE_ENTRIES_COUNT_GET, FORWARDING_TABLE_ENTRIES_GET, or FORWARDING_TABLE_DEPENDENTS_GET. Upon receiving
the response to one of these messages, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success or Obsolete Information, the Directed Forwarding Configuration Client can also determine the current Forwarding Table Update Identifier state of the
Directed Forwarding Configuration Server in the subnet. If the status is Obsolete Information, the Directed Forwarding Configuration Client should discard any previously saved Forwarding Table information from the Directed Forwarding Configuration Server for the identified subnet. The Directed Forwarding Configuration Client
should save the value of the Forwarding_Table_Update_Identifier field.

To determine the number of path entries in the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_ENTRIES_COUNT_GET message with the NetKeyIndex field set to the NetKey Index of the subnet. The response to the
message is a FORWARDING_TABLE_ENTRIES_COUNT_STATUS message that may contain the number of fixed path entries and non-fixed path entries present in the Forwarding Table state of a subnet.

Upon receiving the FORWARDING_TABLE_ENTRIES_COUNT_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the number of fixed path entries and non-fixed path entries in the Forwarding Table state
of a subnet. If the status is an error, the Status field contains the error condition.

To determine a filtered set of path entries in the Forwarding Table state of a Directed Forwarding Configuration Server in a subnet, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_ENTRIES_GET message with the following configuration:

* The NetKeyIndex field shall be set to the NetKey Index of the subnet.
* The Filter_Mask field shall be set to the filter to be applied to the path entries in the Forwarding Table state.
* The Start_Index field shall be set to the number of filtered path entries to ignore when reporting the path entries in the response, counting from the first filtered path entry.
* If the Path_Origin_Match bit in the Filter_Mask field is set to 1, the Path_Origin field shall be set to the Path_Origin field value of the path entries to be reported in the response.
* If the Destination_Match bit in the Filter_Mask field is set to 1, the Destination field shall be set to the Destination field value of the path entries to be reported in the response.
* The Forwarding_Table_Update_Identifier field should be set to the most recent value of the Forwarding Table Update Identifier state of the Directed Forwarding Configuration Server, if the value is available.

The response to the FORWARDING_TABLE_ENTRIES_GET message is a FORWARDING_TABLE_ENTRIES_STATUS message that contains a filtered list of path entries in the Forwarding Table.

Upon receiving the FORWARDING_TABLE_ENTRIES_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.353](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.353 "Table 4.353. Error conditions for FORWARDING_TABLE_ENTRIES_GET message ")). If the status is Success, the Directed Forwarding Configuration Client can determine a filtered set of path entries extracted from the Forwarding Table state of a Directed Forwarding Configuration Server for the
subnet identified by the NetKeyIndex field. The path entries are reported in the Forwarding_Table_Entry_List field in the received message. The path entries are filtered as indicated by the Filter_Mask field and start with the filtered path entry following the one indicated by the Start_Index field.

To determine the list of unicast address ranges of dependent nodes of the Path Origin or the Path Target of a path entry in the Forwarding Table state of a Directed Forwarding Configuration Server in a subnet, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_DEPENDENTS_GET message with the following
configuration:

* The NetKeyIndex field shall be set to the NetKey Index of the subnet.
* The Dependents_List_Mask field shall be set to the filter to be applied to the lists of unicast address ranges to be reported in the response message.
* The Fixed_Path_Flag field shall be set to 1 if the lists of unicast address ranges to be reported in the response message are read from a fixed path entry; otherwise, the Fixed_Path_Flag field shall be set to 0.
* The Start_Index field shall be set to the number of filtered unicast address ranges to ignore in the aggregated lists of unicast address ranges indicated by the Dependents_List_Mask field, counting from the first unicast address range.
* The Path_Origin field shall be set to the Path_Origin field value of the path entry.
* The Destination field shall be set to the Destination field value of the path entry.
* The Forwarding_Table_Update_Identifier field should be set to the most recent value of the Forwarding Table Update Identifier state of the Directed Forwarding Configuration Server, if the value is available.

The response to the FORWARDING_TABLE_DEPENDENTS_GET message is a FORWARDING_TABLE_DEPENDENTS_GET_STATUS message that contains filtered lists of unicast address ranges that are included in the Dependent_Origin_List and Dependent_Target_List fields of a path entry in the Forwarding Table.

Upon receiving a FORWARDING_TABLE_DEPENDENTS_GET_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.354](index-en.html#UUID-d4e18a5e-151b-b9e0-52d4-bb57d4ab147f_Table_4.354 "Table 4.354. Error conditions for FORWARDING_TABLE_DEPENDENTS_GET message")). If the status is Success, the Directed Forwarding Configuration Client can determine filtered lists of unicast address ranges of dependent nodes of the Path Origin and the Path Target of a path entry as follows:

* If bit 1 and bit 0 of the Dependents_List_Mask field in the message are set to 0 and 1 respectively, then the Dependent_Origin_Unicast_Addr_Range_List field, if present, includes a list of unicast address ranges of dependent nodes of the Path Origin, starting from the unicast address range indicated by the Start_Index
  field in the message, considering zero-based indexing (i.e., the first unicast address range is assigned the index 0).
* If bit 1 and bit 0 of the Dependents_List_Mask field in the message are set to 1 and 0 respectively, then the Dependent_Target_Unicast_Addr_Range_List field, if present, includes a list of unicast address ranges of dependent nodes of the Path Target, starting from the unicast address range indicated by the Start_Index
  field in the message, considering zero-based indexing (i.e., the first unicast address range is assigned the index 0).
* If both bit 1 and bit 0 of the Dependents_List_Mask field in the message are set to 1, the Dependent_Origin_Unicast_Addr_Range_List field, if present, includes a list of unicast address ranges of dependent nodes of the Path Origin; and the Dependent_Target_Unicast_Addr_Range_List field, if present, includes a list of
  unicast address ranges of dependent nodes of the Path Target. The value of the Start_Index field in the message indicates the offset in the aggregation of the Dependent_Origin_List field followed by the Dependent_Target_List field of the table entry.

To add a fixed path entry or update an existing fixed path entry in the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_ADD message with the NetKeyIndex field set to the NetKey Index of the
NetKey used in the subnet. The response to the message is a FORWARDING_TABLE_STATUS message that contains the value of the NetKeyIndex and indicates whether the fixed path entry was updated.

To add unicast address ranges of dependent nodes of the Path Origin and the Path Target of an existing fixed path entry in the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_DEPENDENTS_ADD
message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a FORWARDING_TABLE_DEPENDENTS_STATUS message that contains the value of the NetKeyIndex and indicates whether the unicast address ranges were added.

To delete unicast address ranges of dependent nodes of the Path Origin and the Path Target of an existing fixed path entry in the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a
FORWARDING_TABLE_DEPENDENTS_DELETE message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a FORWARDING_TABLE_DEPENDENTS_STATUS message that contains the value of the NetKeyIndex and indicates whether the unicast address ranges were deleted.

To delete path entries from the Forwarding Table state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a FORWARDING_TABLE_DELETE message with the following configuration:

* The NetKeyIndex field shall be set to the NetKey Index of the NetKey used in the subnet.
* The Path_Origin field shall be set to the primary element address of the Path Origin of the path entries to be deleted.
* The Destination field shall be set to the destination of the path entries to be deleted.

The response to the message is a FORWARDING_TABLE_STATUS message that contains the value of the NetKeyIndex and indicates whether the path entries were deleted.

###### 4.4.8.2.5. Wanted Lanes procedure

To determine the Wanted Lanes state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a WANTED_LANES_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a WANTED_LANES_STATUS
message that contains a status, a NetKey Index value, and may contain the value of the Wanted Lanes state of the subnet identified by the NetKey Index value.

To set the Wanted Lanes state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a WANTED_LANES_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
WANTED_LANES_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Wanted Lanes state of the subnet identified by the NetKey Index value.

Upon receiving a WANTED_LANES_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Wanted Lanes state of a Directed Forwarding Configuration Server in the subnet
identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.6. Two Way Path procedure

To determine the Two Way Path state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a TWO_WAY_PATH_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a TWO_WAY_PATH_STATUS
message that contains a status, a NetKey Index value, and may contain the value of the Two Way Path state of the subnet identified by the NetKey Index value.

To set the Two Way Path state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a TWO_WAY_PATH_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
TWO_WAY_PATH_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Two Way Path state of the subnet identified by the NetKey Index value.

Upon receiving a TWO_WAY_PATH_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Two Way Path state of a Directed Forwarding Configuration Server in the subnet
identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.7. Path Echo Interval procedure

To determine the Path Echo Interval state of a Directed Forwarding Configuration Server in a given subnet, a Directed Forwarding Configuration Client shall send a PATH_ECHO_INTERVAL_GET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
PATH_ECHO_INTERVAL_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Path Echo Interval state of the subnet identified by the NetKey Index value.

To set the Path Echo Interval state of a Directed Forwarding Configuration Server in a given subnet with acknowledgment, a Directed Forwarding Configuration Client shall send a PATH_ECHO_INTERVAL_SET message with the NetKeyIndex field set to the NetKey Index of the NetKey used in the subnet. The response to the message is a
PATH_ECHO_INTERVAL_STATUS message that contains a status, a NetKey Index value, and may contain the value of the Path Echo Interval state of the subnet identified by the NetKey Index value.

Upon receiving a PATH_ECHO_INTERVAL_STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either Success or an error (see [Table 4.348](index-en.html#UUID-59e7505c-e5d5-a112-7677-f5135f4d7a9d_Table_4.348 "Table 4.348. Common error condition for messages processed by the Directed Forwarding Configuration Server model")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Path Echo Interval state of a Directed Forwarding Configuration Server in the
subnet identified by the NetKeyIndex field in the received message. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.8. Directed Network Transmit procedure

To determine the Directed Network Transmit state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_­NETWORK_­TRANSMIT_­GET message. The response to the message is a DIRECTED_­NETWORK_­TRANSMIT_­STATUS message that contains the value of the Directed Network
Transmit state.

To set the Directed Network Transmit state of a Directed Forwarding Configuration Server with acknowledgment, a Directed Forwarding Configuration Client shall send a DIRECTED_­NETWORK_­TRANSMIT_­SET message. The response to the message is a DIRECTED_­NETWORK_­TRANSMIT_­STATUS message that contains the value of the Directed
Network Transmit state.

Upon receiving a DIRECTED_­NETWORK_­TRANSMIT_­STATUS message, a Directed Forwarding Configuration Client can determine the current Directed Network Transmit state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.9. Directed Relay Retransmit procedure

To determine the Directed Relay Retransmit state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_RELAY_RETRANSMIT_GET message. The response to the message is a DIRECTED_­RELAY_­RETRANSMIT_­STATUS message that contains the value of the Directed Relay Retransmit
state.

To set the Directed Relay Retransmit state of a Directed Forwarding Configuration Server with acknowledgment, a Directed Forwarding Configuration Client shall send a DIRECTED_­RELAY_­RETRANSMIT_­SET message. The response to the message is a DIRECTED_­RELAY_­RETRANSMIT_­STATUS message that contains the value of the Directed
Relay Retransmit state.

Upon receiving a DIRECTED_­RELAY_­RETRANSMIT_­STATUS message, a Directed Forwarding Configuration Client can determine the current Directed Relay Retransmit state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.10. RSSI Threshold procedure

To determine the RSSI Threshold state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a RSSI_THRESHOLD_GET message. The response to the message is a RSSI_THRESHOLD_STATUS message that contains the value of the RSSI Threshold state.

To set the RSSI Margin state of a Directed Forwarding Configuration Server with acknowledgment, a Directed Forwarding Configuration Client shall send a RSSI_THRESHOLD_SET message. The response to the message is a RSSI_THRESHOLD_STATUS message that contains the value of the RSSI Threshold state.

Upon receiving a RSSI_THRESHOLD_STATUS message, a Directed Forwarding Configuration Client can determine the RSSI Threshold state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.11. Directed Paths procedure

To determine the Directed Paths state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_PATHS_GET message. The response to the message is a DIRECTED_PATHS_STATUS message that contains the value of the Directed Paths state.

Upon receiving a DIRECTED_PATHS_STATUS message, a Directed Forwarding Configuration Client can determine the Directed Paths state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.12. Directed Publish Policy procedure

To determine the Directed Publish Policy state of a given model within an element of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_­PUBLISH_­POLICY_­GET message. The response to the message is a DIRECTED_­PUBLISH_­POLICY_­STATUS message that contains a status and
may contain the value of the Directed Publish Policy state of the model.

To set the Directed Publish Policy state of a given model within an element of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_­PUBLISH_­POLICY_­SET message. The response to the message is a DIRECTED_­PUBLISH_­POLICY_­STATUS message that contains a status and may
contain the value of the Directed Publish Policy state of the model.

Upon receiving a DIRECTED_­PUBLISH_­POLICY_­STATUS message, a Directed Forwarding Configuration Client can determine the status, which is either a Success or an error (see [Table 4.355](index-en.html#UUID-0e5a33c4-c1fa-f026-d278-62c1505bd5f0_Table_4.355 "Table 4.355. Error conditions for DIRECTED_PUBLISH_POLICY_GET and DIRECTED_PUBLISH_POLICY_SET messages")). If the status is Success, the Directed Forwarding Configuration Client can also determine the current Directed Publish Policy state of a particular model within an element of a Directed
Forwarding Configuration Server. If the status is an error, the Status field contains the error condition.

###### 4.4.8.2.13. Path Discovery Timing Control procedure

To determine the Path Discovery Timing Control state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a PATH_DISCOVERY_TIMING_CONTROL_GET message. The response to the message is a PATH_DISCOVERY_TIMING_CONTROL_STATUS message that contains the value of the Path Discovery
Timing Control state.

To set the Path Discovery Timing Control state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a PATH_DISCOVERY_TIMING_CONTROL_SET message. The response to the message is a PATH_DISCOVERY_TIMING_CONTROL_STATUS message that contains the value of the Path Discovery Timing
Control state.

Upon receiving a PATH_DISCOVERY_TIMING_CONTROL_STATUS message, a Directed Forwarding Configuration Client can determine the Path Discovery Timing Control state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.14. Directed Control Network Transmit procedure

To determine the Directed Control Network Transmit state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_­CONTROL_­NETWORK_­TRANSMIT_­GET message. The response to the message is a DIRECTED_­CONTROL_­NETWORK_­TRANSMIT_­STATUS message that contains the value of
the Directed Control Network Transmit state.

To set the Directed Control Network Transmit state of a Directed Forwarding Configuration Server with acknowledgment, a Directed Forwarding Configuration Client shall send a DIRECTED_­CONTROL_­NETWORK_­TRANSMIT_­SET message. The response to the message is a DIRECTED_­CONTROL_­NETWORK_­TRANSMIT_­STATUS message that contains
the value of the Directed Control Network Transmit state.

Upon receiving a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message, a Directed Forwarding Configuration Client can determine the current Directed Control Network Transmit state of a Directed Forwarding Configuration Server.

###### 4.4.8.2.15. Directed Control Relay Retransmit procedure

To determine the Directed Control Relay Retransmit state of a Directed Forwarding Configuration Server, a Directed Forwarding Configuration Client shall send a DIRECTED_­CONTROL_­RELAY_­RETRANSMIT_­GET message. The response to the message is a DIRECTED_­CONTROL_­RELAY_­RETRANSMIT_­STATUS message that contains the value of
the Directed Control Relay Retransmit state.

To set the Directed Control Relay Retransmit state of a Directed Forwarding Configuration Server with acknowledgment, a Directed Forwarding Configuration Client shall send a DIRECTED_­CONTROL_­RELAY_­RETRANSMIT_­SET message. The response to the message is a DIRECTED_­CONTROL_­RELAY_­RETRANSMIT_­STATUS message that contains
the value of the Directed Control Relay Retransmit state.

Upon receiving a DIRECTED_­CONTROL_­RELAY_­RETRANSMIT_­STATUS message, a Directed Forwarding Configuration Client can determine the current Directed Control Relay Retransmit state of a Directed Forwarding Configuration Server.

#### 4.4.9. Bridge Configuration Server model

##### 4.4.9.1. Description

The Bridge Configuration Server model is used to support the configuration of the subnet bridge functionality of a node.

The Bridge Configuration Server model is a main model that extends the Configuration Server model.

The Bridge Configuration Server model defines the state instances listed in [Table 4.357](index-en.html#UUID-71e223a5-46c0-a275-197c-bd5b57f2842d_Table_4.357 "Table 4.357. Bridge Configuration Server states and bindings") and the messages listed in [Table 4.358](index-en.html#UUID-71e223a5-46c0-a275-197c-bd5b57f2842d_Table_4.358 "Table 4.358. Bridge Configuration Server model messages").

If supported, the Bridge Configuration Server model shall be supported on the primary element and shall not be supported by any secondary elements. The access layer security on the Bridge Configuration Server model shall use the device key.

[Table 4.357](index-en.html#UUID-71e223a5-46c0-a275-197c-bd5b57f2842d_Table_4.357 "Table 4.357. Bridge Configuration Server states and bindings") illustrates the state bindings between the Bridge Configuration Server model states and the states of the models that
the Bridge Configuration Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Subnet Bridge | – | – |
| Bridging Table | Configuration Server | NetKey List |
| Bridging Table Size | – | – |

Table 4.357. Bridge Configuration Server states and bindings

[Table 4.358](index-en.html#UUID-71e223a5-46c0-a275-197c-bd5b57f2842d_Table_4.358 "Table 4.358. Bridge Configuration Server model messages") lists the Bridge Configuration Server model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Bridge Configuration Main (Primary) | Bridge Configuration Server | Subnet Bridge  (see [Section 4.2.41](index-en.html#UUID-bf3cdcfa-6e44-defb-18c2-ad69949b80cf "4.2.41. Subnet Bridge")) | SUBNET_BRIDGE_GET | M | – |
| SUBNET_BRIDGE SET | M | – |
| SUBNET_BRIDGE_STATUS | – | M |
| Bridging Table  (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) | BRIDGING_TABLE_ADD | M | – |
| BRIDGING_TABLE_REMOVE | M | – |
| BRIDGING_TABLE_STATUS | – | M |
| BRIDGED_SUBNETS_GET | M | – |
| BRIDGED_SUBNETS_LIST | – | M |
| BRIDGING_TABLE_GET | M | – |
| BRIDGING_TABLE_LIST | – | M |
| Bridging Table Size  (see [Section 4.2.43](index-en.html#UUID-40ebf047-039b-ff9d-e508-290dfe8681ca "4.2.43. Bridging Table Size")) | BRIDGING_TABLE_­SIZE_­GET | M | – |
| BRIDGING_TABLE_­SIZE_­STATUS | – | M |

Table 4.358. Bridge Configuration Server model messages

##### 4.4.9.2. Behavior

This section describes behaviors for states and messages for the Bridge Configuration server model.

###### 4.4.9.2.1. Subnet Bridge state

When an element receives a SUBNET_BRIDGE_GET message, it shall respond with a SUBNET_BRIDGE_STATUS message with the Subnet_Bridge field set to the current Subnet Bridge state.

When an element receives a SUBNET_BRIDGE_SET message, it shall set the Subnet Bridge state to the Subnet_Bridge field value in the received message and shall respond with a SUBNET_BRIDGE_STATUS message with the Subnet_Bridge field set to the new Subnet Bridge state.

###### 4.4.9.2.2. Bridging Table state

When an element receives a BRIDGING_TABLE_ADD message (see [Section 4.3.11.4](index-en.html#UUID-cc95fff6-a91e-1b79-abd1-2c0debf5feea "4.3.11.4. BRIDGING_TABLE_ADD")) that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.359](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.359 "Table 4.359. Error conditions for the BRIDGING_TABLE_ADD messages")), the element checks whether a Bridging Table state entry corresponding to the received message exists. A Bridging Table
state entry corresponding to the received message exists if the values of the NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields in the entry match the values of the corresponding fields in the message.

If a Bridging Table state entry corresponding to the received message does not exist, the element shall add a new entry to the Bridging Table state with the Directions, NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields set to the values of the corresponding fields in the received message.

If a Bridging Table state entry corresponding to the received message exists, the element shall set the Directions field in the entry to the value of the Directions field in the received message.

After the element updates the Bridging Table state based on a successfully processed BRIDGING_TABLE_ADD message, the element shall respond with a BRIDGING_TABLE_STATUS message (see [Section 4.3.11.6](index-en.html#UUID-fab530f3-84a3-1c86-14af-c4e8723e1100 "4.3.11.6. BRIDGING_TABLE_STATUS")) with the following configuration:

* The Status field shall be set to Success.
* The Current_Directions field shall be set to the value of the Directions field in the BRIDGING_TABLE_ADD message.
* The NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields shall be set to the values of the corresponding fields in the BRIDGING_TABLE_ADD message.

| Error Condition | Status Code Name (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| Either NetKeyIndex1 or NetKeyIndex2 is not known. | Invalid NetKey Index |
| There is not sufficient memory to add a Bridging Table state entry. | Insufficient Resources |

Table 4.359. Error conditions for the BRIDGING_TABLE_ADD messages

When an element receives a BRIDGING_TABLE_ADD message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.359](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.359 "Table 4.359. Error conditions for the BRIDGING_TABLE_ADD messages")), the element shall respond with a BRIDGING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to the Status Code corresponding to the error condition as defined in [Table 4.359](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.359 "Table 4.359. Error conditions for the BRIDGING_TABLE_ADD messages").
* The Current_Directions field shall be set to the value of the Directions field in the received message.
* The NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields shall be set to the values of the corresponding fields in the received message.

When an element receives a BRIDGING_TABLE_REMOVE message (see [Section 4.3.11.5](index-en.html#UUID-e423d1ae-47f6-ec68-83e3-986dc5f20da8 "4.3.11.5. BRIDGING_TABLE_REMOVE")) that is successfully processed (i.e., it does not result in any error condition listed in
[Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages")), it checks whether Bridging Table state entries corresponding to the received message
exist. A Bridging Table state entry corresponding to the received message exists if one of the following conditions is met:

* The values of the NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields in the entry match the values of the corresponding fields in the message.
* The values of the NetKeyIndex1, NetKeyIndex2, and Address1 fields in the entry match the values of the corresponding fields in the message, and the Address2 field value in the message is the unassigned address.
* The values of the NetKeyIndex1, NetKeyIndex2, and Address2 fields in the entry match the values of the corresponding fields in the message, and the Address1 field value in the message is the unassigned address.
* The values of the NetKeyIndex1 and NetKeyIndex2 fields in the entry match the values of the corresponding fields in the message, and the values of the Address1 and Address2 fields in the message are both the unassigned address.

If Bridging Table state entries corresponding to the received message exist, the element shall remove those entries from the Bridging Table state.

After the element updates the Bridging Table state based on a successfully processed BRIDGING_TABLE_REMOVE message, the element shall respond with a BRIDGING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to Success.
* The Current_Directions field shall be set to 0x00.
* The NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields shall be set to the values of the corresponding fields in the BRIDGING_TABLE_REMOVE message.

| Error Condition | Status Code Name (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| Either NetKeyIndex1 or NetKeyIndex2 is not known | Invalid NetKey Index |

Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages

When an element receives a BRIDGING_TABLE_REMOVE message that is not successfully processed (i.e., it results in any error condition listed in [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages")), the element shall respond with a BRIDGING_TABLE_STATUS message with the following configuration:

* The Status field shall be set to the Status Code corresponding to the error condition as defined in [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages").
* The Current_Directions field shall be set to 0x00.
* The NetKeyIndex1, NetKeyIndex2, Address1, and Address2 fields shall be set to the values of the corresponding fields in the received message.

When an element receives a BRIDGED_SUBNETS_GET messages (see [Section 4.3.11.7](index-en.html#UUID-898d24ab-99b1-ce66-728f-68f15dde8472 "4.3.11.7. BRIDGED_SUBNETS_GET")), it shall respond with a BRIDGED_SUBNETS_LIST message (see [Section 4.3.11.8](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a "4.3.11.8. BRIDGED_SUBNETS_LIST")) with the following configuration:

* The Filter, NetKeyIndex, and Start_Index fields shall be set to the values of the corresponding fields in the received message.
* The Bridged_Subnets_List field shall contain a filtered set of not repeated (i.e., unique) entries that are formatted as described in [Table 4.293](index-en.html#UUID-03b058d1-d0f3-dddc-ebef-390e0c5c1b7a_Table_4.293 "Table 4.293. Bridged_Subnets_List entry format"). The filtered set includes (NetKeyIndex1, NetKeyIndex2) pairs extracted from the Bridging Table state entries that meet the filtering condition in the Filter field (see [Table 4.291](index-en.html#UUID-898d24ab-99b1-ce66-728f-68f15dde8472_Table_4.291 "Table 4.291. Filter field values")) and starts with the filtered (NetKeyIndex1, NetKeyIndex2) pair indicated by the Start_Index field, considering zero-based indexing (i.e., the first filtered NetKey Indexes pair is
  assigned the index 0). If the Filter field value is 0b00, the NetKeyIndex field in the received BRIDGED_SUBNETS_GET message shall be ignored.

When an element receives a BRIDGING_TABLE_GET message (see [Section 4.3.11.9](index-en.html#UUID-90c0b066-0a8e-c6cb-2e97-280461179578 "4.3.11.9. BRIDGING_TABLE_GET")) that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages")), it shall respond with a BRIDGING_TABLE_LIST message (see [Section 4.3.11.10](index-en.html#UUID-fecb508a-86df-1ea4-6cb1-a6ac09e1e444 "4.3.11.10. BRIDGING_TABLE_LIST")) with the following configuration:

* The Status field shall be set to Success.
* The NetKeyIndex1, NetKeyIndex2, and Start_Index fields shall be set to the values of the corresponding fields in the received message.
* The Bridged_Addresses_List field shall contain a filtered set of entries that are extracted from the Bridging Table state (see [Section 4.2.42](index-en.html#UUID-b0b80feb-de53-0ffd-26bc-267a0db075c2 "4.2.42. Bridging Table")) and that are associated with the
  pair of subnets identified by the NetKeyIndex1 and NetKeyIndex2 fields and that are formatted as defined in [Table 4.296](index-en.html#UUID-fecb508a-86df-1ea4-6cb1-a6ac09e1e444_Table_4.296 "Table 4.296. Bridged_Addresses_List entry format"). The first
  Bridged_Addresses_List entry shall correspond to the filtered Bridging Table state entry that is indicated by the Start_Index field, considering zero-based indexing (i.e., the first filtered Bridging Table state entry is assigned the index 0).

When an element receives a BRIDGING_TABLE_GET message that is not successfully processed (i.e., it does not result in any error condition listed in [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages")), it shall respond with a BRIDGING_TABLE_LIST message with the following configuration:

* The Status field shall be set to the Status Code corresponding to the error condition as defined in [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages").
* The NetKeyIndex1, NetKeyIndex2, and Start_Index fields shall be set to the values of the corresponding fields in the received message.
* The Bridged_Addresses_List field value shall be empty.

###### 4.4.9.2.3. Bridging Table Size state

When an element receives a BRIDGING_TABLE_SIZE_GET message, it shall respond with a BRIDGING_TABLE_SIZE_STATUS message with the Bridging_Table_Size field set to Bridging Table Size state.

#### 4.4.10. Bridge Configuration Client model

##### 4.4.10.1. Description

The Bridge Configuration Client model is used to support the functionality of a node that can configure the subnet bridge functionality of another node.

The Bridge Configuration Client model is a root model and a main model that does not extend any other models. The Bridge Configuration Client model may operate on states defined by the Bridge Configuration Server model (see [Section 4.4.9](index-en.html#UUID-a56f2dd2-de1f-17af-7a79-f2c33ca03e26 "4.4.9. Bridge Configuration Server model")) using Bridge messages (see [Section 4.3.11](index-en.html#UUID-2d23f042-29b5-77af-ef59-49704c4c59a7 "4.3.11. Bridge messages")).

If supported, the Bridge Configuration Client shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Bridge Configuration Client model shall use the device key of the node supporting the Bridge Configuration Server model.

[Table 4.361](index-en.html#UUID-1c9c123b-9639-437c-3848-39828fbd64a2_Table_4.361 "Table 4.361. Bridge Configuration Client model messages") lists the Bridge Configuration Client model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Bridge Configuration Main  (Primary) | Bridge Configuration Client | Subnet Bridge | SUBNET_BRIDGE_SET | – | M |
| SUBNET_BRIDGE_GET | – | M |
| SUBNET_BRIDGE_STATUS | M | – |
| Bridging Table | BRIDGING_TABLE_ADD | – | M |
| BRIDGING_TABLE_REMOVE | – | M |
| BRIDGING_TABLE_STATUS | M | – |
| BRIDGED_SUBNETS_GET | – | M |
| BRIDGED_SUBNETS_LIST | M | – |
| BRIDGING_TABLE_GET | – | M |
| BRIDGING_TABLE_LIST | M | – |
| Bridging Table Size | BRIDGING_TABLE_SIZE_GET | – | M |
| BRIDGING_TABLE_SIZE_STATUS | M | – |

Table 4.361. Bridge Configuration Client model messages

##### 4.4.10.2. Behavior

This section describes behaviors for procedures and messages for the Bridge Configuration Client model.

###### 4.4.10.2.1. Subnet Bridge procedure

To determine the Subnet Bridge state of a Bridge Configuration Server, a Bridge Configuration Client shall send a SUBNET_BRIDGE_GET message. The response is a SUBNET_BRIDGE_STATUS message that contains the Subnet Bridge state.

To set the Subnet Bridge state of a Bridge Configuration Server with an acknowledgment, a Bridge Configuration Client shall send a SUBNET_­BRIDGE_­SET message. The response is a SUBNET_­BRIDGE_­STATUS message that contains the Subnet Bridge state.

Upon receiving a SUBNET_BRIDGE_STATUS message, a Bridge Configuration Client can determine the Subnet Bridge state of a Bridge Configuration Server.

###### 4.4.10.2.2. Bridging Table procedure

To add or update an entry in the Bridging Table state of a Bridge Configuration Server with an acknowledgment, a Bridge Configuration Client shall send a BRIDGING_TABLE_ADD message. The response is a BRIDGING_TABLE_STATUS message that contains a status and the Bridging Table state entry.

To remove entries from the Bridging Table state of a Bridge Configuration Server with an acknowledgment, a Bridge Configuration Client shall send a BRIDGING_TABLE_REMOVE message. The response is a BRIDGING_TABLE_STATUS message that contains a status and a copy of the values of the fields in the BRIDGING_TABLE_REMOVE
message.

Upon receiving a BRIDGING_TABLE_STATUS message, a Bridge Configuration Client can determine the status, which is either Success or one of the error codes listed in [Table 4.359](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.359 "Table 4.359. Error conditions for the BRIDGING_TABLE_ADD messages") and [Table 4.360](index-en.html#UUID-08e15c5a-da7a-4762-06cd-fa25d2304717_Table_4.360 "Table 4.360. Error conditions for the BRIDGING_TABLE_REMOVE and BRIDGING_TABLE_GET messages"). If the status is Success, the Bridge Configuration Client can determine the addresses in the subnets that were used to change the Bridging Table state. If the status is an error, the Status field will
contain the error condition.

To determine a filtered set of pairs of bridged subnets extracted from the Bridging Table state entries of a Bridge Configuration Server, a Bridge Configuration Client shall send a BRIDGED_SUBNETS_GET message. The response is a BRIDGED_SUBNETS_LIST message that contains a filtered set of pairs of NetKey Indexes extracted
from the Bridging Table state entries. The filtered set of pairs of NetKey Indexes reported in the response message starts with the pair of NetKey Indexes that is indicated by the Start_Index field, considering zero-based indexing (i.e., the first filtered pair of NetKey Indexes is assigned the index 0).

To determine a filtered set of bridged addresses of a pair of bridged subnets formatted as described in [Table 4.296](index-en.html#UUID-fecb508a-86df-1ea4-6cb1-a6ac09e1e444_Table_4.296 "Table 4.296. Bridged_Addresses_List entry format") and extracted from the
Bridging Table state entries of a Bridge Configuration Server corresponding to a given pair of subnets, a Bridge Configuration Client shall send a BRIDGING_TABLE_GET message. The response is a BRIDGING_TABLE_LIST message that contains a status. If the Status is Success, the Bridged_Addresses_List field of the response message
contains a filtered set of pairs of bridged addresses with allowed traffic directions that are extracted from the Bridging Table state entries and that correspond to the pair of subnets indicated in the BRIDGING_TABLE_GET message. The filtered set of pairs of bridged addresses reported in the response message starts with the
pair of bridged addresses that is indicated by the Start_Index field, considering zero-based numbering (i.e., the first filtered pair of bridged addresses is assigned the index 0).

###### 4.4.10.2.3. Bridging Table Size procedure

To determine the Bridging Table Size state of a Bridge Configuration Server, a Bridge Configuration Client shall send a BRIDGING_TABLE_SIZE_GET message. The response is a BRIDGING_TABLE_SIZE_STATUS message that contains the Bridging Table Size state.

#### 4.4.11. Mesh Private Beacon Server model

##### 4.4.11.1. Description

The Mesh Private Beacon Server model is used to support the configuration of the Mesh Private beacons functionality of a node (see [Section 3.10.4](index-en.html#UUID-7b47a908-e147-61ac-8aa0-d60bd1ad9c37 "3.10.4. Mesh Private beacon")).

The Mesh Private Beacon Server model is a main model that extends the Configuration Server model.

The Mesh Private Beacon Server model defines the state instances listed in [Table 4.362](index-en.html#UUID-cd9ab335-e917-2f96-6ee5-9a8a1c44cc8d_Table_4.362 "Table 4.362. Mesh Private Beacon Server states and bindings") and the messages listed in [Table 4.363](index-en.html#UUID-cd9ab335-e917-2f96-6ee5-9a8a1c44cc8d_Table_4.363 "Table 4.363. Mesh Private Beacon Server model messages").

If supported, the Mesh Private Beacon Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Mesh Private Beacon Server model shall use the device key.

[Table 4.362](index-en.html#UUID-cd9ab335-e917-2f96-6ee5-9a8a1c44cc8d_Table_4.362 "Table 4.362. Mesh Private Beacon Server states and bindings") illustrates the state bindings between the Mesh Private Beacon Server model states and the states of the models that
the Mesh Private Beacon Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Mesh Private Beacon | – | – |
| Random Update Period | – | – |
| Private GATT Proxy | Configuration Server | GATT Proxy |
| Private Node Identity | Configuration Server | Node Identity |

Table 4.362. Mesh Private Beacon Server states and bindings

[Table 4.363](index-en.html#UUID-cd9ab335-e917-2f96-6ee5-9a8a1c44cc8d_Table_4.363 "Table 4.363. Mesh Private Beacon Server model messages") lists the Mesh Private Beacon Server model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Mesh Private Beacon Main  (Primary) | Mesh Private Beacon Server | Mesh Private Beacon | PRIVATE_BEACON_GET | M | – |
| PRIVATE_BEACON_SET | M | – |
| PRIVATE_BEACON_STATUS | – | M |
| Private GATT Proxy | PRIVATE_GATT_PROXY_­GET | M | – |
| PRIVATE_GATT_PROXY_­SET | M | – |
| PRIVATE_GATT_PROXY_­STATUS | – | M |
| Private Node Identity | PRIVATE_NODE_IDENTITY_­GET | M | – |
| PRIVATE_NODE_IDENTITY_­SET | M | – |
| PRIVATE_NODE_IDENTITY_­STATUS | – | M |

Table 4.363. Mesh Private Beacon Server model messages

##### 4.4.11.2. Behavior

This section describes behaviors for states and messages for the Mesh Private Beacon Server model.

###### 4.4.11.2.1. Mesh Private Beacon state

When an element receives a PRIVATE_BEACON_GET message, the element shall respond with a PRIVATE_BEACON_STATUS message.

When an element receives a PRIVATE_BEACON_SET message, the element shall set the Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) to the value of the Private_Beacon field in the message.
If the Random_Update_Interval_Steps field is present in the PRIVATE_BEACON_SET message, the element shall set the Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) to the value of the Random_Update_Interval_Steps field in the message. The element shall respond with a PRIVATE_BEACON_STATUS message.

When responding to a MESH_PRIVATE_BEACON_GET message or a MESH_PRIVATE_BEACON_SET message with a PRIVATE_BEACON_STATUS message, the Private_Beacon field shall be set to the current Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) and the Random_Update_Interval_Steps field shall be set to the current Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of the node.

###### 4.4.11.2.2. Private GATT Proxy state

When an element receives a PRIVATE_GATT_PROXY_GET message, it shall respond with a PRIVATE_GATT_PROXY_STATUS message with the Private_GATT_Proxy field set to the current Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

When an element receives a PRIVATE_GATT_PROXY_SET message, and the node supports the Mesh GATT Proxy Service, the node shall set the Private GATT Proxy state to the value of the Private_GATT_Proxy field of the message (see the binding rules in [Section 4.2.45.1](index-en.html#UUID-0fffd5be-d88d-fbc6-bd8a-4264edb44070 "4.2.45.1. Binding with GATT Proxy")) and shall respond with a PRIVATE_GATT_PROXY_STATUS message with the Private_GATT_Proxy field set to the current Private GATT Proxy state.

When an element receives a PRIVATE_GATT_PROXY_SET message, and the node does not support the Mesh GATT Proxy Service, the node shall respond with a PRIVATE_GATT_PROXY_STATUS message with the Private_GATT_Proxy field set to the current Private GATT Proxy state.

###### 4.4.11.2.3. Private Node Identity state

When an element receives a PRIVATE_NODE_IDENTITY_GET message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state")), it shall respond with a PRIVATE_NODE_IDENTITY_STATUS message with the Private_Identity field set to the current Private Node Identity state (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")) of the subnet identified by the NetKeyIndex field, with the NetKeyIndex field set to the corresponding value in the incoming message, and with the Status field set to Success.

| Error Condition | Status Code Name  (see Assigned Numbers document [[4](index-en.html#idp254746)]) |
| --- | --- |
| The key identified by the NetKeyIndex is not valid for this device | Invalid NetKey Index |
| The node cannot change the Private Node Identity state due to binding with the Node Identity state (see [Section 4.2.46.1](index-en.html#UUID-68bd1f46-2483-c874-f363-2f3e64057cac "4.2.46.1. Binding with Node Identity")). | Temporarily Unable to Change State |
| The node cannot start advertising due to lack of advertising resources like radio slots, buffers etc. | Insufficient Resources |

Table 4.364. Error Conditions for Private Node Identity state

When an element receives a PRIVATE_NODE_IDENTITY_GET message that is not successfully processed (i.e., it results in any error conditions listed in [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state")), it shall respond with a PRIVATE_NODE_IDENTITY_STATUS message with the NetKeyIndex field set to the corresponding value in the incoming message, with the Private_Identity field set to Disabled, and with the Status field set to a
status code defined in [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state").

When an element receives a PRIVATE_NODE_IDENTITY_SET message that is successfully processed (i.e., it does not result in any error conditions listed in [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state")), it shall set the Private Node Identity state identified by the NetKeyIndex field to the value of the Private_Identity field in the message (see the binding rules in [Section 4.2.46.1](index-en.html#UUID-68bd1f46-2483-c874-f363-2f3e64057cac "4.2.46.1. Binding with Node Identity")) and shall respond with a PRIVATE_NODE_IDENTITY_STATUS message with the Private_Identity field set to the current Private Node Identity state of the NetKey, with the NetKeyIndex field set to the
corresponding value in the incoming message, and with the Status field set to Success.

When an element receives a PRIVATE_NODE_IDENTITY_SET message that is not successfully processed (i.e., it results in any error conditions listed in [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state")), it shall respond with a PRIVATE_NODE_IDENTITY_STATUS message with the NetKeyIndex and Private_Identity fields set to the corresponding values in the incoming message and with the Status field set to a status code defined in
[Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state").

#### 4.4.12. Mesh Private Beacon Client model

##### 4.4.12.1. Description

The Mesh Private Beacon Client model is used to support the functionality of a node that can configure the Mesh Private beacons functionality of another node (see [Section 3.10.4](index-en.html#UUID-7b47a908-e147-61ac-8aa0-d60bd1ad9c37 "3.10.4. Mesh Private beacon")).

The Mesh Private Beacon Client model is a root model and a main model that does not extend any other models. The Mesh Private Beacon Client model may operate on states defined by the Mesh Private Beacon Server model (see [Section 4.4.11](index-en.html#UUID-17060fa4-826d-6459-f06b-a036fb0e8b43 "4.4.11. Mesh Private Beacon Server model")) using Mesh Private Beacon messages (see [Section 4.3.12](index-en.html#UUID-a8dc7606-cf17-7bb6-c44e-7bf65c28b45f "4.3.12. Mesh Private Beacon messages")).

If supported, the Mesh Private Beacon Client model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Mesh Private Beacon Client model shall use the device key of the node supporting the Mesh Private Beacon Server model.

[Table 4.365](index-en.html#UUID-c41f9706-ad76-6d1b-b72e-daafc6875a7c_Table_4.365 "Table 4.365. Mesh Private Beacon Client model messages") lists the Mesh Private Beacon Client model messages. The model shall support receiving the messages marked as mandatory in
the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Mesh Private Beacon Main  (Primary) | Mesh Private Beacon Client | Mesh Private Beacon | PRIVATE_BEACON_GET | – | M |
| PRIVATE_BEACON_SET | – | M |
| PRIVATE_BEACON_STATUS | M | – |
| Private GATT Proxy | PRIVATE_GATT_PROXY_GET | – | M |
| PRIVATE_GATT_PROXY_SET | – | M |
| PRIVATE_GATT_PROXY_­STATUS | M | – |
| Private Node Identity | PRIVATE_NODE_IDENTITY_­GET | – | M |
| PRIVATE_NODE_IDENTITY_­SET | – | M |
| PRIVATE_NODE_IDENTITY_­STATUS | M | – |

Table 4.365. Mesh Private Beacon Client model messages

##### 4.4.12.2. Behavior

This section describes behaviors for procedures and messages for the Mesh Private Beacon Client model.

An element can send any Mesh Private Beacon Client message at any time to query or change a state of a peer element.

###### 4.4.12.2.1. Mesh Private Beacon procedure

To determine the Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) and Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of a node, a Mesh Private Beacon Client shall send a PRIVATE_BEACON_GET message. The response is a PRIVATE_BEACON_STATUS message that contains the Private Beacon state and the Random Update
Interval Steps state of the node.

To set the Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) and the Random Update Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of a node, a Mesh Private Beacon Client shall send a PRIVATE_BEACON_SET message with the Private_Beacon field (see [Table 4.300](index-en.html#UUID-12408cf3-da06-4112-efc3-ebd7549c4b78_Table_4.300 "Table 4.300. PRIVATE_BEACON_SET message structure")) and the Random_Update_Interval_Steps field (see [Table 4.300](index-en.html#UUID-12408cf3-da06-4112-efc3-ebd7549c4b78_Table_4.300 "Table 4.300. PRIVATE_BEACON_SET message structure")) set to the intended new values. If no change to the Random Update Interval Steps state is needed, the Random_Update_Interval_Steps field should not be present in the message. The response is a PRIVATE_BEACON_STATUS message that contains the
Private Beacon state and the Random Update Interval Steps state.

Upon receiving a PRIVATE_BEACON_STATUS message, a Mesh Private Beacon Client can determine the current Private Beacon state (see [Section 4.2.44.1](index-en.html#UUID-6ab79b08-aa31-e788-a5ad-83aaf5f21853 "4.2.44.1. Private Beacon")) and the current Random Update
Interval Steps state (see [Section 4.2.44.2](index-en.html#UUID-7b1df5c3-8dcd-1992-7dab-d3f8401392cb "4.2.44.2. Random Update Interval Steps")) of the node.

###### 4.4.12.2.2. Private GATT Proxy procedure

To determine the Private GATT Proxy state of a Mesh Private Beacon Server, a Mesh Private Beacon Client shall send a PRIVATE_GATT_PROXY_GET message. The response is a PRIVATE_GATT_PROXY_STATUS message that contains the Private GATT Proxy state (see [Section 4.2.45](index-en.html#UUID-59ed979f-f456-1084-b297-24a895912eb4 "4.2.45. Private GATT Proxy")).

To set the Private GATT Proxy state of a Mesh Private Beacon Server with acknowledgment, a Mesh Private Beacon Client shall send a PRIVATE_GATT_PROXY_SET message. The response is a PRIVATE_GATT_PROXY_STATUS message that contains the Private GATT Proxy state.

Upon receiving a PRIVATE_GATT_PROXY_STATUS message, a Mesh Private Beacon Client can determine the current Private GATT Proxy state of a Mesh Private Beacon Server.

###### 4.4.12.2.3. Private Node Identity procedure

To determine the Private Node Identity state of the NetKey identified by the NetKeyIndex of a Mesh Private Beacon Server, a Mesh Private Beacon Client shall send a PRIVATE_NODE_IDENTITY_GET message. The response is a PRIVATE_NODE_IDENTITY_STATUS message that contains a status, NetKeyIndex value, and the Private Node Identity
state (see [Section 4.2.46](index-en.html#UUID-b6b0536d-9b37-9620-e31b-57b6b1d1ebee "4.2.46. Private Node Identity")) of the NetKey.

To set the Private Node Identity state of the NetKey identified by the NetKeyIndex of a Mesh Private Beacon Server with acknowledgment, a Mesh Private Beacon Client shall send a PRIVATE_NODE_IDENTITY_SET message. The response is a PRIVATE_NODE_IDENTITY_STATUS message that contains a status, NetKeyIndex value, and the Private
Node Identity state.

Upon receiving a PRIVATE_NODE_IDENTITY_STATUS message, a Mesh Private Beacon Client can determine the status, which can be either Success or an error (see [Table 4.364](index-en.html#UUID-d96f48fa-adf0-dc81-b6fc-d7c5c312c308_Table_4.364 "Table 4.364. Error Conditions for Private Node Identity state")). If the status is Success, the Mesh Private Beacon Client can also determine the current Private Node Identity state of the NetKey identified by the NetKeyIndex of a Mesh Private Beacon Server. If the status is an error, the Status
field will contain the error condition, and the Private_Identity field will be set to Disabled.

#### 4.4.13. On-Demand Private Proxy Server model

##### 4.4.13.1. Description

The On-Demand Private Proxy Server model is used to support the configuration of the advertising with Private Network Identity type (see [Section 7.2.2.2.4](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19 "7.2.2.2.4. Advertising with Private Network Identity"))
functionality of a node.

The On-Demand Private Proxy Server model is a main model that extends the Mesh Private Beacon Server model and corresponds with the Solicitation PDU RPL Configuration Server model (see [Section 4.4.17](index-en.html#UUID-5193c244-60d7-2072-f72a-c00de41f5002 "4.4.17. Solicitation PDU RPL Configuration Server model")).

When this model is present on an element, the corresponding Solicitation PDU RPL Configuration Server model (see [Section 4.4.17](index-en.html#UUID-5193c244-60d7-2072-f72a-c00de41f5002 "4.4.17. Solicitation PDU RPL Configuration Server model")) shall also be
present.

The On-Demand Private Proxy Server model defines the state instances listed in [Table 4.366](index-en.html#UUID-dc3e8dc4-b9fc-af4c-9b44-cb76a79da01f_Table_4.366 "Table 4.366. On-Demand Private Proxy Server states and bindings") and the messages listed in [Table 4.367](index-en.html#UUID-dc3e8dc4-b9fc-af4c-9b44-cb76a79da01f_Table_4.367 "Table 4.367. On-Demand Private Proxy Server model messages").

If supported, the On-Demand Private Proxy Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the On-Demand Private Proxy Server model shall use the device key.

[Table 4.366](index-en.html#UUID-dc3e8dc4-b9fc-af4c-9b44-cb76a79da01f_Table_4.366 "Table 4.366. On-Demand Private Proxy Server states and bindings") illustrates the state bindings between the On-Demand Private Proxy Server model states and the states of the models
that the On-demand Private Proxy Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| On-Demand_Private_GATT_Proxy | Mesh Private Beacon Server | Private GATT Proxy |

Table 4.366. On-Demand Private Proxy Server states and bindings

[Table 4.367](index-en.html#UUID-dc3e8dc4-b9fc-af4c-9b44-cb76a79da01f_Table_4.367 "Table 4.367. On-Demand Private Proxy Server model messages") lists the On-Demand Private Proxy Server model messages. The model shall support receiving the messages marked as
mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| On-Demand Proxy Main (Primary) | On-Demand Private Proxy Server | On-Demand Private GATT Proxy | ON_DEMAND_PRIVATE_PROXY_GET | M | – |
| ON_DEMAND_PRIVATE_PROXY_SET | M | – |
| ON_DEMAND_PRIVATE_PROXY_STATUS | – | M |

Table 4.367. On-Demand Private Proxy Server model messages

##### 4.4.13.2. Behavior

This section describes behaviors for states and messages for the On-Demand Private Proxy Server model.

###### 4.4.13.2.1. On-Demand Private GATT Proxy state

When an element receives an ON_DEMAND_PRIVATE_PROXY_GET message, it shall respond with an ON_DEMAND_PRIVATE_PROXY_STATUS message with the On-Demand_Private_GATT_Proxy field set to the current On-Demand Private GATT Proxy state.

When an element receives an ON_DEMAND_PRIVATE_PROXY_SET message, and the Private GATT Proxy state value is set to either Disabled or Enabled, it shall set the On-Demand Private GATT Proxy state to the value of the On-Demand_Private_GATT_Proxy field of the message and shall respond with an ON_DEMAND_PRIVATE_PROXY_STATUS
message with the On-Demand_Private_GATT_Proxy field set to the current On-Demand Private GATT Proxy state.

When an element receives an ON_DEMAND_PRIVATE_PROXY_SET message, and the Private GATT Proxy state value is set to Not Supported, it shall respond with an ON_DEMAND_PRIVATE_PROXY_STATUS message with the On-Demand_Private_GATT_Proxy field value set to Disabled.

#### 4.4.14. On-Demand Private Proxy Client model

##### 4.4.14.1. Description

The On-Demand Private Proxy Client model is used to support the functionality of a node that can configure the advertising with Private Network Identity type (see [Section 7.2.2.2.4](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19 "7.2.2.2.4. Advertising with Private Network Identity")) functionality of another node (see [Section 3.10.4](index-en.html#UUID-7b47a908-e147-61ac-8aa0-d60bd1ad9c37 "3.10.4. Mesh Private beacon")).

The On-Demand Private Proxy Client model is a root model and a main model that does not extend any other models. The On-Demand Private Proxy Client model may operate on states defined by the On-Demand Private Proxy Server model (see [Section 4.4.13](index-en.html#UUID-c50312c6-d68d-0472-0e62-d2f09c0e600a "4.4.13. On-Demand Private Proxy Server model")) using On-Demand Private Proxy messages (see [Section 4.3.6](index-en.html#UUID-410cbfe0-1409-84f9-37a8-db5569b6f082 "4.3.6. On-Demand Private GATT Proxy messages")).

If supported, the On-Demand Private Proxy Client model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the On-Demand Private Proxy Client model shall use the device key of the node supporting the On-Demand Private Proxy Server model.

[Table 4.368](index-en.html#UUID-6bdf7518-58c7-5491-bbc9-cf920b40315b_Table_4.368 "Table 4.368. On-Demand Private Proxy Client model messages") lists the On-Demand Private Proxy Client model messages. The model shall support receiving the messages marked as
mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| On-Demand Proxy Main (Primary) | On-Demand Private Proxy Client | On-Demand Private GATT Proxy | ON_DEMAND_PRIVATE_­PROXY_­GET | – | M |
| ON_DEMAND_PRIVATE_­PROXY_­SET | – | M |
| ON_DEMAND_PRIVATE_­PROXY_­STATUS | M | – |

Table 4.368. On-Demand Private Proxy Client model messages

##### 4.4.14.2. Behavior

This section describes behaviors for procedures and messages for the On-Demand Private Proxy Client model.

An element can send any On-Demand Private GATT Proxy message at any time to query or change a configuration state of a peer element. On-Demand Private GATT Proxy messages shall be secured using a DevKey.

###### 4.4.14.2.1. On-Demand Private GATT Proxy procedure

To determine the On-Demand Private GATT Proxy state of an On-Demand Private Proxy Server, an On-Demand Private Proxy Client shall send an ON_DEMAND_PRIVATE_PROXY_GET message. The response is an ON_DEMAND_PRIVATE_PROXY_STATUS message that contains the On-Demand Private GATT Proxy state.

To set the On-Demand Private GATT Proxy state of an On-Demand Private GATT Proxy Server with acknowledgment, an On-Demand Private GATT Proxy Client shall send an ON_DEMAND_PRIVATE_PROXY_SET message. The response is an ON_DEMAND_PRIVATE_PROXY_STATUS message that contains the On-Demand Private GATT Proxy state.

Upon receiving an ON_DEMAND_PRIVATE_PROXY_STATUS message, an On-Demand Private Proxy Client can determine the current On-Demand Private GATT Proxy state of an On-Demand Private Proxy Server.

#### 4.4.15. SAR Configuration Server model

##### 4.4.15.1. Description

The SAR Configuration Server model is used to support the configuration of the segmentation and reassembly behavior of a node (see [Section 3.5.3](index-en.html#UUID-ab0dc347-855f-b185-41a4-78f7ddd03586 "3.5.3. Segmentation and reassembly")).

The SAR Configuration Server model is a root model and a main model that does not extend any other models.

The SAR Configuration Server model defines the state instances listed in [Table 4.369](index-en.html#UUID-31fc39fe-e27b-97df-042d-f766b93095c9_Table_4.369 "Table 4.369. SAR Configuration Server states and bindings") and the messages listed in [Table 4.370](index-en.html#UUID-31fc39fe-e27b-97df-042d-f766b93095c9_Table_4.370 "Table 4.370. SAR Configuration Server model messages").

If supported, the SAR Configuration Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the SAR Configuration Server model shall use the device key.

[Table 4.369](index-en.html#UUID-31fc39fe-e27b-97df-042d-f766b93095c9_Table_4.369 "Table 4.369. SAR Configuration Server states and bindings") illustrates the state bindings between the SAR Configuration Server model states and the states of the models that the
SAR Configuration Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| SAR Transmitter | – | – |
| SAR Receiver | – | – |

Table 4.369. SAR Configuration Server states and bindings

[Table 4.370](index-en.html#UUID-31fc39fe-e27b-97df-042d-f766b93095c9_Table_4.370 "Table 4.370. SAR Configuration Server model messages") lists the SAR Configuration Server model messages. The model shall support receiving the messages marked as mandatory in the
Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| SAR Configuration Main (Primary) | SAR Configuration Server | SAR Transmitter  (see [Section 4.2.48](index-en.html#UUID-7aedc200-c204-f2bb-fb46-5912392a1a67 "4.2.48. SAR Transmitter")) | SAR_TRANSMITTER_GET | M | – |
| SAR_TRANSMITTER_SET | M | – |
| SAR_TRANSMITTER_STATUS | – | M |
| SAR Receiver  (see [Section 4.2.49](index-en.html#UUID-53d1addb-d801-574a-cf82-b7f3749083c3 "4.2.49. SAR Receiver")) | SAR_RECEIVER_GET | M | – |
| SAR_RECEIVER_SET | M | – |
| SAR_RECEIVER_STATUS | – | M |

Table 4.370. SAR Configuration Server model messages

##### 4.4.15.2. Behavior

This section describes behaviors for states and messages for the SAR Configuration Server model.

###### 4.4.15.2.1. SAR Transmitter state

When an element receives a SAR_TRANSMITTER_GET message, it shall respond with a SAR_TRANSMITER_STATUS message with the following configuration:

* The SAR_Segment_Interval_Step field shall be set to the current SAR Segment Interval Step state (see [Section 4.2.48.1](index-en.html#UUID-8e9f8c8e-5f5b-cfc3-c6c5-8104d04ea236 "4.2.48.1. SAR Segment Interval Step")).
* The SAR_Unicast_Retransmissions_Count field shall be set to the current SAR Unicast Retransmissions Count state (see [Section 4.2.48.2](index-en.html#UUID-2dd0fc6f-d7a1-15d5-b9a7-1d63c5752ce4 "4.2.48.2. SAR Unicast Retransmissions Count")).
* The SAR_Unicast_Retransmissions_Without_Progress_Count field shall be set to the current SAR Unicast Retransmissions Without Progress Count state (see [Section 4.2.48.3](index-en.html#UUID-eff91da3-c5c0-f4c0-6037-c9e713dc7d9a "4.2.48.3. SAR Unicast Retransmissions Without Progress Count")).
* The SAR_Unicast_Retransmissions_Interval_Step field shall be set to the current SAR Unicast Retransmissions Interval Step state (see [Section 4.2.48.4](index-en.html#UUID-26e4432b-aeba-a9ff-71b1-7880bcad6605 "4.2.48.4. SAR Unicast Retransmissions Interval Step")).
* The SAR_Unicast_Retransmissions_Interval_Increment field shall be set to the current SAR Unicast Retransmissions Interval Increment state (see [Section 4.2.48.5](index-en.html#UUID-fd2d1be5-ca83-2c6e-724f-99e63a6824a7 "4.2.48.5. SAR Unicast Retransmissions Interval Increment")).
* The SAR_Multicast_Retransmissions_Count field shall be set to the current SAR Multicast Retransmissions Count state (see [Section 4.2.48.6](index-en.html#UUID-5f949ca2-e0af-4e91-83b4-fa41f68fd284 "4.2.48.6. SAR Multicast Retransmissions Count")).
* The SAR_Multicast_Retransmissions_Interval_Step field shall be set to the current SAR Multicast Retransmissions Interval Step state (see [Section 4.2.48.7](index-en.html#UUID-2dd60df5-b721-e70e-e473-b8c4ad9faec0 "4.2.48.7. SAR Multicast Retransmissions Interval Step")).

When an element receives a SAR_TRANSMITTER_SET message, it shall set following states to the corresponding field values in the received message:

* SAR Segment Interval Step state
* SAR Unicast Retransmissions Count state
* SAR Unicast Retransmissions Without Progress Count state
* SAR Unicast Retransmissions Interval Step state
* SAR Unicast Retransmissions Interval Increment state
* SAR Multicast Retransmissions Count state
* SAR Multicast Retransmissions Interval Step state

In response to a SAR_TRANSMITTER_SET message, the element shall also transmit a SAR_TRANSMITTER_STATUS message with the following configuration:

* The SAR_Segment_Interval_Step field shall be set to the current SAR Segment Interval Step state (see [Section 4.2.48.1](index-en.html#UUID-8e9f8c8e-5f5b-cfc3-c6c5-8104d04ea236 "4.2.48.1. SAR Segment Interval Step")).
* The SAR_Unicast_Retransmissions_Count field shall be set to the current SAR Unicast Retransmissions Count state (see [Section 4.2.48.2](index-en.html#UUID-2dd0fc6f-d7a1-15d5-b9a7-1d63c5752ce4 "4.2.48.2. SAR Unicast Retransmissions Count")).
* The SAR_Unicast_Retransmissions_Without_Progress_Count field shall be set to the current SAR Unicast Retransmissions Without Progress Count state (see [Section 4.2.48.3](index-en.html#UUID-eff91da3-c5c0-f4c0-6037-c9e713dc7d9a "4.2.48.3. SAR Unicast Retransmissions Without Progress Count")).
* The SAR_Unicast_Retransmissions_Interval_Step field shall be set to the current SAR Unicast Retransmissions Interval Step state (see [Section 4.2.48.4](index-en.html#UUID-26e4432b-aeba-a9ff-71b1-7880bcad6605 "4.2.48.4. SAR Unicast Retransmissions Interval Step")).
* The SAR_Unicast_Retransmissions_Interval_Increment field shall be set to the current SAR Unicast Retransmissions Interval Increment state (see [Section 4.2.48.5](index-en.html#UUID-fd2d1be5-ca83-2c6e-724f-99e63a6824a7 "4.2.48.5. SAR Unicast Retransmissions Interval Increment")).
* The SAR_Multicast_Retransmissions_Count field shall be set to the current SAR Multicast Retransmissions Count state (see [Section 4.2.48.6](index-en.html#UUID-5f949ca2-e0af-4e91-83b4-fa41f68fd284 "4.2.48.6. SAR Multicast Retransmissions Count")).
* The SAR_Multicast_Retransmissions_Interval_Step field shall be set to the current SAR Multicast Retransmissions Interval Step state (see [Section 4.2.48.7](index-en.html#UUID-2dd60df5-b721-e70e-e473-b8c4ad9faec0 "4.2.48.7. SAR Multicast Retransmissions Interval Step")).

###### 4.4.15.2.2. SAR Receiver state

When an element receives a SAR_RECEIVER_GET message, it shall respond with a SAR_RECEIVER_STATUS message with the following configuration:

* The SAR_Segments_Threshold field shall be set to the current SAR Segments Threshold state (see [Section 4.2.49.1](index-en.html#UUID-1485ed5f-fe9d-3af8-923b-e4a1464adee6 "4.2.49.1. SAR Segments Threshold")).
* The SAR_Discard_Timeout field shall be set to the current SAR Discard Timeout state (see [Section 4.2.49.4](index-en.html#UUID-b566885f-47f4-a84d-9ca9-fbabaf87406a "4.2.49.4. SAR Discard Timeout")).
* The SAR_Acknowledgment_Delay_Increment field shall be set to the current SAR Acknowledgment Delay Increment state (see [Section 4.2.49.2](index-en.html#UUID-41e1a57f-f1ae-d323-67e4-54a8b8aeb70f "4.2.49.2. SAR Acknowledgment Delay Increment")).
* The SAR_Acknowledgment_Retransmissions_Count field shall be set to the current SAR Acknowledgment Retransmissions Count state (see [Section 4.2.49.3](index-en.html#UUID-604f7ad9-8618-da8f-cf30-edd183f08c66 "4.2.49.3. SAR Acknowledgment Retransmissions Count")).
* The SAR_Receiver_Segment_Interval_Step field shall be set to the current SAR Receiver Segment Interval Step (see [Section 4.2.49.5](index-en.html#UUID-cb59ec2b-0564-e693-a2b2-498e11382769 "4.2.49.5. SAR Receiver Segment Interval Step")).

When an element receives a SAR_RECEIVER_SET message, it shall set the following states to the value corresponding value in the received message:

* SAR Segments Threshold state
* SAR Discard Timeout state
* SAR Acknowledgment Delay Increment state
* SAR Acknowledgment Retransmissions Count state
* SAR Discard Timeout
* SAR Receiver Segment Interval Step

In response to a SAR_RECEIVER_SET message, the element also shall transmit a SAR_RECEIVER_STATUS message with the following configuration:

* The SAR_Segments_Threshold field shall be set to the current SAR Segments Threshold state (see [Section 4.2.49.1](index-en.html#UUID-1485ed5f-fe9d-3af8-923b-e4a1464adee6 "4.2.49.1. SAR Segments Threshold")).
* The SAR_Discard_Timeout field shall be set to the current SAR Discard Timeout state (see [Section 4.2.49.4](index-en.html#UUID-b566885f-47f4-a84d-9ca9-fbabaf87406a "4.2.49.4. SAR Discard Timeout")).
* The SAR_Acknowledgment_Delay_Increment field shall be set to the current SAR Acknowledgment Delay Increment state (see [Section 4.2.49.2](index-en.html#UUID-41e1a57f-f1ae-d323-67e4-54a8b8aeb70f "4.2.49.2. SAR Acknowledgment Delay Increment")).
* The SAR_Acknowledgment_Retransmissions_Count field shall be set to the current SAR Acknowledgment Retransmissions Count state (see [Section 4.2.49.3](index-en.html#UUID-604f7ad9-8618-da8f-cf30-edd183f08c66 "4.2.49.3. SAR Acknowledgment Retransmissions Count")).
* The SAR_Receiver_Segment_Interval_Step field shall be set to the current SAR Receiver Segment Interval Step (see [Section 4.2.49.5](index-en.html#UUID-cb59ec2b-0564-e693-a2b2-498e11382769 "4.2.49.5. SAR Receiver Segment Interval Step")).

#### 4.4.16. SAR Configuration Client model

##### 4.4.16.1. Description

The SAR Configuration Client model is used to support the functionality of configuring the behavior of the lower transport layer of a node that supports the SAR Configuration Server model.

The SAR Configuration Client model is a root model and a main model that does not extend any other models. The SAR Configuration Client model may operate on states defined by the SAR Configuration Server model (see [Section 4.4.15](index-en.html#UUID-0819a78a-3843-e234-4f74-95ae1d357c0c "4.4.15. SAR Configuration Server model")) using SAR Configuration messages (see [Section 4.3.8](index-en.html#UUID-4deab493-9bad-8143-144e-0089dd4dce13 "4.3.8. SAR Configuration messages")).

If supported, the SAR Configuration Client model shall be supported by the primary element and shall not be supported by any secondary elements. The access layer security on the SAR Configuration Client model shall use the device key of the node supporting the SAR Configuration Server model.

[Table 4.371](index-en.html#UUID-fe5d7684-8b59-2693-e503-73871eee503e_Table_4.371 "Table 4.371. SAR Configuration Client model messages") lists the SAR Configuration Client model messages. The model shall support receiving the messages marked as mandatory in the
Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| SAR Configuration Main (Primary) | SAR Configuration Client | SAR Transmitter | SAR_TRANSMITTER_GET | – | M |
| SAR_TRANSMITTER_SET | – | M |
| SAR_TRANSMITTER_STATUS | M | – |
| SAR Receiver | SAR_RECEIVER_GET | – | M |
| SAR_RECEIVER_SET | – | M |
| SAR_RECEIVER_STATUS | M | – |

Table 4.371. SAR Configuration Client model messages

##### 4.4.16.2. Behavior

This section describes behaviors for procedures and messages for the SAR Configuration Client model.

An element can send any SAR Configuration Client message at any time to query or change the states supported by the SAR Configuration Server model of a peer node.

###### 4.4.16.2.1. SAR Transmitter procedure

To determine the SAR Transmit state of a SAR Configuration Server, a SAR Configuration Client shall send a SAR_TRANSMITTER_GET message. The response to the message is a SAR_TRANSMITTER_STATUS message that contains the value of the SAR Transmitter state.

To set the SAR Transmitter state of a SAR Configuration Server with acknowledgment, a SAR Configuration Client shall send a SAR_TRANSMITTER_SET message. The response to the message is a SAR_TRANSMITTER_STATUS message that contains the value of the SAR Transmitter state.

Upon receiving a SAR_TRANSMITTER_STATUS message, a SAR Configuration Client can determine the current SAR Transmitter state of a SAR Configuration Server.

###### 4.4.16.2.2. SAR Receiver procedure

To determine the SAR Receiver state of a SAR Configuration Server, a SAR Configuration Client shall send a SAR_RECEIVER_GET message. The response to the message is a SAR_RECEIVER_STATUS message that contains the value of the SAR Receiver state.

To set the SAR Receiver state of a SAR Configuration Server with acknowledgment, a SAR Configuration Client shall send a SAR_RECEIVER_SET message. The response to the message is a SAR_RECEIVER_STATUS message that contains the value of the SAR Receiver state.

Upon receiving a SAR_RECEIVER_STATUS message, a SAR Configuration Client can determine the current SAR Receiver state of a SAR Configuration Server.

#### 4.4.17. Solicitation PDU RPL Configuration Server model

##### 4.4.17.1. Description

The Solicitation PDU RPL Configuration Server model is used to support the functionality of removing items from the solicitation replay protection list of a node.

The Solicitation PDU RPL Configuration Server model corresponds with the On-Demand Private Proxy Server model (see [Section 4.4.13](index-en.html#UUID-c50312c6-d68d-0472-0e62-d2f09c0e600a "4.4.13. On-Demand Private Proxy Server model")).

If supported, the Solicitation PDU RPL Configuration Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Solicitation PDU RPL Configuration Server model shall use the application key.

By using an application key, a multicast address may be used as a destination address for the messages defined by this model.

This model does not define any states.

[Table 4.372](index-en.html#UUID-734785af-aa36-39df-9d82-f46bd17cf5a7_Table_4.372 "Table 4.372. Solicitation PDU RPL Configuration Server model messages") lists the Solicitation PDU RPL Configuration Server model messages. The model shall support receiving the
messages marked as mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Solicitation PDU RPL Configuration Main (Primary) | Solicitation PDU RPL Configuration Server | – | SOLICITATION_PDU_­RPL_­ITEM_­CLEAR | M | – |
| SOLICITATION_PDU_­RPL_­ITEM_­CLEAR_­UNACKNOWLEDGED | M | – |
| SOLICITATION_PDU_­RPL_­ITEM_­STATUS | – | M |

Table 4.372. Solicitation PDU RPL Configuration Server model messages

##### 4.4.17.2. Behavior

This section describes behaviors for messages for the Solicitation PDU RPL Configuration Server model.

###### 4.4.17.2.1. Receiving a SOLICITATION_PDU_RPL_ITEM_CLEAR message

When an element receives a SOLICITATION_PDU_RPL_ITEM_CLEAR message, it shall clear the solicitation replay protection list items corresponding to the addresses indicated in the Address_Range field and shall respond with a SOLICITATION_PDU_RPL_ITEM_STATUS message with the Address_Range field copied from the
SOLICITATION_PDU_RPL_ITEM_CLEAR message.

###### 4.4.17.2.2. Receiving a SOLICITATION_PDU_RPL_ITEM_CLEAR_UNACKNOWLEDGED message

When an element receives a SOLICITATION_PDU_RPL_ITEM_CLEAR_UNACKNOWLEDGED message, it shall clear the solicitation replay protection list items corresponding to the addresses indicated in the Address_Range field.

#### 4.4.18. Solicitation PDU RPL Configuration Client model

##### 4.4.18.1. Description

The Solicitation PDU RPL Configuration Client model is used to support the functionality of removing addresses from the solicitation replay protection list of a node that supports the Solicitation PDU RPL Configuration Server model. A Configuration Manager can use the Solicitation PDU RPL Configuration Client model to remove
from the solicitation replay protection list the addresses that have been reassigned to a new node after a node was removed from the network.

The Solicitation PDU RPL Configuration Client model is a root model and a main model that does not extend any other models. The Solicitation PDU RPL Configuration Client model may be used to remove items from a solicitation replay protection list of a peer node by using Solicitation PDU RPL Configuration messages (see
[Section 4.3.7](index-en.html#UUID-8c82b677-8e9b-44b6-e271-bd83404f2b3d "4.3.7. Solicitation PDU RPL Configuration messages")).

If supported, the Solicitation PDU RPL Configuration Client model shall be supported by the primary element and shall not be supported by any secondary elements. The access layer security on the Solicitation PDU RPL Configuration Client model shall use the application key.

[Table 4.373](index-en.html#UUID-92446ea8-ca2b-ae39-b5c9-5c7a156af132_Table_4.373 "Table 4.373. Solicitation PDU RPL Configuration Client model messages") lists the Solicitation PDU RPL Configuration Client model messages. The model shall support receiving the
messages marked as mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Solicitation PDU RPL Configuration Main (Primary) | Solicitation PDU RPL Configuration Client | Solicitation PDU RPL Items Clear | SOLICITATION_PDU_­RPL_­ITEM_­CLEAR | – | M |
| SOLICITATION_PDU_­RPL_­ITEM_­CLEAR_­UNACKNOWLEDGED | – | M |
| SOLICITATION_PDU_­RPL_­ITEM_­STATUS | M | – |

Table 4.373. Solicitation PDU RPL Configuration Client model messages

##### 4.4.18.2. Behavior

This section describes behaviors for procedures and messages for the Solicitation PDU RPL Configuration Client model.

###### 4.4.18.2.1. Solicitation PDU RPL Items Clear procedure

An element can send a SOLICITATION_PDU_RPL_ITEM_CLEAR message or a SOLICITATION_PDU_RPL_ITEM_CLEAR_UNACKNOWLEDGED message at any time to clear a range of addresses indicated by the Address_Range field from of solicitation replay protection list.

To clear a range of addresses from a solicitation replay protection list, a Solicitation PDU RPL Configuration Client shall send a SOLICITATION_PDU_RPL_ITEM_CLEAR or a SOLICITATION_PDU_RPL_ITEM_CLEAR_UNACKNOWLEDGED message. The response to the SOLICITATION_PDU_RPL_ITEM_CLEAR message is a SOLICITATION_PDU_RPL_ITEM_STATUS
message.

#### 4.4.19. Opcodes Aggregator Server model

##### 4.4.19.1. Description

The Opcodes Aggregator Server model is used to support the functionality of processing a sequence of access layer messages.

The Opcodes Aggregator Server model is a root model that does not extend any other models.

If supported, the Opcodes Aggregator Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Opcodes Aggregator Server model shall use the device key and application keys.

This model does not define any states.

[Table 4.374](index-en.html#UUID-30fbf0c9-b64b-fec4-d06a-40a202db8d71_Table_4.374 "Table 4.374. Opcodes Aggregator Server model messages") lists the Opcodes Aggregator Server model messages. The model shall support receiving the messages marked as mandatory in the
Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Opcodes Aggregator Main (Primary) | Opcodes Aggregator Server | – | OPCODES_AGGREGATOR_­SEQUENCE | M | – |
| OPCODES_AGGREGATOR_­STATUS | – | M |

Table 4.374. Opcodes Aggregator Server model messages

##### 4.4.19.2. Behavior

###### 4.4.19.2.1. Message Request List Processing procedure

The Message Request List Processing procedure is used to process a list of Access messages and collects response messages in a message results list.

As an input, the procedure takes an element and a message request list. The message request list is an ordered list of Access messages contained in the Items field in an OPCODES_AGGREGATOR_SEQUENCE message. The model instance is identified by the Element_Address field and the opcode from each entry of the Items field in an
OPCODES_AGGREGATOR_SEQUENCE message.

The procedure is complete when all Access messages have been successfully processed or when processing of a message results in an error condition in [Table 4.375](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28_Table_4.375 "Table 4.375. Error conditions for the message results list"). The procedure completes with a status code that reflects the result of the operation. This status is then reported in an OPCODES_AGGREGATOR_STATUS message.

The procedure operates on the message request lists and determines a message results list. The message results list is an ordered list of Access messages that result from processing Access messages from a message request list.

When an Access message or an empty item is added to the message results list, it shall be located at the same index as the corresponding Access message from the message request list. When more than one Access message is generated as a result of single Access message processing (such as messages generated as a result of state
change publication), only the response message shall be added to the message results list; the other generated messages shall be ignored.

Access messages from the message request list shall be processed in the order in which they appear in the list, starting with the Access message located at index 0. The Access message within an item and the Element_Address field uniquely identify the model instance on a node.

Each Access message shall be processed by performing the following steps:

1. When an Access message with an opcode identifying an acknowledged message is successfully processed by the identified model, the resulting Access message shall be added to the message results list.
2. When an Access message with an opcode identifying an unacknowledged message is successfully processed by the identified model, the empty item shall be added to the message results list.
3. When an Access message is not successfully processed by the identified model (i.e., it results in any of the error conditions in [Table 4.375](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28_Table_4.375 "Table 4.375. Error conditions for the message results list")), processing of the message request list shall stop, and the procedure shall be completed by returning the current message results list and the Status set to the error condition that was encountered as defined in [Table 4.375](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28_Table_4.375 "Table 4.375. Error conditions for the message results list").
4. When an Access message with an opcode identifying an acknowledged message is successfully processed by the identified model, but the resulting Access message cannot be added to the message results list due to the message results list becoming too large to be transported in a single OPCODES_AGGREGATOR_STATUS message,
   the resulting Access message shall not be added to the message results list, processing of the message request list shall stop, and the procedure shall be completed by returning the current message results list and the Status set to ResponseOverflow.
5. When an Access message with an opcode identifying an unacknowledged message is successfully processed by the identified model, but an empty item cannot be added to the message results list due to the message results list becoming too large to be transported in a single OPCODES_AGGREGATOR_STATUS message, the empty item
   shall not be added to the message results list, processing of the message request list shall stop, and the procedure shall be completed by returning the current message results list and the Status set to ResponseOverflow.
6. When all Access messages are successfully processed by the identified model, the procedure shall be completed by returning the message results list and the Status set to Success.

| Error Condition | Status Code Name  (see [Table 4.309](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.309 "Table 4.309. Summary of status codes for Opcodes Aggregator messages ")) |
| --- | --- |
| The OPCODES_AGGREGATOR_SEQUENCE message is encrypted with an application key, and the identified model is not bound to the same application key, or the identified model’s access layer security is not using application keys. | WrongAccessKey |
| The OPCODES_AGGREGATOR_SEQUENCE message is encrypted with a device key, and the identified model’s access layer security is not using a device key. | WrongAccessKey |
| An Access message has an opcode that is not supported by any of the models on the element identified by the Element_Address field of the OPCODES_AGGREGATOR_SEQUENCE message. | WrongOpCode |
| An Access message has a valid opcode but is not understood by the identified model (see [Section 3.7.3.4](index-en.html#UUID-3fad2ba1-effb-ca5c-3d33-e342dbb8da6d "3.7.3.4. Message error procedure")) | MessageNotUnderstood |

Table 4.375. Error conditions for the message results list

### Note on Opcodes Aggregator Key Binding

Note: The error conditions in [Table 4.375](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28_Table_4.375 "Table 4.375. Error conditions for the message results list") imply that the Opcodes Aggregator Server model is implicitly bound to the node’s
device key. Additionally, the Configuration Manager should bind the same application key to the Opcodes Aggregator Server model and to one or more desired models on one or more elements on a node for which the OPCODES_AGGREGATOR_SEQUENCE message will be sent; otherwise, the Opcodes Aggregator Server could encounter the
WrongAccessKey error condition while executing this procedure.

###### 4.4.19.2.2. Receiving an OPCODES_AGGREGATOR_SEQUENCE message

When an Opcodes Aggregator Server receives an OPCODES_AGGREGATOR_SEQUENCE message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.376](index-en.html#UUID-123fded0-df65-0360-ce78-5aa007e7ba21_Table_4.376 "Table 4.376. Error conditions for the OPCODES_AGGREGATOR_SEQUENCE message")), the server shall populate the message request list with items copied from the OPCODES_AGGREGATOR_SEQUENCE message and shall clear the message results list. The order of the items in the message request list shall be the
same as in the OPCODES_AGGREGATOR_SEQUENCE message. The Element_Address field and opcode of Item #0 shall identify the model for all the items.

When an Opcodes AggregatorIn Server receives an OPCODES_AGGREGATOR_SEQUENCE message that is not successfully processed (i.e., the error conditions are checked, starting from the first row of [Table 4.376](index-en.html#UUID-123fded0-df65-0360-ce78-5aa007e7ba21_Table_4.376 "Table 4.376. Error conditions for the OPCODES_AGGREGATOR_SEQUENCE message"), and an error condition is satisfied), the server shall respond with an OPCODES_AGGREGATOR_STATUS message with the Status field set to the status code corresponding to the error condition as defined in [Table 4.376](index-en.html#UUID-123fded0-df65-0360-ce78-5aa007e7ba21_Table_4.376 "Table 4.376. Error conditions for the OPCODES_AGGREGATOR_SEQUENCE message").

| Error Condition | Status Code Name  (see [Table 4.309](index-en.html#UUID-fe79327d-9bea-3bb7-3a40-8c3030e12cc6_Table_4.309 "Table 4.309. Summary of status codes for Opcodes Aggregator messages ")) |
| --- | --- |
| The unicast address provided in the Element_Address field is not known to the node. | Invalid Address |

Table 4.376. Error conditions for the OPCODES_AGGREGATOR_SEQUENCE message

When an Opcodes Aggregator Server receives an OPCODES_AGGREGATOR_SEQUENCE message that is successfully processed (i.e., it does not result in any error condition listed in [Table 4.376](index-en.html#UUID-123fded0-df65-0360-ce78-5aa007e7ba21_Table_4.376 "Table 4.376. Error conditions for the OPCODES_AGGREGATOR_SEQUENCE message")), the server shall start a Message Request List Processing procedure, as defined in [Section 4.4.19.2.1](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28 "4.4.19.2.1. Message Request List Processing procedure"), and shall respond with an OPCODES_AGGREGATOR_STATUS message with the Status field set as defined in [Section 4.4.19.2.1](index-en.html#UUID-d4e57d79-5b93-f02d-954a-8ea233a79b28 "4.4.19.2.1. Message Request List Processing procedure").

###### 4.4.19.2.3. Sending an OPCODES_AGGREGATOR_STATUS message

When the Opcodes Aggregator Server sends an OPCODES_AGGREGATOR_STATUS message, the Status field shall be set as defined in [Section 4.4.19.2.2](index-en.html#UUID-123fded0-df65-0360-ce78-5aa007e7ba21 "4.4.19.2.2. Receiving an OPCODES_AGGREGATOR_SEQUENCE message"),
the Element_Address field shall be set as in the corresponding OPCODES_AGGREGATOR_SEQUENCE message, and the Status_Items field shall be set to items in the message results list, in the same order as in the message results list.

###### 4.4.19.2.4. Example of OPCODES_AGGREGATOR_SEQUENCE message processing

[Figure 4.10](index-en.html#UUID-2f261bc2-af7a-2aae-7d84-4d1915dc1cec_Figure_4.10 "Figure 4.10. Example of OPCODES_AGGREGATOR_SEQUENCE message processing") shows how the OPCODES_AGGREGATOR_SEQUENCE message is processed when the message has the following
configuration:

* The message identifies an element N.
* The message contains four items:

  * Item A: an Access message with an opcode identifying an acknowledged message for model Z
  * Item B: an Access message with an opcode identifying an unacknowledged message for model Z
  * Item C: an Access message with parameters not understood by element N
  * Item D: an Access message with an opcode identifying an acknowledged message for model Z

Because the items are processed sequentially, items A and B will be processed successfully, item C will result in a processing error, and item D will not be processed.

In this case the OPCODES_AGGREGATOR_STATUS message is sent in response to the OPCODES_AGGREGATOR_SEQUENCE message and has the following configuration:

* The Status field is set to MessageNotUnderstood.
* The Element_Address field is set to the value of the Element_Address field in the OPCODES_AGGREGATOR_SEQUENCE message.
* The number of reported items in the OPCODES_AGGREGATOR_STATUS message (see [Section 4.3.9.3](index-en.html#UUID-d2fc676d-d3de-804c-321b-c4bb5cc6bee0 "4.3.9.3. OPCODES_AGGREGATOR_STATUS")) is 2, as shown in [Figure 4.10](index-en.html#UUID-2f261bc2-af7a-2aae-7d84-4d1915dc1cec_Figure_4.10 "Figure 4.10. Example of OPCODES_AGGREGATOR_SEQUENCE message processing"). Status_Items element #0 is set to the response to item A, and Status_Items element #1 is set to an empty item.

|  |
| --- |
| Example of OPCODES_AGGREGATOR_SEQUENCE message processing |

Figure 4.10. Example of OPCODES_AGGREGATOR_SEQUENCE message processing

#### 4.4.20. Opcodes Aggregator Client model

##### 4.4.20.1. Description

The Opcodes Aggregator Client model is used to support the functionality of dispatching a sequence of access layer messages to nodes supporting the Opcodes Aggregator Server model.

The Opcodes Aggregator Client model is a root model and a main model that does not extend any other models.

If supported, the Opcodes Aggregator Client shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Opcodes Aggregator Client model shall use the device key and application keys.

[Table 4.377](index-en.html#UUID-4314a8d2-b4e4-b424-5727-3685b2826657_Table_4.377 "Table 4.377. Opcodes Aggregator Client model messages") lists the Opcodes Aggregator Client model messages. The model shall support receiving the messages marked as mandatory in the
Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Opcodes Aggregator Main  (Primary) | Opcodes Aggregator Client | Dispatch sequence of Access messages | OPCODES_AGGREGATOR_­SEQUENCE | – | M |
| OPCODES_AGGREGATOR_­STATUS | M | – |

Table 4.377. Opcodes Aggregator Client model messages

##### 4.4.20.2. Behavior

###### 4.4.20.2.1. Dispatch sequence of Access messages procedure

To dispatch a sequence of Access messages to an Opcodes Aggregator Server, an Opcodes Aggregator Client shall send an OPCODES_AGGREGATOR_SEQUENCE message. The response is an OPCODES_AGGREGATOR_STATUS message.

Upon receiving an OPCODES_AGGREGATOR_STATUS message, an Opcodes Aggregator Client can determine the following:

* the status, which can be either a Success or an error
* the index of the most recent Access message delivered to the Opcodes Aggregator Server
* the number of successfully processed Access messages from the list
* one or more Access messages sent as a result of the processing of Access messages.

If the status is Success, the Status is set to Success. If the status is an error or processing of one Access message resulted in error, the Status field contains the error condition.

When constructing an OPCODES_AGGREGATOR_SEQUENCE message, the Opcodes Aggregator Client should avoid the situation where the response Access messages would become too large to be transported in a single OPCODES_AGGREGATOR_STATUS message. The Opcodes Aggregator Client should consider the lengths of the response Access
messages it will receive, and when necessary, send multiple OPCODES_AGGREGATOR_SEQUENCE messages instead of one.

#### 4.4.21. Large Composition Data Server model

##### 4.4.21.1. Description

The Large Composition Data Server model is used to support the functionality of exposing pages of Composition Data that do not fit in a Config Composition Data Status message (see [Section 4.3.2.5](index-en.html#UUID-333f1590-4676-e6c8-d91a-6b8006fbb01d "4.3.2.5. Config Composition Data Status")) and to expose metadata of the model instances.

The Large Composition Data Server is a main model that extends the Configuration Server model (see [Section 4.4.1](index-en.html#UUID-983db022-d6e3-ac72-0296-26a0d31afc91 "4.4.1. Configuration Server model")).

The Large Composition Data Server model defines the state instances listed in [Table 4.378](index-en.html#UUID-443cca33-9b56-a4e4-ec83-65219f9ee498_Table_4.378 "Table 4.378. Large Composition Data Server model states and bindings") and the messages listed in
[Table 4.379](index-en.html#UUID-443cca33-9b56-a4e4-ec83-65219f9ee498_Table_4.379 "Table 4.379. Large Composition Data Server model messages").

If supported, the Large Composition Data Server model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security on the Large Composition Data Server model shall use the device key.

[Table 4.378](index-en.html#UUID-443cca33-9b56-a4e4-ec83-65219f9ee498_Table_4.378 "Table 4.378. Large Composition Data Server model states and bindings") illustrates the state bindings between the Large Composition Data Server model states and the states of the
models that the Large Composition Data Server extends.

| State | Bound State | |
| --- | --- | --- |
| Model | State |
| Models Metadata Page | – | – |

Table 4.378. Large Composition Data Server model states and bindings

[Table 4.379](index-en.html#UUID-443cca33-9b56-a4e4-ec83-65219f9ee498_Table_4.379 "Table 4.379. Large Composition Data Server model messages") lists the Large Composition Data Server model messages. The model shall support receiving the messages marked as
mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | State | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Large Composition Data Main  (Primary) | Large Composition Data Server | – | LARGE_COMPOSITION_­DATA_­GET | M | – |
| LARGE_COMPOSITION_­DATA_­STATUS | – | M |
| Models Metadata Page | MODELS_METADATA_­GET | M | – |
| MODELS_METADATA_­STATUS | – | M |

Table 4.379. Large Composition Data Server model messages

##### 4.4.21.2. Behavior

This section describes behaviors for states and messages for the Large Composition Data Server model.

###### 4.4.21.2.1. Large Composition Data

When an element receives a LARGE_COMPOSITION_DATA_GET message with the Page field of the message containing a value of a Composition Data Page that the node contains, the element shall respond with a LARGE_COMPOSITION_DATA_STATUS message. The LARGE_COMPOSITION_DATA_STATUS message shall have the following configuration:

* The Page field and the Offset field shall be set to the values of the corresponding fields in the LARGE_COMPOSITION_DATA_GET message.
* The Total_Size field shall be set to the total size of the identified Composition Data Page.
* If the Offset field value is less than the Total_Size field value, the Data field shall be set to the value of the portion of the identified Composition Data Page that fits in the Data field, starting from the position in number of octets indicated by the Offset field value. Otherwise, the Data field shall be
  empty.

When an element receives a LARGE_COMPOSITION_DATA_GET message with the Page field of the message containing a reserved page number or a page number the node does not support, it shall respond with a LARGE_COMPOSITION_DATA_STATUS message.

The response page is the page with the largest page number of the Composition Data that the node supports and that is smaller than the Page field value of the received LARGE_COMPOSITION_DATA_GET message.

The LARGE_COMPOSITION_DATA_STATUS message shall have the following configuration:

* The Page field shall be set to the response page number.
* The Offset field shall be set to the value of the corresponding field in the LARGE_COMPOSITION_DATA_GET message.
* The Total_Size field shall be set to the total size of the response page.
* If the Offset field value is less than the Total_Size field value, the Data field shall be set to the portion of the response page, starting from the position in number of octets indicated by the Offset field value. Otherwise, the Data field shall be empty.

###### 4.4.21.2.2. Models Metadata Page state

When an element receives a MODELS_METADATA_GET message, the Large Composition Data Server model shall identify the requested Models Metadata Page and shall respond with a MODELS_METADATA_STATUS message containing the value of the requested Models Metadata Page state.

The Large Composition Data Server model shall identify the response Models Metadata Page state using the following conditions:

* If the Page field of the message identifies a Models Metadata Page state that is present on the node, the response Models Metadata Page state is set to the identified Models Metadata Page state.
* If the Page field of the message does not identify any Models Metadata Page state present on the node, the response Models Metadata Page state is set to the highest Models Metadata Page state that is smaller than the Page field value.

When sending the MODELS_METADATA_STATUS message, the message shall have the following configuration:

* The Page field shall be set to the value of the response Models Metadata Page number and the Offset field shall be set to the value of the Offset field of the MODELS_METADATA _GET message.
* The Total_Size field shall be set to the total size of the response Models Metadata Page state.
* If the Offset field value is less than the Total_Size field value, the Data field shall be set to the value of the portion of the response Models Metadata Page state that fits in the Data field, starting from the octet position indicated by the Offset field value. Otherwise, the Data field shall be empty.

#### 4.4.22. Large Composition Data Client model

##### 4.4.22.1. Description

The Large Composition Data Client model is used to support the functionality of reading pages of Composition Data that do not fit in a Config Composition Data Status message (see [Section 4.3.2.5](index-en.html#UUID-333f1590-4676-e6c8-d91a-6b8006fbb01d "4.3.2.5. Config Composition Data Status")) and reading the metadata of the model instances.

The Large Composition Data Client model is a root model that does not extend any other models. The Large Composition Data Client model may operate on states defined by the Large Composition Data Server model (see [Section 4.4.21](index-en.html#UUID-8a446433-55e4-3763-bc4b-53efb2955beb "4.4.21. Large Composition Data Server model")) using Large Composition Data messages (see [Section 4.3.10](index-en.html#UUID-4bda503f-6818-9f1e-9153-ec078dfd3e64 "4.3.10. Large Composition Data messages")).

If supported, the Large Composition Data Client model shall be supported by a primary element and shall not be supported by any secondary elements. The access layer security of the Large Composition Data Client model shall use the device key of the node supporting the Large Composition Data Server model.

[Table 4.380](index-en.html#UUID-62dc7c1d-82f6-e00e-cf99-f085dd81e0f7_Table_4.380 "Table 4.380. Large Composition Data Client model messages") lists the Large Composition Data Client model messages. The model shall support receiving the messages marked as
mandatory in the Rx column and shall support sending the messages marked as mandatory in the Tx column.

| Element | Model Name | Procedure | Message | Rx | Tx |
| --- | --- | --- | --- | --- | --- |
| Large Composition Data Main  (Primary) | Large Composition Data Client | Large Composition Data | LARGE_COMPOSITION_­DATA_­GET | – | M |
| LARGE_COMPOSITION_­DATA_­STATUS | M | – |

Table 4.380. Large Composition Data Client model messages

##### 4.4.22.2. Behavior

This section describes behaviors for procedures and messages for the Large Composition Data Client model.

An element can send a LARGE_COMPOSITION_DATA_GET message at any time to query the Composition Data state of a node and can send a MODELS_METADATA_GET message at any time to query the Models Metadata state of a node. Messages for the Large Composition Data Client and Server models shall be secured using a DevKey.

###### 4.4.22.2.1. Large Composition Data procedure

To find out a portion of a page of the Composition Data state of the Large Composition Data Server, a Large Composition Data Client shall send a LARGE_COMPOSITION_DATA_GET message. The response is a LARGE_COMPOSITION_DATA_STATUS message that contains the requested portion of the page and the total size of the page.

Upon receiving a LARGE_COMPOSITION_DATA_STATUS message, a Large Composition Data Client can determine a portion or the entire value of the requested Composition Data Page state of a Large Composition Data Server.

###### 4.4.22.2.2. Models Metadata procedure

To find out a portion of a page of the Models Metadata state of the Large Composition Data Server, a Large Composition Data Client shall send a MODELS_METADATA_GET message. The response is a MODELS_METADATA_STATUS message that contains the requested portion of the page and the total size of the page.

Upon receiving a MODELS_METADATA_STATUS message, a Large Composition Data Client can determine a portion or the entire value of the requested Models Metadata Page state of a Large Composition Data Server.

#### 4.4.23. Summary of Model IDs

The Model IDs for the models that are defined in this specification are defined in the Assigned Numbers document [[4](index-en.html#idp254746)].
