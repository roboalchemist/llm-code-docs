# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.md.txt

# FirebaseVisionCloudDetectorOptions

public class **FirebaseVisionCloudDetectorOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Options for all cloud vision detectors (e.g. text, landmark, label).  

### Nested Class Summary

|------------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) || Builder of [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions).                                                                                                                                                                           |
| @interface | [FirebaseVisionCloudDetectorOptions.ModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.ModelType) || Model types for cloud vision APIs: [STABLE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#STABLE_MODEL) and [LATEST_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#LATEST_MODEL). |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| int | [LATEST_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#LATEST_MODEL) | Latest model would be used. |
| int | [STABLE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#STABLE_MODEL) | Stable model would be used. |

### Field Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| public static final [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) | [DEFAULT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#DEFAULT) | Default options for Firebase vision cloud detector. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) | [builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#builder())() Creates a new builder for [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions). |
| boolean                                                                                                                                                                         | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                                                                     |
| int                                                                                                                                                                             | [getMaxResults](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#getMaxResults())() Gets maximum number of results to be detected.                                                                                                                                 |
| int                                                                                                                                                                             | [getModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#getModelType())() Gets the detector model type.                                                                                                                                                    |
| int                                                                                                                                                                             | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#hashCode())()                                                                                                                                                                                          |

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

## Constants

#### public static final int
**LATEST_MODEL**

Latest model would be used.  
Constant Value: 2  

#### public static final int
**STABLE_MODEL**

Stable model would be used.  
Constant Value: 1

## Fields

#### public static final FirebaseVisionCloudDetectorOptions **DEFAULT**

Default options for Firebase vision cloud detector. The max result size is 10, and
the model is [STABLE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#STABLE_MODEL).

## Public Methods

#### public [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) **builder** ()

Creates a new builder for [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions).  

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public int **getMaxResults** ()

Gets maximum number of results to be detected.  

#### public int **getModelType** ()

Gets the detector model type. It is either [LATEST_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#LATEST_MODEL) or [STABLE_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions#STABLE_MODEL).  

#### public int **hashCode** ()