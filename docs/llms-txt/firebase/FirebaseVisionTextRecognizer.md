# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer.md.txt

# FirebaseVisionTextRecognizer

public class **FirebaseVisionTextRecognizer** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
Text recognizer for performing optical character recognition(OCR) on an input image.

A text recognizer is created via [getOnDeviceTextRecognizer()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceTextRecognizer()) or [getCloudTextRecognizer()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudTextRecognizer()). See the code example below.

To use on-device text recognizer:  

     FirebaseVisionTextRecognizer textRecognizer =
        FirebaseVision.getInstance().getOnDeviceTextRecognizer();
     
Or use cloud text recognizer:  

     FirebaseVisionTextRecognizer textRecognizer =
        FirebaseVision.getInstance().getCloudTextRecognizer();
     
To perform OCR on an image, you first need to create an instance of [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html).  

    FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect texts in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<FirebaseVisionText> task = textRecognizer.processImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Nested Class Summary

|------------|---|---|-------------------|
| @interface | [FirebaseVisionTextRecognizer.RecognizerType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer.RecognizerType) || Recognizer types. |

### Constant Summary

|-----|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| int | [CLOUD](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer#CLOUD)         | Indicates that the recognizer is using a cloud model.      |
| int | [ON_DEVICE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer#ON_DEVICE) | Indicates that the recognizer is using an on-device model. |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                             | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer#close())() Closes the text detector and release its model resources.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| int                                                                                                                                                                                                                              | [getRecognizerType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer#getRecognizerType())() Gets recognizer type in terms of on-device or cloud.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)\> | [processImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer#processImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects [FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText) from a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage). |

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

## Constants

#### public static final int
**CLOUD**

Indicates that the recognizer is using a cloud model.  
Constant Value: 2  

#### public static final int
**ON_DEVICE**

Indicates that the recognizer is using an on-device model.  
Constant Value: 1

## Public Methods

#### public void **close** ()

Closes the text detector and release its model resources.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public int **getRecognizerType** ()

Gets recognizer type in terms of on-device or cloud.  

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)\>
**processImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects [FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText)
from a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage). The OCR is performed asynchronously. Right now, only
the following input types are supported:

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object using one of the following ways:

- [fromMediaImage(Image, int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int)) with a [YUV_420_888](https://developer.android.com/reference/android/graphics/ImageFormat.html#YUV_420_888) formatted image from [android.hardware.camera2](https://firebase.google.com/docs/reference/android/reference/android/hardware/camera2/package-summary).
- [fromByteArray(byte[], FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteArray(byte[], com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) with a [NV21](https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21) formatted image from [Camera](https://developer.android.com/reference/android/hardware/Camera.html) (deprecated).
- [fromByteBuffer(ByteBuffer, FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) if you need to pre-process the image. E.g. allocate a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) and write processed pixels into the [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).

All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly slower.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for [FirebaseVisionText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionText).