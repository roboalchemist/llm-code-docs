# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options.md.txt

# firebase::firestore::SetOptions Class Reference

# firebase::firestore::SetOptions


`#include <set_options.h>`

An options object that configures the behavior of Set() calls.

## Summary

By providing the [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options) objects returned by [Merge()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a64fc825a4de04509f392f3947075cc14), the Set() methods in [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference), [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) and [Transaction](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction) can be configured to perform granular merges instead of overwriting the target documents in their entirety.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1ab655936516fa63ebe64e2cb6a278c136()` Creates [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options) with overwrite semantics. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1ac4b2e1b8fdf115d6fc4e1d317fe0d83f(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a8464c5185ad38b43f8a45c26b03cf588(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a04a00853cb04e602d6fe5868e9af016d()` ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a2135efa4447faa76a8c400eab7084205{ https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a2135efa4447faa76a8c400eab7084205abfd4483cecc9ffd36f88de2c9f53b8dc, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a2135efa4447faa76a8c400eab7084205a95704621f6cc655bcd2a198b33be9bcf, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a2135efa4447faa76a8c400eab7084205afa73c9a632b76599acd400459861bcbf }` | enumThe enumeration of all types of [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options). |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a091efd6dd6503e33f02604cd8b785da7(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options & other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a944b74a2855310c3c996a1409949ef47(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options && other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options &` Move assignment operator. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1a64fc825a4de04509f392f3947075cc14()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` Returns an instance that can be used to change the behavior of Set() calls to only replace the values specified in its data argument. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1aeaa962277a4419b7dd2f8e1044e9fccf(const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path > & fields)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` Returns an instance that can be used to change the behavior of Set() calls to only replace the given fields. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options_1aa304a67776e89b98c385eb8929e64a98(const std::vector< std::string > & fields)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` Returns an instance that can be used to change the behavior of Set() calls to only replace the given fields. |

## Public types

### Type

```c++
 Type
```
The enumeration of all types of [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options).

| Properties ||
|---|---|
| `kMergeAll` | Replaces the values specified in the call parameter while leaves omitted fields untouched. |
| `kMergeSpecific` | Replaces the values of the fields explicitly specified in the call parameter. |
| `kOverwrite` | Overwrites the whole document. |

## Public functions

### SetOptions

```c++
 SetOptions()=default
```
Creates [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options) with overwrite semantics.

### SetOptions

```c++
 SetOptions(
  const SetOptions & other
)=default
```
Copy constructor.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` to copy from. | |

### SetOptions

```c++
 SetOptions(
  SetOptions && other
)=default
```
Move constructor.

Moving is more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options`. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` to move data from. | |

### operator=

```c++
SetOptions & operator=(
  const SetOptions & other
)=default
```
Copy assignment operator.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options`. |

### operator=

```c++
SetOptions & operator=(
  SetOptions && other
)=default
```
Move assignment operator.

Moving is more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options`. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options`. |

### \~SetOptions

```c++
 ~SetOptions()
```

## Public static functions

### Merge

```c++
SetOptions Merge()
```
Returns an instance that can be used to change the behavior of Set() calls to only replace the values specified in its data argument.

Fields omitted from the Set() call will remain untouched.

### MergeFieldPaths

```c++
SetOptions MergeFieldPaths(
  const std::vector< FieldPath > & fields
)
```
Returns an instance that can be used to change the behavior of Set() calls to only replace the given fields.

Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options) object to a Set() call that is missing a value for any of the fields specified here in its to data argument.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fields` | The list of fields to merge. | |

### MergeFields

```c++
SetOptions MergeFields(
  const std::vector< std::string > & fields
)
```
Returns an instance that can be used to change the behavior of Set() calls to only replace the given fields.

Any field that is not specified in `fields` is ignored and remains untouched.

It is an error to pass a [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options) object to a Set() call that is missing a value for any of the fields specified here.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fields` | The list of fields to merge. Fields can contain dots to reference nested fields within the document. | |