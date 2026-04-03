# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata.md.txt

# UploadMetadata | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [storage](https://firebase.google.com/docs/reference/node/firebase.storage).
- UploadMetadata

Object metadata that can be set at upload.

## Index

### Properties

- [cacheControl](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#cachecontrol)
- [contentDisposition](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#contentdisposition)
- [contentEncoding](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#contentencoding)
- [contentLanguage](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#contentlanguage)
- [contentType](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#contenttype)
- [customMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#custommetadata)
- [md5Hash](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata#md5hash)

## Properties

### Optional cacheControl

cacheControl: string \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[cacheControl](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#cachecontrol)  
Served as the 'Cache-Control' header on object download.

### Optional contentDisposition

contentDisposition: string \| null
| Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[contentDisposition](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentdisposition)

### Optional contentEncoding

contentEncoding: string \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[contentEncoding](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentencoding)  
Served as the 'Content-Encoding' header on object download.

### Optional contentLanguage

contentLanguage: string \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[contentLanguage](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentlanguage)  
Served as the 'Content-Language' header on object download.

### Optional contentType

contentType: string \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[contentType](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contenttype)  
Served as the 'Content-Type' header on object download.

### Optional customMetadata

customMetadata: {} \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[customMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#custommetadata)  
Additional user-defined custom metadata.

### Optional md5Hash

md5Hash: string \| null  
A Base64-encoded MD5 hash of the object being uploaded.