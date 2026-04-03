# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.FullMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata.md.txt

# FullMetadata | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [storage](https://firebase.google.com/docs/reference/node/firebase.storage).
- FullMetadata

The full set of object metadata, including read-only properties.

## Index

### Properties

- [bucket](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#bucket)
- [cacheControl](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#cachecontrol)
- [contentDisposition](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentdisposition)
- [contentEncoding](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentencoding)
- [contentLanguage](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contentlanguage)
- [contentType](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#contenttype)
- [customMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#custommetadata)
- [fullPath](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#fullpath)
- [generation](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#generation)
- [md5Hash](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#md5hash)
- [metageneration](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#metageneration)
- [name](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#name)
- [size](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#size)
- [timeCreated](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#timecreated)
- [updated](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#updated)

## Properties

### bucket

bucket: string  
The bucket this object is contained in.

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

### fullPath

fullPath: string  
The full path of this object.

### generation

generation: string  
The object's generation.

see

:   <https://cloud.google.com/storage/docs/generations-preconditions>

### Optional md5Hash

md5Hash: string \| null
Inherited from [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata).[md5Hash](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata#md5hash)  
A Base64-encoded MD5 hash of the object being uploaded.

### metageneration

metageneration: string  
The object's metageneration.

see

:   <https://cloud.google.com/storage/docs/generations-preconditions>

### name

name: string  
The short name of this object, which is the last component of the full path.
For example, if fullPath is 'full/path/image.png', name is 'image.png'.

### size

size: number  
The size of this object, in bytes.

### timeCreated

timeCreated: string  
A date string representing when this object was created.

### updated

updated: string  
A date string representing when this object was last updated.