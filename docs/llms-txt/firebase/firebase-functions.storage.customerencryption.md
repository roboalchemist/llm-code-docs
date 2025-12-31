# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.customerencryption.md.txt

# storage.CustomerEncryption interface

Metadata of customer-supplied encryption key, if the object is encrypted by such a key.

**Signature:**  

    export interface CustomerEncryption 

## Properties

|                                                                                        Property                                                                                        |  Type  |               Description                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------|
| [encryptionAlgorithm](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.customerencryption.md#storagecustomerencryptionencryptionalgorithm) | string | The encryption algorithm.                |
| [keySha256](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.customerencryption.md#storagecustomerencryptionkeysha256)                     | string | SHA256 hash value of the encryption key. |

## storage.CustomerEncryption.encryptionAlgorithm

The encryption algorithm.

**Signature:**  

    encryptionAlgorithm?: string;

## storage.CustomerEncryption.keySha256

SHA256 hash value of the encryption key.

**Signature:**  

    keySha256?: string;