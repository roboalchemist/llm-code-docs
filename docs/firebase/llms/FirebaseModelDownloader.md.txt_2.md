# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader.md.txt

# FirebaseModelDownloader

# FirebaseModelDownloader


```
class FirebaseModelDownloader
```

<br />

*** ** * ** ***

## Summary

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#deleteDownloadedModel(java.lang.String)(modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Deletes the local model. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModel(java.lang.String,com.google.firebase.ml.modeldownloader.DownloadType,com.google.firebase.ml.modeldownloader.CustomModelDownloadConditions)( modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, downloadType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType, conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions? )` Gets the downloaded model file based on download type and conditions. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModelDownloadId(java.lang.String,com.google.android.gms.tasks.Task<com.google.firebase.ml.modeldownloader.CustomModel>)(modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, getModelTask: https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>?)` Gets the current model's download ID (returns background download ID when applicable). |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#listDownloadedModels()()` Lists all models downloaded to device. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#setModelDownloaderCollectionEnabled(java.lang.Boolean)(enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?)` Enables stats collection in Firebase ML ModelDownloader via Firelog. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.Factory!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#modelFactory()` |

## Public functions

### deleteDownloadedModel

```
fun deleteDownloadedModel(modelName: String): Task<Void!>
```

Deletes the local model. Removes any information and files associated with the model name.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of the model. |

### getInstance

```
java-static fun getInstance(): FirebaseModelDownloader
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance |

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseModelDownloader
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | A custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance |

### getModel

```
fun getModel(
    modelName: String,
    downloadType: DownloadType,
    conditions: CustomModelDownloadConditions?
): Task<CustomModel!>
```

Gets the downloaded model file based on download type and conditions. DownloadType behaviours:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL`: returns the current model if present, otherwise triggers new download (or finds one in progress) and only completes when download is finished
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND`: returns the current model if present and triggers an update to fetch a new version in the background. If no local model is present triggers a new download (or finds one in progress) and only completes when download is finished.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL`: returns the latest model. Checks if latest model is different from local model. If the models are the same, returns the current model. Otherwise, triggers a new model download and returns when this download finishes.

Most common exceptions include:

<!-- -->

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NO_NETWORK_CONNECTION()`: Error connecting to the network.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_FOUND()`: No model found with the given name.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_ENOUGH_SPACE()`: Not enough space on device to download model.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DOWNLOAD_URL_EXPIRED()`: URL used to fetch model expired before model download completed. (This return is rare; these calls are retried internally before being raised.)

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Model name. |
| `downloadType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType` to determine which model to return. |
| `conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` to be used during file download. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>` | Custom model |

### getModelDownloadId

```
fun getModelDownloadId(modelName: String, getModelTask: Task<CustomModel!>?): Task<Long!>
```

Gets the current model's download ID (returns background download ID when applicable). This ID can be used to create a progress bar to track file download progress.

\[Preferred\] If getModelTask is not null, then this task returns when the download ID is not 0 (download has been enqueued) or when the getModelTask completes (returning 0).

If getModelTask is null, then this task immediately returns the download ID of the model. This will be 0 if the model doesn't exist, the model has completed downloading, or the download hasn't been enqueued.

| Parameters |
|---|---|
| `modelName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Model name. |
| `getModelTask: https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>?` | The most recent getModel task associated with the model name. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html!>` | Download ID associated with Android `DownloadManager`. |

### listDownloadedModels

```
fun listDownloadedModels(): Task<(Mutable)Set<CustomModel!>!>
```

Lists all models downloaded to device.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel!>!>` | The set of all models that are downloaded to this device. |

### setModelDownloaderCollectionEnabled

```
fun setModelDownloaderCollectionEnabled(enabled: Boolean?): Unit
```

Enables stats collection in Firebase ML ModelDownloader via Firelog. The stats include API calls counts, errors, API call durations, options, etc. No personally identifiable information is logged.

The setting is set by the initialization of `FirebaseApp`, and it is persistent together with the app's private data. It means that if the user uninstalls the app or clears all app data, the setting will be erased. The best practice is to set the flag in each initialization.

By default, the logging matches the Firebase-wide data collection switch.

| Parameters |
|---|---|
| `enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | Turns the logging state on or off. To revert to using the Firebase-wide data collection switch, set this value to `null`. |

## Public properties

### modelFactory

```
val modelFactory: CustomModel.Factory!
```