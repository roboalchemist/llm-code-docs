# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource.md.txt

# FirebaseCloudModelSource

public class **FirebaseCloudModelSource** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
The model source for cloud models.

The model source defines the download conditions of the model, whether or not to download
updated versions of the model, and the model's name specified by the developer in the cloud
console.  

### Nested Class Summary

|-------|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource.Builder) || Builder of [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource). |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                                                   | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)        |
| [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions) | [getInitialDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#getInitialDownloadConditions())() Gets the conditions for the initial model download. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                   | [getModelName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#getModelName())() Gets the model name.                                                                |
| [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions) | [getUpdatesDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#getUpdatesDownloadConditions())() Gets the conditions for downloading model updates.  |
| int                                                                                                                                                       | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#hashCode())()                                                                                             |
| boolean                                                                                                                                                   | [isModelUpdatesEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource#isModelUpdatesEnabled())() Indicates whether the model updates are enabled.                  |

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

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions) **getInitialDownloadConditions** ()

Gets the conditions for the initial model download.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getModelName** ()

Gets the model name.  

#### public [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions) **getUpdatesDownloadConditions** ()

Gets the conditions for downloading model updates. Note the conditions will be
ignored unless model updates are enabled.  

#### public int **hashCode** ()

#### public boolean **isModelUpdatesEnabled** ()

Indicates whether the model updates are enabled.

If false, SDK would still download the first model under initial download
conditions, and would not update the model any more.

If true, SDK would check model updates and download the models even if there is
already a downloaded model.