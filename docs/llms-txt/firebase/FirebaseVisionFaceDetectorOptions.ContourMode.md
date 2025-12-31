# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.ContourMode.md.txt

# FirebaseVisionFaceDetectorOptions.ContourMode

public static abstract @interface **FirebaseVisionFaceDetectorOptions.ContourMode** implements [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)  
Sets whether to detect contours or not. Processing time increases as the number of
contours to search for increases, so detecting all contours will increase the overall
detection time.  

### Inherited Method Summary

From interface java.lang.annotation.Annotation  

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| abstract [Class](https://developer.android.com/reference/java/lang/Class.html)\<? extends [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)\> | annotationType()                                                                     |
| abstract boolean                                                                                                                                                                       | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| abstract int                                                                                                                                                                           | hashCode()                                                                           |
| abstract [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                       | toString()                                                                           |