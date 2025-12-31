# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector.md.txt

# FirebaseVisionFaceDetector

public class **FirebaseVisionFaceDetector** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html) [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Detector for finding [FirebaseVisionFace](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace)s
in a supplied image.

A face detector is created via [getVisionFaceDetector(FirebaseVisionFaceDetectorOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionFaceDetector(com.google.firebase.ml.vision.face.FirebaseVisionFaceDetectorOptions)) or [getVisionFaceDetector()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionFaceDetector()), if you wish to use the default options. For example, the
code below creates a face detector with default options.  

     FirebaseVisionFaceDetector faceDetector =
        FirebaseVision.getInstance().getVisionFaceDetector();
     
To perform face detection in an image, you first need to create an instance of [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html).  

          FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect faces in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<List<FirebaseVisionFace>> task = faceDetector.detectInImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                    | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector#close())() Closes this [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) and releases its model resources.                                                                 |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionFace](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace)\>\> | [detectInImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector#detectInImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects human faces from the supplied image. |

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

Closes this [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) and releases its model resources.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionFace](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace)\>\>
**detectInImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects human faces from the supplied image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object using one of the following ways:

- [fromMediaImage(Image, int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int)) with a [YUV_420_888](https://developer.android.com/reference/android/graphics/ImageFormat.html#YUV_420_888) formatted image from [android.hardware.camera2](https://firebase.google.com/docs/reference/android/reference/android/hardware/camera2/package-summary).
- [fromByteArray(byte[], FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteArray(byte[], com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) with a [NV21](https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21) formatted image from [Camera](https://developer.android.com/reference/android/hardware/Camera.html) (deprecated).
- [fromByteBuffer(ByteBuffer, FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) if you need to pre-process the image. E.g. allocate a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) and write processed pixels into the [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).

All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly slower.

Note that the width of the provided image cannot be less than 32 if [ALL_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_CONTOURS) is specified.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [List](https://developer.android.com/reference/java/util/List.html) of detected [FirebaseVisionFace](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFace)s.