# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager.md.txt

# FirebaseModelManager

public class **FirebaseModelManager** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Manages the remote models.

Before using a remote model, download it with [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager). The model name is the key for a model. The model name should
be consistent with the name of the model that has been uploaded to the Firebase console.

This class is thread safe.  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                                                                                                                            | [deleteDownloadedModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#deleteDownloadedModel(com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel))([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel) Deletes the given `remoteModel` from disk.                                                                                                                                                                                                                                                                     |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>                                                                                                                                                            | [download](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#download(com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel, com.google.firebase.ml.common.modeldownload.FirebaseModelDownloadConditions))([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel, [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) downloadConditions) Initiates the download of `remoteModel` if the download hasn't begun. |
| \<T extends [FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel)\> [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Set](https://developer.android.com/reference/java/util/Set.html)\<T\>\> | [getDownloadedModels](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#getDownloadedModels(java.lang.Class<T>))([Class](https://developer.android.com/reference/java/lang/Class.html)\<T\> modelType) Returns the set of all currently downloaded models of the given `modelType`.                                                                                                                                                                                                                                                                                                                                                     |
| synchronized static [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager)                                                                                                                                                                  | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#getInstance())() Gets an instance of a [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) corresponding to the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) instance.                                                                                                                                                                                                                                             |
| synchronized static [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager)                                                                                                                                                                  | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) firebaseApp) Gets an instance of a [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) corresponding to the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) instance.                                                                                                   |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[File](https://developer.android.com/reference/java/io/File.html)\>                                                                                                                                                              | [getLatestModelFile](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#getLatestModelFile(com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel))([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel) Returns the [File](https://developer.android.com/reference/java/io/File.html) containing the latest model for the remote model name.                                                                                                                                                                                 |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Boolean](https://developer.android.com/reference/java/lang/Boolean.html)\>                                                                                                                                                      | [isModelDownloaded](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager#isModelDownloaded(com.google.firebase.ml.common.modeldownload.FirebaseRemoteModel))([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel) Returns whether the given `remoteModel` is currently downloaded.                                                                                                                                                                                                                                                       |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Methods

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>
**deleteDownloadedModel** ([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel)

Deletes the given `remoteModel` from disk. Does nothing if the model is
not downloaded.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Void](https://developer.android.com/reference/java/lang/Void.html)\>
**download** ([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel, [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) downloadConditions)

Initiates the download of `remoteModel` if the download hasn't begun.

If the model's download is already in progress, the current download task will be
returned.

If the model is already downloaded to the device, and there is no update, the task
will immediately succeed.

If the model is already downloaded to the device, and there is update, a download
for the updated version will be attempted.  

##### Returns

- The task for the `remoteModel` download.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Set](https://developer.android.com/reference/java/util/Set.html)\<T\>\>
**getDownloadedModels** ([Class](https://developer.android.com/reference/java/lang/Class.html)\<T\> modelType)

Returns the set of all currently downloaded models of the given
`modelType`.  

#### public static synchronized [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) **getInstance**
()

Gets an instance of a [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) corresponding to the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)
instance.  

#### public static synchronized [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) **getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) firebaseApp)

Gets an instance of a [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelManager) corresponding to the given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)
instance.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[File](https://developer.android.com/reference/java/io/File.html)\>
**getLatestModelFile** ([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel)

Returns the [File](https://developer.android.com/reference/java/io/File.html) containing the
latest model for the remote model name. If no model file was downloaded yet then the
file will be null.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[Boolean](https://developer.android.com/reference/java/lang/Boolean.html)\>
**isModelDownloaded** ([FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) remoteModel)

Returns whether the given `remoteModel` is currently downloaded.