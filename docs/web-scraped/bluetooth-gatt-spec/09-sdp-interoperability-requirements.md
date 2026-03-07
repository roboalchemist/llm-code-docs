# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 9. SDP interoperability requirements

A device that supports GATT over BR/EDR and only one of ATT or EATT shall publish the SDP record shown in  [Table 9.1](generic-attribute-profile--gatt-.html#UUID-748be175-5220-ddd2-0722-d73c541e0533_table-idm13359013046580 "Table 9.1: SDP record for the Generic Attribute Profile, if only one of ATT or EATT is supported"); if both ATT and EATT are supported, the device shall publish the SDP record shown in  [Table 9.2](generic-attribute-profile--gatt-.html#UUID-748be175-5220-ddd2-0722-d73c541e0533_table-idm13359013396072 "Table 9.2: SDP record for the Generic Attribute Profile, if both ATT and EATT are supported"). The GATT Service Start Handle shall be set to the attribute handle of the «GATT Service» service declaration. The GATT Service End Handle shall be set to the attribute handle of the last attribute within the «GATT Service» service definition group.

| Item | | | Type | Value | Meaning |
| --- | --- | --- | --- | --- | --- |
| Attribute ID | | | uint16 | 0x0001 | ServiceClassIDList |
| Attribute Value | | | Data element sequence (1 item) | | |
|  | Service Class | | UUID | «GATT Service» | |
| Attribute ID | | | uint16 | 0x0004 | ProtocolDescriptorList |
| Attribute Value | | | Data element sequence (2 items) | | |
|  | Protocol Descriptor | | Data element sequence (2 items) | | |
|  | | Protocol | UUID | «L2CAP» | |
|  | | Parameter 0 | uint16 | 0x001F  *or* 0x0027 | PSM = ATT  *or* PSM = EATT |
|  | Protocol Descriptor | | Data element sequence (3 items) | | |
|  | | Protocol | UUID | «ATT» | |
|  | | Parameter 0 | uint16 | 0xHHHH | GATT service start handle |
|  | | Parameter 1 | uint16 | 0xHHHH | GATT service end handle |
| Attribute ID | | | uint16 | 0x0005 | BrowseGroupList |
| Attribute Value | | | Data element sequence (1 item) | | |
|  | Group | | UUID | «PublicBrowseRoot» | |

Table 9.1: SDP record for the Generic Attribute Profile, if only one of ATT or EATT is supported

| Item | | | | Type | Value | Meaning |
| --- | --- | --- | --- | --- | --- | --- |
| Attribute ID | | | | uint16 | 0x0001 | ServiceClassIDList |
| Attribute Value | | | | Data element sequence (1 item) | | |
|  | Service class | | | UUID | «GATT Service» | |
| Attribute ID | | | | uint16 | 0x0004 | ProtocolDescriptorList |
| Attribute Value | | | | Data element sequence (2 items) | | |
|  | Protocol Descriptor | | | Data element sequence (2 items) | | |
|  | | Protocol | | UUID | «L2CAP» | |
|  | | Parameter 0 | | uint16 | 0x001F | PSM = ATT |
|  | Protocol Descriptor | | | Data element sequence (3 items) | | |
|  | | Protocol | | UUID | «ATT» | |
|  | | Parameter 0 | | uint16 | 0xHHHH | GATT service start handle |
|  | | Parameter 1 | | uint16 | 0xHHHH | GATT service end handle |
| Attribute ID | | | | uint16 | 0x000D | AdditionalProtocolDescriptorList |
| Attribute Value | | | | Data element sequence (1 item) | | |
|  | Protocol Descriptor List | | | Data element sequence (2 items) | | |
|  | | Protocol Descriptor | | Data element sequence (2 items) | | |
|  | | | Protocol | UUID | «L2CAP» | |
|  | | | Parameter 0 | uint16 | 0x0027 | PSM = EATT |
|  | | Protocol Descriptor | | Data element sequence (3 items) | | |
|  | | | Protocol | UUID | «ATT» | |
|  | | | Parameter 0 | uint16 | 0xHHHH | GATT service start handle |
|  | | | Parameter 1 | uint16 | 0xHHHH | GATT service end handle |
| Attribute ID | | | | uint16 | 0x0005 | BrowseGroupList |
| Attribute Value | | | | Data element sequence (1 item) | | |
|  | Group | | | UUID | «PublicBrowseRoot» | |

Table 9.2: SDP record for the Generic Attribute Profile, if both ATT and EATT are supported
