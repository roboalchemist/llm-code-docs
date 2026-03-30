# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.md.txt

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
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).childEvents()` Starts listening to this query's child events and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).snapshots()` Starts listening to this query and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance for the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.DataSnapshot).getValue()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot receiver)` Returns the content of the DataSnapshot converted to a POJO. |
| `static final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.MutableData).getValue()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData receiver)` Returns the content of the MutableData converted to a POJO. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.Query).values()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query receiver)` Starts listening to this query and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Public fields

### childEvents

```
public final @NonNull Flow<@NonNull ChildEvent> childEvents
```

Starts listening to this query's child events and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener` will be attached.

- When the flow completes, the listener will be removed.

### database

```
public final @NonNull FirebaseDatabase database
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### snapshots

```
public final @NonNull Flow<@NonNull DataSnapshot> snapshots
```

Starts listening to this query and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.

## Public methods

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(@NonNull Firebase receiver, @NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(@NonNull Firebase receiver, @NonNull String url)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance for the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(kotlin.String)`.

### DatabaseKt.database

```
public static final @NonNull FirebaseDatabase DatabaseKt.database(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String url
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` instance of the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)`.

### DatabaseKt.getValue

```
public static final T <T extends Object> DatabaseKt.getValue(@NonNull DataSnapshot receiver)
```

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

### DatabaseKt.getValue

```
public static final T <T extends Object> DatabaseKt.getValue(@NonNull MutableData receiver)
```

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.

### DatabaseKt.values

```
public static final @NonNull Flow<T> <T extends Object> DatabaseKt.values(@NonNull Query receiver)
```

Starts listening to this query and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener` will be attached.

- When the flow completes, the listener will be removed.