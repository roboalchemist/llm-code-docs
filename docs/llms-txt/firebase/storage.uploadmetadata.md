# Source: https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md.txt

# UploadMetadata interface

Object metadata that can be set at upload.

**Signature:**  

    export interface UploadMetadata extends SettableMetadata 

**Extends:** [SettableMetadata](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadata_interface)

## Properties

|                                                 Property                                                 |        Type         |                       Description                       |
|----------------------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------|
| [md5Hash](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadatamd5hash) | string \| undefined | A Base64-encoded MD5 hash of the object being uploaded. |

## UploadMetadata.md5Hash

A Base64-encoded MD5 hash of the object being uploaded.

**Signature:**  

    md5Hash?: string | undefined;