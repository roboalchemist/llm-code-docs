# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject.md.txt

# FirebaseVisionObject

public class **FirebaseVisionObject** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represents a detected object by [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector).  

### Nested Class Summary

|------------|---|---|----------------------------------------------|
| @interface | [FirebaseVisionObject.Category](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject.Category) || Classification category of detected objects. |

### Constant Summary

|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| int | [CATEGORY_FASHION_GOOD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_FASHION_GOOD) |   |
| int | [CATEGORY_FOOD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_FOOD)                 |   |
| int | [CATEGORY_HOME_GOOD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_HOME_GOOD)       |   |
| int | [CATEGORY_PLACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_PLACE)               |   |
| int | [CATEGORY_PLANT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_PLANT)               |   |
| int | [CATEGORY_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_UNKNOWN)           |   |

### Public Method Summary

|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#getBoundingBox())() Gets the axis-aligned bounding rectangle of the detected object.                                                                                                                                      |
| int                                                                        | [getClassificationCategory](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#getClassificationCategory())() Gets the [FirebaseVisionObject.Category](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject.Category) of the object. |
| [Float](https://developer.android.com/reference/java/lang/Float.html)      | [getClassificationConfidence](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#getClassificationConfidence())() Gets the confidence of the on-device object classification.                                                                                                                 |
| [Integer](https://developer.android.com/reference/java/lang/Integer.html)  | [getTrackingId](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#getTrackingId())() Gets the tracking ID of the object.                                                                                                                                                                     |

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
**CATEGORY_FASHION_GOOD**

Constant Value: 2  

#### public static final int
**CATEGORY_FOOD**

Constant Value: 3  

#### public static final int
**CATEGORY_HOME_GOOD**

Constant Value: 1  

#### public static final int
**CATEGORY_PLACE**

Constant Value: 4  

#### public static final int
**CATEGORY_PLANT**

Constant Value: 5  

#### public static final int
**CATEGORY_UNKNOWN**

Constant Value: 0

## Public Methods

#### public [Rect](https://developer.android.com/reference/android/graphics/Rect.html) **getBoundingBox** ()

Gets the axis-aligned bounding rectangle of the detected object.  

#### public int **getClassificationCategory** ()

Gets the [FirebaseVisionObject.Category](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject.Category) of the object. If on-device classification is
disabled, it returns [CATEGORY_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_UNKNOWN).  

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getClassificationConfidence** ()

Gets the confidence of the on-device object classification. To be valid, the
confidence must be in the range \[0.0, 1.0\]. If the confidence is [CATEGORY_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject#CATEGORY_UNKNOWN), the call will return `null`.  

#### public [Integer](https://developer.android.com/reference/java/lang/Integer.html) **getTrackingId** ()

Gets the tracking ID of the object. The ID is a non-negative number in
[STREAM_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#STREAM_MODE) and `null` in [SINGLE_IMAGE_MODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions#SINGLE_IMAGE_MODE).