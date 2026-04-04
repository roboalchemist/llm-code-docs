# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path.md.txt

# firebase::firestore::FieldPath Class Reference

# firebase::firestore::FieldPath


`#include <field_path.h>`

A [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) refers to a field in a document.

## Summary

The path may consist of a single field name (referring to a top level field in the document) or a list of field names (referring to a nested field in the document).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a1bfb61ea96153e870611dfeca9ca5768()` Creates an invalid [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a90bbfc3b4b5bb5b55141d82132731e02(std::initializer_list< std::string > field_names)` Creates a [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) from the provided field names. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a8dab4ca0013815114265c7511610de84(const std::vector< std::string > & field_names)` Creates a [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) from the provided field names. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1aa617f978bee4f464d276fc1a0215f099(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a43f69c580d47778b38bb5983a5bcfb64(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a2c94e4c32bda8843949b852b09e70f04()` ||

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a10e933ec9e2a2a071089c3010b4c842a` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to the given stream. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1aca9b72ef3032adb6ff43441b1c3429eb` | `friend struct` |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1aa693aa20233f691f7a9276bb3612da3d() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1ae790d81eb90c8300376657fd29546908() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a809f83bf473db1342bb0f5d68551f539(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1aa34e90a6cd8ebeab23d0c120251eae40(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path && other) noexcept` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path &` Move assignment operator. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1a0d5805f5220f6229494c6461e527d7d9()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` A special sentinel [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) to refer to the ID of a document. |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const FieldPath &path)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path_1aa693aa20233f691f7a9276bb3612da3d` for comments on the representation format.

### std::hash\< FieldPath \>

```c++
friend struct std::hash< FieldPath >
```

## Public functions

### FieldPath

```c++
 FieldPath()
```
Creates an invalid [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) that has to be reassigned before it can be used.

Calling any member function on an invalid [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### FieldPath

```c++
 FieldPath(
  std::initializer_list< std::string > field_names
)
```
Creates a [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) from the provided field names.

If more than one field name is provided, the path will point to a nested field in a document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field_names` | A list of field names. | |

### FieldPath

```c++
 FieldPath(
  const std::vector< std::string > & field_names
)
```
Creates a [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) from the provided field names.

If more than one field name is provided, the path will point to a nested field in a document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field_names` | A vector of field names. | |

### FieldPath

```c++
 FieldPath(
  const FieldPath & other
)
```
Copy constructor.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to copy from. | |

### FieldPath

```c++
 FieldPath(
  FieldPath && other
) noexcept
```
Move constructor.

Moving is more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path`. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to move data from. | |

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path`.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is invalid. |

### operator=

```c++
FieldPath & operator=(
  const FieldPath & other
)
```
Copy assignment operator.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path`. |

### operator=

```c++
FieldPath & operator=(
  FieldPath && other
) noexcept
```
Move assignment operator.

Moving is more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path`. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path`. |

### \~FieldPath

```c++
 ~FieldPath()
```

## Public static functions

### DocumentId

```c++
FieldPath DocumentId()
```
A special sentinel [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) to refer to the ID of a document.

It can be used in queries to sort or filter by the document ID.