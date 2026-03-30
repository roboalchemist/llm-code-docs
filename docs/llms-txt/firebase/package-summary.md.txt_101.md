# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary.md.txt

# com.google.firebase.firestore.ktx

# com.google.firebase.firestore.ktx

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` | `[firestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#firestoreSettings(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#memoryCacheSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#memoryEagerGcSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#memoryLruGcSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#persistentCacheSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T?>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.[dataObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges))(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.[dataObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges))(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.ktx.Firebase).firestore(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.ktx.Firebase).firestore(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.ktx.Firebase).firestore(kotlin.String)(database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath))(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String))(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.[snapshots](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges))(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` **This function is deprecated.** com.google.firebase.fires |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.[snapshots](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges))(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.ktx.Firebase).firestore()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### firestoreSettings

```
fun [firestoreSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#firestoreSettings(kotlin.Function1))(init: FirebaseFirestoreSettings.Builder.() -> Unit): FirebaseFirestoreSettings
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#firestoreSettings(kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### memoryCacheSettings

```
fun memoryCacheSettings(init: MemoryCacheSettings.Builder.() -> Unit): MemoryCacheSettings
```

### memoryEagerGcSettings

```
fun memoryEagerGcSettings(init: MemoryEagerGcSettings.Builder.() -> Unit): MemoryEagerGcSettings
```

### memoryLruGcSettings

```
fun memoryLruGcSettings(init: MemoryLruGcSettings.Builder.() -> Unit): MemoryLruGcSettings
```

### persistentCacheSettings

```
fun persistentCacheSettings(init: PersistentCacheSettings.Builder.() -> Unit): PersistentCacheSettings
```

## Extension functions

### dataObjects

```
inline fun <T : Any> DocumentReference.[dataObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges))(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<T?>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### dataObjects

```
inline fun <T : Any> Query.[dataObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges))(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<List<T>>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### firestore

```
fun Firebase.firestore(app: FirebaseApp, database: String): FirebaseFirestore
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and database name.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### firestore

```
fun Firebase.firestore(app: FirebaseApp): FirebaseFirestore
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### firestore

```
fun Firebase.firestore(database: String): FirebaseFirestore
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, given the database name.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getField

```
inline fun <T : Any?> DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))(
    fieldPath: FieldPath,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath))(fieldPath: FieldPath): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.[getField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String))(field: String): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### snapshots

```
fun DocumentReference.[snapshots](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges))(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<DocumentSnapshot>
```

> [!CAUTION]
> **This function is deprecated.**   
> com.google.firebase.fires

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### snapshots

```
fun Query.[snapshots](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges))(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<QuerySnapshot>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject())(): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |

| Returns |
|---|---|
| `T?` | The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject())(): T
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the document converted to a POJO.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T. |

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.[toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the document converted to a POJO.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T. |

### toObjects

```
inline fun <T : Any> QuerySnapshot.[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects())(): List<T>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The POJO type used to convert the documents in the list. |

### toObjects

```
inline fun <T : Any> QuerySnapshot.[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ktx/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): List<T>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The POJO type used to convert the documents in the list. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. ``` |

## Extension properties

### firestore

```
val Firebase.firestore: FirebaseFirestore
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)