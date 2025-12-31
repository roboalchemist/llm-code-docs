# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change.md.txt

# Firebase.Storage.MetadataChange Class Reference

# Firebase.Storage.MetadataChange

[MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) is a set of new metadata values used during object upload or when modifying the metadata of an object.

## Summary

A [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) can be created from an existing [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata) or it can be created from scratch.

| ### Constructors and Destructors ||
|---|---|
| [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a8ce00ed2180afc83f1be0466abe83a60)`()` Creates an empty set of metadata. ||
| [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1adf5e3b7fb77118009b873c4849d214df)`(`[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` original)` Used to create a modified version of the original set of metadata. ||

|                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                       ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CacheControl](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1af9cd8a2dee07a8e71e30da9eae0bb6b8)       | `string` Gets or sets the Cache Control for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).           |
| [ContentDisposition](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a2da136a160fd98c27dc015a7212f17d4) | `string` Gets or sets the content disposition for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).     |
| [ContentEncoding](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a3dc680dc77b3d5cfaf861056d9db4a24)    | `string` Gets or sets the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).        |
| [ContentLanguage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a2b88a684bb9a3562aea92687187b4075)    | `string` Gets or sets the content language for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).        |
| [ContentType](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a63f5e6d86b505005523b40ec0489829c)        | `string` Gets or sets the Content Type of this associated [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference). |
| [CustomMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change_1a802c12458359136ad1ec873e05ab9a47)     | `IDictionary< string, string >` Gets or sets custom metadata.                                                                                                                                                             |

## Properties

### CacheControl

```c#
string CacheControl
```  
Gets or sets the Cache Control for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).  

### ContentDisposition

```c#
string ContentDisposition
```  
Gets or sets the content disposition for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).  

### ContentEncoding

```c#
string ContentEncoding
```  
Gets or sets the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).  

### ContentLanguage

```c#
string ContentLanguage
```  
Gets or sets the content language for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).

This must be an ISO 639-1

two-letter language code. E.g. "zh", "es", "en".  

### ContentType

```c#
string ContentType
```  
Gets or sets the Content Type of this associated [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference).  

### CustomMetadata

```c#
IDictionary< string, string > CustomMetadata
```  
Gets or sets custom metadata.

To use this in an object initalizer, you may use the form: var change = new [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) { CustomMetadata = new Dictionary { {"customkey1", "customValue1"}, {"customkey2", "customValue2"} } }

## Public functions

### MetadataChange

```c#
 MetadataChange()
```  
Creates an empty set of metadata.  

### MetadataChange

```c#
 MetadataChange(
  StorageMetadata original
)
```  
Used to create a modified version of the original set of metadata.

<br />

|                                                              Details                                                              ||
|------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------| | `original` | The source of the metadata to build from. | |