# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 8. Sample data

This section provides sample data that can be used to verify implementations. The security keys and the UUIDs provided as sample data shall not be used by implementations.

### 8.1. Security sample data

In this section, all derivations are from the following keys:

|  |  |  |
| --- | --- | --- |
| AppKey | : | 3216d1509884b533248541792b877f98 |
| NetKey | : | f7a2a44f8e8a8029064f173ddc1e2b00 |
| DevKey (1201) | : | 37c612c4a2d337cb7b98355531b3617f |

#### 8.1.1. s1 SALT generation function

The s1 function is used to generate a 128-bit value, typically known as a “salt” from a sequence of octets. In this case, the sequence of octets is the ASCII string ”test”.

|  |  |  |
| --- | --- | --- |
| s1 (test) | : | b73cefbd641ef2ea598c2b6efb62f79c |

#### 8.1.2. k1 function

The k1 function is used to convert some input key material into some output key material that uses two inputs, known as salt and info.

|  |  |  |
| --- | --- | --- |
| k1 N | : | 3216d1509884b533248541792b877f98 |
| k1 SALT | : | 2ba14ffa0df84a2831938d57d276cab4 |
| k1 P | : | 5a09d60797eeb4478aada59db3352a0d |
| k1 T | : | c764bea25cf9738b08956ea3c712d5af |
| k1 | : | f6ed15a8934afbe7d83e8dcb57fcf5d7 |

#### 8.1.3. k2 function (managed flooding)

The k2 function is used to convert the managed flooding security credentials, NetKey as N into the managed flooding security material, NID, EncryptionKey, and PrivacyKey.

|  |  |  |
| --- | --- | --- |
| k2 N | : | f7a2a44f8e8a8029064f173ddc1e2b00 |
| k2 P | : | 00 |
| k2 s1(smk2) | : | 4f90480c1871bfbffd16971f4d8d10b1 |
| k2 T | : | 2ea6467aa3378c4c545eda62935b9b86 |
| k2 T0 | : |  |
| k2 T1 | : | 82bea685dc2f1deec255ac643741f5ff |
| k2 T2 | : | 9f589181a0f50de73c8070c7a6d27f46 |
| k2 T3 | : | 4c715bd4a64b938f99b453351653124f |
| NID | : | 7f |
| EncryptionKey | : | 9f589181a0f50de73c8070c7a6d27f46 |
| PrivacyKey | : | 4c715bd4a64b938f99b453351653124f |

#### 8.1.4. k2 function (friendship)

The k2 function is also used to convert the friendship security credentials, NetKey as N, LPNAddress, FriendAddress, LPNCounter, and FriendCounter into the friendship security material, NID, EncryptionKey, and PrivacyKey.

|  |  |  |
| --- | --- | --- |
| LPNAddress | : | 0203 |
| FriendAddress | : | 0405 |
| LPNCounter | : | 0607 |
| FriendCounter | : | 0809 |
| k2 N | : | f7a2a44f8e8a8029064f173ddc1e2b00 |
| k2 P | : | 010203040506070809 |
| k2 s1(smk2) | : | 4f90480c1871bfbffd16971f4d8d10b1 |
| k2 T | : | 2ea6467aa3378c4c545eda62935b9b86 |
| k2 T0 | : |  |
| k2 T1 | : | 3a6b950f56718c1eab2c600a92d4e9f3 |
| k2 T2 | : | 11efec0642774992510fb5929646df49 |
| k2 T3 | : | d4d7cc0dfa772d836a8df9df5510d7a7 |
| NID | : | 73 |
| EncryptionKey | : | 11efec0642774992510fb5929646df49 |
| PrivacyKey | : | d4d7cc0dfa772d836a8df9df5510d7a7 |

#### 8.1.5. k3 function

The k3 function is used to generate a 64-bit Network ID used to identify the mesh network in public messages such as a Secure Network beacon.

|  |  |  |
| --- | --- | --- |
| k3 N | : | f7a2a44f8e8a8029064f173ddc1e2b00 |
| k3 SALT | : | 0036443503f195cc8a716e136291c302 |
| k3 T | : | 6da9698c95f500e4edce3bb47f92754f |
| k3 CMAC(“id64”||0x01) | : | 3527c5985f0c05ccff046958233db014 |
| Network ID | : | ff046958233db014 |

#### 8.1.6. k4 function

The k4 function is used to generate an AID from an application key.

|  |  |  |
| --- | --- | --- |
| k4 N | : | 3216d1509884b533248541792b877f98 |
| k4 SALT | : | 0e9ac1b7cefa66874c97ee54ac5f49be |
| k4 T | : | 62e5d9240cdb3bb0b2743207ea2d6276 |
| k4 CMAC(“id6”||0x01) | : | 1431ea1afeb05224ab892a0217ccab38 |
| AID | : | 38 |

### 8.2. Mesh key derivation sample data

In this section, all derivations are from the following keys. These are the same keys used in the mesh message sample data.

|  |  |  |
| --- | --- | --- |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| DevKey (1201) | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |

#### 8.2.1. Application key AID

The application key’s AID is calculated using the k4 function.

|  |  |  |
| --- | --- | --- |
| k4 N | : | 63964771734fbd76e3b40519d1d94a48 |
| k4 SALT | : | 0e9ac1b7cefa66874c97ee54ac5f49be |
| k4 T | : | 921cb4f908cc5932e1d7b059fc163ce6 |
| k4 CMAC(“id6”||0x01) | : | 5f79cf09bbdab560e7f1ee404fd341a6 |
| AID | : | 26 |

#### 8.2.2. EncryptionKey and PrivacyKey (managed flooding)

The NID, EncryptionKey, and PrivacyKey for a normal mesh message sent using the managed flooding security credentials.

|  |  |  |
| --- | --- | --- |
| k2 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k2 P | : | 00 |
| k2 s1(smk2) | : | 4f90480c1871bfbffd16971f4d8d10b1 |
| k2 T | : | 39885e0463bafd54ca6e495b1001515a |
| k2 T0 | : |  |
| k2 T1 | : | 88dad4892e81fecbe061ebd3fb093268 |
| k2 T2 | : | 0953fa93e7caac9638f58820220a398e |
| k2 T3 | : | 8b84eedec100067d670971dd2aa700cf |
| NID | : | 68 |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf |

#### 8.2.3. EncryptionKey and PrivacyKey (friendship)

The NID, EncryptionKey, and PrivacyKey for a mesh message between a Friend node and a Low Power node sent using the friendship security credentials.

|  |  |  |
| --- | --- | --- |
| LPNAddress | : | 1201 |
| FriendAddress | : | 2345 |
| LPNCounter | : | 0000 |
| FriendCounter | : | 072f |
| k2 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k2 P | : | 01120123450000072f |
| k2 s1(smk2) | : | 4f90480c1871bfbffd16971f4d8d10b1 |
| k2 T | : | 39885e0463bafd54ca6e495b1001515a |
| k2 T0 | : |  |
| k2 T1 | : | d91a3b3c63b5c50a98c838e52a4bc0de |
| k2 T2 | : | be635105434859f484fc798e043ce40e |
| k2 T3 | : | 5d396d4b54d3cbafe943e051fe9a4eb8 |
| NID | : | 5e |
| EncryptionKey | : | be635105434859f484fc798e043ce40e |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 |

#### 8.2.4. EncryptionKey and PrivacyKey (Directed)

The NID, EncryptionKey, and PrivacyKey for a mesh message between two Directed Forwarding nodes sent using the directed security credentials.

|  |  |  |
| --- | --- | --- |
| k2 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k2 P | : | 02 |
| k2 s1(smk2) | : | 4f90480c1871bfbffd16971f4d8d10b1 |
| k2 T | : | 39885e0463bafd54ca6e495b1001515a |
| k2 T0 | : |  |
| k2 T1 | : | c9521c6bb2e56117ecffbdf9aa77b70d |
| k2 T2 | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 |
| k2 T3 | : | 9bf7ab5a5ad415fbd77e07bb808f4865 |
| NID | : | 0d |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 |

#### 8.2.5. Network ID

The Network ID used to identify this NetKey, for example, in a Secure Network beacon.

|  |  |  |
| --- | --- | --- |
| k3 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k3 SALT | : | 0036443503f195cc8a716e136291c302 |
| k3 T | : | 36b82fd0fc400e797977bd12d08a4782 |
| k3 CMAC(“id64”||0x01) | : | ca296bcee3ccc2d33ecaff672f673370 |
| Network ID | : | 3ecaff672f673370 |

#### 8.2.6. IdentityKey

The Identify key used to help identify the device in the Mesh Proxy Service’s Service Data using Node Identity.

|  |  |  |
| --- | --- | --- |
| k1 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k1 SALT | : | f8795a1aabf182e4f163d86e245e19f4 |
| k1 P | : | 696431323801 |
| k1 T | : | 55efb6c898c2a38bc9bd0a6097bff966 |
| IdentityKey | : | 84396c435ac48560b5965385253e210c |

#### 8.2.7. BeaconKey

The Beacon key is used to help secure the Secure Network beacon.

|  |  |  |
| --- | --- | --- |
| k1 N | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| k1 SALT | : | 2c24619ab793c1233f6e226738393dec |
| k1 P | : | 696431323801 |
| k1 T | : | 829816cd429fde7d238b56d8bf771efb |
| BeaconKey | : | 5423d967da639a99cb02231a83f7d254 |

#### 8.2.8. PrivateBeaconKey

The PrivateBeaconKey is used to help secure the Mesh Private beacon. The samples in the following subsections show examples of PrivateBeaconKey generation from NetKey.

##### 8.2.8.1. Sample #1

|  |  |  |
| --- | --- | --- |
| NetKey | : | 3bbb6f1fbd53e157417f308ce7aec58f |
| k1 P | : | 696431323801 |
| k1 SALT | : | 2c8b71fb5d95e86cfb753bfee3ab934f |
| k1 T | : | 3ce1266ffb0a64fac224f9e46e49ad86 |
| PrivateBeaconKey | : | ca478cdac626b7a8522d7272dd124f26 |

##### 8.2.8.2. Sample #2

|  |  |  |
| --- | --- | --- |
| NetKey | : | db662f48d477740621f5e301cdd69611 |
| k1 P | : | 696431323801 |
| k1 SALT | : | 2c8b71fb5d95e86cfb753bfee3ab934f |
| k1 T | : | 1af86c79ab70760441fa7a96bd452ec9 |
| PrivateBeaconKey | : | 0f30694a3a91b616a48a54701053cb90 |

### 8.3. Mesh message sample data

In this section, all messages are secured using the following keys:

|  |  |  |
| --- | --- | --- |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| DevKey (1201) | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |

The messages below show a typical set of transactions used by a Low Power node that are intended to show multiple examples of mesh messages.

#### 8.3.1. Message #1

This shows an example of a new node that supports the Low Power feature attempting to find a Friend node. It does this by sending a Friend Request with its requirements to the all-friends address using a TTL of zero.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 03 (Friend Request) |
|  | Criteria | : | 4b |
|  | ReceiveDelay | : | 50 |
|  | PollTimeout | : | 057e40 |
|  | PreviousAddress | : | 0000 |
|  | NumElements | : | 01 |
|  | LPNCounter | : | 0000 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 000001 |
| SRC | : | 1201 |
| DST | : | fffd |
| UpperTransportPDU | : | 4b50057e400000010000 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 000001 |
| SRC | : | 1201 |
| DST | : | fffd |
| SEG | : | 00 |
| Opcode | : | 03 |
| Header | : | 03 |
| UpperTransportPDU | : | 4b50057e400000010000 |
| LowerTransportPDU | : | 034b50057e400000010000 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 000001 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | fffd | | | | | | |
| LowerTransportPDU | : | 034b50057e400000010000 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00800000011201000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000001 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | fffd | | |
| TransportPDU | : |  |  |  |  |  | 034b50057e400000010000 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b5e5bfdacbaf6cb7fb6bff871f | | |
| NetMIC | : |  |  |  |  |  |  | 035444ce83a670df |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678b5e5bfdacbaf6c |
| PECB | : | 6ca487507564 |
| CTL||TTL||SEQ||SRC | : | 800000011201 |
|  | | |
| NetworkPDU | : | 68eca487516765b5e5bfdacbaf6cb7fb6bff871f035444ce83a670df |

#### 8.3.2. Message #2

A node that supports the Friend feature responds to the Friend Request with a Friend Offer.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 04 (Friend Offer) |
|  | ReceiveWindow | : | 32 |
|  | QueueSize | : | 03 |
|  | SubListSize | : | 08 |
|  | RSSI | : | ba (-70) |
|  | FriendCounter | : | 072f |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 014820 |
| SRC | : | 2345 |
| DST | : | 1201 |
| UpperTransportPDU | : | 320308ba072f |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 014820 |
| SRC | : | 2345 |
| DST | : | 1201 |
| SEG | : | 00 |
| Opcode | : | 04 |
| Header | : | 04 |
| UpperTransportPDU | : | 320308ba072f |
| LowerTransportPDU | : | 04320308ba072f |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 014820 | | | | | | |
| SRC | : | 2345 | | | | | | |
| DST | : | 1201 | | | | | | |
| LowerTransportPDU | : | 04320308ba072f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00800148202345000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 014820 | | | | |
| SRC | : |  |  |  | 2345 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 04320308ba072f | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 79d7dbc0c9b4d43eeb | | |
| NetMIC | : |  |  |  |  |  |  | ec129d20a620d01e |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 00000000001234567879d7dbc0c9b4d4 |
| PECB | : | 54c96e094e3c |
| CTL||TTL||SEQ||SRC | : | 800148202345 |
|  | | |
| NetworkPDU | : | 68d4c826296d7979d7dbc0c9b4d43eebec129d20a620d01e |

#### 8.3.3. Message #3

Another node supporting the Friend feature responds with another Friend Offer. This Friend Offer has a smaller queue size and a significantly worse RSSI figure than the other Friend Offer message.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 04 (Friend Offer) |
|  | ReceiveWindow | : | fa |
|  | QueueSize | : | 02 |
|  | SubListSize | : | 05 |
|  | RSSI | : | a6 (-90) |
|  | FriendCounter | : | 000a |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 2b3832 |
| SRC | : | 2fe3 |
| DST | : | 1201 |
| UpperTransportPDU | : | fa0205a6000a |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 2b3832 |
| SRC | : | 2fe3 |
| DST | : | 1201 |
| SEG | : | 00 |
| Opcode | : | 04 |
| Header | : | 04 |
| UpperTransportPDU | : | fa0205a6000a |
| LowerTransportPDU | : | 04fa0205a6000a |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 2b3832 | | | | | | |
| SRC | : | 2fe3 | | | | | | |
| DST | : | 1201 | | | | | | |
| LowerTransportPDU | : | 04fa0205a6000a | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00802b38322fe3000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 2b3832 | | | | |
| SRC | : |  |  |  | 2fe3 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 04fa0205a6000a | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 53273086b8c5ee00bd | | |
| NetMIC | : |  |  |  |  |  |  | d9cfcc62a2ddf572 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 00000000001234567853273086b8c5ee |
| PECB | : | 5a2d13fb4211 |
| CTL||TTL||SEQ||SRC | : | 802b38322fe3 |
|  | | |
| NetworkPDU | : | 68da062bc96df253273086b8c5ee00bdd9cfcc62a2ddf572 |

#### 8.3.4. Message #4

The node sends a Friend Poll to confirm the friendship with one of the Friend nodes.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 01 (Friend Poll) |
|  | FSN | : | 0 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 000002 |
| SRC | : | 1201 |
| DST | : | 2345 |
| UpperTransportPDU | : | 00 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 000002 |
| SRC | : | 1201 |
| DST | : | 2345 |
| SEG | : | 00 |
| Opcode | : | 01 |
| Header | : | 01 |
| UpperTransportPDU | : | 00 |
| LowerTransportPDU | : | 0100 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| LPNAddress | : | 1201 | | | | | | |
| FriendAddress | : | 2345 | | | | | | |
| LPNCounter | : | 0000 | | | | | | |
| FriendCounter | : | 072f | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 000002 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | 2345 | | | | | | |
| LowerTransportPDU | : | 0100 | | | | | | |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00800000021201000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000002 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 2345 | | |
| TransportPDU | : |  |  |  |  |  | 0100 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b0e5d0ad | | |
| NetMIC | : |  |  |  |  |  |  | 970d579a4e88051c |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678b0e5d0ad970d57 |
| PECB | : | 04eba0902a0e |
| CTL||TTL||SEQ||SRC | : | 800000021201 |
|  | | |
| NetworkPDU | : | 5e84eba092380fb0e5d0ad970d579a4e88051c |

#### 8.3.5. Message #5

The Friend node confirms this friendship with a Friend Update message. The two nodes are now friends.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 02 (Friend Update) |
|  | Flags | : | 00 |
|  | IV Index | : | 12345678 |
|  | MD | : | 00 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 014834 |
| SRC | : | 2345 |
| DST | : | 1201 |
| UpperTransportPDU | : | 001234567800 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 014834 |
| SRC | : | 2345 |
| DST | : | 1201 |
| SEG | : | 00 |
| Opcode | : | 02 |
| Header | : | 02 |
| UpperTransportPDU | : | 001234567800 |
| LowerTransportPDU | : | 02001234567800 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| LPNAddress | : | 1201 | | | | | | |
| FriendAddress | : | 2345 | | | | | | |
| LPNCounter | : | 0000 | | | | | | |
| FriendCounter | : | 072f | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 014834 | | | | | | |
| SRC | : | 2345 | | | | | | |
| DST | : | 1201 | | | | | | |
| LowerTransportPDU | : | 02001234567800 | | | | | | |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00800148342345000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 014834 | | | | |
| SRC | : |  |  |  | 2345 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 02001234567800 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5c39da1792b1fee9ec | | |
| NetMIC | : |  |  |  |  |  |  | 74b786c56d3a9dee |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456785c39da1792b1fe |
| PECB | : | 2fd7bd08609e |
| CTL||TTL||SEQ||SRC | : | 800148342345 |
|  | | |
| NetworkPDU | : | 5eafd6f53c43db5c39da1792b1fee9ec74b786c56d3a9dee |

#### 8.3.6. Message #6

A Configuration Client sends a Config AppKey Add message to the Low Power node. This message is sent in two segments.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 00 (Config AppKey Add) |
| NetKeyIndex | : | 456 |
| AppKeyIndex | : | 123 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| Access message | : | 0056341263964771734fbd76e3b40519d1d94a48 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 04 |
| SEQ | : | 3129ab |
| SRC | : | 0003 |
| DST | : | 1201 |
| Application nonce | : | 02003129ab0003120112345678 |
| EncAccessMessage | : | ee9dddfd2169326d23f3afdfcfdc18c52fdef772 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | e0e17308 |
| UpperTransportPDU | : | ee9dddfd2169326d23f3afdfcfdc18c52fdef772e0e17308 |
| Segment#0 | : | ee9dddfd2169326d23f3afdf |
| Segment#1 | : | cfdc18c52fdef772e0e17308 |

|  |  |  |
| --- | --- | --- |
| LowerTransportSegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 04 |
| SEQ | : | 3129ab |
| SRC | : | 0003 |
| DST | : | 1201 |
| SEG | : | 01 |
| AKF | : | 00 |
| AID | : | 00 |
| SZMIC | : | 00 |
| SeqZero | : | 9ab |
| SegO | : | 00 |
| SegN | : | 01 |
| Header | : | 8026ac01 |
| Segment#0 | : | ee9dddfd2169326d23f3afdf |
| LowerTransportPDU | : | 8026ac01ee9dddfd2169326d23f3afdf |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 04 | | | | | | |
| SEQ | : | 3129ab | | | | | | |
| SRC | : | 0003 | | | | | | |
| DST | : | 1201 | | | | | | |
| LowerTransportPDU | : | 8026ac01ee9dddfd2169326d23f3afdf | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00043129ab0003000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 04 | | | | | |
| SEQ | : |  |  | 3129ab | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac01ee9dddfd2169326d23f3afdf | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0afba8c63d4e686364979deaf4fd40961145 | | |
| NetMIC | : |  |  |  |  |  |  | 939cda0e |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456780afba8c63d4e68 |
| PECB | : | ce84ec9f8a20 |
| CTL||TTL||SEQ||SRC | : | 043129ab0003 |
|  | | |
| NetworkPDU | : | 68cab5c5348a230afba8c63d4e686364979deaf4fd40961145939cda0e |

|  |  |  |
| --- | --- | --- |
| LowerTransportSegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 04 |
| SEQ | : | 3129ac |
| SRC | : | 0003 |
| DST | : | 1201 |
| SEG | : | 01 |
| AKF | : | 00 |
| AID | : | 00 |
| SZMIC | : | 00 |
| SeqZero | : | 3129ab |
| SegO | : | 01 |
| SegN | : | 01 |
| Header | : | 8026ac21 |
| Segment#1 | : | cfdc18c52fdef772e0e17308 |
| LowerTransportPDU | : | 8026ac21cfdc18c52fdef772e0e17308 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 04 | | | | | | |
| SEQ | : | 3129ac | | | | | | |
| SRC | : | 0003 | | | | | | |
| DST | : | 1201 | | | | | | |
| LowerTransportPDU | : | 8026ac21cfdc18c52fdef772e0e17308 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00043129ac0003000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 04 | | | | | |
| SEQ | : |  |  | 3129ac | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac21cfdc18c52fdef772e0e17308 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 6cae0c032bf0746f44f1b8cc8ce5edc57e55 | | |
| NetMIC | : |  |  |  |  |  |  | beed49c0 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456786cae0c032bf074 |
| PECB | : | 12249c714a87 |
| CTL||TTL||SEQ||SRC | : | 043129ac0003 |
|  | | |
| NetworkPDU | : | 681615b5dd4a846cae0c032bf0746f44f1b8cc8ce5edc57e55beed49c0 |

#### 8.3.7. Message #7

A friend of the destination acknowledges only one of the segments.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 00 (Segment Acknowledgment) |
|  | OBO | : | 01 |
|  | SeqZero | : | 09ab |
|  | BlockAck | : | 00000002 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 0b |
| SEQ | : | 014835 |
| SRC | : | 2345 |
| DST | : | 0003 |
| UpperTransportPDU | : | a6ac00000002 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 0b |
| SEQ | : | 014835 |
| SRC | : | 2345 |
| DST | : | 0003 |
| SEG | : | 00 |
| Opcode | : | 00 |
| Header | : | 00 |
| UpperTransportPDU | : | a6ac00000002 |
| LowerTransportPDU | : | 00a6ac00000002 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 0b | | | | | | |
| SEQ | : | 014835 | | | | | | |
| SRC | : | 2345 | | | | | | |
| DST | : | 0003 | | | | | | |
| LowerTransportPDU | : | 00a6ac00000002 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 008b0148352345000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 8b | | | | | |
| SEQ | : |  |  | 014835 | | | | |
| SRC | : |  |  |  | 2345 | | | |
| DST | : |  |  |  |  | 0003 | | |
| TransportPDU | : |  |  |  |  |  | 00a6ac00000002 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0d0d730f94d7f3509d | | |
| NetMIC | : |  |  |  |  |  |  | f987bb417eb7c05f |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456780d0d730f94d7f3 |
| PECB | : | 6f77fd62bfdd |
| CTL||TTL||SEQ||SRC | : | 8b0148352345 |
|  | | |
| NetworkPDU | : | 68e476b5579c980d0d730f94d7f3509df987bb417eb7c05f |

#### 8.3.8. Message #8

The Configuration Client receives the segment acknowledgment and retransmits the unacknowledged segment.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00043129ad0003000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 04 | | | | | |
| SEQ | : |  |  | 3129ad | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac01ee9dddfd2169326d23f3afdf | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0e2f91add6f06e66006844cec97f973105ae | | |
| NetMIC | : |  |  |  |  |  |  | 2534f958 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456780e2f91add6f06e |
| PECB | : | 499b4bcac2cc |
| CTL||TTL||SEQ||SRC | : | 043129ad0003 |
|  | | |
| NetworkPDU | : | 684daa6267c2cf0e2f91add6f06e66006844cec97f973105ae2534f958 |

#### 8.3.9. Message #9

The Friend node receives this last segment and sends an acknowledgment of this last segment.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 00 (Segment Acknowledgment) |
|  | OBO | : | 01 |
|  | SeqZero | : | 09ab |
|  | BlockAck | : | 00000003 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 0b |
| SEQ | : | 014836 |
| SRC | : | 2345 |
| DST | : | 0003 |
| UpperTransportPDU | : | a6ac00000003 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 0b |
| SEQ | : | 014836 |
| SRC | : | 2345 |
| DST | : | 0003 |
| SEG | : | 00 |
| Opcode | : | 00 |
| Header | : | 00 |
| UpperTransportPDU | : | a6ac00000003 |
| LowerTransportPDU | : | 00a6ac00000003 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 0b | | | | | | |
| SEQ | : | 014836 | | | | | | |
| SRC | : | 2345 | | | | | | |
| DST | : | 0003 | | | | | | |
| LowerTransportPDU | : | 00a6ac00000003 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 008b0148362345000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 8b | | | | | |
| SEQ | : |  |  | 014836 | | | | |
| SRC | : |  |  |  | 2345 | | | |
| DST | : |  |  |  |  | 0003 | | |
| TransportPDU | : |  |  |  |  |  | 00a6ac00000003 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d85d806bbed248614f | | |
| NetMIC | : |  |  |  |  |  |  | 938067b0d983bb7b |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678d85d806bbed248 |
| PECB | : | 25c52fdb6a44 |
| CTL||TTL||SEQ||SRC | : | 8b0148362345 |
|  | | |
| NetworkPDU | : | 68aec467ed4901d85d806bbed248614f938067b0d983bb7b |

#### 8.3.10. Message #10

Sometime later, the Low Power node polls its Friend node to check for more stored messages.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 01 (Friend Poll) |
|  | FSN | : | 1 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 000003 |
| SRC | : | 1201 |
| DST | : | 2345 |
| UpperTransportPDU | : | 01 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 000003 |
| SRC | : | 1201 |
| DST | : | 2345 |
| SEG | : | 00 |
| Opcode | : | 01 |
| Header | : | 01 |
| UpperTransportPDU | : | 01 |
| LowerTransportPDU | : | 0101 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| LPNAddress | : | 1201 | | | | | | |
| FriendAddress | : | 2345 | | | | | | |
| LPNCounter | : | 0000 | | | | | | |
| FriendCounter | : | 072f | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 000003 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | 2345 | | | | | | |
| LowerTransportPDU | : | 0101 | | | | | | |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00800000031201000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000003 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 2345 | | |
| TransportPDU | : |  |  |  |  |  | 0101 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 7777ed35 | | |
| NetMIC | : |  |  |  |  |  |  | 5afaf66d899c1e3d |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456787777ed355afaf6 |
| PECB | : | fb78656b679e |
| CTL||TTL||SEQ||SRC | : | 800000031201 |
|  | | |
| NetworkPDU | : | 5e7b786568759f7777ed355afaf66d899c1e3d |

#### 8.3.11. Message #11

The Friend node responds to this poll with the first segment of the stored message.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00033129ad0003000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 3129ad | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac01ee9dddfd2169326d23f3afdf | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d5e708a20ecfd98ddfd32de80befb400213d | | |
| NetMIC | : |  |  |  |  |  |  | 98468322 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678d5e708a20ecfd9 |
| PECB | : | e55a21d1fb5c |
| CTL||TTL||SEQ||SRC | : | 033129ad0003 |
|  | | |
| NetworkPDU | : | 5ee66b087cfb5fd5e708a20ecfd98ddfd32de80befb400213d98468322 |

#### 8.3.12. Message #12

The Low Power node didn't receive that message, so polls again for the same message with the FSN value having the same value as last time.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 01 (Friend Poll) |
|  | FSN | : | 1 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 000004 |
| SRC | : | 1201 |
| DST | : | 2345 |
| UpperTransportPDU | : | 01 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 000004 |
| SRC | : | 1201 |
| DST | : | 2345 |
| SEG | : | 00 |
| Opcode | : | 01 |
| Header | : | 01 |
| UpperTransportPDU | : | 01 |
| LowerTransportPDU | : | 0101 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| LPNAddress | : | 1201 | | | | | | |
| FriendAddress | : | 2345 | | | | | | |
| LPNCounter | : | 0000 | | | | | | |
| FriendCounter | : | 072f | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 000004 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | 2345 | | | | | | |
| LowerTransportPDU | : | 0101 | | | | | | |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00800000041201000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000004 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 2345 | | |
| TransportPDU | : |  |  |  |  |  | 0101 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | ae214660 | | |
| NetMIC | : |  |  |  |  |  |  | 87599c2426ce9a35 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678ae21466087599c |
| PECB | : | 0a18fc6a5f04 |
| CTL||TTL||SEQ||SRC | : | 800000041201 |
|  | | |
| NetworkPDU | : | 5e8a18fc6e4d05ae21466087599c2426ce9a35 |

#### 8.3.13. Message #13

The Friend node responds with the same message as last time.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00033129ad0003000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 3129ad | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac01ee9dddfd2169326d23f3afdf | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d5e708a20ecfd98ddfd32de80befb400213d | | |
| NetMIC | : |  |  |  |  |  |  | 98468322 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678d5e708a20ecfd9 |
| PECB | : | e55a21d1fb5c |
| CTL||TTL||SEQ||SRC | : | 033129ad0003 |
|  | | |
| NetworkPDU | : | 5ee66b087cfb5fd5e708a20ecfd98ddfd32de80befb400213d98468322 |

#### 8.3.14. Message #14

The Low Power node received the retransmitted stored message. Because that message is not a Friend Update with the MD field set to 0, it sends another Friend Poll to obtain the next message.

|  |  |  |  |
| --- | --- | --- | --- |
| Transport Control message | | | |
|  | | | |
| Opcode | | : | 01 (Friend Poll) |
|  | FSN | : | 0 |

|  |  |  |
| --- | --- | --- |
| UpperTransportControlPDU | | |
|  | | |
| TTL | : | 00 |
| SEQ | : | 000005 |
| SRC | : | 1201 |
| DST | : | 2345 |
| UpperTransportPDU | : | 00 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedControlPDU | | |
|  | | |
| CTL | : | 01 |
| TTL | : | 00 |
| SEQ | : | 000005 |
| SRC | : | 1201 |
| DST | : | 2345 |
| SEG | : | 00 |
| Opcode | : | 01 |
| Header | : | 01 |
| UpperTransportPDU | : | 00 |
| LowerTransportPDU | : | 0100 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| LPNAddress | : | 1201 | | | | | | |
| FriendAddress | : | 2345 | | | | | | |
| LPNCounter | : | 0000 | | | | | | |
| FriendCounter | : | 072f | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | 000005 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | 2345 | | | | | | |
| LowerTransportPDU | : | 0100 | | | | | | |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00800000051201000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000005 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 2345 | | |
| TransportPDU | : |  |  |  |  |  | 0100 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 7d3ae62a | | |
| NetMIC | : |  |  |  |  |  |  | 3c75dff683dce24e |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456787d3ae62a3c75df |
| PECB | : | 8bbaf92e4e8e |
| CTL||TTL||SEQ||SRC | : | 800000051201 |
|  | | |
| NetworkPDU | : | 5e0bbaf92b5c8f7d3ae62a3c75dff683dce24e |

