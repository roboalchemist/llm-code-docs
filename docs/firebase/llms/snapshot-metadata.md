# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata.md.txt

# Firebase.Firestore.SnapshotMetadata Class Reference

# Firebase.Firestore.SnapshotMetadata

Metadata about a snapshot, describing the state of the snapshot.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [SnapshotMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1ac77d05832cdc11ea503c5a709f8b7f4d)`(bool hasPendingWrites, bool isFromCache)` Creates a new instance of the class. ||

|                                                                                                                                                  ### Properties                                                                                                                                                  ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [HasPendingWrites](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1ad82a4beede53aa1cdb4ca4d522406527) | `bool` `true` if the snapshot contains the result of local writes (e.g.                                   |
| [IsFromCache](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1a71762ba2d51746a0285af93a1a1dcf44)      | `bool` `true` if the snapshot was created from cached data rather than guaranteed up-to-date server data. |

|                                                                                                                                                                                                             ### Public functions                                                                                                                                                                                                             ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1adbcb3ccd1f2fbdaa508234964c8c2307)`(object obj)`                                                                                                                                                                 | `override bool`                                                   |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1a602485aba60748fc9977b5d398082d13)`(`[SnapshotMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata)` other)` | `bool` Compares this snapshot metadata with another for equality. |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata_1a7be3512a85742371ff57611327bd3f33)`()`                                                                                                                                                                      | `override int`                                                    |

## Properties

### HasPendingWrites

```c#
bool HasPendingWrites
```  
`true` if the snapshot contains the result of local writes (e.g.

`SetAsync` or `UpdateAsync` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via `MetadataChanges.Include`) you will receive another snapshot with `HasPendingWrites` equal to `false` once the writes have been committed to the backend.  

### IsFromCache

```c#
bool IsFromCache
```  
`true` if the snapshot was created from cached data rather than guaranteed up-to-date server data.

If your listener has opted into metadata updates (via `MetadataChanges.Include`) you will receive another snapshot with `IsFromCache` equal to `false` once the client has received up-to-date data from the backend.

## Public functions

### Equals

```c#
override bool Equals(
  object obj
)
```  

### Equals

```c#
bool Equals(
  SnapshotMetadata other
)
```  
Compares this snapshot metadata with another for equality.

<br />

|                                                                 Details                                                                  ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-------------------------------------------------| | `other` | The snapshot metadata to compare this one with. | |
| **Returns** | `true` if this snapshot metadata is equal to *other* ; `false` otherwise.                                                   |

### GetHashCode

```c#
override int GetHashCode()
```  

### SnapshotMetadata

```c#
 SnapshotMetadata(
  bool hasPendingWrites,
  bool isFromCache
)
```  
Creates a new instance of the class.

<br />

|                                                                                                                      Details                                                                                                                       ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|-----------------------------------------------------| | `hasPendingWrites` | Indicates whether this snapshot has pending writes. | | `isFromCache`      | Indicates whether this snapshot is from the cache.  | |