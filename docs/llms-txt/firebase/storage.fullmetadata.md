# Source: https://firebase.google.com/docs/reference/js/storage.fullmetadata.md.txt

# FullMetadata interface

The full set of object metadata, including read-only properties.

**Signature:**  

    export interface FullMetadata extends UploadMetadata 

**Extends:** [UploadMetadata](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadata_interface)

## Properties

|                                                      Property                                                      |                                                                 Type                                                                  |                                                                     Description                                                                      |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bucket](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatabucket)                 | string                                                                                                                                | The bucket this object is contained in.                                                                                                              |
| [downloadTokens](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatadownloadtokens) | string\[\] \| undefined                                                                                                               | Tokens to allow access to the download URL.                                                                                                          |
| [fullPath](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatafullpath)             | string                                                                                                                                | The full path of this object.                                                                                                                        |
| [generation](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatageneration)         | string                                                                                                                                | The object's generation. <https://cloud.google.com/storage/docs/metadata#generation-number>                                                          |
| [metageneration](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatametageneration) | string                                                                                                                                | The object's metageneration. <https://cloud.google.com/storage/docs/metadata#generation-number>                                                      |
| [name](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadataname)                     | string                                                                                                                                | The short name of this object, which is the last component of the full path. For example, if fullPath is 'full/path/image.png', name is 'image.png'. |
| [ref](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadataref)                       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) \| undefined | `StorageReference` associated with this upload.                                                                                                      |
| [size](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatasize)                     | number                                                                                                                                | The size of this object, in bytes.                                                                                                                   |
| [timeCreated](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadatatimecreated)       | string                                                                                                                                | A date string representing when this object was created.                                                                                             |
| [updated](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadataupdated)               | string                                                                                                                                | A date string representing when this object was last updated.                                                                                        |

## FullMetadata.bucket

The bucket this object is contained in.

**Signature:**  

    bucket: string;

## FullMetadata.downloadTokens

Tokens to allow access to the download URL.

**Signature:**  

    downloadTokens: string[] | undefined;

## FullMetadata.fullPath

The full path of this object.

**Signature:**  

    fullPath: string;

## FullMetadata.generation

The object's generation. <https://cloud.google.com/storage/docs/metadata#generation-number>

**Signature:**  

    generation: string;

## FullMetadata.metageneration

The object's metageneration. <https://cloud.google.com/storage/docs/metadata#generation-number>

**Signature:**  

    metageneration: string;

## FullMetadata.name

The short name of this object, which is the last component of the full path. For example, if fullPath is 'full/path/image.png', name is 'image.png'.

**Signature:**  

    name: string;

## FullMetadata.ref

`StorageReference` associated with this upload.

**Signature:**  

    ref?: StorageReference | undefined;

## FullMetadata.size

The size of this object, in bytes.

**Signature:**  

    size: number;

## FullMetadata.timeCreated

A date string representing when this object was created.

**Signature:**  

    timeCreated: string;

## FullMetadata.updated

A date string representing when this object was last updated.

**Signature:**  

    updated: string;