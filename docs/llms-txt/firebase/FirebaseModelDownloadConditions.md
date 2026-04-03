# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseModelDownloadConditions.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.md.txt

# FirebaseModelDownloadConditions

public class **FirebaseModelDownloadConditions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Conditions to download remote models.  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [FirebaseModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions.Builder) || Builder of [FirebaseModelDownloadConditions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions). |

### Public Method Summary

|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| int     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions#hashCode())()                                                                                      |
| boolean | [isChargingRequired](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions#isChargingRequired())()                                                                  |
| boolean | [isDeviceIdleRequired](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions#isDeviceIdleRequired())()                                                              |
| boolean | [isWifiRequired](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/modeldownload/FirebaseModelDownloadConditions#isWifiRequired())()                                                                          |

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

#### public int **hashCode** ()

#### public boolean **isChargingRequired** ()

##### Returns

- true if charging is required for download.  

#### public boolean **isDeviceIdleRequired** ()

##### Returns

- true if device idle is required for download.  

#### public boolean **isWifiRequired** ()

##### Returns

- true if wifi is required for download.