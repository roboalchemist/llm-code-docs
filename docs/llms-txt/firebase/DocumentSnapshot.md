# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.md.txt

# DocumentSnapshot

# DocumentSnapshot


```
class DocumentSnapshot
```

<br />

Known direct subclasses  
[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot)  

|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot) | A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. |

*** ** * ** ***

A `DocumentSnapshot` contains data read from a document in your Cloud Firestore database. The data can be extracted with the [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData()) or [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)) methods.

If the `DocumentSnapshot` points to a non-existing document, [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData()) and its corresponding methods will return `null`. You can always explicitly check for a document's existence by calling [exists](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists()).

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                                                                                                               ### Nested types                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enum `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) Controls the return value for server timestamps that have not yet been set to their final value. |

|                                                                                                                                                                         ### Public functions                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                    | [contains](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns whether or not the field exists in the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                    | [contains](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(com.google.firebase.firestore.FieldPath))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`)` Returns whether or not the field exists in the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                    | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#equals(java.lang.Object))`(obj: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                    | [exists](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                                                                                                                                                                                                         | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value at the field or `null` if the field doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                                                                                                                                                                                                         | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`)` Returns the value at the field or `null` if the field or document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                                                                                                                                                                                                         | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field or `null` if the field doesn't exist.                                                                                                                                                                                                               |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.                                                                                                                                                                                                                                                                                                                                     |
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                                                                                                                                                                                                         | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field or `null` if the field or document doesn't exist.                                                                                                                                                  |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`, valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.                                                                                                                                                                                                                                                                                    |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.                                                  |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`,` ` valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| [Blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)`?`                                                                                                                                                                                                                                                                       | [getBlob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBlob(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a Blob.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?`                                                                                                                                                                                                                                                                                 | [getBoolean](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBoolean(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a boolean.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>?` | [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData())`()` Returns the fields of the document as a Map or `null` if the document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>?` | [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the fields of the document as a Map or `null` if the document doesn't exist.                                                                                                                                                                                                                                                                                                      |
| [Date](https://developer.android.com/reference/kotlin/java/util/Date.html)`?`                                                                                                                                                                                                                                                                                         | [getDate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a Date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Date](https://developer.android.com/reference/kotlin/java/util/Date.html)`?`                                                                                                                                                                                                                                                                                         | [getDate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value of the field as a Date.                                                                                                                                                                                                                                  |
| [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`?`                                                                                                                                                                                                                                             | [getDocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDocumentReference(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a DocumentReference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?`                                                                                                                                                                                                                                                                                   | [getDouble](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDouble(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a double.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [GeoPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint)`?`                                                                                                                                                                                                                                                               | [getGeoPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getGeoPoint(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a GeoPoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                                                                      | [getId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getId())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`?`                                                                                                                                                                                                                                                                                       | [getLong](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getLong(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a long.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                                                                                                                                                                                                                | [getReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getReference())`()` Gets the reference to the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                                                                   | [getString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getString(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a String.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`?`                                                                                                                                                                                                                                                                       | [getTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a `com.google.firebase.Timestamp`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`?`                                                                                                                                                                                                                                                                       | [getTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value of the field as a `com.google.firebase.Timestamp`.                                                                                                                                                                                             |
| [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)`?`                                                                                                                                                                                                                                                         | [getVectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getVectorValue(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value of the field as a [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) or `null` if the field does not exist in the document.                                                                                                                                                                                                                                                                                                                                        |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                                                                            | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#hashCode())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>))`(valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>)` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `T?`                                                                                                                                                                                                                                                                                                                                                                  | `<T> `[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.                                                                                                                                                            |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                                                                   | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toString())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

|                                                  ### Public properties                                                  |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [SnapshotMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata)`!` | [metadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#metadata()) |

| ### Extension functions |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                                                                                                                                                                                                                                                                                                     |
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                     |
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                                                                                                                                                                                                                                                 |
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject())`()` Returns the contents of the document converted to a POJO or null if the document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `inline T?`             | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> `[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`.`[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the contents of the document converted to a POJO or null if the document doesn't exist.                                                                                                                                                                      |

## Public functions

### contains

```
funÂ contains(field:Â String):Â Boolean
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the path to the field. |

|                                      Returns                                       |
|------------------------------------------------------------------------------------|----------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true iff the field exists. |

### contains

```
funÂ contains(fieldPath:Â FieldPath):Â Boolean
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.  

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | the path to the field. |

|                                      Returns                                       |
|------------------------------------------------------------------------------------|----------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true iff the field exists. |

### equals

```
funÂ equals(obj:Â Any?):Â Boolean
```  

### exists

```
funÂ exists():Â Boolean
```  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if the document existed in this snapshot. |

### get

```
funÂ get(field:Â String):Â Any?
```

Returns the value at the field or `null` if the field doesn't exist.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-----------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|-----------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | The value at the given field or `null`. |

### get

```
funÂ get(fieldPath:Â FieldPath):Â Any?
```

Returns the value at the field or `null` if the field or document doesn't exist.  

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|-----------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | The path to the field |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|-----------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | The value at the given field or `null`. |

### get

```
funÂ get(
Â Â Â Â field:Â String,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â Any?
```

Returns the value at the field or `null` if the field doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                       | The path to the field                                                                          |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|-----------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | The value at the given field or `null`. |

### get

```
funÂ <T> get(field:Â String,Â valueType:Â Class<T!>):Â T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)       | The path to the field                         |
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>` | The Java class to convert the field value to. |

| Returns |
|---------|-----------------------------------------|
| `T?`    | The value at the given field or `null`. |

### get

```
funÂ get(
Â Â Â Â fieldPath:Â FieldPath,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â Any?
```

Returns the value at the field or `null` if the field or document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)                                                                             | The path to the field                                                                          |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|-----------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | The value at the given field or `null`. |

### get

```
funÂ <T> get(fieldPath:Â FieldPath,Â valueType:Â Class<T!>):Â T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.  

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | The path to the field                         |
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>`                     | The Java class to convert the field value to. |

| Returns |
|---------|-----------------------------------------|
| `T?`    | The value at the given field or `null`. |

### get

```
funÂ <T> get(
Â Â Â Â field:Â String,
Â Â Â Â valueType:Â Class<T!>,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                       | The path to the field                                                                          |
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>`                                                                                                 | The Java class to convert the field value to.                                                  |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---------|-----------------------------------------|
| `T?`    | The value at the given field or `null`. |

### get

```
funÂ <T> get(
Â Â Â Â fieldPath:Â FieldPath,
Â Â Â Â valueType:Â Class<T!>,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)                                                                             | The path to the field                                                                          |
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>`                                                                                                 | The Java class to convert the field value to.                                                  |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---------|-----------------------------------------|
| `T?`    | The value at the given field or `null`. |

### getBlob

```
funÂ getBlob(field:Â String):Â Blob?
```

Returns the value of the field as a Blob.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                             Returns                                             |
|-------------------------------------------------------------------------------------------------|------------------------|
| [Blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a Blob. |

### getBoolean

```
funÂ getBoolean(field:Â String):Â Boolean?
```

Returns the value of the field as a boolean. If the value is not a boolean this will throw a runtime exception.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                        Returns                                        |
|---------------------------------------------------------------------------------------|------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?` | The value of the field |

### getData

```
funÂ getData():Â (Mutable)Map<String!,Â Any!>?
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.  

|                                                                                                                                                                                Returns                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>?` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getData

```
funÂ getData(
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â (Mutable)Map<String!,Â Any!>?
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

|                                                                                                                                                                                Returns                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>?` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getDate

```
funÂ getDate(field:Â String):Â Date?
```

Returns the value of the field as a Date.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|------------------------|
| [Date](https://developer.android.com/reference/kotlin/java/util/Date.html)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a Date. |

### getDate

```
funÂ getDate(
Â Â Â Â field:Â String,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â Date?
```

Returns the value of the field as a Date.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                       | The path to the field.                                                                         |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

|                                    Returns                                    |
|-------------------------------------------------------------------------------|------------------------|
| [Date](https://developer.android.com/reference/kotlin/java/util/Date.html)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a Date. |

### getDocumentReference

```
funÂ getDocumentReference(field:Â String):Â DocumentReference?
```

Returns the value of the field as a DocumentReference.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                                          Returns                                                          |
|---------------------------------------------------------------------------------------------------------------------------|------------------------|
| [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a DocumentReference. |

### getDouble

```
funÂ getDouble(field:Â String):Â Double?
```

Returns the value of the field as a double.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|------------------------|
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a number. |

### getGeoPoint

```
funÂ getGeoPoint(field:Â String):Â GeoPoint?
```

Returns the value of the field as a GeoPoint.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                                 Returns                                                 |
|---------------------------------------------------------------------------------------------------------|------------------------|
| [GeoPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a GeoPoint. |

### getId

```
funÂ getId():Â String
```  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The id of the document. |

### getLong

```
funÂ getLong(field:Â String):Â Long?
```

Returns the value of the field as a long.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                     Returns                                     |
|---------------------------------------------------------------------------------|------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a number. |

### getReference

```
funÂ getReference():Â DocumentReference
```

Gets the reference to the document.  

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The reference to the document. |

### getString

```
funÂ getString(field:Â String):Â String?
```

Returns the value of the field as a String.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a String. |

### getTimestamp

```
funÂ getTimestamp(field:Â String):Â Timestamp?
```

Returns the value of the field as a `com.google.firebase.Timestamp`.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                             Returns                                             |
|-------------------------------------------------------------------------------------------------|------------------------|
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if this is not a timestamp field. |

### getTimestamp

```
funÂ getTimestamp(
Â Â Â Â field:Â String,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â Timestamp?
```

Returns the value of the field as a `com.google.firebase.Timestamp`.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                       | The path to the field.                                                                         |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

|                                             Returns                                             |
|-------------------------------------------------------------------------------------------------|------------------------|
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`?` | The value of the field |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a timestamp field. |

### getVectorValue

```
funÂ getVectorValue(field:Â String):Â VectorValue?
```

Returns the value of the field as a [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) or `null` if the field does not exist in the document.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field. |

|                                                    Returns                                                    |
|---------------------------------------------------------------------------------------------------------------|-------------------------|
| [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)`?` | The value of the field. |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `java.lang.RuntimeException: `[java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) | if the value is not a `VectorValue`. |

### hashCode

```
funÂ hashCode():Â Int
```  

### toObject

```
funÂ <T> toObject(valueType:Â Class<T!>):Â T?
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|--------------------------|
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>` | The Java class to create |

| Returns |
|---------|----------------------------------------------------------------------------------------------|
| `T?`    | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toObject

```
funÂ <T> toObject(
Â Â Â Â valueType:Â Class<T!>,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `valueType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>`                                                                                                 | The Java class to create                                                                       |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---------|----------------------------------------------------------------------------------------------|
| `T?`    | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toString

```
funÂ toString():Â String!
```  

## Public properties

### metadata

```
valÂ metadata:Â SnapshotMetadata!
```  

## Extension functions

### getField

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.getField(field:Â String):Â T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>`     | The type to convert the field value to. |
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The path to the field.                  |

| Returns |
|---------|---------------------------------------|
| `T?`    | The value at the given field or null. |

### getField

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.getField(
Â Â Â Â field:Â String,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>`                                                                                                           | The type to convert the field value to.                                                                                                                    |
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                       | The path to the field.                                                                                                                                     |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.getField(fieldPath:Â FieldPath):Â T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>`                               | The type to convert the field value to. |
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | The path to the field.                  |

| Returns |
|---------|---------------------------------------|
| `T?`    | The value at the given field or null. |

### getField

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.getField(
Â Â Â Â fieldPath:Â FieldPath,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>`                                                                                                           | The type to convert the field value to.                                                                                                                    |
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)                                                                             | The path to the field.                                                                                                                                     |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### toObject

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.toObject():Â T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.  

|                                      Parameters                                       |
|---------------------------------------------------------------------------------------|-----------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>` | The type of the object to create. |

| Returns |
|---------|----------------------------------------------------------------------------------------------------------|
| `T?`    | The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inlineÂ funÂ <TÂ :Â Any?> DocumentSnapshot.toObject(
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>`                                                                                                           | The type of the object to create.                                                                                                                                                                                             |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |