# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.md.txt

# DatabaseKt

# DatabaseKt


```
public final class DatabaseKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).childEvents()` **This field is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/package-summary#(com.google.firebase.database.Query).snapshots()` **This field is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.ktx.Firebase).database(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.DataSnapshot).getValue())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.MutableData).getValue())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.[values](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.Query).values())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### childEvents

```
public final @NonNull Flow<@NonNull ChildEvent> childEvents
```

> [!CAUTION]
> **This field is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query's child events and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### database

```
public final @NonNull FirebaseDatabase database
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### snapshots

```
public final @NonNull Flow<@NonNull DataSnapshot> snapshots
```

> [!CAUTION]
> **This field is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(@NonNull Firebase receiver, @NonNull FirebaseApp app)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(@NonNull Firebase receiver, @NonNull String url)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance for the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(kotlin.String)`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String url
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/package-summary#(com.google.firebase.ktx.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### DatabaseKt.getValue

```
public static final T <T extends Object> DatabaseKt.[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.DataSnapshot).getValue())(@NonNull DataSnapshot receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### DatabaseKt.getValue

```
public static final T <T extends Object> DatabaseKt.[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.MutableData).getValue())(@NonNull MutableData receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### DatabaseKt.values

```
public static final @NonNull Flow<T> <T extends Object> DatabaseKt.[values](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt#(com.google.firebase.database.Query).values())(@NonNull Query receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening to this query and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)