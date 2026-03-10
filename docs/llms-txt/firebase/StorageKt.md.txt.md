# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.md.txt

# StorageKt

# StorageKt


```
public final class StorageKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StorageTask).taskState()` Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

| ### Public methods |
|---|---|
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its items. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its prefixes. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount. |
| `static final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.ListResult).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its pageToken. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream. |
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata. |
| `static final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance for a custom storage bucket at `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and storage bucket `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt#storageMetadata(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` object initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)` function. |

## Public fields

### storage

```
public final @NonNull FirebaseStorage storage
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### taskState

```
public final @NonNull Flow<@NonNull TaskState<@NonNull T>> taskState
```

Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, it attaches the following listeners: `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener`, `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener`, `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html`.

- When the flow completes the listeners will be removed.

## Public methods

### StorageKt.component1

```
public static final long StorageKt.component1(@NonNull FileDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `long` | the bytesTransferred of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |

### StorageKt.component1

```
public static final @NonNull List<@NonNull StorageReference> StorageKt.component1(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its items.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | the items of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |

### StorageKt.component1

```
public static final long StorageKt.component1(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `long` | the bytesTransferred of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### StorageKt.component1

```
public static final long StorageKt.component1(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `long` | the bytesTransferred of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component2

```
public static final long StorageKt.component2(@NonNull FileDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `long` | the totalByteCount of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |

### StorageKt.component2

```
public static final @NonNull List<@NonNull StorageReference> StorageKt.component2(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its prefixes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | the prefixes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |

### StorageKt.component2

```
public static final long StorageKt.component2(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `long` | the totalByteCount of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### StorageKt.component2

```
public static final long StorageKt.component2(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `long` | the totalByteCount of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component3

```
public static final String StorageKt.component3(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its pageToken.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | the pageToken of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |

### StorageKt.component3

```
public static final @NonNull InputStream StorageKt.component3(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | the stream of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### StorageKt.component3

```
public static final StorageMetadata StorageKt.component3(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | the metadata of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component4

```
public static final Uri StorageKt.component4(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the uploadSessionUri of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.storage

```
public static final @NonNull FirebaseStorage StorageKt.storage(@NonNull Firebase receiver, @NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### StorageKt.storage

```
public static final @NonNull FirebaseStorage StorageKt.storage(@NonNull Firebase receiver, @NonNull String url)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance for a custom storage bucket at `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)`.

### StorageKt.storage

```
public static final @NonNull FirebaseStorage StorageKt.storage(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String url
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and storage bucket `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)`.

### storageMetadata

```
public static final @NonNull StorageMetadata storageMetadata(
    @ExtensionFunctionType @NonNull Function1<@NonNull StorageMetadata.Builder, Unit> init
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` object initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)` function.