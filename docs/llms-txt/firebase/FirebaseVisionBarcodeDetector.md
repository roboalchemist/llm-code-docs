# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector.md.txt

# FirebaseVisionBarcodeDetector

public class **FirebaseVisionBarcodeDetector** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html) [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Recognizes barcodes (in a variety of 1D and 2D formats) in a supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).

A barcode detector is created via [getVisionBarcodeDetector(FirebaseVisionBarcodeDetectorOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionBarcodeDetector(com.google.firebase.ml.vision.barcode.FirebaseVisionBarcodeDetectorOptions)) or [getVisionBarcodeDetector()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionBarcodeDetector()). The default option is not recommended because it tries
to detect all barcode formats, which is slow. For example, the code below creates a barcode
detector for [FORMAT_PDF417](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_PDF417).  

     
     FirebaseVisionBarcodeDetector barcodeDetector =
          FirebaseVision.getInstance().getVisionBarcodeDetector(
              new FirebaseVisionBarcodeDetectorOptions.Builder()
                  .setBarcodeFormats(FirebaseVisionBarcode.FORMAT_PDF417)
                  .build());
     

     
To perform barcode detection in an image, you first need to create an instance of `
`[FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html), [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html), etc. See [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) documentation for more details. For example, the code below creates a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) from a [Image](https://developer.android.com/reference/android/media/Image.html).  

     FirebaseVisionImage image =
        FirebaseVisionImage.fromMediaImage(mediaImage, ImageFormat.YUV_420_888);
     
Then the code below can detect barcodes in the supplied [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage).  


     Task<List<FirebaseVisionBarcode>> task = barcodeDetector.detectInImage(image);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                                                                             | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector#close())() Closes this [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) and releases its model.                                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode)\>\> | [detectInImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector#detectInImage(com.google.firebase.ml.vision.common.FirebaseVisionImage))([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image) Detects barcodes from the supplied image. |

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

Closes this [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) and releases its model.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseVisionBarcode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode)\>\>
**detectInImage** ([FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) image)

Detects barcodes from the supplied image.

For best efficiency, create a [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) object using one of the following ways:

- [fromMediaImage(Image, int)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromMediaImage(android.media.Image, int)) with a [YUV_420_888](https://developer.android.com/reference/android/graphics/ImageFormat.html#YUV_420_888) formatted image from [android.hardware.camera2](https://firebase.google.com/docs/reference/android/reference/android/hardware/camera2/package-summary).
- [fromByteArray(byte[], FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteArray(byte[], com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) with a [NV21](https://developer.android.com/reference/android/graphics/ImageFormat.html#NV21) formatted image from [Camera](https://developer.android.com/reference/android/hardware/Camera.html) (deprecated).
- [fromByteBuffer(java.nio.ByteBuffer, FirebaseVisionImageMetadata)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage#fromByteBuffer(java.nio.ByteBuffer, com.google.firebase.ml.vision.common.FirebaseVisionImageMetadata)) if you need to pre-process the image. E.g. allocate a direct [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html) and write processed pixels into the [ByteBuffer](https://developer.android.com/reference/java/nio/ByteBuffer.html).

All other [FirebaseVisionImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionImage) factory methods will work as well, but possibly slightly slower.

To get the best detection result, we recommend the following:

- The image size is at least 1280 x 960.
- The barcode covers most of the image.
- Narrow down the barcode formats in [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions).  

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [List](https://developer.android.com/reference/java/util/List.html) of detected [FirebaseVisionBarcode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode)s. An empty list is returned by the [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) if nothing is found.