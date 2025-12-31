# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot.md.txt

# Firebase.Firestore.DocumentSnapshot Class Reference

# Firebase.Firestore.DocumentSnapshot

An immutable snapshot of the data for a document.

## Summary

A [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot) contains data read from a document in your Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) database. The data can be extracted with the [DocumentSnapshot.ToDictionary(ServerTimestampBehavior)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1ac32602ac4e08b5f54354696f9175f7c3) or M:DocumentSnapshot.GetValue\`1{T}(string, ServerTimestampBehavior) methods.

If the [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot) points to a non-existing document, `ToDictionary` will return `null`. You can always explicitly check for a document's existence by checking [DocumentSnapshot.Exists](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a1c7d7b7c88746e4bd3d85c97641a84b2).

|                                                                                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                                                                                        ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a734cee9c3d88d7c80d425aaca41b3230) | [SnapshotMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata) The metadata for this [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot). |

|                                                                                                                                                                                                                        ### Public attributes                                                                                                                                                                                                                         ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Exists](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a1c7d7b7c88746e4bd3d85c97641a84b2)` => _proxy.exists()`                                          | `bool` Whether or not the document exists.                                                                                                                                                                |
| [Id](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a4d887a7e68b7b9a408f2eb7d0254be97)` => _proxy.id()`                                                  | `string` The ID of the document.                                                                                                                                                                          |
| [Reference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a2c5ef30d49da7bfe3adbf123e91e23bf)` => new DocumentReference(_proxy.reference(), _firestore)` | [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) The full reference to the document. |

|                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                     ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [ContainsField](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a2637f949d4c5f10bd2282ee8e0269ab6)`(string path)`                                                                                                                                                                                                                                                                                                                                                                  | `bool` Determines whether or not the given field path is present in the document.                        |
| [ContainsField](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1aeb7ed06433f6229dfd08611d0025f5a9)`(`[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)` path)`                                                                                                                                                                                                                         | `bool` Determines whether or not the given field path is present in the document.                        |
| [ConvertTo< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1ab69fc552b2395c8a086e1413b63e4f8f)`(`[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)`                                                                                                                                                                      | `T` Deserializes the document data as the specified type.                                                |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a13b2e3d197b3b7b77a73d995dd4ad32e)`(object obj)`                                                                                                                                                                                                                                                                                                                                                                          | `override bool`                                                                                          |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a1d87df0a5a880a4b4c81794c0ee0ad6b)`(`[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` other)`                                                                                                                                                                                                          | `bool`                                                                                                   |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1ad2a4ab9955213e93337873440dfec864)`()`                                                                                                                                                                                                                                                                                                                                                                               | `override int`                                                                                           |
| [GetValue< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1aed20af05d758009ba8120063badd3fa8)`(string path, `[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)`                                                                                                                                                          | `T` Fetches a field value from the document, throwing an exception if the field does not exist.          |
| [GetValue< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a067d3a9a4c757b4b05bc3d82c1a7d1ef)`(`[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)` path, `[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)`                 | `T` Fetches a field value from the document, throwing an exception if the field does not exist.          |
| [ToDictionary](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1ac32602ac4e08b5f54354696f9175f7c3)`(`[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)`                                                                                                                                                                        | `Dictionary< string, object >` Returns the document data as a Dictionary{String, Object}.                |
| [TryGetValue< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1aefc34d4c753d79a804b65b3f38bdf5ee)`(string path, out T value, `[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)`                                                                                                                                          | `bool` Attempts to fetch the given field value from the document, returning whether or not it was found. |
| [TryGetValue< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a2306d85a1328a8d8a6e90d3d194a6fc0)`(`[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)` path, out T value, `[ServerTimestampBehavior](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a9082d514d3a7e574c9a40a4e7730dc60)` serverTimestampBehavior)` | `bool` Attempts to fetch the given field value from the document, returning whether or not it was found. |

## Properties

### Metadata

```c#
SnapshotMetadata Metadata
```  
The metadata for this [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot).

## Public attributes

### Exists

```c#
bool Exists => _proxy.exists()
```  
Whether or not the document exists.  

### Id

```c#
string Id => _proxy.id()
```  
The ID of the document.  

### Reference

```c#
DocumentReference Reference => new DocumentReference(_proxy.reference(), _firestore)
```  
The full reference to the document.

## Public functions

### ContainsField

```c#
bool ContainsField(
  string path
)
```  
Determines whether or not the given field path is present in the document.

If this snapshot represents a missing document, this method will always return `false`.

<br />

|                                                                                    Details                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|---------------------------------------------------------------------| | `path` | The dot-separated field path to check. Must not be `null` or empty. | |
| **Returns** | `true` if the specified path represents a field in the document; `false` otherwise.                                                                               |

### ContainsField

```c#
bool ContainsField(
  FieldPath path
)
```  
Determines whether or not the given field path is present in the document.

If this snapshot represents a missing document, this method will always return `false`.

<br />

|                                                             Details                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|----------------------------------------------| | `path` | The field path to check. Must not be `null`. | |
| **Returns** | `true` if the specified path represents a field in the document; `false` otherwise.                                 |

### ConvertTo\< T \>

```c#
T ConvertTo< T >(
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Deserializes the document data as the specified type.

<br />

|                                                                                                                                      Details                                                                                                                                       ||
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|-----------------------------------------------| | `T` | The type to deserialize the document data as. |                                                                                                                                               |
| Parameters          | |---------------------------|------------------------------------------------------------------------------------------------| | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. | |
| **Returns**         | The deserialized data or `default(T)` if this is a nonexistent document.                                                                                                                                                                                      |

### Equals

```c#
override bool Equals(
  object obj
)
```  

### Equals

```c#
bool Equals(
  DocumentSnapshot other
)
```  

### GetHashCode

```c#
override int GetHashCode()
```  

### GetValue\< T \>

```c#
T GetValue< T >(
  string path,
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Fetches a field value from the document, throwing an exception if the field does not exist.

<br />

|                                                                                                                                                                                                  Details                                                                                                                                                                                                  ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------------|------------------------------------------------------------------------------------------------| | `path`                    | The dot-separated field path to fetch. Must not be `null` or empty.                            | | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. | |
| Exceptions  | |-----------------------------|------------------------------------------------| | `InvalidOperationException` | The field does not exist in the document data. |                                                                                                                                                                                                                            |
| **Returns** | The deserialized value.                                                                                                                                                                                                                                                                                                                                                                      |

### GetValue\< T \>

```c#
T GetValue< T >(
  FieldPath path,
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Fetches a field value from the document, throwing an exception if the field does not exist.

<br />

|                                                                                                                                                                                                  Details                                                                                                                                                                                                  ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------------|------------------------------------------------------------------------------------------------| | `path`                    | The field path to fetch. Must not be `null` or empty.                                          | | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. | |
| Exceptions  | |-----------------------------|------------------------------------------------| | `InvalidOperationException` | The field does not exist in the document data. |                                                                                                                                                                                                                            |
| **Returns** | The deserialized value.                                                                                                                                                                                                                                                                                                                                                                      |

### ToDictionary

```c#
Dictionary< string, object > ToDictionary(
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Returns the document data as a Dictionary{String, Object}.

<br />

|                                                                                                                                  Details                                                                                                                                   ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------------|------------------------------------------------------------------------------------------------| | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. | |
| **Returns** | A Dictionary{String, Object} containing the document data or `null` if this is a nonexistent document.                                                                                                                                                        |

### TryGetValue\< T \>

```c#
bool TryGetValue< T >(
  string path,
  out T value,
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Attempts to fetch the given field value from the document, returning whether or not it was found.

This method does not throw an exception if the field is not found, but does throw an exception if the field was found but cannot be deserialized.

<br />

|                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------------|--------------------------------------------------------------------------------------------------------------------------| | `path`                    | The dot-separated field path to fetch. Must not be `null` or empty.                                                      | | `value`                   | When this method returns, contains the deserialized value if the field was found, or the default value of *T* otherwise. | | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value.                           | |
| **Returns** | `true` if the field was found in the document; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### TryGetValue\< T \>

```c#
bool TryGetValue< T >(
  FieldPath path,
  out T value,
  ServerTimestampBehavior serverTimestampBehavior
)
```  
Attempts to fetch the given field value from the document, returning whether or not it was found.

This method does not throw an exception if the field is not found, but does throw an exception if the field was found but cannot be deserialized.

<br />

|                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------------|--------------------------------------------------------------------------------------------------------------------------| | `path`                    | The field path to fetch. Must not be `null` or empty.                                                                    | | `value`                   | When this method returns, contains the deserialized value if the field was found, or the default value of *T* otherwise. | | `serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value.                           | |
| **Returns** | `true` if the field was found in the document; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |