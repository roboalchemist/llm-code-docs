# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder.md.txt

# FirebaseModelDownloadConditions.Builder

public static class **FirebaseModelDownloadConditions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions).  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder#FirebaseModelDownloadConditions.Builder())() |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder#build())() Builds [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions). |
| [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) | [requireCharging](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder#requireCharging())() Sets whether charging is required.                                                                                                                    |
| [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) | [requireDeviceIdle](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder#requireDeviceIdle())() Sets whether device idle is required.                                                                                                             |
| [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) | [requireWifi](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder#requireWifi())() Sets whether wifi is required.                                                                                                                                |

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

#### public **FirebaseModelDownloadConditions.Builder** ()

## Public Methods

#### public [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions) **build** ()

Builds [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions).  

#### public [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) **requireCharging** ()

Sets whether charging is required. Only works on Android N and above.  

#### public [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) **requireDeviceIdle** ()

Sets whether device idle is required.

Idle mode is a loose definition provided by the system, which means that the device
is not in use, and has not been in use for some time.

Only works on Android N and above.  

#### public [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) **requireWifi** ()

Sets whether wifi is required.