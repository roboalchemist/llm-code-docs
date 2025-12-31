# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder.md.txt

# FirebaseCloudModelSource.Builder

public static class **FirebaseCloudModelSource.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder#FirebaseCloudModelSource.Builder(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) modelName) Creates a builder for [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource). |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder#build())() Builds an instance of [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource)                                                                                                                                                                                          |
| [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) | [enableModelUpdates](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder#enableModelUpdates(boolean))(boolean enableModelUpdates) Enables the download of model updates.                                                                                                                                                                                                                                                                  |
| [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) | [setInitialDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder#setInitialDownloadConditions(com.google.firebase.ml.common.modeldownload.FirebaseModelDownloadConditions))([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) initialConditions) Sets the conditions for initial model download.        |
| [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) | [setUpdatesDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder#setUpdatesDownloadConditions(com.google.firebase.ml.common.modeldownload.FirebaseModelDownloadConditions))([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) updatesConditions) Sets the conditions for downloading the model updates. |

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

## Public Constructors

#### public **FirebaseCloudModelSource.Builder** ([String](https://developer.android.com/reference/java/lang/String.html) modelName)

Creates a builder for [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource).  

##### Parameters

| modelName | the model name as specified in Firebase Console. |
|-----------|--------------------------------------------------|

## Public Methods

#### public [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource) **build**
()

Builds an instance of [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource)  

#### public [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) **enableModelUpdates** (boolean enableModelUpdates)

Enables the download of model updates.  

#### public [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) **setInitialDownloadConditions** ([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) initialConditions)

Sets the conditions for initial model download.  

#### public [FirebaseCloudModelSource.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseCloudModelSource.Builder) **setUpdatesDownloadConditions** ([FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) updatesConditions)

Sets the conditions for downloading the model updates.