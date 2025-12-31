# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector.md.txt

# FirebaseVisionLabelDetector

public class **FirebaseVisionLabelDetector** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html) [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
Detector for finding [FirebaseVisionLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabel)s
in a supplied image.

A label detector is created via [getVisionLabelDetector(FirebaseVisionLabelDetectorOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionLabelDetector(com.google.firebase.ml.vision.label.FirebaseVisionLabelDetectorOptions)), or [getVisionLabelDetector()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionLabelDetector()) if you wish to use the default options. For example, the
code below creates a label detector with default options.  

     FirebaseVisionLabelDetector labelDetector =
        FirebaseVision.getInstance().getVisionLabelDetector();
     
To perform label detection in an image, you first need to create an instance of [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html).  

          FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect labels in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<List<FirebaseVisionLabel>> task = labelDetector.detectInImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                       | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector#close())() Closes the [FirebaseVisionLabelDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector) and releases its model resources.                                                            |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabel)\>\> | [detectInImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector#detectInImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects image labels from supplied image. |

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

From interface java.io.Closeable  

|---------------|---------|
| abstract void | close() |

From interface java.lang.AutoCloseable  

|---------------|---------|
| abstract void | close() |

## Public Methods

#### public void **close** ()

Closes the [FirebaseVisionLabelDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabelDetector) and releases its model resources.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabel)\>\>
**detectInImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects image labels from supplied image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object from [fromBitmap(android.graphics.Bitmap)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromBitmap(android.graphics.Bitmap)). All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly
slower.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [List](https://developer.android.com/reference/java/util/List.html) of detected [FirebaseVisionLabel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionLabel)s.