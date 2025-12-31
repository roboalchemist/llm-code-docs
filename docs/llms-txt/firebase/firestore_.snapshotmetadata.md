# Source: https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md.txt

# SnapshotMetadata class

Metadata about a snapshot, describing the state of the snapshot.

**Signature:**  

    export declare class SnapshotMetadata 

## Properties

|                                                             Property                                                              | Modifiers |  Type   |                                                                                                                                                                           Description                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromCache](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadatafromcache)               |           | boolean | True if the snapshot was created from cached data rather than guaranteed up-to-date server data. If your listener has opted into metadata updates (via `SnapshotListenOptions`) you will receive another snapshot with `fromCache` set to false once the client has received up-to-date data from the backend.                                                  |
| [hasPendingWrites](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadatahaspendingwrites) |           | boolean | True if the snapshot contains the result of local writes (for example `set()` or `update()` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via `SnapshotListenOptions`) you will receive another snapshot with `hasPendingWrites` equal to false once the writes have been committed to the backend. |

## Methods

|                                                         Method                                                         | Modifiers |                              Description                              |
|------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------|
| [isEqual(other)](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadataisequal) |           | Returns true if this `SnapshotMetadata` is equal to the provided one. |

## SnapshotMetadata.fromCache

True if the snapshot was created from cached data rather than guaranteed up-to-date server data. If your listener has opted into metadata updates (via `SnapshotListenOptions`) you will receive another snapshot with `fromCache` set to false once the client has received up-to-date data from the backend.

**Signature:**  

    readonly fromCache: boolean;

## SnapshotMetadata.hasPendingWrites

True if the snapshot contains the result of local writes (for example `set()` or `update()` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via `SnapshotListenOptions`) you will receive another snapshot with `hasPendingWrites` equal to false once the writes have been committed to the backend.

**Signature:**  

    readonly hasPendingWrites: boolean;

## SnapshotMetadata.isEqual()

Returns true if this `SnapshotMetadata` is equal to the provided one.

**Signature:**  

    isEqual(other: SnapshotMetadata): boolean;

#### Parameters

| Parameter |                                                          Type                                                           |                Description                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| other     | [SnapshotMetadata](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadata_class) | The `SnapshotMetadata` to compare against. |

**Returns:**

boolean

true if this `SnapshotMetadata` is equal to the provided one.