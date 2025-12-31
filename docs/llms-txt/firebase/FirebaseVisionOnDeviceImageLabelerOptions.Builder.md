# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder.md.txt

# FirebaseVisionOnDeviceImageLabelerOptions.Builder

public static class **FirebaseVisionOnDeviceImageLabelerOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions).  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionOnDeviceImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder#FirebaseVisionOnDeviceImageLabelerOptions.Builder())() |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder#build())()                                                                                                               |
| [FirebaseVisionOnDeviceImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder) | [setConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder#setConfidenceThreshold(float))(float confidenceThreshold) Sets confidence threshold of detected labels. |

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

#### public **FirebaseVisionOnDeviceImageLabelerOptions.Builder**
()

## Public Methods

#### public [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions) **build** ()

#### public [FirebaseVisionOnDeviceImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions.Builder) **setConfidenceThreshold** (float confidenceThreshold)

Sets confidence threshold of detected labels. Only labels detected with confidence
higher than this threshold are returned.

Default is 0.5.  

##### Throws

| [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if the `confidenceThreshold` is out of the range \[0.0f, 1.0f\]. |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|