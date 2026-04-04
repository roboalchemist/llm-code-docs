# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.md.txt

# FirebaseVisionObjectDetectorOptions

public class **FirebaseVisionObjectDetectorOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Options for [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector).  

### Nested Class Summary

|------------|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionObjectDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.Builder) || Builder of [FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions). |
| @interface | [FirebaseVisionObjectDetectorOptions.DetectorMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions.DetectorMode) || The detector mode which indicates whether detection is for single image or for streaming.                                                                                       |

### Constant Summary

|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| int | [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE) | It is designed for single images where the detection of each image is independent. |
| int | [STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE)             | It is designed for streaming frames from video or camera.                          |

### Public Method Summary

|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| int     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#hashCode())()                                                                                      |

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
**SINGLE_IMAGE_MODE**

It is designed for single images where the detection of each image is independent.
In this mode, the detector would return detection results slower than [STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE).  
Constant Value: 2  

#### public static final int
**STREAM_MODE**

It is designed for streaming frames from video or camera. In this mode, the detector
would return the detection results faster than [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE), since it leverages the detection results from previous
images. Therefore, it may not return results for a new object in the first few frames
after a new object appears in the images, since there is no previous result about this
object to help.

Note that if the time-interval between two consecutive frames is too large, say
several hundred milliseconds, the previous detected objects would be lost and all
objects would be treated as new objects.  
Constant Value: 1

## Public Methods

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public int **hashCode** ()