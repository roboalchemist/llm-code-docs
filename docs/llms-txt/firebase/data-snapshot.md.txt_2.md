# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot.md.txt

# firebase::database::DataSnapshot Class Reference

# firebase::database::DataSnapshot


`#include <data_snapshot.h>`

A [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) instance contains data from a Firebase [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) location.

## Summary

Any time you read [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) data, you receive the data as a [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). These are efficiently-generated and cannot be changed. To modify data, use [DatabaseReference::SetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1adf3c8604639c1c09e954412d709e942e) or [DatabaseReference::RunTransaction()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a968af852dee06997c7767f6f318ae88c).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a46297f17dfd896d932a765e9c3a54b38()` Default constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a3a12c7ce620cd5d9d310e4c40aec2418(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot & snapshot)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a51e5a5d80f6c18af1144a268dd77d06f(https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot && snapshot)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a6bab651dd5633268708bfb7be336b9ed()` Destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a859c49a11fd17f89927af9c05ad920cc(const char *path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot` Get a [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) for the location at the specified relative path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1affbeb84e5f2a51607466d3abac622a2c(const std::string & path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot` Get a [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) for the location at the specified relative path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1adea1125f39e034cfde842c9e792454a9() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Obtain a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the source location for this snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a28b54e1f1822597de2aac68112db612a(const char *path) const ` | `bool` Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have data at a particular location? |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a947d48fcb9cdf4c6dfb50c8ef22f127b(const std::string & path) const ` | `bool` Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have data at a particular location? |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a2dedc81fb243e0e9b417b0aafa2f56b5() const ` | `std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot >` Get all the immediate children of this location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a8e70f000750747461cd92635fe9344ce() const ` | `size_t` Get the number of children of this location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a489191042a09a78ff98570e9c303284d() const ` | `bool` Returns true if the data is non-empty. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1ac4c2cd0f61ae2b92e2a7e5e61cbc7833() const ` | `bool` Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have any children at all? |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a4915ddb07d211d40dfd7c99cc7fe55ec() const ` | `bool` Returns true if this snapshot is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a423dc39dc62c4953508209b8a1656d96() const ` | `const char *` Get the key name of the source location of this snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a710bda01d4bc218472dee8afeebebaa3() const ` | `std::string` Get the key name of the source location of this snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a2a3705dbdb2d0923ad3adc4be49de936(const https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot & snapshot)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a08acf027091d0537c830c0d79aed474b(https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot && snapshot)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a98b727d4cf30a47e0ecb706244959793() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` Get the priority of the data contained in this snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1aaf7e2866b329ee41a249961b72ad70d0() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` Get the value of the data contained in this snapshot. |

## Public functions

### Child

```c++
DataSnapshot Child(
  const char *path
) const 
```
Get a [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) for the location at the specified relative path.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. It only needs to be valid during this call. | |
| **Returns** | A [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) corresponding to specified child location. |

### Child

```c++
DataSnapshot Child(
  const std::string & path
) const 
```
Get a [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) for the location at the specified relative path.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. | |
| **Returns** | A [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) corresponding to specified child location. |

### DataSnapshot

```c++
 DataSnapshot()
```
Default constructor.

This [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) contains nothing and is considered invalid (i.e. [is_valid()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot_1a4915ddb07d211d40dfd7c99cc7fe55ec) == false). Use this to construct an empty [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) that you will later populate with data from a database callback.

### DataSnapshot

```c++
 DataSnapshot(
  const DataSnapshot & snapshot
)
```
Copy constructor.

DataSnapshots are immutable, so they can be efficiently copied.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) to copy. | |

### DataSnapshot

```c++
 DataSnapshot(
  DataSnapshot && snapshot
)
```
Move constructor.

DataSnapshots are immutable, so they can be efficiently moved.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) to move into this one. | |

### GetReference

```c++
DatabaseReference GetReference() const 
```
Obtain a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the source location for this snapshot.

<br />

| Details ||
|---|---|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) corresponding to same location as this snapshot. |

### HasChild

```c++
bool HasChild(
  const char *path
) const 
```
Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have data at a particular location?

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. The pointer only needs to be valid during this call. | |
| **Returns** | True if the snapshot has data at the specified location, false if not. |

### HasChild

```c++
bool HasChild(
  const std::string & path
) const 
```
Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have data at a particular location?

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. | |
| **Returns** | True if the snapshot has data at the specified location, false if not. |

### children

```c++
std::vector< DataSnapshot > children() const 
```
Get all the immediate children of this location.

<br />

| Details ||
|---|---|
| **Returns** | The immediate children of this snapshot. |

### children_count

```c++
size_t children_count() const 
```
Get the number of children of this location.

<br />

| Details ||
|---|---|
| **Returns** | The number of immediate children of this snapshot. |

### exists

```c++
bool exists() const 
```
Returns true if the data is non-empty.

### has_children

```c++
bool has_children() const 
```
Does this [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) have any children at all?

<br />

| Details ||
|---|---|
| **Returns** | True if the snapshot has any children, false otherwise. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this snapshot is valid, false if it is not valid.

An invalid snapshot could be returned by a transaction where an error has occurred.

<br />

| Details ||
|---|---|
| **Returns** | true if this snapshot is valid, false if this snapshot is invalid. |

### key

```c++
const char * key() const 
```
Get the key name of the source location of this snapshot.


> [!NOTE]
> **Note:** The returned pointer is only guaranteed to be valid while the [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) is still in memory.

<br />

| Details ||
|---|---|
| **Returns** | Key name of the source location of this snapshot. |

### key_string

```c++
std::string key_string() const 
```
Get the key name of the source location of this snapshot.

<br />

| Details ||
|---|---|
| **Returns** | Key name of the source location of this snapshot. |

### operator=

```c++
DataSnapshot & operator=(
  const DataSnapshot & snapshot
)
```
Copy assignment operator.

DataSnapshots are immutable, so they can be efficiently copied.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) to copy. | |
| **Returns** | Reference to the destination [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). |

### operator=

```c++
DataSnapshot & operator=(
  DataSnapshot && snapshot
)
```
Move assignment operator.

DataSnapshots are immutable, so they can be efficiently moved.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot) to move into this one. | |
| **Returns** | Reference to this destination [DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot). |

### priority

```c++
Variant priority() const 
```
Get the priority of the data contained in this snapshot.

<br />

| Details ||
|---|---|
| **Returns** | The value of this location's Priority relative to its siblings. |

### value

```c++
Variant value() const 
```
Get the value of the data contained in this snapshot.

<br />

| Details ||
|---|---|
| **Returns** | The value of the data contained in this location. |

### \~DataSnapshot

```c++
 ~DataSnapshot()
```
Destructor.