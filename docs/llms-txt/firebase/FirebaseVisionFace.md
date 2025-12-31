# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace.md.txt

# FirebaseVisionFace

public class **FirebaseVisionFace** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represents a face detected by [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector).  

### Constant Summary

|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| int   | [INVALID_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#INVALID_ID)                         | Invalid tracking ID.                     |
| float | [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY) | Default value for certain face features. |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                     | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getBoundingBox())() Returns the axis-aligned bounding rectangle of the detected face.                                                                                                                                                               |
| [FirebaseVisionFaceContour](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour)   | [getContour](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getContour(int))(int contourType) Gets contour based on the provided [FirebaseVisionFaceContour.ContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.ContourType) type.         |
| float                                                                                                                                          | [getHeadEulerAngleY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getHeadEulerAngleY())() Returns the rotation of the face about the vertical axis of the image.                                                                                                                                                  |
| float                                                                                                                                          | [getHeadEulerAngleZ](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getHeadEulerAngleZ())() Returns the rotation of the face about the axis pointing out of the image.                                                                                                                                              |
| [FirebaseVisionFaceLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark) | [getLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getLandmark(int))(int landmarkType) Gets landmark based on the provided [FirebaseVisionFaceLandmark.LandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.LandmarkType) type. |
| float                                                                                                                                          | [getLeftEyeOpenProbability](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getLeftEyeOpenProbability())() Returns a value between 0.0 and 1.0 giving a probability that the face's left eye is open.                                                                                                                |
| float                                                                                                                                          | [getRightEyeOpenProbability](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getRightEyeOpenProbability())() Returns a value between 0.0 and 1.0 giving a probability that the face's right eye is open.                                                                                                             |
| float                                                                                                                                          | [getSmilingProbability](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getSmilingProbability())() Returns a value between 0.0 and 1.0 giving a probability that the face is smiling.                                                                                                                                |
| int                                                                                                                                            | [getTrackingId](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getTrackingId())() Returns the tracking ID if the tracking is enabled.                                                                                                                                                                               |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                        | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#toString())()                                                                                                                                                                                                                                             |

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
**INVALID_ID**

Invalid tracking ID.  
Constant Value: -1  

#### public static final float
**UNCOMPUTED_PROBABILITY**

Default value for certain face features. See [getRightEyeOpenProbability()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getRightEyeOpenProbability()), [getLeftEyeOpenProbability()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getLeftEyeOpenProbability()), [getSmilingProbability()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getSmilingProbability()).  
Constant Value: -1.0

## Public Methods

#### public [Rect](https://developer.android.com/reference/android/graphics/Rect.html) **getBoundingBox** ()

Returns the axis-aligned bounding rectangle of the detected face.  

#### public [FirebaseVisionFaceContour](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour) **getContour** (int contourType)

Gets contour based on the provided [FirebaseVisionFaceContour.ContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.ContourType) type. If the contour is not available,
it would contain an empty point list.  

#### public float **getHeadEulerAngleY** ()

Returns the rotation of the face about the vertical axis of the image. Positive
euler y is when the face turns toward the right side of the image that is being
processed.  

##### Returns

- the rotation of the face about the vertical axis of the image  

#### public float **getHeadEulerAngleZ** ()

Returns the rotation of the face about the axis pointing out of the image. Positive
euler z is a counter-clockwise rotation within the image plane.  

#### public [FirebaseVisionFaceLandmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark) **getLandmark** (int landmarkType)

Gets landmark based on the provided [FirebaseVisionFaceLandmark.LandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.LandmarkType) type. It returns null if the
landmark type is not available.  

#### public float **getLeftEyeOpenProbability** ()

Returns a value between 0.0 and 1.0 giving a probability that the face's left eye is
open. Otherwise, return [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY)

This returns [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY) if the probability was not computed. The probability
is not computed if eye open classification is not enabled via [setClassificationMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setClassificationMode(int)) or the feature is not available.  

#### public float **getRightEyeOpenProbability** ()

Returns a value between 0.0 and 1.0 giving a probability that the face's right eye
is open. Otherwise, return [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY)

See also [getLeftEyeOpenProbability()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#getLeftEyeOpenProbability()).  

#### public float **getSmilingProbability** ()

Returns a value between 0.0 and 1.0 giving a probability that the face is smiling.
Otherwise, return [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY)

This returns [UNCOMPUTED_PROBABILITY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#UNCOMPUTED_PROBABILITY) if the probability was not computed. The probability
is not computed if smile classification is not enabled via [setClassificationMode(int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setClassificationMode(int)) or the required landmarks are not found.  

#### public int **getTrackingId** ()

Returns the tracking ID if the tracking is enabled. Otherwise, returns
[INVALID_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace#INVALID_ID);  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()