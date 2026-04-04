# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/StorageKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.md.txt

# StorageKt

# StorageKt


```
public final class StorageKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                                                                                                                           ### Public fields                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage)                                                                                                                                                                                                                                                                                                                | [storage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage()) Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[TaskState](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>>` | [taskState](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StorageTask).taskState()) Starts listening to this task's progress and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).                                               |

|                                                                                                                                                                                               ### Public methods                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)` receiver)` Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide bytesTransferred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)`>` | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult)` receiver)` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its items.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)` receiver)` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide bytesTransferred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide bytesTransferred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)` receiver)` Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide totalByteCount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)`>` | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult)` receiver)` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its prefixes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)` receiver)` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide totalByteCount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `static final long`                                                                                                                                                                                                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide totalByteCount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `static final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                                                                                                                                                                  | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component3())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult)` receiver)` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its pageToken.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)                                                                                                                                                                                                            | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)` receiver)` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide its stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `static final `[StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata)                                                                                                                                                                                                                                                                               | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `static final `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                                                                                                                                                                                                                                                                                                      | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component4](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its uploadSessionUri.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage)                                                                                                                                                                                 | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[storage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage)                                                                                                                                                                                 | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[storage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance for a custom storage bucket at [url](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)).                                                                                                                                                                                                                                                                                                                                                                                      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage)                                                                                                                                                                                 | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[storage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url` `)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and storage bucket [url](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)). |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata)                                                                                                                                                                                 | [storageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#storageMetadata(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageMetadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns a [StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) object initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)) function.                                                                                                                                                                                                                                                                                                                                                               |

## Public fields

### storage

```
publicÂ finalÂ @NonNull FirebaseStorageÂ storage
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### taskState

```
publicÂ finalÂ @NonNull Flow<@NonNull TaskState<@NonNull T>>Â taskState
```

Starts listening to this task's progress and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, it attaches the following listeners: [OnProgressListener](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener), [OnPausedListener](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener), [OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html).

- When the flow completes the listeners will be removed.

## Public methods

### StorageKt.component1

```
publicÂ staticÂ finalÂ longÂ StorageKt.component1(@NonNull FileDownloadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide bytesTransferred.  

| Returns |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the bytesTransferred of the [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |

### StorageKt.component1

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull StorageReference>Â StorageKt.component1(@NonNull ListResultÂ receiver)
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its items.  

|                                                                                                                                                                                              Returns                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)`>` | the items of the [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) |

### StorageKt.component1

```
publicÂ staticÂ finalÂ longÂ StorageKt.component1(@NonNull StreamDownloadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide bytesTransferred.  

| Returns |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the bytesTransferred of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

### StorageKt.component1

```
publicÂ staticÂ finalÂ longÂ StorageKt.component1(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide bytesTransferred.  

| Returns |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the bytesTransferred of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component2

```
publicÂ staticÂ finalÂ longÂ StorageKt.component2(@NonNull FileDownloadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide totalByteCount.  

| Returns |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the totalByteCount of the [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |

### StorageKt.component2

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull StorageReference>Â StorageKt.component2(@NonNull ListResultÂ receiver)
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its prefixes.  

|                                                                                                                                                                                              Returns                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)`>` | the prefixes of the [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) |

### StorageKt.component2

```
publicÂ staticÂ finalÂ longÂ StorageKt.component2(@NonNull StreamDownloadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide totalByteCount.  

| Returns |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the totalByteCount of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

### StorageKt.component2

```
publicÂ staticÂ finalÂ longÂ StorageKt.component2(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide totalByteCount.  

| Returns |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the totalByteCount of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component3

```
publicÂ staticÂ finalÂ StringÂ StorageKt.component3(@NonNull ListResultÂ receiver)
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) to provide its pageToken.  

|                                    Returns                                     |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html) | the pageToken of the [ListResult](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult) |

### StorageKt.component3

```
publicÂ staticÂ finalÂ @NonNull InputStreamÂ StorageKt.component3(@NonNull StreamDownloadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide its stream.  

|                                                                                        Returns                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | the stream of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

### StorageKt.component3

```
publicÂ staticÂ finalÂ StorageMetadataÂ StorageKt.component3(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its metadata.  

|                                                      Returns                                                      |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) | the metadata of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component4

```
publicÂ staticÂ finalÂ UriÂ StorageKt.component4(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its uploadSessionUri.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | the uploadSessionUri of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.storage

```
publicÂ staticÂ finalÂ @NonNull FirebaseStorageÂ StorageKt.storage(@NonNull FirebaseÂ receiver,Â @NonNull FirebaseAppÂ app)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### StorageKt.storage

```
publicÂ staticÂ finalÂ @NonNull FirebaseStorageÂ StorageKt.storage(@NonNull FirebaseÂ receiver,Â @NonNull StringÂ url)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance for a custom storage bucket at [url](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)).  

### StorageKt.storage

```
publicÂ staticÂ finalÂ @NonNull FirebaseStorageÂ StorageKt.storage(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull StringÂ url
)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and storage bucket [url](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)).  

### storageMetadata

```
publicÂ staticÂ finalÂ @NonNull StorageMetadataÂ storageMetadata(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull StorageMetadata.Builder,Â Unit>Â init
)
```

Returns a [StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) object initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)) function.