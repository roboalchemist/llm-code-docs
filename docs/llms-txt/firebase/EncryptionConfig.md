# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig.md.txt

Encryption configuration for a new database being created from another source.

The source could be a[Backup](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups#Backup)or a[PitrSnapshot](https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/CloneDatabaseMetadata#PitrSnapshot).

|                                                                                                                                                                                                                                                                                             JSON representation                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `encryption_type` can be only one of the following: "googleDefaultEncryption": { object (https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#GoogleDefaultEncryptionOptions) }, "useSourceEncryption": { object (https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#SourceEncryptionOptions) }, "customerManagedEncryption": { object (https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#CustomerManagedEncryptionOptions) } // End of list of possible types for union field `encryption_type`. } ``` |

|                                                                                                                          Fields                                                                                                                          ||
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field`encryption_type`. The method for encrypting the database.`encryption_type`can be only one of the following:                                                                                                                                  ||
| `googleDefaultEncryption`   | `object (`[GoogleDefaultEncryptionOptions](https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#GoogleDefaultEncryptionOptions)`)` Use Google default encryption.                                  |
| `useSourceEncryption`       | `object (`[SourceEncryptionOptions](https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#SourceEncryptionOptions)`)` The database will use the same encryption configuration as the source.        |
| `customerManagedEncryption` | `object (`[CustomerManagedEncryptionOptions](https://firebase.google.com/docs/firestore/reference/rest/v1/EncryptionConfig#CustomerManagedEncryptionOptions)`)` Use Customer Managed Encryption Keys (CMEK) for encryption. |

## GoogleDefaultEncryptionOptions

This type has no fields.
The configuration options for using Google default encryption.

## SourceEncryptionOptions

This type has no fields.
The configuration options for using the same encryption method as the source.

## CustomerManagedEncryptionOptions

The configuration options for using CMEK (Customer Managed Encryption Key) encryption.

|       JSON representation        |
|----------------------------------|
| ``` { "kmsKeyName": string } ``` |

|                                                                                                                                                                                                                               Fields                                                                                                                                                                                                                                ||
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kmsKeyName` | `string` Required. Only keys in the same location as the database are allowed to be used for encryption. For Firestore's nam5 multi-region, this corresponds to Cloud KMS multi-region us. For Firestore's eur3 multi-region, this corresponds to Cloud KMS multi-region europe. See<https://cloud.google.com/kms/docs/locations>. The expected format is`projects/{projectId}/locations/{kms_location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. |