# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder.md.txt

# FirebaseVisionCloudDetectorOptions.Builder

public static class **FirebaseVisionCloudDetectorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder#FirebaseVisionCloudDetectorOptions.Builder())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder#build())() Creates a [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) instance. |
| [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) | [enforceCertFingerprintMatch](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder#enforceCertFingerprintMatch())() Only allow registered application instances with matching certificate fingerprint to use Cloud Vision API.                              |
| [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) | [setMaxResults](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder#setMaxResults(int))(int maxResults) Sets maximum number of results of this type.                                                                                                       |
| [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) | [setModelType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder#setModelType(int))(int model) Sets model type for the detection.                                                                                                                        |

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

#### public **FirebaseVisionCloudDetectorOptions.Builder** ()

## Public Methods

#### public [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) **build** ()

Creates a [FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) instance.  

#### public [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) **enforceCertFingerprintMatch** ()

Only allow registered application instances with matching certificate fingerprint to
use Cloud Vision API.

Do not set this for debug build if you use simulators to test.  

#### public [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) **setMaxResults** (int maxResults)

Sets maximum number of results of this type. It will be ignored by [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer).

Default is 10.  

#### public [FirebaseVisionCloudDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions.Builder) **setModelType** (int model)

Sets model type for the detection.

Default is `STABLE_MODEL`.