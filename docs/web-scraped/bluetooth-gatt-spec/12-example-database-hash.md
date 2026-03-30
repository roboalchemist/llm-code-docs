# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## Appendix B. Example Database Hash

[Table B.1](generic-attribute-profile--gatt-.html#UUID-108023e0-a27e-d7ef-85ee-24cc931b63e6_table-idm13359013642564 "Table B.1: Example database") shows how the variable length data *m* for calculating the Database Hash is constructed from an example GATT database. The column *Included in Hash* indicates whether the *Attribute Handle* (H), *Attribute Type* (T), or *Attribute Value* (V) are included in *m*.

| Attribute Handle | Attribute Type | Attribute Value | Notes | Included in Hash | Data Included in m |
| --- | --- | --- | --- | --- | --- |
| 0x0001 | 0x2800 | 0x1800 | Primary Service: GAP Service | HTV | 01 00 00 28 00 18 |
| 0x0002 | 0x2803 | {0x0A, 0x0003, 0x2A00} | Characteristic (Read, Write): Device Name | HTV | 02 00 03 28 0A 03 00 00 2A |
| 0x0003 | 0x2A00 | *any* | Characteristic Value: Device Name | No | *none* |
| 0x0004 | 0x2803 | {0x02, 0x0005, 0x2A01} | Characteristic (Read): Appearance | HTV | 04 00 03 28 02 05 00 01 2A |
| 0x0005 | 0x2A01 | *any* | Characteristic Value: Appearance | No | *none* |
| 0x0006 | 0x2800 | 0x1801 | Primary Service: GATT Service | HTV | 06 00 00 28 01 18 |
| 0x0007 | 0x2803 | {0x20, 0x0008, 0x2A05} | Characteristic (Indicate): Service Changed | HTV | 07 00 03 28 20 08 00 05 2A |
| 0x0008 | 0x2A05 | *any* | Characteristic Value: Service Changed | No | *none* |
| 0x0009 | 0x2902 | 0x0002 | Client Characteristic Configuration Descriptor | HT | 09 00 02 29 |
| 0x000A | 0x2803 | {0x0A, 0x000B, 0x2B29} | Characteristic (Read, Write): Client Supported Features | HTV | 0A 00 03 28 0A 0B 00 29 2B |
| 0x000B | 0x2B29 | *any* | Characteristic Value: Client Supported Features | No | *none* |
| 0x000C | 0x2803 | {0x02, 0x000D, 0x2B2A} | Characteristic (Read): Database Hash | HTV | 0C 00 03 28 02 0D 00 2A 2B |
| 0x000D | 0x2B2A | *any* | Characteristic Value: Database Hash | No | *none* |
| 0x000E | 0x2800 | 0x1808 | Primary Service: Glucose Service | HTV | 0E 00 00 28 08 18 |
| 0x000F | 0x2802 | {0x0014, 0x0016, 0x180F} | Included Service: Battery Service | HTV | 0F 00 02 28 14 00 16 00 0F 18 |
| 0x0010 | 0x2803 | {0xA2, 0x0011, 0x2A18} | Characteristic (Read, Indicate, Extended Properties): Glucose Measurement | HTV | 10 00 03 28 A2 11 00 18 2A |
| 0x0011 | 0x2A18 | *any* | Characteristic Value: Glucose Measurement | No | *none* |
| 0x0012 | 0x2902 | 0x0002 | Client Characteristic Configuration Descriptor | HT | 12 00 02 29 |
| 0x0013 | 0x2900 | 0x0000 | Extended Properties | HTV | 13 00 00 29 00 00 |
| 0x0014 | 0x2801 | 0x180F | Secondary Service: Battery Service | HTV | 14 00 01 28 0F 18 |
| 0x0015 | 0x2803 | {0x02, 0x0016, 0x2A19} | Characteristic (Read):  Battery Level | HTV | 15 00 03 28 02 16 00 19 2A |
| 0x0016 | 0x2A19 | *any* | Characteristic Value: Battery Level | No | *none* |

Table B.1: Example database

The resulting variable length data m divided into blocks M0 to M6 is:

M0: 01000028 00180200 03280A03 00002A04
M1: 00032802 0500012A 06000028 01180700
M2: 03282008 00052A09 0002290A 0003280A
M3: 0B00292B 0C000328 020D002A 2B0E0000
M4: 2808180F 00022814 0016000F 18100003
M5: 28A21100 182A1200 02291300 00290000
M6: 14000128 0F181500 03280216 00192A

The resulting Database Hash is (MSB to LSB):

Database Hash = AES-CMACk(m) = F1 CA 2D 48 EC F5 8B AC 8A
88 30 BB B9 FB A9 90

# Note

Note: The bytes in M0 to M6 and the Database Hash are ordered from the most significant on the left to the least significant on the right.