#### 8.3.15. Message #15

The Friend node responds with the next message in the friend queue.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NID | : | 5e | | | | | | |
| EncryptionKey | : | be635105434859f484fc798e043ce40e | | | | | | |
| PrivacyKey | : | 5d396d4b54d3cbafe943e051fe9a4eb8 | | | | | | |
| Network nonce | : | 00033129ac0003000012345678 | | | | | | |
| IVI NID | : | 5e | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 3129ac | | | | |
| SRC | : |  |  |  | 0003 | | | |
| DST | : |  |  |  |  | 1201 | | |
| TransportPDU | : |  |  |  |  |  | 8026ac21cfdc18c52fdef772e0e17308 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | f1d29805664d235eacd707217dedfe78497f | | |
| NetMIC | : |  |  |  |  |  |  | efec7391 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345678f1d29805664d23 |
| PECB | : | abeb9ca27ee4 |
| CTL||TTL||SEQ||SRC | : | 033129ac0003 |
|  | | |
| NetworkPDU | : | 5ea8dab50e7ee7f1d29805664d235eacd707217dedfe78497fefec7391 |

#### 8.3.16. Message #16

The Low Power node has now received the complete Config AppKey Add message, so it responds to the segmented message with a status message. This is sent directly to the Configuration Client.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 8003 (Config AppKey Status) |
| Status | : | 00 |
| NetKeyIndex | : | 456 |
| AppKeyIndex | : | 123 |
| Access message | : | 800300563412 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 0b |
| SEQ | : | 000006 |
| SRC | : | 1201 |
| DST | : | 0003 |
| Application nonce | : | 02000000061201000312345678 |
| EncAccessMessage | : | 89511bf1d1a8 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 1c11dcef |
| UpperTransportPDU | : | 89511bf1d1a81c11dcef |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 0b |
| SEQ | : | 000006 |
| SRC | : | 1201 |
| DST | : | 0003 |
| SEG | : | 00 |
| AFK | : | 00 |
| AID | : | 00 |
| Header | : | 00 |
| UpperTransportPDU | : | 89511bf1d1a81c11dcef |
| LowerTransportPDU | : | 0089511bf1d1a81c11dcef |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 0b | | | | | | |
| SEQ | : | 000006 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | 0003 | | | | | | |
| LowerTransportPDU | : | 0089511bf1d1a81c11dcef | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000b0000061201000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 0b | | | | | |
| SEQ | : |  |  | 000006 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 0003 | | |
| TransportPDU | : |  |  |  |  |  | 0089511bf1d1a81c11dcef | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 6b9be7f5a642f2f98680e61c3a | | |
| NetMIC | : |  |  |  |  |  |  | 8b47f228 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456786b9be7f5a64287 |
| PECB | : | b037280f9de9 |
| CTL||TTL||SEQ||SRC | : | 0b0000061201 |
|  | | |
| NetworkPDU | : | 68e80e5da5af0e6b9be7f5a642f2f98680e61c3a8b47f228 |

#### 8.3.17. Message #17

A Relay node receives the message from the Low Power node and relays it, decrementing the TTL value.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000a0000061201000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 0a | | | | | |
| SEQ | : |  |  | 000006 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | 0003 | | |
| TransportPDU | : |  |  |  |  |  | 0089511bf1d1a81c11dcef | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2a80d381b91f824dd4f0a3cd54 | | |
| NetMIC | : |  |  |  |  |  |  | cea23b7a |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456782a80d381b91f82 |
| PECB | : | b8bd2c18096e |
| CTL||TTL||SEQ||SRC | : | 0a0000061201 |
|  | | |
| NetworkPDU | : | 68b2bd2c1e1b6f2a80d381b91f824dd4f0a3cd54cea23b7a |

#### 8.3.18. Message #18

The Low Power node sends a Health Current Status message indicating that there are no faults.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 04 (Health Current Status) |
| TestID: | : | 00 |
| CompanyID | : | 0000 |
| Faults | : | 00 |
| Access message | : | 0400000000 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345678 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 000007 |
| SRC | : | 1201 |
| DST | : | ffff |
| Application nonce | : | 01000000071201ffff12345678 |
| EncAccessMessage | : | 5a8bde6d91 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 06ea078a |
| UpperTransportPDU | : | 5a8bde6d9106ea078a |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 000007 |
| SRC | : | 1201 |
| DST | : | ffff |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| UpperTransportPDU | : | 5a8bde6d9106ea078a |
| LowerTransportPDU | : | 665a8bde6d9106ea078a |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 000007 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | ffff | | | | | | |
| LowerTransportPDU | : | 665a8bde6d9106ea078a | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00030000071201000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 000007 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | ffff | | |
| TransportPDU | : |  |  |  |  |  | 665a8bde6d9106ea078a | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5673728a627fb938535508e2 | | |
| NetMIC | : |  |  |  |  |  |  | 1a6baf57 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456785673728a627fb9 |
| PECB | : | 4bcba430940f |
| CTL||TTL||SEQ||SRC | : | 030000071201 |
|  | | |
| NetworkPDU | : | 6848cba437860e5673728a627fb938535508e21a6baf57 |

#### 8.3.19. Message #19

The Low Power node sends another Health Current Status message indicating that there are three faults: Battery Low Warning, Power Supply Interrupted Warning, and Supply Voltage Too Low Warning.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 04 (Health Current Status) |
| TestID | : | 00 |
| CompanyID | : | 0000 |
| Faults | : | 010703 |
| Access message | : | 04000000010703 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345678 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 000009 |
| SRC | : | 1201 |
| DST | : | ffff |
| Application nonce | : | 01000000091201ffff12345678 |
| EncAccessMessage | : | ca6cd88e698d12 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 65f43fc5 |
| UpperTransportPDU | : | ca6cd88e698d1265f43fc5 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 000009 |
| SRC | : | 1201 |
| DST | : | ffff |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| UpperTransportPDU | : | ca6cd88e698d1265f43fc5 |
| LowerTransportPDU | : | 66ca6cd88e698d1265f43fc5 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 000009 | | | | | | |
| SRC | : | 1201 | | | | | | |
| DST | : | ffff | | | | | | |
| LowerTransportPDU | : | 66ca6cd88e698d1265f43fc5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00030000091201000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 000009 | | | | |
| SRC | : |  |  |  | 1201 | | | |
| DST | : |  |  |  |  | ffff | | |
| TransportPDU | : |  |  |  |  |  | 66ca6cd88e698d1265f43fc5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 3010a05e1b23a926023da75d25ba | | |
| NetMIC | : |  |  |  |  |  |  | 91793736 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456783010a05e1b23a9 |
| PECB | : | 120edee5ca3d |
| CTL||TTL||SEQ||SRC | : | 030000091201 |
|  | | |
| NetworkPDU | : | 68110edeecd83c3010a05e1b23a926023da75d25ba91793736 |

#### 8.3.20. Message #20

The Low Power node sends the Health Current Status message with the same three faults.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 04 (Health Current Status) |
| TestID | : | 00 |
| CompanyID | : | 0000 |
| Faults | : | 010703 |
| Access message | : | 04000000010703 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345677 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 070809 |
| SRC | : | 1234 |
| DST | : | ffff |
| Application nonce | : | 01000708091234ffff12345677 |
| EncAccessMessage | : | 9c9803e110fea9 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 29e9542d |
| UpperTransportPDU | : | 9c9803e110fea929e9542d |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 070809 |
| SRC | : | 1234 |
| DST | : | ffff |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| Segment#0 | : | 9c9803e110fea929e9542d |
| LowerTransportPDU | : | 669c9803e110fea929e9542d |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 070809 | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | ffff | | | | | | |
| LowerTransportPDU | : | 669c9803e110fea929e9542d | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 00030708091234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 070809 | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | ffff | | |
| TransportPDU | : |  |  |  |  |  | 669c9803e110fea929e9542d | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 8c3dc87344a16c787f6b08cc897c | | |
| NetMIC | : |  |  |  |  |  |  | 941a5368 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456778c3dc87344a16c |
| PECB | : | 5fcd59ebfaad |
| CTL||TTL||SEQ||SRC | : | 030708091234 |
|  | | |
| NetworkPDU | : | e85cca51e2e8998c3dc87344a16c787f6b08cc897c941a5368 |

#### 8.3.21. Message #21

The Low Power node sends a vendor command to a group address.

|  |
| --- |
| Company ID: 0x000A - Cambridge Silicon Radio (See Bluetooth Assigned Numbers) |
| Vendor Opcode: 0x15 |

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 0x15 : 0x000a (Opcode 15 : Company ID 000a) |
| Params | : | 48656c6c6f |
| Access message | : | d50a0048656c6c6f |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345677 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 07080a |
| SRC | : | 1234 |
| DST | : | c105 |
| Application nonce | : | 010007080a1234c10512345677 |
| EncAccessMessage | : | 4d92e9dfcf3ab85b |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 6e8fcf03 |
| UpperTransportPDU | : | 4d92e9dfcf3ab85b6e8fcf03 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 07080a |
| SRC | : | 1234 |
| DST | : | c105 |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| UpperTransportPDU | : | 4d92e9dfcf3ab85b6e8fcf03 |
| LowerTransportPDU | : | 664d92e9dfcf3ab85b6e8fcf03 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 07080a | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | c105 | | | | | | |
| LowerTransportPDU | : | 664d92e9dfcf3ab85b6e8fcf03 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000307080a1234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 07080a | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | c105 | | |
| TransportPDU | : |  |  |  |  |  | 664d92e9dfcf3ab85b6e8fcf03 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | a4d61157bb76352ea6307eebfe0f30 | | |
| NetMIC | : |  |  |  |  |  |  | b83500e9 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345677a4d61157bb7635 |
| PECB | : | 4d88b60a2d6c |
| CTL||TTL||SEQ||SRC | : | 0307080a1234 |
|  | | |
| NetworkPDU | : | e84e8fbe003f58a4d61157bb76352ea6307eebfe0f30b83500e9 |

#### 8.3.22. Message #22

The Low Power node sends a vendor command to a virtual address.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 15 : 000a (Vendor 15 : 000a) |
| Params | : | 48656c6c6f |
| Access message | : | d50a0048656c6c6f |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345677 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 07080b |
| SRC | : | 1234 |
| Label UUID | : | 0073e7e4d8b9440faf8415df4c56c0e1 |
| DST (Virtual Address) | : | b529 |
| Application nonce | : | 010007080b1234b52912345677 |
| EncAccessMessage | : | 3871b904d4315263 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 16ca48a0 |
| UpperTransportPDU | : | 3871b904d431526316ca48a0 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 07080b |
| SRC | : | 1234 |
| DST | : | b529 |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| UpperTransportPDU | : | 3871b904d431526316ca48a0 |
| LowerTransportPDU | : | 663871b904d431526316ca48a0 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 07080b | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | b529 | | | | | | |
| LowerTransportPDU | : | 343871b904d431526316ca48a0 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000307080b1234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 07080b | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | b529 | | |
| TransportPDU | : |  |  |  |  |  | 663871b904d431526316ca48a0 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | ed31f3fdcf88a411135fea55df730b | | |
| NetMIC | : |  |  |  |  |  |  | 6b28e255 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345677ed31f3fdcf88a4 |
| PECB | : | db5ba6c5e3d7 |
| CTL||TTL||SEQ||SRC | : | 0307080b1234 |
|  | | |
| NetworkPDU | : | e8d85caecef1e3ed31f3fdcf88a411135fea55df730b6b28e255 |

#### 8.3.23. Message #23

The Low Power node sends a vendor command to a different virtual address.

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Opcode | : | 15 : 000a (Vendor 15 : 000a) |
| Params | : | 48656c6c6f |
| Access message | : | d50a0048656c6c6f |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345677 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 07080c |
| SRC | : | 1234 |
| Label UUID | : | f4a002c7fb1e4ca0a469a021de0db875 |
| DST (Virtual Address) | : | 9736 |
| Application nonce | : | 010007080c1234973612345677 |
| EncAccessMessage | : | 2456db5e3100eef6 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 5daa7a38 |
| UpperTransportPDU | : | 2456db5e3100eef65daa7a38 |

|  |  |  |
| --- | --- | --- |
| LowerTransportUnsegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 07080c |
| SRC | : | 1234 |
| DST | : | 9736 |
| SEG | : | 00 |
| AKF | : | 01 |
| AID | : | 26 |
| Header | : | 66 |
| UpperTransportPDU | : | 2456db5e3100eef65daa7a38 |
| LowerTransportPDU | : | 662456db5e3100eef65daa7a38 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 07080c | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | 9736 | | | | | | |
| LowerTransportPDU | : | 342456db5e3100eef65daa7a38 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000307080c1234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 07080c | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | 9736 | | |
| TransportPDU | : |  |  |  |  |  | 662456db5e3100eef65daa7a38 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 7a9d696d3dd16a75489696f0b70c71 | | |
| NetMIC | : |  |  |  |  |  |  | 1b881385 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 0000000000123456777a9d696d3dd16a |
| PECB | : | 74a385d9ec19 |
| CTL||TTL||SEQ||SRC | : | 0307080c1234 |
|  | | |
| NetworkPDU | : | e877a48dd5fe2d7a9d696d3dd16a75489696f0b70c711b881385 |

#### 8.3.24. Message #24

The Low Power node sends a vendor command to a virtual address using a 64-bit TransMIC.

|  |
| --- |
| Company ID: 0x000A - Cambridge Silicon Radio (See Bluetooth Assigned Numbers) |
| Vendor Opcode: 0x2A |

|  |  |  |
| --- | --- | --- |
| Access message | | |
|  | | |
| Vendor Opcode | : | 0x2A : 0x000A (Opcode 2a : Company ID 000a) |
| Params | : | 576f726c64 |
| Access message | : | ea0a00576f726c64 |

|  |  |  |
| --- | --- | --- |
| UpperTransportAccessPDU | | |
|  | | |
| IV Index | : | 12345677 |
| AppKey | : | 63964771734fbd76e3b40519d1d94a48 |
| TTL | : | 03 |
| SEQ | : | 07080d |
| SRC | : | 1234 |
| Label UUID | : | f4a002c7fb1e4ca0a469a021de0db875 |
| DST (Virtual Address) | : | 9736 |
| Application nonce | : | 018007080d1234973612345677 |
| EncAccessMessage | : | c3c51d8e476b28e3 |
| TransMIC Size | : | 64 bits |
| TransMIC | : | aa5001f31c01cea6 |
| UpperTransportPDU | : | c3c51d8e476b28e3aa5001f31c01cea6 |
| Segment#0 | : | c3c51d8e476b28e3aa5001f3 |
| Segment#1 | : | 1c01cea6 |

|  |  |  |
| --- | --- | --- |
| LowerTransportSegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 07080d |
| SRC | : | 1234 |
| DST | : | 9736 |
| SEG | : | 01 |
| AKF | : | 01 |
| AID | : | 26 |
| SZMIC | : | 01 |
| SeqZero | : | 80d |
| SegO | : | 00 |
| SegN | : | 01 |
| Header | : | e6a03401 |
| Segment#0 | : | c3c51d8e476b28e3aa5001f3 |
| LowerTransportPDU | : | e6a03401c3c51d8e476b28e3aa5001f3 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 07080d | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | 9736 | | | | | | |
| LowerTransportPDU | : | e6a03401c3c51d8e476b28e3aa5001f3 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000307080d1234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 07080d | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | 9736 | | |
| TransportPDU | : |  |  |  |  |  | e6a03401c3c51d8e476b28e3aa5001f3 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 94e998b4081f47a35251fdd3896d99e4db48 | | |
| NetMIC | : |  |  |  |  |  |  | 9b918599 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 00000000001234567794e998b4081f47 |
| PECB | : | 61496db69e23 |
| CTL||TTL||SEQ||SRC | : | 0307080d1234 |
|  | | |
| NetworkPDU | : | e8624e65bb8c1794e998b4081f47a35251fdd3896d99e4db489b918599 |

|  |  |  |
| --- | --- | --- |
| LowerTransportSegmentedAccessPDU | | |
|  | | |
| CTL | : | 00 |
| TTL | : | 03 |
| SEQ | : | 07080e |
| SRC | : | 1234 |
| DST | : | 9736 |
| SEG | : | 01 |
| AKF | : | 01 |
| AID | : | 26 |
| SZMIC | : | 01 |
| SeqZero | : | 80d |
| SegO | : | 01 |
| SegN | : | 01 |
| Header | : | e6a03421 |
| Segment#1 | : | 1c01cea6 |
| LowerTransportPDU | : | e6a034211c01cea6 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetworkPDU | | | | | | | | |
|  | | | | | | | | |
| IVindex | : | 12345677 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 03 | | | | | | |
| SEQ | : | 07080e | | | | | | |
| SRC | : | 1234 | | | | | | |
| DST | : | 9736 | | | | | | |
| LowerTransportPDU | : | e6a034211c01cea6 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 000307080e1234000012345677 | | | | | | |
| IVI NID | : | e8 | | | | | | |
| CTL TTL | : |  | 03 | | | | | |
| SEQ | : |  |  | 07080e | | | | |
| SRC | : |  |  |  | 1234 | | | |
| DST | : |  |  |  |  | 9736 | | |
| TransportPDU | : |  |  |  |  |  | e6a034211c01cea6 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | dc2f4dd6fb4db33a6c08 | | |
| NetMIC | : |  |  |  |  |  |  | 8d023b47 |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| Privacy Plaintext | : | 000000000012345677dc2f4dd6fb4db3 |
| PECB | : | a4d7f8acf876 |
| CTL||TTL||SEQ||SRC | : | 0307080e1234 |
|  | | |
| NetworkPDU | : | e8a7d0f0a2ea42dc2f4dd6fb4db33a6c088d023b47 |

### 8.4. Beacon sample data

The following beacon sample data shows examples of beacons.

#### 8.4.1. Unprovisioned device beacon (without URI)

This shows an example of an unprovisioned device. This device has some OOB information that is an ASCII-string written on a piece of paper and on the device itself.

|  |  |  |
| --- | --- | --- |
| Device UUID | : | 70cf7c9732a345b691494810d2e9cbf4 |
| OOB | : | String, on piece of paper, on device |
| OOB Information | : | a040 |
|  | | |
| Beacon | : | 0070cf7c9732a345b691494810d2e9cbf4a040 |

#### 8.4.2. Unprovisioned device beacon (with URI)

This shows an example of an unprovisioned device that also includes some OOB information as a number on the inside of the manual, and also a URI-hash that can be used to help identify the device.

|  |  |  |
| --- | --- | --- |
| Device UUID | : | 70cf7c9732a345b691494810d2e9cbf4 |
| OOB | : | Number, Inside Manual |
| OOB Information | : | 4020 |
| URI | : | https://www.example.com/meshuri |
| URI Data | : | 172f2f7777772e6578616d706c652e636f6d2f6d657368757269 |
| URI Hash | : | d36b25b8f8a600bd055c73049ef82227 |
| Beacon | : | 0070cf7c9732a345b691494810d2e9cbf44020d36b25b8 |

#### 8.4.3. Secure Network beacon

This shows an example of a Secure Network beacon that includes the IV Index for a given network key. There are now key refresh or IV updates occurring at this time.

|  |  |  |
| --- | --- | --- |
| IV Update Flag | : | 0 |
| Key Refresh Flag | : | 0 |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| IV Index | : | 12345678 |
| Flags | : | 00 |
| Network ID | : | 3ecaff672f673370 |
| Message | : | 003ecaff672f67337012345678 |
| BeaconKey | : | 5423d967da639a99cb02231a83f7d254 |
| Authentication Value | : | 8ea261582f364f6f3c74ef80336ca17e |
|  |  |  |
| Beacon | : | 01003ecaff672f673370123456788ea261582f364f6f |

#### 8.4.4. Secure Network beacon (IV update in progress)

This shows an example Secure Network beacon that would be sent when the IV Index is being updated. In this example, the IV Index has been incremented and the IV Update Flag is set.

|  |  |  |
| --- | --- | --- |
| IV Update Flag | : | 1 |
| Key Refresh Flag | : | 0 |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| IV Index | : | 12345679 |
| Flags | : | 02 |
| Network ID | : | 3ecaff672f673370 |
| Message | : | 023ecaff672f67337012345679 |
| BeaconKey | : | 5423d967da639a99cb02231a83f7d254 |
| Authentication Value | : | c2af80ad072a135c28cf843369887039 |
|  |  |  |
| Beacon | : | 01023ecaff672f67337012345679c2af80ad072a135c |

#### 8.4.5. Secure Network beacon (IV update complete)

This shows an example of a Secure Network beacon after the IV Index has been updated. The IV Index has the same value as the previous Secure Network beacon, but the IV Update Flag is now cleared.

|  |  |  |
| --- | --- | --- |
| IV Update Flag | : | 0 |
| Key Refresh Flag | : | 0 |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 |
| IV Index | : | 12345679 |
| Flags | : | 00 |
| Network ID | : | 3ecaff672f673370 |
| Message | : | 003ecaff672f67337012345679 |
| BeaconKey | : | 5423d967da639a99cb02231a83f7d254 |
| Authentication Value | : | c62f09e4c957f59d96f506f64604bfc1 |
|  |  |  |
| Beacon | : | 01003ecaff672f67337012345679c62f09e4c957f59d |

#### 8.4.6. Mesh Private Beacon

The following sections show examples of Mesh Private beacons that includes the IV Update Flag, Key Refresh Flag, and IV Index for a given network key.

##### 8.4.6.1. IV update in Progress

|  |  |  |
| --- | --- | --- |
| Random | : | 435f18f85cf78a3121f58478a5 |
| Key Refresh Flag | : | 00 |
| IV Update Flag | : | 01 |
| IVindex | : | 1010abcd |
| NetKey | : | f7a2a44f8e8a8029064f173ddc1e2b00 |
| k1 P | : | 696431323801 |
| k1 Salt | : | 2c8b71fb5d95e86cfb753bfee3ab934f |
| PrivateBeaconKey | : | 6be76842460b2d3a5850d4698409f1bb |
| Flags | : | 02 |
| Private Beacon Data | : | 021010abcd |
| Obfuscated_Private_­Beacon_­Data | : | 61e488e7cb |
| Authentication_Tag | : | f3174f022a514741 |
| Payload | : | 435f18f85cf78a3121f58478a561e488e7cbf3174f022a514741 |
| Private Beacon | : | 1c2b02435f18f85cf78a3121f58478a561e488e7cbf3174f022a514741 |

##### 8.4.6.2. IV update complete

|  |  |  |
| --- | --- | --- |
| Random | : | 1b998f82927535ea6f3076f422 |
| Key Refresh Flag | : | 00 |
| IV Update Flag | : | 00 |
| IVindex | : | 00000000 |
| NetKey | : | 3bbb6f1fbd53e157417f308ce7aec58f |
| k1 P | : | 696431323801 |
| k1 Salt | : | 2c8b71fb5d95e86cfb753bfee3ab934f |
| PrivateBeaconKey | : | ca478cdac626b7a8522d7272dd124f26 |
| Flags | : | 00 |
| Private Beacon Data | : | 0000000000 |
| Obfuscated_Private_­Beacon_­Data | : | ce827408ab |
| Authentication_Tag | : | 2f0ffb94cf97f881 |
| Payload | : | 1b998f82927535ea6f3076f422ce827408ab2f0ffb94cf97f881 |
| Private Beacon | : | 1c2b021b998f82927535ea6f3076f422ce827408ab2f0ffb94cf97f881 |

### 8.5. Provisioning Service sample data

The following sample data shows the advertising data for a Provisioning Service advertisement.

#### 8.5.1. Mesh Provisioning Service advertising service data

This sample data shows that the device has some OOB information as a number that is printed inside of the manual.

|  |  |  |
| --- | --- | --- |
| Device UUID | : | 70cf7c9732a345b691494810d2e9cbf4 |
| OOB | : | Number, Inside Manual |
| OOB Information | : | 4020 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Adv Len | : | 15 | | | | |
| Adv (Service Data) | : |  | 16 |  | | |
| Mesh Provisioning UUID | : |  |  | 1827 | | |
| Device UUID | : |  |  |  | 70cf7c9732a345b691494810d2e9cbf4 | |
| OOB Information | : |  |  |  |  | 4020 |
| ADV Data | : | 1516271870cf7c9732a345b691494810d2e9cbf42040 | | | | |

### 8.6. Mesh Proxy Service sample data

The following sample data shows Mesh Proxy service sample data.

#### 8.6.1. Service data using Network ID

This shows the advertising data used to broadcast the Network ID of a network that can be accessed through a Mesh Proxy service. This would be used to allow a device to connect to a specific mesh network.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| Adv Len | : | 0c | | | | | | |
| Adv (Service Data) | : |  | 16 | | | | | | |
| Mesh Proxy UUID | : |  |  | 1828 | | | | | | |
| Type | : |  |  |  | 00 | | | | | | |
| Network ID | : |  |  |  |  | 3ecaff672f673370 | | | | | | |
| ADV Data | : | 0c162818003ecaff672f673370 | | | | |

#### 8.6.2. Service data using Node Identity

This shows the advertising data used to broadcast the identity of a node in a private manner that can be accessed through a Mesh Proxy service. This would be used to allow a device to connect to a specific node.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| Source Address | : | 1201 | | | | | |
| Random | : | 34ae608fbbc1f2c6 | | | | | |
| Nonce | : | 00000000000034ae608fbbc1f2c61201 | | | | | |
| IdentityKey | : | 84396c435ac48560b5965385253e210c | | | | | |
| Adv Len | : | 14 | | | | | |
| Adv (Service Data) | : |  | 16 | | | | |
| Mesh Proxy UUID | : |  |  | 1828 | | | |
| Type | : |  |  |  | 01 | | |
| Hash | : |  |  |  |  | 00861765aefcc57b | |
| Random | : |  |  |  |  |  | 34ae608fbbc1f2c6 |
| ADV Data | : | 141628180100861765aefcc57b34ae608fbbc1f2c6 | | | | | |

#### 8.6.3. Service data using Private Network Identity

This shows the advertising data used to broadcast the identity of a network in a private manner that can be accessed through a Mesh Proxy service. This would be used to allow a device to connect to a specific mesh network.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| Random | : | 34ae608fbbc1f2c6 | | | | | |
| IdentityKey | : | 84396c435ac48560b5965385253e210c | | | | | |
| Network ID | : | 3ecaff672f673370 | | | | | |
| e plaintext | : | 3ecaff672f67337034ae608fbbc1f2c6 | | | | | |
| IdentityHash | : | a19967973d8094ecd30f7229ef045435 | | | | | |
| Adv Len | : | 14 | | | | | |
| Adv (Service Data) | : |  | 16 | | | | |
| Mesh Proxy UUID | : |  |  | 1828 | | | |
| Type | : |  |  |  | 02 | | |
| Hash | : |  |  |  |  | d30f7229ef045435 | |
| Random | : |  |  |  |  |  | 34ae608fbbc1f2c6 |
| ADV Data | : | 1416281802d30f7229ef04543534ae608fbbc1f2c6 | | | | | |

#### 8.6.4. Service data using Private Node Identity

This shows the advertising data used to broadcast the identity of a node in a private manner that can be accessed through a Mesh Proxy service. This would be used to allow a device to connect to a specific node.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| Source Address | : | 1201 | | | | | |
| Random | : | 34ae608fbbc1f2c6 | | | | | |
| IdentityKey | : | 84396c435ac48560b5965385253e210c | | | | | |
| e plaintext | : | 00000000000334ae608fbbc1f2c61201 | | | | | |
| IdentityHash | : | 2eba33b59d60593e2c64a8cbca65bfe1 | | | | | |
| Adv Len | : | 14 | | | | | |
| Adv (Service Data) | : |  | 16 | | | | |
| Mesh Proxy UUID | : |  |  | 1828 | | | |
| Type | : |  |  |  | 03 | | |
| Hash | : |  |  |  |  | 2c64a8cbca65bfe1 | |
| Random | : |  |  |  |  |  | 34ae608fbbc1f2c6 |
| ADV Data | : | 14162818032c64a8cbca65bfe134ae608fbbc1f2c6 | | | | | |

### 8.7. PB-ADV provisioning sample data

The following sample data shows a complete set of provisioning transactions over PB-ADV. The following sample data is based on the provisioning and device private keys documented below.

|  |  |  |
| --- | --- | --- |
| Prov Private Key | : | 06a516693c9aa31a6084545d0c5db641b48572b97203ddffb7ac73f7d0457663 |
| Prov Public Key | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
|  |  | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| Device Private Key | : | 529aa0670d72cd6497502ed473502b037e8803b5c60829a5a3caa219505530ba |
| Device Public Key | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
|  |  | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| Prov ECDH | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| Device ECDH | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| Prov Random | : | 8b19ac31d58b124c946209b5db1021b9 |
| Device Random | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a |

#### 8.7.1. PB-ADV Link Open

The Provisioner, after receiving the Mesh Provisioning Service advertising data, will send a Link Open message including the Device UUID of the new device.

|  |
| --- |
| Link Open |

|  |  |  |
| --- | --- | --- |
| Device UUID | : | 70cf7c9732a345b691494810d2e9cbf4 |

|  |
| --- |
| Provisioning Control |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 00 |
| Opcode | : | 00 (Link Open) | |
| Message | : | 23af5850000370cf7c9732a345b691494810d2e9cbf4 | |

#### 8.7.2. PB-ADV Link ACK

The new device will respond with a Link ACK to confirm that it is accepting this Link Open. All other messages after this point will use this LinkID to identify this session until the Link Close message is received.

|  |
| --- |
| Link ACK |

|  |
| --- |
| Provisioning Control |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 00 |
| Opcode | : | 01 (Link ACK) | |
| Message | : | 23af58500007 | |

#### 8.7.3. PB-ADV Provisioning Invite

The Provisioner will invite the new device to join the mesh network. This includes a duration for which the new device will attract attention of the user such that the user knows which new device is currently being provisioned. In this case, the duration is 0 seconds, meaning that the Provisioner didn’t need the new device to
make itself known to the user.

|  |
| --- |
| Provisioning Invite |

