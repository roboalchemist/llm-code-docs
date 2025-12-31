# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md.txt

# storage.ObjectMetadata interface

Interface representing a Google Google Cloud Storage object metadata object.

**Signature:**  

    export interface ObjectMetadata 

## Properties

|                                                                                 Property                                                                                  |                                                                                                                                     Type                                                                                                                                     |                                                                                                                                                                                                                               Description                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [acl](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataacl)                                         | \[ { kind?: string; id?: string; selfLink?: string; bucket?: string; object?: string; generation?: string; entity?: string; role?: string; email?: string; entityId?: string; domain?: string; projectTeam?: { projectNumber?: string; team?: string; }; etag?: string; } \] |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [bucket](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatabucket)                                   | string                                                                                                                                                                                                                                                                       | Storage bucket that contains the object.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [cacheControl](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacachecontrol)                       | string                                                                                                                                                                                                                                                                       | The value of the `Cache-Control` header, used to determine whether Internet caches are allowed to cache public data for an object.                                                                                                                                                                                                                                                                                                                                       |
| [componentCount](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacomponentcount)                   | string                                                                                                                                                                                                                                                                       | Specifies the number of originally uploaded objects from which a composite object was created.                                                                                                                                                                                                                                                                                                                                                                           |
| [contentDisposition](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacontentdisposition)           | string                                                                                                                                                                                                                                                                       | The value of the `Content-Disposition` header, used to specify presentation information about the data being transmitted.                                                                                                                                                                                                                                                                                                                                                |
| [contentEncoding](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacontentencoding)                 | string                                                                                                                                                                                                                                                                       | Content-Encoding to indicate that an object is compressed (for example, with gzip compression) while maintaining its Content-Type.                                                                                                                                                                                                                                                                                                                                       |
| [contentLanguage](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacontentlanguage)                 | string                                                                                                                                                                                                                                                                       | ISO 639-1 language code of the content.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [contentType](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacontenttype)                         | string                                                                                                                                                                                                                                                                       | The object's content type, also known as the MIME type.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [crc32c](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacrc32c)                                   | string                                                                                                                                                                                                                                                                       | The object's CRC32C hash. All Google Cloud Storage objects have a CRC32C hash or MD5 hash.                                                                                                                                                                                                                                                                                                                                                                               |
| [customerEncryption](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatacustomerencryption)           | { encryptionAlgorithm?: string; keySha256?: string; }                                                                                                                                                                                                                        | Customer-supplied encryption key.This object contains the following properties: \* `encryptionAlgorithm` (`string|undefined`): The encryption algorithm that was used. Always contains the value `AES256`. \* `keySha256` (`string|undefined`): An RFC 4648 base64-encoded string of the SHA256 hash of your encryption key. You can use this SHA256 hash to uniquely identify the AES-256 encryption key required to decrypt the object, which you must store securely. |
| [etag](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataetag)                                       | string                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [generation](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatageneration)                           | string                                                                                                                                                                                                                                                                       | Generation version number that changes each time the object is overwritten.                                                                                                                                                                                                                                                                                                                                                                                              |
| [id](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataid)                                           | string                                                                                                                                                                                                                                                                       | The ID of the object, including the bucket name, object name, and generation number.                                                                                                                                                                                                                                                                                                                                                                                     |
| [kind](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatakind)                                       | string                                                                                                                                                                                                                                                                       | The kind of the object, which is always `storage#object`.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [md5Hash](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatamd5hash)                                 | string                                                                                                                                                                                                                                                                       | MD5 hash for the object. All Google Cloud Storage objects have a CRC32C hash or MD5 hash.                                                                                                                                                                                                                                                                                                                                                                                |
| [mediaLink](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatamedialink)                             | string                                                                                                                                                                                                                                                                       | Media download link.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [metadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatametadata)                               | { \[key: string\]: string; }                                                                                                                                                                                                                                                 | User-provided metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [metageneration](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatametageneration)                   | string                                                                                                                                                                                                                                                                       | Meta-generation version number that changes each time the object's metadata is updated.                                                                                                                                                                                                                                                                                                                                                                                  |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataname)                                       | string                                                                                                                                                                                                                                                                       | The object's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [owner](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataowner)                                     | { entity?: string; entityId?: string; }                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [selfLink](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataselflink)                               | string                                                                                                                                                                                                                                                                       | Link to access the object, assuming you have sufficient permissions.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [size](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatasize)                                       | string                                                                                                                                                                                                                                                                       | The value of the `Content-Length` header, used to determine the length of the object data in bytes.                                                                                                                                                                                                                                                                                                                                                                      |
| [storageClass](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatastorageclass)                       | string                                                                                                                                                                                                                                                                       | Storage class of the object.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [timeCreated](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatatimecreated)                         | string                                                                                                                                                                                                                                                                       | The creation time of the object in RFC 3339 format.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [timeDeleted](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatatimedeleted)                         | string                                                                                                                                                                                                                                                                       | The deletion time of the object in RFC 3339 format. Returned only if this version of the object has been deleted.                                                                                                                                                                                                                                                                                                                                                        |
| [timeStorageClassUpdated](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadatatimestorageclassupdated) | string                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [updated](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadataupdated)                                 | string                                                                                                                                                                                                                                                                       | The modification time of the object metadata in RFC 3339 format.                                                                                                                                                                                                                                                                                                                                                                                                         |

## storage.ObjectMetadata.acl

**Signature:**  

    acl?: [
            {
                kind?: string;
                id?: string;
                selfLink?: string;
                bucket?: string;
                object?: string;
                generation?: string;
                entity?: string;
                role?: string;
                email?: string;
                entityId?: string;
                domain?: string;
                projectTeam?: {
                    projectNumber?: string;
                    team?: string;
                };
                etag?: string;
            }
        ];

## storage.ObjectMetadata.bucket

Storage bucket that contains the object.

**Signature:**  

    bucket: string;

## storage.ObjectMetadata.cacheControl

The value of the `Cache-Control` header, used to determine whether Internet caches are allowed to cache public data for an object.

**Signature:**  

    cacheControl?: string;

## storage.ObjectMetadata.componentCount

Specifies the number of originally uploaded objects from which a composite object was created.

**Signature:**  

    componentCount?: string;

## storage.ObjectMetadata.contentDisposition

The value of the `Content-Disposition` header, used to specify presentation information about the data being transmitted.

**Signature:**  

    contentDisposition?: string;

## storage.ObjectMetadata.contentEncoding

Content-Encoding to indicate that an object is compressed (for example, with gzip compression) while maintaining its Content-Type.

**Signature:**  

    contentEncoding?: string;

## storage.ObjectMetadata.contentLanguage

ISO 639-1 language code of the content.

**Signature:**  

    contentLanguage?: string;

## storage.ObjectMetadata.contentType

The object's content type, also known as the MIME type.

**Signature:**  

    contentType?: string;

## storage.ObjectMetadata.crc32c

The object's CRC32C hash. All Google Cloud Storage objects have a CRC32C hash or MD5 hash.

**Signature:**  

    crc32c?: string;

## storage.ObjectMetadata.customerEncryption

Customer-supplied encryption key.

This object contains the following properties: \* `encryptionAlgorithm` (`string|undefined`): The encryption algorithm that was used. Always contains the value `AES256`. \* `keySha256` (`string|undefined`): An RFC 4648 base64-encoded string of the SHA256 hash of your encryption key. You can use this SHA256 hash to uniquely identify the AES-256 encryption key required to decrypt the object, which you must store securely.

**Signature:**  

    customerEncryption?: {
            encryptionAlgorithm?: string;
            keySha256?: string;
        };

## storage.ObjectMetadata.etag

**Signature:**  

    etag?: string;

## storage.ObjectMetadata.generation

Generation version number that changes each time the object is overwritten.

**Signature:**  

    generation?: string;

## storage.ObjectMetadata.id

The ID of the object, including the bucket name, object name, and generation number.

**Signature:**  

    id: string;

## storage.ObjectMetadata.kind

The kind of the object, which is always `storage#object`.

**Signature:**  

    kind: string;

## storage.ObjectMetadata.md5Hash

MD5 hash for the object. All Google Cloud Storage objects have a CRC32C hash or MD5 hash.

**Signature:**  

    md5Hash?: string;

## storage.ObjectMetadata.mediaLink

Media download link.

**Signature:**  

    mediaLink?: string;

## storage.ObjectMetadata.metadata

User-provided metadata.

**Signature:**  

    metadata?: {
            [key: string]: string;
        };

## storage.ObjectMetadata.metageneration

Meta-generation version number that changes each time the object's metadata is updated.

**Signature:**  

    metageneration?: string;

## storage.ObjectMetadata.name

The object's name.

**Signature:**  

    name?: string;

## storage.ObjectMetadata.owner

**Signature:**  

    owner?: {
            entity?: string;
            entityId?: string;
        };

## storage.ObjectMetadata.selfLink

Link to access the object, assuming you have sufficient permissions.

**Signature:**  

    selfLink?: string;

## storage.ObjectMetadata.size

The value of the `Content-Length` header, used to determine the length of the object data in bytes.

**Signature:**  

    size: string;

## storage.ObjectMetadata.storageClass

Storage class of the object.

**Signature:**  

    storageClass: string;

## storage.ObjectMetadata.timeCreated

The creation time of the object in RFC 3339 format.

**Signature:**  

    timeCreated: string;

## storage.ObjectMetadata.timeDeleted

The deletion time of the object in RFC 3339 format. Returned only if this version of the object has been deleted.

**Signature:**  

    timeDeleted?: string;

## storage.ObjectMetadata.timeStorageClassUpdated

**Signature:**  

    timeStorageClassUpdated?: string;

## storage.ObjectMetadata.updated

The modification time of the object metadata in RFC 3339 format.

**Signature:**  

    updated: string;