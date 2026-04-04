# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.md.txt

# FirestoreKt

# FirestoreKt


```
public final class FirestoreKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`, given the database name. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and database name. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#firestoreSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)` function. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryCacheSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryEagerGcSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryLruGcSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#persistentCacheSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).toObject()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver)` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot receiver)` Returns the contents of the document converted to a POJO. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the document converted to a POJO. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QuerySnapshot).toObjects()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot receiver)` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |

## Public fields

### firestore

```
public final @NonNull FirebaseFirestore firestore
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### FirestoreKt.dataObjects

```
public static final @NonNull Flow<T> <T extends Object> FirestoreKt.dataObjects(
    @NonNull DocumentReference receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to convert to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### FirestoreKt.dataObjects

```
public static final @NonNull Flow<@NonNull List<@NonNull T>> <T extends Object> FirestoreKt.dataObjects(
    @NonNull Query receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to convert to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### FirestoreKt.firestore

```
public static final @NonNull FirebaseFirestore FirestoreKt.firestore(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### FirestoreKt.firestore

```
public static final @NonNull FirebaseFirestore FirestoreKt.firestore(
    @NonNull Firebase receiver,
    @NonNull String database
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`, given the database name.

### FirestoreKt.firestore

```
public static final @NonNull FirebaseFirestore FirestoreKt.firestore(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String database
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and database name.

### firestoreSettings

```
public static final @NonNull FirebaseFirestoreSettings firestoreSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull FirebaseFirestoreSettings.Builder, Unit> init
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)` function.

### FirestoreKt.getField

```
public static final T <T extends Object> FirestoreKt.getField(
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
public static final T <T extends Object> FirestoreKt.getField(
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
public static final T <T extends Object> FirestoreKt.getField(
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
public static final T <T extends Object> FirestoreKt.getField(
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

### memoryCacheSettings

```
public static final @NonNull MemoryCacheSettings memoryCacheSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull MemoryCacheSettings.Builder, Unit> init
)
```

### memoryEagerGcSettings

```
public static final @NonNull MemoryEagerGcSettings memoryEagerGcSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull MemoryEagerGcSettings.Builder, Unit> init
)
```

### memoryLruGcSettings

```
public static final @NonNull MemoryLruGcSettings memoryLruGcSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull MemoryLruGcSettings.Builder, Unit> init
)
```

### persistentCacheSettings

```
public static final @NonNull PersistentCacheSettings persistentCacheSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull PersistentCacheSettings.Builder, Unit> init
)
```

### FirestoreKt.snapshots

```
public static final @NonNull Flow<@NonNull DocumentSnapshot> FirestoreKt.snapshots(
    @NonNull DocumentReference receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### FirestoreKt.snapshots

```
public static final @NonNull Flow<@NonNull QuerySnapshot> FirestoreKt.snapshots(
    @NonNull Query receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### FirestoreKt.toObject

```
public static final T <T extends Object> FirestoreKt.toObject(@NonNull DocumentSnapshot receiver)
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
public static final @NonNull T <T extends Object> FirestoreKt.toObject(@NonNull QueryDocumentSnapshot receiver)
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
public static final T <T extends Object> FirestoreKt.toObject(
    @NonNull DocumentSnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ``` exist. ``` |

### FirestoreKt.toObject

```
public static final @NonNull T <T extends Object> FirestoreKt.toObject(
    @NonNull QueryDocumentSnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to create. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. @return ``` The contents of the document in an object of type T. |

### FirestoreKt.toObjects

```
public static final @NonNull List<@NonNull T> <T extends Object> FirestoreKt.toObjects(@NonNull QuerySnapshot receiver)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The POJO type used to convert the documents in the list. |

### FirestoreKt.toObjects

```
public static final @NonNull List<@NonNull T> <T extends Object> FirestoreKt.toObjects(
    @NonNull QuerySnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The POJO type used to convert the documents in the list. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. ``` |