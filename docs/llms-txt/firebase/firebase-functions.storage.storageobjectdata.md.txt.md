# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md.txt

# storage.StorageObjectData interface

An object within Google Cloud Storage. Ref: https://github.com/googleapis/google-cloudevents-nodejs/blob/main/cloud/storage/v1/StorageObjectData.ts

**Signature:**

    export interface StorageObjectData 

## Properties

| Property | Type | Description |
|---|---|---|
| [bucket](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatabucket) | string | The name of the bucket containing this object. |
| [cacheControl](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacachecontrol) | string | Cache-Control directive for the object data, matching \[https://tools.ietf.org/html/rfc7234#section-5.2"\]\[RFC 7234 §5.2\]. |
| [componentCount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacomponentcount) | number | Number of underlying components that make up this object. Components are accumulated by compose operations. Attempting to set this field will result in an error. |
| [contentDisposition](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacontentdisposition) | string | Content-Disposition of the object data, matching \[https://tools.ietf.org/html/rfc6266\]\[RFC 6266\]. |
| [contentEncoding](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacontentencoding) | string | Content-Encoding of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.2.2\]\[RFC 7231 §3.1.2.2\] |
| [contentLanguage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacontentlanguage) | string | Content-Language of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.3.2\]\[RFC 7231 §3.1.3.2\]. |
| [contentType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacontenttype) | string | Content-Type of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.1.5\]\[RFC 7231 §3.1.1.5\]. If an object is stored without a Content-Type, it is served as `application/octet-stream`. |
| [crc32c](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacrc32c) | string | CRC32c checksum. For more information about using the CRC32c checksum, see \[https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI\]\[Hashes and ETags: Best Practices\]. |
| [customerEncryption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatacustomerencryption) | [CustomerEncryption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.customerencryption.md#storagecustomerencryption_interface) | Metadata of customer-supplied encryption key, if the object is encrypted by such a key. |
| [etag](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdataetag) | string | HTTP 1.1 Entity tag for the object. See \[https://tools.ietf.org/html/rfc7232#section-2.3\]\[RFC 7232 §2.3\]. |
| [generation](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatageneration) | number | The content generation of this object. Used for object versioning. Attempting to set this field will result in an error. |
| [id](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdataid) | string | The ID of the object, including the bucket name, object name, and generation number. |
| [kind](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatakind) | string | The kind of item this is. For objects, this is always "storage#object". |
| [md5Hash](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatamd5hash) | string | MD5 hash of the data; encoded using base64 as per \[https://tools.ietf.org/html/rfc4648#section-4\]\[RFC 4648 §4\]. For more information about using the MD5 hash, see \[https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI\]\[Hashes and ETags: Best Practices\]. |
| [mediaLink](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatamedialink) | string | Media download link. |
| [metadata](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatametadata) | { \[key: string\]: string; } | User-provided metadata, in key/value pairs. |
| [metageneration](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatametageneration) | number | The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. |
| [name](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdataname) | string | The name of the object. |
| [selfLink](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdataselflink) | string | The link to this object. |
| [size](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatasize) | number | Content-Length of the object data in bytes, matching \[https://tools.ietf.org/html/rfc7230#section-3.3.2\]\[RFC 7230 §3.3.2\]. |
| [storageClass](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatastorageclass) | string | Storage class of the object. |
| [timeCreated](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatatimecreated) | Date \| string | The creation time of the object. Attempting to set this field will result in an error. |
| [timeDeleted](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatatimedeleted) | Date \| string | The deletion time of the object. Will be returned if and only if this version of the object has been deleted. |
| [timeStorageClassUpdated](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdatatimestorageclassupdated) | Date \| string | The time at which the object's storage class was last changed. |
| [updated](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdataupdated) | Date \| string | The modification time of the object metadata. |

## storage.StorageObjectData.bucket

The name of the bucket containing this object.

**Signature:**

    bucket: string;

## storage.StorageObjectData.cacheControl

Cache-Control directive for the object data, matching \[https://tools.ietf.org/html/rfc7234#section-5.2"\]\[RFC 7234 §5.2\].

**Signature:**

    cacheControl?: string;

## storage.StorageObjectData.componentCount

Number of underlying components that make up this object. Components are accumulated by compose operations. Attempting to set this field will result in an error.

**Signature:**

    componentCount?: number;

## storage.StorageObjectData.contentDisposition

Content-Disposition of the object data, matching \[https://tools.ietf.org/html/rfc6266\]\[RFC 6266\].

**Signature:**

    contentDisposition?: string;

## storage.StorageObjectData.contentEncoding

Content-Encoding of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.2.2\]\[RFC 7231 §3.1.2.2\]

**Signature:**

    contentEncoding?: string;

## storage.StorageObjectData.contentLanguage

Content-Language of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.3.2\]\[RFC 7231 §3.1.3.2\].

**Signature:**

    contentLanguage?: string;

## storage.StorageObjectData.contentType

Content-Type of the object data, matching \[https://tools.ietf.org/html/rfc7231#section-3.1.1.5\]\[RFC 7231 §3.1.1.5\]. If an object is stored without a Content-Type, it is served as `application/octet-stream`.

**Signature:**

    contentType?: string;

## storage.StorageObjectData.crc32c

CRC32c checksum. For more information about using the CRC32c checksum, see \[https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI\]\[Hashes and ETags: Best Practices\].

**Signature:**

    crc32c?: string;

## storage.StorageObjectData.customerEncryption

Metadata of customer-supplied encryption key, if the object is encrypted by such a key.

**Signature:**

    customerEncryption?: CustomerEncryption;

## storage.StorageObjectData.etag

HTTP 1.1 Entity tag for the object. See \[https://tools.ietf.org/html/rfc7232#section-2.3\]\[RFC 7232 §2.3\].

**Signature:**

    etag?: string;

## storage.StorageObjectData.generation

The content generation of this object. Used for object versioning. Attempting to set this field will result in an error.

**Signature:**

    generation: number;

## storage.StorageObjectData.id

The ID of the object, including the bucket name, object name, and generation number.

**Signature:**

    id: string;

## storage.StorageObjectData.kind

The kind of item this is. For objects, this is always "storage#object".

**Signature:**

    kind?: string;

## storage.StorageObjectData.md5Hash

MD5 hash of the data; encoded using base64 as per \[https://tools.ietf.org/html/rfc4648#section-4\]\[RFC 4648 §4\]. For more information about using the MD5 hash, see \[https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI\]\[Hashes and ETags: Best Practices\].

**Signature:**

    md5Hash?: string;

## storage.StorageObjectData.mediaLink

Media download link.

**Signature:**

    mediaLink?: string;

## storage.StorageObjectData.metadata

User-provided metadata, in key/value pairs.

**Signature:**

    metadata?: {
            [key: string]: string;
        };

## storage.StorageObjectData.metageneration

The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object.

**Signature:**

    metageneration: number;

## storage.StorageObjectData.name

The name of the object.

**Signature:**

    name: string;

## storage.StorageObjectData.selfLink

The link to this object.

**Signature:**

    selfLink?: string;

## storage.StorageObjectData.size

Content-Length of the object data in bytes, matching \[https://tools.ietf.org/html/rfc7230#section-3.3.2\]\[RFC 7230 §3.3.2\].

**Signature:**

    size: number;

## storage.StorageObjectData.storageClass

Storage class of the object.

**Signature:**

    storageClass: string;

## storage.StorageObjectData.timeCreated

The creation time of the object. Attempting to set this field will result in an error.

**Signature:**

    timeCreated?: Date | string;

## storage.StorageObjectData.timeDeleted

The deletion time of the object. Will be returned if and only if this version of the object has been deleted.

**Signature:**

    timeDeleted?: Date | string;

## storage.StorageObjectData.timeStorageClassUpdated

The time at which the object's storage class was last changed.

**Signature:**

    timeStorageClassUpdated?: Date | string;

## storage.StorageObjectData.updated

The modification time of the object metadata.

**Signature:**

    updated?: Date | string;