# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.md.txt

# QueryDocumentSnapshot

# QueryDocumentSnapshot


```
class QueryDocumentSnapshot : DocumentSnapshot
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) ||
|   | ↳ | [com.google.firebase.firestore.QueryDocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot) |

*** ** * ** ***

A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#getData()` or the various `get()` methods in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` (such as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)`).

`QueryDocumentSnapshot` offers the same API surface as `DocumentSnapshot`. Since query results contain only existing documents, the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists()` method will always return true and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#getData()` will never be `null`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#getData()()` Returns the fields of the document as a Map. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#getData(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the fields of the document as a Map. |
| `T` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#toObject(java.lang.Class<T>)(valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the contents of the document converted to a POJO. |
| `T` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#toObject(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO. |

| ### Extension functions |
|---|---|
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject()()` Returns the contents of the document converted to a POJO. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns whether or not the field exists in the document. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns whether or not the field exists in the document. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value at the field or `null` if the field doesn't exist. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns the value at the field or `null` if the field or document doesn't exist. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field or `null` if the field doesn't exist. | | `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field or `null` if the field or document doesn't exist. | | `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBlob(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a Blob. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBoolean(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a boolean. | | `https://developer.android.com/reference/kotlin/java/util/Date.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a Date. | | `https://developer.android.com/reference/kotlin/java/util/Date.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value of the field as a Date. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDocumentReference(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a DocumentReference. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDouble(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a double. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getGeoPoint(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a GeoPoint. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getId()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getLong(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a long. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getMetadata()()` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getReference()()` Gets the reference to the document. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getString(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a String. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a `com.google.firebase.Timestamp`. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value of the field as a `com.google.firebase.Timestamp`. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getVectorValue(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#hashCode()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toString()()` | |

| ### Inherited properties |
|---|
| From [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#metadata()` | |

## Public functions

### getData

```
fun getData(): (Mutable)Map<String!, Any!>
```

Returns the fields of the document as a Map. Field values will be converted to their native Java representation.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The fields of the document as a Map. |

### getData

```
fun getData(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): (Mutable)Map<String!, Any!>
```

Returns the fields of the document as a Map. Field values will be converted to their native Java representation.

| Parameters |
|---|---|
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The fields of the document as a Map or `null` if the document doesn't exist. |

### toObject

```
fun <T> toObject(valueType: Class<T!>): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to create |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T |

### toObject

```
fun <T> toObject(
    valueType: Class<T!>,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to create |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T. |

## Extension functions

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.toObject(): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T. |

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.toObject(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T. |