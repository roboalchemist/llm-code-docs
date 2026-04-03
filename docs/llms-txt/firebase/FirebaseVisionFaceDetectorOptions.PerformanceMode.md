# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.PerformanceMode.md.txt

# FirebaseVisionFaceDetectorOptions.PerformanceMode

public static abstract @interface **FirebaseVisionFaceDetectorOptions.PerformanceMode** implements [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)  
Extended option for controlling additional accuracy / speed trade-offs in performing face
detection. In general, choosing the more accurate mode will generally result in longer
runtime, whereas choosing the faster mode will generally result in detecting fewer faces.  

### Inherited Method Summary

From interface java.lang.annotation.Annotation  

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| abstract [Class](https://developer.android.com/reference/java/lang/Class.html)\<? extends [Annotation](https://developer.android.com/reference/java/lang/annotation/Annotation.html)\> | annotationType()                                                                     |
| abstract boolean                                                                                                                                                                       | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| abstract int                                                                                                                                                                           | hashCode()                                                                           |
| abstract [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                       | toString()                                                                           |