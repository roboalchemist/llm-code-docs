# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.md.txt

# DocumentSnapshot

# DocumentSnapshot


```
class DocumentSnapshot
```

<br />

Known direct subclasses [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot` | A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. |

*** ** * ** ***

A `DocumentSnapshot` contains data read from a document in your Cloud Firestore database. The data can be extracted with the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)` methods.

If the `DocumentSnapshot` points to a non-existing document, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData()` and its corresponding methods will return `null`. You can always explicitly check for a document's existence by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists()`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` Controls the return value for server timestamps that have not yet been set to their final value. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns whether or not the field exists in the document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#contains(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns whether or not the field exists in the document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#exists()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value at the field or `null` if the field doesn't exist. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns the value at the field or `null` if the field or document doesn't exist. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field or `null` if the field doesn't exist. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field or `null` if the field or document doesn't exist. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBlob(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a Blob. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getBoolean(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a boolean. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData()()` Returns the fields of the document as a Map or `null` if the document doesn't exist. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getData(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the fields of the document as a Map or `null` if the document doesn't exist. |
| `https://developer.android.com/reference/kotlin/java/util/Date.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a Date. |
| `https://developer.android.com/reference/kotlin/java/util/Date.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value of the field as a Date. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDocumentReference(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a DocumentReference. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getDouble(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a double. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getGeoPoint(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a GeoPoint. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getId()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getLong(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a long. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getReference()()` Gets the reference to the document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getString(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a String. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a `com.google.firebase.Timestamp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value of the field as a `com.google.firebase.Timestamp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#getVectorValue(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value of the field as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#hashCode()()` |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>)(valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toString()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#metadata()` |

| ### Extension functions |
|---|---|
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject()()` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |

## Public functions

### contains

```
fun contains(field: String): Boolean
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true iff the field exists. |

### contains

```
fun contains(fieldPath: FieldPath): Boolean
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | the path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true iff the field exists. |

### equals

```
fun equals(obj: Any?): Boolean
```

### exists

```
fun exists(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if the document existed in this snapshot. |

### get

```
fun get(field: String): Any?
```

Returns the value at the field or `null` if the field doesn't exist.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value at the given field or `null`. |

### get

```
fun get(fieldPath: FieldPath): Any?
```

Returns the value at the field or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value at the given field or `null`. |

### get

```
fun get(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): Any?
```

Returns the value at the field or `null` if the field doesn't exist.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value at the given field or `null`. |

### get

```
fun <T> get(field: String, valueType: Class<T!>): T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to convert the field value to. |

| Returns |
|---|---|
| `T?` | The value at the given field or `null`. |

### get

```
fun get(
    fieldPath: FieldPath,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): Any?
```

Returns the value at the field or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value at the given field or `null`. |

### get

```
fun <T> get(fieldPath: FieldPath, valueType: Class<T!>): T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to convert the field value to. |

| Returns |
|---|---|
| `T?` | The value at the given field or `null`. |

### get

```
fun <T> get(
    field: String,
    valueType: Class<T!>,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to convert the field value to. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `T?` | The value at the given field or `null`. |

### get

```
fun <T> get(
    fieldPath: FieldPath,
    valueType: Class<T!>,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to convert the field value to. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `T?` | The value at the given field or `null`. |

### getBlob

```
fun getBlob(field: String): Blob?
```

Returns the value of the field as a Blob.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a Blob. |

### getBoolean

```
fun getBoolean(field: String): Boolean?
```

Returns the value of the field as a boolean. If the value is not a boolean this will throw a runtime exception.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | The value of the field |

### getData

```
fun getData(): (Mutable)Map<String!, Any!>?
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>?` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getData

```
fun getData(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): (Mutable)Map<String!, Any!>?
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.

| Parameters |
|---|---|
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>?` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getDate

```
fun getDate(field: String): Date?
```

Returns the value of the field as a Date.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/util/Date.html?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a Date. |

### getDate

```
fun getDate(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): Date?
```

Returns the value of the field as a Date.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/util/Date.html?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a Date. |

### getDocumentReference

```
fun getDocumentReference(field: String): DocumentReference?
```

Returns the value of the field as a DocumentReference.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a DocumentReference. |

### getDouble

```
fun getDouble(field: String): Double?
```

Returns the value of the field as a double.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a number. |

### getGeoPoint

```
fun getGeoPoint(field: String): GeoPoint?
```

Returns the value of the field as a GeoPoint.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a GeoPoint. |

### getId

```
fun getId(): String
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The id of the document. |

### getLong

```
fun getLong(field: String): Long?
```

Returns the value of the field as a long.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a number. |

### getReference

```
fun getReference(): DocumentReference
```

Gets the reference to the document.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The reference to the document. |

### getString

```
fun getString(field: String): String?
```

Returns the value of the field as a String.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a String. |

### getTimestamp

```
fun getTimestamp(field: String): Timestamp?
```

Returns the value of the field as a `com.google.firebase.Timestamp`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if this is not a timestamp field. |

### getTimestamp

```
fun getTimestamp(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): Timestamp?
```

Returns the value of the field as a `com.google.firebase.Timestamp`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | The value of the field |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a timestamp field. |

### getVectorValue

```
fun getVectorValue(field: String): VectorValue?
```

Returns the value of the field as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue?` | The value of the field. |

| Throws |
|---|---|
| `java.lang.RuntimeException: https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html` | if the value is not a `VectorValue`. |

### hashCode

```
fun hashCode(): Int
```

### toObject

```
fun <T> toObject(valueType: Class<T!>): T?
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.

| Parameters |
|---|---|
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to create |

| Returns |
|---|---|
| `T?` | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toObject

```
fun <T> toObject(
    valueType: Class<T!>,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.

| Parameters |
|---|---|
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The Java class to create |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `T?` | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toString

```
fun toString(): String
```

## Public properties

### metadata

```
val metadata: SnapshotMetadata!
```

## Extension functions

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(field: String): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(fieldPath: FieldPath): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(
    fieldPath: FieldPath,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.toObject(): T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |

| Returns |
|---|---|
| `T?` | The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.toObject(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |