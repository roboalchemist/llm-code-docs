# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder.md.txt

# FirebaseVisionCloudImageLabelerOptions.Builder

public static class **FirebaseVisionCloudImageLabelerOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder#FirebaseVisionCloudImageLabelerOptions.Builder())() |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder#build())()                                                                                                                                                        |
| [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder) | [enforceCertFingerprintMatch](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder#enforceCertFingerprintMatch())() Only allow registered application instances with matching certificate fingerprint to use Cloud Vision API. |
| [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder) | [setConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder#setConfidenceThreshold(float))(float confidenceThreshold) Sets confidence threshold of detected labels.                                          |

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

#### public **FirebaseVisionCloudImageLabelerOptions.Builder**
()

## Public Methods

#### public [FirebaseVisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions) **build** ()

#### public [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder) **enforceCertFingerprintMatch** ()

Only allow registered application instances with matching certificate fingerprint to
use Cloud Vision API.

Do not set this for debug build if you use simulators to test.  

#### public [FirebaseVisionCloudImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions.Builder) **setConfidenceThreshold** (float confidenceThreshold)

Sets confidence threshold of detected labels. Only labels detected with confidence
higher than this threshold are returned.

Default is 0.5.  

##### Throws

| [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if the `confidenceThreshold` is out of the range \[0.0f, 1.0f\]. |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|