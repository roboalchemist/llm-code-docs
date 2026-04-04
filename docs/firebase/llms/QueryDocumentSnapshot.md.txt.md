# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot.md.txt

# QueryDocumentSnapshot

# QueryDocumentSnapshot


```
public class QueryDocumentSnapshot extends DocumentSnapshot
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot) ||
|   | ↳ | [com.google.firebase.firestore.QueryDocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot) |

*** ** * ** ***

A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted using the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#getData()` or the various `get()` methods in `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot` (such as `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)`).

`QueryDocumentSnapshot` offers the same API surface as `DocumentSnapshot`. Since query results contain only existing documents, the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#exists()` method will always return true and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#getData()` will never be `null`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#getData()()` Returns the fields of the document as a Map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#getData(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the fields of the document as a Map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#toObject(java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the contents of the document converted to a POJO. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#toObject(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot receiver)` Returns the contents of the document converted to a POJO. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO. |

| ### Inherited fields |
|---|
| From [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#metadata()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot) |---|---| | `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#contains(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns whether or not the field exists in the document. | | `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#contains(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Returns whether or not the field exists in the document. | | `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` | | `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#exists()()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value at the field or `null` if the field doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Returns the value at the field or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field or `null` if the field doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getBlob(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a Blob. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getBoolean(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a boolean. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a Date. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value of the field as a Date. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDocumentReference(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a DocumentReference. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDouble(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a double. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getGeoPoint(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a GeoPoint. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getId()()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getLong(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a long. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getMetadata()()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getReference()()` Gets the reference to the document. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getString(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a String. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a `com.google.firebase.Timestamp`. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value of the field as a `com.google.firebase.Timestamp`. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getVectorValue(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document. | | `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#hashCode()()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#toString()()` | |

## Public methods

### getData

```
public @NonNull Map<String, Object> getData()
```

Returns the fields of the document as a Map. Field values will be converted to their native Java representation.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The fields of the document as a Map. |

### getData

```
public @NonNull Map<String, Object> getData(
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the fields of the document as a Map. Field values will be converted to their native Java representation.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The fields of the document as a Map or `null` if the document doesn't exist. |

### toObject

```
public @NonNull T <T> toObject(@NonNull Class<T> valueType)
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to create |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | The contents of the document in an object of type T |

### toObject

```
public @NonNull T <T> toObject(
    @NonNull Class<T> valueType,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to create |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | The contents of the document in an object of type T. |

## Extension functions

### FirestoreKt.toObject

```
public final @NonNull T <T extends Object> FirestoreKt.toObject(@NonNull QueryDocumentSnapshot receiver)
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | The contents of the document in an object of type T. |

### FirestoreKt.toObject

```
public final @NonNull T <T extends Object> FirestoreKt.toObject(
    @NonNull QueryDocumentSnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The contents of the document in an object of type T. |