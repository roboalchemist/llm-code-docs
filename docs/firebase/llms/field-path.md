# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path.md.txt

# Firebase.Firestore.FieldPath Class Reference

# Firebase.Firestore.FieldPath

An immutable path of field names, used to identify parts of a document.

## Summary

A [FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path) refers to a field in a document. The path may consist of a single field name (referring to a top level field in the document), or a list of field names (referring to a nested field in the document).

### Inheritance

Inherits from: IEquatable\< FieldPath \>

| ### Constructors and Destructors ||
|---|---|
| [FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1a8e1c019e47216d1cdea6641a71a4c917)`(params string[] segments)` Creates a path from multiple segments. ||

|                                                                                                                                                                                         ### Properties                                                                                                                                                                                          ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DocumentId](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1ac055d7d976ed8eaa6a8df8f709df50e1) | `static `[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path) Sentinel field path to refer to the ID of a document. |

|                                                                                                                                                                   ### Public functions                                                                                                                                                                    ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1aa908f5781cce570163c7446c8d66098a)`(object obj)`                                                                                                                                            | `override bool`   |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1a804f334ffd7d95f1384f2defc0fc63af)`(`[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)` other)` | `bool`            |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1abb2513401647dbf4fe2b6c927edea6be)`()`                                                                                                                                                 | `override int`    |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path_1ab7679b2bed5536e7ab094b0d88aa62aa)`()`                                                                                                                                                    | `override string` |

## Properties

### DocumentId

```c#
static FieldPath DocumentId
```  
Sentinel field path to refer to the ID of a document.

Used in queries to sort or filter by the document ID.

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
  FieldPath other
)
```  

### FieldPath

```c#
 FieldPath(
  params string[] segments
)
```  
Creates a path from multiple segments.

Each segment is treated verbatim: it may contain dots, which will lead to the segment being escaped in the path's string representation.

<br />

|                                                                                                                                      Details                                                                                                                                      ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------------------------------------------------------------------------------| | `segments` | The segments of the path. This must not be `null` or empty, and it must not contain any `null` or empty elements. | |

### GetHashCode

```c#
override int GetHashCode()
```  

### ToString

```c#
override string ToString()
```