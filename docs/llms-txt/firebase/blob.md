# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob.md.txt

# Firebase.Firestore.Blob Struct Reference

# Firebase.Firestore.Blob

An immutable sequence of bytes.

## Summary

Although this is a struct, it's effectively just a wrapper around a byte\[\].

### Inheritance

Inherits from: IEquatable\< Blob \>

|                                                                                                            ### Public attributes                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [Length](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a29bff39fbd2ba27bd4f9fc5152819268)` => _bytes.Length`          | `int` The length of the blob, in bytes.    |
| [this[int index]](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a19959067be0fa7bcf638afc3c3ce6dd9)` => _bytes[index]` | `byte` Returns the byte at index *index* . |

|                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                     ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1aff79c17a2384ddbafed2d06691750a62)`(object obj)`                                                                                                                             | `override bool`                                                                                                                                                               |
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a23071560ae74d601e7277bae3d2925ec)`(`[Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob)` other)` | `bool`                                                                                                                                                                        |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1ae80aac5d2f60fdaccef20ad68c85909d)`()`                                                                                                                                  | `override int`                                                                                                                                                                |
| [ToBytes](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a1e9025aebdd409e25eb623d3bbf402e5)`()`                                                                                                                                      | `byte[]` Returns a copy of this [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) as a byte\[\]. |
| [ToString](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a1f683454986101f30154307982eca988)`()`                                                                                                                                     | `override string`                                                                                                                                                             |

|                                                                                                                                                                                                                                                                                                                                                                            ### Public static functions                                                                                                                                                                                                                                                                                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CopyFrom](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a3859b2104888a865d579d9137fbe1381)`(byte[] bytes)`                                                                                                                                                                                                                                                                 | [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) Constructs a new [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) by copying the current content of *bytes* . |
| [operator!=](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a3e55d25ce3e1df875c62376d568d8d8a)`(`[Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob)` lhs, `[Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob)` rhs)` | `bool` Operator overload to compare two [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) values for inequality.                                                                                                                              |
| [operator==](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a93171704c4d5aa26bebd8291ed1e2994)`(`[Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob)` lhs, `[Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob)` rhs)` | `bool` Operator overload to compare two [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) values for equality.                                                                                                                                |

## Public attributes

### Length

```c#
int Firebase::Firestore::Blob::Length => _bytes.Length
```  
The length of the blob, in bytes.  

### this\[int index\]

```c#
byte Firebase::Firestore::Blob::this[int index] => _bytes[index]
```  
Returns the byte at index *index* .

<br />

|                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `index` | The index in the blob to return. Must be greater than or equal to 0, and less than [Length](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob_1a29bff39fbd2ba27bd4f9fc5152819268). | |
| **Returns** | The byte at index *index* .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Public functions

### Equals

```c#
override bool Firebase::Firestore::Blob::Equals(
  object obj
)
```  

### Equals

```c#
bool Firebase::Firestore::Blob::Equals(
  Blob other
)
```  

### GetHashCode

```c#
override int Firebase::Firestore::Blob::GetHashCode()
```  

### ToBytes

```c#
byte[] Firebase::Firestore::Blob::ToBytes()
```  
Returns a copy of this [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) as a byte\[\].  

### ToString

```c#
override string Firebase::Firestore::Blob::ToString()
```  

## Public static functions

### CopyFrom

```c#
Blob Firebase::Firestore::Blob::CopyFrom(
  byte[] bytes
)
```  
Constructs a new [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) by copying the current content of *bytes* .

<br />

|                                     Details                                      ||
|-------------|---------------------------------------------------------------------|
| Parameters  | |---------|---------------------| | `bytes` | Byte array to copy. | |
| **Returns** | A new blob containing a copy of *bytes* .                           |

### operator!=

```c#
bool Firebase::Firestore::Blob::operator!=(
  Blob lhs,
  Blob rhs
)
```  
Operator overload to compare two [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) values for inequality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | false if *lhs* is equal to *rhs* ; otherwise true.                                                       |

### operator==

```c#
bool Firebase::Firestore::Blob::operator==(
  Blob lhs,
  Blob rhs
)
```  
Operator overload to compare two [Blob](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/blob#struct_firebase_1_1_firestore_1_1_blob) values for equality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | true if *lhs* is equal to *rhs* ; otherwise false.                                                       |