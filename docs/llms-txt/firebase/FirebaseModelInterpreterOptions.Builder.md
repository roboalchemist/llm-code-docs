# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions.Builder.md.txt

# FirebaseModelInterpreterOptions.Builder

public static class **FirebaseModelInterpreterOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelInterpreterOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions.Builder#FirebaseModelInterpreterOptions.Builder(com.google.firebase.ml.custom.FirebaseCustomLocalModel))([FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel) localModel) Creates a new builder to build [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) with a local model [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel).       |
|   | [FirebaseModelInterpreterOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions.Builder#FirebaseModelInterpreterOptions.Builder(com.google.firebase.ml.custom.FirebaseCustomRemoteModel))([FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel) remoteModel) Creates a new builder to build [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) with a cloud model [FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel). |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions.Builder#build())() Builds a `FirebaseModelInterpreterOptions`. |

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

#### public **FirebaseModelInterpreterOptions.Builder** ([FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel) localModel)

Creates a new builder to build [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) with a local model [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel).  

#### public **FirebaseModelInterpreterOptions.Builder** ([FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel) remoteModel)

Creates a new builder to build [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) with a cloud model [FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel).

## Public Methods

#### public [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) **build** ()

Builds a `FirebaseModelInterpreterOptions`.