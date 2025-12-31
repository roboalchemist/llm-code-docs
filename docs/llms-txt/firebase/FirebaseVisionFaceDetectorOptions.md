# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.md.txt

# FirebaseVisionFaceDetectorOptions

public class **FirebaseVisionFaceDetectorOptions** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Options for [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector).  

### Nested Class Summary

|------------|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) || Builder class of [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions). |
| @interface | [FirebaseVisionFaceDetectorOptions.ClassificationMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.ClassificationMode) || Indicates whether to run additional classifiers for characterizing attributes such as "smiling" and "eyes open".                                                               |
| @interface | [FirebaseVisionFaceDetectorOptions.ContourMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.ContourMode) || Sets whether to detect contours or not.                                                                                                                                        |
| @interface | [FirebaseVisionFaceDetectorOptions.LandmarkMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.LandmarkMode) || Sets whether to detect no landmarks or all landmarks.                                                                                                                          |
| @interface | [FirebaseVisionFaceDetectorOptions.PerformanceMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.PerformanceMode) || Extended option for controlling additional accuracy / speed trade-offs in performing face detection.                                                                           |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int | [ACCURATE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ACCURATE)                       | Indicates a preference for accuracy in extended settings that may make an accuracy vs.                                                                                   |
| int | [ALL_CLASSIFICATIONS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_CLASSIFICATIONS) | Performs "eyes open" and "smiling" classification.                                                                                                                       |
| int | [ALL_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_CONTOURS)               | Detects [FirebaseVisionFaceContour](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour) for a given face.   |
| int | [ALL_LANDMARKS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_LANDMARKS)             | Detects [FirebaseVisionFaceLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark) for a given face. |
| int | [FAST](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#FAST)                               | Indicates a preference for speed in extended settings that may make an accuracy vs.                                                                                      |
| int | [NO_CLASSIFICATIONS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CLASSIFICATIONS)   | Does not perform classification.                                                                                                                                         |
| int | [NO_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CONTOURS)                 | Does not perform contour detection.                                                                                                                                      |
| int | [NO_LANDMARKS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_LANDMARKS)               | Does not perform landmark detection.                                                                                                                                     |

### Public Method Summary

|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o)                                                         |
| int                                                                     | [getClassificationMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#getClassificationMode())() Gets the classifiers mode for characterizing attributes, such as "smiling" and "eyes open".                        |
| int                                                                     | [getContourMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#getContourMode())() Gets the contour mode for face detection.                                                                                        |
| int                                                                     | [getLandmarkMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#getLandmarkMode())() Gets the landmark mode for face detection.                                                                                     |
| float                                                                   | [getMinFaceSize](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#getMinFaceSize())() Sets the smallest desired face size, expressed as a proportion of the width of the head to the image width.                      |
| int                                                                     | [getPerformanceMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#getPerformanceMode())() Extended option for controlling additional accuracy / speed trade-offs in performing face detection.                     |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#hashCode())()                                                                                                                                              |
| boolean                                                                 | [isTrackingEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#isTrackingEnabled())() Returns if face tracking is enabled, which will maintain a consistent ID for each face when processing consecutive frames. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#toString())()                                                                                                                                              |

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
**ACCURATE**

Indicates a preference for accuracy in extended settings that may make an accuracy
vs. speed trade-off. This will tend to detect more faces and may be more precise in
determining values such as position, at the cost of speed.  
Constant Value: 2  

#### public static final int
**ALL_CLASSIFICATIONS**

Performs "eyes open" and "smiling" classification.  
Constant Value: 2  

#### public static final int
**ALL_CONTOURS**

Detects [FirebaseVisionFaceContour](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour) for a given face. Note that it would return
contours for up to 5 faces  
Constant Value: 2  

#### public static final int
**ALL_LANDMARKS**

Detects [FirebaseVisionFaceLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark) for a given face.  
Constant Value: 2  

#### public static final int
**FAST**

Indicates a preference for speed in extended settings that may make an accuracy vs.
speed trade-off. This will tend to detect fewer faces and may be less precise in
determining values such as position, but will run faster.  
Constant Value: 1  

#### public static final int
**NO_CLASSIFICATIONS**

Does not perform classification.  
Constant Value: 1  

#### public static final int
**NO_CONTOURS**

Does not perform contour detection.  
Constant Value: 1  

#### public static final int
**NO_LANDMARKS**

Does not perform landmark detection.  
Constant Value: 1

## Public Methods

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public int **getClassificationMode** ()

Gets the classifiers mode for characterizing attributes, such as "smiling" and "eyes
open". See [setClassificationMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setClassificationMode(int)).  

#### public int **getContourMode** ()

Gets the contour mode for face detection. See [setContourMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setContourMode(int)).  

#### public int **getLandmarkMode** ()

Gets the landmark mode for face detection. See [setLandmarkMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setLandmarkMode(int)).  

#### public float **getMinFaceSize** ()

Sets the smallest desired face size, expressed as a proportion of the width of the
head to the image width. See [setMinFaceSize(float)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setMinFaceSize(float)).  

#### public int **getPerformanceMode** ()

Extended option for controlling additional accuracy / speed trade-offs in performing
face detection. In general, choosing the more accurate mode will generally result in
longer runtime, whereas choosing the faster mode will generally result in detecting
fewer faces. See [setPerformanceMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setPerformanceMode(int)).  

#### public int **hashCode** ()

#### public boolean **isTrackingEnabled** ()

Returns if face tracking is enabled, which will maintain a consistent ID for each
face when processing consecutive frames. See [enableTracking()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#enableTracking()).  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()