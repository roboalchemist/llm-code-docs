# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.md.txt

# FirebaseVisionFaceLandmark

public class **FirebaseVisionFaceLandmark** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represent a face landmark. A landmark is a point on a detected face, such as an eye, nose,
or mouth.

When 'left' and 'right' are used, they are relative to the subject in the image. For
example, the [LEFT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#LEFT_EYE) landmark is the subject's left eye, not the eye that is on the left when
viewing the image.  

### Nested Class Summary

|------------|---|---|--------------------------|
| @interface | [FirebaseVisionFaceLandmark.LandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.LandmarkType) || Landmark types for face. |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| int | [LEFT_CHEEK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#LEFT_CHEEK)     | The midpoint between the subject's left mouth corner and the outer corner of the subject's left eye.   |
| int | [LEFT_EAR](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#LEFT_EAR)         | The midpoint of the subject's left ear tip and left ear lobe.                                          |
| int | [LEFT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#LEFT_EYE)         | The center of the subject's left eye cavity.                                                           |
| int | [MOUTH_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#MOUTH_BOTTOM) | The center of the subject's bottom lip.                                                                |
| int | [MOUTH_LEFT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#MOUTH_LEFT)     | The subject's left mouth corner where the lips meet.                                                   |
| int | [MOUTH_RIGHT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#MOUTH_RIGHT)   | The subject's right mouth corner where the lips meet.                                                  |
| int | [NOSE_BASE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#NOSE_BASE)       | The midpoint between the subject's nostrils where the nose meets the face.                             |
| int | [RIGHT_CHEEK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#RIGHT_CHEEK)   | The midpoint between the subject's right mouth corner and the outer corner of the subject's right eye. |
| int | [RIGHT_EAR](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#RIGHT_EAR)       | The midpoint of the subject's right ear tip and right ear lobe.                                        |
| int | [RIGHT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#RIGHT_EYE)       | The center of the subject's right eye cavity.                                                          |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                                                                                | [getLandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#getLandmarkType())() Gets the [FirebaseVisionFaceLandmark.LandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.LandmarkType) type. |
| [FirebaseVisionPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint) | [getPosition](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#getPosition())() Gets a 2D point for landmark position, where (0, 0) is the upper-left corner of the image.                                                                                                      |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                            | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark#toString())()                                                                                                                                                                                                       |

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
**LEFT_CHEEK**

The midpoint between the subject's left mouth corner and the outer corner of the
subject's left eye. For full profile faces, this becomes the centroid of the nose base,
nose tip, left ear lobe and left ear tip.  
Constant Value: 1  

#### public static final int
**LEFT_EAR**

The midpoint of the subject's left ear tip and left ear lobe.  
Constant Value: 3  

#### public static final int
**LEFT_EYE**

The center of the subject's left eye cavity.  
Constant Value: 4  

#### public static final int
**MOUTH_BOTTOM**

The center of the subject's bottom lip.  
Constant Value: 0  

#### public static final int
**MOUTH_LEFT**

The subject's left mouth corner where the lips meet.  
Constant Value: 5  

#### public static final int
**MOUTH_RIGHT**

The subject's right mouth corner where the lips meet.  
Constant Value: 11  

#### public static final int
**NOSE_BASE**

The midpoint between the subject's nostrils where the nose meets the face.  
Constant Value: 6  

#### public static final int
**RIGHT_CHEEK**

The midpoint between the subject's right mouth corner and the outer corner of the
subject's right eye. For full profile faces, this becomes the centroid of the nose
base, nose tip, right ear lobe and right ear tip.  
Constant Value: 7  

#### public static final int
**RIGHT_EAR**

The midpoint of the subject's right ear tip and right ear lobe.  
Constant Value: 9  

#### public static final int
**RIGHT_EYE**

The center of the subject's right eye cavity.  
Constant Value: 10

## Public Methods

#### public int **getLandmarkType** ()

Gets the [FirebaseVisionFaceLandmark.LandmarkType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceLandmark.LandmarkType) type.  

#### public [FirebaseVisionPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint)
**getPosition** ()

Gets a 2D point for landmark position, where (0, 0) is the upper-left corner of the
image. The point is guaranteed to be within the bounds of the image.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()