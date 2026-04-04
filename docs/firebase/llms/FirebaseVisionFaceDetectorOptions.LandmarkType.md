# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.LandmarkType.md.txt

# FirebaseVisionFaceDetectorOptions.LandmarkType

public static abstract @interface **FirebaseVisionFaceDetectorOptions.LandmarkType** implements [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)  
Sets whether to detect no landmarks or all landmarks. Processing time increases as the
number of landmarks to search for increases, so detecting all landmarks will increase the
overall detection time. Detecting landmarks can improve pose estimation.  

### Inherited Method Summary

From interface java.lang.annotation.Annotation  

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| abstract [Class](https://developer.android.com/reference/java/lang/Class.html)\<? extends [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)\> | annotationType()                                                                     |
| abstract boolean                                                                                                                                                                       | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| abstract int                                                                                                                                                                           | hashCode()                                                                           |
| abstract [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                       | toString()                                                                           |