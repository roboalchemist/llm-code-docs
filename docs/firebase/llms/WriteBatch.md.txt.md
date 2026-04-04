# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.md.txt

# WriteBatch

# WriteBatch


```
public class WriteBatch
```

<br />

*** ** * ** ***

A write batch, used to perform multiple writes as a single atomic unit.

A Batch object can be acquired by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#batch()`. It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#commit()` is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function` An interface for providing code to be executed within a `WriteBatch` context. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#commit()()` Commits all of the writes in this write batch as a single atomic unit. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#delete(com.google.firebase.firestore.DocumentReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef)` Deletes the document referred to by the provided `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data)` Overwrites the document referred to by the provided `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object,com.google.firebase.firestore.SetOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions options )` Writes to the document referred to by the provided `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.util.Map<java.lang.String,java.lang.Object>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> data )` Updates fields in the document referred to by the provided `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.lang.String,java.lang.Object,java.lang.Object...)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, Object[] moreFieldsAndValues )` Updates field in the document referred to by the provided `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, Object[] moreFieldsAndValues )` Updates fields in the document referred to by the provided `DocumentReference`. |

## Public methods

### commit

```
public @NonNull Task<Void> commit()
```

Commits all of the writes in this write batch as a single atomic unit.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

### delete

```
public @NonNull WriteBatch delete(@NonNull DocumentReference documentRef)
```

Deletes the document referred to by the provided `DocumentReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to delete. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
public @NonNull WriteBatch set(@NonNull DocumentReference documentRef, @NonNull Object data)
```

Overwrites the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to overwrite. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data` | The data to write to the document (like a Map or a POJO containing the desired document contents). |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
public @NonNull WriteBatch set(
    @NonNull DocumentReference documentRef,
    @NonNull Object data,
    @NonNull SetOptions options
)
```

Writes to the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to overwrite. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data` | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions options` | An object to configure the set behavior. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
public @NonNull WriteBatch update(
    @NonNull DocumentReference documentRef,
    @NonNull Map<String, Object> data
)
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to update. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> data` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
public @NonNull WriteBatch update(
    @NonNull DocumentReference documentRef,
    @NonNull String field,
    @Nullable Object value,
    Object[] moreFieldsAndValues
)
```

Updates field in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to update. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The first value |
| `Object[] moreFieldsAndValues` | Additional field/value pairs. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
public @NonNull WriteBatch update(
    @NonNull DocumentReference documentRef,
    @NonNull FieldPath fieldPath,
    @Nullable Object value,
    Object[] moreFieldsAndValues
)
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documentRef` | The `DocumentReference` to update. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The first field to update. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The first value |
| `Object[] moreFieldsAndValues` | Additional field/value pairs. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |