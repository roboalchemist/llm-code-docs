# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel.md.txt

# CustomModel

# CustomModel


```
public class CustomModel
```

<br />

*** ** * ** ***

Stores information about custom models that are being downloaded or are already downloaded on a device. In the case where an update is available, after the updated model file is fully downloaded, the original model file will be removed once it is safe to do so.

## Summary

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#downloadId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#downloadUrl()` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#downloadUrlExpiry()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#localFilePath()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#modelHash()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#name()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#getDownloadId()()` The download ID (returns 0 if no download in progress), which can be used with the Android `DownloadManager` to query download progress. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/io/File.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#getFile()()` The local model file. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#getModelHash()()` Retrieves the model hash. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#getName()()` Retrieves the model name and identifier. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#getSize()()` The size of the file currently associated with this model. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#toString()()` |

| ### Extension functions |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/io/File.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/ModelDownloaderKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel receiver)` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/ModelDownloaderKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel receiver)` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/ModelDownloaderKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel receiver)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/ModelDownloaderKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component4()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel receiver)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/ModelDownloaderKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component5()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel receiver)` |

## Public fields

### downloadId

```
public final long downloadId
```

### downloadUrl

```
public final String downloadUrl
```

### downloadUrlExpiry

```
public final long downloadUrlExpiry
```

### localFilePath

```
public final String localFilePath
```

### modelHash

```
public final String modelHash
```

### name

```
public final String name
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getDownloadId

```
public long getDownloadId()
```

The download ID (returns 0 if no download in progress), which can be used with the Android `DownloadManager` to query download progress. The retrieved progress information can be used to populate a progress bar, monitor when an updated model is available, etc.

| Returns |
|---|---|
| `long` | The download ID (if download in progress), otherwise returns 0. |

### getFile

```
public @Nullable File getFile()
```

The local model file. If `null` is returned, use the download ID to check the download status.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/io/File.html` | The local file associated with the model. If the original file download is still in progress, returns `null`. If a file update is in progress, returns the last fully downloaded model. |

### getModelHash

```
public @NonNull String getModelHash()
```

Retrieves the model hash.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The model hash |

### getName

```
public @NonNull String getName()
```

Retrieves the model name and identifier.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The name of the model. |

### getSize

```
public long getSize()
```

The size of the file currently associated with this model. If a download is in progress, this will be the size of the current model, not the new model currently being downloaded.

| Returns |
|---|---|
| `long` | The local model size. |

### hashCode

```
public int hashCode()
```

### toString

```
public @NonNull String toString()
```

## Extension functions

### ModelDownloaderKt.component1

```
public final File ModelDownloaderKt.component1(@NonNull CustomModel receiver)
```

### ModelDownloaderKt.component2

```
public final long ModelDownloaderKt.component2(@NonNull CustomModel receiver)
```

### ModelDownloaderKt.component3

```
public final long ModelDownloaderKt.component3(@NonNull CustomModel receiver)
```

### ModelDownloaderKt.component4

```
public final @NonNull String ModelDownloaderKt.component4(@NonNull CustomModel receiver)
```

### ModelDownloaderKt.component5

```
public final @NonNull String ModelDownloaderKt.component5(@NonNull CustomModel receiver)
```