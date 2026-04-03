# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint.md.txt

# FirebaseVisionPoint

public final class **FirebaseVisionPoint** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Represent a 2D or 3D point for [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

### Public Method Summary

|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                 | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) o) |
| [Float](https://developer.android.com/reference/java/lang/Float.html)   | [getX](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#getX())() Gets x coordinate.                                                                           |
| [Float](https://developer.android.com/reference/java/lang/Float.html)   | [getY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#getY())() Gets y coordinate.                                                                           |
| [Float](https://developer.android.com/reference/java/lang/Float.html)   | [getZ](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#getZ())() Gets z coordinate (or depth).                                                                |
| int                                                                     | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#hashCode())()                                                                                      |
| [String](https://developer.android.com/reference/java/lang/String.html) | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionPoint#toString())()                                                                                      |

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

## Public Methods

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) o)

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getX** ()

Gets x coordinate.  

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getY** ()

Gets y coordinate.  

#### public [Float](https://developer.android.com/reference/java/lang/Float.html) **getZ** ()

Gets z coordinate (or depth). Z is null if it is a 2D point.  

#### public int **hashCode** ()

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()