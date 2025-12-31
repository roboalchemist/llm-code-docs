# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder.md.txt

# FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder

public static class **FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions).  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder#FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(com.google.firebase.ml.vision.automl.FirebaseAutoMLLocalModel))([FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel) localModel) Creates a new builder to build [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) with a local model [FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel).        |
|   | [FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder#FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder(com.google.firebase.ml.vision.automl.FirebaseAutoMLRemoteModel))([FirebaseAutoMLRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel) remoteModel) Creates a new builder to build [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) with a remote model [FirebaseAutoMLRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel). |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder#build())()                                                                                                                   |
| [FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder) | [setConfidenceThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder#setConfidenceThreshold(float))(float confidenceThreshold) Sets the confidence threshold of detected labels. |

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

#### public **FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder**
([FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel) localModel)

Creates a new builder to build [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) with a local model
[FirebaseAutoMLLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLLocalModel).  

#### public **FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder**
([FirebaseAutoMLRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel) remoteModel)

Creates a new builder to build [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) with a remote model
[FirebaseAutoMLRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/automl/FirebaseAutoMLRemoteModel).

## Public Methods

#### public [FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) **build** ()

#### public [FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions.Builder) **setConfidenceThreshold** (float confidenceThreshold)

Sets the confidence threshold of detected labels. Only labels detected with
confidence higher than or equal to this threshold are returned.

Default is 0.5f.  

##### Throws

| [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if the `confidenceThreshold` is out of the range \[0.0f, 1.0f\]. |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|