# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.Reference.md.txt

# Reference | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [storage](https://firebase.google.com/docs/reference/node/firebase.storage).
- Reference

Represents a reference to a Google Cloud Storage object. Developers can
upload, download, and delete objects, as well as get/set object metadata.

## Index

### Properties

- [bucket](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#bucket)
- [fullPath](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#fullpath)
- [name](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#name)
- [parent](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#parent)
- [root](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#root)
- [storage](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#storage)

### Methods

- [child](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#child)
- [delete](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#delete)
- [getDownloadURL](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#getdownloadurl)
- [getMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#getmetadata)
- [list](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#list)
- [listAll](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#listall)
- [put](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#put)
- [putString](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#putstring)
- [toString](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#tostring)
- [updateMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.Reference#updatemetadata)

## Properties

### bucket

bucket: string  
The name of the bucket containing this reference's object.

### fullPath

fullPath: string  
The full path of this object.

### name

name: string  
The short name of this object, which is the last component of the full path.
For example, if fullPath is 'full/path/image.png', name is 'image.png'.

### parent

parent: [Reference](https://firebase.google.com/docs/reference/node/firebase.storage.Reference) \| null  
A reference pointing to the parent location of this reference, or null if
this reference is the root.

### root

root: [Reference](https://firebase.google.com/docs/reference/node/firebase.storage.Reference)  
A reference to the root of this reference's bucket.

### storage

storage: [Storage](https://firebase.google.com/docs/reference/node/firebase.storage.Storage)  
The storage service associated with this reference.

## Methods

### child

- child ( path : string ) : [Reference](https://firebase.google.com/docs/reference/node/firebase.storage.Reference)
- Returns a reference to a relative path from this reference.

  #### Parameters

  -

    ##### path: string

    The relative path from this reference.
    Leading, trailing, and consecutive slashes are removed.

  #### Returns [Reference](https://firebase.google.com/docs/reference/node/firebase.storage.Reference)

  The reference to the given path.

### delete

- delete ( ) : Promise \< void \>
- Deletes the object at this reference's location.

  #### Returns Promise\<void\>

  A Promise that resolves if the deletion
  succeeded and rejects if it failed, including if the object didn't exist.

### getDownloadURL

- getDownloadURL ( ) : Promise \< string \>
- Fetches a long lived download URL for this object.

  #### Returns Promise\<string\>

  A Promise that resolves with the download
  URL or rejects if the fetch failed, including if the object did not
  exist.

### getMetadata

- getMetadata ( ) : Promise \< [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata) \>
- Fetches metadata for the object at this location, if one exists.

  #### Returns Promise\<[FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata)\>

  A Promise that
  resolves with the metadata, or rejects if the fetch failed, including if
  the object did not exist.

### list

- list ( options ? : [ListOptions](https://firebase.google.com/docs/reference/node/firebase.storage.ListOptions) ) : Promise \< [ListResult](https://firebase.google.com/docs/reference/node/firebase.storage.ListResult) \>
- List items (files) and prefixes (folders) under this storage reference.

  List API is only available for Firebase Rules Version 2.

  GCS is a key-blob store. Firebase Storage imposes the semantic of '/'
  delimited folder structure.
  Refer to GCS's List API if you want to learn more.

  To adhere to Firebase Rules's Semantics, Firebase Storage does not
  support objects whose paths end with "/" or contain two consecutive
  "/"s. Firebase Storage List API will filter these unsupported objects.
  `list()` may fail if there are too many unsupported objects in the bucket.

  #### Parameters

  -

    ##### Optional options: [ListOptions](https://firebase.google.com/docs/reference/node/firebase.storage.ListOptions)

    See `ListOptions` for details.

  #### Returns Promise\<[ListResult](https://firebase.google.com/docs/reference/node/firebase.storage.ListResult)\>

  A Promise that resolves with the items and prefixes.
  `prefixes` contains references to sub-folders and `items`
  contains references to objects in this folder. `nextPageToken`
  can be used to get the rest of the results.

### listAll

- listAll ( ) : Promise \< [ListResult](https://firebase.google.com/docs/reference/node/firebase.storage.ListResult) \>
- List all items (files) and prefixes (folders) under this storage reference.

  This is a helper method for calling `list()` repeatedly until there are
  no more results. The default pagination size is 1000.

  Note: The results may not be consistent if objects are changed while this
  operation is running.

  Warning: `listAll` may potentially consume too many resources if there are
  too many results.

  #### Returns Promise\<[ListResult](https://firebase.google.com/docs/reference/node/firebase.storage.ListResult)\>

  A Promise that resolves with all the items and prefixes under
  the current storage reference. `prefixes` contains references to
  sub-directories and `items` contains references to objects in this
  folder. `nextPageToken` is never returned.

### put

- put ( data : Blob \| Uint8Array \| ArrayBuffer , metadata ? : [UploadMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata) ) : firebase.storage.UploadTask
- Uploads data to this reference's location.

  #### Parameters

  -

    ##### data: Blob \| Uint8Array \| ArrayBuffer

    The data to upload.
  -

    ##### Optional metadata: [UploadMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata)

    Metadata for the newly
    uploaded object.

  #### Returns firebase.storage.UploadTask

  An object that can be used to monitor
  and manage the upload.

### putString

- putString ( data : string , format ? : [StringFormat](https://firebase.google.com/docs/reference/node/firebase.storage#stringformat) , metadata ? : [UploadMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata) ) : firebase.storage.UploadTask
- Uploads string data to this reference's location.

  throws

  :   If the format is not an allowed format, or if the given string
      doesn't conform to the specified format.

  #### Parameters

  -

    ##### data: string

    The string to upload.
  -

    ##### Optional format: [StringFormat](https://firebase.google.com/docs/reference/node/firebase.storage#stringformat)

    The format of the string to
    upload.
  -

    ##### Optional metadata: [UploadMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.UploadMetadata)

    Metadata for the newly
    uploaded object.

  #### Returns firebase.storage.UploadTask

### toString

- toString ( ) : string
- Returns a gs:// URL for this object in the form
  `gs://<bucket>/<path>/<to>/<object>`

  #### Returns string

  The gs:// URL.

### updateMetadata

- updateMetadata ( metadata : [SettableMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.SettableMetadata) ) : Promise \< [FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata) \>
- Updates the metadata for the object at this location, if one exists.

  #### Parameters

  -

    ##### metadata: [SettableMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.SettableMetadata)

    The new metadata.
    Setting a property to 'null' removes it on the server, while leaving
    a property as 'undefined' has no effect.

  #### Returns Promise\<[FullMetadata](https://firebase.google.com/docs/reference/node/firebase.storage.FullMetadata)\>

  A Promise that
  resolves with the full updated metadata or rejects if the updated failed,
including if the object did not exist.