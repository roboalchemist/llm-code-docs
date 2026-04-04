# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder.md.txt

# FirebaseVisionLabelDetectorOptions.Builder

public static class **FirebaseVisionLabelDetectorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionLabelDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionLabelDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder#FirebaseVisionLabelDetectorOptions.Builder())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionLabelDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder#build())()                                                                                                               |
| [FirebaseVisionLabelDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder) | [setConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder#setConfidenceThreshold(float))(float confidenceThreshold) Sets confidence threshold of detected labels. |

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

#### public **FirebaseVisionLabelDetectorOptions.Builder** ()

## Public Methods

#### public [FirebaseVisionLabelDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions) **build** ()

#### public [FirebaseVisionLabelDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetectorOptions.Builder) **setConfidenceThreshold** (float confidenceThreshold)

Sets confidence threshold of detected labels. Only labels detected with confidence
higher than this threshold are returned.

Default is 0.5.  

##### Throws

| [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if the `confidenceThreshold` is out of the range \[0.0f, 1.0f\]. |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|