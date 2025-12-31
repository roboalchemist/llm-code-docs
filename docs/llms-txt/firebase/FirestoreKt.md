# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ktx/FirestoreKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.md.txt

# FirestoreKt

# FirestoreKt


```
public final class FirestoreKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                       ### Public fields                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) | [firestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore()) Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |

|                                                                                                                                                                                                                                                 ### Public methods                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<T>`                                                                                                                                                                                                                                                                           | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[dataObjects](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentReference](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` `)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                                                                                                                        |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>>` | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[dataObjects](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Query](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` `)` Starts listening to this query with the given options and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                                                                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore)                                                                                                                                                                                                                                                                               | [FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[firestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` `)` Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                 |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore)                                                                                                                                                                                                                                                                               | [FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[firestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` database` `)` Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp), given the database name.                                                                                                                                                                                                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore)                                                                                                                                                                                                                                                                               | [FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[firestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` database` `)` Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and database name.                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings)                                                                                                                                                                                                                                                               | [firestoreSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#firestoreSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns a [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)) function.                                                                                                                                                                                                                                                                                     |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[getField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` field` `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[getField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FieldPath](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath)` fieldPath` `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                          |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[getField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` field,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.                                                        |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[getField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FieldPath](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath)` fieldPath,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` `)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings)                                                                                                                                                                                                                                                                           | [memoryCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryCacheSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryEagerGcSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings)                                                                                                                                                                                                                                                                       | [memoryEagerGcSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryEagerGcSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryEagerGcSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryLruGcSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings)                                                                                                                                                                                                                                                                           | [memoryLruGcSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#memoryLruGcSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryLruGcSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[PersistentCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings)                                                                                                                                                                                                                                                                   | [persistentCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#persistentCacheSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[PersistentCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)`>`                                                       | [FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[snapshots](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentReference](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` `)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                                                                                                                                                                                                                                               |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[QuerySnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot)`>`                                                             | [FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[snapshots](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Query](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` `)` Starts listening to this query with the given options and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                                                                                                                                                                                                                                                                                                                                                            |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObject](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).toObject())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver)` Returns the contents of the document converted to a POJO or null if the document doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T`                                                                                                                                                                                                                                                                                                                                                                                                     | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObject](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot)` receiver)` Returns the contents of the document converted to a POJO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `static final T`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObject](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` `)` Returns the contents of the document converted to a POJO or null if the document doesn't exist.                                                                                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T`                                                                                                                                                                                                                                                                                                                                                                                                     | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObject](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` `)` Returns the contents of the document converted to a POJO.                                                                                                                                                                                                                                                                                           |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>`                                                                                                                                                                                                                         | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObjects](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QuerySnapshot).toObjects())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[QuerySnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot)` receiver)` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>`                                                                                                                                                                                                                         | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FirestoreKt](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt)`.`[toObjects](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[QuerySnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` `)` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.                                                                                                                                                                                                                                                                   |

## Public fields

### firestore

```
publicÂ finalÂ @NonNull FirebaseFirestoreÂ firestore
```

Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

## Public methods

### FirestoreKt.dataObjects

```
publicÂ staticÂ finalÂ @NonNull Flow<T>Â <TÂ extendsÂ Object> FirestoreKt.dataObjects(
Â Â Â Â @NonNull DocumentReferenceÂ receiver,
Â Â Â Â @NonNull MetadataChangesÂ metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, an [EventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener) will be attached.

- When the flow completes, the listener will be removed.

|                                                                                                              Parameters                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                        | The type of the object to convert to.                                                                                                                                        |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` | controls metadata-only changes. Default: [MetadataChanges.EXCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE) |

### FirestoreKt.dataObjects

```
publicÂ staticÂ finalÂ @NonNull Flow<@NonNull List<@NonNull T>>Â <TÂ extendsÂ Object> FirestoreKt.dataObjects(
Â Â Â Â @NonNull QueryÂ receiver,
Â Â Â Â @NonNull MetadataChangesÂ metadataChanges
)
```