|  |  |  |
| --- | --- | --- |
| Attention Duration | : | 00 (0 seconds) |
| Message | : | 0000 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 00 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 0000 |
| SegN | : | 00 |
| TotalLength | : | 0002 |
| FCS | : | 14 |
| Message0 | : | 23af585000000002140000 |

##### 8.7.3.1. PB-ADV Transaction Ack

The Provisioner acknowledges the invite transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 00 |
| Message | : | 23af58500001 | |

#### 8.7.4. PB-ADV Provisioning Capabilities

The new device responds to the invite by sending its capabilities. The new device has only one element, supports the P-256 elliptic curve, and has no OOB information or input or output capabilities.

|  |
| --- |
| Provisioning Capabilities |

|  |  |  |
| --- | --- | --- |
| Number of Elements | : | 01 |
| Algorithms | : | 0001 |
| Public Key Type | : | 00 |
| OOB Type | : | 00 |
| Output OOB Size | : | 00 |
| Output OOB Action | : | 0000 |
| Input OOB Size | : | 00 |
| Input OOB Action | : | 0000 |
| Message | : | 010100010000000000000000 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 80 |
| Segment0 | : | 010100010000000000000000 | |
| SegN | : | 00 | |
| TotalLength | : | 000c | |
| FCS | : | d6 | |
| Message0 | : | 23af58508000000cd6010100010000000000000000 | |

##### 8.7.4.1. PB-ADV Transaction Ack

The Provisioner acknowledges the capabilities transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 80 |
| Message | : | 23af58508001 | |

#### 8.7.5. PB-ADV Provisioning Start

The Provisioner upon receiving the capabilities, sends a provisioning start message stating the algorithm and authentication method to use.

|  |
| --- |
| Provisioning Start |

|  |  |  |
| --- | --- | --- |
| Algorithm | : | 00 |
| Public Key | : | 0000 |
| Authentication Method | : | 00 |
| Authentication Action | : | 00 |
| Authentication Size | : | 00 |
| Message | : | 020000000000 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 01 |
|  | | | |
| Segment0 | : | 020000000000 | |
| SegN | : | 00 | |
| TotalLength | : | 0006 | |
| FCS | : | 64 | |
| Message0 | : | 23af58500100000664020000000000 | |

##### 8.7.5.1. PB-ADV Transaction Ack

The new device acknowledges this start transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 01 |
| Message | : | 23af58500101 | |

#### 8.7.6. PB-ADV Provisioning Public Key (Provisioner)

The Provisioner sends its public key to the new device. This message contains the 512-bit public key, and is therefore transmitted using three segments in three messages.

|  |
| --- |
| Provisioning Start |

|  |  |  |
| --- | --- | --- |
| Public Key X | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
| Public Key Y | : | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| Message | : | 032c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78 |
|  |  | dd919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d 4f |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 02 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 032c31a47b5779809ef44cb5eaaf5c3e43d5f8fa |
| Segment1 | : | ad4a8794cb987e9b03745c78dd919512183898dfbecd52 |
| Segment2 | : | e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| SegN | : | 02 |
| TotalLength | : | 0041 |
| FCS | : | d1 |
| Message0 | : | 23af585002080041d1032c31a47b5779809ef44cb5eaaf5c3e43d5f8fa |
| Message1 | : | 23af58500206ad4a8794cb987e9b03745c78dd919512183898dfbecd52 |
| Message2 | : | 23af5850020ae2408e43871fd021109117bd3ed4eaf8437743715d4f |

##### 8.7.6.1. PB-ADV Transaction Ack

Once the new device receives all the segments of the provisioning public key transaction, it will send the acknowledgment for that transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 02 |
| Message | : | 23af58500201 | |

#### 8.7.7. PB-ADV Provisioning Public Key (Device)

The device sends its public key to the Provisioner. This is again a multi-segment transaction.

|  |
| --- |
| Provisioning Start |

|  |  |  |
| --- | --- | --- |
| Public Key X | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
| Public Key Y | : | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| Message | : | 03f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500 |
|  |  | cc0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 81 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 03f465e43ff23d3f1b9dc7dfc04da8758184dbc9 |
| Segment1 | : | 66204796eccf0d6cf5e16500cc0201d048bcbbd899eeef |
| Segment2 | : | c424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| SegN | : | 02 |
| TotalLength | : | 0041 |
| FCS | : | 10 |
| Message0 | : | 23af5850810800411003f465e43ff23d3f1b9dc7dfc04da8758184dbc9 |
| Message1 | : | 23af5850810666204796eccf0d6cf5e16500cc0201d048bcbbd899eeef |
| Message2 | : | 23af5850810ac424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |

##### 8.7.7.1. PB-ADV Transaction Ack

The Provisioner sends a transaction acknowledgment when it receives all the segments of the public key transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 81 |
| Message | : | 23af58508101 | |

#### 8.7.8. PB-ADV Provisioning Confirmation (Provisioner)

The Provisioner will calculate a confirmation value that is based off of all the information already exchanged, a random number that has not been exchanged yet, and an authentication value that is communicated OOB. As this provisioning is not using any authentication, the AuthValue is set to 0.

|  |  |  |
| --- | --- | --- |
| InvitePDUValue | : | 00 |
| CapabilitiesPDUValue | : | 0100010000000000000000 |
| StartPDUValue | : | 0000000000 |
| ProvisionerPublicKey | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
|  |  | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| DevicePublicKey | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
|  |  | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| ConfirmationInputs | : | 00010001000000000000000000000000002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| ConfirmationSalt | : | 5faabe187337c71cc6c973369dcaa79a |
| ECDHSecret | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| k1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| k1 SALT | : | 5faabe187337c71cc6c973369dcaa79a |
| k1 P | : | 7072636b |
| k1 T | : | ace84c6f002e0b4c23467e75687bae8f |
| ConfirmationKey | : | e31fe046c68ec339c425fc6629f0336f |
| RandomProvisioner | : | 8b19ac31d58b124c946209b5db1021b9 |
| AuthValue | : | 00000000000000000000000000000000 |

|  |
| --- |
| Provisioning Confirmation |

|  |  |  |  |
| --- | --- | --- | --- |
| Confirmation | : | b38a114dfdca1fe153bd2c1e0dc46ac2 | |
| Message | : | 05b38a114dfdca1fe153bd2c1e0dc46ac2 | |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 03 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 05b38a114dfdca1fe153bd2c1e0dc46ac2 |
| SegN | : | 00 |
| TotalLength | : | 0011 |
| FCS | : | d1 |
| Message0 | : | 23af585003000011d105b38a114dfdca1fe153bd2c1e0dc46ac2 |

##### 8.7.8.1. PB-ADV Transaction Ack

The new device will acknowledge the confirmation transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 03 |
| Message | : | 23af58500301 | |

#### 8.7.9. PB-ADV Provisioning Confirmation (Device)

The new device will send its confirmation value using all the information that it has exchanged so far, the authentication value communicated OOB, and a random number that has not been disclosed yet.

|  |  |  |
| --- | --- | --- |
| InvitePDUValue | : | 00 |
| CapabilitiesPDUValue | : | 0100010000000000000000 |
| StartPDUValue | : | 0000000000 |
| ProvisionerPublicKey | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
|  |  | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| DevicePublicKey | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
|  |  | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| ConfirmationInputs | : | 00010001000000000000000000000000002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| ConfirmationSalt | : | 5faabe187337c71cc6c973369dcaa79a |
| ECDHSecret | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| k1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| k1 SALT | : | 5faabe187337c71cc6c973369dcaa79a |
| k1 P | : | 7072636b |
| k1 T | : | ace84c6f002e0b4c23467e75687bae8f |
| ConfirmationKey | : | e31fe046c68ec339c425fc6629f0336f |
| RandomDevice | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a |
| AuthValue | : | 00000000000000000000000000000000 |

|  |
| --- |
| Provisioning Confirmation |

|  |  |  |
| --- | --- | --- |
| Confirmation | : | eeba521c196b52cc2e37aa40329f554e |
| Message | : | 05eeba521c196b52cc2e37aa40329f554e |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 82 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 05eeba521c196b52cc2e37aa40329f554e |
| SegN | : | 00 |
| TotalLength | : | 0011 |
| FCS | : | ec |
| Message0 | : | 23af585082000011ec05eeba521c196b52cc2e37aa40329f554e |

##### 8.7.9.1. PB-ADV Transaction Ack

The Provisioner will acknowledge the confirmation transaction from the new device.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 82 |
| Message | : | 23af58508201 | |

#### 8.7.10. PB-ADV Provisioning Random (Provisioner)

The Provisioner will now expose its random number used to generate its confirmation value that it has previously committed to.

|  |
| --- |
| Provisioning Random |

|  |  |  |
| --- | --- | --- |
| Random | : | 8b19ac31d58b124c946209b5db1021b9 |
| Message | : | 068b19ac31d58b124c946209b5db1021b9 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 04 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 068b19ac31d58b124c946209b5db1021b9 |
| SegN | : | 00 |
| TotalLength | : | 0011 |
| FCS | : | d3 |
| Message0 | : | 23af585004000011d3068b19ac31d58b124c946209b5db1021b9 |

##### 8.7.10.1. PB-ADV Transaction Ack

The new device acknowledges this random number transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 04 |
| Message | : | 23af58500401 | |

#### 8.7.11. PB-ADV Provisioning Random (Device)

The new device now sends its random number to the Provisioner.

|  |
| --- |
| Provisioning Random |

|  |  |  |
| --- | --- | --- |
| Random | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a |
| Message | : | 0655a2a2bca04cd32ff6f346bd0a0c1a3a |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 83 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 0655a2a2bca04cd32ff6f346bd0a0c1a3a |
| SegN | : | 00 |
| TotalLength | : | 0011 |
| FCS | : | 59 |
| Message0 | : | 23af585083000011590655a2a2bca04cd32ff6f346bd0a0c1a3a |

##### 8.7.11.1. PB-ADV Transaction Ack

The Provisioner acknowledges receiving this random number transaction from the new device.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 83 |
| Message | : | 23af58508301 | |

#### 8.7.12. PB-ADV Provisioning Data

The Provisioner can now provide the provisioning data required by the new device to become a node in a mesh network. This includes a NetKey along with a network key index, the current IV Index of this network key, and the unicast address of the first element of this node, and therefore all the subsequent addresses of additional
elements. This data is encrypted and authenticated using a session key derived from the ECDH shared secret. This data requires two segments to communicate.

|  |  |  |  |
| --- | --- | --- | --- |
| ConfirmationSalt | : | 5faabe187337c71cc6c973369dcaa79a | |
| Random Provisioner | : | 8b19ac31d58b124c946209b5db1021b9 | |
| Random Device | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a | |
| ProvisioningInputs | : | 5faabe187337c71cc6c973369dcaa79a8b19ac31d58b124c946209b5db | |
|  |  | 1021b955a2a2bca04cd32ff6f346bd0a0c1a3a | |
| ProvisioningSalt | : | a21c7d45f201cf9489a2fb57145015b4 | |
| DeviceKey | : | 0520adad5e0142aa3e325087b4ec16d8 | |
| SessionKey | : | c80253af86b33dfa450bbdb2a191fea3 | |
| Nonce | : |  | da7ddbe78b5f62b81d6847487e |
| NetKey | : | efb2255e6422d330088e09bb015ed707 | |
| NetKeyIndex | : | 0567 | |
| Flags | : | 00 | |
| IVIndex | : | 01020304 | |
| UnicastAddress | : | 0b0c | |
| ProvisioningData | : | efb2255e6422d330088e09bb015ed707056700010203040b0c | |
| Encrypted Provisioning Data | : | d0bd7f4a89a2ff6222af59a90a60ad58acfe3123356f5cec29 | |
| Provisioning Data MIC | : | 73e0ec50783b10c7 | |

|  |
| --- |
| Provisioning Data |

|  |  |  |
| --- | --- | --- |
| EncProvisioningData | : | d0bd7f4a89a2ff6222af59a90a60ad58acfe3123356f5cec29 |
| ProvisioningDataMIC | : | 73e0ec50783b10c7 |
| Message | : | 07d0bd7f4a89a2ff6222af59a90a60ad58acfe3123356f5cec2973e0ec |
|  |  | 50783b10c7 |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 05 |

|  |  |  |
| --- | --- | --- |
| Segment0 | : | 07d0bd7f4a89a2ff6222af59a90a60ad58acfe31 |
| Segment1 | : | 23356f5cec2973e0ec50783b10c7 |
| SegN | : | 01 |
| TotalLength | : | 0022 |
| FCS | : | 8b |
| Message0 | : | 23af5850050400228b07d0bd7f4a89a2ff6222af59a90a60ad58acfe31 |
| Message1 | : | 23af5850050623356f5cec2973e0ec50783b10c7 |

##### 8.7.12.1. PB-ADV Transaction Ack

The new device acknowledges the reception of the provisioning data transaction.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 05 |
| Message | : | 23af58500501 | |

#### 8.7.13. PB-ADV Provisioning Complete

The new device now indicates that it has successfully received and processed the provisioning data.

|  |
| --- |
| Provisioning Complete |

|  |  |  |  |
| --- | --- | --- | --- |
| Message | : | 08 | |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 84 |
| Segment0 | : | 08 | |
| SegN | : | 00 | |
| TotalLength | : | 0001 | |
| FCS | : | 3e | |
| Message0 | : | 23af5850840000013e08 | |

##### 8.7.13.1. PB-ADV Transaction Ack

The Provisioner acknowledges receiving the provisioning complete transaction from the new device.

|  |
| --- |
| PBADV Transaction Acknowledge |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 84 |
| Message | : | 23af58508401 | |

#### 8.7.14. PB-ADV Link Close

Finally, the Provisioner closes the PB-ADV session by using the Link Close message.

|  |
| --- |
| Link Close |

|  |  |  |
| --- | --- | --- |
| Reason | : | 00 |

|  |
| --- |
| Provisioning Control |

|  |  |  |  |
| --- | --- | --- | --- |
| LinkID | : | 23af5850 | |
| Transaction | : |  | 00 |
| Opcode | : | 02 (Link Close) | |
| Message | : | 23af5850000b00 | |

### 8.8. PB-GATT SAR sample data

The Provisioner is using PB-GATT to transport Provisioning PDU. The ATT_MTU is 23. The Type is Provisioning Public Key (0x03) and the value of the Parameters is:

|  |  |  |
| --- | --- | --- |
| Provisioning PDU Type | : | 03 (Provisioning Public Key) |
| Public Key X | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
| Public Key Y | : | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |

#### 8.8.1. 1st segment

|  |  |  |
| --- | --- | --- |
| ATT Opcode | : | 52 (Write Command) |
| ATT Handle | : | 0003 |
| ATT Value | : | 43032c31a47b5779809ef44cb5eaaf5c3e43d5f8 |

#### 8.8.2. 2nd segment

|  |  |  |
| --- | --- | --- |
| ATT Opcode | : | 52 (Write Command) |
| ATT Handle | : | 0003 |
| ATT Value | : | 83faad4a8794cb987e9b03745c78dd9195121838 |

#### 8.8.3. 3rd segment

|  |  |  |
| --- | --- | --- |
| ATT Opcode | : | 52 (Write Command) |
| ATT Handle | : | 0003 |
| ATT Value | : | 8398dfbecd52e2408e43871fd021109117bd3ed4 |

#### 8.8.4. 4th segment

|  |  |  |
| --- | --- | --- |
| ATT Opcode | : | 52 (Write Command) |
| ATT Handle | : | 0003 |
| ATT Value | : | c3eaf8437743715d4f |

### 8.9. Proxy configuration message sample data

The following sample data shows examples of proxy configuration messages.

#### 8.9.1. Set Filter Type

The Proxy client is configuring Proxy to use accept list filtering.

|  |  |  |
| --- | --- | --- |
| CTL | : | 01 |
| ProxyFilterPkt | : | 0000 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | d1aafb2a1a3c281cbdb0e960edfad852 | | | | | | |
| NID | : | 10 | | | | | | |
| EncryptionKey | : | 3a4fe84a6cc2c6a766ea93f1084d4039 | | | | | | |
| PrivacyKey | : | f695fcce709ccface4d8b7a1e6e39d25 | | | | | | |
| IV Index | : | 12345678 | | | | | | |
| Proxy nonce | : | 03000000010001000012345678 | | | | | | |
| IVI NID | : | 10 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | 000001 | | | | |
| SRC | : |  |  |  | 0001 | | | |
| DST | : |  |  |  |  | 0000 | | |
| TransportPDU | : |  |  |  |  |  | 0000 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 8b8c2851 | | |
| NetMIC | : |  |  |  |  |  |  | 2e792d3711f4b526 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456788b8c28512e792d |
| PECB | : | b86bd60ffbba6ca41e7109226f247a16 |
| CTL||TTL||SEQ||SRC | : | 800000010001 |

|  |  |  |
| --- | --- | --- |
| ProxyMessage | : | 10386bd60efbbb8b8c28512e792d3711f4b526 |
| ProxyPDU | : | 0210386bd60efbbb8b8c28512e792d3711f4b526 |

#### 8.9.2. DIRECTED_PROXY_CAPABILITIES_STATUS

A Directed Proxy Server sends a DIRECTED_PROXY_CAPABILITIES_STATUS message to report that directed proxy functionality is enabled and directed forwarding is used for retransmitting messages received from the Proxy Client over a subnet.

|  |  |  |
| --- | --- | --- |
| CTL | : | 01 |
| DirProxyCapsStatus | : | 040101 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| IV Index | : | 12345678 | | | | | | |
| Proxy nonce | : | 0300df03f00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df03f0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0000 | | |
| TransportPDU | : |  |  |  |  |  | 040101 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0f6d4e5324 | | |
| NetMIC | : |  |  |  |  |  |  | d385b9ef75d6936b |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| PrivacyRandom | : | 0000000000123456780f6d4e5324d385 |
| PECB | : | ba30e23c2a16947faba01d88f8428317 |
| preObfuscation | : | 80df03f00405 |

|  |  |  |
| --- | --- | --- |
| ProxyMessage | : | 683aefe1cc2e130f6d4e5324d385b9ef75d6936b |
|  | | |
| ProxyPDU | : | 02683aefe1cc2e130f6d4e5324d385b9ef75d6936b |

#### 8.9.3. DIRECTED_PROXY_CONTROL

A Directed Proxy Client sends a DIRECTED_PROXY_CONTROL message to configure the Directed Proxy Server to use directed forwarding for retransmitting messages received from the Directed Proxy Client over a subnet and originated by an element address within the provided unicast address range.

|  |  |  |
| --- | --- | --- |
| CTL | : | 01 |
| UseDirected | : | 01 |
| ProxyClientStartAddr | : | 0607 |
| ProxyClientNumElem | : | 03 |
| DirProxyCtrl | : | 0501860703 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| IV Index | : | 12345678 | | | | | | |
| Proxy nonce | : | 0300df04000607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df0400 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0000 | | |
| TransportPDU | : |  |  |  |  |  | 0501860703 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 02896f29a0ace2 | | |
| NetMIC | : |  |  |  |  |  |  | f0360a19bb04890d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| PrivacyRandom | : | 00000000001234567802896f29a0ace2 |
| PECB | : | 0048b82c42b228e298a389e5f55b3ddf |
| preObfuscation | : | 80df04000607 |

|  |  |  |
| --- | --- | --- |
| ProxyMessage | : | 688097bc2c44b502896f29a0ace2f0360a19bb04890d |
|  | | |
| ProxyPDU | : | 02688097bc2c44b502896f29a0ace2f0360a19bb04890d |

### 8.10. Composition Data sample data

This section provides examples of sample data for Composition Data pages states.

#### 8.10.1. Composition Data Page 0 sample data

