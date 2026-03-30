# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data.md.txt

# firebase::database::MutableData Class Reference

# firebase::database::MutableData


`#include <mutable_data.h>`

Instances of this class encapsulate the data and priority at a location.

## Summary

It is used in transactions, and it is intended to be inspected and then updated to the desired data at that location.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a53c623589a6d99a21d2801c987091ff5()` Destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a195fd2c2b8a8c8e8b8186afd4f41a437(const char *path)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data` Used to obtain a [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a2ca694b89725d586d2bdb341efdc26c7(const std::string & path)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data` Used to obtain a [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a710159ef446a1ac2524a5f2221c84f12(const char *path) const ` | `bool` Does this [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) have data at a particular location? |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1acbe7e7f7c4ed0c068795e807108258e6(const std::string & path) const ` | `bool` Does this [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) have data at a particular location? |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a4f856005cc1fb90c7bcb8132b48775c4()` | `std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data >` Get all the immediate children of this location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1aee49dfdb4f4cc0741dd2329727a8610f()` | `size_t` Get the number of children of this location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1af3d27a14a310606ba745fe3cdfbe9f3a() const ` | `const char *` Get the key name of the source location of this data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a66c55f22712a08c4f33b058c8c12db67() const ` | `std::string` Get the key name of the source location of this data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a6cd529e1a816e423146fa80652b104cc()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` Get the priority of the data contained at this snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a9f72e95b1db5fac02e7e682ebbb2d5e6(const https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant & priority)` | `void` Sets the priority of this field, which controls its sort order relative to its siblings. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a53a6a2bf6a0ecce0fa06537060320c9b(const https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant & value)` | `void` Sets the data at this location to the given value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1ab43ecdbc034434a3183a59206d601cb6() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` Get the value of the data contained at this location. |

## Public functions

### Child

```c++
MutableData Child(
  const char *path
)
```
Used to obtain a [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path.

Note that changes made to a child [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) instance will be visible to the parent and vice versa.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. The pointer only needs to be valid during this call. | |
| **Returns** | [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) for the Child relative to this location. The memory will be freed when the Transaction is finished. |

### Child

```c++
MutableData Child(
  const std::string & path
)
```
Used to obtain a [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this snapshot's location. | |
| **Returns** | [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) for the Child relative to this location. The memory will be freed when the Transaction is finished. |

### HasChild

```c++
bool HasChild(
  const char *path
) const 
```
Does this [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) have data at a particular location?

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this data's location. The pointer only needs to be valid during this call. | |
| **Returns** | True if there is data at the specified location, false if not. |

### HasChild

```c++
bool HasChild(
  const std::string & path
) const 
```
Does this [MutableData](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data) have data at a particular location?

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this data's location. | |
| **Returns** | True if there is data at the specified location, false if not. |

### children

```c++
std::vector< MutableData > children()
```
Get all the immediate children of this location.

<br />

| Details ||
|---|---|
| **Returns** | The immediate children of this location. |

### children_count

```c++
size_t children_count()
```
Get the number of children of this location.

<br />

| Details ||
|---|---|
| **Returns** | The number of immediate children of this location. |

### key

```c++
const char * key() const 
```
Get the key name of the source location of this data.


> [!NOTE]
> **Note:** The returned pointer is only guaranteed to be valid during the transaction.

<br />

| Details ||
|---|---|
| **Returns** | Key name of the source location of this data. |

### key_string

```c++
std::string key_string() const 
```
Get the key name of the source location of this data.

<br />

| Details ||
|---|---|
| **Returns** | Key name of the source location of this data. |

### priority

```c++
Variant priority()
```
Get the priority of the data contained at this snapshot.

<br />

| Details ||
|---|---|
| **Returns** | The value of this location's Priority relative to its siblings. |

### set_priority

```c++
void set_priority(
  const Variant & priority
)
```
Sets the priority of this field, which controls its sort order relative to its siblings.

**See also:** [firebase::database::DatabaseReference::SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6) for information on how Priority affects the ordering of a node's [children](https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data#classfirebase_1_1database_1_1_mutable_data_1a4f856005cc1fb90c7bcb8132b48775c4).

| Details ||
|---|---|
| Parameters | |---|---| | `priority` | Sort priority for this child relative to its siblings. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types accepted are Null, Int64, Double, and String. Other types will return kErrorInvalidVariantType. | |

### set_value

```c++
void set_value(
  const Variant & value
)
```
Sets the data at this location to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `value` | The value to set this location to. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type corresponds to the types accepted by the database JSON: Null: Deletes this location from the database. Int64: Inserts an integer value into this location. Double: Inserts a floating point value into this location. String: Inserts a string into this location. (Accepts both Mutable and Static strings) Vector: Inserts a JSON array into this location. The elements can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type, including Vector and Map. Map: Inserts a JSON associative array into this location. The keys must be of type String (or Int64/Double which are converted to String). The values can be any [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type, including Vector and Map. | |

### value

```c++
Variant value() const 
```
Get the value of the data contained at this location.

<br />

| Details ||
|---|---|
| **Returns** | The value of the data contained at this location. |

### \~MutableData

```c++
 ~MutableData()
```
Destructor.