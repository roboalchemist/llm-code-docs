# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.md.txt

# DocumentSnapshot

# DocumentSnapshot


```
public class DocumentSnapshot
```

<br />

Known direct subclasses [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot` | A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. |

*** ** * ** ***

A `DocumentSnapshot` contains data read from a document in your Cloud Firestore database. The data can be extracted with the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getData()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)` methods.

If the `DocumentSnapshot` points to a non-existing document, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getData()` and its corresponding methods will return `null`. You can always explicitly check for a document's existence by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#exists()`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` Controls the return value for server timestamps that have not yet been set to their final value. |

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#metadata()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#contains(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns whether or not the field exists in the document. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#contains(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Returns whether or not the field exists in the document. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#exists()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value at the field or `null` if the field doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Returns the value at the field or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field or `null` if the field doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(java.lang.String,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#get(com.google.firebase.firestore.FieldPath,java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getBlob(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a Blob. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getBoolean(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a boolean. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getData()()` Returns the fields of the document as a Map or `null` if the document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getData(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the fields of the document as a Map or `null` if the document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a Date. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDate(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value of the field as a Date. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDocumentReference(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a DocumentReference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getDouble(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a double. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getGeoPoint(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a GeoPoint. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getId()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getLong(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a long. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getMetadata()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getReference()()` Gets the reference to the document. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getString(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a String. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a `com.google.firebase.Timestamp`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getTimestamp(java.lang.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value of the field as a `com.google.firebase.Timestamp`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#getVectorValue(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Returns the value of the field as a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO or `null` if the document doesn't exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#toString()()` |

| ### Extension functions |
|---|---|
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver)` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |

## Public fields

### metadata

```
public final SnapshotMetadata metadata
```

## Public methods

### contains

```
public boolean contains(@NonNull String field)
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | the path to the field. |

| Returns |
|---|---|
| `boolean` | true iff the field exists. |

### contains

```
public boolean contains(@NonNull FieldPath fieldPath)
```

Returns whether or not the field exists in the document. Returns false if the document does not exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | the path to the field. |

| Returns |
|---|---|
| `boolean` | true iff the field exists. |

### equals

```
public boolean equals(@Nullable Object obj)
```

### exists

```
public boolean exists()
```

| Returns |
|---|---|
| `boolean` | true if the document existed in this snapshot. |

### get

```
public @Nullable Object get(@NonNull String field)
```

Returns the value at the field or `null` if the field doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The value at the given field or `null`. |

### get

```
public @Nullable Object get(@NonNull FieldPath fieldPath)
```

Returns the value at the field or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The value at the given field or `null`. |

### get

```
public @Nullable Object get(
    @NonNull String field,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field or `null` if the field doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The value at the given field or `null`. |

### get

```
public @Nullable T <T> get(@NonNull String field, @NonNull Class<T> valueType)
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to convert the field value to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The value at the given field or `null`. |

### get

```
public @Nullable Object get(
    @NonNull FieldPath fieldPath,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The value at the given field or `null`. |

### get

```
public @Nullable T <T> get(@NonNull FieldPath fieldPath, @NonNull Class<T> valueType)
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to convert the field value to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The value at the given field or `null`. |

### get

```
public @Nullable T <T> get(
    @NonNull String field,
    @NonNull Class<T> valueType,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The value at the given field or `null`. |

### get

```
public @Nullable T <T> get(
    @NonNull FieldPath fieldPath,
    @NonNull Class<T> valueType,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or `null` if the field or document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The value at the given field or `null`. |

### getBlob

```
public @Nullable Blob getBlob(@NonNull String field)
```

Returns the value of the field as a Blob.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a Blob. |

### getBoolean

```
public @Nullable Boolean getBoolean(@NonNull String field)
```

Returns the value of the field as a boolean. If the value is not a boolean this will throw a runtime exception.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | The value of the field |

### getData

```
public @Nullable Map<String, Object> getData()
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getData

```
public @Nullable Map<String, Object> getData(
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the fields of the document as a Map or `null` if the document doesn't exist. Field values will be converted to their native Java representation.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The fields of the document as a Map or `null` if the document doesn't exist. |

### getDate

```
public @Nullable Date getDate(@NonNull String field)
```

Returns the value of the field as a Date.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a Date. |

### getDate

```
public @Nullable Date getDate(
    @NonNull String field,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value of the field as a Date.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Date.html` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a Date. |

### getDocumentReference

```
public @Nullable DocumentReference getDocumentReference(@NonNull String field)
```

Returns the value of the field as a DocumentReference.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a DocumentReference. |

### getDouble

```
public @Nullable Double getDouble(@NonNull String field)
```

Returns the value of the field as a double.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a number. |

### getGeoPoint

```
public @Nullable GeoPoint getGeoPoint(@NonNull String field)
```

Returns the value of the field as a GeoPoint.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a GeoPoint. |

### getId

```
public @NonNull String getId()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The id of the document. |

### getLong

```
public @Nullable Long getLong(@NonNull String field)
```

Returns the value of the field as a long.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a number. |

### getMetadata

```
public @NonNull SnapshotMetadata getMetadata()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | The metadata for this document snapshot. |

### getReference

```
public @NonNull DocumentReference getReference()
```

Gets the reference to the document.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | The reference to the document. |

### getString

```
public @Nullable String getString(@NonNull String field)
```

Returns the value of the field as a String.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a String. |

### getTimestamp

```
public @Nullable Timestamp getTimestamp(@NonNull String field)
```

Returns the value of the field as a `com.google.firebase.Timestamp`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if this is not a timestamp field. |

### getTimestamp

```
public @Nullable Timestamp getTimestamp(
    @NonNull String field,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value of the field as a `com.google.firebase.Timestamp`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | The value of the field |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a timestamp field. |

### getVectorValue

```
public @Nullable VectorValue getVectorValue(@NonNull String field)
```

Returns the value of the field as a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` or `null` if the field does not exist in the document.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | The value of the field. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html java.lang.RuntimeException` | if the value is not a `VectorValue`. |

### hashCode

```
public int hashCode()
```

### toObject

```
public @Nullable T <T> toObject(@NonNull Class<T> valueType)
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to create |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toObject

```
public @Nullable T <T> toObject(
    @NonNull Class<T> valueType,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO or `null` if the document doesn't exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The Java class to create |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | The contents of the document in an object of type T or `null` if the document doesn't exist. |

### toString

```
public @NonNull String toString()
```

## Extension functions

### FirestoreKt.getField

```
public final T <T extends Object> FirestoreKt.getField(
    @NonNull DocumentSnapshot receiver,
    @NonNull String field
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |

| Returns |
|---|---|
| `T` | The value at the given field or null. |

### FirestoreKt.getField

```
public final T <T extends Object> FirestoreKt.getField(
    @NonNull DocumentSnapshot receiver,
    @NonNull String field,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The path to the field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The value at the given field or null. |

### FirestoreKt.getField

```
public final T <T extends Object> FirestoreKt.getField(
    @NonNull DocumentSnapshot receiver,
    @NonNull FieldPath fieldPath
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field. |

| Returns |
|---|---|
| `T` | The value at the given field or null. |

### FirestoreKt.getField

```
public final T <T extends Object> FirestoreKt.getField(
    @NonNull DocumentSnapshot receiver,
    @NonNull FieldPath fieldPath,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type to convert the field value to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The path to the field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The value at the given field or null. |

### FirestoreKt.toObject

```
public final T <T extends Object> FirestoreKt.toObject(@NonNull DocumentSnapshot receiver)
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T or null if the document doesn't ``` exist. ``` |

### FirestoreKt.toObject

```
public final T <T extends Object> FirestoreKt.toObject(
    @NonNull DocumentSnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ``` exist. ``` |