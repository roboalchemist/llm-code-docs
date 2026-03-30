# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader.md.txt

# FirebaseModelDownloader

# FirebaseModelDownloader


```
public class FirebaseModelDownloader
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel.Factory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#modelFactory()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#deleteDownloadedModel(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName)` Deletes the local model. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModel(java.lang.String,com.google.firebase.ml.modeldownloader.DownloadType,com.google.firebase.ml.modeldownloader.CustomModelDownloadConditions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType downloadType, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions conditions )` Gets the downloaded model file based on download type and conditions. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Long.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModelDownloadId(java.lang.String,com.google.android.gms.tasks.Task<com.google.firebase.ml.modeldownloader.CustomModel>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel> getModelTask )` Gets the current model's download ID (returns background download ID when applicable). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/util/Set.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#listDownloadedModels()()` Lists all models downloaded to device. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#setModelDownloaderCollectionEnabled(java.lang.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html enabled)` Enables stats collection in Firebase ML ModelDownloader via Firelog. |

## Public fields

### modelFactory

```
public final CustomModel.Factory modelFactory
```

## Public methods

### deleteDownloadedModel

```
public @NonNull Task<Void> deleteDownloadedModel(@NonNull String modelName)
```

Deletes the local model. Removes any information and files associated with the model name.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | Name of the model. |

### getInstance

```
public static @NonNull FirebaseModelDownloader getInstance()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance |

### getInstance

```
public static @NonNull FirebaseModelDownloader getInstance(@NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | A custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance |

### getModel

```
public @NonNull Task<CustomModel> getModel(
    @NonNull String modelName,
    @NonNull DownloadType downloadType,
    @Nullable CustomModelDownloadConditions conditions
)
```

Gets the downloaded model file based on download type and conditions. DownloadType behaviours:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL`: returns the current model if present, otherwise triggers new download (or finds one in progress) and only completes when download is finished
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND`: returns the current model if present and triggers an update to fetch a new version in the background. If no local model is present triggers a new download (or finds one in progress) and only completes when download is finished.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL`: returns the latest model. Checks if latest model is different from local model. If the models are the same, returns the current model. Otherwise, triggers a new model download and returns when this download finishes.

Most common exceptions include:

<!-- -->

- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseMlException#NO_NETWORK_CONNECTION()`: Error connecting to the network.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_FOUND()`: No model found with the given name.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_ENOUGH_SPACE()`: Not enough space on device to download model.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseMlException#DOWNLOAD_URL_EXPIRED()`: URL used to fetch model expired before model download completed. (This return is rare; these calls are retried internally before being raised.)

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | Model name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType downloadType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType` to determine which model to return. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions conditions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` to be used during file download. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel>` | Custom model |

### getModelDownloadId

```
public @NonNull Task<Long> getModelDownloadId(
    @NonNull String modelName,
    @Nullable Task<CustomModel> getModelTask
)
```

Gets the current model's download ID (returns background download ID when applicable). This ID can be used to create a progress bar to track file download progress.

\[Preferred\] If getModelTask is not null, then this task returns when the download ID is not 0 (download has been enqueued) or when the getModelTask completes (returning 0).

If getModelTask is null, then this task immediately returns the download ID of the model. This will be 0 if the model doesn't exist, the model has completed downloading, or the download hasn't been enqueued.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html modelName` | Model name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel> getModelTask` | The most recent getModel task associated with the model name. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Long.html>` | Download ID associated with Android `DownloadManager`. |

### listDownloadedModels

```
public @NonNull Task<Set<CustomModel>> listDownloadedModels()
```

Lists all models downloaded to device.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/util/Set.html<https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel>>` | The set of all models that are downloaded to this device. |

### setModelDownloaderCollectionEnabled

```
public void setModelDownloaderCollectionEnabled(@Nullable Boolean enabled)
```

Enables stats collection in Firebase ML ModelDownloader via Firelog. The stats include API calls counts, errors, API call durations, options, etc. No personally identifiable information is logged.

The setting is set by the initialization of `FirebaseApp`, and it is persistent together with the app's private data. It means that if the user uninstalls the app or clears all app data, the setting will be erased. The best practice is to set the flag in each initialization.

By default, the logging matches the Firebase-wide data collection switch.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html enabled` | Turns the logging state on or off. To revert to using the Firebase-wide data collection switch, set this value to `null`. |