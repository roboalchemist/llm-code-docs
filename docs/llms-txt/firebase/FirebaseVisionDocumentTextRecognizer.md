# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer.md.txt

# FirebaseVisionDocumentTextRecognizer

public class **FirebaseVisionDocumentTextRecognizer** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
Detector for performing optical character recognition(OCR) on an input image by sending
the image to Google cloud ML backend. In comparison to [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer), it detects dense document text.

A cloud document text detector is created via [getCloudDocumentTextRecognizer(FirebaseVisionCloudDocumentRecognizerOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudDocumentTextRecognizer(com.google.firebase.ml.vision.document.FirebaseVisionCloudDocumentRecognizerOptions)) or
[getCloudDocumentTextRecognizer()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudDocumentTextRecognizer()) if you wish to use the default [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions). For example, the code below creates
a cloud document text detector with default options.  


     FirebaseVisionDocumentTextRecognizer cloudDocumentTextDetector =
        FirebaseVision.getInstance().getCloudDocumentTextRecognizer();
     
To perform document text detection in an image, you first need to create an instance of [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html).  

          FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(bitmap);

Then the code below can detect texts in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<FirebaseVisionDocumentText> task = cloudDocumentTextDetector.processImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                 | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer#close())()                                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionDocumentText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)\> | [processImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer#processImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects text from supplied document image. |

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

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[FirebaseVisionDocumentText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText)\>
**processImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects text from supplied document image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object using one of the following ways:

- [fromMediaImage(Image, int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int)) with a [JPEG](https://developer.android.com/reference/android/graphics/ImageFormat.html#JPEG) formatted image from [android.hardware.camera2](https://firebase.google.com/docs/reference/android/reference/android/hardware/camera2/package-summary).
- [fromBitmap(android.graphics.Bitmap)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromBitmap(android.graphics.Bitmap)).

All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly slower.  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns the detected [FirebaseVisionDocumentText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText).