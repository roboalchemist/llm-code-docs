# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/DatabaseKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.md.txt

# DatabaseKt

# DatabaseKt


```
public final class DatabaseKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                                                                              ### Public fields                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEvent)`>`     | [childEvents](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).childEvents()) Starts listening to this query's child events and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase)                                                                                                                                                                                                                   | [database](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database()) Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DataSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot)`>` | [snapshots](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.database.Query).snapshots()) Starts listening to this query and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                   |

|                                                                                                            ### Public methods                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase)        | [DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[database](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase)        | [DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[database](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url)` Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance for the specified [url](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(kotlin.String)).                                                                                                                                                                                                                                                                                                                                                                                      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase)        | [DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[database](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url` `)` Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [url](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)). |
| `static final T`                                                                                                                                                                                                                         | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.DataSnapshot).getValue())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DataSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot)` receiver)` Returns the content of the DataSnapshot converted to a POJO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `static final T`                                                                                                                                                                                                                         | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.MutableData).getValue())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData)` receiver)` Returns the content of the MutableData converted to a POJO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<T>` | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[values](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt#(com.google.firebase.database.Query).values())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Query](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query)` receiver)` Starts listening to this query and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Public fields

### childEvents

```
publicÂ finalÂ @NonNull Flow<@NonNull ChildEvent>Â childEvents
```

Starts listening to this query's child events and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ChildEventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener) will be attached.

- When the flow completes, the listener will be removed.

### database

```
publicÂ finalÂ @NonNull FirebaseDatabaseÂ database
```

Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### snapshots

```
publicÂ finalÂ @NonNull Flow<@NonNull DataSnapshot>Â snapshots
```

Starts listening to this query and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ValueEventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener) will be attached.

- When the flow completes, the listener will be removed.

## Public methods

### DatabaseKt.database

```
publicÂ staticÂ finalÂ @NonNull FirebaseDatabaseÂ DatabaseKt.database(@NonNull FirebaseÂ receiver,Â @NonNull FirebaseAppÂ app)
```

Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### DatabaseKt.database

```
publicÂ staticÂ finalÂ @NonNull FirebaseDatabaseÂ DatabaseKt.database(@NonNull FirebaseÂ receiver,Â @NonNull StringÂ url)
```

Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance for the specified [url](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(kotlin.String)).  

### DatabaseKt.database

```
publicÂ staticÂ finalÂ @NonNull FirebaseDatabaseÂ DatabaseKt.database(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull StringÂ url
)
```

Returns the [FirebaseDatabase](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) instance of the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [url](https://firebase.google.com/docs/reference/android/com/google/firebase/database/package-summary#(com.google.firebase.Firebase).database(com.google.firebase.FirebaseApp,kotlin.String)).  

### DatabaseKt.getValue

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> DatabaseKt.getValue(@NonNull DataSnapshotÂ receiver)
```

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.  

### DatabaseKt.getValue

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> DatabaseKt.getValue(@NonNull MutableDataÂ receiver)
```

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.  

### DatabaseKt.values

```
publicÂ staticÂ finalÂ @NonNull Flow<T>Â <TÂ extendsÂ Object> DatabaseKt.values(@NonNull QueryÂ receiver)
```

Starts listening to this query and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, a [ValueEventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener) will be attached.

- When the flow completes, the listener will be removed.