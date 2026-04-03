# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder.md.txt

# FirebaseModelOptions.Builder

public static class **FirebaseModelOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions).  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder#FirebaseModelOptions.Builder())() Creates a new builder to build [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions). |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder#build())() Builds a `FirebaseModelOptions`.                                                                                                                                                                                                                                                           |
| [FirebaseModelOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder) | [setLocalModelName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder#setLocalModelName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) localModelName) Sets a local model name to [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions).    |
| [FirebaseModelOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder) | [setRemoteModelName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder#setRemoteModelName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) remoteModelName) Sets a cloud model name to [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions). |

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

#### public **FirebaseModelOptions.Builder** ()

Creates a new builder to build [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions).

## Public Methods

#### public [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions)
**build** ()

Builds a `FirebaseModelOptions`.  

#### public [FirebaseModelOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder)
**setLocalModelName** ([String](https://developer.android.com/reference/java/lang/String.html) localModelName)

Sets a local model name to [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions).
Note local model has a lower priority than the cloud model, if specified. It will only
be used if there is no [FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) or the download of [FirebaseRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseRemoteModel) fails.  

#### public [FirebaseModelOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions.Builder)
**setRemoteModelName** ([String](https://developer.android.com/reference/java/lang/String.html) remoteModelName)

Sets a cloud model name to [FirebaseModelOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOptions).
Once set, it has higher priority than the local model. If you would like to use local
model, do not assign cloud model source.

It would trigger a model downloading if there is no previous downloaded model under
the given model name, or the model in cloud is different from the latest downloaded
model on device.