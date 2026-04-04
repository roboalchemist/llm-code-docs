# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary.md.txt

# com.google.firebase.database.ktx

# com.google.firebase.database.ktx

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Added` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Changed` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Moved` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent.Removed` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(kotlin.String)(url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot.[getValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.DataSnapshot).getValue())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData.[getValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.MutableData).getValue())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T?>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query.[values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).values())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/ChildEvent>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).childEvents()` **This property is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).snapshots()` **This property is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions

### database

```
fun Firebase.database(app: FirebaseApp, url: String): FirebaseDatabase
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### database

```
fun Firebase.database(app: FirebaseApp): FirebaseDatabase
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### database

```
fun Firebase.database(url: String): FirebaseDatabase
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` instance for the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(kotlin.String)`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getValue

```
inline fun <T : Any?> DataSnapshot.[getValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.DataSnapshot).getValue())(): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getValue

```
inline fun <T : Any?> MutableData.[getValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.MutableData).getValue())(): T?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### values

```
inline fun <T : Any> Query.[values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).values())(): Flow<T?>
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### childEvents

```
val Query.childEvents: Flow<ChildEvent>
```

> [!CAUTION]
> **This property is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query's child events and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### database

```
val Firebase.database: FirebaseDatabase
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### snapshots

```
val Query.snapshots: Flow<DataSnapshot>
```

> [!CAUTION]
> **This property is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)