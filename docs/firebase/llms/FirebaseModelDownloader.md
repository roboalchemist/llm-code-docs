# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader.md.txt

# FirebaseModelDownloader

# FirebaseModelDownloader


```
class FirebaseModelDownloader
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                           | [deleteDownloadedModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#deleteDownloadedModel(java.lang.String))`(modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Deletes the local model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `java-static `[FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader)                                                                                                                                                                                                                                                                 | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance())`()` Returns the [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                            |
| `java-static `[FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader)                                                                                                                                                                                                                                                                 | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getInstance(com.google.firebase.FirebaseApp))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Returns the [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>`                                                                                                                                                                                                  | [getModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModel(java.lang.String,com.google.firebase.ml.modeldownloader.DownloadType,com.google.firebase.ml.modeldownloader.CustomModelDownloadConditions))`(` ` modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` downloadType: `[DownloadType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType)`,` ` conditions: `[CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions)`?` `)` Gets the downloaded model file based on download type and conditions. |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`!>`                                                                                                                                                                                                                                         | [getModelDownloadId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#getModelDownloadId(java.lang.String,com.google.android.gms.tasks.Task<com.google.firebase.ml.modeldownloader.CustomModel>))`(modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, getModelTask: `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>?)` Gets the current model's download ID (returns background download ID when applicable).                                                                                  |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)`)`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>!>` | [listDownloadedModels](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#listDownloadedModels())`()` Lists all models downloaded to device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                                                                                                                              | [setModelDownloaderCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#setModelDownloaderCollectionEnabled(java.lang.Boolean))`(enabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?)` Enables stats collection in Firebase ML ModelDownloader via Firelog.                                                                                                                                                                                                                                                                                                                                                                                               |

|                                                         ### Public properties                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomModel.Factory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.Factory)`!` | [modelFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader#modelFactory()) |

## Public functions

### deleteDownloadedModel

```
funÂ deleteDownloadedModel(modelName:Â String):Â Task<Void!>
```

Deletes the local model. Removes any information and files associated with the model name.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|--------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Name of the model. |

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseModelDownloader
```

Returns the [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                                                   Returns                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) | A [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) instance |

### getInstance

```
java-staticÂ funÂ getInstance(app:Â FirebaseApp):Â FirebaseModelDownloader
```

Returns the [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                               Parameters                                                |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) | A custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) |

|                                                                   Returns                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) | A [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader) instance |

### getModel

```
funÂ getModel(
Â Â Â Â modelName:Â String,
Â Â Â Â downloadType:Â DownloadType,
Â Â Â Â conditions:Â CustomModelDownloadConditions?
):Â Task<CustomModel!>
```

Gets the downloaded model file based on download type and conditions. DownloadType behaviours:

- [LOCAL_MODEL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL): returns the current model if present, otherwise triggers new download (or finds one in progress) and only completes when download is finished
- [LOCAL_MODEL_UPDATE_IN_BACKGROUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND): returns the current model if present and triggers an update to fetch a new version in the background. If no local model is present triggers a new download (or finds one in progress) and only completes when download is finished.
- [LATEST_MODEL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL): returns the latest model. Checks if latest model is different from local model. If the models are the same, returns the current model. Otherwise, triggers a new model download and returns when this download finishes.

Most common exceptions include:

<!-- -->

- [NO_NETWORK_CONNECTION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NO_NETWORK_CONNECTION()): Error connecting to the network.
- [NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_FOUND()): No model found with the given name.
- [NOT_ENOUGH_SPACE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_ENOUGH_SPACE()): Not enough space on device to download model.
- [DOWNLOAD_URL_EXPIRED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DOWNLOAD_URL_EXPIRED()): URL used to fetch model expired before model download completed. (This return is rare; these calls are retried internally before being raised.)

|                                                                                Parameters                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                            | Model name.                                                                                                                                                                              |
| `downloadType: `[DownloadType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType)                                    | [DownloadType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType) to determine which model to return.                                |
| `conditions: `[CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions)`?` | [CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions) to be used during file download. |

|                                                                                                         Returns                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>` | Custom model |

### getModelDownloadId

```
funÂ getModelDownloadId(modelName:Â String,Â getModelTask:Â Task<CustomModel!>?):Â Task<Long!>
```

Gets the current model's download ID (returns background download ID when applicable). This ID can be used to create a progress bar to track file download progress.

\[Preferred\] If getModelTask is not null, then this task returns when the download ID is not 0 (download has been enqueued) or when the getModelTask completes (returning 0).

If getModelTask is null, then this task immediately returns the download ID of the model. This will be 0 if the model doesn't exist, the model has completed downloading, or the download hasn't been enqueued.  

|                                                                                                                Parameters                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| `modelName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                             | Model name.                                                   |
| `getModelTask: `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>?` | The most recent getModel task associated with the model name. |

|                                                                                      Returns                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`!>` | Download ID associated with Android `DownloadManager`. |

### listDownloadedModels

```
funÂ listDownloadedModels():Â Task<(Mutable)Set<CustomModel!>!>
```

Lists all models downloaded to device.  

|                                                                                                                                                                                                          Returns                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)`)`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)`<`[CustomModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel)`!>!>` | The set of all models that are downloaded to this device. |

### setModelDownloaderCollectionEnabled

```
funÂ setModelDownloaderCollectionEnabled(enabled:Â Boolean?):Â Unit
```

Enables stats collection in Firebase ML ModelDownloader via Firelog. The stats include API calls counts, errors, API call durations, options, etc. No personally identifiable information is logged.

The setting is set by the initialization of `FirebaseApp`, and it is persistent together with the app's private data. It means that if the user uninstalls the app or clears all app data, the setting will be erased. The best practice is to set the flag in each initialization.

By default, the logging matches the Firebase-wide data collection switch.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `enabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?` | Turns the logging state on or off. To revert to using the Firebase-wide data collection switch, set this value to `null`. |

## Public properties

### modelFactory

```
valÂ modelFactory:Â CustomModel.Factory!
```