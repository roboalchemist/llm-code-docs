# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector.md.txt

# FirebaseVisionObjectDetector

public class **FirebaseVisionObjectDetector** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html) [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Detector for finding [FirebaseVisionObject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject)s
in a supplied image.

A object detector is created via [getOnDeviceObjectDetector(FirebaseVisionObjectDetectorOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceObjectDetector(com.google.firebase.ml.vision.objects.FirebaseVisionObjectDetectorOptions)) or [getOnDeviceObjectDetector()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceObjectDetector()), if you wish to use the default options. For example,
the code below creates an object detector with default options.  

     FirebaseVisionObjectDetector objectDetector =
        FirebaseVision.getInstance().getOnDeviceObjectDetector();
     
To perform object detection in an image, you first need to create an instance of `
`[FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).  

     FirebaseVisionImage image
        = FirebaseVisionImage.fromByteBuffer(byteBuffer, imageMetadata);
     
Then the code below can detect objects in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<List<FirebaseVisionObject>> task = objectDetector.processImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                           | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector#close())()                                                                                                                                                                                                                                                    |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionObject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject)\>\> | [processImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector#processImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects objects from supplied image. |

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

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionObject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject)\>\>
**processImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects objects from supplied image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object using following way:

- [fromByteBuffer(ByteBuffer, FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) if you need to pre-process the image. E.g. allocate a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) and write processed pixels into the [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).

All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly slower.

Note that the width and height of the provided image cannot be less than 32.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [List](https://developer.android.com/reference/java/util/List.html) of detected [FirebaseVisionObject](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObject)s.