Starts listening to this query with the given options and emits its values converted to a POJO via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, an [EventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener) will be attached.

- When the flow completes, the listener will be removed.

|                                                                                                              Parameters                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                        | The type of the object to convert to.                                                                                                                                        |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` | controls metadata-only changes. Default: [MetadataChanges.EXCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE) |

### FirestoreKt.firestore

```
publicÂ staticÂ finalÂ @NonNull FirebaseFirestoreÂ FirestoreKt.firestore(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app
)
```

Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### FirestoreKt.firestore

```
publicÂ staticÂ finalÂ @NonNull FirebaseFirestoreÂ FirestoreKt.firestore(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull StringÂ database
)
```

Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp), given the database name.  

### FirestoreKt.firestore

```
publicÂ staticÂ finalÂ @NonNull FirebaseFirestoreÂ FirestoreKt.firestore(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull StringÂ database
)
```

Returns the [FirebaseFirestore](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and database name.  

### firestoreSettings

```
publicÂ staticÂ finalÂ @NonNull FirebaseFirestoreSettingsÂ firestoreSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull FirebaseFirestoreSettings.Builder,Â Unit>Â init
)
```

Returns a [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)) function.  

### FirestoreKt.getField

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.getField(
Â Â Â Â @NonNull DocumentSnapshotÂ receiver,
Â Â Â Â @NonNull StringÂ field
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                       Parameters                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                         | The type to convert the field value to. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` field` | The path to the field.                  |

| Returns |
|---------|---------------------------------------|
| `T`     | The value at the given field or null. |

### FirestoreKt.getField

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.getField(
Â Â Â Â @NonNull DocumentSnapshotÂ receiver,
Â Â Â Â @NonNull FieldPathÂ fieldPath
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                                     Parameters                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                      | The type to convert the field value to. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FieldPath](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath)` fieldPath` | The path to the field.                  |

| Returns |
|---------|---------------------------------------|
| `T`     | The value at the given field or null. |

### FirestoreKt.getField

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.getField(
Â Â Â Â @NonNull DocumentSnapshotÂ receiver,
Â Â Â Â @NonNull StringÂ field,
Â Â Â Â @NonNull DocumentSnapshot.ServerTimestampBehaviorÂ serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                                                                           Parameters                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                                                                                  | The type to convert the field value to.                                                                                                                          |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` field`                                                                                                          | The path to the field.                                                                                                                                           |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```transact-sql been set to their final value. @return ``` The value at the given field or null. |

### FirestoreKt.getField

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.getField(
Â Â Â Â @NonNull DocumentSnapshotÂ receiver,
Â Â Â Â @NonNull FieldPathÂ fieldPath,
Â Â Â Â @NonNull DocumentSnapshot.ServerTimestampBehaviorÂ serverTimestampBehavior
)
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.  

|                                                                                                                                           Parameters                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                                                                                  | The type to convert the field value to.                                                                                                                          |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FieldPath](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath)` fieldPath`                                                                             | The path to the field.                                                                                                                                           |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```transact-sql been set to their final value. @return ``` The value at the given field or null. |

### memoryCacheSettings

```
publicÂ staticÂ finalÂ @NonNull MemoryCacheSettingsÂ memoryCacheSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull MemoryCacheSettings.Builder,Â Unit>Â init
)
```  

### memoryEagerGcSettings

```
publicÂ staticÂ finalÂ @NonNull MemoryEagerGcSettingsÂ memoryEagerGcSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull MemoryEagerGcSettings.Builder,Â Unit>Â init
)
```  

### memoryLruGcSettings

```
publicÂ staticÂ finalÂ @NonNull MemoryLruGcSettingsÂ memoryLruGcSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull MemoryLruGcSettings.Builder,Â Unit>Â init
)
```  

### persistentCacheSettings

```
publicÂ staticÂ finalÂ @NonNull PersistentCacheSettingsÂ persistentCacheSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull PersistentCacheSettings.Builder,Â Unit>Â init
)
```  

### FirestoreKt.snapshots

```
publicÂ staticÂ finalÂ @NonNull Flow<@NonNull DocumentSnapshot>Â FirestoreKt.snapshots(
Â Â Â Â @NonNull DocumentReferenceÂ receiver,
Â Â Â Â @NonNull MetadataChangesÂ metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, an [EventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener) will be attached.

- When the flow completes, the listener will be removed.

|                                                                                                              Parameters                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` | controls metadata-only changes. Default: [MetadataChanges.EXCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE) |

### FirestoreKt.snapshots

```
publicÂ staticÂ finalÂ @NonNull Flow<@NonNull QuerySnapshot>Â FirestoreKt.snapshots(
Â Â Â Â @NonNull QueryÂ receiver,
Â Â Â Â @NonNull MetadataChangesÂ metadataChanges
)
```

Starts listening to this query with the given options and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, an [EventListener](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener) will be attached.

- When the flow completes, the listener will be removed.

|                                                                                                              Parameters                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MetadataChanges](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges)` metadataChanges` | controls metadata-only changes. Default: [MetadataChanges.EXCLUDE](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE) |

### FirestoreKt.toObject

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.toObject(@NonNull DocumentSnapshotÂ receiver)
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.  

|                                           Parameters                                           |
|------------------------------------------------------------------------------------------------|-----------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>` | The type of the object to create. |

| Returns |
|---------|--------------------------------------------------------------------------------------------------------|
| `T`     | The contents of the document in an object of type T or null if the document doesn't ```text exist. ``` |

### FirestoreKt.toObject

```
publicÂ staticÂ finalÂ @NonNull TÂ <TÂ extendsÂ Object> FirestoreKt.toObject(@NonNull QueryDocumentSnapshotÂ receiver)
```

Returns the contents of the document converted to a POJO.  

|                                           Parameters                                           |
|------------------------------------------------------------------------------------------------|-----------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>` | The type of the object to create. |

|                                              Returns                                              |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T` | The contents of the document in an object of type T. |

### FirestoreKt.toObject

```
publicÂ staticÂ finalÂ TÂ <TÂ extendsÂ Object> FirestoreKt.toObject(
Â Â Â Â @NonNull DocumentSnapshotÂ receiver,
Â Â Â Â @NonNull DocumentSnapshot.ServerTimestampBehaviorÂ serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.  

|                                                                                                                                           Parameters                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                                                                                  | The type of the object to create.                                                                                                                                                                                                 |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```transact-sql been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ```text exist. ``` |

### FirestoreKt.toObject

```
publicÂ staticÂ finalÂ @NonNull TÂ <TÂ extendsÂ Object> FirestoreKt.toObject(
Â Â Â Â @NonNull QueryDocumentSnapshotÂ receiver,
Â Â Â Â @NonNull DocumentSnapshot.ServerTimestampBehaviorÂ serverTimestampBehavior
)
```

Returns the contents of the document converted to a POJO.  

|                                                                                                                                           Parameters                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                                                                                  | The type of the object to create.                                                                                                                                               |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```transact-sql been set to their final value. @return ``` The contents of the document in an object of type T. |

### FirestoreKt.toObjects

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull T>Â <TÂ extendsÂ Object> FirestoreKt.toObjects(@NonNull QuerySnapshotÂ receiver)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.  

|                                           Parameters                                           |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>` | The POJO type used to convert the documents in the list. |

### FirestoreKt.toObjects

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull T>Â <TÂ extendsÂ Object> FirestoreKt.toObjects(
Â Â Â Â @NonNull QuerySnapshotÂ receiver,
Â Â Â Â @NonNull DocumentSnapshot.ServerTimestampBehaviorÂ serverTimestampBehavior
)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.  

|                                                                                                                                           Parameters                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>`                                                                                                                                                                                                  | The POJO type used to convert the documents in the list.                                                   |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior)` serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```text been set to their final value. ``` |