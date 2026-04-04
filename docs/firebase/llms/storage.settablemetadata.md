# Source: https://firebase.google.com/docs/reference/js/storage.settablemetadata.md.txt

# SettableMetadata interface

Object metadata that can be set at any time.

**Signature:**  

    export interface SettableMetadata 

## Properties

|                                                              Property                                                              |                   Type                    |                          Description                           |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------------------------------|
| [cacheControl](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacachecontrol)             | string \| undefined                       | Served as the 'Cache-Control' header on object download.       |
| [contentDisposition](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacontentdisposition) | string \| undefined                       | Served as the 'Content-Disposition' header on object download. |
| [contentEncoding](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacontentencoding)       | string \| undefined                       | Served as the 'Content-Encoding' header on object download.    |
| [contentLanguage](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacontentlanguage)       | string \| undefined                       | Served as the 'Content-Language' header on object download.    |
| [contentType](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacontenttype)               | string \| undefined                       | Served as the 'Content-Type' header on object download.        |
| [customMetadata](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadatacustommetadata)         | { \[key: string\]: string; } \| undefined | Additional user-defined custom metadata.                       |

## SettableMetadata.cacheControl

Served as the 'Cache-Control' header on object download.

**Signature:**  

    cacheControl?: string | undefined;

## SettableMetadata.contentDisposition

Served as the 'Content-Disposition' header on object download.

**Signature:**  

    contentDisposition?: string | undefined;

## SettableMetadata.contentEncoding

Served as the 'Content-Encoding' header on object download.

**Signature:**  

    contentEncoding?: string | undefined;

## SettableMetadata.contentLanguage

Served as the 'Content-Language' header on object download.

**Signature:**  

    contentLanguage?: string | undefined;

## SettableMetadata.contentType

Served as the 'Content-Type' header on object download.

**Signature:**  

    contentType?: string | undefined;

## SettableMetadata.customMetadata

Additional user-defined custom metadata.

**Signature:**  

    customMetadata?: {
            [key: string]: string;
        } | undefined;