This sample represents an example of Composition Data Page 0 (see [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0")). The data below is a sequence of octets.

|  |
| --- |
| 0C001A0001000800030000010501000000800100001003103F002A00 |

To help with parsing of this sequence of octets, it has been formatted with appropriate spacing characters.

|  |
| --- |
| 0C00 1A00 0100 0800 0300 0001 05 01 0000 0080 0100 0010 0310 3F002A00 |

### Note

Note: The composition data is little-endian.

The above Composition Data Page 0 can be described as follows:

* CID is 0x000C
* PID is 0x001A
* VID is 0x0001
* CRPL is 0x0008
* Features is 0x0003 – Relay and Friend features.
* Loc is “front” – 0x0100
* NumS is 5
* NumV is 1
* The Bluetooth SIG Models supported are:

  * 0x0000, 0x8000, 0x0001, 0x1000, 0x1003
* The Vendor Models supported are:

  * Company Identifier 0x003F and Model Identifier 0x002A

#### 8.10.2. Composition Data Page 1 sample data

This sample represents an example of Composition Data Page 1 (see [Section 4.2.2.2](index-en.html#UUID-ff76024f-e57d-3480-a98e-d0a5931cbd31 "4.2.2.2. Composition Data Page 1")). The data below is a sequence of octets and represents the example from [Section 4.2.2.2.1](index-en.html#UUID-4e1fc0d5-521d-ddf3-d45f-2b70018ff676 "4.2.2.2.1. Example of Composition Data Page 1").

|  |
| --- |
| 02010005000000010201000501170101 |

To help with parsing of this sequence of octets, the octets have been formatted with the appropriate spacing characters.

|  |
| --- |
| 02 01 00 050000 00 01 02 0100 050117 0101 |

[Table 8.1](index-en.html#UUID-53c62d4e-8e49-d489-9ea3-1b190333d1f1_Table_8.1 "Table 8.1. Composition Data Page 1 example values encoding") presents raw value inputs and encoded fields for the example Composition Data Page 1.

| Element | Field or model | Raw values | Encoded field |
| --- | --- | --- | --- |
| Element 1 | Number_S | 02 | 02 |
| Number_V | 01 | 01 |
| ModelA | 00, 00, 00 | 00 |
| ModelB | 01, 00, 01, 00, 00, 00 | 050000 |
| ModelV | 00, 00, 00 | 00 |
| Element 2 | Number_S | 01 | 01 |
| Number_V | 02 | 02 |
| ModelC | 01, 00, 00, 00 | 0100 |
| ModelX | 01, 00, 01, 01, 07, 02 | 050117 |
| ModelY | 01, 00, 00, 01 | 0101 |

Table 8.1. Composition Data Page 1 example values encoding

### 8.11. Certificate-based provisioning sample data

This section provides examples of sample data for various aspects of certificate-based provisioning, including certificate encoding, Certificate-Based Provisioning URI construction, and HTTP messaging.

#### 8.11.1. Device UUID

The following Device UUID, shown in hexadecimal digits, is used in all of the sample data for certificate-based provisioning:

|  |  |
| --- | --- |
|  | b0 9d c8 47 54 08 40 cc 9c 54 0f e8 c8 74 29 e7 |

##### 8.11.1.1. Canonical string representation

The following is the string representation of the Device UUID used in the sample data. The sample Device UUID is based on the UUID format in [[14](index-en.html#idp254774)].

|  |  |
| --- | --- |
|  | b09dc847-5408-40cc-9c54-0fe8c87429e7 |

#### 8.11.2. Device Certificate

This section provides an example of a Device Certificate, along with the corresponding device private key, which would be stored internally on the device and used when provisioning the device.

The device private key, in Privacy-Enhanced Mail (PEM) format, is as follows:

|  |
| --- |
| -----BEGIN EC PARAMETERS----- |
| BggqhkjOPQMBBw== |
| -----END EC PARAMETERS----- |
| -----BEGIN EC PRIVATE KEY----- |
| MHcCAQEEIJYX5gCdXJn853I/OPzB3EObLfIWkRyLY+tcxSb9+SppoAoGCCqGSM49 |
| AwEHoUQDQgAEjQKXzLPnx2sVLg+wJeTnHjkpoPCdK4xF8Wi4fhYEHeRLAky4BjT8 |
| 0HBsJKgz7dsutXFRUQMWyYk+5LS8hfbeWQ== |
| -----END EC PRIVATE KEY----- |

The Device Certificate structure and its PEM encoding are as follows. Note that the Common Name identifies the device as well as the device CID and PID values. The policy defined in the certificate policies extension is a NIST test policy.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Certificate: | | | | | |
|  | Data: | | | | |
|  |  | Version: 3 (0x2) | | | |
|  |  | Serial Number: 4096 (0x1000) | | | |
|  | Signature Algorithm: ecdsa-with-SHA256 | | | | |
|  |  | Issuer: C=FI, ST=Uusimaa, L=Espoo, O=Example Company, OU=Embedded Devices, | | | |
| CN=Example CA | | | | | |
|  |  | Validity | | | |
|  |  |  | Not Before: Mar 30 08:18:40 2023 GMT | | |
|  |  |  | Not After : Mar 29 08:18:40 2024 GMT | | |
|  |  | Subject: C=FI, ST=Uusimaa, L=Espoo, O=Example Company, OU=Embedded Devices, | | | |
| CN=b09dc847-5408-40cc-9c54-0fe8c87429e7 BCID:8001 BPID:03ff | | | | | |
|  |  | Subject Public Key Info: | | | |
|  |  |  | Public Key Algorithm: id-ecPublicKey | | |
|  |  |  |  | Public-Key: (256 bit) | |
|  |  |  |  | pub: | |
|  |  |  |  |  | 04:8d:02:97:cc:b3:e7:c7:6b:15:2e:0f:b0:25:e4: |
|  |  |  |  |  | e7:1e:39:29:a0:f0:9d:2b:8c:45:f1:68:b8:7e:16: |
|  |  |  |  |  | 04:1d:e4:4b:02:4c:b8:06:34:fc:d0:70:6c:24:a8: |
|  |  |  |  |  | 33:ed:db:2e:b5:71:51:51:03:16:c9:89:3e:e4:b4: |
|  |  |  |  |  | bc:85:f6:de:59 |
|  |  |  |  | ASN1 OID: prime256v1 | |
|  |  |  |  | NIST CURVE: P-256 | |
|  |  | X509v3 extensions: | | | |
|  |  |  | X509v3 Basic Constraints: | | |
|  |  |  |  | CA:FALSE | |
|  |  |  | X509v3 Key Usage: | | |
|  |  |  |  | Key Agreement | |
|  |  |  | X509v3 Subject Key Identifier: | | |
|  |  |  |  | 28:BC:42:6A:68:DB:63:96:70:85:71:E4:CF:C9:72:1C:E9:8B:68:15 | |
|  |  |  | X509v3 Authority Key Identifier: | | |
|  |  |  |  | keyid:87:73:70:B7:D3:04:A1:05:EC:0D:0F:CD:4D:40:59:73:63:20:DD:43 | |
|  | | | | | |
|  |  |  | X509v3 Certificate Policies: critical | | |
|  |  |  |  | Policy: 2.16.840.1.101.3.2.1.48.1 | |
|  | | | | | |
|  | Signature Algorithm: ecdsa-with-SHA256 | | | | |
|  |  | 30:45:02:21:00:a1:d6:e9:78:79:5d:2f:6a:36:8f:d6:ab:f5: | | | |
|  |  | b3:e1:17:ae:2f:04:7d:56:a0:0a:3a:90:7d:25:42:74:a0:47 | | | |
|  |  | c2:02:20:2d:ac:81:29:8c:21:ac:75:2e:16:13:39:b0:68:bb: | | | |
|  |  | b9:d0:54:9b:f5:0d:94:7b:bd:8d:0e:11:a7:18:d6:c4:77 | | | |

|  |
| --- |
| -----BEGIN CERTIFICATE----- |
| MIIChzCCAi2gAwIBAgICEAAwCgYIKoZIzj0EAwIweTELMAkGA1UEBhMCRkkxEDAO |
| BgNVBAgMB1V1c2ltYWExDjAMBgNVBAcMBUVzcG9vMRgwFgYDVQQKDA9FeGFtcGxl |
| IENvbXBhbnkxGTAXBgNVBAsMEEVtYmVkZGVkIERldmljZXMxEzARBgNVBAMMCkV4 |
| YW1wbGUgQ0EwHhcNMjMwMzMwMDgxODQwWhcNMjQwMzI5MDgxODQwWjCBpzELMAkG |
| A1UEBhMCRkkxEDAOBgNVBAgMB1V1c2ltYWExDjAMBgNVBAcMBUVzcG9vMRgwFgYD |
| VQQKDA9FeGFtcGxlIENvbXBhbnkxGTAXBgNVBAsMEEVtYmVkZGVkIERldmljZXMx |
| QTA/BgNVBAMMOGIwOWRjODQ3LTU0MDgtNDBjYy05YzU0LTBmZThjODc0MjllNyBC |
| Q0lEOjgwMDEgQlBJRDowM2ZmMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEjQKX |
| zLPnx2sVLg+wJeTnHjkpoPCdK4xF8Wi4fhYEHeRLAky4BjT80HBsJKgz7dsutXFR |
| UQMWyYk+5LS8hfbeWaN2MHQwCQYDVR0TBAIwADALBgNVHQ8EBAMCAwgwHQYDVR0O |
| BBYEFCi8Qmpo22OWcIVx5M/Jchzpi2gVMB8GA1UdIwQYMBaAFIdzcLfTBKEF7A0P |
| zU1AWXNjIN1DMBoGA1UdIAEB/wQQMA4wDAYKYIZIAWUDAgEwATAKBggqhkjOPQQD |
| AgNIADBFAiEAodbpeHldL2o2j9ar9bPhF64vBH1WoAo6kH0lQnSgR8ICIC2sgSmM |
| Iax1LhYTObBou7nQVJv1DZR7vY0OEacY1sR3 |
| -----END CERTIFICATE----- |

DER-formatted Device Certificate contents in hexadecimal are shown below. Note that the first column is a hexadecimal offset value, not part of the actual data.

0000000    30 82 02 87 30 82 02 2d a0 03 02 01 02 02 02 10
0000010    00 30 0a 06 08 2a 86 48 ce 3d 04 03 02 30 79 31
0000020    0b 30 09 06 03 55 04 06 13 02 46 49 31 10 30 0e
0000030    06 03 55 04 08 0c 07 55 75 73 69 6d 61 61 31 0e
0000040    30 0c 06 03 55 04 07 0c 05 45 73 70 6f 6f 31 18
0000050    30 16 06 03 55 04 0a 0c 0f 45 78 61 6d 70 6c 65
0000060    20 43 6f 6d 70 61 6e 79 31 19 30 17 06 03 55 04
0000070    0b 0c 10 45 6d 62 65 64 64 65 64 20 44 65 76 69
0000080    63 65 73 31 13 30 11 06 03 55 04 03 0c 0a 45 78
0000090    61 6d 70 6c 65 20 43 41 30 1e 17 0d 32 33 30 33
00000a0    33 30 30 38 31 38 34 30 5a 17 0d 32 34 30 33 32
00000b0    39 30 38 31 38 34 30 5a 30 81 a7 31 0b 30 09 06
00000c0    03 55 04 06 13 02 46 49 31 10 30 0e 06 03 55 04
00000d0    08 0c 07 55 75 73 69 6d 61 61 31 0e 30 0c 06 03
00000e0    55 04 07 0c 05 45 73 70 6f 6f 31 18 30 16 06 03
00000f0    55 04 0a 0c 0f 45 78 61 6d 70 6c 65 20 43 6f 6d
0000100    70 61 6e 79 31 19 30 17 06 03 55 04 0b 0c 10 45
0000110    6d 62 65 64 64 65 64 20 44 65 76 69 63 65 73 31
0000120    41 30 3f 06 03 55 04 03 0c 38 62 30 39 64 63 38
0000130    34 37 2d 35 34 30 38 2d 34 30 63 63 2d 39 63 35
0000140    34 2d 30 66 65 38 63 38 37 34 32 39 65 37 20 42
0000150    43 49 44 3a 38 30 30 31 20 42 50 49 44 3a 30 33
0000160    66 66 30 59 30 13 06 07 2a 86 48 ce 3d 02 01 06
0000170    08 2a 86 48 ce 3d 03 01 07 03 42 00 04 8d 02 97
0000180    cc b3 e7 c7 6b 15 2e 0f b0 25 e4 e7 1e 39 29 a0
0000190    f0 9d 2b 8c 45 f1 68 b8 7e 16 04 1d e4 4b 02 4c
00001a0    b8 06 34 fc d0 70 6c 24 a8 33 ed db 2e b5 71 51
00001b0    51 03 16 c9 89 3e e4 b4 bc 85 f6 de 59 a3 76 30
00001c0    74 30 09 06 03 55 1d 13 04 02 30 00 30 0b 06 03
00001d0    55 1d 0f 04 04 03 02 03 08 30 1d 06 03 55 1d 0e
00001e0    04 16 04 14 28 bc 42 6a 68 db 63 96 70 85 71 e4
00001f0    cf c9 72 1c e9 8b 68 15 30 1f 06 03 55 1d 23 04
0000200    18 30 16 80 14 87 73 70 b7 d3 04 a1 05 ec 0d 0f
0000210    cd 4d 40 59 73 63 20 dd 43 30 1a 06 03 55 1d 20
0000220    01 01 ff 04 10 30 0e 30 0c 06 0a 60 86 48 01 65
0000230    03 02 01 30 01 30 0a 06 08 2a 86 48 ce 3d 04 03
0000240    02 03 48 00 30 45 02 21 00 a1 d6 e9 78 79 5d 2f
0000250    6a 36 8f d6 ab f5 b3 e1 17 ae 2f 04 7d 56 a0 0a
0000260    3a 90 7d 25 42 74 a0 47 c2 02 20 2d ac 81 29 8c
0000270    21 ac 75 2e 16 13 39 b0 68 bb b9 d0 54 9b f5 0d
0000280    94 7b bd 8d 0e 11 a7 18 d6 c4 77

#### 8.11.3. Out-of-band data delivery over the Internet

This section provides examples of Certificate-Based Provisioning URI construction, as well as an example HTTP request and response for retrieving certificate data from a server.

##### 8.11.3.1. Certificate-Based Provisioning URI

If the domain name for the vendor’s server that contains the OOB data is “mesh.example.com” and the path for the data is simply “/oob”, the following Certificate-Based Provisioning Base URI would be used:

|  |  |
| --- | --- |
|  | https://mesh.example.com/oob |

The following sample Certificate-Based Provisioning URI retrieves the Device Certificate only for the device identified by the UUID query:

|  |  |
| --- | --- |
|  | https://mesh.example.com/oob?uuid=b09dc847-5408-40cc-9c54-0fe8c87429e7&content=device-certificate |

The following sample Certificate-Based Provisioning URI retrieves all data that the server has for the device identified by the UUID query:

|  |  |
| --- | --- |
|  | https://mesh.example.com/oob?uuid=b09dc847-5408-40cc-9c54-0fe8c87429e7 |

##### 8.11.3.2. Request

The following sample is an example of an HTTP request for a certificate:

|  |
| --- |
| GET /oob?uuid=b09dc847-5408-40cc-9c54-0fe8c87429e7&amp;content=device-certificate HTTP/1.1 |
| Accept: */* |
| Accept-Encoding: identity |
| Host: mesh.example.com |

##### 8.11.3.3. Response

The following sample is an example of an HTTP response with a certificate in DER format as the payload:

|  |
| --- |
| HTTP/1.1 200 OK |
| Content-Type: application/pkix-cert |
| Date: Mon, 17 Oct 2022 09:26:15 GMT |
| Last-Modified: Mon, 17 Oct 2022 09:26:15 GMT |
| Content-Length: 685 |
| [DER contents redacted for brevity] |

#### 8.11.4. NFC tag contents

This section provides examples of URI data encoded as NFC NDEF messages that can be written on NFC tags.

##### 8.11.4.1. URI record

If the domain name of the certificate server is “mesh.example.com” and the URI path for certificate data is “/oob”, the Certificate-Based Provisioning Base URI “https://mesh.example.com/oob” appended with a query component with the device UUID filled in would be represented as an NFC URI record containing the following
hexadecimal bytes. Note that whitespace and comments (identified by a semicolon followed by the explanatory text) are not part of the message contents.

|  |  |  |
| --- | --- | --- |
| d1 01 3f | ; | Record header |
| 55 | ; | Record type |
| 04 6d 65 73 68 2e 65 78 61 6d 70 6c 65 2e 63 6f | ; | Record payload |
| 6d 2f 6f 6d 62 3f 75 75 69 64 3d 62 30 39 64 63 | ; | (encoded URI) |
| 38 34 37 2d 35 34 30 38 2d 34 30 63 63 2d 39 63 | ; |  |
| 35 34 2d 30 66 65 38 63 38 37 34 32 39 65 37 | ; |  |

The URI record above is also a self-contained NDEF message, which can be written to an NFC tag as it is. For details of the NDEF message structure, refer to [[16](index-en.html#idp254780)]; for details of the URI record structure, refer to [[18](index-en.html#idp254786)].

#### 8.11.5. Barcode contents

This section provides examples of QR codes that contain Certificate-Based Provisioning URI information. The technology and the encoding parameters in the examples were chosen only to illustrate a potential implementation, and are not requirements. The choice of technology and encoding parameters is an implementation detail.

##### 8.11.5.1. Certificate-Based Provisioning URI

In [Figure 8.1](index-en.html#UUID-ab7e0377-e2dd-9d10-f75f-e0e9829972d2_Figure_8.1 "Figure 8.1. Example QR code that uses 8-bit encoding"), the image is the QR code generated for the Certificate-Based Provisioning Base URI <https://mesh.example.com/oob>, appended with a UUID query containing the Device UUID. The QR code has been generated with a medium level of error correction using 8-bit encoding.

|  |
| --- |
| Example QR code that uses 8-bit encoding |

Figure 8.1. Example QR code that uses 8-bit encoding

If the Certificate-Based Provisioning Base URI path is uppercase, or if the server can handle the URI path in a case-insensitive manner, the string “HTTPS://MESH.EXAMPLE.COM/OOB” can be encoded using mostly alphanumeric encoding in a smaller space, as illustrated by the image in [Figure 8.2](index-en.html#UUID-ab7e0377-e2dd-9d10-f75f-e0e9829972d2_Figure_8.2 "Figure 8.2. Example QR code that uses alphanumeric encoding").

|  |
| --- |
| Example QR code that uses alphanumeric encoding |

Figure 8.2. Example QR code that uses alphanumeric encoding

### 8.12. Subnet bridging sample data

This section provides sample data that can be used to verify implementations of subnet bridge functionality.

#### 8.12.1. SUBNET_BRIDGE_GET

A Bridge Configuration Client sends a SUBNET_BRIDGE_GET message to a Bridge Configuration Server to read its Subnet Bridge state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b1 (SUBNET_BRIDGE_GET) |
| Access message | : | 80b1 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0410 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04100405060712345678 |
| EncAccessMessage | : | 18b0 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | b6618b2b |
| UpperTransportPDU | : | 18b0b6618b2b |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0410 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 18b0b6618b2b | |
| LowerTransportPDU | : | 0018b0b6618b2b | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0410 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 0018b0b6618b2b | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04100405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0410 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 0018b0b6618b2b |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5a9b96d5df3adcdb54 | |
| NetMIC | : |  |  |  |  |  | 13db54b8 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785a9b96d5df3adc |
| PECB | : | 213725c8edc91fd0b28b9a774c4cd63b |
| CTL||TTL||SEQ||SRC | : | 7fdf04100405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 685ee821d8e9cc5a9b96d5df3adcdb5413db54b8 |

#### 8.12.2. SUBNET_BRIDGE_SET

A Bridge Configuration Client sends a SUBNET_BRIDGE_SET message to a Bridge Configuration Server to enable subnet bridge functionality.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b2 (SUBNET_BRIDGE_SET) |
| Subnet_Bridge | : | 01 (enabled) |
| Access message | : | 80b201 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0420 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04200405060712345678 |
| EncAccessMessage | : | 4b39a5 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 9c510751 |
| UpperTransportPDU | : | 4b39a59c510751 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0420 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 4b39a59c510751 | |
| LowerTransportPDU | : | 004b39a59c510751 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0420 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 004b39a59c510751 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04200405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0420 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 004b39a59c510751 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 8841181f05eaf128c7c8 | |
| NetMIC | : |  |  |  |  |  | 1e1af02c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456788841181f05eaf1 |
| PECB | : | 0948f1e69d358dd7fb0d667ff00fc3eb |
| CTL||TTL||SEQ||SRC | : | 7fdf04200405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 687697f5c699308841181f05eaf128c7c81e1af02c |

#### 8.12.3. SUBNET_BRIDGE_STATUS

A Bridge Configuration Server receives a SUBNET_BRIDGE_GET message or a SUBNET_BRIDGE_SET message from a Bridge Configuration Client and responds with a SUBNET_BRIDGE_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b3 (SUBNET_BRIDGE_STATUS) |
| Subnet_Bridge | : | 01 (enabled) |
| Access message | : | 80b301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0430 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df04300607040512345678 |
| EncAccessMessage | : | 426c2a |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 5b3a9ac6 |
| UpperTransportPDU | : | 426c2a5b3a9ac6 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0430 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 426c2a5b3a9ac6 | |
| LowerTransportPDU | : | 00426c2a5b3a9ac6 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0430 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 00426c2a5b3a9ac6 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04300607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0430 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 00426c2a5b3a9ac6 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | c74097ec51d32b554ff4 | |
| NetMIC | : |  |  |  |  |  | cf513a18 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678c74097ec51d32b |
| PECB | : | 1759a7a2a9552245edceb0e51be266c8 |
| CTL||TTL||SEQ||SRC | : | 7fdf04300607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 686886a392af52c74097ec51d32b554ff4cf513a18 |

#### 8.12.4. BRIDGING_TABLE_ADD

A Bridge Configuration Client sends a BRIDGING_TABLE_ADD message to a Bridge Configuration Server to add or update an entry in the Bridging Table state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b4 (BRIDGING_TABLE_ADD) |
| Directions | : | 02 (both directions) |
| NetKeyIndex1 | : | 123 |
| NetKeyIndex2 | : | 456 |
| Address1 | : | 0aaa |
| Address2 | : | 0bbb |
| Access message | : | 80b402236145aa0abb0b |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0440 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04400405060712345678 |
| EncAccessMessage | : | a68f8ac9d4a2ee3ecb52 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 388821a9 |
| UpperTransportPDU | : | a68f8ac9d4a2ee3ecb52388821a9 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0440 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | a68f8ac9d4a2ee3ecb52388821a9 | |
| LowerTransportPDU | : | 00a68f8ac9d4a2ee3ecb52388821a9 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0440 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 00a68f8ac9d4a2ee3ecb52388821a9 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04400405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0440 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 00a68f8ac9d4a2ee3ecb52388821a9 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | a2fee57d9aad3e6f1c634cd470ddb6b5cd | |
| NetMIC | : |  |  |  |  |  | c18edfe2 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678a2fee57d9aad3e |
| PECB | : | 3e5a290bae10509fcb0b2fa82e5f70b8 |
| CTL||TTL||SEQ||SRC | : | 7fdf04400405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6841852d4baa15a2fee57d9aad3e6f1c634cd470ddb6b5cdc18edfe2 |

#### 8.12.5. BRIDGING_TABLE_REMOVE

A Bridge Configuration Client sends a BRIDGING_TABLE_REMOVE message to a Bridge Configuration Server to remove an entry from the Bridging Table state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b5 (BRIDGING_TABLE_REMOVE) |
| NetKeyIndex1 | : | 123 |
| NetKeyIndex2 | : | 456 |
| Address1 | : | 0aaa |
| Address2 | : | 0bbb |
| Access message | : | 80b5236145aa0abb0b |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0450 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04500405060712345678 |
| EncAccessMessage | : | 5cc0e1ae66c89d37d2 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 0cf6551d |
| UpperTransportPDU | : | 5cc0e1ae66c89d37d20cf6551d |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0450 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 5cc0e1ae66c89d37d20cf6551d | |
| LowerTransportPDU | : | 005cc0e1ae66c89d37d20cf6551d | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0450 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 005cc0e1ae66c89d37d20cf6551d | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04500405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0450 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 005cc0e1ae66c89d37d20cf6551d |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | fa3c9ad67cf0c9a084fed9414844287c | |
| NetMIC | : |  |  |  |  |  | b28daca2 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678fa3c9ad67cf0c9 |
| PECB | : | f56130d26d7e8bc9c43d3021c953e9cb |
| CTL||TTL||SEQ||SRC | : | 7fdf04500405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 688abe3482697bfa3c9ad67cf0c9a084fed9414844287cb28daca2 |

#### 8.12.6. BRIDGING_TABLE_STATUS

A Bridge Configuration Server receives a BRIDGING_TABLE_REMOVE message from a Bridge Configuration Client and responds with a BRIDGING_TABLE_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b6 (BRIDGING_TABLE_STATUS) |
| Status | : | 00 (Success) |
| Current_Directions | : | 00 (no direction) |
| NetKeyIndex1 | : | 123 |
| NetKeyIndex2 | : | 456 |
| Address1 | : | 0aaa |
| Address2 | : | 0bbb |
| Access message | : | 80b60000236145aa0abb0b |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0460 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df04600607040512345678 |
| EncAccessMessage | : | 772ee99a84a87b296a7fa3 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 4b429b1d |
| UpperTransportPDU | : | 772ee99a84a87b296a7fa34b429b1d |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0460 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 772ee99a84a87b296a7fa34b429b1d | |
| LowerTransportPDU | : | 00772ee99a84a87b296a7fa34b429b1d | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0460 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 00772ee99a84a87b296a7fa34b429b1d | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04600607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0460 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 00772ee99a84a87b296a7fa34b429b1d |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5e3c223fdabec9ac2da45dd156114810c8aa | |
| NetMIC | : |  |  |  |  |  | bb906e72 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785e3c223fdabec9 |
| PECB | : | 5e73a51cf5d360ee89a14845fcd9aadf |
| CTL||TTL||SEQ||SRC | : | 7fdf04600607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6821aca17cf3d45e3c223fdabec9ac2da45dd156114810c8aabb906e72 |

#### 8.12.7. BRIDGED_SUBNETS_GET

A Bridge Configuration Client sends a BRIDGED_SUBNETS_GET message to a Bridge Configuration Server to get a filtered list of NetKey Indexes pairs extracted from the Bridging Table state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b6 (BRIDGED_SUBNETS_GET) |
| Filter | : | 1 |
| NetKeyIndex | : | 123 |
| Start_Index | : | 00 |
| Access message | : | 80b7311200 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0470 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04700405060712345678 |
| EncAccessMessage | : | 23a1542d07 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 90a51f95 |
| UpperTransportPDU | : | 23a1542d0790a51f95 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0470 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 23a1542d0790a51f95 | |
| LowerTransportPDU | : | 0023a1542d0790a51f95 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0470 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 0023a1542d0790a51f95 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04700405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0470 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 0023a1542d0790a51f95 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5581a47b26b0d671b1a88cb5 | |
| NetMIC | : |  |  |  |  |  | f7dc655b |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785581a47b26b0d6 |
| PECB | : | af01a3ead51349a6b03c797cf6c329ec |
| CTL||TTL||SEQ||SRC | : | 7fdf04700405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68d0dea79ad1165581a47b26b0d671b1a88cb5f7dc655b |

#### 8.12.8. BRIDGED_SUBNETS_LIST

A Bridge Configuration Server receives a BRIDGED_SUBNETS_GET message from a Bridge Configuration Client and responds with a BRIDGED_SUBNETS_LIST message. The message is sent in two segments.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 80b8 (BRIDGED_SUBNETS_LIST) |
| Filter | | | : | 1 |
| NetKeyIndex | | | : | 123 |
| Start_Index | | | : | 00 |
| Bridged_Subnets_List | | | | |
|  | (#00) | NetKeyIndex1 | : | 123 |
|  |  | NetKeyIndex2 | : | 456 |
|  | (#01) | NetKeyIndex1 | : | 123 |
|  |  | NetKeyIndex2 | : | 789 |
| Access message | | | : | 80b8311200236145239178 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0480 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df04800607040512345678 |
| EncAccessMessage | : | e882efc004e2bd903e46ae |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 014f4a8f |
| UpperTransportPDU | : | e882efc004e2bd903e46ae014f4a8f |
| Segment#00 | : | e882efc004e2bd903e46ae01 |
| Segment#01 | : | 4f4a8f |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0480 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0480 | |
| SegO | : | 00 | |
| SegN | : | 01 | |
| Header | : | 80120001 | |
| Segment#00 | : | e882efc004e2bd903e46ae01 | |
| LowerTransportPDU | : | 80120001e882efc004e2bd903e46ae01 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0480 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 80120001e882efc004e2bd903e46ae01 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04800607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0480 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 80120001e882efc004e2bd903e46ae01 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 32242b358a924a1853198dfee8c00fc8b182 | |
| NetMIC | : |  |  |  |  |  | e033df41 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567832242b358a924a |
| PECB | : | 710638dbc0c70df438314443cf1828fb |
| CTL || TTL || SEQ || SRC | : | 7fdf04800607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 680ed93c5bc6c032242b358a924a1853198dfee8c00fc8b182e033df41 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0481 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0480 | |
| SegO | : | 01 | |
| SegN | : | 01 | |
| Header | : | 80120021 | |
| Segment#01 | : |  | 4f4a8f |
| LowerTransportPDU | : | 801200214f4a8f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0481 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 801200214f4a8f | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04810607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0481 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 801200214f4a8f |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | ae381b126f72e7eb1d | |
| NetMIC | : |  |  |  |  |  | 04968a3d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678ae381b126f72e7 |
| PECB | : | 9b3be8f90ac7191b9a2fdce77cc2fec9 |
| CTL||TTL||SEQ||SRC | : | 7fdf04810607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68e4e4ec780cc0ae381b126f72e7eb1d04968a3d |

#### 8.12.9. BRIDGING_TABLE_GET

A Bridge Configuration Client sends a BRIDGING_TABLE_GET message to a Bridge Configuration Server to get a filtered list of the Bridging Table state entries.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b9 (BRIDGING_TABLE_GET) |
| NetKeyIndex1 | : | 123 |
| NetKeyIndex2 | : | 456 |
| Start_Index | : | 0000 |
| Access message | : | 80b92361450000 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df0490 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04900405060712345678 |
| EncAccessMessage | : | 5afcefddd74091 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 11d92b23 |
| UpperTransportPDU | : | 5afcefddd7409111d92b23 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df0490 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 5afcefddd7409111d92b23 | |
| LowerTransportPDU | : | 005afcefddd7409111d92b23 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df0490 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 005afcefddd7409111d92b23 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04900405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df0490 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 005afcefddd7409111d92b23 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | a8f77dfdc72477cd52a79430468f | |
| NetMIC | : |  |  |  |  |  | b4aa33a4 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678a8f77dfdc72477 |
| PECB | : | 65e5d73970888c077a42692e5649a98c |
| CTL || TTL || SEQ || SRC | : | 7fdf04900405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681a3ad3a9748da8f77dfdc72477cd52a79430468fb4aa33a4 |

#### 8.12.10. BRIDGING_TABLE_LIST

A Bridge Configuration Server receives a BRIDGING_TABLE_GET message from a Bridge Configuration Client and responds with a BRIDGING_TABLE_LIST message. The message is sent in three segments.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 80ba (BRIDGING_TABLE_LIST) |
| Status | | | : | 00 (Success) |
| NetKeyIndex1 | | | : | 123 |
| NetKeyIndex2 | | | : | 456 |
| Start_Index | | | : | 0000 |
| Bridged_Addresses_List | | | | |
|  | (#00) | Address1 | : | 0aaa |
|  |  | Address2 | : | 0bbb |
|  |  | Directions | : | 02 (both directions) |
|  | (#01) | Address1 | : | 0aaa |
|  |  | Address2 | : | 0ccc |
|  |  | Directions | : | 01 (from Address1 to Address2) |
|  | (#02) | Address1 | : | 0ddd |
|  |  | Address2 | : | 0ccc |
|  |  | Directions | : | 02 (both directions) |
| Access message | | | : | 80ba002361450000aa0abb0b02aa0acc0c01dd0dcc0c02 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df04a0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df04a00607040512345678 |
| EncAccessMessage | : | 33138340c63603fbd056c7fd891c39c4a6431d9e4fb947 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | cea57b7b |
| UpperTransportPDU | : | 33138340c63603fbd056c7fd891c39c4a6431d9e4fb947cea57b7b |
| Segment#00 | : | 33138340c63603fbd056c7fd |
| Segment#01 | : | 891c39c4a6431d9e4fb947ce |
| Segment#02 | : | a57b7b |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df04a0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 04a0 | |
| SegO | : | 00 | |
| SegN | : | 02 | |
| Header | : | 80128002 | |
| Segment#00 | : | 33138340c63603fbd056c7fd | |
| LowerTransportPDU | : | 8012800233138340c63603fbd056c7fd | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df04a0 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 8012800233138340c63603fbd056c7fd | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04a00607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df04a0 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 8012800233138340c63603fbd056c7fd |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b6720d5b9b7ac1ccb468d1aee55420a4a74c | |
| NetMIC | : |  |  |  |  |  | 9b6c7f1c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678b6720d5b9b7ac1 |
| PECB | : | 892f613f2533969d6615ea7235cc9f0b |
| CTL || TTL || SEQ || SRC | : | 7fdf04a00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68f6f0659f2334b6720d5b9b7ac1ccb468d1aee55420a4a74c9b6c7f1c |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df04a1 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 04a0 | |
| SegO | : | 01 | |
| SegN | : | 02 | |
| Header | : | 80128022 | |
| Segment#01 | : | 891c39c4a6431d9e4fb947ce | |
| LowerTransportPDU | : | 80128022891c39c4a6431d9e4fb947ce | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df04a1 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 80128022891c39c4a6431d9e4fb947ce | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04a10607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df04a1 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 80128022891c39c4a6431d9e4fb947ce |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d92402cca50bab611a23e691f21532b32273 | |
| NetMIC | : |  |  |  |  |  | 6d2ca780 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678d92402cca50bab |
| PECB | : | 852dd12de522933b8705278c5a2ea382 |
| CTL||TTL||SEQ||SRC | : | 7fdf04a10607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68faf2d58ce325d92402cca50bab611a23e691f21532b322736d2ca780 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df04a2 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 04a0 | |
| SegO | : | 02 | |
| SegN | : | 02 | |
| Header | : | 80128042 | |
| Segment#02 | : | a57b7b | |
| LowerTransportPDU | : | 80128042a57b7b | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df04a2 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 80128042a57b7b | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04a20607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df04a2 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 80128042a57b7b |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 7b79793e3c5ea123f0 | |
| NetMIC | : |  |  |  |  |  | 5340bacc |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456787b79793e3c5ea1 |
| PECB | : | 3cbf0fa26b7e256c3ff4a9c24495ad96 |
| CTL || TTL || SEQ || SRC | : | 7fdf04a20607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6843600b006d797b79793e3c5ea123f05340bacc |

#### 8.12.11. BRIDGING_TABLE_SIZE_GET

A Bridge Configuration Client sends a BRIDGING_TABLE_SIZE_GET message to a Bridge Configuration Server to read the Bridging Table Size state.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 80bb (BRIDGING_TABLE_SIZE_GET) |
| Access message | | | : | 80bb |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df04b0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df04b00405060712345678 |
| EncAccessMessage | : | 6bda |
| TransMIC Size | : | 32 bits |
| TransMIC | : | d8446576 |
| UpperTransportPDU | : | 6bdad8446576 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df04b0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 6bdad8446576 | |
| LowerTransportPDU | : | 006bdad8446576 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df04b0 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | 0607 | | | | | |
| LowerTransportPDU | : | 006bdad8446576 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04b00405000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df04b0 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | 0607 | |
| TransportPDU | : |  |  |  |  |  | 006bdad8446576 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0868603e8c88880066 | |
| NetMIC | : |  |  |  |  |  | 10589fbe |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456780868603e8c8888 |
| PECB | : | 7b0050c1d349e8e7cea97ddd7c102bb2 |
| CTL||TTL||SEQ||SRC | : | 7fdf04b00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6804df5471d74c0868603e8c8888006610589fbe |

#### 8.12.12. BRIDGING_TABLE_SIZE_STATUS

A Bridge Configuration Server receives a BRIDGING_TABLE_SIZE_GET message from a Bridge Configuration Client and responds with a BRIDGING_TABLE_SIZE_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80bc (BRIDGING_TABLE_SIZE_STATUS) |
| Bridging_Table_Size | : | 0100 |
| Access message | : | 80bc0001 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 7f |
| SEQ | : | df04c0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df04c00607040512345678 |
| EncAccessMessage | : | a5f01428 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 53761e58 |
| UpperTransportPDU | : | a5f0142853761e58 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 7f | |
| SEQ | : | df04c0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | a5f0142853761e58 | |
| LowerTransportPDU | : | 00a5f0142853761e58 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 00 | | | | | |
| TTL | : | 7f | | | | | |
| SEQ | : | df04c0 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 0405 | | | | | |
| LowerTransportPDU | : | 00a5f0142853761e58 | | | | | |
| NID | : | 68 | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | |
| Network nonce | : | 007fdf04c00607000012345678 | | | | | |
| IVI NID | : | 68 | | | | | |
| CTL TTL | : |  | 7f | | | | |
| SEQ | : |  |  | df04c0 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 0405 | |
| TransportPDU | : |  |  |  |  |  | 00a5f0142853761e58 |
| NetMIC Size | : | 32 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0fbd2168a5dc0bbae2543a | |
| NetMIC | : |  |  |  |  |  | 47bb53c5 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456780fbd2168a5dc0b |
| PECB | : | cdf89ffd2a6ac08d5315177cbbf29938 |
| CTL||TTL||SEQ||SRC | : | 7fdf04c00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68b2279b3d2c6d0fbd2168a5dc0bbae2543a47bb53c5 |

### 8.13. Provisioning Record Retrieval

This sample represents a part of a message exchange over PB-ADV for querying provisioning records and retrieving the device certificate record contents from an unprovisioned device.

The provisioning link has been opened, and the link ID is 0x1289ef.

The Provisioner is requesting the device certificate, so the Device Certificate Record ID is being used in the Provisioning Record Request PDU.

The Provisioner is requesting the certificate in 58-byte fragments.

The length of the device certificate data is 695 bytes. The certificate data is the sample data presented in [Section 8.11.2](index-en.html#UUID-b0d84512-6e92-49e3-bda1-a348cb246ab5 "8.11.2. Device Certificate").

#### 8.13.1. PB-ADV Provisioning Records Get

The Provisioner requests the list of provisioning records the unprovisioned device supports.

|  |
| --- |
| Provisioning Records Get |
|  |
| Message : 0c |
|  |
| LinkID : 001289ef |
| Transaction : 00 |
|  |
| Segment0 : 0c |
| SegN : 00 |
| PDU Length : 0001 |
| FCS : 39 |
| Message0 : 001289ef00000001390c |

#### 8.13.2. PB-ADV Transaction Ack

The unprovisioned device acknowledges the transaction for requesting provisioning records.

|  |
| --- |
| PBADV Transaction Acknowledge |
|  |
| LinkID : 001289ef |
| Transaction : 00 |
| Message : 001289ef0001 |

#### 8.13.3. PB-ADV Provisioning Records List

The unprovisioned device responds with the list of provisioning records it supports. In this case, the device stores the Device Certificate record and one Intermediate Certificate record.

|  |
| --- |
| Provisioning Records List |
|  |
| Extensions : 0000 (no extensions) |
| Records List : 00010002 (Device Certificate, Intermediate Certificate 1) |
| Message : 0d000000010002 |
|  |
| LinkID : 001289ef |
| Transaction : 80 |
|  |
| Segment0 : 0d000000010002 |
| SegN : 00 |
| PDU Length : 0007 |
| FCS : f1 |
| Message0 : 001289ef80000007f10d000000010002 |

#### 8.13.4. PB-ADV Transaction Ack

The Provisioner acknowledges the transaction for provisioning records list.

|  |
| --- |
| PBADV Transaction Acknowledge |
|  |
| LinkID : 001289ef |
| Transaction : 80 |
| Message : 001289ef8001 |

#### 8.13.5. PB-ADV Device Certificate Record Request

The Provisioner requests a 58-byte fragment of the Device Certificate record starting at offset 0.

|  |
| --- |
| Provisioning Record Request |
|  |
| Record ID : 0001 |
| Fragment Offset : 0000 |
| Fragment Maximum Size : 003a |
| Message : 0a00010000003a |
|  |
| LinkID : 001289ef |
| Transaction : 01 |
|  |
| Segment0 : 0a00010000003a |
| SegN : 00 |
| PDU Length : 0007 |
| FCS : 94 |
| Message0 : 001289ef01000007940a00010000003a |

#### 8.13.6. PB-ADV Transaction Ack

The unprovisioned device acknowledges the transaction for requesting Device Certificate record fragment.

|  |
| --- |
| PBADV Transaction Acknowledge |
|  |
| LinkID : 001289ef |
| Transaction : 01 |
| Message : 001289ef0101 |

#### 8.13.7. PB-ADV Device Certificate Record Response

The unprovisioned device responds to the certificate request by sending the first 58 bytes of the Device Certificate record stored on the device.

|  |
| --- |
| Provisioning Record Response |
|  |
| Status : 00 |
| Record ID : 0001 |
| Fragment Offset : 0000 |
| Total Length : 02b8 |
| Data : |
| 308202b43082025aa00302010202021000300a06082a8648ce3d0403023081a7310b3009060355040613024649311 |
| 0300e06035504080c075575 |
| Message : |
| 0b0001000002b8308202b43082025aa00302010202021000300a06082a8648ce3d0403023081a7310b30090603550 |
| 406130246493110300e06035504080c075575 |

|  |
| --- |
| LinkID : 001289ef |
| Transaction : 81 |

|  |
| --- |
| Segment0 : 0b000001000002b8308202b43082025aa0030201 |
| Segment1 : 0202021000300a06082a8648ce3d0403023081a7310b30 |
| Segment2 : 090603550406130246493110300e06035504080c075575 |

|  |
| --- |
| SegN : 02 |
| PDU Length : 0042 |
| FCS : ce |
| Message0 : 001289ef81080042ce0b000001000002b8308202b43082025aa0030201 |
| Message1 : 001289ef81060202021000300a06082a8648ce3d0403023081a7310b30 |
| Message2 : 001289ef810a090603550406130246493110300e06035504080c075575 |

#### 8.13.8. PB-ADV Transaction Ack

The Provisioner acknowledges the transaction for the first fragment of the Device Certificate record.

After this, the Provisioner will issue more requests for Device Certificate record fragments at increasing offsets until the whole record has been retrieved.

After retrieving the Device Certificate record, the Provisioner will retrieve the Intermediate Certificate 1 record in the same manner if it needs the record.

|  |
| --- |
| PBADV Transaction Acknowledge |
|  |
| LinkID : 001289ef |
| Transaction : 81 |
| Message : 001289ef8101 |

### 8.14. Models Metadata sample data

This sample represents an example of Models Metadata Page 0 (see [Section 4.2.50.1](index-en.html#UUID-7834fe80-da97-e9e3-7a53-1a03d73efaad "4.2.50.1. Models Metadata Page 0")).

|  |
| --- |
| 02010000010700010000112233445566010001040002000011223336010100010600030000112233445500013601020001050004000011223344 |

To help with parsing of this sequence of octets, the octets have been formatted with the appropriate spacing characters.

|  |
| --- |
| 02 01 0000 01 0700 0100 00112233445566 0100 01 0400 0200 00112233 3601 0100 01 0600 0300 001122334455 00 01 3601 0200 01 0500 0400 0011223344 |

The above Models Metadata Page 0 can be described as follows:

Element 1:

* Items_Number_SIG_Models field is 0x02
* Items_Number_Vendor_Models field is 0x01
* Metadata Item for SIG Model 1:

  * SIG Model ID is 0x0000
  * Metadata Entries Number is 0x01

    * Metadata Length is 0x0007
    * Metadata ID is 0x0001
    * Metadata is 0x00112233445566

* Metadata Item for SIG Model 2:

  * SIG Model ID is 0x0001
  * Metadata Entries Number is 0x01

    * Metadata Length is 0x0004
    * Metadata ID is 0x0002
    * Metadata is 0x00112233

* Metadata Item for Vendor Model 1:

  * Company ID is 0x0136
  * Vendor Model ID is 0x0001
  * Metadata Entries Number is 0x01

    * Metadata Length is 0x0006
    * Metadata ID is 0x0003
    * Metadata is 0x001122334455

Element 2:

* Items_Number_SIG_Models field is 0x00
* Items_Number_Vendor_Models field is 0x01
* Metadata Item for SIG Model 1:

  * Company ID is 0x0136
  * Vendor Model ID is 0x0002
  * Metadata Entries Number is 0x01

    * Metadata Length is 0x0005
    * Metadata ID is 0x0004
    * Metadata is 0x 0011223344

### 8.15. Proxy solicitation sample data

A Solicitation PDU is an undirected advertising PDU with a Service UUID AD Type that includes the «Mesh Proxy Solicitation Service» and a Service Data AD Type that carries network layer information for the Mesh Proxy Solicitation Service.

The sample data for Solicitation PDU:

|  |  |  |
| --- | --- | --- |
| CTL | : | 01 |
| SEG | : | 00 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NetKey | : | 18eed9c2a56add85049ffc3c59ad0e12 | | | | | | |
| NID | : | 74 | | | | | | |
| EncryptionKey | : | 5a3e94de21e0427d0ac97df472fb566c | | | | | | |
| PrivacyKey | : | ae3df330624a3458b893c16f2ef0a17c | | | | | | |
| IV Index | : | 00000000 | | | | | | |
| Proxy solicitation nonce | : | 04000000010031000000000000 | | | | | | |
| NID | : | 74 | | | | | | |
| TTL | : |  | 00 | | | | | |
| SEQ | : |  |  | 000001 | | | | |
| SRC | : |  |  |  | 0031 | | | |
| DST | : |  |  |  |  | 0000 | | |
| EncDST | : |  |  |  |  | 3525 | | |
| NetMIC | : |  |  |  |  |  | 63afe281ff9497ef | |

|  |  |  |
| --- | --- | --- |
| Obfuscation | | |
|  | | |
| PrivacyRandom | : | 000000000000000000352563afe281ff |
| PECB | : | babfe810ce18a0929d4a43afa2da2e3a |
| preObfuscation | : | 800000010031 |

|  |  |  |
| --- | --- | --- |
| Solicitation PDU | : | 743abfe811ce29352563afe281ff9497ef |
| Identification Type | : | 00 |
| Identification Par. | : | 743abfe811ce29352563afe281ff9497ef |
| Service Data | : | 00743abfe811ce29352563afe281ff9497ef |

### 8.16. Directed forwarding sample data

This section provides examples of sample data that can be used to verify implementations.

#### 8.16.1. PATH_REQUEST without dependent node addresses and address range lengths

A Directed Forwarding node sends a PATH_REQUEST message as a Path Origin to discover a path. Dependent node addresses and address range lengths are not present. Path metric type, path lifetime, and path discovery interval are set to their respective default values.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0b (PATH_REQUEST) |
| On_Behalf_Of_Dependent_Origin | : | 00 |
| Path_Origin_Path_Metric_Type | : | 00 |
| Path_Origin_Path_Lifetime | : | 02 |
| Path_Discovery_Interval | : | 01 |
| Path_Origin_Forwarding_Number | : | 0c |
| Path_Origin_Path_Metric | : | 00 |
| Destination | : | 0607 |
| Path_Origin_Unicast_Addr_Range | : | (primary:0405, range_length:01) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0000 |
| SRC | : | 0405 |
| DST | : | fffb |
| UpperTransportPDU | : | 0a0c0006070405 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0000 | |
| SRC | : | 0405 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 0b | |
| Header | : | 0b | |
| UpperTransportPDU | : | 0a0c0006070405 | |
| LowerTransportPDU | : | 0b0a0c0006070405 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 01 | | | | | |
| TTL | : | 00 | | | | | |
| SEQ | : | df0000 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | fffb | | | | | |
| LowerTransportPDU | : | 0b0a0c0006070405 | | | | | |
| Security Material | : | directed security material | | | | | |
| NID | : | 0d | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | |
| Network nonce | : | 0080df00000405000012345678 | | | | | |
| IVI NID | : | 0d |  |  |  |  |  |
| CTL TTL | : |  | 80 |  |  |  |  |
| SEQ | : |  |  | df0000 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | fffb | |
| TransportPDU | : |  |  |  |  |  | 0b0a0c0006070405 |
| NetMIC Size | : | 64 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 705434e686764132357a | |
| NetMIC | : |  |  |  |  |  | |
| 135e042c1e6773df | | | | | | | |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678705434e6867641 |
| PECB | : | 40ed7de1151860165aac234e7c56440c |
| CTL||TTL||SEQ||SRC | : | 80df00000405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : |  |
| 0dc0327de1111d705434e686764132357a135e042c1e6773df | | |

#### 8.16.2. PATH_REQUEST with dependent node addresses and address range lengths

A Directed Forwarding node sends a PATH_REQUEST message as a Path Origin to discover a path on behalf of a dependent node. Address range lengths are set. Path metric type, path lifetime, and path discovery interval are set to their respective default values.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0b (PATH_REQUEST) |
| On_Behalf_Of_Dependent_Origin | : | 01 |
| Path_Origin_Path_Metric_Type | : | 00 |
| Path_Origin_Path_Lifetime | : | 02 |
| Path_Discovery_Interval | : | 01 |
| Path_Origin_Forwarding_Number | : | 0c |
| Path_Origin_Path_Metric | : | 00 |
| Destination | : | 0607 |
| Path_Origin_Unicast_Addr_Range | : | (primary:0405, range_length:06) |
| Dependent_Origin_Unicast_Addr_Range | : | (primary:0777, range_length:03) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0010 |
| SRC | : | 0405 |
| DST | : | fffb |
| UpperTransportPDU | : | 8a0c000607840506877703 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0010 | |
| SRC | : | 0405 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 0b | |
| Header | : | 0b | |
| UpperTransportPDU | : |  | 8a0c000607840506877703 |
| LowerTransportPDU | : | 0b8a0c000607840506877703 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 01 | | | | | |
| TTL | : | 00 | | | | | |
| SEQ | : | df0010 | | | | | |
| SRC | : | 0405 | | | | | |
| DST | : | fffb | | | | | |
| LowerTransportPDU | : | 0b8a0c000607840506877703 | | | | | |
| Security Material | : | directed security material | | | | | |
| NID | : | 0d | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | |
| Network nonce | : | 0080df00100405000012345678 | | | | | |
| IVI NID | : | 0d |  |  |  |  |  |
| CTL TTL | : |  | 80 |  |  |  |  |
| SEQ | : |  |  | df0010 | | | |
| SRC | : |  |  |  | 0405 | | |
| DST | : |  |  |  |  | fffb | |
| TransportPDU | : |  |  |  |  |  | 0b8a0c000607840506877703 |
| NetMIC Size | : | 64 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 4d4461df33cc61383559915f940d | |
| NetMIC | : |  |  |  |  |  | |
| 200b340c24003226 | | | | | | | |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456784d4461df33cc61 |
| PECB | : | 49eedbe51773e294bb3d7496178c8e32 |
| CTL||TTL||SEQ||SRC | : | 80df00100405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : |  |
| 0dc931dbf513764d4461df33cc61383559915f940d200b340c24003226 | | |

#### 8.16.3. PATH_REPLY without dependent node addresses and address range lengths

A Directed Forwarding node sends a PATH_REPLY message as a Path Target in response to a PATH_REQUEST message. Dependent node addresses and address range lengths are not present.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0c (PATH_REPLY) |
| Unicast_Destination | : | 01 |
| On_Behalf_Of_Dependent_Target | : | 00 |
| Confirmation_Request | : | 00 |
| Path_Origin | : | 0405 |
| Path_Origin_Forwarding_Number | : | 0c |
| Path_Target_Unicast_Addr_Range | : | (primary:0607, range_length:01) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0020 |
| SRC | : | 0607 |
| DST | : | 1234 |
| UpperTransportPDU | : | 8004050c0607 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0020 | |
| SRC | : | 0607 | |
| DST | : | 1234 | |
| SEG | : | 00 | |
| Opcode | : | 0c | |
| Header | : | 0c | |
| UpperTransportPDU | : | 8004050c0607 | |
| LowerTransportPDU | : | 0c8004050c0607 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 01 | | | | | |
| TTL | : | 00 | | | | | |
| SEQ | : | df0020 | | | | | |
| SRC | : | 0607 | | | | | |
| DST | : | 1234 | | | | | |
| LowerTransportPDU | : | 0c8004050c0607 | | | | | |
| Security Material | : | directed security material | | | | | |
| NID | : | 0d | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | |
| Network nonce | : | 0080df00200607000012345678 | | | | | |
| IVI NID | : | 0d |  |  |  |  |  |
| CTL TTL | : |  | 80 |  |  |  |  |
| SEQ | : |  |  | df0020 | | | |
| SRC | : |  |  |  | 0607 | | |
| DST | : |  |  |  |  | 1234 | |
| TransportPDU | : |  |  |  |  |  | 0c8004050c0607 |
| NetMIC Size | : | 64 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 53e0647c7259d25c68 | |
| NetMIC | : |  |  |  |  |  | |
| a6c2a12fd8015eee | | | | | | | |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567853e0647c7259d2 |
| PECB | : | c283b35b728a10bd991b947cce1ec265 |
| CTL||TTL||SEQ||SRC | : | 80df00200607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : |  |
| 0d425cb37b748d53e0647c7259d25c68a6c2a12fd8015eee | | |

|  |
| --- |
| 0d425cb37b748d53e0647c7259d25c68a6c2a12fd8015eee |

#### 8.16.4. PATH_REPLY with dependent node addresses and address range lengths

A Directed Forwarding node sends a PATH_REPLY message as a Path Target in response to a PATH_REQUEST message on behalf of a dependent node. Address range lengths are set. The reception of the PATH_REPLY message is to be confirmed by the Path Origin.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0c (PATH_REPLY) |
| Unicast_Destination | : | 01 |
| On_Behalf_Of_Dependent_Target | : | 01 |
| Confirmation_Request | : | 01 |
| Path_Origin | : | 0405 |
| Path_Origin_Forwarding_Number | : | 0c |
| Path_Target_Unicast_Addr_Range | : | (primary:0666, range_length:05) |
| Dependent_Target_Unicast_Addr_Range | : | (primary:0607, range_length:04) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0030 |
| SRC | : | 0666 |
| DST | : | 1234 |
| UpperTransportPDU | : | e004050c866605860704 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0030 | |
| SRC | : | 0666 | |
| DST | : | 1234 | |
| SEG | : | 00 | |
| Opcode | : | 0c | |
| Header | : | 0c | |
| UpperTransportPDU | : | e004050c866605860704 | |
| LowerTransportPDU | : | 0ce004050c866605860704 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | |
| CTL | : | 01 | | | | | |
| TTL | : | 00 | | | | | |
| SEQ | : | df0030 | | | | | |
| SRC | : | 0666 | | | | | |
| DST | : | 1234 | | | | | |
| LowerTransportPDU | : | 0ce004050c866605860704 | | | | | |
| Security Material | : | directed security material | | | | | |
| NID | : | 0d | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | |
| Network nonce | : | 0080df00300666000012345678 | | | | | |
| IVI NID | : | 0d |  |  |  |  |  |
| CTL TTL | : |  | 80 |  |  |  |  |
| SEQ | : |  |  | df0030 | | | |
| SRC | : |  |  |  | 0666 | | |
| DST | : |  |  |  |  | 1234 | |
| TransportPDU | : |  |  |  |  |  | 0ce004050c866605860704 |
| NetMIC Size | : | 64 bits | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5a3d39ab72cbed9251d7f974b9 | |
| NetMIC | : |  |  |  |  |  | |
| 86b61f404decbbc9 | | | | | | | |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785a3d39ab72cbed |
| PECB | : | 127316975db08b331c93bd0124cfbfd5 |
| CTL||TTL||SEQ||SRC | : | 80df00300666 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : |  |
| 0d92ac16a75bd65a3d39ab72cbed9251d7f974b986b61f404decbbc9 | | |

#### 8.16.5. PATH_CONFIRMATION

A Directed Forwarding node sends a PATH_CONFIRMATION message as a Path Origin to confirm that a two-way path is established.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0d (PATH_CONFIRMATION) |
| Path_Origin | : | 0405 |
| Path_Target | : | 0607 |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0040 |
| SRC | : | 0405 |
| DST | : | fffb |
| UpperTransportPDU | : | 04050607 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0040 | |
| SRC | : | 0405 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 0d | |
| Header | : | 0d | |
| UpperTransportPDU | : | 04050607 | |
| LowerTransportPDU | : | 0d04050607 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | df0040 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | fffb | | | | | | |
| LowerTransportPDU | : | 0d04050607 | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 0080df00400405000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df0040 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | fffb | | |
| TransportPDU | : |  |  |  |  |  | 0d04050607 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | fc6a9039ed3e7b | | |
| NetMIC | : |  |  |  |  |  |  | b98fd9525c749c11 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678fc6a9039ed3e7b |
| PECB | : | fbb6a25dd0108745a67c0d6bf7d5635a |
| CTL||TTL||SEQ||SRC | : | 80df00400405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 0d7b69a21dd415fc6a9039ed3e7bb98fd9525c749c11 |

#### 8.16.6. PATH_ECHO_REQUEST

A Path Origin sends a PATH_ECHO_REQUEST message to a Path Target to validate a path.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0e (PATH_ECHO_REQUEST) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 7f |
| SEQ | : | df0050 |
| SRC | : | 0405 |
| DST | : | 0607 |
| UpperTransportPDU | : |  |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 7f | |
| SEQ | : | df0050 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| Opcode | : | 0e | |
| Header | : | 0e | |
| UpperTransportPDU | : |  |  |
| LowerTransportPDU | : | 0e | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 7f | | | | | | |
| SEQ | : | df0050 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0e | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 00ffdf00500405000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | ff | | | | | |
| SEQ | : |  |  | df0050 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0e | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 217537 | | |
| NetMIC | : |  |  |  |  |  |  | f1d03a8c14e2ef98 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678217537f1d03a8c |
| PECB | : | b0949fe874325c54a3700df317d7c627 |
| CTL||TTL||SEQ||SRC | : | ffdf00500405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 0d4f4b9fb87037217537f1d03a8c14e2ef98 |

#### 8.16.7. PATH_ECHO_REPLY

A Path Target sends a PATH_ECHO_REPLY message to a Path Origin in response to a PATH_ECHO_REQUEST message.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 0f (PATH_ECHO_REPLY) |
| Destination | : | 0405 |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 7f |
| SEQ | : | df0060 |
| SRC | : | 0607 |
| DST | : | 0405 |
| UpperTransportPDU | : | 0405 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 7f | |
| SEQ | : | df0060 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| Opcode | : | 0f | |
| Header | : | 0f | |
| UpperTransportPDU | : | 0405 | |
| LowerTransportPDU | : | 0f0405 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 7f | | | | | | |
| SEQ | : | df0060 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0f0405 | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 00ffdf00600607000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | ff | | | | | |
| SEQ | : |  |  | df0060 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0f0405 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | ca969a1d03 | | |
| NetMIC | : |  |  |  |  |  |  | f52e0ca18ba056d3 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678ca969a1d03f52e |
| PECB | : | 3fe1e3abe41e377edace1791def6e038 |
| CTL||TTL||SEQ||SRC | : | ffdf00600607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 0dc03ee3cbe219ca969a1d03f52e0ca18ba056d3 |

#### 8.16.8. DEPENDENT_NODE_UPDATE with dependent node address to remove

A Path Origin sends a DEPENDENT_NODE_UPDATE message to notify that a dependent node address is removed.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 10 (DEPENDENT_NODE_UPDATE) |
| Type | : | 00 (remove) |
| Path_Endpoint | : | 0405 |
| Dependent_Node_Unicast_Addr_Range | : | (primary:0abc, range_length:01) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0070 |
| SRC | : | 0405 |
| DST | : | fffb |
| UpperTransportPDU | : | 0004050abc |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0070 | |
| SRC | : | 0405 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 10 | |
| Header | : | 10 | |
| UpperTransportPDU | : | 0004050abc | |
| LowerTransportPDU | : | 100004050abc | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | df0070 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | fffb | | | | | | |
| LowerTransportPDU | : | 100004050abc | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 0080df00700405000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df0070 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | fffb | | |
| TransportPDU | : |  |  |  |  |  | 100004050abc | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 20643759c86d1d22 | | |
| NetMIC | : |  |  |  |  |  |  | 9817761fb8353ef3 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567820643759c86d1d |
| PECB | : | ed2f8d7a78135e236ac3cf336a41a70f |
| CTL||TTL||SEQ||SRC | : | 80df00700405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 0d6df08d0a7c1620643759c86d1d229817761fb8353ef3 |

#### 8.16.9. DEPENDENT_NODE_UPDATE with dependent node address to add

A Path Origin sends a DEPENDENT_NODE_UPDATE message to notify that a dependent node address is added. The dependent node supports secondary elements.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 10 (DEPENDENT_NODE_UPDATE) |
| Type | : | 01 (add) |
| Path_Endpoint | : | 0405 |
| Dependent_Node_Unicast_Addr_Range | : | (primary:0def, range_length:03) |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0080 |
| SRC | : | 0405 |
| DST | : | fffb |
| UpperTransportPDU | : | 8004058def03 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0080 | |
| SRC | : | 0405 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 10 | |
| Header | : | 10 | |
| UpperTransportPDU | : | 8004058def03 | |
| LowerTransportPDU | : | 108004058def03 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | df0080 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | fffb | | | | | | |
| LowerTransportPDU | : | 108004058def03 | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 0080df00800405000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df0080 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | fffb | | |
| TransportPDU | : |  |  |  |  |  | 108004058def03 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 144bc9dd860a6ab250 | | |
| NetMIC | : |  |  |  |  |  |  |  |
| dc817b6ac2db0bf1 | | | | | | | | |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678144bc9dd860a6a |
| PECB | : | e3bab400f30026ea0d76983586b6c4ff |
| CTL||TTL||SEQ||SRC | : | 80df00800405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : |  |
| 0d6365b480f705144bc9dd860a6ab250dc817b6ac2db0bf1 | | |

#### 8.16.10. PATH_REQUEST_SOLICITATION

A Path Target sends a PATH_REQUEST_SOLICITATION message to solicit the creation of a Directed Originating Path State Machine for a group address the Path Target has subscribed to. The message reports an address list containing a single group address.

|  |
| --- |
| Transport Control message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 11 (PATH_REQUEST_SOLICITATION) |
| Addr_List | : | c000 |

|  |
| --- |
| UpperTransportControlPDU |

|  |  |  |
| --- | --- | --- |
| TTL | : | 00 |
| SEQ | : | df0090 |
| SRC | : | 0607 |
| DST | : | fffb |
| UpperTransportPDU | : | c000 |

|  |
| --- |
| LowerTransportUnsegmentedControlPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 01 | |
| TTL | : | 00 | |
| SEQ | : | df0090 | |
| SRC | : | 0607 | |
| DST | : | fffb | |
| SEG | : | 00 | |
| Opcode | : | 11 | |
| Header | : | 11 | |
| UpperTransportPDU | : | c000 | |
| LowerTransportPDU | : | 11c000 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 01 | | | | | | |
| TTL | : | 00 | | | | | | |
| SEQ | : | df0090 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | fffb | | | | | | |
| LowerTransportPDU | : | 11c000 | | | | | | |
| Security Material | : | directed security material | | | | | | |
| NID | : | 0d | | | | | | |
| EncryptionKey | : | b47a02c6cc9b4ac4cb9b88e765c9ade4 | | | | | | |
| PrivacyKey | : | 9bf7ab5a5ad415fbd77e07bb808f4865 | | | | | | |
| Network nonce | : | 0080df00700405000012345678 | | | | | | |
| IVI NID | : | 0d | | | | | | |
| CTL TTL | : |  | 80 | | | | | |
| SEQ | : |  |  | df0090 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | fffb | | |
| TransportPDU | : |  |  |  |  |  | 11c000 | |
| NetMIC Size | : | 64 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 240b7087b8 | | |
| NetMIC | : |  |  |  |  |  |  | 2d3e1b96e0fa6e56 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678240b7087b82d3e |
| PECB | : | aa384de8ec64d47e36129ac3f662655c |
| CTL||TTL||SEQ||SRC | : | 80df00900607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 0d2ae74d78ea63240b7087b82d3e1b96e0fa6e56 |

#### 8.16.11. DIRECTED_CONTROL_GET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_GET message to a Directed Forwarding Configuration Server to read its Directed Control state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 807b (DIRECTED_CONTROL_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 807b2301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00a0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df00a00405060712345678 |
| EncAccessMessage | : | 2b8c08d2 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | a19d092f |
| UpperTransportPDU | : | 2b8c08d2a19d092f |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00a0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 2b8c08d2a19d092f | |
| LowerTransportPDU | : | 002b8c08d2a19d092f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00a0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 002b8c08d2a19d092f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00a00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00a0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 002b8c08d2a19d092f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 59d97fe6f6705ef5228715 | | |
| NetMIC | : |  |  |  |  |  |  | 5f1823c3 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567859d97fe6f6705e |
| PECB | : | 1793c29f8b8293106b8cb60e31fc2860 |
| CTL||TTL||SEQ||SRC | : | 07df00a00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68104cc23f8f8759d97fe6f6705ef52287155f1823c3 |

#### 8.16.12. DIRECTED_CONTROL_SET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_SET message to a Directed Forwarding Configuration Server to enable both the directed forwarding and directed friend functionalities and to disable directed relay functionality.

|  |
| --- |
| Access message |

|  |  |  |  |
| --- | --- | --- | --- |
| Opcode | : | 807c (DIRECTED_CONTROL_SET) | |
| NetKeyIndex |  | : | 0123 |
| Directed_Forwarding |  | : | 01 (enabled) |
| Directed_Relay |  | : | 00 (disabled) |
| Directed_Proxy |  | : | ff (ignored) |
| Directed_Proxy_Use_Directed_Default |  | : | ff (ignored) |
| Directed_Friend |  | : | 01 (enabled) |
| Access message | : | 807c23010100ffff01 | |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00b0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df00b00405060712345678 |
| EncAccessMessage | : | eb00f9c3a40ec128d8 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 961ef64f |
| UpperTransportPDU | : | eb00f9c3a40ec128d8961ef64f |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00b0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | eb00f9c3a40ec128d8961ef64f | |
| LowerTransportPDU | : | 00eb00f9c3a40ec128d8961ef64f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00b0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00eb00f9c3a40ec128d8961ef64f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00b00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00b0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00eb00f9c3a40ec128d8961ef64f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d082104b2275a91a1086295df2740272 | | |
| NetMIC | : |  |  |  |  |  |  | 633327e7 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678d082104b2275a9 |
| PECB | : | 7d52b2e1d9bb5b4f6514f175e308984d |
| CTL||TTL||SEQ||SRC | : | 07df00b00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 687a8db251ddbed082104b2275a91a1086295df2740272633327e7 |

#### 8.16.13. DIRECTED_CONTROL_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_CONTROL_GET message or a DIRECTED_CONTROL_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_CONTROL_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |  |
| --- | --- | --- | --- |
| Opcode | : | 807d (DIRECTED_CONTROL_STATUS) | |
| Status |  | : | 00 (Success) |
| NetKeyIndex |  | : | 0123 |
| Directed_Forwarding |  | : | 01 (enabled) |
| Directed_Relay |  | : | 00 (disabled) |
| Directed_Proxy |  | : | 02 (not supported) |
| Directed_Proxy_Use_Directed_Default |  | : | 02 (not supported) |
| Directed_Friend |  | : | 01 (supported and enabled) |
| Access message | : | 807d0023010100020201 | |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00c0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df00c00607040512345678 |
| EncAccessMessage | : | d62fbb61810b123b483d |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 3acb3447 |
| UpperTransportPDU | : | d62fbb61810b123b483d3acb3447 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00c0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | d62fbb61810b123b483d3acb3447 | |
| LowerTransportPDU | : | 00d62fbb61810b123b483d3acb3447 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00c0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 00d62fbb61810b123b483d3acb3447 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00c00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00c0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 00d62fbb61810b123b483d3acb3447 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 13215846ad49a7c046bd42ad5d98da5925 | | |
| NetMIC | : |  |  |  |  |  |  | 852a0635 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567813215846ad49a7 |
| PECB | : | 392fb8ac8c84e73223a6dcf2444f4d0e |
| CTL||TTL||SEQ||SRC | : | 07df00c00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 683ef0b86c8a8313215846ad49a7c046bd42ad5d98da5925852a0635 |

#### 8.16.14. PATH_METRIC_GET

A Directed Forwarding Configuration Client sends a PATH_METRIC_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 807e (PATH_METRIC_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 807e2301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00d0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df00d00405060712345678 |
| EncAccessMessage | : | 2ba8e020 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 20c7ae6b |
| UpperTransportPDU | : | 2ba8e02020c7ae6b |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00d0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 2ba8e02020c7ae6b | |
| LowerTransportPDU | : | 002ba8e02020c7ae6b | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00d0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 002ba8e02020c7ae6b | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00d00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00d0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 002ba8e02020c7ae6b | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | eef52902b1855fc035dd98 | | |
| NetMIC | : |  |  |  |  |  |  | 71d43409 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678eef52902b1855f |
| PECB | : | 8b824af58a55ddfb7b48099b05bb5d10 |
| CTL||TTL||SEQ||SRC | : | 07df00d00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 688c5d4a258e50eef52902b1855fc035dd9871d43409 |

#### 8.16.15. PATH_METRIC_SET

A Directed Forwarding Configuration Client sends a PATH_METRIC_SET message to a Directed Forwarding Configuration Server to set the path metric type to Node Count and set the path lifetime to 12 minutes.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 807f (PATH_METRIC_SET) |
| NetKeyIndex | : | 0123 |
| Path_Metric_Type | : | 00 (Node Count) |
| Path_Lifetime | : | 00 (12 minutes) |
| Access message | : | 807f230100 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00e0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df00e00405060712345678 |
| EncAccessMessage | : | 37e9906fbb |
| TransMIC Size | : | 32 bits |
| TransMIC | : | d2a82c24 |
| UpperTransportPDU | : | 37e9906fbbd2a82c24 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00e0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 37e9906fbbd2a82c24 | |
| LowerTransportPDU | : | 0037e9906fbbd2a82c24 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00e0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0037e9906fbbd2a82c24 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00e00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00e0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0037e9906fbbd2a82c24 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2f4a367c39f5d6453ee78c96 | | |
| NetMIC | : |  |  |  |  |  |  | d905f2fe |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456782f4a367c39f5d6 |
| PECB | : | 75ab432276c5e8cbf88c2221d1f745b9 |
| CTL||TTL||SEQ||SRC | : | 07df00e00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68727443c272c02f4a367c39f5d6453ee78c96d905f2fe |

#### 8.16.16. PATH_METRIC_STATUS

A Directed Forwarding Configuration Server receives a PATH_METRIC_GET message or a PATH_METRIC_SET message from a Directed Forwarding Configuration Client and responds with a PATH_METRIC_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8080 (PATH_METRIC_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Path_Metric_Type | : | 00 (Node Count) |
| Path_Lifetime | : | 00 (1 hour) |
| Access message | : | 808000230100 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df00f0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df00f00607040512345678 |
| EncAccessMessage | : | 84e86cec5e86 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | a0888cbc |
| UpperTransportPDU | : | 84e86cec5e86a0888cbc |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df00f0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 84e86cec5e86a0888cbc | |
| LowerTransportPDU | : | 0084e86cec5e86a0888cbc | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df00f0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0084e86cec5e86a0888cbc | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df00f00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df00f0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0084e86cec5e86a0888cbc | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b0c611929dc36301d77588e735 | | |
| NetMIC | : |  |  |  |  |  |  | b917eb3a |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678b0c611929dc363 |
| PECB | : | bb207c84454e6fa890d3a5a58ab210ee |
| CTL||TTL||SEQ||SRC | : | 07df00f00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68bcff7c744349b0c611929dc36301d77588e735b917eb3a |

#### 8.16.17. DISCOVERY_TABLE_CAPABILITIES_GET

A Directed Forwarding Configuration Client sends a DISCOVERY_TABLE_CAPABILITIES_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8081 (DISCOVERY_TABLE_CAPABILITIES_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 80812301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0100 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01000405060712345678 |
| EncAccessMessage | : | 1a32f8be |
| TransMIC Size | : | 32 bits |
| TransMIC | : | a6d7ca11 |
| UpperTransportPDU | : | 1a32f8bea6d7ca11 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0100 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 1a32f8bea6d7ca11 | |
| LowerTransportPDU | : | 001a32f8bea6d7ca11 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0100 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 001a32f8bea6d7ca11 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01000405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0100 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 001a32f8bea6d7ca11 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | f6cf82d66e956954c1b7c0 | | |
| NetMIC | : |  |  |  |  |  |  | 30d441de |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678f6cf82d66e9569 |
| PECB | : | 1485fa3e85308b14391250459dfe324a |
| CTL||TTL||SEQ||SRC | : | 07df01000405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68135afb3e8135f6cf82d66e956954c1b7c030d441de |

#### 8.16.18. DISCOVERY_TABLE_CAPABILITIES_SET

A Directed Forwarding Configuration Client sends a DISCOVERY_TABLE_CAPABILITIES_SET message to a Directed Forwarding Configuration Server to set the maximum number of concurrent Directed Forwarding Initialization operations to 8.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8082 (DISCOVERY_TABLE_CAPABILITIES_SET) |
| NetKeyIndex | : | 0123 |
| Max_Concurrent_Init | : | 08 |
| Access message | : | 8082230108 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0110 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01100405060712345678 |
| EncAccessMessage | : | 478d52d5b9 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | aa09010d |
| UpperTransportPDU | : | 478d52d5b9aa09010d |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0110 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 478d52d5b9aa09010d | |
| LowerTransportPDU | : | 00478d52d5b9aa09010d | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0110 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00478d52d5b9aa09010d | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01100405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0110 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00478d52d5b9aa09010d | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 001f682125bfeb4877949a55 | | |
| NetMIC | : |  |  |  |  |  |  | 6bbaa49c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678001f682125bfeb |
| PECB | : | 47684d309bc9ff0f20205cc0dc8d24fc |
| CTL||TTL||SEQ||SRC | : | 07df01100405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6840b74c209fcc001f682125bfeb4877949a556bbaa49c |

#### 8.16.19. DISCOVERY_TABLE_CAPABILITIES_STATUS

A Directed Forwarding Configuration Server receives a DISCOVERY_TABLE_CAPABILITIES_GET message or a DISCOVERY_TABLE_CAPABILITIES_SET message from a Directed Forwarding Configuration Client and responds with a DISCOVERY_TABLE_CAPABILITIES_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8083 (DISCOVERY_TABLE_CAPABILITIES_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Max_Concurrent_Init | : | 08 |
| Max_Discovery_Table_Entries_Count | : | 20 |
| Access message | : | 80830023010820 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0120 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df01200607040512345678 |
| EncAccessMessage | : | 5c43fd0f362cac |
| TransMIC Size | : | 32 bits |
| TransMIC | : | bb3ef827 |
| UpperTransportPDU | : | 5c43fd0f362cacbb3ef827 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0120 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | 5c43fd0f362cacbb3ef827 | |
| LowerTransportPDU | : | 005c43fd0f362cacbb3ef827 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0120 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 005c43fd0f362cacbb3ef827 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01200607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0120 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 005c43fd0f362cacbb3ef827 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | a875f3250924e0d4524ff57158ed | | |
| NetMIC | : |  |  |  |  |  |  | 5f29b033 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678a875f3250924e0 |
| PECB | : | 5a12ff0eba0c7aee7541d7c71ca0dfb6 |
| CTL||TTL||SEQ||SRC | : | 07df01200607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 685dcdfe2ebc0ba875f3250924e0d4524ff57158ed5f29b033 |

#### 8.16.20. FORWARDING_TABLE_ADD

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_ADD message to a Directed Forwarding Configuration Server to add a fixed path entry for a destination identified by a unicast address. The path is a two-way path. Both the Path Origin and the Path Target have secondary elements and dependent nodes. The message
is sent in two segments.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8084 (FORWARDING_TABLE_ADD) |
| NetKeyIndex | : | 123 |
| Unicast_Destination | : | 01 |
| Backward_Path_Validated_Flag | : | 01 |
| Path_Origin_Unicast_Addr_Range | : | (primary:1234, range_length:03) |
| Path_Target_Unicast_Addr_Range | : | (primary:5678, range_length:05) |
| Bearer_Toward_Path_Origin | : | 0001 |
| Bearer_Toward_Path_Target | : | 0001 |
| Access message | : | 808423c1692403f1ac0501000100 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0130 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01300405060712345678 |
| EncAccessMessage | : | e87bd369eba1e23878afea57b48c |
| TransMIC Size | : | 32 bits |
| TransMIC | : | fa576d52 |
| UpperTransportPDU | : | e87bd369eba1e23878afea57b48cfa576d52 |
| Segment#00 | : | e87bd369eba1e23878afea57 |
| Segment#01 | : | b48cfa576d52 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0130 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0130 | |
| SegO | : | 00 | |
| SegN | : | 01 | |
| Header | : | 8004c001 | |
| Segment#00 | : | e87bd369eba1e23878afea57 | |
| LowerTransportPDU | : | 8004c001e87bd369eba1e23878afea57 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0130 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8004c001e87bd369eba1e23878afea57 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01300405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0130 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8004c001e87bd369eba1e23878afea57 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 229dd0fc7aded502842a604aecf5771e4ff2 | | |
| NetMIC | : |  |  |  |  |  |  | 6192f90c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678229dd0fc7aded5 |
| PECB | : | 05fae2e0ef3b31edd97cb3ae7072f74d |
| CTL || TTL || SEQ ||SRC | : | 07df01300405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 680225e3d0eb3e229dd0fc7aded502842a604aecf5771e4ff26192f90c |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0131 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0130 | |
| SegO | : | 01 | |
| SegN | : | 01 | |
| Header | : | 8004c021 | |
| Segment#01 | : | b48cfa576d52 | |
| LowerTransportPDU | : | 8004c021b48cfa576d52 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0131 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8004c021b48cfa576d52 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01310405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0131 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8004c021b48cfa576d52 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 8c7b4bc8ca37c8be7677f6d5 | | |
| NetMIC | : |  |  |  |  |  |  | dcdc84db |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456788c7b4bc8ca37c8 |
| PECB | : | 695c73dfc67b6b9f91613b2c76abca85 |
| CTL || TTL || SEQ || SRC | : | 07df01310405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 686e8372eec27e8c7b4bc8ca37c8be7677f6d5dcdc84db |

#### 8.16.21. FORWARDING_TABLE_DELETE

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_DELETE message to a Directed Forwarding Configuration Server to remove a path entry for a destination identified by a unicast address.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8085 (FORWARDING_TABLE_DELETE) |
| NetKeyIndex | : | 0123 |
| Path_Origin | : | 1234 |
| Destination | : | 5678 |
| Access message | : | 8085230134127856 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0140 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01400405060712345678 |
| EncAccessMessage | : | d3f30126ba2094cb |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 3f967cb5 |
| UpperTransportPDU | : | d3f30126ba2094cb3f967cb5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0140 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : | d3f30126ba2094cb3f967cb5 | |
| LowerTransportPDU | : | 00d3f30126ba2094cb3f967cb5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0140 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00d3f30126ba2094cb3f967cb5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01400405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0140 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00d3f30126ba2094cb3f967cb5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 3ba4bd594adcdd2f12deaba95c4a13 | | |
| NetMIC | : |  |  |  |  |  |  | 93df59d7 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456783ba4bd594adcdd |
| PECB | : | 6740f42f6cf64dddbc04de118820b588 |
| CTL||TTL||SEQ||SRC | : | 07df01400405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68609ff56f68f33ba4bd594adcdd2f12deaba95c4a1393df59d7 |

#### 8.16.22. FORWARDING_TABLE_STATUS

A Directed Forwarding Configuration Server receives a FORWARDING_TABLE_ADD message or a FORWARDING_TABLE_DELETE message from a Directed Forwarding Configuration Client and responds with a FORWARDING_TABLE_STATUS message with Status equal to Success.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8086 (FORWARDING_TABLE_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Path_Origin | : | 1234 |
| Destination | : | 5678 |
| Access message | : | 808600230134127856 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0150 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df01500607040512345678 |
| EncAccessMessage | : | 37a4992a82bfd136be |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 2d94927c |
| UpperTransportPDU | : | 37a4992a82bfd136be2d94927c |
| Segment#00 | : | 37a4992a82bfd136be2d9492 |
| Segment#01 | : | 7c |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0150 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0150 | |
| SegO | : | 00 | |
| SegN | : | 01 | |
| Header | : | 80054001 | |
| Segment#00 | : | 37a4992a82bfd136be2d9492 | |
| LowerTransportPDU | : | 8005400137a4992a82bfd136be2d9492 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0150 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 8005400137a4992a82bfd136be2d9492 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01500607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0150 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 8005400137a4992a82bfd136be2d9492 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | d14b93381618952e6de17e7a5bdb7633f1ec | | |
| NetMIC | : |  |  |  |  |  |  | 84629dcb |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678d14b9338161895 |
| PECB | : | 0436d85b3ce599fda15d7a251b4b8e5a |
| CTL || TTL || SEQ || SRC | : | 07df01500607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6803e9d90b3ae2d14b93381618952e6de17e7a5bdb7633f1ec84629dcb |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0151 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0150 | |
| SegO | : | 01 | |
| SegN | : | 01 | |
| Header | : | 80054021 | |
| Segment#01 | : | 7c | |
| LowerTransportPDU | : | 800540217c | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0151 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 800540217c | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01510607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0151 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 800540217c | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 1a5080350ae01b | | |
| NetMIC | : |  |  |  |  |  |  | 2456d17c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456781a5080350ae01b |
| PECB | : | 37436786dabd94d39d77ce1e213bcad6 |
| CTL || TTL || SEQ || SRC | : | 07df01510607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68309c66d7dcba1a5080350ae01b2456d17c |

#### 8.16.23. FORWARDING_TABLE_DEPENDENTS_ADD

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_DEPENDENTS_ADD message to a Directed Forwarding Configuration Server to add dependent node addresses to a fixed path entry. The message is sent in three segments.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 8087 (FORWARDING_TABLE_DEPENDENTS_ADD) |
| NetKeyIndex | | | : | 0123 |
| Path_Origin | | | : | 1234 |
| Destination | | | : | 5678 |
| Dependent_Origin_Unicast_Addr_Range_­List_­Size | | | : | 02 |
| Dependent_Target_Unicast_Addr_Range_List_­Size | | | : | 03 |
| Dependent_Origin_Unicast_Addr_Range_List | | | : |  |
|  | (#00) | Dependent_Origin_Unicast_Addr_Range | : | (primary:12aa, range_length:04) |
|  | (#01) | Dependent_Origin_Unicast_Addr_Range | : | (primary:12bb, range_length:01) |
| Dependent_Target_Unicast_Addr_Range_List | | | : |  |
|  | (#00) | Dependent_Target_Unicast_Addr_Range | : | (primary:56aa, range_length:02) |
|  | (#01) | Dependent_Target_Unicast_Addr_Range | : | (primary:56bb, range_length:06) |
|  | (#02) | Dependent_Target_Unicast_Addr_Range | : | (primary:56cc, range_length:01) |
| Access message | | | : | 80872301341278560203552504762555ad0277ad0698ad |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0160 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01600405060712345678 |
| EncAccessMessage | : | ccebc7db8a4456b3c90aa14470afee3498b853147ceebd |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 461e105f |
| UpperTransportPDU | : | ccebc7db8a4456b3c90aa14470afee3498b853147ceebd461e105f |
| Segment#00 | : | ccebc7db8a4456b3c90aa144 |
| Segment#01 | : | 70afee3498b853147ceebd46 |
| Segment#02 | : | 1e105f |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0160 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0160 | |
| SegO | : | 00 | |
| SegN | : | 02 | |
| Header | : | 80058002 | |
| Segment#00 | : |  | ccebc7db8a4456b3c90aa144 |
| LowerTransportPDU | : | 80058002ccebc7db8a4456b3c90aa144 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0160 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 80058002ccebc7db8a4456b3c90aa144 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01600405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0160 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 80058002ccebc7db8a4456b3c90aa144 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2d76d5a1df8ef32bd14a98b375abfcda815c | | |
| NetMIC | : |  |  |  |  |  |  | a144631c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456782d76d5a1df8ef3 |
| PECB | : | 4cbc87860d1fc67db7540a57763ba0d5 |
| CTL || TTL || SEQ || SRC | : | 07df01600405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 684b6386e6091a2d76d5a1df8ef32bd14a98b375abfcda815ca144631c |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0161 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0160 | |
| SegO | : | 01 | |
| SegN | : | 02 | |
| Header | : | 80058022 | |
| Segment#01 | : |  | 70afee3498b853147ceebd46 |
| LowerTransportPDU | : | 8005802270afee3498b853147ceebd46 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0161 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 80058002ccebc7db8a4456b3c90aa144 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01600405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0160 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 80058002ccebc7db8a4456b3c90aa144 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | edd1d9299d34829ad158fd0d854c8fa987b7 | | |
| NetMIC | : |  |  |  |  |  |  | f911c281 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678edd1d9299d3482 |
| PECB | : | 2684f64b160c9604c94fa4ec37df56fb |
| CTL || TTL || SEQ || SRC | : | 07df01600405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68215bf72a1209edd1d9299d34829ad158fd0d854c8fa987b7f911c281 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0162 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0160 | |
| SegO | : | 02 | |
| SegN | : | 02 | |
| Header | : | 80058042 | |
| Segment#02 | : |  | 1e105f |
| LowerTransportPDU | : | 800580421e105f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0162 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 800580421e105f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01610405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0162 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 800580421e105f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 20fb1e346c14e4978b | | |
| NetMIC | : |  |  |  |  |  |  | 2144ef9f |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567820fb1e346c14e4 |
| PECB | : | a4ef12910e12143f740f33ac9b40a4dc |
| CTL || TTL || SEQ || SRC | : | 07df01610405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68a33013f30a1720fb1e346c14e4978b2144ef9f |

#### 8.16.24. FORWARDING_TABLE_DEPENDENTS_DELETE

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_DEPENDENTS_DELETE message to a Directed Forwarding Configuration Server to remove dependent node addresses from a fixed path entry. The message is sent in two segments.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8088 (FORWARDING_TABLE_DEPENDENTS_DELETE) |
| NetKeyIndex | : | 0123 |
| Path_Origin | : | 1234 |
| Destination | : | 5678 |
| Dependent_Origin_List_Size | : | 01 |
| Dependent_Target_List_Size | : | 01 |
| Dependent_Origin_List | : | 12aa |
| Dependent_Target_List | : | 56cc |
| Access message | : | 80882301341278560101aa12cc56 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0170 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01700405060712345678 |
| EncAccessMessage | : | 78c257101e4fb3897213660da9c4 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 52adce5a |
| UpperTransportPDU | : | 78c257101e4fb3897213660da9c452adce5a |
| Segment#00 | : | 78c257101e4fb3897213660d |
| Segment#01 | : | a9c452adce5a |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0170 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0170 | |
| SegO | : | 00 | |
| SegN | : | 01 | |
| Header | : | 8005c001 | |
| Segment#00 | : |  | 78c257101e4fb3897213660d |
| LowerTransportPDU | : | 8005c00178c257101e4fb3897213660d | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0170 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8005c00178c257101e4fb3897213660d | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01700405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0170 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8005c00178c257101e4fb3897213660d | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | c81c1441d3aad595f9044276045138ac69d7 | | |
| NetMIC | : |  |  |  |  |  |  | beb8ebbd |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678c81c1441d3aad5 |
| PECB | : | f3fae9f0b1bac2c8bef7b2597e5cd444 |
| CTL || TTL || SEQ || SRC | : | 07df01700405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 684b6386e6091a2d76d5a1df8ef32bd14a98b375abfcda815ca144631c |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0161 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0160 | |
| SegO | : | 01 | |
| SegN | : | 02 | |
| Header | : | 80058022 | |
| Segment#01 | : |  | 70afee3498b853147ceebd46 |
| LowerTransportPDU | : | 8005802270afee3498b853147ceebd46 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0161 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8005802270afee3498b853147ceebd46 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01710405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0161 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8005802270afee3498b853147ceebd46 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | edd1d9299d34829ad158fd0d854c8fa987b7 | | |
| NetMIC | : |  |  |  |  |  |  | f911c281 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678edd1d9299d3482 |
| PECB | : | 2684f64b160c9604c94fa4ec37df56fb |
| CTL || TTL || SEQ || SRC | : | 07df01610405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68215bf72a1209edd1d9299d34829ad158fd0d854c8fa987b7f911c281 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0162 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0160 | |
| SegO | : | 02 | |
| SegN | : | 02 | |
| Header | : | 80058042 | |
| Segment#02 | : |  | 1e105f |
| LowerTransportPDU | : | 800580421e105f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0162 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 800580421e105f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01620405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0162 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 800580421e105f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 20fb1e346c14e4978b | | |
| NetMIC | : |  |  |  |  |  |  | 2144ef9f |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567820fb1e346c14e4 |
| PECB | : | a4ef12910e12143f740f33ac9b40a4dc |
| CTL || TTL || SEQ || SRC | : | 07df01620405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68a33013f30a1720fb1e346c14e4978b2144ef9f |

#### 8.16.25. FORWARDING_TABLE_DEPENDENTS_STATUS

A Directed Forwarding Configuration Server receives a FORWARDING_TABLE_DEPENDENTS_DELETE message from a Directed Forwarding Configuration Client and responds with a FORWARDING_TABLE_DEPENDENTS_STATUS message with Status equal to Success.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8089 (FORWARDING_TABLE_DEPENDENTS_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Path_Origin | : | 1234 |
| Destination | : | 5678 |
| Access message | : | 808900230134127856 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0180 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df01800607040512345678 |
| EncAccessMessage | : | fc48b80dd522cf3a68 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | ce790306 |
| UpperTransportPDU | : | fc48b80dd522cf3a68ce790306 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0180 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | fc48b80dd522cf3a68ce790306 |
| LowerTransportPDU | : | 00fc48b80dd522cf3a68ce790306 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0180 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 00fc48b80dd522cf3a68ce790306 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01800607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0180 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 00fc48b80dd522cf3a68ce790306 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | aa1254eeba0c7e92a9da4a7e957f2509 | | |
| NetMIC | : |  |  |  |  |  |  | 3e1f8bab |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678aa1254eeba0c7e |
| PECB | : | f0470e13c29828b74e6b79761ae09640 |
| CTL||TTL||SEQ||SRC | : | 07df01800607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68f7980f93c49faa1254eeba0c7e92a9da4a7e957f25093e1f8bab |

#### 8.16.26. FORWARDING_TABLE_DEPENDENTS_GET

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_DEPENDENTS_GET message to a Directed Forwarding Configuration Server to get the list of dependent node addresses in a path entry.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 808a (FORWARDING_TABLE_DEPENDENTS_GET) |
| NetKeyIndex | : | 0123 |
| Dependents_List_Mask | : | 03 |
| Fixed_Path_Flag | : | 01 |
| Start_Index | : | 0000 |
| Path_Origin | : | 1234 |
| Destination | : | 5678 |
| Forwarding_Table_Update_­Identifier | : | abcd |
| Access message | : | 808a2371000034127856cdab |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0190 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01900405060712345678 |
| EncAccessMessage | : | 8f7188c87cbaf3d8f9932297 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | c6aa8984 |
| UpperTransportPDU | : | 8f7188c87cbaf3d8f9932297c6aa8984 |
| Segment#00 | : | 8f7188c87cbaf3d8f9932297 |
| Segment#01 | : | c6aa8984 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0190 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0190 | |
| SegO | : | 00 | |
| SegN | : | 01 | |
| Header | : | 80064001 | |
| Segment#00 | : |  | 8f7188c87cbaf3d8f9932297 |
| LowerTransportPDU | : | 800640018f7188c87cbaf3d8f9932297 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0190 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 800640018f7188c87cbaf3d8f9932297 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01900405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0190 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 800640018f7188c87cbaf3d8f9932297 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | c466d0c30f01aa9f2bf2986e46ab0db13182 | | |
| NetMIC | : |  |  |  |  |  |  | 7bbb5632 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678c466d0c30f01aa |
| PECB | : | 10c775b0f6fb9d1df8d01ca036e42fa8 |
| CTL || TTL || SEQ || SRC | : | 07df01900405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6817187420f2fec466d0c30f01aa9f2bf2986e46ab0db131827bbb5632 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0191 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 0190 | |
| SegO | : | 01 | |
| SegN | : | 01 | |
| Header | : | 80064021 | |
| Segment#01 | : |  | c6aa8984 |
| LowerTransportPDU | : | 80064021c6aa8984 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0191 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 80064021c6aa8984 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01910405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0191 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 80064021c6aa8984 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 705f4a24fb5c4d99ea1e | | |
| NetMIC | : |  |  |  |  |  |  | 6ad03e61 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678705f4a24fb5c4d |
| PECB | : | 30ffcf20ac383ab6c38682035cbd3d7b |
| CTL || TTL || SEQ || SRC | : | 07df01910405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 683720ceb1a83d705f4a24fb5c4d99ea1e6ad03e61 |

#### 8.16.27. FORWARDING_TABLE_DEPENDENTS_GET_STATUS

A Directed Forwarding Configuration Server receives a FORWARDING_TABLE_DEPENDENTS_GET message from a Directed Forwarding Configuration Client and responds with a FORWARDING_TABLE_DEPENDENTS_GET_STATUS. The message is sent in three segments.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 808b (FORWARDING_TABLE_DEPENDENTS_GET_STATUS) |
| Status | | | : | 00 (Success) |
| NetKeyIndex | | | : | 0123 |
| Dependents_List_Mask | | | : | 03 |
| Fixed_Path_Flag | | | : | 01 |
| Start_Index | | | : | 0000 |
| Path_Origin | | | : | 1234 |
| Destination | | | : | 5678 |
| Forwarding_Table_Update_Identifier | | | : | abcd |
| Dependent_Origin_Unicast_Addr_Range_­List_­Size | | | : | 02 |
| Dependent_Target_Unicast_Addr_Range_­List_­Size | | | : | 03 |
| Dependent_Origin_Unicast_Addr_Range_­List | | | : |  |
|  | (#00) | Dependent_Origin_Unicast_­Addr_­Range | : | (primary:12aa, range_length:02) |
|  | (#01) | Dependent_Origin_Unicast_­Addr_­Range | : | (primary:12bb, range_length:03) |
| Dependent_Target_Unicast_Addr_­Range_­List | | | : |  |
|  | (#00) | Dependent_Target_Unicast_­Addr_­Range | : | (primary:56aa, range_length:01) |
|  | (#01) | Dependent_Target_Unicast_­Addr_­Range | : | (primary:56bb, range_length:02) |
|  | (#02) | Dependent_Target_Unicast_­Addr_­Range | : | (primary:56cc, range_length:03) |
| Access message | | | : | 808b002371000034127856cdab020355250277250354ad77ad0299ad03 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01a0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01a00405060712345678 |
| EncAccessMessage | : | 48e05fa2a97734ce48fb970f6aefc8261bc12d8a0e8662df7851801604 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 7a45e7a0 |
| UpperTransportPDU | : | 48e05fa2a97734ce48fb970f6aefc8261bc12d8a0e8662df78518016047a45e7a0 |
| Segment#00 | : | 48e05fa2a97734ce48fb970f |
| Segment#01 | : | 6aefc8261bc12d8a0e8662df |
| Segment#02 | : | 78518016047a45e7a0 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01a0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01a0 | |
| SegO | : | 00 | |
| SegN | : | 02 | |
| Header | : | 80068002 | |
| Segment#00 | : |  | 48e05fa2a97734ce48fb970f |
| LowerTransportPDU | : | 8006800248e05fa2a97734ce48fb970f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01a0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8006800248e05fa2a97734ce48fb970f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01a00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01a0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8006800248e05fa2a97734ce48fb970f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 50cf373a8fba289a4295c00d0342b1c8029a | | |
| NetMIC | : |  |  |  |  |  |  | 83d87e31 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567850cf373a8fba28 |
| PECB | : | 528c5be5f934bd8212ce768bb06edd44 |
| CTL || TTL || SEQ || SRC | : | 07df01a00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6855535a45fd3150cf373a8fba289a4295c00d0342b1c8029a83d87e31 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01a1 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01a0 | |
| SegO | : | 01 | |
| SegN | : | 02 | |
| Header | : | 80068022 | |
| Segment#01 | : |  | 6aefc8261bc12d8a0e8662df |
| LowerTransportPDU | : | 800680226aefc8261bc12d8a0e8662df | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01a1 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 800680226aefc8261bc12d8a0e8662df | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01a10405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01a1 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 800680226aefc8261bc12d8a0e8662df | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5a1e0e8c2b0ed5a0ad21aa16c2fbfea0f148 | | |
| NetMIC | : |  |  |  |  |  |  | 670c9ba4 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785a1e0e8c2b0ed5 |
| PECB | : | 20fb663e2bb01ac93844c34afc417c8d |
| CTL || TTL || SEQ || SRC | : | 07df01a10405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 682724679f2fb55a1e0e8c2b0ed5a0ad21aa16c2fbfea0f148670c9ba4 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01a2 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01a0 | |
| SegO | : | 02 | |
| SegN | : | 02 | |
| Header | : | 80068042 | |
| Segment#02 | : |  | 78518016047a45e7a0 |
| LowerTransportPDU | : | 8006804278518016047a45e7a0 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01a2 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 8006804278518016047a45e7a0 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01a20405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01a2 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 8006804278518016047a45e7a0 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 6c25bec07bd01f73eb6641c4762174 | | |
| NetMIC | : |  |  |  |  |  |  | 840f3984 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456786c25bec07bd01f |
| PECB | : | 1e57a9478ea75b3c5a6410aaf33a7123 |
| CTL || TTL || SEQ || SRC | : | 07df01a20405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681988a8e58aa26c25bec07bd01f73eb6641c4762174840f3984 |

#### 8.16.28. FORWARDING_TABLE_ENTRIES_COUNT_GET

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_ENTRIES_COUNT_GET message to a Directed Forwarding Configuration Server to get the size of the fixed path entry list and the size of the non-fixed path entry list.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 808c (FORWARDING_TABLE_ENTRIES_COUNT_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 808c2301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01b0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01b00405060712345678 |
| EncAccessMessage | : | 94aadfc2 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | efbe7cb5 |
| UpperTransportPDU | : | 94aadfc2efbe7cb5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01b0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 94aadfc2efbe7cb5 |
| LowerTransportPDU | : | 0094aadfc2efbe7cb5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01b0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0094aadfc2efbe7cb5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01b00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01b0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0094aadfc2efbe7cb5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | f5296d87545c4ac65cfae6 | | |
| NetMIC | : |  |  |  |  |  |  | c6a17638 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678f5296d87545c4a |
| PECB | : | 11cf5cf5d61b874d1ce37e67bb5953f1 |
| CTL||TTL||SEQ||SRC | : | 07df01b00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6816105d45d21ef5296d87545c4ac65cfae6c6a17638 |

#### 8.16.29. FORWARDING_TABLE_ENTRIES_COUNT_STATUS

A Directed Forwarding Configuration Server receives a FORWARDING_TABLE_ENTRIES_COUNT_GET message from a Directed Forwarding Configuration Client and responds with a FORWARDING_TABLE_ENTRIES_COUNT_STATUS message with Status equal to Success.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 808d (FORWARDING_TABLE_ENTRIES_COUNT_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Forwarding_Table_Update_­Identifier | : | abcd |
| Fixed_Path_Entries_­Count | : | 0001 |
| Non_Fixed_Path_Entries_­Count | : | 0002 |
| Access message | : | 808d002301cdab01000200 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01c0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df01c00607040512345678 |
| EncAccessMessage | : | 04e2aaa0d1cc9079d4926e |
| TransMIC Size | : | 32 bits |
| TransMIC | : | b2f241e5 |
| UpperTransportPDU | : | 04e2aaa0d1cc9079d4926eb2f241e5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01c0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 04e2aaa0d1cc9079d4926eb2f241e5 |
| LowerTransportPDU | : | 0004e2aaa0d1cc9079d4926eb2f241e5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01c0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0004e2aaa0d1cc9079d4926eb2f241e5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01c00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01c0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0004e2aaa0d1cc9079d4926eb2f241e5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 327651584f5bab567260df2fb6d372b6eb3f | | |
| NetMIC | : |  |  |  |  |  |  | fc3f8181 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678327651584f5bab |
| PECB | : | a5bd57fb7a09171e7efbc85559695421 |
| CTL||TTL||SEQ||SRC | : | 07df01c00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68a262563b7c0e327651584f5bab567260df2fb6d372b6eb3ffc3f8181 |

#### 8.16.30. FORWARDING_TABLE_ENTRIES_GET

A Directed Forwarding Configuration Client sends a FORWARDING_TABLE_ENTRIES_GET message to a Directed Forwarding Configuration Server to get the list of fixed path entries and non-fixed path entries from any Path Origin to any destination.

|  |
| --- |
| Access message |

|  |  |  |  |
| --- | --- | --- | --- |
| Opcode | | : | 808e (FORWARDING_TABLE_ENTRIES_GET) |
| NetKeyIndex | | : | 0123 |
| Filter_Mask | | : |  |
|  | Fixed_Paths | : | 01 |
|  | Non_Fixed_Paths | : | 01 |
|  | Path_Origin_Match | : | 00 |
|  | Destination_Match | : | 00 |
| Start_Index | | : | 0000 |
| Forwarding_Table_Update_­Identifier | | : | abcd |
| Access message | | : | 808e23310000cdab |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01d0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01d00405060712345678 |
| EncAccessMessage | : | 60792b074f64ba9a |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 116e3ee1 |
| UpperTransportPDU | : | 60792b074f64ba9a116e3ee1 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01d0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 60792b074f64ba9a116e3ee1 |
| LowerTransportPDU | : | 0060792b074f64ba9a116e3ee1 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01d0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0060792b074f64ba9a116e3ee1 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01d00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01d0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0060792b074f64ba9a116e3ee1 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | dca60a478662d827a30fbb64811ab0 | | |
| NetMIC | : |  |  |  |  |  |  | 16574629 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678dca60a478662d8 |
| PECB | : | dde6d076d9c34b152a562bcdbef513c3 |
| CTL||TTL||SEQ||SRC | : | 07df01d00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68da39d1a6ddc6dca60a478662d827a30fbb64811ab016574629 |

#### 8.16.31. FORWARDING_TABLE_ENTRIES_STATUS

A Directed Forwarding Configuration Server receives a FORWARDING_TABLE_ENTRIES_GET message from a Directed Forwarding Configuration Client and responds with a FORWARDING_TABLE_ENTRIES_STATUS message that reports a fixed path entry to a unicast destination, a non-fixed path entry to a unicast destination, and a non-fixed path
entry to a multicast destination. The message is sent in five segments.

|  |
| --- |
| Access message |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opcode | | | : | 808f (FORWARDING_TABLE_ENTRIES_STATUS) |
| Status | | | : | 00 (Success) |
| NetKeyIndex | | | : | 0123 |
| Filter_Mask | | | : |  |
|  | Fixed_Paths | | : | 01 |
|  | Non_Fixed_Paths | | : | 01 |
|  | Path_Origin_Match | | : | 00 |
|  | Destination_Match | | : | 00 |
| Start_Index | | | : | 0000 |
| Forwarding_Table_Update_Identifier | | | : | abcd |
| Forwarding_Table_Entry_List[0] | | | : |  |
|  | Forwarding_Table_Entry_Header | | : |  |
|  |  | Fixed_Path_Flag | : | 01 |
|  |  | Unicast_Destination | : | 01 |
|  |  | Backward_Path_Validated_Flag | : | 01 |
|  |  | Bearer_Toward_Path_Origin_Indicator | : | 01 |
|  |  | Bearer_Toward_Path_Target_Indicator | : | 01 |
|  |  | Dependent_Origin_List_Size_Indicator | : | 01 |
|  |  | Dependent_Target_List_Size_Indicator | : | 01 |
|  | Path_Origin_Unicast_Addr_Range | | : | (primary:1234, range_length:03) |
|  | Dependent_Origin_List_Size | | : | 02 |
|  | Bearer_Toward_Path_Origin | | : | 0001 |
|  | Path_Target_Unicast_Addr_Range | | : | (primary:5678, range_length:05) |
|  | Dependent_Target_List_Size | | : | 03 |
|  | Bearer_Toward_Path_Target | | : | 0001 |
| Forwarding_Table_Entry_List[1] | | | : |  |
|  | Forwarding_Table_Entry_Header | | : |  |
|  |  | Fixed_Path_Flag | : | 00 |
|  |  | Unicast_Destination | : | 01 |
|  |  | Backward_Path_Validated_Flag | : | 01 |
|  |  | Bearer_Toward_Path_Origin_Indicator | : | 01 |
|  |  | Bearer_Toward_Path_Target_Indicator | : | 00 |
|  |  | Dependent_Origin_List_Size_Indicator | : | 01 |
|  |  | Dependent_Target_List_Size_Indicator | : | 01 |
|  | Lane_Counter | | : | 02 |
|  | Path_Remaining_Time | | : | 0014 |
|  | Path_Origin_Forwarding_Number | | : | 0c |
|  | Path_Origin_Unicast_Addr_Range | | : | (primary:0405, range_length:06) |
|  | Dependent_Origin_List_Size | | : | 01 |
|  | Bearer_Toward_Path_Origin | | : | 0001 |
|  | Path_Target_Unicast_Addr_Range | | : | (primary:0607, range_length:05) |
|  | Dependent_Target_List_Size | | : | 01 |
| Forwarding_Table_Entry_List[2] | | | : |  |
|  | Forwarding_Table_Entry_Header | | : |  |
|  |  | Fixed_Path_Flag | : | 00 |
|  |  | Unicast_Destination | : | 00 |
|  |  | Backward_Path_Validated_Flag | : | 00 |
|  |  | Bearer_Toward_Path_Origin_Indicator | : | 01 |
|  |  | Bearer_Toward_Path_Target_Indicator | : | 01 |
|  |  | Dependent_Origin_List_Size_Indicator | : | 00 |
|  |  | Dependent_Target_List_Size_Indicator | : | 00 |
|  | Lane_Counter | | : | 01 |
|  | Path_Remaining_Time | | : | 002d |
|  | Path_Origin_Forwarding_Number | | : | 0d |
|  | Path_Origin_Unicast_Addr_Range | | : | (primary:0405, range_length:06) |
|  | Bearer_Toward_Path_Origin | | : | 0001 |
|  | Multicast_Destination | | : | c000 |
|  | Bearer_Toward_Path_Target | | : | 0001 |
| Access message | | | : |  |
| 808f0023310000cdabbf00692403020100f1ac05030100ae000214000c0b08060101000f0c05011800012d000d0b0806010000c00100 | | | | |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01e0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df01e00607040512345678 |
| EncAccessMessage | : |  |
| c33f46475df1a8413612311277ccebef27d8bda77eab1898d8c6c9f7cbb7c2e6a316f26b4eab5296ee6a2c3a0b08567da4c3d133e9db | | |
| TransMIC Size | : | 32 bits |
| TransMIC | : | f0f13a3f |
| UpperTransportPDU | : |  |
| c33f46475df1a8413612311277ccebef27d8bda77eab1898d8c6c9f7cbb7c2e6a316f26b4eab5296ee6a2c3a0b08567da4c3d133e9dbf0f13a3f | | |
| Segment#00 | : | c33f46475df1a84136123112 |
| Segment#01 | : | 77ccebef27d8bda77eab1898 |
| Segment#02 | : | d8c6c9f7cbb7c2e6a316f26b |
| Segment#03 | : | 4eab5296ee6a2c3a0b08567d |
| Segment#04 | : | a4c3d133e9dbf0f13a3f |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01e0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01e0 | |
| SegO | : | 00 | |
| SegN | : | 04 | |
| Header | : | 80078004 | |
| Segment#00 | : |  | c33f46475df1a84136123112 |
| LowerTransportPDU | : | 80078004c33f46475df1a84136123112 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01e0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 80078004c33f46475df1a84136123112 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01e00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01e0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 80078004c33f46475df1a84136123112 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | cc339eabe291df59e1c7cf2a12f2b8bf7587 | | |
| NetMIC | : |  |  |  |  |  |  | ecfedad9 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678cc339eabe291df |
| PECB | : | 2d48edf40d39f7240d4d09b12b1b9892 |
| CTL || TTL || SEQ || SRC | : | 07df01e00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 682a97ec140b3ecc339eabe291df59e1c7cf2a12f2b8bf7587ecfedad9 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01e1 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01e0 | |
| SegO | : | 01 | |
| SegN | : | 04 | |
| Header | : | 80078024 | |
| Segment#01 | : |  | 77ccebef27d8bda77eab1898 |
| LowerTransportPDU | : | 8007802477ccebef27d8bda77eab1898 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01e1 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 8007802477ccebef27d8bda77eab1898 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01e10607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01e1 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 8007802477ccebef27d8bda77eab1898 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b6e3bdb24821e4aa75a178254a7d03e04481 | | |
| NetMIC | : |  |  |  |  |  |  | 665867a0 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678b6e3bdb24821e4 |
| PECB | : | 4ff535e932bf7a2ea64b099927c494da |
| CTL || TTL || SEQ || SRC | : | 07df01e10607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68482a340834b8b6e3bdb24821e4aa75a178254a7d03e04481665867a0 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01e2 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01e0 | |
| SegO | : | 02 | |
| SegN | : | 04 | |
| Header | : | 80078044 | |
| Segment#02 | : |  | d8c6c9f7cbb7c2e6a316f26b |
| LowerTransportPDU | : | 80078044d8c6c9f7cbb7c2e6a316f26b | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01e2 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 80078044d8c6c9f7cbb7c2e6a316f26b | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01e20607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01e2 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 80078044d8c6c9f7cbb7c2e6a316f26b | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 038bbd0fa5f592b929747b017d0fb7f0292b | | |
| NetMIC | : |  |  |  |  |  |  | da0c7c08 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678038bbd0fa5f592 |
| PECB | : | d4a205b930f70e502851e7eef179cbcc |
| CTL || TTL || SEQ || SRC | : | 07df01e20607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68d37d045b36f0038bbd0fa5f592b929747b017d0fb7f0292bda0c7c08 |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01e3 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01e0 | |
| SegO | : | 03 | |
| SegN | : | 04 | |
| Header | : | 80078064 | |
| Segment#03 | : |  | 4eab5296ee6a2c3a0b08567d |
| LowerTransportPDU | : | 800780644eab5296ee6a2c3a0b08567d | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01e3 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 800780644eab5296ee6a2c3a0b08567d | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01e30607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01e3 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 800780644eab5296ee6a2c3a0b08567d | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 62c9976de32be43dac3003e13bd75b48a3d0 | | |
| NetMIC | : |  |  |  |  |  |  | 97326d0d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567862c9976de32be4 |
| PECB | : | 1cd8e42dec77272ad13c19aedfa56cce |
| CTL || TTL || SEQ || SRC | : | 07df01e30607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681b07e5ceea7062c9976de32be43dac3003e13bd75b48a3d097326d0d |

|  |
| --- |
| LowerTransportSegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01e4 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 01 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| SZMIC | : | 00 | |
| SeqZero | : | 01e0 | |
| SegO | : | 04 | |
| SegN | : | 04 | |
| Header | : | 80078084 | |
| Segment#04 | : |  | a4c3d133e9dbf0f13a3f |
| LowerTransportPDU | : | 80078084a4c3d133e9dbf0f13a3f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01e4 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 80078084a4c3d133e9dbf0f13a3f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01e40607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01e4 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 80078084a4c3d133e9dbf0f13a3f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 610a77caee0801355ab8511e4c6a9a8d | | |
| NetMIC | : |  |  |  |  |  |  | 88fd1afe |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678610a77caee0801 |
| PECB | : | c1420443ac3792d268f6962bbfea673b |
| CTL || TTL || SEQ || SRC | : | 07df01e40607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68c69d05a7aa30610a77caee0801355ab8511e4c6a9a8d88fd1afe |

#### 8.16.32. WANTED_LANES_GET

A Directed Forwarding Configuration Client sends a WANTED_LANES_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8090 (WANTED_LANES_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 80902301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df01f0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df01f00405060712345678 |
| EncAccessMessage | : | d2addc32 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 3fe81403 |
| UpperTransportPDU | : | d2addc323fe81403 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df01f0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | d2addc323fe81403 |
| LowerTransportPDU | : | 00d2addc323fe81403 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df01f0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00d2addc323fe81403 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df01f00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df01f0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00d2addc323fe81403 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 19e0c0f7b56963a718022a | | |
| NetMIC | : |  |  |  |  |  |  | ed3d66fe |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567819e0c0f7b56963 |
| PECB | : | 9c8fe936f6d8e441433588164570d52c |
| CTL || TTL || SEQ || SRC | : | 07df01f00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 689b50e8c6f2dd19e0c0f7b56963a718022aed3d66fe |

#### 8.16.33. WANTED_LANES_SET

A Directed Forwarding Configuration Client sends a WANTED_LANES_SET message to a Directed Forwarding Configuration Server to set the number of wanted lanes to 2.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8091 (WANTED_LANES_SET) |
| NetKeyIndex | : | 0123 |
| Wanted_Lanes | : | 02 |
| Access message | : | 8091230102 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0200 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02000405060712345678 |
| EncAccessMessage | : | 9114c492b9 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 3e772a05 |
| UpperTransportPDU | : | 9114c492b93e772a05 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0200 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 9114c492b93e772a05 |
| LowerTransportPDU | : | 009114c492b93e772a05 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0200 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 009114c492b93e772a05 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02000405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0200 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 009114c492b93e772a05 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2c50ebf1217b60bd8e341b8e | | |
| NetMIC | : |  |  |  |  |  |  | 937be35f |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456782c50ebf1217b60 |
| PECB | : | cdf8a3ef1bf65a69b64897714efdc3ce |
| CTL || TTL || SEQ || SRC | : | 07df02000405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68ca27a1ef1ff32c50ebf1217b60bd8e341b8e937be35f |

#### 8.16.34. WANTED_LANES_STATUS

A Directed Forwarding Configuration Server receives a WANTED_LANES_GET message or a WANTED_LANES_SET message from a Directed Forwarding Configuration Client and responds with a WANTED_LANES_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8092 (WANTED_LANES_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Wanted_Lanes | : | 02 |
| Access message | : | 809200230102 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0210 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02100405060712345678 |
| EncAccessMessage | : | 5084b4df6a89 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 841f73ce |
| UpperTransportPDU | : | 5084b4df6a89841f73ce |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0210 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 5084b4df6a89841f73ce |
| LowerTransportPDU | : | 005084b4df6a89841f73ce | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0210 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 005084b4df6a89841f73ce | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02100405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0210 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 005084b4df6a89841f73ce | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 96205f1771c646f5d2ac4c7afd | | |
| NetMIC | : |  |  |  |  |  |  | 31f0c744 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567896205f1771c646 |
| PECB | : | 788cfc1d34fa840abdd07ef67750805c |
| CTL||TTL||SEQ||SRC | : | 07df02100405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 687f53fe0d30ff96205f1771c646f5d2ac4c7afd31f0c744 |

#### 8.16.35. TWO_WAY_PATH_GET

A Directed Forwarding Configuration Client sends a TWO_WAY_PATH_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8093 (TWO_WAY_PATH_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 80932301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0220 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02200405060712345678 |
| EncAccessMessage | : | f580b18f |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 86d47006 |
| UpperTransportPDU | : | f580b18f86d47006 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0220 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | f580b18f86d47006 |
| LowerTransportPDU | : | 00f580b18f86d47006 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0220 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00f580b18f86d47006 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02200405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0220 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00f580b18f86d47006 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2f1c97e36e519ffe0c7a6e | | |
| NetMIC | : |  |  |  |  |  |  | 3b129eb4 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456782f1c97e36e519f |
| PECB | : | e52f7190e9785cf96205e33d92812d23 |
| CTL||TTL||SEQ||SRC | : | 07df02200405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68e2f073b0ed7d2f1c97e36e519ffe0c7a6e3b129eb4 |

#### 8.16.36. TWO_WAY_PATH_SET

A Directed Forwarding Configuration Client sends a TWO_WAY_PATH_SET message to a Directed Forwarding Configuration Server to not allow the node to send messages along the paths for which the node is the Path Target.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8094 (TWO_WAY_PATH_SET) |
| NetKeyIndex | : | 0123 |
| Two_Way_Path | : | 00 |
| Access message | : | 8094230100 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0230 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02300405060712345678 |
| EncAccessMessage | : | 4044755e75 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 13342708 |
| UpperTransportPDU | : | 4044755e7513342708 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0230 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 4044755e7513342708 |
| LowerTransportPDU | : | 004044755e7513342708 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0230 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 004044755e7513342708 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02300405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0230 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 004044755e7513342708 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 582bef32253b5dcbce3d05ce | | |
| NetMIC | : |  |  |  |  |  |  | bb4ffdae |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678582bef32253b5d |
| PECB | : | 8eb709ba264d4c3fcf498830c8adb7a8 |
| CTL||TTL||SEQ||SRC | : | 07df02300405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6889680b8a2248582bef32253b5dcbce3d05cebb4ffdae |

#### 8.16.37. TWO_WAY_PATH_STATUS

A Directed Forwarding Configuration Server receives a TWO_WAY_PATH_GET message or a TWO_WAY_PATH_SET message from a Directed Forwarding Configuration Client and responds with a TWO_WAY_PATH_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8095 (TWO_WAY_PATH_STATUS) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Two_Way_Path | : | 00 |
| Access message | : | 809500230100 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0240 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02400405060712345678 |
| EncAccessMessage | : | 1a3411c157f5 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 0428e471 |
| UpperTransportPDU | : | 1a3411c157f50428e471 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0240 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 1a3411c157f50428e471 |
| LowerTransportPDU | : | 001a3411c157f50428e471 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0240 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 001a3411c157f50428e471 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02400405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0240 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 001a3411c157f50428e471 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 02ebb7bbb6ec3b3254bf9fab43 | | |
| NetMIC | : |  |  |  |  |  |  | 9ecf472c |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567802ebb7bbb6ec3b |
| PECB | : | b3752c8ff0ea2bca9d1bf77b1103e699 |
| CTL||TTL||SEQ||SRC | : | 07df02400405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68b4aa2ecff4ef02ebb7bbb6ec3b3254bf9fab439ecf472c |

#### 8.16.38. PATH_ECHO_INTERVAL_GET

A Directed Forwarding Configuration Client sends a PATH_ECHO_INTERVAL_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8096 (PATH_ECHO_INTERVAL_GET) |
| NetKeyIndex | : | 0123 |
| Access message | : | 80962301 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0250 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02500405060712345678 |
| EncAccessMessage | : | f86a3f99 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | b3bfcaa8 |
| UpperTransportPDU | : | f86a3f99b3bfcaa8 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0250 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | f86a3f99b3bfcaa8 |
| LowerTransportPDU | : | 00f86a3f99b3bfcaa8 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0250 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00f86a3f99b3bfcaa8 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02500405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0250 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00f86a3f99b3bfcaa8 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 022a91298c8fe49cd22a05 | | |
| NetMIC | : |  |  |  |  |  |  | 21c07239 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678022a91298c8fe4 |
| PECB | : | a8fa5039aa21821b93d326b48ce1d3a5 |
| CTL||TTL||SEQ||SRC | : | 07df02500405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68af255269ae24022a91298c8fe49cd22a0521c07239 |

#### 8.16.39. PATH_ECHO_INTERVAL_SET

A Directed Forwarding Configuration Client sends a PATH_ECHO_INTERVAL_SET message to a Directed Forwarding Configuration Server to allow the execution of the Directed Forwarding Echo operation and set the interval between two Directed Forwarding Echo procedures to the 20% of a path lifetime, for both the unicast address
destinations and the group address or the virtual address destinations.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8097 (PATH_ECHO_INTERVAL_SET) |
| NetKeyIndex | : | 0123 |
| Unicast_Echo_Interval | : | 14 (20%) |
| Multicast_Echo_Interval | : | 14 (20%) |
| Access message | : | 809723011414 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0260 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02600405060712345678 |
| EncAccessMessage | : | 71f675260918 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | de8878a7 |
| UpperTransportPDU | : | 71f675260918de8878a7 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0260 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 71f675260918de8878a7 |
| LowerTransportPDU | : | 0071f675260918de8878a7 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0260 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0071f675260918de8878a7 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02600405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0260 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0071f675260918de8878a7 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 9f44d668a4275663d97f46d1a1 | | |
| NetMIC | : |  |  |  |  |  |  | 00e95cc2 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456789f44d668a42756 |
| PECB | : | 8f34238cfc9ede4e36f3dd5903ecc89b |
| CTL||TTL||SEQ||SRC | : | 07df02600405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6888eb21ecf89b9f44d668a4275663d97f46d1a100e95cc2 |

#### 8.16.40. PATH_ECHO_INTERVAL_STATUS

A Directed Forwarding Configuration Server receives a PATH_ECHO_INTERVAL_GET message or a PATH_ECHO_INTERVAL_SET message from a Directed Forwarding Configuration Client and responds with a PATH_ECHO_INTERVAL_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8098 (PATH_ECHO_INTERVAL_SET) |
| Status | : | 00 (Success) |
| NetKeyIndex | : | 0123 |
| Unicast_Echo_Interval | : | 14 (20%) |
| Multicast_Echo_Interval | : | 14 (20%) |
| Access message | : | 80980023011414 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0270 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02700405060712345678 |
| EncAccessMessage | : | bccc501afc9f40 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | d4a23efa |
| UpperTransportPDU | : | bccc501afc9f40d4a23efa |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0270 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | bccc501afc9f40d4a23efa |
| LowerTransportPDU | : | 00bccc501afc9f40d4a23efa | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0270 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00bccc501afc9f40d4a23efa | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02700405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0270 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00bccc501afc9f40d4a23efa | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | bc2e14d917af9fc73230e97f23db | | |
| NetMIC | : |  |  |  |  |  |  | f54908a9 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678bc2e14d917af9f |
| PECB | : | bd8002cb17af9d16977abd628a5f9a6c |
| CTL||TTL||SEQ||SRC | : | 07df02700405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68ba5f00bb13aabc2e14d917af9fc73230e97f23dbf54908a9 |

#### 8.16.41. DIRECTED_NETWORK_TRANSMIT_GET

A Directed Forwarding Configuration Client sends a DIRECTED_NETWORK_TRANSMIT_GET message to a Directed Forwarding Configuration Server to read its Directed Network Transmit state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 8099 (DIRECTED_NETWORK_TRANSMIT_GET) |
| Access message | : | 8099 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0280 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02800405060712345678 |
| EncAccessMessage | : | e61f |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 9c3816ba |
| UpperTransportPDU | : | e61f9c3816ba |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0280 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | e61f9c3816ba |
| LowerTransportPDU | : | 00e61f9c3816ba | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0280 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00e61f9c3816ba | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02800405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0280 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00e61f9c3816ba | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | cf4b24c0867c7a8cd9 | | |
| NetMIC | : |  |  |  |  |  |  | 4ea473d2 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678cf4b24c0867c7a |
| PECB | : | 70653c8ff65b840df5ef5dbc8c8df0a6 |
| CTL||TTL||SEQ||SRC | : | 07df02800405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6877ba3e0ff25ecf4b24c0867c7a8cd94ea473d2 |

#### 8.16.42. DIRECTED_NETWORK_TRANSMIT_SET

A Directed Forwarding Configuration Client sends a DIRECTED_NETWORK_TRANSMIT_SET message to a Directed Forwarding Configuration Server to set to 3 the number of retransmissions of Network PDUs with CTL equal to 0 originated by the node and sent along paths, and to set the minimum interval between transmissions to 170
milliseconds.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809a (DIRECTED_NETWORK_TRANSMIT_SET) |
| Directed_Network_Transmit_Count | : | 03 |
| Directed_Network_Transmit_Interval_Steps | : | 10 (170 ms) |
| Access message | : | 809a83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0290 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02900405060712345678 |
| EncAccessMessage | : | b4651b |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 68d89822 |
| UpperTransportPDU | : | b4651b68d89822 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0290 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | b4651b68d89822 |
| LowerTransportPDU | : | 00b4651b68d89822 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0290 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00b4651b68d89822 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02900405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0290 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00b4651b68d89822 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 28699a7753541406d94e | | |
| NetMIC | : |  |  |  |  |  |  | 959d22ba |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567828699a77535414 |
| PECB | : | 59c438dbc81195ac08f00e3d18290eac |
| CTL||TTL||SEQ||SRC | : | 07df02900405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 685e1b3a4bcc1428699a7753541406d94e959d22ba |

#### 8.16.43. DIRECTED_NETWORK_TRANSMIT_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_NETWORK_TRANSMIT_GET message or a DIRECTED_NETWORK_TRANSMIT_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_NETWORK_TRANSMIT_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809b (DIRECTED_NETWORK_TRANSMIT_STATUS) |
| Directed_Network_Transmit_Count | : | 03 |
| Directed_Network_Transmit_Interval_­Steps | : | 10 (170 ms) |
| Access message | : | 809b83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02a0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df02a00607040512345678 |
| EncAccessMessage | : | 01020d |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 7519db9b |
| UpperTransportPDU | : | 01020d7519db9b |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02a0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 01020d7519db9b |
| LowerTransportPDU | : | 0001020d7519db9b | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02a0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0001020d7519db9b | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02a00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02a0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0001020d7519db9b | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 87b37571c1fd02592fad | | |
| NetMIC | : |  |  |  |  |  |  | ab9ab507 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567887b37571c1fd02 |
| PECB | : | f20412a1979ec7aeeba4f1d7347466b1 |
| CTL||TTL||SEQ||SRC | : | 07df02a00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68f5db1001919987b37571c1fd02592fadab9ab507 |

#### 8.16.44. DIRECTED_RELAY_RETRANSMIT_GET

A Directed Forwarding Configuration Client sends a DIRECTED_RELAY_RETRANSMIT_GET message to a Directed Forwarding Configuration Server to read its Directed Relay Retransmit state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809c (DIRECTED_RELAY_RETRANSMIT_GET) |
| Access message | : | 809c |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02b0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02b00405060712345678 |
| EncAccessMessage | : | e5bc |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 4df32df6 |
| UpperTransportPDU | : | e5bc4df32df6 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02b0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | e5bc4df32df6 |
| LowerTransportPDU | : | 00e5bc4df32df6 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02b0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00e5bc4df32df6 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02b00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02b0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00e5bc4df32df6 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | be63e8ea463e9aca9c | | |
| NetMIC | : |  |  |  |  |  |  | ea5588c4 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678be63e8ea463e9a |
| PECB | : | d48e56dae17c9f59746fef68382a78c7 |
| CTL||TTL||SEQ||SRC | : | 07df02b00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68d351546ae579be63e8ea463e9aca9cea5588c4 |

#### 8.16.45. DIRECTED_RELAY_RETRANSMIT_SET

A Directed Forwarding Configuration Client sends a DIRECTED_RELAY_RETRANSMIT_SET message to a Directed Forwarding Configuration Server to set to 3 the number of retransmissions of Network PDUs with CTL equal to 0 relayed by the node along paths, and to set the minimum interval between transmissions to 170 milliseconds.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809d (DIRECTED_RELAY_RETRANSMIT_SET) |
| Directed_Relay_Retransmit_Count | : | 03 |
| Directed_Relay_Retransmit_Interval_Steps | : | 10 (170 ms) |
| Access message | : | 809d83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02c0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02c00405060712345678 |
| EncAccessMessage | : | 0627d5 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 50adbeec |
| UpperTransportPDU | : | 0627d550adbeec |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02c0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 0627d550adbeec |
| LowerTransportPDU | : | 000627d550adbeec | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02c0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 000627d550adbeec | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02c00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02c0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 000627d550adbeec | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 03b8147d2d4ba5c0ee19 | | |
| NetMIC | : |  |  |  |  |  |  | cc069181 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567803b8147d2d4ba5 |
| PECB | : | 286d9442467a86ebb795bdf65912fa5b |
| CTL||TTL||SEQ||SRC | : | 07df02c00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 682fb29682427f03b8147d2d4ba5c0ee19cc069181 |

#### 8.16.46. DIRECTED_RELAY_RETRANSMIT_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_RELAY_RETRANSMIT_GET message or a DIRECTED_RELAY_RETRANSMIT_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_RELAY_RETRANSMIT_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809e (DIRECTED_RELAY_RETRANSMIT_STATUS) |
| Directed_Relay_Retransmit_Count | : | 03 |
| Directed_Relay_Retransmit_Interval_Steps | : | 10 (170 ms) |
| Access message | : | 809e83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02d0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df02d00607040512345678 |
| EncAccessMessage | : | e2f581 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | cdb99405 |
| UpperTransportPDU | : | e2f581cdb99405 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02d0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | e2f581cdb99405 |
| LowerTransportPDU | : | 00e2f581cdb99405 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02d0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 00e2f581cdb99405 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02d00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02d0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 00e2f581cdb99405 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 109cd772a70ffb99fd64 | | |
| NetMIC | : |  |  |  |  |  |  | db49df2d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678109cd772a70ffb |
| PECB | : | 70e6917e4d58ff2458f80c1a866d7d00 |
| CTL||TTL||SEQ||SRC | : | 07df02d00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68773993ae4b5f109cd772a70ffb99fd64db49df2d |

#### 8.16.47. RSSI_THRESHOLD_GET

A Directed Forwarding Configuration Client sends a RSSI_THRESHOLD_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 809f (RSSI_THRESHOLD_GET) |
| Access message | : | 809f |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02e0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02e00405060712345678 |
| EncAccessMessage | : | 62f2 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 9cf8686f |
| UpperTransportPDU | : | 62f29cf8686f |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02e0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 62f29cf8686f |
| LowerTransportPDU | : | 0062f29cf8686f | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02e0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0062f29cf8686f | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02e00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02e0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0062f29cf8686f | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 8b48198810a096b4a3 | | |
| NetMIC | : |  |  |  |  |  |  | 7e8db7b8 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456788b48198810a096 |
| PECB | : | c15f555ed4e71a63bb53144064f68663 |
| CTL||TTL||SEQ||SRC | : | 07df02e00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68c68057bed0e28b48198810a096b4a37e8db7b8 |

#### 8.16.48. RSSI_THRESHOLD_SET

A Directed Forwarding Configuration Client sends a RSSI_THRESHOLD_SET message to a Directed Forwarding Configuration Server to set the RSSI margin above the default RSSI threshold to 15 dB.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a0 (RSSI_THRESHOLD_SET) |
| RSSI_Margin | : | 0f (15 dB) |
| Access message | : | 80a00f |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df02f0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df02f00405060712345678 |
| EncAccessMessage | : | 237dc5 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 5e18e360 |
| UpperTransportPDU | : | 237dc55e18e360 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df02f0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 237dc55e18e360 |
| LowerTransportPDU | : | 00237dc55e18e360 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df02f0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00237dc55e18e360 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df02f00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df02f0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00237dc55e18e360 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 57bfefa92be6780a8338 | | |
| NetMIC | : |  |  |  |  |  |  | ee1e1779 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567857bfefa92be678 |
| PECB | : | e7cbcd00dd6033a838b14c070237146b |
| CTL||TTL||SEQ||SRC | : | 07df02f00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68e014cff0d96557bfefa92be6780a8338ee1e1779 |

#### 8.16.49. RSSI_THRESHOLD_STATUS

A Directed Forwarding Configuration Server receives a RSSI_THRESHOLD_GET message or a RSSI_THRESHOLD_SET message from a Directed Forwarding Configuration Client and responds with a RSSI_THRESHOLD_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a1 (RSSI_THRESHOLD_STATUS) |
| Default_RSSI_Threshold | : | b0 (-80 dBm) |
| RSSI_Margin | : | 0f (15 dB) |
| Access message | : | 80a1b00f |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0300 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03000405060712345678 |
| EncAccessMessage | : | e2443314 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | c47df688 |
| UpperTransportPDU | : | e2443314c47df688 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0300 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | e2443314c47df688 |
| LowerTransportPDU | : | 00e2443314c47df688 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0300 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00e2443314c47df688 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03000405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0300 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00e2443314c47df688 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b731db64d73139164e8d53 | | |
| NetMIC | : |  |  |  |  |  |  | 06314603 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678b731db64d73139 |
| PECB | : | 472a14e6b3eff7f94f5ecac6b82f8bbf |
| CTL||TTL||SEQ||SRC | : | 07df03000405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6840f517e6b7eab731db64d73139164e8d5306314603 |

#### 8.16.50. DIRECTED_PATHS_GET

A Directed Forwarding Configuration Client sends a DIRECTED_PATHS_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a2 (DIRECTED_PATHS_GET) |
| Access message | : | 80a2 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0310 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03100405060712345678 |
| EncAccessMessage | : | 597a |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 2cf8be56 |
| UpperTransportPDU | : | 597a2cf8be56 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0310 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 597a2cf8be56 |
| LowerTransportPDU | : | 00597a2cf8be56 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0310 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00597a2cf8be56 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03100405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0310 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00597a2cf8be56 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 5a83b4d5f9c0163029 | | |
| NetMIC | : |  |  |  |  |  |  | 4354263d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456785a83b4d5f9c016 |
| PECB | : | c5d03e33f862ba1211c17a9f110679d2 |
| CTL||TTL||SEQ||SRC | : | 07df03100405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68c20f3d23fc675a83b4d5f9c01630294354263d |

#### 8.16.51. DIRECTED_PATHS_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_PATHS_GET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_PATHS_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a3 (DIRECTED_PATHS_STATUS) |
| Directed_Node_Paths | : | 0014 (20) |
| Directed_Relay_Paths | : | 0014 (20) |
| Directed_Proxy_Paths | : | 0014 (20) |
| Directed_Friend_Paths | : | 0014 (20) |
| Access message | : | 80a31400140014001400 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0320 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03200405060712345678 |
| EncAccessMessage | : | 15e6110547e0efe885ab |
| TransMIC Size | : | 32 bits |
| TransMIC | : | e68ed5ae |
| UpperTransportPDU | : | 15e6110547e0efe885abe68ed5ae |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0320 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 15e6110547e0efe885abe68ed5ae |
| LowerTransportPDU | : | 0015e6110547e0efe885abe68ed5ae | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0320 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0015e6110547e0efe885abe68ed5ae | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03200405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0320 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0015e6110547e0efe885abe68ed5ae | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | cc16936486acc553c5ece93513e54b9361 | | |
| NetMIC | : |  |  |  |  |  |  | 872b9fde |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678cc16936486acc5 |
| PECB | : | b865cee02008da2fee72ed8084f6926c |
| CTL||TTL||SEQ||SRC | : | 07df03200405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68bfbacdc0240dcc16936486acc553c5ece93513e54b9361872b9fde |

#### 8.16.52. DIRECTED_PUBLISH_POLICY_GET

A Directed Forwarding Configuration Client sends a DIRECTED_PUBLISH_POLICY_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a4 (DIRECTED_PUBLISH_POLICY_GET) |
| Element_Addr | : | 0607 |
| Model_ID | : | 1004 (Generic Default Transition Time) |
| Access message | : | 80a407060410 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0330 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03300405060712345678 |
| EncAccessMessage | : | 9ed13cf4d1e1 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 8c8b6fb5 |
| UpperTransportPDU | : | 9ed13cf4d1e18c8b6fb5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0330 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 9ed13cf4d1e18c8b6fb5 |
| LowerTransportPDU | : | 009ed13cf4d1e18c8b6fb5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0330 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 009ed13cf4d1e18c8b6fb5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03300405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0330 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 009ed13cf4d1e18c8b6fb5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 0b49fc1c88cdd068d5bdfb5cb4 | | |
| NetMIC | : |  |  |  |  |  |  | da0cd7b3 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456780b49fc1c88cdd0 |
| PECB | : | 54717ed965eea7b4509b313390d6b773 |
| CTL||TTL||SEQ||SRC | : | 07df03300405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 6853ae7de961eb0b49fc1c88cdd068d5bdfb5cb4da0cd7b3 |

#### 8.16.53. DIRECTED_PUBLISH_POLICY_SET

A Directed Forwarding Configuration Client sends a DIRECTED_PUBLISH_POLICY_SET message to a Directed Forwarding Configuration Server to configure its Generic Default Transition Time model to publish with directed forwarding.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a5 (DIRECTED_PUBLISH_POLICY_SET) |
| Directed_Publish_Policy | : | 01 (Directed Forwarding) |
| Element_Addr | : | 0607 |
| Model_ID | : | 1004 (Generic Default Transition Time) |
| Access message | : | 80a50107060410 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0340 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03400405060712345678 |
| EncAccessMessage | : | bdfa8dcce2c877 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 99f88343 |
| UpperTransportPDU | : | bdfa8dcce2c87799f88343 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0340 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | bdfa8dcce2c87799f88343 |
| LowerTransportPDU | : | 00bdfa8dcce2c87799f88343 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0340 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00bdfa8dcce2c87799f88343 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03400405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0340 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00bdfa8dcce2c87799f88343 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 587670208fd6ba97fd7fe0daa08c | | |
| NetMIC | : |  |  |  |  |  |  | 89b37aff |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678587670208fd6ba |
| PECB | : | 24cf534b2d2b92080e44311838f8a761 |
| CTL||TTL||SEQ||SRC | : | 07df03400405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 682310500b292e587670208fd6ba97fd7fe0daa08c89b37aff |

#### 8.16.54. DIRECTED_PUBLISH_POLICY_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_PUBLISH_POLICY_GET message or a DIRECTED_PUBLISH_POLICY_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_PUBLISH_POLICY_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a6 (DIRECTED_PUBLISH_POLICY_STATUS) |
| Status | : | 00 (Success) |
| Directed_Publish_Policy | : | 01 (Directed Forwarding) |
| Element_Addr | : | 0607 |
| Model_ID | : | 1004 (Generic Default Transition Time) |
| Access message | : | 80a6000107060410 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0350 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03500405060712345678 |
| EncAccessMessage | : | a4e2c4ecbfb16c1e |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 2319829c |
| UpperTransportPDU | : | a4e2c4ecbfb16c1e2319829c |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0350 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | a4e2c4ecbfb16c1e2319829c |
| LowerTransportPDU | : | 00a4e2c4ecbfb16c1e2319829c | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0350 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00a4e2c4ecbfb16c1e2319829c | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03500405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0350 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00a4e2c4ecbfb16c1e2319829c | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 6339d294c02c247ff214b2a5d90cb0 | | |
| NetMIC | : |  |  |  |  |  |  | 26f229c9 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456786339d294c02c24 |
| PECB | : | 15aff99653cfb9e031259bc5a963689c |
| CTL||TTL||SEQ||SRC | : | 07df03500405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681270fac657ca6339d294c02c247ff214b2a5d90cb026f229c9 |

#### 8.16.55. PATH_DISCOVERY_TIMING_CONTROL_GET

A Directed Forwarding Configuration Client sends a PATH_DISCOVERY_TIMING_CONTROL_GET message to a Directed Forwarding Configuration Server.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a7 (PATH_DISCOVERY_TIMING_CONTROL_GET) |
| Access message | : | 80a7 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0360 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03600405060712345678 |
| EncAccessMessage | : | 6255 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 0f04a8fa |
| UpperTransportPDU | : | 62550f04a8fa |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0360 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 62550f04a8fa |
| LowerTransportPDU | : | 0062550f04a8fa | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0360 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0062550f04a8fa | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03600405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0360 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0062550f04a8fa | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 58834404b04e7b6334 | | |
| NetMIC | : |  |  |  |  |  |  | 2e53ad53 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 00000000001234567858834404b04e7b |
| PECB | : | 759bede5d4a2d94e3a51365644c1b429 |
| CTL||TTL||SEQ||SRC | : | 07df03600405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 687244ee85d0a758834404b04e7b63342e53ad53 |

#### 8.16.56. PATH_DISCOVERY_TIMING_CONTROL_SET

A Directed Forwarding Configuration Client sends a PATH_DISCOVERY_TIMING_CONTROL_SET message to a Directed Forwarding Configuration Server to set the interval of collection of confirmations of the use of a path to 300 seconds, and to set the interval between a failing path discovery attempt and a new attempt to 500 seconds, and
to set the interval between the Path Discovery timer expiry and a new path discovery attempt to 2 seconds.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a8 (PATH_DISCOVERY_TIMING_CONTROL_SET) |
| Path_Monitoring_Interval | : | 012c |
| Path_Discovery_Retry_Interval | : | 01f4 |
| Path_Discovery_Interval | : | 01 |
| Lane_Discovery_Guard_Interval | : | 00 |
| Access message | : | 80a82c01f40101 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0370 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03700405060712345678 |
| EncAccessMessage | : | 52660e6a34039b |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 61cd5b74 |
| UpperTransportPDU | : | 52660e6a34039b61cd5b74 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0370 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 52660e6a34039b61cd5b74 |
| LowerTransportPDU | : | 0052660e6a34039b61cd5b74 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0370 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 0052660e6a34039b61cd5b74 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03700405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0370 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 0052660e6a34039b61cd5b74 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 6731cd28ef66f133b150963333f1 | | |
| NetMIC | : |  |  |  |  |  |  | 3dc21126 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456786731cd28ef66f1 |
| PECB | : | 1bfdfb61f3d45480baeb476a9b0521f6 |
| CTL||TTL||SEQ||SRC | : | 07df03700405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681c22f811f7d16731cd28ef66f133b150963333f13dc21126 |

#### 8.16.57. PATH_DISCOVERY_TIMING_CONTROL_STATUS

A Directed Forwarding Configuration Server receives a PATH_DISCOVERY_TIMING_CONTROL_GET message or a PATH_DISCOVERY_TIMING_CONTROL_SET message from a Directed Forwarding Configuration Client and responds with a PATH_DISCOVERY_TIMING_CONTROL_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80a9 (PATH_DISCOVERY_TIMING_CONTROL_STATUS) |
| Path_Monitoring_Interval | : | 012c |
| Path_Discovery_Retry_Interval | : | 01f4 |
| Path_Discovery_Interval | : | 01 |
| Lane_Discovery_Guard_Interval | : | 00 |
| Access message | : | 80a92c01f40101 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0380 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03800405060712345678 |
| EncAccessMessage | : | 4036029d49076c |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 21aba03e |
| UpperTransportPDU | : | 4036029d49076c21aba03e |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0380 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 4036029d49076c21aba03e |
| LowerTransportPDU | : | 004036029d49076c21aba03e | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0380 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 004036029d49076c21aba03e | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03800405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0380 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 004036029d49076c21aba03e | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | f839337a8930ba2ccf0bf8f125b4 | | |
| NetMIC | : |  |  |  |  |  |  | 343f2f37 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678f839337a8930ba |
| PECB | : | 9b97b5d94a7307a06635b5ca9865c610 |
| CTL||TTL||SEQ||SRC | : | 07df03800405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 689c48b6594e76f839337a8930ba2ccf0bf8f125b4343f2f37 |

#### 8.16.58. DIRECTED_CONTROL_NETWORK_TRANSMIT_GET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message to a Directed Forwarding Configuration Server to read its Directed Control Network Transmit state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80ab (DIRECTED_CONTROL_NETWORK_TRANSMIT_GET) |
| Access message | : | 80ab |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df0390 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03900405060712345678 |
| EncAccessMessage | : | 5c5c |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 6fc827c5 |
| UpperTransportPDU | : | 5c5c6fc827c5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df0390 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 5c5c6fc827c5 |
| LowerTransportPDU | : | 005c5c6fc827c5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df0390 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 005c5c6fc827c5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03900405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df0390 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 005c5c6fc827c5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | f0a485544f7792d87d | | |
| NetMIC | : |  |  |  |  |  |  | dae600f8 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678f0a485544f7792 |
| PECB | : | 480cdce96e57aadcefff1c829d0703e8 |
| CTL||TTL||SEQ||SRC | : | 07df03900405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 684fd3df796a52f0a485544f7792d87ddae600f8 |

#### 8.16.59. DIRECTED_CONTROL_NETWORK_TRANSMIT_SET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message to a Directed Forwarding Configuration Server to set to 3 the number of retransmissions of Network PDUs with CTL equal to 1 originated by the node and sent along paths, and to set the minimum interval between transmissions to 170
milliseconds.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80ac (DIRECTED_CONTROL_NETWORK_TRANSMIT_SET) |
| Directed_Control_Network_Transmit_­Count | : | 03 |
| Directed_Control_Network_Transmit_­Interval_­Steps | : | 10 (170 ms) |
| Access message | : | 80ac83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df03a0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03a00405060712345678 |
| EncAccessMessage | : | c350ad |
| TransMIC Size | : | 32 bits |
| TransMIC | : | f67ddd65 |
| UpperTransportPDU | : | c350adf67ddd65 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df03a0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | c350adf67ddd65 |
| LowerTransportPDU | : | 00c350adf67ddd65 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df03a0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00c350adf67ddd65 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03a00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df03a0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00c350adf67ddd65 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 7b1a6a1039ccc42ea812 | | |
| NetMIC | : |  |  |  |  |  |  | 64598598 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456787b1a6a1039ccc4 |
| PECB | : | 4c38286ec509bceec06bc2d720e84f1c |
| CTL||TTL||SEQ||SRC | : | 07df03a00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 684be72bcec10c7b1a6a1039ccc42ea81264598598 |

#### 8.16.60. DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_CONTROL_NETWORK_TRANSMIT_GET message or a DIRECTED_CONTROL_NETWORK_TRANSMIT_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80ad (DIRECTED_CONTROL_NETWORK_TRANSMIT_STATUS) |
| Directed_Control_Network_Transmit_­Count | : | 03 |
| Directed_Control_Network_Transmit_­Interval_­Steps | : | 10 (170 ms) |
| Access message | : | 80ad83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df03b0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df03b00607040512345678 |
| EncAccessMessage | : | 42be7f |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 5124bac5 |
| UpperTransportPDU | : | 42be7f5124bac5 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df03b0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 42be7f5124bac5 |
| LowerTransportPDU | : | 0042be7f5124bac5 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df03b0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0042be7f5124bac5 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03b00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df03b0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0042be7f5124bac5 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | 2a7280d2bd04dc3a9683 | | |
| NetMIC | : |  |  |  |  |  |  | da0b7d77 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 0000000000123456782a7280d2bd04dc |
| PECB | : | f49f0844001cd66d79a23af3af5875f1 |
| CTL||TTL||SEQ||SRC | : | 07df03b00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 68f3400bf4061b2a7280d2bd04dc3a9683da0b7d77 |

#### 8.16.61. DIRECTED_CONTROL_RELAY_RETRANSMIT_GET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message to a Directed Forwarding Configuration Server to read its Directed Control Relay Retransmit state.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80ae (DIRECTED_CONTROL_RELAY_RETRANSMIT_GET) |
| Access message | : | 80ae |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df03c0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03c00405060712345678 |
| EncAccessMessage | : | c75a |
| TransMIC Size | : | 32 bits |
| TransMIC | : | c1b75832 |
| UpperTransportPDU | : | c75ac1b75832 |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df03c0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | c75ac1b75832 |
| LowerTransportPDU | : | 00c75ac1b75832 | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df03c0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00c75ac1b75832 | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03c00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df03c0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00c75ac1b75832 | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | ce292660fc6fbacebb | | |
| NetMIC | : |  |  |  |  |  |  | 1d383d4d |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678ce292660fc6fba |
| PECB | : | 17ed71fe7db0fdf95f7ef8da4c041d9f |
| CTL||TTL||SEQ||SRC | : | 07df03c00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 681032723e79b5ce292660fc6fbacebb1d383d4d |

#### 8.16.62. DIRECTED_CONTROL_RELAY_RETRANSMIT_SET

A Directed Forwarding Configuration Client sends a DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message to a Directed Forwarding Configuration Server to set to 3 the number of retransmissions of Network PDUs with CTL equal to 1 relayed by the node along paths, and to set the minimum interval between transmissions to 170
milliseconds.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80af (DIRECTED_CONTROL_RELAY_RETRANSMIT_SET) |
| Directed_Control_Relay_­Retransmit_­Count | : | 03 |
| Directed_Control_Network_Transmit_­Interval_­Steps | : | 10 (170 ms) |
| Access message | : | 80af83 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df03d0 |
| SRC | : | 0405 |
| DST | : | 0607 |
| Device nonce | : | 0200df03d00405060712345678 |
| EncAccessMessage | : | 146b87 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 4bb5517e |
| UpperTransportPDU | : | 146b874bb5517e |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df03d0 | |
| SRC | : | 0405 | |
| DST | : | 0607 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 146b874bb5517e |
| LowerTransportPDU | : | 00146b874bb5517e | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df03d0 | | | | | | |
| SRC | : | 0405 | | | | | | |
| DST | : | 0607 | | | | | | |
| LowerTransportPDU | : | 00146b874bb5517e | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03d00405000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df03d0 | | | | |
| SRC | : |  |  |  | 0405 | | | |
| DST | : |  |  |  |  | 0607 | | |
| TransportPDU | : |  |  |  |  |  | 00146b874bb5517e | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | e31728d3bc62468278d6 | | |
| NetMIC | : |  |  |  |  |  |  | ea674365 |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678e31728d3bc6246 |
| PECB | : | 3b1bef5d6abd148e22d8de720bd90843 |
| CTL||TTL||SEQ||SRC | : | 07df03d00405 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 683cc4ec8d6eb8e31728d3bc62468278d6ea674365 |

#### 8.16.63. DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS

A Directed Forwarding Configuration Server receives a DIRECTED_CONTROL_RELAY_RETRANSMIT_GET message or a DIRECTED_CONTROL_RELAY_RETRANSMIT_SET message from a Directed Forwarding Configuration Client and responds with a DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS message.

|  |
| --- |
| Access message |

|  |  |  |
| --- | --- | --- |
| Opcode | : | 80b0 (DIRECTED_CONTROL_RELAY_RETRANSMIT_STATUS) |
| Directed_Control_Relay_Retransmit_Count | : | 03 |
| Directed_Control_Network_Transmit_Interval_Steps | : | 10 (170 ms) |
| Access message | : | 80b083 |

|  |
| --- |
| UpperTransportAccessPDU |

|  |  |  |
| --- | --- | --- |
| IVindex | : | 12345678 |
| DevKey | : | 9d6dd0e96eb25dc19a40ed9914f8f03f |
| TTL | : | 07 |
| SEQ | : | df03e0 |
| SRC | : | 0607 |
| DST | : | 0405 |
| Device nonce | : | 0200df03e00607040512345678 |
| EncAccessMessage | : | 224256 |
| TransMIC Size | : | 32 bits |
| TransMIC | : | 04b8f99c |
| UpperTransportPDU | : | 22425604b8f99c |

|  |
| --- |
| LowerTransportUnsegmentedAccessPDU |

|  |  |  |  |
| --- | --- | --- | --- |
| CTL | : | 00 | |
| TTL | : | 07 | |
| SEQ | : | df03e0 | |
| SRC | : | 0607 | |
| DST | : | 0405 | |
| SEG | : | 00 | |
| AKF | : | 00 | |
| AID | : | 00 | |
| Header | : | 00 | |
| UpperTransportPDU | : |  | 22425604b8f99c |
| LowerTransportPDU | : | 0022425604b8f99c | |

|  |
| --- |
| NetworkPDU |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVindex | : | 12345678 | | | | | | |
| NetKey | : | 7dd7364cd842ad18c17c2b820c84c3d6 | | | | | | |
| CTL | : | 00 | | | | | | |
| TTL | : | 07 | | | | | | |
| SEQ | : | df03e0 | | | | | | |
| SRC | : | 0607 | | | | | | |
| DST | : | 0405 | | | | | | |
| LowerTransportPDU | : | 0022425604b8f99c | | | | | | |
| NID | : | 68 | | | | | | |
| EncryptionKey | : | 0953fa93e7caac9638f58820220a398e | | | | | | |
| PrivacyKey | : | 8b84eedec100067d670971dd2aa700cf | | | | | | |
| Network nonce | : | 0007df03e00607000012345678 | | | | | | |
| IVI NID | : | 68 | | | | | | |
| CTL TTL | : |  | 07 | | | | | |
| SEQ | : |  |  | df03e0 | | | | |
| SRC | : |  |  |  | 0607 | | | |
| DST | : |  |  |  |  | 0405 | | |
| TransportPDU | : |  |  |  |  |  | 0022425604b8f99c | |
| NetMIC Size | : | 32 bits | | | | | | |
| EncDST || EncTransportPDU | : |  |  |  |  | b97c432aa45a59cec70d | | |
| NetMIC | : |  |  |  |  |  |  | 5e12a87e |

|  |
| --- |
| Obfuscation |

|  |  |  |
| --- | --- | --- |
| Privacy Plaintext | : | 000000000012345678b97c432aa45a59 |
| PECB | : | 88caf0f987447b883cfcac8ab6d05b2f |
| CTL||TTL||SEQ||SRC | : | 07df03e00607 |

|  |  |  |
| --- | --- | --- |
| NetworkPDU | : | 688f15f3198143b97c432aa45a59cec70d5e12a87e |

### 8.17. Provisioning sample data

The following sample data shows provisioning security functions’ computations.

#### 8.17.1. BTM_ECDH_P256_CMAC_AES128_AES_CCM algorithm

The following sample data shows a provisioning security functions computation when the Algorithm field is BTM_ECDH_P256_CMAC_AES128_AES_CCM.

|  |  |  |
| --- | --- | --- |
| ProvisioningInvite | : | 00 |
| ProvisioningCapabilities | : | 0100010000000000000000 |
| ProvisioningStart | : | 0000000000 |
| PublicKeyProvisionerX | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
| PublicKeyProvisionerY | : | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| PrivateKeyProvisioner | : | 06a516693c9aa31a6084545d0c5db641b48572b97203ddffb7ac73f7d0457663 |
| PublicKeyDeviceX | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
| PublicKeyDeviceY | : | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| PrivateKeyDevice | : | 529aa0670d72cd6497502ed473502b037e8803b5c60829a5a3caa219505530ba |
| ECDHSecret | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| ConfirmationInputs | : | 00010001000000000000000000000000002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| S1 M | : | 00010001000000000000000000000000002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| S1 ZERO | : | 00000000000000000000000000000000 |
| ConfirmationSalt | : | 5faabe187337c71cc6c973369dcaa79a |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | 5faabe187337c71cc6c973369dcaa79a |
| K1 T | : | ace84c6f002e0b4c23467e75687bae8f |
| K1 P | : | 7072636b |
| ConfirmationKey | : | e31fe046c68ec339c425fc6629f0336f |
| AuthValue | : | 00000000000000000000000000000000 |
| RandomProvisioner | : | 8b19ac31d58b124c946209b5db1021b9 |
| ConfirmationProvisionerInput | : | 8b19ac31d58b124c946209b5db1021b900000000000000000000000000000000 |
| ConfirmationProvisioner | : | b38a114dfdca1fe153bd2c1e0dc46ac2 |
| RandomDevice | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a |
| ConfirmationDeviceInput | : | 55a2a2bca04cd32ff6f346bd0a0c1a3a00000000000000000000000000000000 |
| ConfirmationDevice | : | eeba521c196b52cc2e37aa40329f554e |
| ProvisioningSaltInput | : | 5faabe187337c71cc6c973369dcaa79a8b19ac31d58b124c946209b5db1021b9 |
|  |  | 55a2a2bca04cd32ff6f346bd0a0c1a3a |
| S1 M | : | 5faabe187337c71cc6c973369dcaa79a8b19ac31d58b124c946209b5db1021b9 |
|  |  | 55a2a2bca04cd32ff6f346bd0a0c1a3a |
| S1 ZERO | : | 00000000000000000000000000000000 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | a21c7d45f201cf9489a2fb57145015b4 |
| K1 T | : | 97f950b2d08dd315f96ed3e3b7f25a90 |
| K1 P | : | 7072736b |
| SessionKey | : | c80253af86b33dfa450bbdb2a191fea3 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | a21c7d45f201cf9489a2fb57145015b4 |
| K1 T | : | 97f950b2d08dd315f96ed3e3b7f25a90 |
| K1 P | : | 7072736e |
| SessionNonceFull | : | c5e02eda7ddbe78b5f62b81d6847487e |
| SessionNonce | : | da7ddbe78b5f62b81d6847487e |
| NetworkKey | : | efb2255e6422d330088e09bb015ed707 |
| NetKeyIndex | : | 0567 |
| Flags | : | 00 |
| IVindex | : | 01020304 |
| UnicastAddress | : | 0b0c |
| Data | : | efb2255e6422d330088e09bb015ed707056700010203040b0c |
| DataEncrypted | : | d0bd7f4a89a2ff6222af59a90a60ad58acfe3123356f5cec29 |
| DataMIC | : | 73e0ec50783b10c7 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | a21c7d45f201cf9489a2fb57145015b4 |
| K1 T | : | 97f950b2d08dd315f96ed3e3b7f25a90 |
| K1 P | : | 7072646b |
| DeviceKey | : | 0520adad5e0142aa3e325087b4ec16d8 |

#### 8.17.2. BTM_ECDH_P256_HMAC_SHA256_AES_CCM algorithm

The following sample data shows a provisioning security functions computation when the Algorithm field is BTM_ECDH_P256_HMAC_SHA256_AES_CCM.

|  |  |  |
| --- | --- | --- |
| ProvisioningInvite | : | 00 |
| ProvisioningCapabilities | : | 0100030001000000000000 |
| ProvisioningStart | : | 0100010000 |
| PublicKeyProvisionerX | : | 2c31a47b5779809ef44cb5eaaf5c3e43d5f8faad4a8794cb987e9b03745c78dd |
| PublicKeyProvisionerY | : | 919512183898dfbecd52e2408e43871fd021109117bd3ed4eaf8437743715d4f |
| PrivateKeyProvisioner | : | 06a516693c9aa31a6084545d0c5db641b48572b97203ddffb7ac73f7d0457663 |
| PublicKeyDeviceX | : | f465e43ff23d3f1b9dc7dfc04da8758184dbc966204796eccf0d6cf5e16500cc |
| PublicKeyDeviceY | : | 0201d048bcbbd899eeefc424164e33c201c2b010ca6b4d43a8a155cad8ecb279 |
| PrivateKeyDevice | : | 529aa0670d72cd6497502ed473502b037e8803b5c60829a5a3caa219505530ba |
| ECDHSecret | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| ConfirmationInputs | : | 00010003000100000000000001000100002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| S2 M | : | 00010003000100000000000001000100002c31a47b5779809ef44cb5eaaf5c3e |
|  |  | 43d5f8faad4a8794cb987e9b03745c78dd919512183898dfbecd52e2408e4387 |
|  |  | 1fd021109117bd3ed4eaf8437743715d4ff465e43ff23d3f1b9dc7dfc04da875 |
|  |  | 8184dbc966204796eccf0d6cf5e16500cc0201d048bcbbd899eeefc424164e33 |
|  |  | c201c2b010ca6b4d43a8a155cad8ecb279 |
| S2 ZERO | : | 0000000000000000000000000000000000000000000000000000000000000000 |
| ConfirmationSalt | : | a71141ba8cb6b40f4f52b622e1c091614c73fc308f871b78ca775e769bc3ae69 |
| K5 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
|  |  | 906d73a3c7a7cb3ff730dca68a46b9c18d673f50e078202311473ebbe253669f |
| K5 SALT | : | a71141ba8cb6b40f4f52b622e1c091614c73fc308f871b78ca775e769bc3ae69 |
| K5 P | : | 7072636b323536 |
| K5 T | : | bb73fb226a7a26c196f3f649bf8d208eca77ae956fc31a5ab51a47267ad41815 |
| ConfirmationKey | : | 210c3c448152e8d59ef742aa7d22ee5ba59a38648bda6bf05c74f3e46fc2c0bb |
| AuthValue | : | 906d73a3c7a7cb3ff730dca68a46b9c18d673f50e078202311473ebbe253669f |
| RandomProvisioner | : | 36f968b94a13000e64b223576390db6bcc6d62f02617c369ee3f5b3e89df7e1f |
| ConfirmationProvisionerInput : | | |
| 36f968b94a13000e64b223576390db6bcc6d62f02617c369ee3f5b3e89df7e1f | | |
| ConfirmationProvisioner | : | c99b54617ae646f5f32cf7e1ea6fcc49fd69066078eba9580fa6c7031833e6c8 |
| RandomDevice | : | 5b9b1fc6a64b2de8bece53187ee989c6566db1fc7dc8580a73dafdd6211d56a5 |
| ConfirmationDeviceInput | : | 5b9b1fc6a64b2de8bece53187ee989c6566db1fc7dc8580a73dafdd6211d56a5 |
| ConfirmationDevice | : | 56e3722d291373d38c995d6f942c02928c96abb015c233557d7974b6e2df662b |
| ProvisioningSaltInput | : | a71141ba8cb6b40f4f52b622e1c091614c73fc308f871b78ca775e769bc3ae69 |
|  |  | 36f968b94a13000e64b223576390db6bcc6d62f02617c369ee3f5b3e89df7e1f |
|  |  | 5b9b1fc6a64b2de8bece53187ee989c6566db1fc7dc8580a73dafdd6211d56a5 |
| S1 M | : | a71141ba8cb6b40f4f52b622e1c091614c73fc308f871b78ca775e769bc3ae69 |
|  |  | 36f968b94a13000e64b223576390db6bcc6d62f02617c369ee3f5b3e89df7e1f |
|  |  | 5b9b1fc6a64b2de8bece53187ee989c6566db1fc7dc8580a73dafdd6211d56a5 |
| S1 ZERO | : | 00000000000000000000000000000000 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | d1cb10ad8d51286067e348fc4b692122 |
| K1 T | : | 360fab51f3d7b90c41e2abeee866e57b |
| K1 P | : | 7072736b |
| SessionKey | : | df4a494da3d45405e402f1d6a6cea338 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | d1cb10ad8d51286067e348fc4b692122 |
| K1 T | : | 360fab51f3d7b90c41e2abeee866e57b |
| K1 P | : | 7072736e |
| SessionNonceFull | : | caee0611b987db2ae41fbb9e96b80446 |
| SessionNonce | : | 11b987db2ae41fbb9e96b80446 |
| NetworkKey | : | efb2255e6422d330088e09bb015ed707 |
| NetKeyIndex | : | 0567 |
| Flags | : | 00 |
| IVindex | : | 01020304 |
| UnicastAddress | : | 0b0c |
| Data | : | efb2255e6422d330088e09bb015ed707056700010203040b0c |
| DataEncrypted | : | f9df98cbb736be1f600659ac4c37821a82db31e410a03de769 |
| DataMIC | : | 3a2a0428fbdaf321 |
| K1 N | : | ab85843a2f6d883f62e5684b38e307335fe6e1945ecd19604105c6f23221eb69 |
| K1 SALT | : | d1cb10ad8d51286067e348fc4b692122 |
| K1 T | : | 360fab51f3d7b90c41e2abeee866e57b |
| K1 P | : | 7072646b |
| DeviceKey | : | 2770852a737cf05d8813768f22af3a2d |
