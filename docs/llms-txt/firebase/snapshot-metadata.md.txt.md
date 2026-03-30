# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata.md.txt

# firebase::firestore::SnapshotMetadata Class Reference

# firebase::firestore::SnapshotMetadata


`#include <snapshot_metadata.h>`

Metadata about a snapshot, describing the state of the snapshot.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a5ed9881ce7368e6df6a205b6839f88ef()` Constructs a [SnapshotMetadata](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata) that has all of its boolean members set to false. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1ae5da92f585d864dcba7dfbe342c99308(bool has_pending_writes, bool is_from_cache)` Constructs a [SnapshotMetadata](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata) by providing boolean parameters that describe the state of the snapshot. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a2bb80b4b35fa7ba5a397c792de115334(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a3ffd87ecb389f3625df2268d43f8c379(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata && other)` Move constructor, equivalent to copying. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a3485379d4e0cad6002be882dc54d9bd3() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1ad6a023f67b5a2967d544b8f4693cf87f() const ` | `bool` Returns whether the snapshot contains the result of local writes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1ab8378d75002aef0d7a914d1cd861c5ff() const ` | `bool` Returns whether the snapshot was created from cached data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a60fd500bb8404e218dbb8cb83d43efd3(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata & other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a1e9e200108ec49a85b43fb489656e158(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata && other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata &` Move assignment operator, equivalent to copying. |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a69cb1cc1318fe1bbc21487953d3ad6c6` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to the given stream. |

## Public functions

### SnapshotMetadata

```c++
 SnapshotMetadata()=default
```
Constructs a [SnapshotMetadata](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata) that has all of its boolean members set to false.

### SnapshotMetadata

```c++
 SnapshotMetadata(
  bool has_pending_writes,
  bool is_from_cache
)
```
Constructs a [SnapshotMetadata](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata) by providing boolean parameters that describe the state of the snapshot.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `has_pending_writes` | Whether there is any pending write on the snapshot. | | `is_from_cache` | Whether the snapshot is from cache instead of backend. | |

### SnapshotMetadata

```c++
 SnapshotMetadata(
  const SnapshotMetadata & other
)=default
```
Copy constructor.

This performs a deep copy, creating an independent instance.


> [!NOTE]
> **Note:** This class is currently trivially copyable, but it is not guaranteed to stay that way, and code relying on this might be broken by a future release.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to copy from. | |

### SnapshotMetadata

```c++
 SnapshotMetadata(
  SnapshotMetadata && other
)=default
```
Move constructor, equivalent to copying.

After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to move data from. | |

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### has_pending_writes

```c++
bool has_pending_writes() const 
```
Returns whether the snapshot contains the result of local writes.

<br />

| Details ||
|---|---|
| **Returns** | true if the snapshot contains the result of local writes (for example, Set() or Update() calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via [MetadataChanges::kInclude](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a9f0a586c44417cd24932561719c97f54a279a35d9e230b4c8a0796fdf6f0d5360)) you will receive another snapshot with [has_pending_writes()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1ad6a023f67b5a2967d544b8f4693cf87f) equal to false once the writes have been committed to the backend. |

### is_from_cache

```c++
bool is_from_cache() const 
```
Returns whether the snapshot was created from cached data.

<br />

| Details ||
|---|---|
| **Returns** | true if the snapshot was created from cached data rather than guaranteed up-to-date server data. If your listener has opted into metadata updates (via [MetadataChanges::kInclude](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a9f0a586c44417cd24932561719c97f54a279a35d9e230b4c8a0796fdf6f0d5360)) you will receive another snapshot with [is_from_cache()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1ab8378d75002aef0d7a914d1cd861c5ff) equal to false once the client has received up-to-date data from the backend. |

### operator=

```c++
SnapshotMetadata & operator=(
  const SnapshotMetadata & other
)=default
```
Copy assignment operator.

This performs a deep copy, creating an independent instance.


> [!NOTE]
> **Note:** This class is currently trivially copyable, but it is not guaranteed to stay that way, and code relying on this might be broken by a future release.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata`. |

### operator=

```c++
SnapshotMetadata & operator=(
  SnapshotMetadata && other
)=default
```
Move assignment operator, equivalent to copying.

After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata`. |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const SnapshotMetadata &metadata)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata_1a3485379d4e0cad6002be882dc54d9bd3` for comments on the representation format.