# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options.md.txt

# Firebase.Firestore.SetOptions Class Reference

# Firebase.Firestore.SetOptions

An options object that configures the behavior of `SetAsync` calls.

## Summary

By providing one of the [SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) objects returned by [SetOptions.MergeAll](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a5a1c963bf5a45a3008ac2cf69acb87b1) and SetOptions.MergeFields(string\[\]) the `SetAsync` calls in [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference), [WriteBatch](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch) and [Transaction](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction) can be configured to perform granular merges instead of overwriting the target documents in their entirety.

|                                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                                        ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MergeAll](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a5a1c963bf5a45a3008ac2cf69acb87b1)  | `static `[SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) Changes the behavior of `SetAsync` calls to only replace the values specified in its `documentData` argument. |
| [Overwrite](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1ad6276e4792d4c87d0313af76f2f6905a) | `static `[SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) Returns an instance that overwrites the target object.                                                        |

|                                                                                                                                                                                                                                                                             ### Public static functions                                                                                                                                                                                                                                                                              ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MergeFields](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a5a17c8e0b222986600684794c790cc1d)`(params string[] fields)`                                                                                                                                          | [SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) Changes the behavior of `SetAsync` calls to only replace the given fields. |
| [MergeFields](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a39846009cfbd8030e6ef6ff7525f5e7d)`(params `[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)`[] fields)` | [SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) Changes the behavior of `SetAsync` calls to only replace the given fields. |

|                                                                                               ### Public functions                                                                                               ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a87fd0d83511b83aed8d0c9d9f3d1a5a4)`(object obj)` | `override bool`   |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a543060a6fec45afe2272c737cb7eae13)`()`      | `override int`    |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a64e8114b5a808a3bf4c53a85f1b47251)`()`         | `override string` |

## Properties

### MergeAll

```c#
static SetOptions MergeAll
```  
Changes the behavior of `SetAsync` calls to only replace the values specified in its `documentData` argument.

Fields omitted from the `SetAsync` call will remain untouched.  

### Overwrite

```c#
static SetOptions Overwrite
```  
Returns an instance that overwrites the target object.

This is the default when no options are provided.

## Public static functions

### MergeFields

```c#
SetOptions MergeFields(
  params string[] fields
)
```  
Changes the behavior of `SetAsync` calls to only replace the given fields.

Any field that is not specified in *fields* is ignored and remains untouched.

It is an error to pass a [SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) object to a `set()` call that is missing a value for any of the fields specified here.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                        ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `fields` | The fields to merge. An empty array is equivalent to using [MergeAll](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a5a1c963bf5a45a3008ac2cf69acb87b1). Must not be `null` or contain any empty or `null` elements. Each field is treated as a dot-separated list of segments. | |
| **Returns** | An instance that merges the given fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### MergeFields

```c#
SetOptions MergeFields(
  params FieldPath[] fields
)
```  
Changes the behavior of `SetAsync` calls to only replace the given fields.

Any field that is not specified in *fields* is ignored and remains untouched.

It is an error to pass a [SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options) object to a `SetAsync` call that is missing a value for any of the fields specified here in its data argument.

<br />

|                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `fields` | The fields to merge. An empty array is equivalent to using [MergeAll](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1a5a1c963bf5a45a3008ac2cf69acb87b1). Must not be `null` or contain any `null` elements. | |
| **Returns** | An instance that merges the given fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Public functions

### Equals

```c#
override bool Equals(
  object obj
)
```  

### GetHashCode

```c#
override int GetHashCode()
```  

### ToString

```c#
override string ToString()
```