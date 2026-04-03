# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder.md.txt

# FirebaseVisionObjectDetectorOptions.Builder

public static class **FirebaseVisionObjectDetectorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder of [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions).  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder#FirebaseVisionObjectDetectorOptions.Builder())() |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder#build())() Builds a [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions).                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) | [enableClassification](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder#enableClassification())() Enable on-device coarse classification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) | [enableMultipleObjects](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder#enableMultipleObjects())() Enable multiple objects for detection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) | [setDetectorMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder#setDetectorMode(int))(int detectorMode) Sets the [FirebaseVisionObjectDetectorOptions.DetectorMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.DetectorMode), which contains two modes, [STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE) and [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE). |

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

#### public **FirebaseVisionObjectDetectorOptions.Builder** ()

## Public Methods

#### public [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions) **build** ()

Builds a [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions).  

#### public [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) **enableClassification** ()

Enable on-device coarse classification. The classification categories are defined in
[FirebaseVisionObject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject).

By default, the coarse classification is off.  

#### public [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) **enableMultipleObjects** ()

Enable multiple objects for detection. The number of objects is no more than 5.

By default, it is prominent object only.  

#### public [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) **setDetectorMode** (int detectorMode)

Sets the [FirebaseVisionObjectDetectorOptions.DetectorMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.DetectorMode), which contains two modes,
[STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE) and [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE). For more details, please see comments for [STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE) and [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE).

By default, it is [STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE).