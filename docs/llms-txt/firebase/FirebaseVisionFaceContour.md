# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.md.txt

# FirebaseVisionFaceContour

public class **FirebaseVisionFaceContour** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represent a face contour. A contour is a list of points on a detected face, such as the
mouth.

When 'left' and 'right' are used, they are relative to the subject in the image. For
example, the [LEFT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LEFT_EYE) landmark is the subject's left eye, not the eye that is on the left when
viewing the image.  

### Nested Class Summary

|------------|---|---|-------------------------|
| @interface | [FirebaseVisionFaceContour.ContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.ContourType) || Contour types for face. |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| int | [ALL_POINTS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#ALL_POINTS)                     | All points of a face contour.                      |
| int | [FACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#FACE)                                 | The outline of the subject's face.                 |
| int | [LEFT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LEFT_EYE)                         | The outline of the subject's left eye cavity.      |
| int | [LEFT_EYEBROW_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LEFT_EYEBROW_BOTTOM)   | The bottom outline of the subject's left eyebrow.  |
| int | [LEFT_EYEBROW_TOP](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LEFT_EYEBROW_TOP)         | The top outline of the subject's left eyebrow.     |
| int | [LOWER_LIP_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LOWER_LIP_BOTTOM)         | The bottom outline of the subject's lower lip.     |
| int | [LOWER_LIP_TOP](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#LOWER_LIP_TOP)               | The top outline of the subject's lower lip.        |
| int | [NOSE_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#NOSE_BOTTOM)                   | The outline of the subject's nose bridge.          |
| int | [NOSE_BRIDGE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#NOSE_BRIDGE)                   | The outline of the subject's nose bridge.          |
| int | [RIGHT_EYE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#RIGHT_EYE)                       | The outline of the subject's right eye cavity.     |
| int | [RIGHT_EYEBROW_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#RIGHT_EYEBROW_BOTTOM) | The bottom outline of the subject's right eyebrow. |
| int | [RIGHT_EYEBROW_TOP](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#RIGHT_EYEBROW_TOP)       | The top outline of the subject's right eyebrow.    |
| int | [UPPER_LIP_BOTTOM](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#UPPER_LIP_BOTTOM)         | The bottom outline of the subject's upper lip.     |
| int | [UPPER_LIP_TOP](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#UPPER_LIP_TOP)               | The top outline of the subject's upper lip.        |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                                                                                                                                                       | [getFaceContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#getFaceContourType())() Gets the [FirebaseVisionFaceContour.ContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.ContourType) type. |
| [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint)\> | [getPoints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#getPoints())() Gets a list of 2D points for this face contour, where (0, 0) is the upper-left corner of the image.                                                                                                   |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                   | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour#toString())()                                                                                                                                                                                                         |

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
**ALL_POINTS**

All points of a face contour.  
Constant Value: 1  

#### public static final int
**FACE**

The outline of the subject's face.  
Constant Value: 2  

#### public static final int
**LEFT_EYE**

The outline of the subject's left eye cavity.  
Constant Value: 7  

#### public static final int
**LEFT_EYEBROW_BOTTOM**

The bottom outline of the subject's left eyebrow.  
Constant Value: 4  

#### public static final int
**LEFT_EYEBROW_TOP**

The top outline of the subject's left eyebrow.  
Constant Value: 3  

#### public static final int
**LOWER_LIP_BOTTOM**

The bottom outline of the subject's lower lip.  
Constant Value: 12  

#### public static final int
**LOWER_LIP_TOP**

The top outline of the subject's lower lip.  
Constant Value: 11  

#### public static final int
**NOSE_BOTTOM**

The outline of the subject's nose bridge.  
Constant Value: 14  

#### public static final int
**NOSE_BRIDGE**

The outline of the subject's nose bridge.  
Constant Value: 13  

#### public static final int
**RIGHT_EYE**

The outline of the subject's right eye cavity.  
Constant Value: 8  

#### public static final int
**RIGHT_EYEBROW_BOTTOM**

The bottom outline of the subject's right eyebrow.  
Constant Value: 6  

#### public static final int
**RIGHT_EYEBROW_TOP**

The top outline of the subject's right eyebrow.  
Constant Value: 5  

#### public static final int
**UPPER_LIP_BOTTOM**

The bottom outline of the subject's upper lip.  
Constant Value: 10  

#### public static final int
**UPPER_LIP_TOP**

The top outline of the subject's upper lip.  
Constant Value: 9

## Public Methods

#### public int **getFaceContourType** ()

Gets the [FirebaseVisionFaceContour.ContourType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceContour.ContourType) type.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint)\>
**getPoints** ()

Gets a list of 2D points for this face contour, where (0, 0) is the upper-left
corner of the image. The point is guaranteed to be within the bounds of the image.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()